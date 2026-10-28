"""記事の体裁・構成ルール違反を機械的に検出する（判断はしない。検出するだけ）。

article_gate.py / article_style_check.py が使う。
検出：
  - 苦手/得意表の理由列セルの文数・文字数（観点18e/18c）
  - **強み:** ブロック内の否定・null文（観点2）
  - 存在しない参照（「詳細は表の下」「後述」等）
許可マーカー（同一行のHTMLコメント）で個別に許可できる：
  <!-- gate:allow style reason="2つの対戦形態が絡むため3文" -->
"""
import re
from dataclasses import dataclass

MAX_CELL_SENTENCES = 2       # 記事レビュー.md 観点18e：理由列は1〜2文にまとめる
MAX_CELL_CHARS = 100         # 2026-10-18: 200→100。生成セルの中央値80・最大92に合わせた（「表の中も長い」の指摘）
# 長さ・粒度の上限（2026-10-18 ユーザー指摘「冗長にしないルールはなぜ守られないか」→ 上限が数値で無かったため）
MAX_CARD_INTRO_SENTENCES = 2   # 型カード直下の説明文
MAX_CARD_SW_SENTENCES = 2      # 強み / 弱み それぞれ
MAX_PRE_TABLE_SENTENCES = 1    # 苦手/得意の見出しから表までの本文
MAX_PARTNER_PROSE_CHARS = 300  # 同居率の表の後の本文（役割分担）
MAX_PARTNER_PARAGRAPHS = 1
# パートナーが「苦手な相手を受けるか」も「被写体の弱点タイプを受けるか」も partner_grid が表で出す（2026-10-25：
# 前者は○を◎と読み違え、後者はメガグソクムシャのみず等倍を「耐性」と書いた）。本文では受け・耐性の話をさせない
PARTNER_COVER_RE = re.compile(r"苦手|得意|分担|カバー|軽減|範囲|受け|耐性|半減|無効|弱点|補完")
NEGATION_PATTERNS = [
    r"わけではな", r"ではありません", r"とは言えません", r"結論自体は変わりません",
    # 強み欄に「ただし〜できません」で弱みを混ぜる（2026-10-25 セグレイブ型3）
    r"ただし",
]
DANGLING_REF_PATTERNS = [r"詳細は表の[下上]", r"後述", r"前述の表"]

_ALLOW = re.compile(r'<!--\s*gate:allow\s+(\S+)(?:\s+reason="([^"]*)")?\s*-->')


@dataclass
class Finding:
    line: int
    kind: str       # 観点ID
    detail: str
    key: str = "style"


def allowed(line_text: str) -> dict:
    """同一行の許可マーカーを {token: reason} で返す。token は 'style' か個別の文字列。"""
    return {m.group(1): (m.group(2) or "") for m in _ALLOW.finditer(line_text)}


def _line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def check_table_cells(text):
    findings = []
    # 生成ブロック（gate:rows）のセルも数える：「表の中も長い」（2026-10-18）を生成器に守らせるため。
    # 生成セルが超えたら書き手ではなく render_matchup_rows.py を直す（除外して見逃さない）。
    t = text
    for m in re.finditer(r'<td style="padding:8px 12px;border:1px solid #cbd5e1">([^<].*?)</td>', t):
        cell = m.group(1)
        line = _line_of(text, m.start())
        n_sentences = max(cell.count("。"), 1)
        if n_sentences > MAX_CELL_SENTENCES:
            findings.append(Finding(line, "観点18e: セル内の文数が多い",
                                    f"{n_sentences}文（目安{MAX_CELL_SENTENCES}文以内）: {cell[:50]}..."))
        if len(cell) > MAX_CELL_CHARS:
            findings.append(Finding(line, "観点18c: セルの文字数が多い",
                                    f"{len(cell)}字（目安{MAX_CELL_CHARS}字以内）: {cell[:50]}..."))
    return findings


