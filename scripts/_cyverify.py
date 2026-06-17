"""Cythonコンパイル前後の正解一致＆速度検証。
決定的バトル(固定ロール+seed)の勝敗・ターン数と encode_state のハッシュを基準と照合。
"""
import sys, time, random, hashlib
import _pop_gen as G
from simulator.simulate import get_loader
from simulator.az_np import PVNetNP
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, Battle, BattleField
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI, select_party
from simulator.features import encode_state
import simulator.damage as _dmg
from train_az2 import _net_ai

L = get_loader(); net = PVNetNP.load()
D = G.load(season="M-2"); rng = random.Random(0)
parties = [G.gen_party(D, rng) for _ in range(10)]
def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season="M-2", randomize=False) for s in sp]

# --- 正解シグネチャ: 決定的HeuristicバトルK戦の勝敗+ターン, encode_stateハッシュ ---
h = HeuristicAI()
sig = []
_dmg._ROLL_OVERRIDE = 0.85
for i in range(12):
    a, b = parties[i % 10], parties[(i + 3) % 10]
    random.seed(1000 + i)
    s1 = BattleSide(team(a)[:3]); s2 = BattleSide(team(b)[:3])
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    bt = Battle(s1, s2); w = bt.run(h, h)
    sig.append((w, bt.turn))
# encode_state ハッシュ
fs = []
for i in range(6):
    a, b = parties[i], parties[i + 1]
    s1 = BattleSide(team(a)[:3]); s2 = BattleSide(team(b)[:3]); s1.field_idx = 0; s2.field_idx = 1
    vec = encode_state(s1, s2, BattleField())
    fs.append(round(sum(vec), 6))
    fs.append(round(sum(x * x for x in vec), 6))
_dmg._ROLL_OVERRIDE = None
enc_hash = hashlib.md5(str(fs).encode()).hexdigest()[:12]
batt_hash = hashlib.md5(str(sig).encode()).hexdigest()[:12]
print(f"SIG battle={batt_hash} encode={enc_hash}", flush=True)

# --- 速度: d2 バトル ---
d2 = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)
s1 = BattleSide(list(select_party(team(parties[0]), team(parties[1]), L, n=3, temperature=0.0, rng=rng)))
s2 = BattleSide(list(select_party(team(parties[1]), team(parties[0]), L, n=3, temperature=0.0, rng=rng)))
s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
Battle(s1, s2).run(d2, d2)  # warm
t = time.time(); nb = 4
for k in range(nb):
    s1 = BattleSide(list(select_party(team(parties[k % 10]), team(parties[(k+3) % 10]), L, n=3, temperature=0.0, rng=rng)))
    s2 = BattleSide(list(select_party(team(parties[(k+3) % 10]), team(parties[k % 10]), L, n=3, temperature=0.0, rng=rng)))
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    Battle(s1, s2).run(d2, d2)
print(f"SPEED d2-battle {(time.time()-t)/nb:.2f}s/戦", flush=True)
