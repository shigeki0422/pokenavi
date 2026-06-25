import os, collections
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ["HIDDEN_SELECTION"] = "0"
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from simulator.az_np import PVNetNP
from simulator.features import encode_state
from simulator.alphazero import legal_actions_indexed
from train_az2 import _net_ai

L = get_loader()
FLA = "フラエッテ(永遠)@フラエッテナイト:おくびょう:はめつのひかり|ムーンフォース|ドレインキッス|めいそう:0/0/10/24/0/32:フラワーベール"
MASK = "マスカーニャ@こだわりスカーフ:いじっぱり:トリックフラワー|かみなりパンチ|トリプルアクセル|とんぼがえり:4/30/20/0/0/12:へんげんじざい"
GARU = "ガブリアス@こだわりスカーフ:いじっぱり:じしん|げきりん|ほのおのキバ|アイアンヘッド:2/32/0/0/0/32:さめはだ"
STAR = "スターミー@スターミナイト:いじっぱり:アクアブレイク|アクアジェット|アイススピナー|クイックターン:2/32/0/0/0/32:しぜんかいふく"
SGARU = "ガブリアス@こだわりスカーフ:いじっぱり:じしん|げきりん|ほのおのキバ|アイアンヘッド:2/32/0/0/0/32:さめはだ"
GIL = "ギルガルド@たべのこし:いじっぱり:ポルターガイスト|かげうち|せいなるつるぎ|キングシールド:32/32/0/0/0/2:バトルスイッチ"

def mk(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
p1 = [mk(FLA), mk(MASK), mk(GARU)]
p2 = [mk(STAR), mk(SGARU), mk(GIL)]
s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
field = BattleField()
net = PVNetNP.load("az_net_np.json")
legal = legal_actions_indexed(s1, s2, field)
prior, val = net.evaluate(encode_state(s1, s2, field), [ix for _, ix in legal])
def lab(a):
    if a.type == "switch": return f"交代→{p1[a.switch_to].name}"
    if a.type == "move": return f"技 {p1[0].moves[a.move_idx].name_jp}" + ("(メガ)" if getattr(a,'do_mega',False) else "")
    return a.type
print("局面: フラエッテ(永遠) vs スターミー(メガ可) / 控え マスカーニャ・ガブリアス")
print(f"value(P1)={val:.3f}")
print("[生policy]")
for a, ix in sorted(legal, key=lambda x: -prior.get(x[1], 0)):
    print(f"   {lab(a):<24} {prior.get(ix,0):.3f}")
for sims in (400, 1200):
    cnt = collections.Counter()
    for seed in range(8):
        ai = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
        cnt[lab(ai(s1, s2, field))] += 1
    print(f"[MCTS@{sims} 8回] " + "  ".join(f"{k}:{v}" for k, v in cnt.most_common()))
