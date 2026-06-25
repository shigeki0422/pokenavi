import os, collections
os.environ.setdefault("OMP_NUM_THREADS", "1")
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
SGARU = "ガブリアス@こだわりスカーフ:いじっぱり:じしん|げきりん|ほのおのキバ|アイアンヘッド:2/32/0/0/0/32:さめはだ"
GIL = "ギルガルド@たべのこし:いじっぱり:ポルターガイスト|かげうち|せいなるつるぎ|キングシールド:32/32/0/0/0/2:バトルスイッチ"
def mk(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
net = PVNetNP.load("az_net_np.json")

def build():
    p1 = [mk(FLA), mk(MASK), mk(GARU)]; p2 = [mk(STAR), mk(SGARU), mk(GIL)]
    s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    return p1, s1, s2, BattleField()

def lab(p1, a):
    if a.type == "switch": return f"交代→{p1[a.switch_to].name}"
    if a.type == "move": return f"技 {p1[0].moves[a.move_idx].name_jp}" + ("(メガ)" if getattr(a,'do_mega',False) else "")
    return a.type

for sims in (400, 1600):
    p1, s1, s2, field = build()
    ai = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
    root, root_my, _ = ai._build_mcts_root(s1, s2, field, None)
    meN = root["N"][0]; meW = root["W"][0]
    rows = []
    for a in root_my:
        ix = ai._action_index(a); n = meN.get(ix, 0); w = meW.get(ix, 0.0)
        rows.append((lab(p1, a), n, (w / n if n else 0.0)))
    tot = sum(n for _, n, _ in rows) or 1
    print(f"\n=== MCTS@{sims}  ルート各手の 訪問N / Q(=W/N) ===")
    for nm, n, q in sorted(rows, key=lambda x: -x[1]):
        print(f"  {nm:<22} N={n:<4} ({n*100//tot:>2}%)  Q={q:.3f}")
