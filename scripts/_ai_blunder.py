"""Phase C1: ブランダーベンチ。本番AI(@400)同士の実対戦から決定局面をサンプルし、
審判=MCTS-regret@REF_SIMS のQで「最善よりequityを大きく落とす手」の頻度とパターンを測る。
env: N_BATT(100) P_SAMPLE(0.12) REF_SIMS(3200) AI_SIMS(400) GAP(0.15)
     POOL_SEASON(M-3) BELIEF_SEASON(未設定=M-2) PARTIES(パーティ供給元json) OUT(ai_blunder.json)

パーティ供給元は _m6_pool.load_parties()（env PARTIES / MAX_CORE_RANK）。
既定は提案キャッシュの使用率50位以内の軸。

ブランダーは審判との差(gap)だけでなく種類も記録する:
  stay_losing   審判の最善が交代なのに居座って攻撃した
  status_missed 審判の最善が変化技なのに攻撃した
  bad_switch    どちらも交代だが交代先が違う
  wrong_attack  どちらも攻撃だが技が違う
  other         上記以外
"""
import os, json, random, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
SEASON = os.environ.get("POOL_SEASON", "M-3")
_f1._ensure_loaded(SEASON, 8); L = _f1._W["loader"]
REF_SIMS = int(os.environ.get("REF_SIMS", "3200")); AI_SIMS = int(os.environ.get("AI_SIMS", "400"))
P_SAMPLE = float(os.environ.get("P_SAMPLE", "0.12")); GAP = float(os.environ.get("GAP", "0.15"))
_REF = None

def _ref(net, seed):
    global _REF
    if _REF is None:
        from train_az2 import _net_ai
        _REF = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=REF_SIMS, mcts_select="regret", mcts_fast=True)
    return _REF

def _kind(chosen, best, my_side):
    """ブランダーの種類。ユーザー基準「不利なのに交代しない」「変化技を使えない」に対応させる。"""
    if chosen is None or best is None:
        return "other"
    ct, bt = chosen.type, best.type
    if bt == "switch" and ct == "move":
        return "stay_losing"
    if bt == "move" and ct == "move":
        bm = _move_of(best, my_side); cm = _move_of(chosen, my_side)
        if bm is not None and bm.category == "status" and (cm is None or cm.category != "status"):
            return "status_missed"
        return "wrong_attack"
    if bt == "switch" and ct == "switch":
        return "bad_switch"
    return "other"


def _move_of(a, my_side):
    if a is None or a.type != "move":
        return None
    if a.move is not None:
        return a.move
    mv = my_side.active.moves if my_side.active is not None else []
    return mv[a.move_idx] if a.move_idx is not None and 0 <= a.move_idx < len(mv) else None


def _desc(a, my_side):
    if a is None: return "None"
    if a.type == "move":
        nm = a.move.name_jp if a.move is not None else (my_side.active.moves[a.move_idx].name_jp if a.move_idx < len(my_side.active.moves) else f"move{a.move_idx}")
        return nm + ("(メガ)" if getattr(a, "do_mega", False) else "")
    if a.type == "switch":
        j = getattr(a, "switch_to", -1)
        return "交代→" + (my_side.party[j].name if 0 <= j < len(my_side.party) else f"#{j}")
    return a.type

