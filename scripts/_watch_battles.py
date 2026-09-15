"""観戦用ログ: 本番AI同士の対戦を人が読める1戦ログに出す（Phase 0-3）。

ユーザー評価軸「対戦ログを見て中級〜上級プレイヤーが違和感を持たないこと」を
判定するための材料。数値（ブランダー率）だけでは「何が変か」が分からない。

各ターンに「両者の選択」「実際に起きたこと」「残HP」を出し、REF=1 なら審判
（同じAIを8倍の探索量 MCTS@3200）の最善手と比べて gap≥閾値 の手に ⚠ を付ける。

env: N(観戦する対戦数=5) AI_SIMS(400) REF(1で審判注記) REF_SIMS(3200) GAP(0.15)
     P_SAMPLE(審判にかける決定の割合=1.0) SEED(1000) OUT(出力ファイル)
     POOL_SEASON/BELIEF_SEASON/MAX_CORE_RANK は _m6_pool と同じ
"""
import os, sys, random, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1
import _m6_pool

SEASON = os.environ.get("POOL_SEASON", "M-6")
AI_SIMS = int(os.environ.get("AI_SIMS", "400"))
REF_ON = os.environ.get("REF") == "1"
REF_SIMS = int(os.environ.get("REF_SIMS", "3200"))
GAP = float(os.environ.get("GAP", "0.15"))
P_SAMPLE = float(os.environ.get("P_SAMPLE", "1.0"))
N = int(os.environ.get("N", "5"))
SEED = int(os.environ.get("SEED", "1000"))

_f1._ensure_loaded(SEASON, 8)
L = _f1._W["loader"]; NET = _f1._W["net"]

from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, Battle, BattleField
from simulator.belief import OpponentBelief
from simulator.ai import select_party, certain_ko_override
from train_az2 import _net_ai


def _hp(p):
    return f"{p.name}({round(p.hp / max(1, p.max_hp) * 100)}%)"


def _desc(a, side):
    if a is None:
        return "?"
    if a.type == "switch":
        j = getattr(a, "switch_to", -1)
        nm = side.party[j].name if 0 <= j < len(side.party) else f"#{j}"
        return f"交代→{nm}"
    mv = a.move
    if mv is None and a.move_idx is not None and side.active is not None:
        m = side.active.moves
        mv = m[a.move_idx] if 0 <= a.move_idx < len(m) else None
    return (mv.name_jp if mv is not None else "?") + ("(メガ)" if getattr(a, "do_mega", False) else "")


def _skip(line):
    """観戦に不要な行を落とす。開示ログ(▷)は「AIが何を知ったか」なので残す価値があるが、
    毎ターン大量に出て読みにくいので既定では落とす（VERBOSE=1 で出す）。"""
    if os.environ.get("VERBOSE") == "1":
        return False
    return line.startswith("▷")


