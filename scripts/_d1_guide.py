"""Part1 Step D: 選出ガイド計算バッチ。suggest_cacheの各提案パーティ×archetypes_m3(8構築)に
「推奨3匹（EV-2段）＋counter表＋根拠勝率」を付与し suggest_cache_guided.json に書き出す。
env: PILOT(0) N_GUIDE(5) K1(30) K2(16) NB(4) GA_SIMS(120) ENTRIES(空=全61)
"""
import os, json, random, statistics, itertools, time, numpy as np
from collections import Counter
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "120")
import multiprocessing as mp
import feature1 as _f1
SEASON = os.environ.get("POOL_SEASON", "M-3")
_f1._ensure_loaded(SEASON, 8); L = _f1._W["loader"]
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.ai import select_party, _effective_speed
from simulator.battle import BattleField
from _v3_rollout import _greedy_3v3
from _v3_final import _mcts_3v3       # (pa, sa, pb, sb, seed): 両者3匹固定・本番同等MCTS
field = BattleField()
SUBSETS = list(itertools.combinations(range(6), 3))

def build6(specs):
    return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
def valid_subsets(specs):
    P = build6(specs); av = sum(1 for m in P if getattr(m, "mega_data", None) is not None); t = 1 if av >= 1 else 0
    return [S for S in SUBSETS if sum(1 for j in S if getattr(P[j], "mega_data", None) is not None) == t]
def bring_dist(opp_specs, my_specs, nb, ns=150, seed=0):
    O = build6(opp_specs); Pm = build6(my_specs); idx = {id(m): j for j, m in enumerate(O)}
    rng = random.Random(seed); cnt = Counter()
    for _ in range(ns):
        sel = select_party(O, Pm, L, n=3, temperature=0.3, rng=rng)
        cnt[tuple(sorted(idx[id(m)] for m in sel))] += 1
    top = cnt.most_common(nb); tot = sum(c for _, c in top)
    return [(s, c / tot) for s, c in top]

