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
URUGA = "ウルガモス@オボンのみ:ずぶとい:ちょうのまい|ほのおのまい|ギガドレイン|あさのひざし:1/0/1/32/0/32:ほのおのからだ"
STARMIE = "スターミー@スターミナイト:いじっぱり:アクアブレイク|アクアジェット|アイススピナー|クイックターン:2/32/0/0/0/32:しぜんかいふく"
DODO = "ドドゲザン@くろいメガネ:いじっぱり:ふいうち|ドゲザン|アイアンヘッド|つるぎのまい:32/32/0/0/0/2:そうだいしょう"
BASHA = "バシャーモ@バシャーモナイト:いじっぱり:フレアドライブ|インファイト|まもる|つるぎのまい:2/32/0/0/0/32:かそく"
MASK = "マスカーニャ@こだわりスカーフ:ようき:トリックフラワー|トリプルアクセル|とんぼがえり|はたきおとす:2/32/0/0/0/32:へんげんじざい"
ARMOR = "アーマーガア@オボンのみ:わんぱく:はねやすめ|ボディプレス|てっぺき|とんぼがえり:32/0/32/0/0/0:プレッシャー"

def mk(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)

p1 = [mk(URUGA), mk(STARMIE), mk(DODO)]
p2 = [mk(BASHA), mk(MASK), mk(ARMOR)]
p1[0].stage_sp_attack = 2          # ほのおのまい×2でC+2
p1[1].current_hp = int(p1[1].max_hp * 91/137)   # スターミー 91/137
p2[2].current_hp = 0; p2[2].hp = 0              # アーマーガア 瀕死

s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
field = BattleField()
net = PVNetNP.load("az_net_np.json")

from simulator.alphazero import legal_actions_indexed
legal = legal_actions_indexed(s1, s2, field)
prior, val = net.evaluate(__import__("simulator.features", fromlist=["encode_state"]).encode_state(s1, s2, field), [ix for _, ix in legal])

def label(act):
    if act.type == "switch": return f"交代→{p1[act.switch_to].name}"
    if act.type == "move": return f"技 {p1[0].moves[act.move_idx].name_jp}" + ("(メガ)" if getattr(act,'do_mega',False) else "")
    return act.type

print("局面: ウルガモス(C+2,満) vs バシャーモ(メガ可) / 控え スターミー91/137・ドドゲザン")
print(f"value(P1勝率予測)={val:.3f}")
print("[生policy]")
for a, ix in sorted(legal, key=lambda x: -prior.get(x[1], 0)):
    print(f"   {label(a):<22} {prior.get(ix,0):.3f}")
for sims in (400, 1200):
    cnt = collections.Counter()
    for seed in range(8):
        ai = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
        cnt[label(ai(s1, s2, field))] += 1
    print(f"[MCTS@{sims} 8回] " + "  ".join(f"{k}:{v}" for k, v in cnt.most_common()))
