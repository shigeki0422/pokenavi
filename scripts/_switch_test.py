"""基本「不利対面では交代」をAIが学べているかの制御テスト。
相手の主力技に対し控えが無効/半減＆現役が不利、という明白な交代局面を作り、AIが交代を選ぶか測る。
交代率が高い→基本は学習済み。低い→交代という基本戦術が未学習＝設置過小評価より根が深い。
"""
import os, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from simulator.az_np import PVNetNP
from simulator.ai import certain_ko_override
from train_az2 import _net_ai

L = get_loader()

# (説明, 自分[active, 控え...], 相手[active,...], 期待交代先)
SCEN = [
 ("ライチュウ(でんき,対地不利) vs ガブリアス(じしん)／控えギャラドス=地面無効",
  ["ライチュウ@こだわりスカーフ:おくびょう:10まんボルト|きあいだま|くさむすび|ボルトチェンジ:2/0/0/32/0/32:ひらいしん",
   "ギャラドス@オボンのみ:いじっぱり:たきのぼり|じしん|りゅうのまい|アクアブレイク:2/32/0/0/0/32:いかく",
   "ブリジュラス@たべのこし:ひかえめ:りゅうせいぐん|ラスターカノン|10まんボルト|みがわり:2/0/0/32/0/32:じきゅうりょく"],
  ["ガブリアス@きあいのタスキ:ようき:じしん|げきりん|いわなだれ|スケイルショット:2/32/0/0/0/32:さめはだ",
   "マスカーニャ@こだわりスカーフ:ようき:トリックフラワー|トリプルアクセル|とんぼがえり|はたきおとす:2/32/0/0/0/32:へんげんじざい",
   "アシレーヌ@オボンのみ:ひかえめ:ムーンフォース|うたかたのアリア|アクアジェット|アンコール:22/0/0/32/0/12:げきりゅう"],
  "ギャラドス"),
 ("マスカーニャ(対炎不利) vs メガリザードンY(かえん)／控えラグラージ=炎半減",
  ["マスカーニャ@こだわりスカーフ:ようき:トリックフラワー|トリプルアクセル|とんぼがえり|はたきおとす:2/32/0/0/0/32:へんげんじざい",
   "ラグラージ@オボンのみ:いじっぱり:じしん|れいとうパンチ|ウェーブタックル|クイックターン:2/32/0/0/0/32:げきりゅう",
   "ブリジュラス@たべのこし:ひかえめ:りゅうせいぐん|ラスターカノン|10まんボルト|みがわり:2/0/0/32/0/32:じきゅうりょく"],
  ["リザードン@リザードンナイトＹ:ひかえめ:かえんほうしゃ|エアスラッシュ|だいもんじ|ソーラービーム:2/0/0/32/0/32:もうか",
   "ガブリアス@きあいのタスキ:ようき:じしん|げきりん|いわなだれ|スケイルショット:2/32/0/0/0/32:さめはだ",
   "アシレーヌ@オボンのみ:ひかえめ:ムーンフォース|うたかたのアリア|アクアジェット|アンコール:22/0/0/32/0/12:げきりゅう"],
  "ラグラージ"),
]

def run(scen, n=20, sims=400):
    desc, A, B, expect = scen
    net = PVNetNP.load()
    ai0 = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
    def AI(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False) for s in sp]
    sw = move = sw_correct = 0; acts = {}
    for seed in range(n):
        s1 = BattleSide(team(A)); s2 = BattleSide(team(B))
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        f = BattleField()
        random.seed(seed)
        a = AI(s1, s2, f)
        if getattr(a, "type", None) == "switch":
            sw += 1
            tgt = s1.party[a.switch_to].name if a.switch_to is not None else "?"
            acts[tgt] = acts.get(tgt, 0) + 1
            if tgt == expect: sw_correct += 1
        else:
            move += 1
            mn = a.move.name_jp if a.move else "?"
            acts["技:" + mn] = acts.get("技:" + mn, 0) + 1
    print(f"\n■ {desc}")
    print(f"   交代 {sw}/{n}（うち期待先{expect}へ {sw_correct}）/ 技 {move}")
    print(f"   行動内訳: {dict(sorted(acts.items(), key=lambda x:-x[1]))}")

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    for sc in SCEN:
        run(sc, n=n)
