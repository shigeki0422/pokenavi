"""選出A/B: 新select_party(守備項あり) vs 旧式(攻撃のみ)。戦闘はHeuristic共通。"""
import random
from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party
from simulator.battle import Battle, BattleSide, BattleField
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI, select_party, _order_by_lead, HAZARD_MOVES, _AVG_HP, expected_damage

def old_select(party6, opp6, loader, n=3):
    if len(party6) <= n:
        return _order_by_lead(list(party6), opp6)
    field = BattleField()
    def score(poke):
        s = sum(max((expected_damage(poke, opp, mv, field) for mv in poke.moves if mv), default=0.0) for opp in opp6)
        if any(mv and mv.name_jp in HAZARD_MOVES and mv.category=="status" for mv in poke.moves):
            s += len(opp6)*_AVG_HP*0.125*2
        return s
    idx = sorted(enumerate(party6), key=lambda x: score(x[1]), reverse=True)
    sel, seen = [], []
    for _, p in idx:
        if len(sel)>=n: break
        tp=(p.type1,p.type2)
        if seen.count(tp)>=2: continue
        sel.append(p); seen.append(tp)
    for _, p in idx:
        if len(sel)>=n: break
        if p not in sel: sel.append(p)
    return _order_by_lead(sel[:n], opp6)

if __name__ == "__main__":
    loader=get_loader(); parties=load_registered_parties(loader, complete_only=True)
    heur=HeuristicAI(); rng=random.Random(7); newin=oldwin=0; N=120
    for i in range(N):
        pa,pb=rng.sample(parties,2)
        a1=build_party(pa,loader); a2=build_party(pb,loader)
        # P1=新選出, P2=旧選出（同じ6体プールから別ロジックで3選出。手番は交互）
        if i%2==0:
            s1=BattleSide(select_party(a1,a2,loader)); s2=BattleSide(old_select(a2,a1,loader))
            w=Battle(s1,s2).run(heur,heur); newin+=(w==1); oldwin+=(w==2)
        else:
            s1=BattleSide(old_select(a1,a2,loader)); s2=BattleSide(select_party(a2,a1,loader))
            w=Battle(s1,s2).run(heur,heur); newin+=(w==2); oldwin+=(w==1)
        if (i+1)%40==0: print(f"  {i+1}/{N}: 新{newin}-旧{oldwin}", flush=True)
    print(f"\n新選出(守備あり) {newin}勝 vs 旧選出(攻撃のみ) {oldwin}勝  (N={newin+oldwin}, 新勝率{newin/max(1,newin+oldwin):.0%})")
