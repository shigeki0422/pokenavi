import sys, json; sys.path.insert(0,"/Users/shigeki/work/pokenavi/scripts")
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.features import encode_state
L = get_loader()
A = ["ギャラドス@ゴツゴツメット:いじっぱり:たきのぼり|パワーウィップ|じしん|りゅうのまい:1/32/1/0/0/32:いかく",
     "ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:1/32/1/0/0/32:ばけのかわ",
     "アーマーガア@たべのこし:わんぱく:はねやすめ|とんぼがえり|てっぺき|ボディプレス:32/2/17/0/15/0:プレッシャー"]
B = ["ガブリアス@こだわりスカーフ:ようき:じしん|げきりん|がんせきふうじ|ステルスロック:2/32/0/0/0/32:さめはだ",
     "オオニューラ@サイコシード:いじっぱり:トリプルアクセル|れんぞくぎり|つるぎのまい|はたきおとす:1/32/1/0/0/32:わるいてぐせ",
     "クエスパトラ@ひかりのねんど:おくびょう:リフレクター|ひかりのかべ|ルミナコリジョン|めざましビンタ:31/0/3/32/0/0:びびり"]
p1=[build_from_spec(parse_pokemon_spec(s), L, season="M-6", randomize=False) for s in A]
p2=[build_from_spec(parse_pokemon_spec(s), L, season="M-6", randomize=False) for s in B]
s1=BattleSide(p1); s2=BattleSide(p2); s1.field_idx=0; s2.field_idx=1
print(json.dumps(encode_state(s1,s2,BattleField())))
