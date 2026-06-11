#!/usr/bin/env python3
"""持ち物の深い監査（move deep_audit / ability_deep_audit の持ち物版）。

item_master（仕様の真実源）の effect_text から定量フィーチャ（倍率・回復割合・確率・
半減・命中補正）と状態回復を機械抽出し、その持ち物のテスト窓に検証痕跡があるか照合する。
メガストーン（category=mega）は endswith 機構の一律対応のため個別監査は対象外で、
代わりにメガシンカ機構テストの存在を1件要求する。

出力 = フィーチャはあるのに検証痕跡が無い「弱い持ち物テスト」候補。0を保つ。
"""
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "pokenavi.db"
LINES = (ROOT / "tests" / "test_all.py").read_text(encoding="utf-8").splitlines()
FULL = "\n".join(LINES)

CAP = 45  # パラグラフ拡張の上限（暴走防止）


def window_for(name: str) -> str:
    """名前が現れる各箇所について、空行で区切られた連続ブロック（パラグラフ）を窓とする。
    forループ＋末尾checkのようなグループ化テストでも、リスト要素から検証行まで届く。"""
    idxs = [i for i, ln in enumerate(LINES) if name in ln]
    keep = set()
    for i in idxs:
        a = i
        while a > 0 and LINES[a - 1].strip() and i - a < CAP:
            a -= 1
        b = i
        while b < len(LINES) - 1 and LINES[b + 1].strip() and b - i < CAP:
            b += 1
        for j in range(a, b + 1):
            keep.add(j)
    return "\n".join(LINES[j] for j in sorted(keep))


def num_tokens(win: str) -> set:
    # ラベル等の文字列リテラルを除去（値はアサーション側にある前提。ラベル中数値での偽通過を防ぐ）
    win = re.sub(r'f?"(?:[^"\\]|\\.)*"', "", win)
    win = re.sub(r"f?'(?:[^'\\]|\\.)*'", "", win)
    toks = set()
    for m in re.findall(r"\d+\.\d+", win):
        toks.add(m)
        toks.add(str(float(m)))  # 0.90→0.9 正規化
    for m in re.findall(r"//\s*(\d+)", win):
        toks.add("/" + m)
    for m in re.findall(r"(\d+)\s*/\s*(\d+)", win):
        toks.add(m[0] + "/" + m[1])
    for m in re.findall(r"\d+", win):
        toks.add(m)
    return toks


def mult_targets(eff: str):
    out = []
    for v in re.findall(r"(\d\.\d+)倍", eff):
        out.append((f"{v}倍", {v}))
    for v in re.findall(r"(?<![\d.])(\d)倍", eff):
        out.append((f"{v}倍", {v, f"{v}.0"}))
    if "半減" in eff:
        out.append(("半減(0.5)", {"0.5", "1/2", "/2"}))
    return out


def frac_targets(eff: str):
    out = []
    for m in re.finditer(r"1/(\d+)", eff):
        b = m.group(1)
        if b in ("16", "8", "4", "3"):
            out.append((f"1/{b}", {f"1/{b}", f"/{b}"}))
    return out


def prob_targets(eff: str):
    return [(f"{p}%", {p}) for p in re.findall(r"(\d+)[%％]", eff)]


STATUS_WORDS = ["どく", "もうどく", "やけど", "ねむり", "こんらん", "まひ",
                "メロメロ", "ちょうはつ", "アンコール", "わざふうじ", "状態異常"]


def audit():
    conn = sqlite3.connect(DB)
    rows = conn.execute(
        "SELECT name_jp, effect_text, category FROM item_master ORDER BY category, name_jp"
    ).fetchall()
    conn.close()

    weak = []
    mega_seen = False
    for name, eff, cat in rows:
        if cat == "mega":
            mega_seen = True
            continue
        win = window_for(name)
        toks = num_tokens(win)
        missing = []

        for desc, want in mult_targets(eff):
            if not (want & toks):
                missing.append(f"倍率 {desc}")
        for desc, want in frac_targets(eff):
            if not (want & toks):
                missing.append(f"割合 {desc}")
        for desc, want in prob_targets(eff):
            has_loop = ("for _ in range" in win) or ("random.seed" in win)
            if not has_loop:
                missing.append(f"確率 {desc}(試行ループ)")

        # 状態回復きのみ: 「(状態)を回復する」→ status/confused 検証痕跡
        if "回復する" in eff and any(s in eff for s in STATUS_WORDS) and "HP" not in eff and "PP" not in eff:
            if not re.search(r"\.status|is None|confused|taunt_count|encore_count|infatuation", win):
                missing.append("状態回復の検証")

        # 【一般】負例ゲート: 効果が対象サブセット／条件成立／トリガー限定なら、非対象・非成立の負例痕跡を要求
        subset = re.search(
            r"[ァ-ヶ]+タイプの技"          # タイプ限定の強化/半減
            r"|効果バツグン|抜群"           # 半減きのみ等の抜群条件
            r"|以下になった時|以下の時|満タン"  # HP条件
            r"|を受けると|を与えた時|0になった",  # トリガー（急所ランク+1は無条件なので除外）
            eff)
        neg = re.search(
            r"等倍|不変|非|負例|対照|のまま|半減しない|発動しない|しない\"|ひるませない"
            r"|, ?1\.0\)|==\s*1\.0|== 0|通る|消費|not _|not any", win)
        if subset and not neg:
            missing.append("負例(非対象/非成立で効果が出ないこと)未検証")

        if missing:
            weak.append((name, missing))

    # メガストーン機構テストの存在確認（カテゴリ一括）
    mega_tested = ("メガシンカ" in FULL) or ("do_mega" in FULL) or ("_is_megastone" in FULL)
    if mega_seen and not mega_tested:
        weak.append(("（メガストーン機構）", ["メガシンカ機構テストが無い"]))

    print(f"=== 持ち物 deep_audit（item_master {len(rows)}種） ===\n")
    print(f"【弱い持ち物テスト候補: {len(weak)}件】（仕様フィーチャに検証痕跡が無い）")
    for name, ms in weak:
        print(f"  {name}: {', '.join(ms)}")
    return len(weak)


if __name__ == "__main__":
    raise SystemExit(1 if audit() else 0)
