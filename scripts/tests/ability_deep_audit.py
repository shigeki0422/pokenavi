#!/usr/bin/env python3
"""特性の深い監査（move側 deep_audit の特性版）。

ability_audit.py は「特性名が test_all.py に出現するか」しか見ない＝弱い検証。
本スクリプトは effect_text から定量値・条件分岐・無効化などの「仕様フィーチャ」を
機械抽出し、その特性に紐づくテストコード窓の中に、それを実際に検証している痕跡
（具体値・分岐の両側・ダメージ0・状態None等）があるかを照合する。

出力 = フィーチャはあるのに検証痕跡が無い「弱い特性テスト」候補。
これを0にすることが「全特性が仕様通り実装されていることを網羅的にテスト」の定義。
"""
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from simulator.abilities import NO_SINGLE_BATTLE_EFFECT  # 1v1で効果が出ない=no-op検証のみ
DB = ROOT / "pokenavi.db"
LINES = (ROOT / "tests" / "test_all.py").read_text(encoding="utf-8").splitlines()

# 窓: 特性名が出現する行の周辺（コメント見出し→setup→checkの並びを拾う）
WIN_BEFORE, WIN_AFTER = 3, 9  # 窓を狭めて隣接ブロックの負例マーカー混入(窓汚染)を抑制

TYPES = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく",
         "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン",
         "あく", "はがね", "フェアリー"]
_TYPE_ALT = "|".join(TYPES)


def listed_types(eff: str) -> set:
    """「Xタイプ」単独・「Xタイプ・Yタイプ」・「X・Y・Zタイプ」（サフィックス共有）を全て拾う。"""
    found = set()
    for m in re.finditer(rf"((?:(?:{_TYPE_ALT})・)*(?:{_TYPE_ALT}))タイプ", eff):
        seg = m.group(1)
        for t in TYPES:
            if t in seg:
                found.add(t)
    return found


def window_for(name: str) -> str:
    idxs = [i for i, ln in enumerate(LINES) if name in ln]
    keep = set()
    for i in idxs:
        for j in range(max(0, i - WIN_BEFORE), min(len(LINES), i + WIN_AFTER + 1)):
            keep.add(j)
    return "\n".join(LINES[j] for j in sorted(keep))


def _strip_labels(win: str) -> str:
    """check()のラベル等の文字列リテラルを除去。値は必ずアサーション(コード)側にある前提にし、
    『ラベル中の数値』での偽通過（ふくがん 命中1.3倍適用 型）を防ぐ。"""
    win = re.sub(r'f?"(?:[^"\\]|\\.)*"', "", win)
    win = re.sub(r"f?'(?:[^'\\]|\\.)*'", "", win)
    return win


def num_tokens(win: str) -> set:
    """窓中に現れる数値表現を正規化して集合化（near(x, 1.5) や //4 や 1/3 等）。
    ラベル文字列は除外し、アサーション内の値のみを対象とする。"""
    win = _strip_labels(win)
    toks = set()
    for m in re.findall(r"\d+\.\d+", win):
        toks.add(m)
    for m in re.findall(r"//\s*(\d+)", win):
        toks.add("/" + m)        # max_hp // 4 → /4
    for m in re.findall(r"(\d+)\s*/\s*(\d+)", win):
        toks.add(m[0] + "/" + m[1])
    for m in re.findall(r"\d+", win):  # 語境界なし（日本語隣接の「2倍」等も拾う）
        toks.add(m)
    return toks


