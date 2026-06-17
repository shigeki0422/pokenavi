"""価値ネット選出（T1）：選出3体をターン0の価値ネット評価で選ぶ。
対面ダメージ計算でなく学習済み価値ネットを使うので、雨/バトン/イリュージョン/へんしん等の
ヒューリスティックで扱えないシナジー・相性も、ネットが学習した範囲で反映される。
コスト：候補(≤C(6,3)) × 自分の先発候補 × 相手選出サンプル の価値ネット前向き（ミリ秒級）。
"""
import random, math
from itertools import combinations

def select_valuenet(party6, opp6, L, net, n=3, temperature=0.0, rng=None, opp_samples=3):
    from simulator.battle import BattleSide, BattleField
    from simulator.features import encode_state
    from simulator.ai import select_party
    rng = rng or random.Random()
    k = min(n, len(party6))
    if len(party6) <= k:
        return list(party6)
    def is_mega(p): return getattr(p, "mega_data", None) is not None
    def vf(team_self, team_opp):  # P(team_self側勝利) ターン0（team_self[0]が先発）
        s1 = BattleSide(list(team_self)); s2 = BattleSide(list(team_opp))
        s1.field_idx = 0; s2.field_idx = 1
        return net.evaluate(encode_state(s1, s2, BattleField()), [0])[1]
    # 相手選出サンプル（相手の最善応答＋揺らぎ）
    opp_sels = [select_party(opp6, party6, L, n=min(3, len(opp6)), temperature=0.0, rng=rng)]
    for _ in range(max(0, opp_samples - 1)):
        opp_sels.append(select_party(opp6, party6, L, n=min(3, len(opp6)), temperature=1.0, rng=rng))
    scored = []
    for combo in combinations(range(len(party6)), k):
        sub = [party6[i] for i in combo]
        if sum(1 for p in sub if is_mega(p)) > 1:        # 2メガ選出は不可
            continue
        best_v = -1.0; best_order = None
        for li in range(len(sub)):                        # 自分の先発を選ぶ（最善）
            order = [sub[li]] + [sub[j] for j in range(len(sub)) if j != li]
            v = sum(vf(order, o) for o in opp_sels) / len(opp_sels)
            if v > best_v: best_v = v; best_order = order
        if best_order is not None: scored.append((best_order, best_v))
    if not scored:
        return select_party(party6, opp6, L, n=k, temperature=temperature, rng=rng)
    if temperature and temperature > 0:
        mx = max(s for _, s in scored)
        ws = [math.exp((s - mx) / temperature) for _, s in scored]
        tot = sum(ws); r = rng.random() * tot; acc = 0.0
        for (order, _), w in zip(scored, ws):
            acc += w
            if r <= acc: return order
    return max(scored, key=lambda x: x[1])[0]
