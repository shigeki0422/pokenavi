import sys, random
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from train_az2 import _net_ai
from simulator.az_np import PVNetNP

L = get_loader(); net = PVNetNP.load()
def b(s): return build_from_spec(parse_pokemon_spec(s), L, season='M-2', randomize=False)

def setup():
    gab  = b("ガブリアス@オボンのみ:いじっぱり:ドラゴンテール|じしん|ステルスロック|まきびし")
    fla  = b("フラエッテ(永遠)@フラエッテナイト")
    luca = b("ルカリオ@ルカリオナイト:ようき:インファイト|コメットパンチ|ストーンエッジ|しんそく")
    dory = b("ドリュウズ:いじっぱり:じしん|アイアンヘッド|いわなだれ|つるぎのまい")
    luc2 = b("ルカリオ@ルカリオナイト")
    geko = b("ゲッコウガ@こだわりスカーフ:おくびょう:なみのり|れいとうビーム|ヘドロウェーブ|あくのはどう::へんげんじざい")
    s1 = BattleSide([gab, fla, luca], viewer_label="P1")
    s2 = BattleSide([dory, luc2, geko], viewer_label="P2")
    s1.active_idx = 0; s2.active_idx = 0
    field = BattleField(); s1.field_idx = 0; s2.field_idx = 1
    gab.hp = min(gab.hp, 112); gab.stage_sp_attack = -1
    s1.belief = OpponentBelief(L, 'M-2')
    return s1, s2, field

def aname(a):
    try:
        if getattr(a, 'type', None) == 'move' and getattr(a, 'move', None): return f"技:{a.move.name_jp}"
        if getattr(a, 'type', None) == 'switch': return f"交代:idx{getattr(a,'switch_index',getattr(a,'index','?'))}"
    except Exception: pass
    return str(a)

for d in (2, 3):
    random.seed(0)
    s1, s2, field = setup()
    ai = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=d, tree_k=4, tree_det=16)
    sc = sorted(ai.score_actions_tree(s1, s2, field), key=lambda x: -x[1])
    pick = ai(s1, s2, field)
    print(f"\n===== tree_depth={d} =====", flush=True)
    print("  選択手:", aname(pick), flush=True)
    print("  均衡値(降順):", flush=True)
    for a, v in sc[:8]:
        print(f"    {aname(a):<24} {v:.4f}", flush=True)