# 倍率語→期待トークン
def mult_targets(eff: str):
    """effect_text中の倍率仕様を (説明, 期待トークン候補) のリストで返す。
    「Nではなく」の旧値（否定された基準値）は効果ではないので除外する。"""
    eff = re.sub(r"[\d.]+倍ではなく", "", eff)  # 「1.5倍ではなく2.25倍」の旧値を除去
    out = []
    for v in re.findall(r"(\d\.\d+)倍", eff):
        out.append((f"{v}倍", {v}))
    for v in re.findall(r"(?<![\d.])(\d)倍", eff):
        out.append((f"{v}倍", {v, f"{v}.0"}))
    if "半減" in eff or "1/2にする" in eff or "半分" in eff:
        out.append(("半減(0.5)", {"0.5", "1/2", "/2"}))
    if "3/4" in eff:
        out.append(("3/4", {"0.75", "3/4"}))
    if "2倍ではなく2.25" in eff or "2.25" in eff:
        out.append(("2.25倍", {"2.25"}))
    return out


def frac_targets(eff: str):
    """回復/反動の割合（分子1の単位分数）のみ対象。HP閾値『1/3以下』は条件なので除外。"""
    out = []
    for m in re.finditer(r"1/(\d+)", eff):
        b = m.group(1)
        if eff[m.end():m.end() + 2].startswith("以下"):
            continue
        if b in ("16", "8", "4", "3"):
            out.append((f"1/{b}", {f"1/{b}", f"/{b}"}))
    return out


def prob_targets(eff: str):
    return [(f"{p}%", {p}) for p in re.findall(r"(\d+)[%％]", eff)]


def stage_targets(eff: str):
    out = []
    for n in re.findall(r"(\d)段階", eff):
        out.append((f"{n}段階", {n}))
    if "6段階目" in eff:
        out.append(("6段階目", {"6"}))
    return out


# 条件分岐（gate S相当）: 条件語があれば「両側 or 値検証」を要求
COND_WORDS = ["満タンの時", "満タンの時に", "以下になると", "以下で", "の時、", "状態の時",
              "状態異常の時", "こんらん状態の時", "急所に当たる", "急所に当たると"]
WEATHER_WORDS = ["あめ状態", "ゆき状態", "すなあらし状態", "にほんばれ", "エレキフィールド"]

# 無効化（タイプ無効）
TYPE_IMMUNE = ["技が効かず", "技が効かない", "技が効か", "効果がない", "を無視して", "を無視し"]
# 状態異常無効
STATUS_IMMUNE_WORDS = ["にならない", "状態にならない"]


