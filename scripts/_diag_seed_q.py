import os, collections, types
os.environ["HIDDEN_SELECTION"] = "0"
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from simulator.az_np import PVNetNP
from train_az2 import _net_ai
L = get_loader()
FLA = "フラエッテ(永遠)@フラエッテナイト:おくびょう:はめつのひかり|ムーンフォース|ドレインキッス|めいそう:0/0/10/24/0/32:フラワーベール"
MASK = "マスカーニャ@こだわりスカーフ:いじっぱり:トリックフラワー|かみなりパンチ|トリプルアクセル|とんぼがえり:4/30/20/0/0/12:へんげんじざい"
GARU = "ガブリアス@こだわりスカーフ:いじっぱり:じしん|げきりん|ほのおのキバ|アイアンヘッド:2/32/0/0/0/32:さめはだ"
STAR = "スターミー@スターミナイト:いじっぱり:アクアブレイク|アクアジェット|アイススピナー|クイックターン:2/32/0/0/0/32:しぜんかいふく"
GIL = "ギルガルド@たべのこし:いじっぱり:ポルターガイスト|かげうち|せいなるつるぎ|キングシールド:32/32/0/0/0/2:バトルスイッチ"
def mk(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
net = PVNetNP.load("az_net_np.json")

def lab(p1, a):
    if a.type == "switch": return f"交代→{p1[a.switch_to].name}"
    if a.type == "move": return p1[0].moves[a.move_idx].name_jp + ("(M)" if getattr(a,'do_mega',False) else "")
    return a.type

print("seed | Q(居座り最良/技)        | Q(マスカ) | Q(ガブ) || スターミー想定: アクア技% / 性格top / S-EV平均")
for seed in range(8):
    p1 = [mk(FLA), mk(MASK), mk(GARU)]; p2 = [mk(STAR), mk(GARU), mk(GIL)]
    s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    ai = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=400, mcts_select="regret", mcts_fast=True)
    rec = []
    orig = ai._sample_opp_config
    def wrap(self, opp_side, belief, _orig=orig, _rec=rec):
        cfg = _orig(opp_side, belief)
        if cfg and opp_side.party and opp_side.party[0].name == "スターミー" and cfg[0]:
            _rec.append(cfg[0])
        return cfg
    ai._sample_opp_config = types.MethodType(wrap, ai)
    root, root_my, _ = ai._build_mcts_root(s1, s2, BattleField(), None)
    meN = root["N"][0]; meW = root["W"][0]
    def q(a):
        ix = ai._action_index(a); n = meN.get(ix, 0)
        return (meW.get(ix, 0.0)/n if n else 0.0), n
    moves = [(lab(p1,a),)+q(a) for a in root_my if a.type=="move"]
    sw = {p1[a.switch_to].name: q(a) for a in root_my if a.type=="switch"}
    bestmv = max(moves, key=lambda x: x[1])
    # スターミー想定の集計
    naq = sum(1 for c in rec if "アクアブレイク" in c.get("moves", [])) * 100 // max(1, len(rec))
    nat = collections.Counter(c.get("nature") for c in rec).most_common(2)
    sev = sum(c.get("ev", {}).get("S", 0) for c in rec) / max(1, len(rec))
    qm, nm_ = sw.get("マスカーニャ", (0,0)); qg, ng = sw.get("ガブリアス", (0,0))
    print(f"  {seed}  | {bestmv[0]:<10} Q={bestmv[1]:.3f}(N{bestmv[2]}) | {qm:.3f}(N{nm_}) | {qg:.3f}(N{ng}) || アクア{naq}% / {nat} / S-EV{sev:.0f}  (samples{len(rec)})")
