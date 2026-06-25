"""旧ネット(893次元)を新エンコード(905次元・全対面ダメージ行列)へ重み移植。
入力層W1のみ次元依存。pre-matrix/post-matrixの重みはそのまま、新行列18枠は『現役行』に旧6枠を写し
控え行はゼロ初期化。これで挙動は旧ネットと同一のまま、学習で控え対面の重みを獲得させる。
"""
import numpy as np
from simulator.az_np import PVNetNP

OLD = "az_net_np.json"; NEW = "/tmp/transfer_net.json"
BASE = 822          # 2*_PER_SIDE（行列開始位置）
OLD_DIM = 893; NEW_DIM = 905
old = PVNetNP.load(OLD)
assert old.dim == OLD_DIM, f"旧dim={old.dim}"
new = PVNetNP(NEW_DIM, hidden=old.hidden, hidden2=old.hidden2, hidden3=old.hidden3, seed=0)
# 次元非依存の重みを全コピー
new.b1 = old.b1.copy(); new.W2 = old.W2.copy(); new.b2 = old.b2.copy()
new.Wv = old.Wv.copy(); new.bv = float(old.bv); new.Wp = old.Wp.copy(); new.bp = old.bp.copy()
if old.hidden3:
    new.W3 = old.W3.copy(); new.b3 = old.b3.copy()
# 入力層W1の列を再マッピング
W1 = np.zeros((old.hidden, NEW_DIM))
W1[:, 0:BASE] = old.W1[:, 0:BASE]                         # pre-matrix（同一）
W1[:, BASE+0:BASE+3] = old.W1[:, BASE+0:BASE+3]           # 自分現役→相手3（新o1×o2のi=0行）
W1[:, BASE+9:BASE+12] = old.W1[:, BASE+3:BASE+6]          # 相手現役→自分3（新o2×o1のi=0行）
# 残り新行列枠（控え行 BASE+3..8, BASE+12..17）はゼロのまま
W1[:, BASE+18:NEW_DIM] = old.W1[:, BASE+6:OLD_DIM]        # post-matrix（+12シフト）
new.W1 = W1
new.save(NEW)
print(f"移植完了 → {NEW} (dim {old.dim}→{new.dim}, hidden {old.hidden}x{old.hidden2})")

# サニティ: 新エンコードの状態で評価が走る（次元一致）か
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.features import encode_state
import json
L = get_loader()
pool = json.load(open("func1_themed_M-3.json"))["parties"]
T = [build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False) for s in pool[0]["specs"][:3]]
O = [build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False) for s in pool[1]["specs"][:3]]
feat = encode_state(BattleSide(T), BattleSide(O), BattleField())
print("encode_state dim:", len(feat))
v = new.evaluate(feat, [0])
print("評価OK 価値=", round(v[1], 3))
EOF = None