def check_strength_weakness_negation(text):
    findings = []
    for m in re.finditer(r"\*\*強み:\*\*\n\n(.*?)(?=\n\n\*\*弱み:\*\*|\n---|\n##)", text, re.S):
        block = m.group(1)
        base_line = _line_of(text, m.start(1))
        for pat in NEGATION_PATTERNS:
            for nm in re.finditer(pat, block):
                line = base_line + block.count("\n", 0, nm.start())
                findings.append(Finding(line, "観点2: 強み欄に否定・null文の疑い",
                                        f"'{pat}' を含む: ...{block[max(0, nm.start()-25):nm.start()+15]}..."))
    return findings


def check_dangling_refs(text):
    findings = []
    for pat in DANGLING_REF_PATTERNS:
        for m in re.finditer(pat, text):
            findings.append(Finding(_line_of(text, m.start()), "存在しない参照の疑い",
                                    f"'{m.group(0)}' — 参照先が本当に存在するか確認"))
    return findings


def strip_blocks(text):
    """gate:rows ブロックの中身を（行番号を保って）空白化する。長さの検査はLLMが書いた本文だけを対象にするため。"""
    return re.sub(r"(<!-- gate:rows start id=[^\s]+ facts=[0-9a-f]+ -->)(.*?)(<!-- gate:rows end id=[^\s]+ -->)",
                  lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)) + m.group(3), text, flags=re.S)


def _sentences(s):
    s = re.sub(r"<[^>]+>", "", s)
    return max(s.count("。"), 1 if s.strip() else 0)


def check_card_prose(text):
    """型カード：説明文・強み・弱みの文数。"""
    findings = []
    t = strip_blocks(text)
    for m in re.finditer(r"(### 型\d[^\n]*)\n(.*?)(?=\n### 型\d|\n## )", t, re.S):
        head, body = m.group(1), m.group(2)
        base = _line_of(t, m.start(2))
        # 説明文 = カードの外枠 </div> の後から **強み:** まで
        card_end = body.rfind("</div>", 0, body.find("**強み:**")) if "**強み:**" in body else -1
        if card_end != -1:
            intro = body[card_end + 6:body.find("**強み:**")]
            n = _sentences(intro)
            if n > MAX_CARD_INTRO_SENTENCES:
                findings.append(Finding(base + body.count("\n", 0, card_end + 6) + 1, "観点19: 型カードの説明文が長い",
                                        f"{n}文（上限{MAX_CARD_INTRO_SENTENCES}文。型の役割を1〜2文で）: {head}"))
        for label in ("強み", "弱み"):
            mm = re.search(rf"\*\*{label}:\*\*\n\n(.*?)(?=\n\n\*\*|\n---|\n##|\Z)", body, re.S)
            if mm:
                n = _sentences(mm.group(1))
                if n > MAX_CARD_SW_SENTENCES:
                    findings.append(Finding(base + body.count("\n", 0, mm.start(1)), f"観点19: 型カードの{label}が長い",
                                            f"{n}文（上限{MAX_CARD_SW_SENTENCES}文。型としての傾向だけを書く）: {head}"))
    return findings


def check_pre_table(text):
    """苦手/得意の見出しから表までの本文は1文（掲載基準）まで。"""
    findings = []
    t = strip_blocks(text)
    for m in re.finditer(r"## (苦手なポケモン|得意なポケモン)[^\n]*\n(.*?)<table", t, re.S):
        n = _sentences(m.group(2))
        if n > MAX_PRE_TABLE_SENTENCES:
            findings.append(Finding(_line_of(t, m.start(2)) + 1, "観点19: 表の前の本文が長い",
                                    f"{n}文（上限{MAX_PRE_TABLE_SENTENCES}文。表の中で完結させる）: {m.group(1)}"))
    return findings


