import random
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from train_az2 import _net_ai
from simulator.az_np import PVNetNP

L = get_loader(); net = PVNetNP.load()
def b(s): return build_from_spec(parse_pokemon_spec(s), L, season='M-2', randomize=False)

def aname(a):
    if getattr(a, 'type', None) == 'switch': return f"交代→idx{getattr(a,'switch_to','?')}"
    mv = getattr(a, 'move', None)
    return f"技:{mv.name_jp}" if mv else str(a)

def setup():
    gab = b("ガブリアス@オボンのみ:いじっぱり:ドラゴンテール|じしん|ステルスロック|まきびし")
    g2  = b("ゲッコウガ")  # 控え（交代先）
    elf = b("エルフーン:おくびょう:ムーンフォース|おいかぜ|やどりぎのタネ|うそなき::いたずらごころ")
    e2  = b("カバルドン")
    s1 = BattleSide([gab, g2], viewer_label="P1")
    s2 = BattleSide([elf, e2], viewer_label="P2")
    s1.active_idx = 0; s2.active_idx = 0
    field = BattleField(); s1.field_idx = 0; s2.field_idx = 1
    s2.tailwind = True; s2.tailwind_count = 3   # おいかぜ展開後
    s1.belief = OpponentBelief(L, 'M-2')
    return s1, s2, field

for mix in (1.0, 0.6, 0.4):
    random.seed(0)
    s1, s2, field = setup()
    ai = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=16)
    ai.opp_mix = mix
    sc = sorted(ai.score_actions_tree(s1, s2, field), key=lambda x: -x[1])
    pick = ai(s1, s2, field)
    print(f"\n=== opp_mix={mix} （1.0=従来の純maximin）===", flush=True)
    print("  選択:", aname(pick), flush=True)
    for a, v in sc[:6]:
        print(f"    {aname(a):<22} {v:.4f}", flush=True)
