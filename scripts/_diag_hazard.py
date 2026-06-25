import os
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
GARU = "ガブリアス@オボンのみ:いじっぱり:ドラゴンテール|じしん|ステルスロック|まきびし:32/0/32/0/0/2:さめはだ"
MASK = "マスカーニャ@こだわりスカーフ:いじっぱり:トリックフラワー|かみなりパンチ|トリプルアクセル|とんぼがえり:4/30/20/0/0/12:へんげんじざい"
LUKA = "ルカリオ@ルカリオナイト:ようき:インファイト|コメットパンチ|つるぎのまい|バレットパンチ:2/32/0/0/0/32:せいぎのこころ"
RIZA = "リザードン@リザードナイトＹ:ひかえめ:かえんほうしゃ|エアスラッシュ|ソーラービーム|りゅうのはどう:0/0/0/32/0/32:もうか"
MIMI = "ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ"
GIL = "ギルガルド@たべのこし:なまいき:キングシールド|シャドーボール|ラスターカノン|かげうち:32/0/0/30/0/0:バトルスイッチ"
def mk(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
net = PVNetNP.load("az_net_np.json")

def value(p1, p2, sr=False, sp=0):
    s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    f = BattleField(); f.stealth_rock[1] = sr; f.spikes[1] = sp
    legal = legal_actions_indexed(s1, s2, f)
    _, v = net.evaluate(encode_state(s1, s2, f), [ix for _, ix in legal])
    return v

print("=== Test1: 価値ネットは『対リザ陣にステロ』を高評価するか（P1視点value）===")
p1 = [mk(GARU), mk(MASK), mk(LUKA)]; p2 = [mk(GIL), mk(RIZA), mk(MIMI)]
b = value(p1, p2); sr = value(p1, p2, sr=True); sp = value(p1, p2, sp=1)
print(f"  ハザード無し      value={b:.3f}")
print(f"  相手にステロ      value={sr:.3f}  (Δ={sr-b:+.3f})")
print(f"  相手にまきびし1層  value={sp:.3f}  (Δ={sp-b:+.3f})")
print(f"  → ステロ優位 Δ(SR-SP) = {sr-sp:+.3f}")

# 参考：ステロのリザードンへの実ダメージ割合
riz = mk(RIZA); riz.do_mega_evolve()
from simulator.battle import _entry_effects
print(f"  (参考) リザードン(メガ)はいわ二重弱点＝ステロで最大HPの1/2、まきびしはひこうで0")

print("\n=== Test2: MCTSのsimsを増やすとQ(ステロ)−Q(まきびし)は開くか ===")
def garu_first():
    p1 = [mk(GARU), mk(MASK), mk(LUKA)]; p2 = [mk(GIL), mk(RIZA), mk(MIMI)]
    s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    return p1, s1, s2, BattleField()
p1ref, _, _, _ = garu_first()
sr_idx = next(i for i, m in enumerate(p1ref[0].moves) if m.name_jp == "ステルスロック")
sp_idx = next(i for i, m in enumerate(p1ref[0].moves) if m.name_jp == "まきびし")
for sims in (400, 1600, 4000):
    p1, s1, s2, f = garu_first()
    ai = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
    root, root_my, _ = ai._build_mcts_root(s1, s2, f, None)
    meN = root["N"][0]; meW = root["W"][0]
    def qn(idx):
        n = meN.get(idx, 0); return (meW.get(idx, 0.0)/n if n else 0.0), n
    qsr, nsr = qn(sr_idx); qsp, nsp = qn(sp_idx)
    print(f"  sims={sims:<5} ステロ Q={qsr:.3f}(N{nsr})  まきびし Q={qsp:.3f}(N{nsp})  Δ={qsr-qsp:+.3f}")
