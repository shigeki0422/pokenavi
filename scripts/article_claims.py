"""記事Markdownから「数値主張」を機械的に抽出する（正誤判定はしない）。

article_gate.py / article_verify_claims.py が使う。
設計：
  - strip_noise  … frontmatter(本文以外)・HTML属性(style/src/href)・HTMLコメントを、行番号を保ったまま空白化
  - split_units  … 表の行(tr)・パートナーカード・型カード・段落 に分割し、各単位にポケモン名/型名を付ける
  - split_sentences … 単位内を文に分割
  - extract_claims … 文ごとに数値主張を消費型の正規表現で抽出（EV配分→日付→順位→…→裸の数字 の順）
"""
import re
from dataclasses import dataclass, field, asdict
from typing import Optional

NATURE_WORDS = [
    "いじっぱり", "ようき", "おくびょう", "ひかえめ", "わんぱく", "しんちょう", "おだやか", "ずぶとい",
    "むじゃき", "れいせい", "なまいき", "せっかち", "さみしがり", "うっかりや", "やんちゃ", "のんき", "ゆうかん",
]
STAT_WORDS = {"HP": "H", "こうげき": "A", "ぼうぎょ": "B", "とくこう": "C", "とくぼう": "D", "すばやさ": "S"}
TYPE_WORDS = [
    "ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん",
    "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー",
]
_TYPE_ALT = "|".join(TYPE_WORDS)
# 「一致」＝STABの主張。直前/直後に隣接するタイプ名があれば拾う（例：「かくとう一致の打点」「一致フェアリー技」）。
# 「非一致」「一致しない／ではない／補正がかからない」等の否定形、「結果が一致する」等の動詞用法は対象外。
_STAB_RE = re.compile(
    rf"(?:(?P<pre>{_TYPE_ALT}))?(?<!非)一致"
    rf"(?!す|し|では|補正が.{{0,6}}(?:かかりません|かからない))"
    rf"(?:(?P<post>{_TYPE_ALT}))?"
)

ALLOW_TOKEN_RE = re.compile(
    r"M-\d+|TOP\d+|\d+/\d+|\d+〜\d+回|\d+回|\d+〜\d+位|Lv\.?50|\d+px|\d+体|\d+型|\d+段|\d+位以内|\d+文|\d+字|"
    r"pokemon-\d{4}-\d{2}|type-\d{2}-[a-z]+|\d{4}-\d{2}-\d{2}|[A-Za-z]+\d+[A-Za-z]*|"
    # 数字で始まる技名（10まんボルト・100まんボルト）。2026-10-25 裸の数字と誤検出していた
    r"\d+まん[ぁ-んァ-ヶー]+"
)
# 「Nターン」は move_duration 事実がある技の名前が同じ文に無いと解決できないので、
# ALLOW_TOKEN では無く move_duration パターンで明示的に拾う（article_gate.py 側で解決）。


@dataclass
class Unit:
    kind: str                 # tr | partner-card | build-card | description | paragraph
    line_start: int
    line_end: int
    text: str
    pokemon: Optional[str] = None
    arch: Optional[str] = None
    pos: int = 0  # raw テキスト中の絶対開始位置


@dataclass
class Sentence:
    unit: Unit
    line: int
    text: str
    pos: int = 0  # raw テキスト中の絶対位置（strip_noise は長さを保つので clean 側も同じ位置）


@dataclass
class Claim:
    line: int
    kind: str
    value: object
    raw: str
    sentence: str
    unit_kind: str
    unit_pokemon: Optional[str] = None
    unit_arch: Optional[str] = None
    extra: dict = field(default_factory=dict)
    unit_text: str = ""   # 段落/カード全体（strip_noise後）。文に無い主語（直前の文の特性名等）を引くために使う

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------- noise -----

def _blank_keep_newlines(s: str) -> str:
    return re.sub(r"[^\n]", " ", s)


