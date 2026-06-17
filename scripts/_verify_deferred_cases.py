"""deferred_ai_cases.md の違和感ケースの回帰チェック（AI改善後も「担保」できているか確認用）。
各ケースの局面を組み、任意のAI(d2/MCTS等)の「選択手の分布(複数seed)」と「スコア/訪問分布」を出力。
NG手（自殺交代・無効技）の比率が下がっているかを目視判定する。
使い方: cd scripts && ./venv/bin/python _verify_deferred_cases.py
"""
import random, collections
from simulator.simulate import get_loader
from simulator.az_np import PVNetNP
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from train_az2 import _net_ai

L = get_loader(); net = PVNetNP.load()
def b(s): return build_from_spec(parse_pokemon_spec(s), L, season="M-2", randomize=False)

def mvname(side, ix):
    if ix >= 8: return f"交代→{side.party[ix-8].name}"
    if ix == 11: return "わるあがき"
    mv = side.active.moves[ix % 4]
    return (mv.name_jp if mv else f"idx{ix}") + ("(メガ)" if 4 <= ix < 8 else "")

def label(a, side):
    if a is None: return "None"
    if a.type == "switch": return f"交代→{side.party[a.switch_to].name}"
    if a.move_idx is not None and a.move_idx >= 0:
        mv = side.active.moves[a.move_idx]
        return f'{mv.name_jp}{"(メガ)" if getattr(a,"do_mega",False) else ""}'
    return "わるあがき"

def mkstate(p1, p2, setup=None):
    s1 = BattleSide([b(x) for x in p1]); s2 = BattleSide([b(x) for x in p2])
    s1.field_idx = 0; s2.field_idx = 1; s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    f = BattleField()
    if setup: setup(s1, s2, f)
    return s1, s2, f

# 比較するAI（必要に応じて差し替え。改善後の新AIをここに追加して再判定する）
def d2(k): return _net_ai(net, L, 0, 12, k, tree=True, tree_depth=2, tree_k=4, tree_det=16)
def mcts(k): return _net_ai(net, L, 0, 50, k, mcts=True, mcts_sims=1600, c_puct=1.5, mcts_select="regret", mcts_fast=True)
AIS = [("d2(現行)", d2), ("MCTS-regret@1600", mcts)]

def check(name, p1, p2, setup, ng_substr, seeds=8):
    print(f"\n=== {name} ===")
    print(f"    NG手: 「{ng_substr}」の比率が低いほど良い")
    for ainame, mk in AIS:
        # 選択分布
        cnt = collections.Counter()
        for k in range(seeds):
            s1, s2, f = mkstate(p1, p2, setup)
            cnt[label(mk(k)(s1, s2, f), s1)] += 1
        ng = sum(v for kk, v in cnt.items() if ng_substr in kk)
        # スコア/訪問
        s1, s2, f = mkstate(p1, p2, setup)
        ai = mk(0)
        if getattr(ai, "mcts", False):
            _, pi = ai.mcts_policy(s1, s2, f)
            dist = ", ".join(f"{mvname(s1, ix)}={p*100:.0f}%" for ix, p in sorted(pi.items(), key=lambda x: -x[1])[:5])
        else:
            sc = sorted(ai.score_actions_tree(s1, s2, f), key=lambda x: -x[1])
            dist = ", ".join(f"{mvname(s1, ai._action_index(a))}={v:.3f}" for a, v in sc[:5])
        print(f"  [{ainame}] NG選択 {ng}/{seeds}  | {dist}")

# ---- ケース1: ガブ(HP112,C-1) 対面ドリュウズ。ルカリオ交代=じしんで死 ----
GARC1 = "ガブリアス@オボンのみ:いじっぱり:ドラゴンテール|じしん|ステルスロック|まきびし"
LUC = "ルカリオ@ルカリオナイト:ようき:インファイト|コメットパンチ|ストーンエッジ|しんそく"
DOR = "ドリュウズ@やわらかいすな:いじっぱり:じしん|アイアンヘッド|いわなだれ|つるぎのまい"
def setup1(s1, s2, f):
    g = s1.active; g.hp = min(g.hp, 112)
    try: g.stage_sp_attack = -1
    except Exception: pass
check("ケース1 ガブ(HP112,C-1)対面ドリュウズ", [GARC1, "フラエッテ(永遠)@フラエッテナイト", LUC],
      [DOR, "ルカリオ@ルカリオナイト", "ゲッコウガ@こだわりスカーフ"], setup1, "交代→ルカリオ")

# ---- ケース2: ガブ 対面エルフーン(おいかぜ後)。ドラゴンテール=フェアリーに0倍無効 ----
GARC2 = "ガブリアス@オボンのみ:いじっぱり:ドラゴンテール|じしん|ステルスロック|まきびし"
ELF = "エルフーン@きあいのタスキ:おくびょう:ムーンフォース|おいかぜ|やどりぎのタネ|うそなき"
check("ケース2 ガブ対面エルフーン(おいかぜ後)", [GARC2], [ELF],
      lambda s1, s2, f: setattr(s2, "tailwind", True), "ドラゴンテール")

print("\n(ケース3=ステロ下の自殺交代は局面再構成が複雑なため未実装。根本原因はケース1/2と同根)")