def _battle(args):
    pa, pb, seed = args
    import random as _r
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party, certain_ko_override
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField
    from train_az2 import _net_ai
    net = _f1._W["net"]; _r.seed(seed)
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    sel1 = select_party(A, B, L, n=3, temperature=0.3, rng=_r)
    sel2 = select_party(B, A, L, n=3, temperature=0.3, rng=_r)
    s1 = BattleSide(sel1, viewer_label="P1", source6=A); s2 = BattleSide(sel2, viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    a1 = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=AI_SIMS, mcts_select="regret", mcts_fast=True)
    a2 = _net_ai(net, L, 0, 12, seed ^ 1540483477, mcts=True, mcts_sims=AI_SIMS, mcts_select="regret", mcts_fast=True)
    srng = _r.Random(seed ^ 2654435769)
    recs = []
    def ai1(m, o, f):
        act = certain_ko_override(a1(m, o, f), m, o, f)
        if srng.random() < P_SAMPLE and m.active is not None and m.active.hp > 0:
            try:
                ref = _ref(net, seed)
                root, root_my, _ = ref._build_mcts_root(m, o, f, None)
                meN = root["N"][0]; meW = root["W"][0]
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
                    gap = None if cq is None else bq - cq
                    recs.append({
                        "gap": gap, "chosen": _desc(act, m), "best": _desc(ba, m),
                        "chosen_type": act.type, "best_type": ba.type,
                        "my": m.active.name, "my_hp": round(m.active.hp / max(1, m.active.max_hp), 2),
                        "opp": o.active.name, "opp_hp": round(o.active.hp / max(1, o.active.max_hp), 2),
                        "unvisited_chosen": cq is None,
                        "kind": _kind(act, ba, m), "turn": getattr(f, "turn", None)})
            except Exception as e:
                recs.append({"err": str(e)[:80]})
        return act
    def ai2(m, o, f): return certain_ko_override(a2(m, o, f), m, o, f)
    Battle(s1, s2, BattleField()).run(ai1, ai2)
    return recs

if __name__ == "__main__":
    import _m6_pool
    m2 = _m6_pool.load_parties()
    N_BATT = int(os.environ.get("N_BATT", "100"))
    rng = random.Random(141)
    jobs = [(m2[a], m2[b], int(141000000 + i * 7717) & 2147483647)
            for i, (a, b) in enumerate(rng.sample(range(len(m2)), 2) for _ in range(N_BATT))]
    print(f"■ ブランダーベンチ: AI@{AI_SIMS} 審判@{REF_SIMS} {N_BATT}戦 sample率{P_SAMPLE} "
          f"season={SEASON} belief={os.environ.get('BELIEF_SEASON', 'M-2')} "
          f"{_m6_pool.describe()}", flush=True)
    pool = mp.get_context("fork").Pool(max(1, (os.cpu_count() or 2) - 1))
    out = pool.map(_battle, jobs, chunksize=1); pool.close()
    recs = [r for rs in out for r in rs if "err" not in r]
    errs = [r for rs in out for r in rs if "err" in r]
    gaps = [r["gap"] for r in recs if r["gap"] is not None]
    bl = [r for r in recs if r["gap"] is not None and r["gap"] >= GAP]
    json.dump(recs, open(os.environ.get("OUT", "ai_blunder.json"), "w"), ensure_ascii=False)
    print(f"  サンプル決定 {len(recs)}件 (err{len(errs)})", flush=True)
    print(f"  ブランダー率(gap≥{GAP}): {len(bl)/max(1,len(gaps))*100:.1f}% ({len(bl)}/{len(gaps)})", flush=True)
    if gaps:
        print(f"  gap分布: 平均{statistics.mean(gaps)*100:.1f}pt / P90 {sorted(gaps)[int(0.9*len(gaps))]*100:.1f}pt", flush=True)
    from collections import Counter
    pat = Counter((r["chosen_type"], r["best_type"]) for r in bl)
    print("  パターン(選んだ型→最善の型):", dict(pat), flush=True)
    kinds = Counter(r.get("kind", "other") for r in bl)
    _n = max(1, len(gaps))
    print("  種類別ブランダー率:", {k: f"{v}({v/_n*100:.1f}%)" for k, v in kinds.most_common()}, flush=True)
    _sp = Counter(r["my"] for r in bl)
    print("  ブランダーの多い自分側:", dict(_sp.most_common(8)), flush=True)
    for r in sorted(bl, key=lambda x: -x["gap"])[:10]:
        print(f"    gap{r['gap']*100:.0f}pt {r['my']}(HP{r['my_hp']}) vs {r['opp']}(HP{r['opp_hp']}): 選択={r['chosen']} 最善={r['best']}", flush=True)