def strip_noise(text: str) -> str:
    """検証対象でない部分を、行番号を保ったまま空白にする。"""
    out = text
    # frontmatter: title/description 以外の行を空白化
    m = re.match(r"---\n(.*?)\n---\n", out, re.S)
    if m:
        fm = m.group(1)
        kept = []
        for ln in fm.split("\n"):
            if re.match(r"\s*(title|description):", ln):
                kept.append(ln)
            else:
                kept.append(" " * len(ln))
        out = "---\n" + "\n".join(kept) + "\n---\n" + out[m.end():]
    # HTMLコメント（gate:allow マーカーは残す：ゲートが同じ行で読む。gate:rows のハッシュ等は空白化）
    out = re.sub(r"<!--(?!\s*gate:allow)(.*?)-->", lambda mm: "<!--" + _blank_keep_newlines(mm.group(1)) + "-->", out, flags=re.S)
    # 属性値（style/src/href/alt以外のURL系）。alt はポケモン名の解決に使うので残す
    out = re.sub(r'(style|src|href|loading)="([^"]*)"', lambda mm: mm.group(1) + '="' + " " * len(mm.group(2)) + '"', out)
    # <style>…</style> ブロック
    out = re.sub(r"<style>(.*?)</style>", lambda mm: "<style>" + _blank_keep_newlines(mm.group(1)) + "</style>", out, flags=re.S)
    return out


# ---------------------------------------------------------------- units -----

_IMG_ALT = re.compile(r'<img[^>]*alt="([^"]+)"')
_ARCH = re.compile(r'<strong style="[^"]*font-size:1\.05em[^"]*">([^<]+)</strong>')


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def split_units(text: str) -> list:
    """raw(=strip前)のテキストから単位を切り出す。戻り値は出現順の Unit リスト（行範囲は重ならない）。"""
    spans = []
    for m in re.finditer(r"<tr[^>]*>.*?</tr>", text, re.S):
        alt = _IMG_ALT.search(m.group(0))
        pk = alt.group(1) if alt and "/images/pokemon/" in m.group(0) else None
        spans.append((m.start(), m.end(), "tr", pk, None))
    for m in re.finditer(r'<div class="partner-card">.*?<div class="rate">[^<]*</div>\s*</div>', text, re.S):
        nm = re.search(r'<div class="name">([^<]+)</div>', m.group(0))
        spans.append((m.start(), m.end(), "partner-card", nm.group(1) if nm else None, None))
    for m in re.finditer(r'<div class="build-header">.*?(?=\n---\n|\n## )', text, re.S):
        am = _ARCH.search(m.group(0))
        spans.append((m.start(), m.end(), "build-card", None, am.group(1).strip() if am else None))
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if fm:
        dm = re.search(r"^description:.*$", fm.group(1), re.M)
        if dm:
            s = fm.start(1) + dm.start()
            spans.append((s, s + len(dm.group(0)), "description", None, None))
    spans.sort()
    # 重なりは先勝ち（tr は build-card と重ならない。build-card 内に tr は無い）
    units = []
    cursor = 0
    merged = []
    for s, e, kind, pk, arch in spans:
        if s < cursor:
            continue
        merged.append((s, e, kind, pk, arch))
        cursor = e
    cursor = 0
    for s, e, kind, pk, arch in merged:
        if s > cursor:
            units += _paragraph_units(text, cursor, s)
        units.append(Unit(kind, _line_of(text, s), _line_of(text, max(s, e - 1)), text[s:e], pk, arch, s))
        cursor = e
    if cursor < len(text):
        units += _paragraph_units(text, cursor, len(text))
    return units


def _paragraph_units(text: str, start: int, end: int) -> list:
    out = []
    seg = text[start:end]
    pos = 0
    for part in re.split(r"\n\s*\n", seg):
        if part.strip():
            s = start + seg.index(part, pos)
            out.append(Unit("paragraph", _line_of(text, s), _line_of(text, s + len(part) - 1), part, None, None, s))
            pos = s - start + len(part)
        else:
            pos += len(part) + 2
    return out