def check_partner_prose(text):
    """同居率セクション：表（partner-grid と生成表）の後の本文は1段落・300字まで。"""
    findings = []
    t = strip_blocks(text)
    m = re.search(r"## 同居率[^\n]*\n(.*?)(?=\n## |\Z)", t, re.S)
    if not m:
        return findings
    sec = m.group(1)
    i = sec.find('<div class="partner-grid">')
    if i == -1:
        return findings
    j = sec.find("</div>\n", sec.rfind("</div>", i, len(sec)))  # 最後の </div> 以降が本文
    k = sec.rfind("</div>")
    prose = sec[k + 6:] if k != -1 else sec
    prose = re.sub(r"<!-- gate:rows[^\n]*-->", "", prose)
    prose = prose.replace("---", "").strip()
    paras = [p for p in re.split(r"\n\s*\n", prose) if p.strip()]
    chars = len(re.sub(r"\s", "", prose))
    # パートナーが苦手な相手を受けられるかは partner_grid（◎/○と数の行）が表の中で完結させる。本文で言い直すと
    # ○を◎と読む誤りが2記事連続で出た（2026-10-25 ガブリアス・カバルドン）ので、受け・カバーの語を本文に書かせない
    for cm in PARTNER_COVER_RE.finditer(prose):
        pos = t.find(prose[cm.start():cm.start() + 20], m.start(1) + k)
        findings.append(Finding(_line_of(t, pos if pos != -1 else m.start(1) + k), "観点19: 同居率の本文がパートナー表の言い直し",
                                f"'{cm.group(0)}' — 誰が苦手な相手を受けられるかは表（◎/○と数の行）に任せ、本文は同居率の事実（順位・変化）だけにする"))
    if len(paras) > MAX_PARTNER_PARAGRAPHS or chars > MAX_PARTNER_PROSE_CHARS:
        findings.append(Finding(_line_of(t, m.start(1) + k + 6) + 1, "観点19: 同居率の本文が長い",
                                f"{len(paras)}段落・{chars}字（上限{MAX_PARTNER_PARAGRAPHS}段落・{MAX_PARTNER_PROSE_CHARS}字。役割分担だけを書く）"))
    return findings


def check_partner_cover_elsewhere(text):
    """同居率の節の外（まとめ等）で、同居パートナーの受け・耐性を言い直す文（2026-10-25 カバルドンのまとめ）。"""
    findings = []
    t = strip_blocks(text)
    sec = re.search(r"## 同居率[^\n]*\n.*?(?=\n## |\Z)", t, re.S)
    for i, line in enumerate(t.split("\n"), 1):
        if sec and t.count("\n", 0, sec.start()) < i <= t.count("\n", 0, sec.end()) + 1:
            continue
        if line.lstrip().startswith(("<", "|", "#")):
            continue
        for s in re.split(r"(?<=。)", line):
            if re.search(r"同居|パートナー", s) and PARTNER_COVER_RE.search(s):
                findings.append(Finding(i, "観点19: パートナーの受け・耐性の言い直し",
                                        f"'{s[:40]}…' — パートナーが何を受けられるかは同居率の表（partner_grid）だけに書く"))
    return findings


def check_notation(text):
    """表記ゆれ（article_normalize.REPLACE）。揃えるのは scripts/article_normalize.py の仕事なので、残っていれば FAIL。"""
    import article_normalize as AN
    t = strip_blocks(text)
    return [Finding(_line_of(t, m.start()), "表記ゆれ", f"'{a}' → '{b}'（python3 scripts/article_normalize.py <記事> で揃える）")
            for a, b in AN.REPLACE for m in re.finditer(re.escape(a), t)]


SUMMARY_COPY_MIN = 0.85   # まとめの文と型カードの文の文字bigram重なり（短い方基準）。較正：写しは0.85以上、要約は0.82以下


def _bigrams(s):
    s = re.sub(r"[0-9.%（）()、。・「」：]", "", s)
    return {s[i:i + 2] for i in range(len(s) - 1)}


def _prose_sentences(seg):
    out = []
    for line in seg.split("\n"):
        if line.lstrip().startswith(("<", "|", "#")) or "<td" in line:
            continue
        s = re.sub(r"<[^>]+>|\*\*", "", line).lstrip("- ")
        out += [x.strip() for x in re.split(r"(?<=。)", s) if len(x.strip()) >= 20]
    return out


