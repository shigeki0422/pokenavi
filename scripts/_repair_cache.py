"""Part 9 Step 4: suggest_cache.json をオフラインで必然性修復する後処理パス。
各コアエントリの提案を repair_party（死に枠→pick_rate改善代替へ差し替え）に通し、
差し替えが起きた提案は _proposal_detail を再計算して差し替える。ENSスコアで再ソート。
オンラインsuggest経路は無変更（重いpick_rate測定はここだけ）。実対戦A/B 55.7%で採用。
env: NVER_OPP(6) NVER_K(8) NVER_SWAP(12) IN(suggest_cache.json) OUT(=IN上書き)
"""
import os, json, time, random
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "1")
# LEARNED_SELECTION は立てない。pick_rates/bring_dist は simulator.ai.select_party（heuristic）を
# 直接importしており影響を受けず、実際に変わるのは _product3.surrogate_score（ENSの特徴）だけ。
# 立てると _live_rust のガードに掛かってENS採点がPython経路に落ち、4.5ms→2024ms（450倍）になる上、
# 本番モデル・M-6コーパスのラベルがいずれも heuristic 選出なので学習条件とも食い違う。
import multiprocessing as mp
import product3_server as S
import feature1 as _f1
L = S.L; net = _f1._W["net"]; PG = S.PG; TH = S.TH
from _ensemble_surrogate import EnsembleScorer
import _necessity_verify as V

ens = EnsembleScorer(L, net, PG, TH)
NOPP = int(os.environ.get("NVER_OPP", "6"))
opp_panel = [a["party"] for a in S.ARCHES[:NOPP]]
IN = os.environ.get("IN", "suggest_cache.json")
OUT = os.environ.get("OUT", IN)
SAVE_EVERY = int(os.environ.get("SAVE_EVERY", "10"))   # 途中保存の間隔（軸数）
NVER_ROUNDS = int(os.environ.get("NVER_ROUNDS", "1"))   # 1提案あたりのリペア周回数


def _has_violation(party):
    """タイプ被り上限超過、または役割が重なる完全一致ペアがあるか（対戦不要の軽い判定）。"""
    import collections, _explain as EX
    from gen_party_pool import TYPEDUP_MAX
    if TYPEDUP_MAX and PG.type_dup_max(party) > TYPEDUP_MAX:
        return True
    g = collections.defaultdict(list)
    for x in party:
        g[tuple(sorted(PG._types_of_spec(x)))].append(x)
    ATK = {"スカーフ掃除役", "積みエース", "メガ積みエース", "メガエース",
           "物理アタッカー", "特殊アタッカー"}
    for _t, mem in g.items():
        if len(mem) < 2:
            continue
        b = [{"攻" if r in ATK else "補" for r in EX.role_of(x, L)} for x in mem]
        from _party_quality import mon_profile as _mpq
        def _sw(x, y):
            try: return _mpq(x, L)[1] == _mpq(y, L)[1]
            except Exception: return False
        if any((b[i] & b[j]) or _sw(mem[i], mem[j])
               for i in range(len(mem)) for j in range(i + 1, len(mem))):
            return True
    # 役割ラベル完全一致＋タイプ共有＋弱点2以上（D案）も違反として2周目に回す
    import itertools as _it
    from _party_quality import mon_profile as _mp
    for a, b2 in _it.combinations(party, 2):
        try:
            if tuple(sorted(EX.role_of(a, L))) != tuple(sorted(EX.role_of(b2, L))): continue
            if not (set(PG._types_of_spec(a)) & set(PG._types_of_spec(b2))): continue
            if len(_mp(a, L)[1] & _mp(b2, L)[1]) >= 2: return True
        except Exception: pass
    return False


def _core_keys(k):
    try:
        c = json.loads(k)[0]
        return [x.split("@")[0] for x in c] if c else []
    except Exception:
        return []


def _key_rank(k):
    """人気コア順（おまかせ最優先）でキーを並べる＝重要コアから先に確認できる。"""
    cn = _core_keys(k)
    if not cn: return -1
    return PG.rank.get(cn[0], 9999)


