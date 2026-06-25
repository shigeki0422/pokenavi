#!/usr/bin/env python3
"""ポケモン（姿・メガ・フォルム）データの整合監査。

DBが真実源。本スクリプトは「DB内部の整合性・網羅性」を機械照合する。
外部権威ソース（PokeAPI/gamewith）との値照合は pokemon_crosscheck.py（別）で行い、
本監査は『環境に出るのにデータが無い／使う技を覚えない／未知の特性・技を参照』等の
構造的欠落を0にすることを目的とする。

観点:
  A. 環境出現ポケモンに base_stats が無い（姿欠落）
  B. 環境出現ポケモンのメガ石が mega_stats で解決できない
  C. 使用実績のある技が learnset に無い（覚えない技を使う＝学習データ欠落 or 表記揺れ）
  D. learnset/usage の技が move_master に無い（未知の技）
  E. 使用実績のある特性が ability_master に無い（未知の特性）
  F. base_stats / mega_stats の値異常（タイプ不正・種族値0・BST異常）
"""
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from simulator.data import DataLoader
DB = ROOT / "pokenavi.db"
SEASON, RULE = "M-2", "single"

VALID_TYPES = {"ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう",
               "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト",
               "ドラゴン", "あく", "はがね", "フェアリー"}


def norm(name: str) -> str:
    """表記揺れ吸収（()と:、全角空白）。照合キー用。"""
    return (name.replace("：", ":").replace("（", "(").replace("）", ")")
            .replace(" ", "").replace("　", "").replace(":", "").replace("(", "").replace(")", ""))


def main():
    c = sqlite3.connect(DB)
    env = [r[0] for r in c.execute(
        "SELECT DISTINCT pokemon FROM pokemon_usage WHERE season=? AND rule=?", (SEASON, RULE))]
    base_names = {norm(r[0]): r[0] for r in c.execute("SELECT DISTINCT pokemon_name FROM pokemon_base_stats")}
    base_raw = set(r[0] for r in c.execute("SELECT DISTINCT pokemon_name FROM pokemon_base_stats"))
    mega_stones = set(r[0] for r in c.execute("SELECT mega_stone FROM pokemon_mega_stats"))
    env_stones = [r[0] for r in c.execute(
        "SELECT DISTINCT item FROM pokemon_items WHERE item LIKE '%ナイト%' AND season=? AND rule=?", (SEASON, RULE))]
    moves_master = set(r[0] for r in c.execute("SELECT name_jp FROM move_master"))
    ab_master = set(r[0] for r in c.execute("SELECT name_jp FROM ability_master"))

    # A. 姿欠落（実ローダーで種族値テンプレートを解決できない＝シミュレート不能）
    _dl = DataLoader(str(DB))
    A = [p for p in env if _dl.get_pokemon_template(p) is None]

    # B. メガ石未解決
    B = [s for s in env_stones if s not in mega_stones]

    # C. 使用技がlearnsetに無い（learnsetが存在するポケモンのみ対象）
    learn = {}
    for pk, mv in c.execute("SELECT pokemon_name, move_jp FROM pokemon_learnsets"):
        learn.setdefault(norm(pk), set()).add(mv)
    C = []
    for pk, mv in c.execute(
            "SELECT DISTINCT pokemon, move FROM pokemon_moves WHERE season=? AND rule=?", (SEASON, RULE)):
        nk = norm(pk)
        if nk in learn and mv not in learn[nk] and mv in moves_master:
            C.append((pk, mv))

    # D. 未知の技
    used_moves = set(r[0] for r in c.execute(
        "SELECT DISTINCT move FROM pokemon_moves WHERE season=? AND rule=?", (SEASON, RULE)))
    learn_moves = set(r[0] for r in c.execute("SELECT DISTINCT move_jp FROM pokemon_learnsets"))
    D = sorted((used_moves | learn_moves) - moves_master)

    # E. 未知の特性
    used_ab = set(r[0] for r in c.execute(
        "SELECT DISTINCT ability FROM pokemon_abilities WHERE season=? AND rule=?", (SEASON, RULE)))
    E = sorted(used_ab - ab_master)

    # F. 値異常
    F = []
    for row in c.execute("SELECT pokemon_name,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed FROM pokemon_base_stats"):
        nm, t1, t2, *st = row
        if t1 not in VALID_TYPES or (t2 and t2 not in VALID_TYPES):
            F.append(f"{nm}: 不正タイプ {t1}/{t2}")
        elif min(st) <= 0:
            F.append(f"{nm}: 種族値0あり {st}")
        elif not (180 <= sum(st) <= 800):
            F.append(f"{nm}: BST異常 {sum(st)}")
    for row in c.execute("SELECT mega_name_jp,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,ability FROM pokemon_mega_stats"):
        nm, t1, t2, *rest = row
        st, ab = rest[:6], rest[6]
        if t1 not in VALID_TYPES or (t2 and t2 not in VALID_TYPES):
            F.append(f"[mega]{nm}: 不正タイプ {t1}/{t2}")
        elif min(st) <= 0:
            F.append(f"[mega]{nm}: 種族値0あり")
        elif not ab or ab not in ab_master:
            F.append(f"[mega]{nm}: 特性 '{ab}' がmaster外")

    # G. 他種メガ石保持（pokemon_items でその種族の正規石でないナイト＝クロール誤り）
    dexmap = {norm(r[0]): r[1] for r in c.execute("SELECT pokemon_name, dex_number FROM pokemon_base_stats")}
    stone_dex = {r[0]: r[1] for r in c.execute("SELECT mega_stone, base_dex FROM pokemon_mega_stats") if r[0] and r[1] is not None}
    G = []
    for pk, it in c.execute(
            "SELECT DISTINCT pokemon, item FROM pokemon_items WHERE item LIKE '%ナイト%' AND season=? AND rule=?", (SEASON, RULE)):
        pd = dexmap.get(norm(pk))
        if it in stone_dex and pd is not None and pd != stone_dex[it]:
            G.append(f"{pk} が {it}（他種メガ石）を保持")
    c.close()

    secs = [("A. 環境出現だがbase_stats欠落", A),
            ("B. メガ石がmega_stats未解決", B),
            ("C. 使用技がlearnsetに無い", C),
            ("D. move_masterに無い技", D),
            ("E. ability_masterに無い特性", E),
            ("F. base/mega値異常", F),
            ("G. 他種メガ石保持(クロール誤り)", G)]
    total = sum(len(s) for _, s in secs)
    print(f"=== ポケモンデータ整合監査（環境{len(env)}種 / base_stats {len(base_raw)}姿 / mega {len(mega_stones)}）===\n")
    for title, items in secs:
        print(f"【{title}: {len(items)}件】")
        for it in items[:40]:
            print(f"   {it}")
        if len(items) > 40:
            print(f"   ...他 {len(items)-40} 件")
        print()
    print(f"合計: {total} 件の不整合")
    return total


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