def watch(pa, pb, seed, out):
    rng = random.Random(seed)
    random.seed(seed)
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    sel1 = select_party(A, B, L, n=3, temperature=0.3, rng=rng)
    sel2 = select_party(B, A, L, n=3, temperature=0.3, rng=rng)
    s1 = BattleSide(sel1, viewer_label="P1", source6=A)
    s2 = BattleSide(sel2, viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    a1 = _net_ai(NET, L, 0, 12, seed, mcts=True, mcts_sims=AI_SIMS, mcts_select="regret", mcts_fast=True)
    a2 = _net_ai(NET, L, 0, 12, seed ^ 0x5bd1e995, mcts=True, mcts_sims=AI_SIMS, mcts_select="regret", mcts_fast=True)
    ref = _net_ai(NET, L, 0, 12, seed, mcts=True, mcts_sims=REF_SIMS, mcts_select="regret", mcts_fast=True) if REF_ON else None
    srng = random.Random(seed ^ 0x9e3779b9)

    out.write(f"\n{'=' * 72}\n■ 対戦 seed={seed}   AI@{AI_SIMS}" + (f" / 審判@{REF_SIMS}" if REF_ON else "") + "\n")
    out.write(f"  P1 選出: {' / '.join(p.name for p in sel1)}\n")
    out.write(f"      控え含む6体: {' / '.join(p.name for p in A)}\n")
    out.write(f"  P2 選出: {' / '.join(p.name for p in sel2)}\n")
    out.write(f"      控え含む6体: {' / '.join(p.name for p in B)}\n")

    picked = {}
    notes = []

    def wrap(ai, side_key):
        def f(m, o, fld):
            act = certain_ko_override(ai(m, o, fld), m, o, fld)
            # 行動を選んだ時点のHPを控える。on_turn はターン終了後に呼ばれるので、
            # そこで読むと「選択時の状況」ではなく「結果」を表示してしまう。
            picked[side_key] = _desc(act, m)
            picked[side_key + "_hp"] = _hp(m.active) if m.active is not None else "-"
            if ref is not None and srng.random() < P_SAMPLE and m.active is not None and m.active.hp > 0:
                try:
                    root, root_my, _ = ref._build_mcts_root(m, o, fld, None)
                    meN, meW = root["N"][0], root["W"][0]
                    minv = max(10, int(0.01 * REF_SIMS))
                    q = {}
                    for a in root_my:
                        ix = ref._action_index(a); n = meN.get(ix, 0)
                        if n >= minv:
                            q[ix] = (meW.get(ix, 0.0) / n, a)
                    if len(q) >= 2:
                        cix = ref._action_index(act)
                        bix, (bq, ba) = max(q.items(), key=lambda kv: kv[1][0])
                        cq = q.get(cix, (None, None))[0]
                        if cq is not None and bq - cq >= GAP:
                            picked[side_key] += f"  ⚠審判の最善={_desc(ba, m)} (gap{(bq - cq) * 100:.0f}pt)"
                            notes.append((side_key, picked[side_key]))
                except Exception:
                    pass
            return act
        return f

    b = Battle(s1, s2, BattleField())
    seen = [0]

    def on_turn(bt):
        out.write(f"\n--- ターン{bt.turn}   P1 {picked.get('P1_hp', '-')}  vs  P2 {picked.get('P2_hp', '-')}\n")
        out.write(f"    P1の手: {picked.get('P1', '-')}\n")
        out.write(f"    P2の手: {picked.get('P2', '-')}\n")
        for line in bt.logs[seen[0]:]:
            if not _skip(line):
                out.write(f"      {line}\n")
        seen[0] = len(bt.logs)

    res = b.run(wrap(a1, "P1"), wrap(a2, "P2"), on_turn=on_turn)
    out.write(f"\n  結果: {'P1の勝ち' if res == 1 else ('P2の勝ち' if res == 2 else '引き分け')}（{b.turn}ターン）\n")
    if notes:
        out.write(f"  ⚠ 審判と乖離した手: {len(notes)}件\n")
    return len(notes)


def main():
    P = _m6_pool.load_parties()
    rng = random.Random(SEED)
    buf = io.StringIO()
    buf.write(f"対戦AI 観戦ログ  {_m6_pool.describe()}  AI@{AI_SIMS}"
              + (f" 審判@{REF_SIMS} gap≥{GAP}" if REF_ON else " (審判なし)") + "\n")
    total = 0
    for i in range(N):
        a, b = rng.sample(range(len(P)), 2)
        total += watch(P[a], P[b], SEED + i * 7717, buf)
    buf.write(f"\n{'=' * 72}\n合計 ⚠{total}件 / {N}戦\n")
    txt = buf.getvalue()
    path = os.environ.get("OUT")
    if path:
        open(path, "w", encoding="utf-8").write(txt)
        print(f"書き出し: {path}  ({len(txt.splitlines())}行, ⚠{total}件)", flush=True)
    else:
        print(txt)


if __name__ == "__main__":
    main()