def check_summary_copy(text):
    """まとめが型カードの説明文の写しになっていないか（2026-10-25 ボーマンダ・ゴリランダー・キラフロルで毎回指摘）。"""
    t = strip_blocks(text)
    m = re.search(r"\n## まとめ[^\n]*\n(.*?)(?=\n## |\Z)", t, re.S)
    if not m:
        return []
    card_s = [_bigrams(b) for b in _prose_sentences("\n".join(re.findall(r"### 型\d+：[^\n]*\n(.*?)(?=\n### |\n## )", t, re.S)))]
    findings = []
    for a in _prose_sentences(m.group(1)):
        ba = _bigrams(a)
        if any(len(ba & bb) / max(1, min(len(ba), len(bb))) >= SUMMARY_COPY_MIN for bb in card_s):
            pos = t.find(a[:15], m.start(1))
            findings.append(Finding(_line_of(t, pos if pos != -1 else m.start(1)), "観点5: まとめが型カードの写し",
                                    f"'{a[:30]}…' — まとめでは型カードの説明を繰り返さず、型の選び分けなど記事全体の結論を書く"))
    return findings


MAX_SUMMARY_SENTENCES = 0   # 2026-10-25: 手書き2文でも pt の言い直し・空疎な文が選ばれたので、まとめは summary ブロックだけにする


def check_summary_prose(text):
    """まとめの手書き部分は結論1〜2文まで（事実は summary ブロックが出す）。"""
    t = strip_blocks(text)
    m = re.search(r"\n## まとめ[^\n]*\n(.*?)(?=\n## |\Z)", t, re.S)
    if not m:
        return []
    body = re.sub(r"<!-- gate:rows[^\n]*-->", "", m.group(1))
    body = "\n".join(l for l in body.split("\n") if not l.lstrip().startswith(("<p", "<a", "<div", "</")) and "関連記事" not in l)
    n = len(_prose_sentences(body)) if body.strip() else 0
    n = max(n, body.count("。"))
    if n > MAX_SUMMARY_SENTENCES:
        return [Finding(_line_of(t, m.start(1)) + 1, "観点19: まとめの本文が長い",
                        f"{n}文（まとめは summary ブロックだけにする。手書きの文は置かない）")]
    return []


def check_card_sw_hand(text):
    """型カードの強み/弱みは card ブロック（他の型との違い）が出す。手書きの強み/弱みは置かない（2026-10-25）。"""
    t = strip_blocks(text)
    return [Finding(_line_of(t, m.start()), "観点19: 型カードの手書き強み/弱み",
                    "型カードの強み/弱みは card ブロック（他の型との違い）が出す。手書きの強み/弱みは削除する")
            for m in re.finditer(r"\*\*(強み|弱み):\*\*", t)]


def check_data_prose(text):
    """データ分析の節の手書き本文（採用率差の言い直し・根拠の無い解釈が毎回 FAIL した。2026-10-25）。表と diff_movers だけにする。"""
    t = strip_blocks(text)
    m = re.search(r"\n## データ分析[^\n]*\n(.*?)(?=\n## |\Z)", t, re.S)
    if not m:
        return []
    out = []
    in_tbl = False
    for i, line in enumerate(m.group(1).split("\n")):
        s = line.strip()
        if "<table" in s:
            in_tbl = True
        if in_tbl:
            if "</table>" in s:
                in_tbl = False
            continue
        if not s or s.startswith(("<", "|", "#", "---")) or "。" not in s:
            continue
        out.append(Finding(_line_of(t, m.start(1)) + i, "観点19: データ分析の手書き本文",
                           "データ分析は表と diff_movers ブロックだけにする（採用率差の言い直し・解釈は書かない）"))
    return out


def check_paste_comments(text):
    """render_sections.py の「<!-- 貼る位置: … -->」案内が記事に残っていないか（2026-10-25 グソクムシャで4件残り、
    段落数の数え違いで別の FAIL に見えていた）。"""
    return [Finding(_line_of(text, m.start()), "貼る位置コメントの残り", "render_sections.py の案内コメントは貼り付け後に消す")
            for m in re.finditer(r"<!-- 貼る位置", text)]


TAIGEN_END_RE = re.compile(r"[一-龥ァ-ヶー0-9A-Za-z%]$")