DONE = os.environ.get("DONE", "repair_done.json")   # 再開用: 処理済みキー集合
LIMIT = int(os.environ.get("LIMIT", "0"))           # >0で人気順この件数まで処理して打ち切り（残りは後日バックフィル）
# 差し替えが無い提案も detail を作り直す。1v1相性表(matchup)は _explain の確定数計算に依存しており、
# 表示側のバグ修正（ばけのかわの1/8削り・ロール引数）を全提案へ反映するのに要る。既定0＝従来通り。
REDETAIL_ALL = os.environ.get("REDETAIL_ALL", "0") == "1"

if __name__ == "__main__":
    cache = json.load(open(IN, encoding="utf-8"))
    keys = sorted(cache.keys(), key=_key_rank)
    if LIMIT > 0: keys = keys[:LIMIT]
    done = set(json.load(open(DONE)) if os.path.exists(DONE) else [])
    pool = mp.get_context("fork").Pool(max(1, (os.cpu_count() or 2) - 2))
    rng = random.Random(919)
    t0 = time.time(); nswap = 0; nchk = 0

    def _save():
        json.dump(cache, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
        json.dump(sorted(done), open(DONE, "w", encoding="utf-8"), ensure_ascii=False)

    for ki, k in enumerate(keys):
        if k in done: continue
        ent = cache[k]
        core_names = set(_core_keys(k))
        fixed_keys = {PG.keyof_name(n) if hasattr(PG, "keyof_name") else n for n in core_names}
        results = ent.get("results", [])
        changed = False
        # 他提案と同じ種構成に収束するのを防ぐ。リペアは1提案ずつ独立に処理するため、
        # 同じ軸内で「代替として良い駒」が共通し、別々だった2本が同じ6体に落ち着くことがある
        # （実測グソクムシャ軸: #2のMフラエッテと#3のオーロンゲが揃ってMカイリューへ差し替わった）。
        _spsets = [frozenset(x.split("@")[0] for x in r["specs"]) for r in results]
        for ri, r in enumerate(results):
            sp = r["specs"]; nchk += 1
            fixed = {PG.keyof(s) or s.split("@")[0] for s in sp if s.split("@")[0] in core_names}
            new, info = V.repair_party(sp, PG, L, TH, ens, pool, opp_panel, fixed, rng)
            # repair_party は1周1枠しか触らない。死に枠と構成違反が同居する提案では
            # 片方しか直らないので、違反が残っている提案だけ NVER_ROUNDS 周まで回す。
            # pick_rates(対戦を伴う)が重いので、無条件の再実行はしない。
            for _r2 in range(NVER_ROUNDS - 1):
                if not info.get("swapped") or not _has_violation(new):
                    break
                n2, i2 = V.repair_party(new, PG, L, TH, ens, pool, opp_panel, fixed, rng)
                if not i2.get("swapped"):
                    break
                new = n2
                info = dict(info, swapped=info["swapped"] + "+" + i2["swapped"])
            if info.get("swapped"):
                _ns = frozenset(x.split("@")[0] for x in new)
                if any(_ns == t for j, t in enumerate(_spsets) if j != ri):
                    info = dict(info, swapped=None)      # 重複を作る差し替えは取り消す
                else:
                    _spsets[ri] = _ns
            if info.get("swapped"):
                sc = ens.score(new)
                results[ri] = S._proposal_detail((sc, new, [s.split("@")[0] for s in sp if s.split("@")[0] in core_names]))
                changed = True; nswap += 1
            elif REDETAIL_ALL:
                results[ri] = S._proposal_detail((r.get("score", ens.score(sp)), sp,
                                                  [s.split("@")[0] for s in sp if s.split("@")[0] in core_names]))
                changed = True
        if changed:
            results.sort(key=lambda x: -x.get("score", 0))
            ent["results"] = results
        done.add(k)
        if len(done) % SAVE_EVERY == 0:
            _save()
            el = time.time() - t0
            print(f"  {len(done)}/{len(keys)} 差替{nswap} ({el/60:.1f}min ETA {el/max(1,len(done))*(len(keys)-len(done))/60:.0f}min)", flush=True)
    _save()
    pool.close()
    print(f"■ 修復完了: {len(keys)}コア {nchk}提案中 {nswap}差替 → {OUT} ({(time.time()-t0)/60:.0f}min)", flush=True)