def audit():
    conn = sqlite3.connect(DB)
    rows = conn.execute(
        "SELECT name_jp, effect_text FROM ability_master WHERE implemented=1 ORDER BY name_jp"
    ).fetchall()
    conn.close()

    weak = []  # (name, [未検証フィーチャ...])
    for name, eff in rows:
        if name in NO_SINGLE_BATTLE_EFFECT:
            continue  # 1v1で効果なし。no-op検証は ability_audit が担保
        win = window_for(name)
        toks = num_tokens(win)
        missing = []

        for desc, want in mult_targets(eff):
            if not (want & toks):
                missing.append(f"倍率 {desc}")
        for desc, want in frac_targets(eff):
            if not (want & toks):
                missing.append(f"割合 {desc}")
        for desc, want in stage_targets(eff):
            # 段階/優先度は stage_ / priority の実アサーションを要求（裸の数字一致は type1 等で偽成立するため不可）
            if not re.search(r"stage_|priority|優先度", win):
                missing.append(f"段階 {desc}(stage_/priority検証)")

        # 能力変化の逆転（あまのじゃく）: 上昇→下降 と 下降→上昇 の双方向を要求
        if "逆転" in eff or "上がる時には下がり" in eff:
            if not (re.search(r"==\s*-", win) and re.search(r"==\s*[1-9]", win)):
                missing.append("逆転の双方向検証")

        # タイプ無効: ダメージ0 の検証痕跡（== 0 / ==0 / is 0）
        if any(w in eff for w in ["技が効かず", "技が効かない", "音の技が効かない",
                                   "弾の技が効かない"]):
            if not re.search(r"==\s*0|0\s*,|> 0|>0", win):
                missing.append("無効(ダメージ0)検証")

        # 確率: ループ/乱数の痕跡
        for desc, want in prob_targets(eff):
            has_loop = ("for _ in range" in win) or ("random.seed" in win) or ("/200" in win) or ("/60" in win) or ("/100" in win)
            if not has_loop:
                missing.append(f"確率 {desc}(試行ループ)")

        # 【一般】負例ゲート: 効果が「対象サブセット／条件成立／トリガー」に限定されるなら、
        # 非対象・非成立で効果が出ない負例の痕跡を必須とする（個別ゲートを束ねた汎用版）。
        subset = re.search(
            r"(噛む|切る|パンチ|波動|接触|音|弾|粉|連続)の?技"
            r"|[ァ-ヶ]+タイプの技"
            r"|以下|満タン|急所|ひるむ|こんらん状態|状態異常"
            r"|(あめ|ゆき|すなあらし|にほんばれ|エレキフィールド)状態(の時|だと)"
            r"|を受けると|を使うと|倒すと|当てると|当たると|食べ", eff)
        # 交代時に必ず発動するもの（手持ちに戻ると…）は「非成立」が無いので負例不要
        switch_trigger = "手持ちに戻ると" in eff
        # NEG: 「効果が出ない」ことを明示する負例マーカー（正例にも出る stage_/==0/is None/>_ は不可）。
        neg = re.search(
            r"等倍|不変|非|負例|対照|のまま|変化なし|入替なし|変動"
            r"|治らない|上がらない|下がらない|しない|盗まない|効かない\"|通る|, ?1\.0\)|not _|not any", win)
        if subset and not switch_trigger and not neg:
            missing.append("負例(非対象/非成立で効果が出ないこと)未検証")

        # タイプ変換ゲート: 「(音/ノーマル)の技が→Xタイプになる」はサブセット限定効果。
        # 正例（変換後タイプ）＋負例（非対象の技は不変）の両方の検証痕跡を要求。
        m_conv = re.search(rf"(音|ノーマルタイプ|ノーマル)の技が({_TYPE_ALT})タイプにな[るり]", eff)
        if m_conv:
            res_type = m_conv.group(2)
            if res_type not in win:
                missing.append(f"型変換 {res_type}化(正例)未検証")
            if not re.search(r"非|不変|== \"ノーマル\"|のまま", win):
                missing.append("型変換 非対象技は不変(負例)未検証")

        # 列挙タイプ(gate V相当): 「Xタイプ・Yタイプ…」「X・Y・Zタイプ」を複数列挙したら全タイプに検証痕跡
        listed = listed_types(eff)
        if len(listed) >= 2:
            for t in sorted(listed):
                if t not in win:
                    missing.append(f"列挙タイプ {t}未検証")

        # 状態異常無効: 「(状態)にならない」→ status代入＋不変の検証痕跡（.status / apply_status）
        for st in re.findall(r"(まひ|どく|もうどく|やけど|ねむり|こおり|こんらん|メロメロ|ちょうはつ|ねむけ)[・%]?[^。]*?ならない", eff):
            if ".status" not in win and "apply_status" not in win and "confused" not in win and "is None" not in win:
                missing.append(f"状態無効 {st}にならない")
                break

        # 条件分岐(gate S相当): 条件語＋効果がある→比較ベースライン(near/ratio/対照)か両側検証の痕跡を要求
        cond_hit = [w for w in COND_WORDS if w in eff]
        if cond_hit:
            has_branch = bool(re.search(r"near\(|/ ?dmg\(|/ ?_[A-Za-z]|ratio|対照|==\s*old|stage_|priority|_miss|> _|< _|not _|負例|非", win))
            if not has_branch:
                missing.append(f"条件分岐検証({cond_hit[0]})")

        if missing:
            weak.append((name, missing))

    print(f"=== 特性 deep_audit（実装済み{len(rows)}件） ===\n")
    print(f"【弱い特性テスト候補: {len(weak)}件】（仕様フィーチャに検証痕跡が無い）")
    for name, ms in weak:
        print(f"  {name}: {', '.join(ms)}")
    return len(weak)


if __name__ == "__main__":
    raise SystemExit(1 if audit() else 0)