def check_taigen(text):
    """本文の文末が名詞で止まっていないか（2026-10-27 ウォッシュロトム差分レビューの残 FAIL J11「使用率28位（M-6: 27位）。」）。
    文末の括弧書き・閉じかぎは外してから見る。表・見出し・画像・生成ブロックは対象外。"""
    t = strip_blocks(text)
    start = t.find("\n---\n", 4) + 5 if t.startswith("---") else 0
    out = []
    for m in re.finditer(r"[^\n]+", t[start:]):
        line = m.group(0)
        if line.lstrip().startswith(("<", "|", "#", "!", "[", ">", "import ")) or "<td" in line:
            continue
        for x in re.split(r"(?<=。)", re.sub(r"<[^>]+>|\*\*", "", line)):
            x = x.strip()
            if not x.endswith("。"):
                continue
            core = x[:-1]
            while True:
                n = re.sub(r"（[^（）]*）$|\([^()]*\)$|[」』]$", "", core)
                if n == core:
                    break
                core = n
            if core and TAIGEN_END_RE.search(core):
                out.append(Finding(_line_of(t, start + m.start()), "体言止め", f"「…{x[-25:]}」の文末に述語（です・ます）を付ける"))
    return out


STAT_TOKEN_RE = re.compile(r"(?<![-A-Za-z0-9])(?:HP|こうげき|ぼうぎょ|とくこう|とくぼう|すばやさ|[HABCDS])\d{2,3}(?![\d%.\-]|から|→)")


def check_repeat_stat(text):
    """同じ段落で同じ能力値（すばやさ109・S177 など）を2回書いていないか（2026-10-27 アローラキュウコン差分レビューの残 FAIL J6）。
    EV表記（H32-A32）と「A197から394」の計算の起点は除く。"""
    t = strip_blocks(text)
    out, pos = [], 0
    for para in re.split(r"\n\s*\n", t):
        at = t.find(para, pos)
        pos = at + 1
        if para.lstrip().startswith(("<", "|", "#")) or "<td" in para or "<span" in para:
            continue
        toks = STAT_TOKEN_RE.findall(re.sub(r"<[^>]+>", "", para))
        dup = sorted({k for k in toks if toks.count(k) > 1})
        if dup:
            out.append(Finding(_line_of(t, at), "能力値の繰り返し", f"同じ段落で {'・'.join(dup)} を2回書いている（1回目で示した値は繰り返さない）"))
    return out


EFFECT_RESTATE_COVER = 0.55   # 文が効果文の bigram をこの割合以上含み
EFFECT_RESTATE_REST = 9       # かつ効果文以外の bigram がこれ以下（較正：言い直しだけの文は1〜9、情報を足した文は11以上）


def _bg(s):
    s = re.sub(r"[0-9.%（）()、。・「」：\s]", "", s)
    return {s[i:i + 2] for i in range(len(s) - 1)}


def card_effect_restatements(text, effects):
    """型カードの説明文（見出しから card:N ブロックまで、技の一覧行を除く）で、技の効果文を言い直しただけの文。"""
    out = []
    t = strip_blocks(text)
    for m in re.finditer(r"### 型\d+：[^\n]*\n(.*?)<!-- gate:rows start id=card", t, re.S):
        base = _line_of(t, m.start(1))
        for i, line in enumerate(m.group(1).split("\n")):
            if line.lstrip().startswith(("<", "・", "#")):
                continue
            for sent in re.split(r"(?<=。)", re.sub(r"<[^>]+>|\*\*", "", line)):
                sent = sent.strip()
                for mv, eff in effects.items():
                    if not sent or not eff or mv not in sent:
                        continue
                    E = _bg(eff)
                    if len(E) < 4:
                        continue
                    rest = sent.replace(mv, "")
                    for x in ("型です", "技です", "てから", "する", "ます", "です", "。"):
                        rest = rest.replace(x, "")
                    if len(E & _bg(sent)) / len(E) >= EFFECT_RESTATE_COVER and len(_bg(rest) - E) <= EFFECT_RESTATE_REST:
                        out.append((base + i, sent, mv))
    return out


