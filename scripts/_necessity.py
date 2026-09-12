"""必然性チェック（Part 9）: 反実仮想でパーティ各枠の採用理由を測定する安価指標群。
(A) loo_coverage: 限界脅威カバレッジ（外すとどの脅威に無対応になるか）
(B) loo_matchup: 限界対面貢献（固定パネルへの攻撃系featのleave-one-out差分）
両方≈0の枠＝冗長枠（他5体で代替済み＝そのポケモンである理由がない）

注: git未追跡のまま git clean で消失し、__pycache__ の逆アセンブルから復元した。
cond_payoff / credit_matchup / necessity_probe（分析レポート系）は未復元。
"""
import statistics
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleField
from simulator.data import get_type_effectiveness
from _threat_coverage import adj_eff
import _matchup_surrogate as M

_FIELD = BattleField()


def _build6(specs, L):
    mons = []
    for s in specs:
        p = build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
        if p.mega_data is not None:
            p.do_mega_evolve()
        mons.append(p)
    return mons


def _atk_feats(A, B, spd):
    """matchup_feats の攻撃系成分のみ（LOOで単調＝差分が固有貢献として解釈できる）。
    a_2hko + a_rev + a_faster を合成。"""
    f = M.matchup_feats(A, B, _FIELD, spd)
    a_2hko, a_rev, a_faster = f[2], f[7], f[6]
    return a_2hko + a_rev + a_faster


def _dmg_mats(A, B, field):
    return ([[M._bestdmg(a, b, field) for b in B] for a in A],
            [[M._bestdmg(b, a, field) for a in A] for b in B])
