"""Part 9 Step 4: パーティ提案の必然性検証・修復。
top候補ごとに、ENS非劣化の範囲で1枠を差し替えて必然性を改善（1周上限・コア枠は対象外）:
 (1) 死に枠: pick_rate=0（どの想定相手のbest選出にも入らない枠）→ pick_rate改善する代替へ
 (2) 穴: 上位30種に1v1で回答なし（有利を取れる味方が皆無）→ その相手に有利な代替へ
 (3) タイプ被り: 同一タイプが gen_party_pool.TYPEDUP_MAX 体超 → 減らす代替へ
env: NVER_OPP(4) NVER_K(8) NVER_NB(3) NVER_SWAP(12) HOLE_TOPN(30) SWAP_MARGIN(0.02)
"""
import os, random, numpy as np

NVER_OPP = int(os.environ.get("NVER_OPP", "4"))
NVER_K = int(os.environ.get("NVER_K", "8"))
NVER_NB = int(os.environ.get("NVER_NB", "3"))
NVER_SWAP = int(os.environ.get("NVER_SWAP", "12"))
SWAP_MARGIN = float(os.environ.get("SWAP_MARGIN", "0.02"))
HOLE_TOPN = int(os.environ.get("HOLE_TOPN", "30"))   # ポケモン相性の穴判定に使う上位相手数
NVER_TRY = int(os.environ.get("NVER_TRY", "3"))       # 代替案のうち pick_rate を測る上位件数
PICK_SLACK = float(os.environ.get("PICK_SLACK", "0"))  # 構成違反の修復時に許す最小pick低下幅
NVER_VICTIM = int(os.environ.get("NVER_VICTIM", "1"))  # 構成違反の修復で試す差し替え枠の数
NVER_RECHECK = int(os.environ.get("NVER_RECHECK", "1"))  # 採用後のENS再チェックの平均サンプル数

_HCOLS = None
def hole_mons(sp, L):
    """上位HOLE_TOPN種のうち、有利(1v1 score>=0.5)を取れる味方が1体もいない相手名の集合＝穴。"""
    global _HCOLS
    if _HCOLS is None:
        import _explain as E
        from simulator.battle import BattleField
        E._TOPB = None; E.load_top_builds.__defaults__ = (HOLE_TOPN, 1); E._OPPCOLS = None
        _HCOLS = (E._opp_columns(L), E._build, E._mu_score, BattleField())
    cols, _bd, _mu, fld = _HCOLS
    mons = [_bd(s, L) for s in sp]
    holes = set()
    for col in cols:
        if max(max(_mu(mo, v["p"], fld)["score"] for v in col["variants"]) for mo in mons) < 0.5:
            holes.add(col["label"])
    return holes


def pick_rates(pool, sp, opp_panel, seed0=142_000_000):
    """各枠の相手別best選出への登場率（greedyのみ・軽量）。pool=mp.Pool"""
    from _d1_guide import valid_subsets, bring_dist
    from _v3_rollout import _greedy_3v3
    subs = valid_subsets(sp)
    rates = np.zeros(6)
    for oi, op in enumerate(opp_panel):
        dist = bring_dist(op, sp, NVER_NB, ns=60, seed=seed0 + oi)
        jobs = [(sp, s, op, list(ob), int(seed0 + oi * 9973 + ri * 101 + ci * 7 + k) & 0x7fffffff)
                for ri, s in enumerate(subs) for ci, (ob, w) in enumerate(dist) for k in range(NVER_K)]
        res = pool.map(_greedy_3v3, jobs, chunksize=16)
        Mx = np.zeros((len(subs), len(dist))); D = np.zeros_like(Mx); idx = 0
        for ri in range(len(subs)):
            for ci in range(len(dist)):
                for k in range(NVER_K):
                    r = res[idx]; idx += 1
                    D[ri, ci] += 1 if r in (1, 2) else 0; Mx[ri, ci] += 1 if r == 1 else 0
        Mx = Mx / np.maximum(1, D)
        wts = np.array([w for _, w in dist])
        best = int(np.argmax(Mx @ wts))
        for j in subs[best]: rates[j] += 1
    return rates / len(opp_panel)


