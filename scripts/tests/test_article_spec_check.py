#!/usr/bin/env python3
"""article_spec_check の回帰テスト。実行: cd /Users/shigeki/work/pokenavi && python3 scripts/tests/test_article_spec_check.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import article_spec_check as ASC  # noqa: E402

PASS = FAIL = 0


def check(desc, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  ✗ FAIL: {desc}" + (f" → {detail}" if detail else ""))


class _Conn:
    def __init__(self, megas):
        self.megas = megas

    def execute(self, sql, params=()):
        class R:
            def __init__(s, rows): s.rows = rows
            def __iter__(s): return iter(s.rows)
            def fetchone(s): return s.rows[0] if s.rows else None
        return R(self.megas)


def _pool(groups):
    return {"ミミッキュ": {"rank": 5, "groups": groups}}


def _g(name, share, builds):
    return {"name": name, "share": share, "builds": [{"moves": m, "item": it, "nature": n, "ev": ev, "weight": w} for m, it, n, ev, w in builds]}


pool = _pool([
    _g("つるぎのまい", 0.8, [(["かげうち", "じゃれつく", "つるぎのまい", "シャドークロー"], "いのちのたま", "いじっぱり", [2, 32, 0, 0, 0, 32], 0.7),
                           (["かげうち", "じゃれつく", "つるぎのまい", "ウッドハンマー"], "いのちのたま", "いじっぱり", [2, 32, 0, 0, 0, 32], 0.3)]),
    _g("のろい・速攻", 0.1, [(["かげうち", "じゃれつく", "のろい", "トリックルーム"], "ゴツゴツメット", "いじっぱり", [2, 32, 0, 0, 0, 32], 0.6),
                           (["かげうち", "じゃれつく", "のろい", "ウッドハンマー"], "ゴツゴツメット", "ようき", [2, 32, 0, 0, 0, 32], 0.4)]),
    _g("のろい・耐久", 0.1, [(["かげうち", "じゃれつく", "のろい", "トリックルーム"], "ゴツゴツメット", "いじっぱり", [28, 30, 6, 0, 0, 2], 1.0)]),
])
conn = _Conn([])
card = lambda arch, pg, moves, item="いのちのたま", nature="いじっぱり", ev=(2, 32, 0, 0, 0, 32): {"arch": arch, "pool_group": pg, "moves": moves, "mpool": moves, "item": item, "nature": nature, "ev": list(ev), "ability": "ばけのかわ"}

print("[spec] 型名の技が型内で少数派なら die、候補を提示")
ps = ASC.check_spec({"subject": "ミミッキュ", "cards": [card("ウッドハンマー型", "のろい・速攻", ["かげうち", "じゃれつく", "のろい", "ウッドハンマー"])]}, pool, conn)
d = [p for p in ps if p.level == "die"]
check("die が出る", d and d[0].code == "arch_name_minority", str(ps))
check("候補に のろい が入る（型内100%かつ他カードに無い）", d and "のろい" in d[0].msg, d[0].msg if d else "")

print("[spec] 型名の技が多数派なら die 無し")
ps = ASC.check_spec({"subject": "ミミッキュ", "cards": [card("つるぎのまい型", "つるぎのまい", ["かげうち", "じゃれつく", "つるぎのまい", "シャドークロー"])]}, pool, conn)
check("die 無し", not any(p.level == "die" for p in ps), str(ps))

print("[spec] 技構成が同じでEVだけ違う2カードは warn、完全同一は die")
c1 = card("のろい・速攻型", "のろい・速攻", ["かげうち", "じゃれつく", "のろい", "トリックルーム"], item="ゴツゴツメット")
c2 = card("のろい・耐久型", "のろい・耐久", ["かげうち", "じゃれつく", "のろい", "トリックルーム"], item="ゴツゴツメット", ev=(28, 30, 6, 0, 0, 2))
ps = ASC.check_spec({"subject": "ミミッキュ", "cards": [c1, c2]}, pool, conn)
check("card_same_moves の warn", any(p.code == "card_same_moves" for p in ps), str(ps))
check("die 無し", not any(p.level == "die" for p in ps), str(ps))
ps = ASC.check_spec({"subject": "ミミッキュ", "cards": [c1, {**c1, "arch": "別名型"}]}, pool, conn)
check("完全同一は card_duplicate で die", any(p.code == "card_duplicate" and p.level == "die" for p in ps), str(ps))

print("[spec] pool_group が無い/不在")
ps = ASC.check_spec({"subject": "ミミッキュ", "cards": [card("のろい型", "存在しない", ["かげうち", "じゃれつく", "のろい", "トリックルーム"])]}, pool, conn)
check("pool_group 不在は die", any(p.code == "pool_group_missing" and p.level == "die" for p in ps), str(ps))

print("[spec] 型名トークンの包含（メガガブリアスZ と メガガブリアス）")
toks = ASC.arch_name_tokens("メガガブリアスZ型", {"メガガブリアス", "メガガブリアスZ", "じしん"})
check("長い方だけを拾う", toks == ["メガガブリアスZ"], str(toks))

print("[spec] エンジン後：mixed かつ上位20位で extra_pokemon に無い相手を提案（自動追記はしない）")
spec = {"extra_pokemon": ["カバルドン"]}
engine = {"excluded": [{"sp": "カバルドン"}, {"sp": "ブリジュラス"}, {"sp": "ドヒドイデ"}]}
ps = ASC.check_after_engine(spec, engine, lambda sp: {"カバルドン": 4, "ブリジュラス": 3, "ドヒドイデ": 40}[sp])
check("ブリジュラスだけ提案される", len(ps) == 1 and "ブリジュラス" in ps[0].msg and "ドヒドイデ" not in ps[0].msg and "カバルドン" not in ps[0].msg, str(ps))
check("spec は書き換えない", spec["extra_pokemon"] == ["カバルドン"], str(spec))

print(f"\n{PASS} passed, {FAIL} failed")
if FAIL:
    sys.exit(1)