def guide_for(pool, sp, arch, gseed):
    """1提案パーティ×1相手構築のガイド: {recommend, wr, counter}"""
    K1 = int(os.environ.get("K1", "30")); K2 = int(os.environ.get("K2", "16")); NB = int(os.environ.get("NB", "4"))
    my_names = [x.split("@")[0] for x in sp]
    op = arch["party"]; op_names = arch.get("names") or [x.split("@")[0] for x in op]
    subs = valid_subsets(sp)
    dist = bring_dist(op, sp, NB, seed=gseed)
    # stage1: greedy行列
    jobs, meta = [], []
    for ri, s in enumerate(subs):
        for ci, (ob, w) in enumerate(dist):
            for k in range(K1):
                seed = int(230_000_000 + gseed * 7919 + ri * 101 + ci * 7 + k) & 0x7fffffff
                jobs.append((sp, s, op, ob, seed)); meta.append((ri, ci))
    res = pool.map(_greedy_3v3, jobs, chunksize=8)
    M = np.zeros((len(subs), NB)); D = np.zeros_like(M)
    for (ri, ci), r in zip(meta, res):
        D[ri, ci] += 1 if r in (1, 2) else 0; M[ri, ci] += 1 if r == 1 else 0
    M = M / np.maximum(1, D)
    wts = np.array([w for _, w in dist] + [0.0] * (NB - len(dist)))
    ev = M @ wts
    _TOPK = min(int(os.environ.get("GTOPK", "2")), len(subs))   # FULL構成=3。既定2=従来互換
    top2 = [int(x) for x in np.argsort(ev)[-_TOPK:]]
    # stage2: top2×相手パターン別にMCTS実測（本番同等）。おすすめ選定も表示もこのMm行列で一貫させる
    #   （旧: おすすめ=MCTS/表=greedy の別エンジン混在で非整合だった問題を解消）
    # P3 段階判定（GUIDE_STAGED=1）: 各列をまずK0=6戦で測り、|wr-0.5|>0.25でバンド確定なら打ち切り、
    #   曖昧な列だけK2まで追加測定。表示はバンド（◎○△×・境界0.4/0.6/0.75）なので勝率の粗さは非可視。
    #   GUIDE_STAGED=0 は従来と同一シード/同一戦数＝ビット一致。
    _STAGED = os.environ.get("GUIDE_STAGED", "0") == "1"
    _K0 = int(os.environ.get("GUIDE_K0", "6"))
    def _seed2(ri, ci, k):
        return int(240_000_000 + gseed * 7919 + ri * 101 + ci * 13 + k) & 0x7fffffff
    def _wr(seg):
        dec = sum(1 for r in seg if r in (1, 2)); win = sum(1 for r in seg if r == 1)
        return win / max(1, dec)
    def _mcts_rows(ris):
        if not _STAGED:
            out = {}
            for ri in ris:
                jobs2 = [(sp, subs[ri], op, list(dist[ci][0]), _seed2(ri, ci, k))
                         for ci in range(len(dist)) for k in range(K2)]
                res2 = pool.map(_mcts_3v3, jobs2, chunksize=4)
                out[ri] = np.array([_wr(res2[ci * K2:(ci + 1) * K2]) for ci in range(len(dist))])
            return out
        cells = [(ri, ci) for ri in ris for ci in range(len(dist))]
        j1 = [(sp, subs[ri], op, list(dist[ci][0]), _seed2(ri, ci, k))
              for (ri, ci) in cells for k in range(_K0)]
        r1 = pool.map(_mcts_3v3, j1, chunksize=4)
        seg1 = {cells[i]: list(r1[i * _K0:(i + 1) * _K0]) for i in range(len(cells))}
        amb = [c for c in cells if abs(_wr(seg1[c]) - 0.5) <= 0.25]   # バンド未確定＝追加測定
        j2 = [(sp, subs[ri], op, list(dist[ci][0]), _seed2(ri, ci, k))
              for (ri, ci) in amb for k in range(_K0, K2)]
        r2 = pool.map(_mcts_3v3, j2, chunksize=4) if j2 else []
        m = K2 - _K0
        seg2 = {amb[i]: list(r2[i * m:(i + 1) * m]) for i in range(len(amb))}
        out = {ri: np.zeros(len(dist)) for ri in ris}
        for (ri, ci) in cells:
            out[ri][ci] = _wr(seg1[(ri, ci)] + seg2.get((ri, ci), []))
        return out
    Mm = _mcts_rows(top2)
    wd = np.array([w for _, w in dist])
    pick = max(top2, key=lambda ri: float(Mm[ri] @ wd))
    pwr = float(Mm[pick] @ wd)
    # vs: 「おすすめ選出そのもの」の相手パターン別MCTS勝率（表と総合wrが同一測定＝整合）。
    #     苦しい列(wr<0.45)には、その列を読み切れた場合の対抗選出(alt)をMCTSで実測し併記。
    vs = []
    for ci, (ob, w) in enumerate(dist):
        cell = float(Mm[pick][ci])
        row = {"opp3": [op_names[j] for j in ob], "share": round(w, 2), "wr": round(cell, 2)}
        if cell < 0.45:
            br = int(np.argmax(M[:, ci]))   # greedyで対抗候補を絞り、MCTSで確認
            if br != pick:
                def _altseed(k):
                    return int(245_000_000 + gseed * 7919 + br * 101 + ci * 13 + k) & 0x7fffffff
                if _STAGED:
                    # まずK0戦。cell+0.15の閾値に届く見込みが無い（K0でcell以下）なら打ち切り＝alt無し。
                    r3 = pool.map(_mcts_3v3, [(sp, subs[br], op, list(ob), _altseed(k))
                                              for k in range(_K0)], chunksize=4)
                    if _wr(r3) > cell:
                        r3 += pool.map(_mcts_3v3, [(sp, subs[br], op, list(ob), _altseed(k))
                                                   for k in range(_K0, K2)], chunksize=4)
                else:
                    r3 = pool.map(_mcts_3v3, [(sp, subs[br], op, list(ob), _altseed(k))
                                              for k in range(K2)], chunksize=4)
                awr = _wr(r3)
                if awr >= cell + 0.15:
                    row["alt"] = {"my3": [my_names[j] for j in subs[br]], "wr": round(awr, 2)}
        vs.append(row)
    # 生データ（raw）: 表示変更を再シミュレーションなしで行えるよう、測定行列を保存。
    #   subsets=各行の3匹インデックス, dist=相手bring(インデックス+確率),
    #   M_greedy=全選出×相手列のgreedy勝率, Mm_mcts=top2選出のMCTS勝率行, pick=採用行index
    raw = {
        "subsets": [list(s) for s in subs],
        "dist": [{"opp3_idx": list(ob), "share": round(w, 4)} for ob, w in dist],
        "M_greedy": [[round(float(M[ri, ci]), 3) for ci in range(len(dist))] for ri in range(len(subs))],
        "Mm_mcts": {str(ri): [round(float(Mm[ri][ci]), 3) for ci in range(len(dist))] for ri in top2},
        "pick": int(pick), "K1": K1, "K2": K2,
        "my_names": my_names, "opp_names": op_names,
    }
    return {"label": arch.get("label", ""), "opp": op_names,
            "recommend": [my_names[j] for j in subs[pick]], "wr": round(float(pwr), 2), "vs": vs, "raw": raw}

