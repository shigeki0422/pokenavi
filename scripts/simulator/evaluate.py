"""学習成果の評価（Phase 5）。

主要指標:
1. 行動方策: SearchAI vs HeuristicAI の勝率（選出はヒューリスティック共通）。
2. 選出方策: ナッシュ均衡選出 vs ヒューリスティック選出の勝率（行動は HeuristicAI 共通）。
3. 統合: (Nash選出 + SearchAI) vs (Heuristic選出 + HeuristicAI) の勝率。
4. 推定器の較正: ダメージ観測で相手の耐久(防御/特防)推定誤差が事前より縮むか（真値比較）。
"""
import random
from itertools import combinations

from .simulate import get_loader
from .env import load_registered_parties, build_party, heuristic_selection
from .belief import OpponentBelief
from .battle import Battle, BattleSide
from .ai import HeuristicAI
from .search_ai import SearchAI
from .selection import selection_to_party
from .train import load_selection_table, make_nash_selection


def eval_search_vs_heuristic(loader, parties, N=30, K=16, depth=50, seed=11):
    heur = HeuristicAI()
    rng = random.Random(seed)
    sw = hw = 0
    for i in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        sc = SearchAI(loader, rollouts=K, depth=depth, seed=1000 + i)
        if i % 2 == 0:
            s1.belief = OpponentBelief(loader); w = Battle(s1, s2).run(sc, heur)
            sw += (w == 1); hw += (w == 2)
        else:
            s2.belief = OpponentBelief(loader); w = Battle(s1, s2).run(heur, sc)
            sw += (w == 2); hw += (w == 1)
    return sw, hw


def eval_nash_vs_heuristic_selection(loader, parties, cache, N=300, seed=22):
    """学習済みカード（cacheにある対戦）でNash選出 vs Heuristic選出。行動はHeuristic共通。"""
    heur = HeuristicAI()
    rng = random.Random(seed)
    ids = [p.party_id for p in parties]
    by_id = {p.party_id: p for p in parties}
    cached_pairs = [(i, j) for i, j in combinations(ids, 2) if f"{i}-{j}" in cache]
    if not cached_pairs:
        return 0, 0
    nw = hw = 0
    random.seed(seed)
    for n in range(N):
        i, j = rng.choice(cached_pairs)
        p1, p2 = by_id[i], by_id[j]
        nash_sel = make_nash_selection(cache, i, j, seed=n)
        a1 = build_party(p1, loader); a2 = build_party(p2, loader)
        sp1 = nash_sel(a1, a2, loader)            # P1 = Nash選出
        sp2 = heuristic_selection(a2, a1, loader)  # P2 = Heuristic選出
        w = Battle(BattleSide(sp1), BattleSide(sp2)).run(heur, heur)
        nw += (w == 1); hw += (w == 2)
    return nw, hw


def eval_combined(loader, parties, cache, N=20, K=16, depth=50, seed=33):
    """統合エージェント (Nash選出+SearchAI) vs (Heuristic選出+HeuristicAI)。"""
    heur = HeuristicAI()
    rng = random.Random(seed)
    ids = [p.party_id for p in parties]
    by_id = {p.party_id: p for p in parties}
    cached_pairs = [(i, j) for i, j in combinations(ids, 2) if f"{i}-{j}" in cache]
    if not cached_pairs:
        return 0, 0
    aw = bw = 0
    for n in range(N):
        i, j = rng.choice(cached_pairs)
        learned_is_s1 = (n % 2 == 0)
        p1, p2 = by_id[i], by_id[j]
        a1 = build_party(p1, loader); a2 = build_party(p2, loader)
        sc = SearchAI(loader, rollouts=K, depth=depth, seed=2000 + n)
        if learned_is_s1:
            nash = make_nash_selection(cache, i, j, seed=n)
            s1 = BattleSide(nash(a1, a2, loader)); s1.belief = OpponentBelief(loader)
            s2 = BattleSide(heuristic_selection(a2, a1, loader))
            w = Battle(s1, s2).run(sc, heur)
            aw += (w == 1); bw += (w == 2)
        else:
            nash = make_nash_selection(cache, j, i, seed=n)
            s1 = BattleSide(heuristic_selection(a1, a2, loader))
            s2 = BattleSide(nash(a2, a1, loader)); s2.belief = OpponentBelief(loader)
            w = Battle(s1, s2).run(heur, sc)
            aw += (w == 2); bw += (w == 1)
    return aw, bw


def eval_belief_calibration(loader, parties, N=40, seed=44):
    """ダメージ観測で相手の耐久推定誤差が事前→事後で縮むかを真値比較。"""
    heur = HeuristicAI()
    rng = random.Random(seed)
    prior_err = post_err = 0.0
    count = 0
    for n in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        true_by_name = {p.name: p for p in s2.party}  # side2の真の個体
        s1.belief = OpponentBelief(loader)
        Battle(s1, s2).run(heur, heur)
        for name, pb_belief in s1.belief.species.items():
            true = true_by_name.get(name)
            if true is None or not pb_belief.cands:
                continue
            for attr in ("defense", "sp_defense"):
                tv = getattr(true, attr)
                pri = sum(c["defender"].__dict__[attr] * p for c, p in zip(pb_belief.cands, pb_belief.prior))
                pos = pb_belief.expected_stat(attr)
                prior_err += abs(pri - tv)
                post_err += abs(pos - tv)
                count += 1
    if count == 0:
        return 0.0, 0.0
    return prior_err / count, post_err / count


def main():
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    cache = load_selection_table()
    print("=" * 56)
    print("AI戦略学習 評価レポート")
    print("=" * 56)

    sw, hw = eval_search_vs_heuristic(loader, parties, N=30)
    print(f"\n[1] 行動方策 SearchAI vs HeuristicAI")
    print(f"    Search {sw}勝 / Heuristic {hw}勝 → SearchAI勝率 {sw/max(1,sw+hw):.1%}")

    nw, hsw = eval_nash_vs_heuristic_selection(loader, parties, cache, N=300)
    print(f"\n[2] 選出方策 Nash選出 vs Heuristic選出（行動はHeuristic共通, 学習済み{sum(1 for k in cache)//2}カード）")
    print(f"    Nash {nw}勝 / Heuristic {hsw}勝 → Nash勝率 {nw/max(1,nw+hsw):.1%}")

    aw, bw = eval_combined(loader, parties, cache, N=20)
    print(f"\n[3] 統合 (Nash選出+SearchAI) vs (Heuristic選出+HeuristicAI)")
    print(f"    学習側 {aw}勝 / ベースライン {bw}勝 → 学習側勝率 {aw/max(1,aw+bw):.1%}")

    pe, poe = eval_belief_calibration(loader, parties, N=40)
    print(f"\n[4] 推定器の較正（相手の防御/特防 実数推定誤差）")
    print(f"    事前誤差 {pe:.1f} → 事後誤差 {poe:.1f} （{'改善' if poe < pe else '悪化'} {(pe-poe)/max(1e-9,pe):+.1%}）")
    print("=" * 56)


if __name__ == "__main__":
    main()