def split_sentences(unit: Unit) -> list:
    """単位内を文に分割。行番号は文の先頭位置から求める。"""
    out = []
    text = unit.text
    pos = 0
    for part in re.split(r"(?<=。)|<br>|\n(?=・)", text):
        if part is None or not part.strip():
            pos += len(part or "")
            continue
        s = text.index(part, pos)
        line = unit.line_start + text.count("\n", 0, s)
        out.append(Sentence(unit, line, part, unit.pos + s))
        pos = s + len(part)
    return out


# ---------------------------------------------------------------- claims ----

# (kind, regex, value-builder)
_PATTERNS = [
    ("ev_spread", re.compile(r"(?<![A-Za-z])([HABCDS])(\d{1,2})((?:-[HABCDS]\d{1,2}){1,5})(?![A-Za-z0-9])"),
     lambda m: m.group(0)),
    ("ev_single", re.compile(r"EV\s*(\d{1,2})(?!\d)"), lambda m: int(m.group(1))),
    ("date", re.compile(r"(\d{4}-\d{2}-\d{2})"), lambda m: m.group(1)),
    ("rank", re.compile(r"(?<![〜~\d])(\d+)位"), lambda m: int(m.group(1))),  # 「1〜10位」の範囲表記は順位主張にしない
    # 符号なし（「7.0pt下がり」「5.8pt増えて」）も拾う。2026-10-25 書き手が足し算した「非スカーフ勢は5.8pt増」が素通りしていた
    ("pt_diff", re.compile(r"(?<![\d.])([+-]?\d+(?:\.\d)?)pt"), lambda m: float(m.group(1))),
    ("ko", re.compile(r"(確定|乱数)(\d)発(?:（約?(\d+)%）)?"),
     lambda m: {"certain": m.group(1) == "確定", "hits": int(m.group(2)), "prob": int(m.group(3)) if m.group(3) else None}),
    ("ko_prob_roll", re.compile(r"16通り中(\d+)通り"), lambda m: int(m.group(1))),
    ("pct_range", re.compile(r"(\d+(?:\.\d)?)[〜~](\d+(?:\.\d)?)%"), lambda m: (float(m.group(1)), float(m.group(2)))),
    ("pct", re.compile(r"(\d+(?:\.\d)?)%"), lambda m: float(m.group(1))),
    ("stage", re.compile(r"(\d)段階"), lambda m: int(m.group(1))),
    ("move_duration", re.compile(r"(\d+)(?:[〜~](\d+))?ターン"),
     lambda m: {"min": int(m.group(1)), "max": int(m.group(2)) if m.group(2) else int(m.group(1))}),
    ("mult", re.compile(r"×\s*(\d+(?:\.\d+)?)|(\d+(?:\.\d+)?)倍"), lambda m: float(m.group(1) or m.group(2))),
    # 「一致打点／一致技／タイプ一致／○○一致／一致○○技」の主張。技（またはすぐ隣接するタイプ名）が、
    # 文中で言及されたポケモン（無ければ被写体）のいずれかのタイプと一致するかを article_gate.py 側で
    # types/move_power 事実と照合する。隣接するタイプ名があればそれを、無ければ文中の技名を使う。
    # 「結果が一致する」のような動詞用法・「非一致」「一致しない」等の否定形は対象外。
    # 2026-10-18: くさ技・かくとう技をゴースト/フェアリー複合の一致技と誤記する事例が繰り返し発生したため追加。
    ("stab", _STAB_RE, lambda m: {"type": m.group("pre") or m.group("post")}),
    ("stat_token", re.compile(r"(?<![A-Za-z0-9])([ABCDSH])(\d{2,3})(?![A-Za-z0-9%])"),
     lambda m: {"stat": m.group(1), "value": int(m.group(2))}),
    ("base_stat", re.compile(r"種族値\D{0,4}?(\d{2,3})(?!\d)"), lambda m: int(m.group(1))),
    ("bare_number", re.compile(r"(?<![\d.\-+])(\d{2,4})(?![\d.%])"), lambda m: int(m.group(1))),
]


def _stat_word_near(sentence: str, pos: int) -> Optional[str]:
    seg = sentence[max(0, pos - 12):pos]
    for w, letter in STAT_WORDS.items():
        if w in seg:
            return letter
    return None