if __name__ == "__main__":
    from gen_party_pool import PartyGen as _PG
    PG_RANK = _PG().rank
    cache = json.load(open(os.environ.get("GIN","suggest_cache.json")))
    archs = json.load(open("archetypes_m3.json"))
    N_GUIDE = int(os.environ.get("N_GUIDE", "5"))
    PILOT = os.environ.get("PILOT", "0") == "1"
    out_path = os.environ.get("GOUT","suggest_cache_guided.json")
    raw_path = os.environ.get("GRAW", out_path.replace(".json", "") + "_raw.json")   # 生データ(行列)サイドカー
    out = json.load(open(out_path)) if os.path.exists(out_path) else {}
    raw_all = json.load(open(raw_path)) if os.path.exists(raw_path) else {}
    pool = mp.get_context("fork").Pool(max(1, (os.cpu_count() or 2) - 1))
    # 人気コア順（キー先頭要素=core指定の使用率rank）で焼く。おまかせ([])は最優先
    def _key_rank(k):
        try:
            core = json.loads(k)[0]
            if not core: return -1
            sp = core[0]["sp"] if isinstance(core[0], dict) else str(core[0]).split("@")[0]
            return PG_RANK.get(sp, 9999)
        except Exception:
            return 9999
    all_keys = sorted(cache.keys(), key=_key_rank)
    keys = all_keys[:1] if PILOT else all_keys
    for ki, key in enumerate(keys):
        if key in out and not PILOT: continue   # 再開可能
        ent = json.loads(json.dumps(cache[key]))   # deep copy
        results = ent["results"][:N_GUIDE] if not PILOT else ent["results"][:1]
        raw_ent = []
        for pi, r in enumerate(results):
            t0 = time.time()
            sp = r["specs"]
            guides = []
            for ai_, arch in enumerate(archs):
                gseed = ki * 1000 + pi * 100 + ai_
                guides.append(guide_for(pool, sp, arch, gseed))
            # 基本形（最頻の推奨3匹）を、それが採用されなかった相手でもMCTS実測する。
            # これが無いと「基本形から入れ替える理由」を基本形と比較できない（次点との比較になってしまう）。
            base_trio = Counter(tuple(g["recommend"]) for g in guides).most_common(1)[0][0]
            for ai_, (arch, g) in enumerate(zip(archs, guides)):
                raw = g.get("raw")
                if not raw: continue
                subs = raw["subsets"]; my = raw["my_names"]
                bi = next((i for i, s in enumerate(subs)
                           if set(my[j] for j in s) == set(base_trio)), None)
                if bi is None or str(bi) in raw["Mm_mcts"]: continue   # 既に実測済み or 構成不可
                K2 = int(os.environ.get("K2", "10"))
                gseed = ki * 1000 + pi * 100 + ai_
                _staged = os.environ.get("GUIDE_STAGED", "0") == "1"
                _k0 = int(os.environ.get("GUIDE_K0", "6"))
                def _wr0(res):
                    dec = sum(1 for x in res if x in (1, 2)); win = sum(1 for x in res if x == 1)
                    return win / max(1, dec)
                def _bseed(ci, k):
                    return int(247_000_000 + gseed * 7919 + bi * 101 + ci * 13 + k) & 0x7fffffff
                row = []
                for ci, d in enumerate(raw["dist"]):
                    op3 = list(d["opp3_idx"])
                    if _staged:
                        res = pool.map(_mcts_3v3, [(sp, subs[bi], arch["party"], op3, _bseed(ci, k))
                                                   for k in range(min(_k0, K2))], chunksize=4)
                        if abs(_wr0(res) - 0.5) <= 0.25 and K2 > _k0:   # バンド未確定なら追加測定
                            res += pool.map(_mcts_3v3, [(sp, subs[bi], arch["party"], op3, _bseed(ci, k))
                                                        for k in range(_k0, K2)], chunksize=4)
                    else:
                        res = pool.map(_mcts_3v3, [(sp, subs[bi], arch["party"], op3, _bseed(ci, k))
                                                   for k in range(K2)], chunksize=4)
                    row.append(round(_wr0(res), 3))
                raw["Mm_mcts"][str(bi)] = row
                raw["base_row"] = bi
            # 配信用は raw を剥がして軽量化。raw はサイドカーへ
            raw_ent.append([g.pop("raw", None) for g in guides])
            r["guide"] = guides
            print(f"[{ki+1}/{len(keys)}] party{pi}: {time.time()-t0:.0f}s "
                  + " / ".join(f"{g['label']}:{'+'.join(g['recommend'][:1])}..{g['wr']:.2f}" for g in guides[:3]), flush=True)
        out[key] = ent
        raw_all[key] = raw_ent
        json.dump(out, open(out_path, "w"), ensure_ascii=False)
        json.dump(raw_all, open(raw_path, "w"), ensure_ascii=False)
    pool.close()
    print(f"■ ガイド付与完了 {len(out)}/{len(cache)}エントリ → {out_path}（生データ→{raw_path}）", flush=True)
