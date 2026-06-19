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
        if sum(1 for p in sub if is_mega(p)) > 2:        # 2メガ選出許容(メガ石2枚は合法・進化は1戦1体)
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


def select_calib(party6, opp6, L, head, n=3, temperature=0.0, rng=None, opp_samples=3, det=None):
    """校正ヘッド選出：実勝率で教師あり学習した校正ヘッドでターン0選出を採点。
    本体ネットの価値ヘッド(チーム強さと反相関)でなく、シナジー組成データで校正したヘッドを使う。
    相手は学習時と同様beliefから決定化してencode(det=SearchAI)。"""
    import copy
    from itertools import combinations
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    from simulator.ai import select_party
    rng = rng or random.Random()
    k = min(n, len(party6))
    if len(party6) <= k:
        return list(party6)
    def is_mega(p): return getattr(p, "mega_data", None) is not None
    opp_sels = [select_party(opp6, party6, L, n=min(3, len(opp6)), temperature=0.0, rng=rng)]
    for _ in range(max(0, opp_samples - 1)):
        opp_sels.append(select_party(opp6, party6, L, n=min(3, len(opp6)), temperature=1.0, rng=rng))
    det_opps = []
    for os_ in opp_sels:
        s2 = BattleSide([copy.deepcopy(p) for p in os_])
        if det is not None:
            bel = OpponentBelief(L)
            cfg = det._sample_opp_config(s2, bel)
            for poke, c in zip(s2.party, cfg):
                if c is not None: det._determinize(poke, c)
        det_opps.append(s2.party)
    def vf(team_self):
        feats = []
        for od in det_opps:
            s1 = BattleSide(list(team_self)); s2 = BattleSide(list(od))
            s1.field_idx = 0; s2.field_idx = 1
            feats.append(encode_state(s1, s2, BattleField()))
        return float(sum(head.predict([f])[0] for f in feats)) / len(feats)
    scored = []
    for combo in combinations(range(len(party6)), k):
        sub = [party6[i] for i in combo]
        if sum(1 for p in sub if is_mega(p)) > 2: continue
        best_v = -1.0; best_order = None
        for li in range(len(sub)):
            order = [sub[li]] + [sub[j] for j in range(len(sub)) if j != li]
            v = vf(order)
            if v > best_v: best_v = v; best_order = order
        if best_order is not None: scored.append((best_order, best_v))
    if not scored:
        return select_party(party6, opp6, L, n=k, temperature=temperature, rng=rng)
    return max(scored, key=lambda x: x[1])[0]


def select_mcts(party6, opp6, L, ai, n=3, rng=None, opp_samples=1, topk=4, extra_orders=None, max_mega=1):
    """T2選出：候補選出をMCTSのルート価値(ΣW/ΣN=その局面の勝率推定)で評価して選ぶ。
    生のターン0価値(T1)より、実際に読みを入れた分だけ選出の良し悪しを正確に測れる。
    コスト抑制: 候補はヒューリスティックtop-k(combo)に限定し、各leadをMCTS評価。
    ai = _net_ai(mcts=True...) のMCTS探索AI(_build_mcts_root を持つ)。"""
    import random as _r
    from itertools import combinations
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    rng = rng or _r.Random()
    k = min(n, len(party6))
    if len(party6) <= k:
        return list(party6)
    def is_mega(p): return getattr(p, "mega_data", None) is not None
    def rootval(team_self, team_opp):
        s1 = BattleSide(list(team_self)); s2 = BattleSide(list(team_opp))
        s1.field_idx = 0; s2.field_idx = 1
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        root, root_my, _ = ai._build_mcts_root(s1, s2, BattleField(), None)
        meN = root["N"][0]; meW = root["W"][0]
        tot = sum(meN.values())
        return (sum(meW.values()) / tot) if tot else 0.5
    opp_sel = select_party(opp6, party6, L, n=min(3, len(opp6)), temperature=0.0, rng=rng)
    opp_alt = [opp_sel] + [select_party(opp6, party6, L, n=min(3, len(opp6)), temperature=1.0, rng=rng)
                           for _ in range(max(0, opp_samples - 1))]
    combos = [c for c in combinations(range(len(party6)), k)
              if sum(1 for i in c if is_mega(party6[i])) <= max_mega]
    rng.shuffle(combos); combos = combos[:max(1, topk)]
    orders = []
    for combo in combos:
        sub = [party6[i] for i in combo]
        orders += [[sub[li]] + [sub[j] for j in range(len(sub)) if j != li] for li in range(len(sub))]
    if extra_orders:                       # シナジー組成候補(ルールベース検出器が提案)も探索で検証
        orders = list(extra_orders) + orders
    best_order = None; best_v = -1.0
    for order in orders:
        v = sum(rootval(order, o) for o in opp_alt) / len(opp_alt)
        if v > best_v: best_v = v; best_order = order
    return best_order if best_order is not None else select_party(party6, opp6, L, n=k, rng=rng)
