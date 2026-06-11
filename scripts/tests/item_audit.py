#!/usr/bin/env python3
"""持ち物のテストカバレッジ監査（ability_audit の持ち物版・名前ベース）。

item_master の各持ち物について test_all.py に「狙ったテスト」（名前がラベル/リテラルで出現）
があるかを照合する。メガストーン（category=mega）は endswith 機構の一括対応のため、
個別ではなく「メガストーン機構テスト」の存在1件で全件カバー済みとみなす。

  A. 実装済み×テスト無し ＝ 盲点（最優先で0に保つ）
  B. 未実装
  C. 実装済み×テスト有
"""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "pokenavi.db"
TEST_ALL = (ROOT / "tests" / "test_all.py").read_text(encoding="utf-8")

MEGA_MECH_TESTED = "_is_megastone" in TEST_ALL or "メガシンカ" in TEST_ALL


def has_test(name: str) -> bool:
    return f'"{name}"' in TEST_ALL or f"'{name}'" in TEST_ALL


def main():
    conn = sqlite3.connect(DB)
    rows = conn.execute(
        "SELECT name_jp, category, implemented FROM item_master ORDER BY implemented DESC, name_jp"
    ).fetchall()
    conn.close()

    impl_no_test, not_impl, impl_tested = [], [], []
    for name, cat, impl in rows:
        tested = MEGA_MECH_TESTED if cat == "mega" else has_test(name)
        if impl and not tested:
            impl_no_test.append(name)
        elif impl and tested:
            impl_tested.append(name)
        if not impl:
            not_impl.append(name)

    n_mega = sum(1 for _, c, _ in rows if c == "mega")
    print(f"=== 持ち物カバレッジ監査（全{len(rows)}種・メガ{n_mega}） ===")
    print(f"実装済み: {sum(1 for _,_,i in rows if i)} / 未実装: {sum(1 for _,_,i in rows if not i)}")
    print(f"メガ機構テスト: {'有' if MEGA_MECH_TESTED else '無'}\n")
    print(f"【A. 実装済み×テスト無し（盲点・最優先）: {len(impl_no_test)}件】")
    for n in impl_no_test:
        print(f"  {n}")
    print(f"\n【C. 実装済み×テスト有: {len(impl_tested)}件】")
    print(f"\n【B. 未実装: {len(not_impl)}件】 {' '.join(not_impl)}")
    return len(impl_no_test)


if __name__ == "__main__":
    raise SystemExit(1 if main() else 0)
