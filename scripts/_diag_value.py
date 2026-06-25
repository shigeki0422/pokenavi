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
from simulator.damage import calc_damage

L = get_loader()
FLA = "フラエッテ(永遠)@フラエッテナイト:おくびょう:はめつのひかり|ムーンフォース|ドレインキッス|めいそう:0/0/10/24/0/32:フラワーベール"
MASK = "マスカーニャ@こだわりスカーフ:いじっぱり:トリックフラワー|かみなりパンチ|トリプルアクセル|とんぼがえり:4/30/20/0/0/12:へんげんじざい"
GARU = "ガブリアス@こだわりスカーフ:いじっぱり:じしん|げきりん|ほのおのキバ|アイアンヘッド:2/32/0/0/0/32:さめはだ"
STAR = "スターミー@スターミナイト:いじっぱり:アクアブレイク|アクアジェット|アイススピナー|クイックターン:2/32/0/0/0/32:しぜんかいふく"
SGARU = "ガブリアス@こだわりスカーフ:いじっぱり:じしん|げきりん|ほのおのキバ|アイアンヘッド:2/32/0/0/0/32:さめはだ"
GIL = "ギルガルド@たべのこし:いじっぱり:ポルターガイスト|かげうち|せいなるつるぎ|キングシールド:32/32/0/0/0/2:バトルスイッチ"

def mk(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
net = PVNetNP.load("az_net_np.json")

def value(p1, p2):
    s1 = BattleSide(p1); s2 = BattleSide(p2); s1.field_idx = 0; s2.field_idx = 1
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    legal = legal_actions_indexed(s1, s2, BattleField())
    _, v = net.evaluate(encode_state(s1, s2, BattleField()), [ix for _, ix in legal])
    return v

# ① ターン1 (3v3, フラエッテ生存・両者メガ前)
p1 = [mk(FLA), mk(MASK), mk(GARU)]; p2 = [mk(STAR), mk(SGARU), mk(GIL)]
print(f"① ターン1 (3v3 フラエッテ生存): value(P1) = {value(p1, p2):.3f}")

# ② 居座り→フラエッテ死亡後 (2v3, マスカーニャ着地・スターミーはメガ済)
p1a = [mk(MASK), mk(GARU), mk(FLA)]; p1a[2].hp = 0; p1a[2].is_alive = False
p2a = [mk(STAR), mk(SGARU), mk(GIL)]; p2a[0].do_mega_evolve()
s1a = BattleSide(p1a); s1a.mega_used = True   # フラエッテでメガ消費済み
print(f"② 居座りでフラエッテ死亡後 (2v3): value(P1) = {value(p1a, p2a):.3f}  ※P1メガ消費済")

# ③ 理想ライン後 (3v2, マスカーニャ半減被弾でスターミー撃破・フラエッテ温存)
mask_b = mk(MASK)
star_m = mk(STAR); star_m.do_mega_evolve()
dmg = calc_damage(star_m, mask_b, L.get_move("アクアブレイク"), BattleField(), False, 0.85)
mask_b.hp = max(1, mask_b.max_hp - dmg)
p1b = [mask_b, mk(FLA), mk(GARU)]            # フラエッテ生存・未メガ
p2b = [mk(SGARU), mk(GIL)]                   # スターミー撃破済
print(f"③ 理想ライン後 (3v2 スターミー撃破/マスカーニャ {mask_b.hp}/{mask_b.max_hp}・P1メガ温存): value(P1) = {value(p1b, p2b):.3f}")
print(f"   （参考: アクアブレイク被ダメ {dmg}＝マスカーニャ最大HP{mask_b.max_hp}の{dmg*100//mask_b.max_hp}%）")