def check_all(text):
    out = (check_table_cells(text) + check_strength_weakness_negation(text) + check_dangling_refs(text)
           + check_card_prose(text) + check_pre_table(text) + check_partner_prose(text) + check_paste_comments(text)
           + check_partner_cover_elsewhere(text) + check_notation(text) + check_summary_copy(text) + check_summary_prose(text)
           + check_card_sw_hand(text) + check_data_prose(text) + check_taigen(text)
           + check_repeat_stat(text))
    out.sort(key=lambda f: f.line)
    return out


# ---------------------------------------------------------------- causal ----
# 2026-10-18: 事実ファイルは数値だけを持ち、技・特性の「発動タイミング」「何を固定するか」のような仕組みは
# 持たない。So What を満たそうとしてLLMがそれを記憶で書き、2回連続で誤った（メガ進化のタイミング、
# タイプ変化技の確定数の向き）。仕組み語と因果接続が同じ文にあれば検出し、gate:allow causal で
# エンジン実装の行を引用しない限り通さない。
CAUSAL_RE = re.compile(
    r"ため|ことで|により|によって|ので|おかげで|せいで(?!ん)|ことから"
    r"|(?:ない|です|ます|いる|ある|れる|せる|った|える|きる|ない)から"
)
# 強い仕組み語（1つでも因果接続と同居すれば検出）。発動タイミング・効果の対象が事実ファイルに無いもの。
MECHANIC_STRONG_RE = re.compile(
    r"メガ進化|アンコール|トリック(?!ルーム|フラワー)|リベロ|へんげんじざい|優先度|先制|まひ|やけど|ねむり|こおり状態"
    r"|きあいのタスキ|ばけのかわ|がんじょう|ふゆう|マルチスケイル"
)
# 弱い仕組み語（2種類以上が同居したときだけ検出。単独では「受け出し先を用意できるため」のような通常の戦術文に多い）
MECHANIC_WEAK_RE = re.compile(r"特性|発動|交代|受け出し|後出し|居座")
# 仕組み語が「名前として」出ているだけの用法：直後が数値・採用率・括弧、または「を持つ/持たない/採用」
NAME_ONLY_RE = r"(?:\d|％|%|（|\(|・|の採用|採用率|を持|も持|は持|を採用|を覚え)"
EV_CONTEXT_RE = re.compile(r"EV|振り|配分")


def _mechanic_words(s):
    strong = [m.group(0) for m in MECHANIC_STRONG_RE.finditer(s)
              if not re.match(NAME_ONLY_RE, s[m.end():m.end() + 4])]
    weak = sorted({m.group(0) for m in MECHANIC_WEAK_RE.finditer(s)})
    if strong:
        return sorted(set(strong)) + weak
    if len(weak) >= 2:
        return weak
    return []


def check_causal(text, skip_ranges=()):
    """仕組み語＋因果接続を含む文を列挙する。skip_ranges=[(line_start,line_end)] は検証済み生成ブロック。
    較正（2026-10-18、既存5記事28件→本物17件）：強い語は1つで検出、弱い語は2種類以上、名前だけの用法
    （「がんじょう31.8%」「アンコールを持たないため」）は除外、EV配分の説明（「S振りのため」）は除外。"""
    import article_claims as AC  # noqa: WPS433（循環 import 回避のため関数内）
    findings = []
    clean = AC.strip_noise(text)
    for u in AC.split_units(text):
        if u.kind == "tr":
            continue  # 技データ表の effect_text 転記など
        for sent in AC.split_sentences(u):
            if any(a <= sent.line <= b for a, b in skip_ranges):
                continue
            s = clean[sent.pos:sent.pos + len(sent.text)]
            if "<td" in s:
                continue
            if not CAUSAL_RE.search(s):
                continue
            mech = _mechanic_words(s)
            if not mech:
                continue
            if set(mech) <= {"特性", "発動"} and EV_CONTEXT_RE.search(s):
                continue
            findings.append(Finding(sent.line, "仕組みの因果（" + "・".join(mech) + "）",
                                    s.strip()[:90], key="causal"))
    return findings
