"""MCTS選出（T2）：候補選出をMCTS探索のルート価値で採点して選ぶ。
ヒューリスティック選出(対面ダメージ計算)比 約+6〜9pt（シナジー構築のA/Bで再現確認、2026-06）。
探索が実際に数手読んで3体の組み合わせの良し悪しを評価するため、対面採点より良い選出を返す。
本番選出(機能1)の drop-in 経路。有効化: SELECT_MODE=mcts（既定OFF=heuristic）。
選出評価の探索数=SELECT_SIMS(既定100)、候補数=SELECT_TOPK(既定6)。
"""
import os
import random
from itertools import combinations

_AI = None


def _get_ai(loader):
    global _AI
    if _AI is not None:
        return _AI
    from .az_np import PVNetNP
    from .search_ai import SearchAI
    from .alphazero import NetGreedyAI, legal_actions_indexed
    from .features import encode_state
    net = PVNetNP.load()
    sims = int(os.environ.get("SELECT_SIMS", "100"))

    def vfn(s1, s2, f):
        return net.evaluate(encode_state(s1, s2, f), [0])[1]

    def pfn(s1, s2, f):
        legal = [ix for _, ix in legal_actions_indexed(s1, s2, f)]
        return net.evaluate(encode_state(s1, s2, f), legal)[0] if legal else {}

    ai = SearchAI(loader, value_fn=vfn, policy_fn=pfn, policy_weight=0.15, rollout_ai=NetGreedyAI(net))
    ai.mcts = True
    ai.mcts_sims = sims
    ai.c_puct = 1.5
    ai.mcts_select = "regret"

    def nefn(s1, s2, f):
        legal = [ix for _, ix in legal_actions_indexed(s1, s2, f)]
        return net.evaluate(encode_state(s1, s2, f), legal if legal else [0])

    ai.net_eval = nefn
    ai.fast_clone = True
    _AI = ai
    return ai


def mcts_select_party(party6, opp6, loader, n=3, temperature=0.0, rng=None, opp_samples=2):
    from .battle import BattleSide, BattleField
    from .belief import OpponentBelief
    from .ai import select_party
    rng = rng or random.Random()
    k = min(n, len(party6))
    if len(party6) <= k:
        return list(party6)
    ai = _get_ai(loader)
    topk = int(os.environ.get("SELECT_TOPK", "6"))
    max_mega = int(os.environ.get("MAX_MEGA", "2"))   # メガ石2枚保持は合法(進化は1戦1体)。2メガ選出は基本的に強い

    def is_mega(p):
        return getattr(p, "mega_data", None) is not None

    def rootval(team_self, team_opp):
        s1 = BattleSide(list(team_self)); s2 = BattleSide(list(team_opp))
        s1.field_idx = 0; s2.field_idx = 1
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        root, _, _ = ai._build_mcts_root(s1, s2, BattleField(), None)
        meN = root["N"][0]; meW = root["W"][0]
        tot = sum(meN.values())
        return (sum(meW.values()) / tot) if tot else 0.5

    opp_alt = [select_party(opp6, party6, loader, n=min(3, len(opp6)), temperature=0.0, rng=rng)]
    for _ in range(max(0, opp_samples - 1)):
        opp_alt.append(select_party(opp6, party6, loader, n=min(3, len(opp6)), temperature=1.0, rng=rng))
    combos = [c for c in combinations(range(len(party6)), k)
              if sum(1 for i in c if is_mega(party6[i])) <= max_mega]
    rng.shuffle(combos)
    combos = combos[:max(1, topk)]
    scored = []
    for combo in combos:
        sub = [party6[i] for i in combo]
        for li in range(len(sub)):
            order = [sub[li]] + [sub[j] for j in range(len(sub)) if j != li]
            v = sum(rootval(order, o) for o in opp_alt) / len(opp_alt)
            scored.append((order, v))
    if not scored:
        return select_party(party6, opp6, loader, n=k, temperature=temperature, rng=rng)
    if temperature and temperature > 0:
        import math
        mx = max(s for _, s in scored)
        ws = [math.exp((s - mx) / temperature) for _, s in scored]
        tot = sum(ws); r = rng.random() * tot; acc = 0.0
        for (order, _), w in zip(scored, ws):
            acc += w
            if r <= acc:
                return order
    return max(scored, key=lambda x: x[1])[0]