# 防御側と読むのは「タイプに/には/へ/の相手/側」のように「タイプ」が付く形だけ（「いわ・どくへの耐性」は攻撃側）
_DEF_SUFFIX = re.compile(r"^タイプ(?:に|には|へ|の相手|相手|側|のポケモン)")
_ATK_SUFFIX = re.compile(r"^(?:技|打点|タイプの技|一致|の技|攻撃)")


def _type_roles_near(sentence: str, pos: int, window: int = 24) -> dict:
    """×N/N倍 の直前window文字以内のタイプ名を、攻撃側(atk)／防御側(def)に振り分けて返す。
    直後が「に／には／へ／相手／側」なら防御側（「はがねタイプには×2」）、「技／打点／一致」または無印なら攻撃側
    （「でんき技は×0.5」「こおり×4」）。見つからなければ空 dict（スカーフの1.5倍等、タイプ相性ではない×N）。
    2026-10-18: 役割を見ずに最も近いタイプ語を攻撃側と決め打ちしていたため、「みずタイプには×2」で
    みず を攻撃側と誤って type_eff を絞り、誤FAILになった。"""
    seg = sentence[max(0, pos - window):pos]
    roles = {}
    for w in TYPE_WORDS:
        for m in re.finditer(re.escape(w), seg):
            after = seg[m.end():]
            role = "def" if _DEF_SUFFIX.match(after) else "atk"
            # 同じ役割が複数あれば ×N に近い方
            if role not in roles or m.start() > roles[role][1]:
                roles[role] = (w, m.start())
    return {k: v[0] for k, v in roles.items()}


def extract_claims(text: str, units: Optional[list] = None) -> list:
    """全単位・全文から数値主張を抽出。text は raw（strip_noise はこの関数内で適用）。"""
    raw = text
    clean = strip_noise(raw)
    units = units if units is not None else split_units(raw)
    claims = []
    for u in units:
        # 単位の位置を clean 側で切り出す（行番号は raw と一致している）
        for sent in split_sentences(u):
            # 文を clean 側の同位置から取る
            s_clean = _clean_slice(clean, raw, sent)
            consumed = []
            def taken(a, b):
                return any(not (b <= x or a >= y) for x, y in consumed)
            for kind, rx, build in _PATTERNS:
                for m in rx.finditer(s_clean):
                    if taken(m.start(), m.end()):
                        continue
                    if kind == "bare_number":
                        # 許容トークン（M-7 / TOP30 / 1/8 / 画像番号 等）の一部なら除外
                        if _in_allowed_token(s_clean, m.start(), m.end()):
                            continue
                    consumed.append((m.start(), m.end()))
                    extra = {}
                    if kind == "bare_number":
                        sw = _stat_word_near(s_clean, m.start())
                        if sw:
                            extra["stat_word"] = sw
                    if kind == "mult":
                        roles = _type_roles_near(s_clean, m.start())
                        if roles.get("atk"):
                            extra["atk_type"] = roles["atk"]
                        if roles.get("def"):
                            extra["def_type"] = roles["def"]
                    claims.append(Claim(
                        line=sent.line + s_clean.count("\n", 0, m.start()),
                        kind=kind, value=build(m), raw=m.group(0),
                        sentence=sent.text.strip(), unit_kind=u.kind,
                        unit_pokemon=u.pokemon, unit_arch=u.arch, extra=extra,
                        unit_text=clean[u.pos:u.pos + len(u.text)] if len(clean) == len(raw) else u.text,
                    ))
    return claims


def _clean_slice(clean: str, raw: str, sent: Sentence) -> str:
    """raw の文と同じ文字範囲を clean 側から取る（strip_noise は長さを保つので絶対位置で切る）。"""
    if len(clean) != len(raw):
        return sent.text
    return clean[sent.pos:sent.pos + len(sent.text)]


def _in_allowed_token(s: str, a: int, b: int) -> bool:
    for m in ALLOW_TOKEN_RE.finditer(s):
        if m.start() <= a and b <= m.end():
            return True
    return False


def natures_in(sentence: str) -> list:
    return [w for w in NATURE_WORDS if w in sentence]