def repair_party(sp, pg, L, th, ens, pool, opp_panel, fixed_keys, rng):
    """1党を検証・修復して返す (new_sp, info)。fixed_keys=差し替え禁止のコア種。
    2つの必然性課題を同一枠組みで修復（ENS非劣化かつ悪化させない範囲で）:
      (1) 死に枠: pick_rate=0 の枠 → pick_rate改善する代替へ
      (2) 穴: 上位30種に回答なし → その相手に有利を取れる代替へ（穴を減らす）
    victim=死に枠優先、無ければ穴があるとき最低pick_rate枠。"""
    from _product3_complete import complete_core
    from gen_party_pool import TYPEDUP_MAX
    names = [s.split("@")[0] for s in sp]
    keys = [pg.keyof(s) or names[i] for i, s in enumerate(sp)]
    rates = pick_rates(pool, sp, opp_panel)
    base_ens = ens.score(sp)
    base_holes = hole_mons(sp, L)
    dead = [i for i in range(6) if rates[i] == 0 and keys[i] not in fixed_keys]

    _ATK_ROLES = {"スカーフ掃除役", "積みエース", "メガ積みエース", "メガエース",
                  "物理アタッカー", "特殊アタッカー"}

    def _role_bucket(roles):
        """役割を「攻め」「補助」の大分類にまとめる。role_of のラベルは粒度が細かく、
        アシレーヌ(積みエース)とマリルリ(物理アタッカー)が別扱いになってしまうが、
        両方ともみず/フェアリーの攻め駒で役割は重なる。逆にバチンウニ(設置)とMライチュウ(メガエース)は
        フィールドを張る側と乗る側で噛み合うので分けたい。"""
        b = set()
        for r in roles:
            b.add("攻" if r in _ATK_ROLES else "補")
        return b

    def _mega_shared_excess(party):
        """メガ2体の共有弱点が MEGA_SHARED_MAX を超えた分。1つの技で両方に抜群＝メガ2枚の意味が薄い。"""
        import itertools as _it, os as _os
        lim = int(_os.environ.get("SUGGEST_MEGA_SHARED_MAX", "0"))
        if not lim:
            return 0
        try:
            from _party_quality import mon_profile as _mp
            from gen_party_pool import _spec_mega as _sm
        except Exception:
            return 0
        ms = [x for x in party if _sm(x)]
        n = 0
        for a, b in _it.combinations(ms, 2):
            try:
                if len(_mp(a, L)[1] & _mp(b, L)[1]) > lim:
                    n += 1
            except Exception:
                pass
        return n

    def _role_dup_pairs(party):
        """役割ラベルが完全一致し、タイプを共有し、弱点も2つ以上重なる組の数。
        「ほのおの受けが2枚」のような実質同一の駒を検出する（ラウドボーン＋ウルガモス）。
        タイプ完全一致だけでは、タイプが違うのに同じ仕事をする駒を拾えなかった。
        判定基準は実上位307構築と生成物で比較して決めた:
          役割ラベル一致のみ        実上位54% / 生成66%  → 広すぎる
          ＋タイプ1つ共有          実上位 7% / 生成20%  → アシレーヌ+ミミッキュ(弱点共有0)まで拾う
          ＋弱点共有2以上(採用)     実上位 3% / 生成 3%  → 実データと同水準
        """
        import itertools as _it
        try:
            import _explain as _EX3
            from _party_quality import mon_profile as _mp
        except Exception:
            return 0
        n = 0
        for a, b in _it.combinations(party, 2):
            try:
                if tuple(sorted(_EX3.role_of(a, L))) != tuple(sorted(_EX3.role_of(b, L))):
                    continue
                if not (set(pg._types_of_spec(a)) & set(pg._types_of_spec(b))):
                    continue
                if len(_mp(a, L)[1] & _mp(b, L)[1]) >= 2:
                    n += 1
            except Exception:
                pass
        return n

    def _same_type_pairs(party):
        """タイプ構成が完全一致し、かつ役割も重なる味方の組の過剰数。
        TYPEDUP_MAX=2 では「みず2・フェアリー2」＝上限内となり、アシレーヌ＋マリルリのような
        完全一致ペアを一切検出できなかった。
        ただしタイプ一致だけでは粗い。バチンウニ(エレキメイカー・設置)＋Mライチュウ(メガエース)は
        フィールドを張る側と乗る側でシナジーがあり問題ない。対してアーマーガア(受け)＋エアームド(受け)は
        技も3/4一致で完全な役割重複。役割集合が交わる場合だけ違反と数える。"""
        import collections as _c
        try:
            import _explain as _EX
        except Exception:
            _EX = None
        groups = _c.defaultdict(list)
        for x in party:
            groups[tuple(sorted(pg._types_of_spec(x)))].append(x)
        n = 0
        for _t, mem in groups.items():
            if len(mem) < 2:
                continue
            if _EX is None:
                n += len(mem) - 1; continue
            try:
                from _party_quality import mon_profile as _mpq
            except Exception:
                _mpq = None
            roles = [_role_bucket(_EX.role_of(x, L)) for x in mem]
            for i in range(len(mem)):
                for j in range(i + 1, len(mem)):
                    # 役割の大分類が重なる、または弱点まで完全一致（役割が違っても代替が利く）
                    same_w = False
                    if _mpq is not None:
                        try:
                            same_w = _mpq(mem[i], L)[1] == _mpq(mem[j], L)[1]
                        except Exception:
                            pass
                    if (roles[i] & roles[j]) or same_w:
                        n += 1
        return n

    def _excess(party):
        """必然性上の構成違反数。タイプ被りの上限超過（gen_party_pool.TYPEDUP_MAX）＋完全一致ペア。"""
        ex = max(0, pg.type_dup_max(party) - TYPEDUP_MAX) if TYPEDUP_MAX else 0
        return ex + _same_type_pairs(party) + _role_dup_pairs(party) + _mega_shared_excess(party)

    base_ex = _excess(sp)
    if not dead and not base_holes and not base_ex:
        return sp, {"dead": [], "holes": 0, "typedup": 0, "swapped": None, "ens": base_ens,
                    "pick": [round(float(r), 2) for r in rates]}
    free = [i for i in range(6) if keys[i] not in fixed_keys]

    def _violation_slots():
        """構成違反（タイプ被り上限超過・役割が重なる完全一致ペア）を構成する枠。"""
        import collections as _c
        cnt = _c.Counter(t for x in sp for t in pg._types_of_spec(x))
        over = {t for t, v in cnt.items() if v > TYPEDUP_MAX}
        import _explain as _EX2
        _g = _c.defaultdict(list)
        for _x in sp:
            _g[tuple(sorted(pg._types_of_spec(_x)))].append(_x)
        dupsets = set()
        for _t, _mem in _g.items():
            if len(_mem) < 2:
                continue
            _r = [_role_bucket(_EX2.role_of(_x, L)) for _x in _mem]
            from _party_quality import mon_profile as _mpq2
            def _same_w(a, b):
                try: return _mpq2(a, L)[1] == _mpq2(b, L)[1]
                except Exception: return False
            if any((_r[i] & _r[j]) or _same_w(_mem[i], _mem[j])
                   for i in range(len(_mem)) for j in range(i + 1, len(_mem))):
                dupsets.add(_t)
        # 役割重複ペア（役割一致＋タイプ共有＋弱点2以上）を構成する枠も対象にする
        import itertools as _it3
        from _party_quality import mon_profile as _mp3
        rd = set()
        for _i, _j in _it3.combinations(range(6), 2):
            try:
                if tuple(sorted(_EX2.role_of(sp[_i], L))) != tuple(sorted(_EX2.role_of(sp[_j], L))):
                    continue
                if not (set(pg._types_of_spec(sp[_i])) & set(pg._types_of_spec(sp[_j]))):
                    continue
                if len(_mp3(sp[_i], L)[1] & _mp3(sp[_j], L)[1]) >= 2:
                    rd.update((_i, _j))
            except Exception:
                pass
        # メガ共有弱点が上限超過ならメガ枠も差し替え対象にする
        import os as _os4
        _lim = int(_os4.environ.get("SUGGEST_MEGA_SHARED_MAX", "0"))
        if _lim:
            from gen_party_pool import _spec_mega as _sm4
            _ms = [i for i in range(6) if _sm4(sp[i])]
            for _i, _j in _it3.combinations(_ms, 2):
                try:
                    if len(_mp3(sp[_i], L)[1] & _mp3(sp[_j], L)[1]) > _lim:
                        rd.update((_i, _j))
                except Exception:
                    pass
        return [i for i in free
                if (set(pg._types_of_spec(sp[i])) & over)
                or tuple(sorted(pg._types_of_spec(sp[i]))) in dupsets
                or i in rd]

    if dead and base_ex:
        # 死に枠と構成違反が同居する提案では、死に枠だけを見て違反を放置していた
        # （実測エースバーン軸: ウルガモス(死に枠)を差し替え、アーマーガア＋エアームドの
        #  役割重複はそのまま残った）。両方を候補にし、目的関数(穴削減,違反削減,最小pick)で選ぶ。
        _d = sorted(dead, key=lambda i: rates[i])[:1]
        _v = sorted(_violation_slots(), key=lambda i: rates[i])[:NVER_VICTIM]
        victims = list(dict.fromkeys(_d + _v))
    elif dead:
        victims = [min(dead, key=lambda i: rates[i])]
    elif base_ex:
        # 被り超過があるときは、超過タイプを持つ駒のうち最も選出されない枠を差し替える。
        # 一致ペアは2体とも差し替え候補にする（NVER_VICTIM件まで試す）。pick_rateが同値のとき
        # 先着だけ試して諦めていた（実測ボーマンダ軸: アシレーヌ0.33/マリルリ0.33で不成立）。
        cand = _violation_slots()
        victims = sorted(cand or free, key=lambda i: rates[i])[:NVER_VICTIM]
    else:
        victims = [min(free, key=lambda i: rates[i])]
    seen = {tuple(sorted(s.split("@")[0] for s in sp))}
    # 目的関数: (穴削減, 被り超過削減, 最小pick改善) をENS非劣化の中で最大化。タイブレークはENS。
    best_sp, best, best_victim = sp, (0, 0, min(rates), base_ens), victims[0]
    base_h = len(base_holes)
    cands = []
    for vi in victims:
        keep = [sp[i] for i in range(6) if i != vi]
        for a in complete_core(pg, L, th, keep, rng, NVER_SWAP):
            if tuple(sorted(s.split("@")[0] for s in a)) in seen: continue
            cands.append((ens.score(a), a, vi))
    scored = sorted(cands, key=lambda x: -x[0])[:NVER_TRY]
    for sc, a, vi in scored:
        if sc < base_ens - 0.03: continue            # ENS大幅劣化は却下
        ar = pick_rates(pool, a, opp_panel)
        # 新たな死に枠を作る差し替えは却下。ただし構成違反（被り上限超過・完全一致ペア）の修復時は
        # PICK_SLACK まで低下を許す。死に枠ゼロ・穴ゼロで最小pickが高い健全な党ほど
        # min(新)>=min(現) を満たす代替が無く、違反が一切直せなくなっていた（実測3件中0件成功）。
        slack = PICK_SLACK if base_ex and _excess(a) < base_ex else 0.0
        if min(ar) < min(rates) - slack - 1e-9: continue
        if min(ar) <= 1e-9 < min(rates): continue    # 死に枠を新設するのは常に却下
        dh = base_h - len(hole_mons(a, L))           # 穴の削減数（正=改善）
        dt = base_ex - _excess(a)                    # 被り超過の削減数（正=改善）
        if dt < 0: continue                          # 被りを増やす差し替えは却下
        cand_key = (dh, dt, min(ar), sc)
        # 採用条件: 穴を減らす or 被りを減らす or (どちらも同数で)最小pickを上げる。悪化は不可
        improves = dh > 0 or dt > 0 or (dh == 0 and dt == 0 and min(ar) > min(rates) + 1e-9)
        if improves and cand_key > best:
            best_sp, best, best_victim = a, cand_key, vi
            # 構成違反の修復は「穴を増やさず違反を消せた最初の案」で打ち切る。scoredはENS降順なので
            # これが最良ENSの解。全件のpick_rateを測るとNVER_TRYに比例して線形に重くなる。
            if base_ex and dt > 0 and dh >= 0:
                break
    # 事後チェック: ens.score は実行ごとに±0.03程度ぶれるため、採用判定時のサンプルが
    # たまたま高く出るとENSガード(-0.03)をすり抜ける（実測ボーマンダ軸#5: 0.431→0.359 = -0.072）。
    # 採用後に両者を測り直し、なお許容を超えて劣化していれば差し替えを取り消す。
    if best_sp is not sp:
        # ens.score の標準偏差は実測0.011。1サンプル同士だと差の標準偏差が0.016になり、
        # 真に-0.03劣化していても5割しか検出できない（実測で-0.063の見逃しあり）。
        def _avg(party):
            return sum(ens.score(party) for _ in range(NVER_RECHECK)) / NVER_RECHECK
        if _avg(best_sp) < _avg(sp) - 0.03:
            best_sp, best = sp, (0, 0, min(rates), base_ens)
    victim = best_victim
    swapped = None if best_sp is sp else names[victim]
    return best_sp, {"dead": [names[i] for i in dead], "holes": base_h, "victim": names[victim],
                     "swapped": swapped, "ens": base_ens, "ens_new": best[3],
                     "holes_new": base_h - best[0],
                     "typedup": pg.type_dup_max(sp), "typedup_new": pg.type_dup_max(best_sp),
                     "samepair": _same_type_pairs(sp), "samepair_new": _same_type_pairs(best_sp),
                     "min_pick": round(float(min(rates)), 2), "min_pick_new": round(float(best[2]), 2),
                     "pick": [round(float(r), 2) for r in rates]}
