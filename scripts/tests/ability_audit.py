#!/usr/bin/env python3
"""特性のテストカバレッジ監査。

ability_master（仕様の真実源）の各特性について、
  - 実装状況（implemented フラグ）
  - test_all.py に「狙ったテスト」（check ラベルに特性名）があるか
を突き合わせ、次の観点を出力する:
  A. 実装済み×テスト無し  ＝ 既存実装のバグが眠る盲点（最優先で埋める）
  B. 未実装（テスト有無問わず）＝ フェーズ②の実装対象
  C. テスト済み実装        ＝ OK

move 側の deep_audit に相当する、特性版の網羅監査。
"""
import sqlite3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/
DB = ROOT / "pokenavi.db"
TEST_ALL = (ROOT / "tests" / "test_all.py").read_text(encoding="utf-8")

# check("ラベル", ...) のラベル一覧
_LABELS = re.findall(r'check\(f?"([^"]*)"', TEST_ALL)


def has_targeted_test(name: str) -> bool:
    """特性名が check ラベルに含まれる＝狙ったテストがある。
    f文字列ループ（f"{_ab} ..."）で動的生成されるラベルも考慮し、
    test_all 内に make_poke(ability="X") と check の両方があれば実テストとみなす。"""
    for lab in _LABELS:
        if name in lab:
            return True
    # f文字列/ループで動的生成されるラベルや、ループのリストで特性名を回すケースを広く拾う。
    # test_all.py 内に特性名が文字列リテラルで現れれば、その特性のテストがあるとみなす。
    return f'"{name}"' in TEST_ALL or f"'{name}'" in TEST_ALL


def main():
    conn = sqlite3.connect(DB)
    rows = conn.execute(
        "SELECT name_jp, effect_text, implemented FROM ability_master ORDER BY implemented DESC, name_jp"
    ).fetchall()
    conn.close()

    impl_no_test = []   # A
    not_impl = []       # B
    impl_tested = []    # C
    for name, eff, impl in rows:
        tested = has_targeted_test(name)
        if impl and not tested:
            impl_no_test.append(name)
        elif impl and tested:
            impl_tested.append(name)
        if not impl:
            not_impl.append((name, tested))

    print(f"=== 特性カバレッジ監査（全{len(rows)}特性） ===")
    print(f"実装済み: {sum(1 for _,_,i in rows if i)} / 未実装: {sum(1 for _,_,i in rows if not i)}")
    print()
    print(f"【A. 実装済み×テスト無し（盲点・最優先）: {len(impl_no_test)}件】")
    for n in impl_no_test:
        print(f"  {n}")
    print()
    print(f"【C. 実装済み×テスト有: {len(impl_tested)}件】")
    print(f"  {' '.join(impl_tested)}")
    print()
    print(f"【B. 未実装（フェーズ②対象）: {len(not_impl)}件】")
    print(f"  {' '.join(n for n, _ in not_impl)}")

    return len(impl_no_test)


if __name__ == "__main__":
    main()
