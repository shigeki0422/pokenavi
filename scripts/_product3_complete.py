"""Product3本体：コア固定・残り枠補完。
任意のポケ(コア)を固定→残り枠を同居率＋役割＋脅威カバレッジで補完→サロゲートで強い順にランキング。
使い方: venv/bin/python _product3_complete.py "サザンドラ@..." "メタグロス@..."   (specは簡略名でも可)
env NCAND(150) TOP(5)
"""
import os, sys, re, sqlite3, json, random, collections, statistics, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1
from gen_party_pool import (PartyGen, _spec_mega, _item_of, _ROLE_TARGET, _moves_of,
                             sample_role_targets, ROLE_W, ITEM_USAGE_W, IU_FLOOR, DBPATH, TYPEDUP_MAX)
from _threat_coverage import load_threats, team_coverage
import _product3 as P3
import gen_party_pool as _GP
import seed_rule

SEASON = "M-3"
NCAND = int(os.environ.get("NCAND", "150"))
TOP = int(os.environ.get("TOP", "5"))
MAX_RANK = int(os.environ.get("MAX_RANK", "80"))   # 補完に使う種の使用率順位上限（コアは対象外）
MEGA2_PROB = float(os.environ.get("MEGA2_PROB", "0.95"))   # 2メガ目標の確率（前提ルール・2026-07-12）

def resolve_fixed(pg, args):
    """コア指定を pool の代表 spec に解決。
    各要素は次のいずれか:
      - {"sp": 種名, "mega": None|""|"○○ナイトX"}  … Noneは自動(メガ優先)、""は非メガ、文字列は該当メガ石
      - "種名@..." フル spec
      - "種名"（=メガ優先の先頭型）
    """
    out = []
    alts = []   # 自動で選んだ枠の代わりの候補（持ち物が他の固定枠と重なったときに使う）
    auto = []   # メガの有無を自動で選んだ枠の種キー（メガが上限を超えたら・タイプが重なったら替えてよい枠）
    for a in args:
        alts.append(None); auto.append(None)
        if isinstance(a, dict):
            sp, mega = a.get("sp"), a.get("mega")
            if mega is None: auto[-1] = sp
            blds = pg.pool.get(sp)
            if not blds:
                raise SystemExit(f"プールに種 '{sp}' が無い")
            if mega is None:
                out.append(blds[0]); alts[-1] = [s for s in blds if _spec_mega(s) == _spec_mega(blds[0])]
            elif mega == "":
                nm = [s for s in blds if not _spec_mega(s)]
                if not nm:
                    raise SystemExit(f"'{sp}' の非メガ型は使用率が低く未収録です（低使用率型の対応は準備中）")
                out.append(nm[0]); alts[-1] = nm
            else:
                mm = [s for s in blds if _spec_mega(s) and _item_of(s) == mega]
                if not mm:
                    raise SystemExit(f"'{sp}' の {mega} 型は使用率が低く未収録です（低使用率型の対応は準備中）")
                out.append(mm[0])
        elif "@" in a:
            out.append(a)
        else:
            blds = pg.pool.get(a)
            if not blds:
                raise SystemExit(f"プールに種 '{a}' が無い")
            auto[-1] = a
            out.append(blds[0]); alts[-1] = [s for s in blds if _spec_mega(s) == _spec_mega(blds[0])]
    # 持ち物は1パーティで重複できないので、自動で選んだ枠の持ち物が先の枠と重なったら次点の型に替える
    # （例: カバルドン＋ブリジュラスがどちらも先頭型オボンのみ→合法なパーティが1件も作れなかった）
    used = set()
    for i, sp in enumerate(out):
        it = _item_of(sp)
        if it in used and alts[i]:
            alt = next((x for x in alts[i] if _item_of(x) not in used), None)
            if alt is not None:
                out[i] = sp = alt; it = _item_of(sp)
        used.add(it)
    # 自動で選んだ枠のシードは、指定の中に設置役がいなければ同じ形の別の持ち物の型に替える（seed_rule）
    for i in seed_rule.violations(out):
        if alts[i]:
            others = {_item_of(x) for j, x in enumerate(out) if j != i}
            alt = next((x for x in alts[i] if _item_of(x) not in others
                        and i not in seed_rule.violations(out[:i] + [x] + out[i + 1:])), None)
            if alt is not None:
                out[i] = alt
    out = _fit_fixed(pg, out, auto)
    why = infeasible_reason(pg, out)
    if why:
        raise SystemExit(why)
    return out


def _fit_fixed(pg, out, auto):
    """メガの有無を自動で選んだ枠を、条件（メガ2体まで・持ち物・タイプの重なり）に合うよう替える。
    メガが上限を超えたら使用率の低い方から非メガの型へ。それでもタイプが重なるなら、自動の枠の形（非メガ／メガ石ごと）を替える
    組み合わせを、替える枠の少ない順に探す（同数なら使用率の低い枠を替える方を先に）。合う組み合わせが無ければそのまま
    （理由は infeasible_reason が返す）"""
    import itertools
    form = lambda b: _item_of(b) if _spec_mega(b) else ""
    def forms(i, cur, others):
        """枠 i の今と違う形の型（形ごとに先頭・持ち物が他と重ならないもの）"""
        used = {_item_of(x) for x in others}
        res = {}
        for b in pg.pool.get(auto[i], []):
            f = form(b)
            if f != form(cur) and f not in res and _item_of(b) not in used:
                res[f] = b
        return list(res.values())
    out = list(out)
    megas = sum(bool(_spec_mega(x)) for x in out)
    if megas > MEGA_MAX:
        for i in sorted([i for i, a in enumerate(auto) if a and _spec_mega(out[i])],
                        key=lambda i: -pg.rank.get(auto[i], 9999)):
            if megas <= MEGA_MAX:
                break
            nm = [b for b in forms(i, out[i], out[:i] + out[i + 1:]) if not _spec_mega(b)]
            if nm:
                out[i] = nm[0]; megas -= 1
    if infeasible_reason(pg, out) is None:
        return out
    idx = [i for i, a in enumerate(auto) if a]
    for k in range(1, len(idx) + 1):
        for comb in sorted(itertools.combinations(idx, k), key=lambda c: -sum(pg.rank.get(auto[i], 9999) for i in c)):
            def rec(n, cand):
                if n == len(comb):
                    return cand if infeasible_reason(pg, cand) is None else None
                i = comb[n]
                for b in forms(i, cand[i], cand[:i] + cand[i + 1:]):
                    r = rec(n + 1, cand[:i] + [b] + cand[i + 1:])
                    if r is not None:
                        return r
                return None
            r = rec(0, list(out))
            if r is not None:
                return r
    return out


# 残り枠の生成方式（2026-10-01）: weighted＝条件を満たす型だけから引く（既定）、legacy＝引いてから確かめて捨てる（旧方式）
GEN_MODE = os.environ.get("GEN_MODE", "weighted")
# weighted で、引いた種・メガの有無のまま型を役割目標で選び直す（_role_builds。旧方式と同じ型の選び方）
GEN_ROLE_REFINE = os.environ.get("GEN_ROLE_REFINE", "1") == "1"
MEGA_MAX = 2


def _type_names(pg, spec):
    return pg._types_of_spec(spec)


def _build_probs(pg, p):
    """種 p の型確率: pg.build_weight（型プールは型の重み、md は（持ち物の使用率+1）×技構成の使用率）を種内で正規化（_role_builds の役割を除いた重みと同じ）。
    返り値 [(spec, 確率, メガか, 持ち物, タイプ), ...]"""
    cache = pg.__dict__.setdefault("_bp_cache", {})
    if p not in cache:
        bs = pg.pool.get(p, [])
        ws = [pg.build_weight(p, b) for b in bs]
        t = sum(ws) or 1.0
        cache[p] = [(b, w / t, bool(_spec_mega(b)), _item_of(b), _type_names(pg, b)) for b, w in zip(bs, ws)]
    return cache[p]


def _build_ok(info, used_items, tcount, megas, m, rem_after):
    """型が今の条件（使用済みの持ち物・タイプの重なり上限・メガの残り枠・最後までにメガを m 体にできるか）を満たすか"""
    _, _, mg, it, ty = info
    if it in used_items:
        return False
    if TYPEDUP_MAX and any(tcount[t] + 1 > TYPEDUP_MAX for t in ty):
        return False
    if mg:
        return megas + 1 <= m
    return m - megas <= rem_after


def _species_tables(pg):
    """_species_base 用の前計算（並びは pg.pokes／同居の並びのまま）: 補完対象の種 [(種, 図鑑, 使用率重み)]、
    種ごとの同居相手 [(相手, 図鑑, 重み)]（pg.w にあり順位内のものだけ）"""
    t = pg.__dict__.get("_sp_tables")
    if t is None or t[0] != MAX_RANK:
        inrank = lambda p: pg.rank.get(p, 9999) <= MAX_RANK
        cand = [(p, pg.dex.get(p), pg.w[p]) for p in pg.pokes if inrank(p)]
        nb = {q: [(pt, pg.dex.get(pt), w) for pt, w in d.items() if pt in pg.w and inrank(pt)] for q, d in pg.cooc.items()}
        t = pg._sp_tables = (MAX_RANK, cand, nb)
    return t[1], t[2]


def _species_base(pg, picked, used_dex):
    """次の種の選ばれやすさ（今の使用率ベースの重み）: 同居の重み 70%＋使用率の重み 30%（旧方式の抽選の周辺分布）"""
    cand_all, nb = _species_tables(pg)
    cand = [(p, w) for p, d, w in cand_all if d not in used_dex]
    neigh = collections.Counter()
    for q in picked:
        for pt, d, w in nb.get(q, ()):
            if d not in used_dex:
                neigh[pt] += w
    W = sum(w for _, w in cand) or 1.0
    if not neigh:
        return {p: w / W for p, w in cand}
    Nn = sum(neigh.values())
    return {p: 0.3 * w / W + 0.7 * neigh.get(p, 0) / Nn for p, w in cand}


def _fixed_state(pg, fixed_specs):
    used_items = {_item_of(s) for s in fixed_specs}
    tcount = collections.Counter(t for s in fixed_specs for t in _type_names(pg, s))
    return used_items, tcount, sum(bool(_spec_mega(s)) for s in fixed_specs)


def sample_weighted(pg, fixed_keys, fixed_specs, rng, m):
    """残り枠を「条件を満たす型だけ」から順に引く。種の重み＝使用率ベースの重み×（条件を満たす型の確率の合計）、
    型はその中で確率を正規化して引く。設置役のいないシードは同じ種の別の持ち物の型に替える（seed_rule）。
    行き止まり（どの種も条件を満たせない・シードを替えられない）なら None。返り値 (picked, {種: 型})"""
    picked = list(fixed_keys)
    used_dex = {pg.dex.get(k) for k in fixed_keys}
    used_items, tcount, megas = _fixed_state(pg, fixed_specs)
    chosen = {}
    while len(picked) < 6:
        rem_after = 6 - len(picked) - 1
        base = _species_base(pg, picked, used_dex)
        # _build_ok と同じ判定。この枠で一定の部分（メガ可否・上限に達したタイプ）を先に決めておく
        ok_mega, ok_non = megas + 1 <= m, m - megas <= rem_after
        full_t = {t for t, c in tcount.items() if c + 1 > TYPEDUP_MAX} if TYPEDUP_MAX else set()
        sps, wts, valid = [], [], {}
        for p, bw in base.items():
            v = [x for x in _build_probs(pg, p)
                 if (ok_mega if x[2] else ok_non) and x[3] not in used_items and full_t.isdisjoint(x[4])]
            mass = sum(x[1] for x in v)
            if mass > 0 and bw > 0:
                sps.append(p); wts.append(bw * mass); valid[p] = v
        if not sps:
            return None
        p = rng.choices(sps, weights=wts, k=1)[0]
        v = valid[p]
        info = rng.choices(v, weights=[x[1] for x in v], k=1)[0]
        b, _, mg, it, ty = info
        chosen[p] = b; picked.append(p); used_dex.add(pg.dex.get(p)); used_items.add(it)
        for t in ty:
            tcount[t] += 1
        megas += mg
    nfix = len(fixed_keys)
    party = list(fixed_specs) + [chosen[k] for k in picked[nfix:]]
    if seed_rule.violations(party, fixed_specs):
        party = pg.fix_seeds(party, rng, keep=set(fixed_specs))
        if party is None or seed_rule.violations(party, fixed_specs):
            return None
        chosen = dict(zip(picked[nfix:], party[nfix:]))
    return picked, chosen


def infeasible_reason(pg, fixed_specs):
    """種族の時点で作れない指定の理由（フロントに出す文言）。作れるなら None"""
    names = [s.split("@")[0] for s in fixed_specs]
    dex = [pg.dexof(s) for s in fixed_specs]
    if len(set(dex)) != len(dex):
        return "同じポケモン（リージョンフォーム・性別違いを含む）は1パーティに1体までです。"
    megas = sum(bool(_spec_mega(s)) for s in fixed_specs)
    if megas > MEGA_MAX:
        return f"メガシンカの型は1パーティ{MEGA_MAX}体までです（指定に{megas}体含まれています）。"
    items = collections.Counter(_item_of(s) for s in fixed_specs)
    dup = [it for it, c in items.items() if c > 1]
    if dup:
        return f"持ち物「{dup[0]}」が重なっています（同じ持ち物は1パーティに1つまでです）。"
    if TYPEDUP_MAX:
        tc = collections.Counter(t for s in fixed_specs for t in _type_names(pg, s))
        over = [(t, c) for t, c in tc.items() if c > TYPEDUP_MAX]
        if over:
            t, c = over[0]
            who = "・".join(n for n, s in zip(names, fixed_specs) if t in _type_names(pg, s))
            return f"{who} で {t}タイプが{c}体になります（同じタイプは{TYPEDUP_MAX}体までです）。"
    if len(fixed_specs) >= 6:
        return None if megas >= 1 else "メガシンカの型が1体も入っていません（1パーティ1〜2体）。"
    fixed_keys = [pg.keyof(s) or s.split("@")[0] for s in fixed_specs]
    used_dex = set(dex)
    used_items, tcount, _ = _fixed_state(pg, fixed_specs)
    rem_after = 6 - len(fixed_specs) - 1
    base = _species_base(pg, fixed_keys, used_dex)
    for m in sorted({max(megas, 1), max(megas, 2)}):
        if any(_build_ok(x, used_items, tcount, megas, m, rem_after) for p in base for x in _build_probs(pg, p)):
            return None
    return "この組み合わせでは残りの枠に入れられるポケモンがいません（タイプの重なり・持ち物・メガシンカの枠の条件）。"


def _seed_fix(pg, party, rng, fixed_specs):
    """設置役のいないシードを固定枠以外で同じ種の別の持ち物の型に替える（替えられなければそのまま＝is_legal で落ちる）"""
    return pg.fix_seeds(party, rng, keep=set(fixed_specs)) or party


def complete_core(pg, L, th, fixed_specs, rng, N, dedupe=True, strict=False):
    """固定軸 fixed_specs の残り枠を補完した候補パーティを最大 N 件。GEN_MODE=weighted（既定）は条件を満たす型だけから引く。
    作れない指定は strict なら SystemExit（理由つき・フロントに出す文言）、でなければ []"""
    if GEN_MODE == "legacy":
        return complete_core_legacy(pg, L, th, fixed_specs, rng, N, dedupe)
    why = infeasible_reason(pg, fixed_specs)
    if why:
        if strict:
            raise SystemExit(why)
        print(f"[gen] 作れない指定: {why}", flush=True)
        return []
    fixed_keys = [pg.keyof(s) or s.split("@")[0] for s in fixed_specs]
    fixed_map = dict(zip(fixed_keys, fixed_specs))
    fixed_mega = sum(bool(_spec_mega(s)) for s in fixed_specs)
    results = []; seen = set(); guard = 0
    rej = collections.Counter()
    t_rb = 0.0; t_all = time.perf_counter()
    while len(results) < N and guard < N * 30:
        guard += 1
        m = max(fixed_mega, 2 if rng.random() < MEGA2_PROB else 1)
        r = sample_weighted(pg, fixed_keys, fixed_specs, rng, m)
        if r is None:
            rej["行き止まり"] += 1; continue
        picked, chosen = r
        party = [fixed_map[k] if k in fixed_map else chosen[k] for k in picked]
        if GEN_ROLE_REFINE:
            holders = {k for k in picked if _spec_mega(fixed_map.get(k) or chosen[k])}
            _t0 = time.perf_counter()
            rb = pg._role_builds(picked, holders, rng, fixed=fixed_map)
            t_rb += time.perf_counter() - _t0
            if rb and pg.is_legal(rb, megas_set=(1, 2), seed_exempt=fixed_specs):
                party = rb
            else:
                rej["役割の選び直し失敗(引いた型のまま)"] += 1
        party = _seed_fix(pg, party, rng, fixed_specs)
        if not pg.is_legal(party, megas_set=(1, 2), seed_exempt=fixed_specs):
            rej["非合法"] += 1; continue
        if not _synergy_ok(party): rej["シナジー不足"] += 1; continue
        key = tuple(sorted(party))
        if dedupe and key in seen: rej["重複"] += 1; continue
        seen.add(key); results.append(party)
    print(f"[gen] mode=weighted fixed={len(fixed_specs)} N={N} got={len(results)} try={guard} "
          f"total={time.perf_counter()-t_all:.1f}s role_builds={t_rb:.1f}s rej={dict(rej.most_common())}", flush=True)
    if not results and strict:
        raise SystemExit("この組み合わせでは条件（タイプの重なり・持ち物・メガシンカの枠）を満たすパーティが作れませんでした。")
    return results


def complete_core_legacy(pg, L, th, fixed_specs, rng, N, dedupe=True):
    """旧方式（引いてから確かめて捨てる）。照合用に残す（GEN_MODE=legacy）"""
    fixed_keys = [pg.keyof(s) or s.split("@")[0] for s in fixed_specs]
    fixed_map = dict(zip(fixed_keys, fixed_specs))
    fixed_dex = {pg.dex.get(k) for k in fixed_keys}
    fixed_mega = sum(_spec_mega(s) for s in fixed_specs)
    results = []; seen = set()
    guard = 0
    rej = collections.Counter()   # 棄却理由の内訳（費用のほぼ全額が本関数なので常時計測する）
    t_rb = [0.0]; t_all = time.perf_counter()
    while len(results) < N and guard < N * 30:
        guard += 1
        picked = list(fixed_keys); used_dex = set(fixed_dex); ok = True
        inrank = lambda p: pg.rank.get(p, 9999) <= MAX_RANK
        while len(picked) < 6:
            neigh = collections.Counter()
            for q in picked:
                for pt, w in pg.cooc.get(q, {}).items():
                    if pt in pg.w and pg.dex.get(pt) not in used_dex and inrank(pt): neigh[pt] += w
            if neigh and rng.random() < 0.7:
                cs = list(neigh); nxt = rng.choices(cs, weights=[neigh[c] for c in cs], k=1)[0]
            else:
                cand = [p for p in pg.pokes if pg.dex.get(p) not in used_dex and inrank(p)]
                if not cand: ok = False; break
                nxt = rng.choices(cand, weights=[pg.w[p] for p in cand], k=1)[0]
            picked.append(nxt); used_dex.add(pg.dex.get(nxt))
        if not ok: rej['候補枯渇'] += 1; continue
        # 2メガをほぼ強制（前提ルール・2026-07-12）: 総当たり実勝率は1メガ/2メガでほぼ拮抗(0.502/0.495)だが、
        # これは両者フルインフォメーションの対戦AIによる測定＝「相手がどちらのメガ軸で来るか」という
        # チームプレビュー時の読み合い（1メガは相手に軸を確定させ対策を容易にする）を原理的に測れない。
        # 選出柔軟性＋読み合い優位（ユーザー判断）を前提ルールとして反映し、A/Bゲートは適用しない。
        holders = set(k for k in fixed_keys if _spec_mega(fixed_map[k]))
        nonfixed = [p for p in picked if p not in fixed_keys]
        # 非メガ型がプールに無い種は、メガ担当に選ばれなければ党ごと捨てるしかない。
        # かつては抽選任せで、外れるたびに棄却していた（実測で棄却の72%＝1722/2385回）。
        # 最初からメガ担当に確定させれば同じ党を捨てずに済む。
        holders |= {p for p in nonfixed if pg.mega.get(p) and not pg.nonm.get(p)}
        if any(not pg.mega.get(p) and not pg.nonm.get(p) for p in nonfixed):
            rej['型なし'] += 1; continue
        megas = max(fixed_mega, len(holders), 2 if rng.random() < MEGA2_PROB else 1)
        if megas > 2: rej['メガ3体以上'] += 1; continue
        need = megas - len(holders)
        cap = [p for p in nonfixed if pg.mega.get(p) and p not in holders]
        if need > 0:
            if len(cap) < need: rej['メガ石不足'] += 1; continue
            holders |= set(rng.sample(cap, need))
        # タイプは「種＋メガ有無」で決まるため、型を割り当てる前に判定できる。
        # _role_builds は gen 時間の96%を占める最重量処理なので、ここで先に弾く。
        if TYPEDUP_MAX:
            proto = [fixed_map[k] if k in fixed_map else (pg.mega[k][0] if k in holders else pg.nonm[k][0])
                     for k in picked]
            if pg.type_dup_max(proto) > TYPEDUP_MAX:
                rej['タイプ被り(事前)'] += 1; continue
        _t0 = time.perf_counter()
        # 固定軸を渡さないと、その持ち物を知らないまま型を選んで後から差し込むことになり、
        # 持ち物重複で党ごと捨てていた（実測225/1732回）。_role_builds 側で除外させる。
        rb = pg._role_builds(picked, holders, rng, fixed=fixed_map)
        t_rb[0] += time.perf_counter() - _t0
        if not rb: rej['型割当失敗'] += 1; continue
        party = _seed_fix(pg, [fixed_map[k] if k in fixed_map else rb[i] for i, k in enumerate(picked)], rng, fixed_specs)
        if not pg.is_legal(party, megas_set=(1, 2), seed_exempt=fixed_specs):
            if pg.type_dup_max(party) > 2: rej['非合法:タイプ被り'] += 1
            elif len({_item_of(x) for x in party}) != 6: rej['非合法:持ち物重複'] += 1
            elif not seed_rule.ok(party, fixed_specs): rej['非合法:設置役のいないシード'] += 1
            else: rej['非合法:その他'] += 1
            continue
        if not _synergy_ok(party): rej['シナジー不足'] += 1; continue
        key = tuple(sorted(party))
        if dedupe and key in seen: rej['重複'] += 1; continue
        seen.add(key); results.append(party)
    print(f"[gen] fixed={len(fixed_specs)} N={N} got={len(results)} try={guard} "
          f"total={time.perf_counter()-t_all:.1f}s role_builds={t_rb[0]:.1f}s "
          f"rej={dict(rej.most_common())}", flush=True)
    return results


# 天候始動役のうち「単体では弱く、シナジーがあって初めて価値が出る」ことを実測した種は、
# 味方がその天候のペイオフを提供する党でのみ採用する。実測（_standalone/, MCTS採点 n=18文脈）:
#   ペリッパー: シナジー無 -3.54pt[-5.03,-1.91] / 有 +1.75pt / 差 +5.29pt[+2.41,+8.13]
# 一律に「天候始動役は受け手必須」とすると誤爆する（リザードンは晴れの有無で価値が変わらず +0.07pt、
# カバルドン/バンギラスは砂の受け手がプールに0種）ため、対象は実測で条件を満たした種に限定する。
# 特性による始動（あめふらし等）は _role_builds の payoff ゲート（技ベース）では捕まえられない
# ＝全ての型が同じ特性を持つので型の選び直しでは回避できない。よってここ（党の合否）で判定する。
SYNERGY_REQUIRED = {"ペリッパー": ("rain", 2)}   # 種 → (天候, 必要ペイオフ)
SYNERGY_GATE = os.environ.get("SYNERGY_GATE", "0") == "1"


def _synergy_ok(party):
    if not SYNERGY_GATE: return True
    try:
        import _synergy_feat as _SF
    except Exception:
        return True          # 特徴モジュールが無い環境では素通し（生成を止めない）
    for i, s in enumerate(party):
        req = SYNERGY_REQUIRED.get(s.split("@")[0])
        if not req: continue
        w, need = req
        if _SF.party_weather_payoff(party, w, exclude=i) < need: return False
    return True

_DEX_FULL = {}   # 種名→図鑑番号（型プール非所属の種もDB全体から解決。遅延ロード・プロセス内キャッシュ）

def _resolve_dex(pg, name):
    """種名→図鑑番号。pg.dex（型プール所属種のみ）に無ければDB全種から解決（フォームは基底名一致でも可）。
    それでも解決不能なら種固有の疑似キー("X:"+name)にフォールバックし、少なくとも同名同士の重複判定はできる形にする。"""
    if name in pg.dex:
        return pg.dex[name]
    if not _DEX_FULL:
        con = sqlite3.connect(DBPATH)
        for nm, pid in con.execute("SELECT DISTINCT pokemon,pokemon_id FROM pokemon_usage WHERE pokemon_id IS NOT NULL"):
            if pid and len(pid) >= 4:
                _DEX_FULL.setdefault(nm, pid[:4])
        con.close()
    if name in _DEX_FULL:
        return _DEX_FULL[name]
    base = lambda n: re.split(r"[（(:：]", n)[0].strip()
    bn = base(name)
    for nm, d in _DEX_FULL.items():
        if base(nm) == bn:
            return d
    return "X:" + name

def _role_builds_ext(pg, picked, fixed_map, holders, rng, tries=120, targets=None):
    """_role_builds() の固定メンバー対応版。fixed_map にある種は型選択をスキップし既存specをそのまま使う
    （型プール非所属でも可）。役割目標の充足・持ち物の重複回避は固定メンバーの分も考慮したうえで、
    新規に埋める種にのみ型を選ぶ。返り値は picked と同順の6spec（fixedはそのまま・新規は選定結果）。"""
    targets = targets or (_GP.sample_role_targets_pool(rng) if pg.src == "pool" else sample_role_targets(rng))
    new_p = [p for p in picked if p not in fixed_map]
    has_slow_ace = any(pg._traits(q, q in holders)[0] for q in picked)
    has_rain = any(pg._traits(q, q in holders)[1] for q in picked)
    def payoff(b):
        mv = _moves_of(b)
        if "トリックルーム" in mv and not has_slow_ace: return 0.0
        if "あまごい" in mv and not has_rain: return 0.0
        return 1.0
    fixed_items = {_item_of(fixed_map[p]) for p in picked if p in fixed_map}
    fixed_roles = collections.Counter()
    for p in picked:
        if p in fixed_map:
            for t in pg._role_tags(fixed_map[p]):
                fixed_roles[t] += 1
    base_need = {t: max(0, targets.get(t, 0) - fixed_roles.get(t, 0)) for t in targets}
    best = None; best_score = -1
    for _ in range(tries):
        order = list(new_p); rng.shuffle(order)
        party = dict(fixed_map); used_items = set(fixed_items); need = dict(base_need); ok = True
        for p in order:
            builds = [b for b in (pg.mega[p] if p in holders else pg.nonm[p]) if _item_of(b) not in used_items]
            if not builds: ok = False; break
            def gain(b):
                return sum(1 for t in pg.build_roles.get(b, ()) if need.get(t, 0) > 0)
            wts = [pg.build_weight(p, b) * (1 + pg.role_w * gain(b)) * payoff(b) for b in builds]
            if sum(wts) <= 0: wts = [pg.build_weight(p, b) * (1 + pg.role_w * gain(b)) for b in builds]
            chosen = rng.choices(builds, weights=wts, k=1)[0]
            party[p] = chosen; used_items.add(_item_of(chosen))
            for t in pg.build_roles.get(chosen, ()):
                if need.get(t, 0) > 0: need[t] -= 1
        if not ok: continue
        roles = sum(targets[t] - max(0, need[t]) for t in targets)
        usage = sum(pg._rb_info(p, party[p])[4] for p in picked) / 100.0
        score = roles + ITEM_USAGE_W * usage
        if score > best_score:
            best_score = score; best = [party[p] for p in picked]
            if score == sum(targets.values()): break
    return best

def complete_core_free(pg, L, th, fixed_specs, rng, N):
    """complete_core() のプール非所属対応版：fixed_specs（任意のspec文字列。型プールに無くてもよい）を
    固定メンバーとしてそのまま採点に使い、残り(6-len(fixed_specs))枠をプールから補完する。
    図鑑番号・持ち物の重複判定は _resolve_dex() でプール非所属種も含めて行う。"""
    fixed_keys = [s.split("@")[0] for s in fixed_specs]
    fixed_map = dict(zip(fixed_keys, fixed_specs))
    fixed_dex = [_resolve_dex(pg, k) for k in fixed_keys]
    fixed_mega = sum(_spec_mega(s) for s in fixed_specs)
    if len(set(fixed_dex)) != len(fixed_dex) or fixed_mega > 2:
        return []   # 固定メンバー自体が既に非合法（種重複／メガ3体以上）
    results = []; seen = set()
    guard = 0
    rej = collections.Counter()   # 棄却理由の内訳（費用のほぼ全額が本関数なので常時計測する）
    while len(results) < N and guard < N * 30:
        guard += 1
        picked = list(fixed_keys); used_dex = set(fixed_dex); ok = True
        inrank = lambda p: pg.rank.get(p, 9999) <= MAX_RANK
        while len(picked) < 6:
            neigh = collections.Counter()
            for q in picked:
                for pt, w in pg.cooc.get(q, {}).items():
                    if pt in pg.w and pg.dex.get(pt) not in used_dex and inrank(pt): neigh[pt] += w
            if neigh and rng.random() < 0.7:
                cs = list(neigh); nxt = rng.choices(cs, weights=[neigh[c] for c in cs], k=1)[0]
            else:
                cand = [p for p in pg.pokes if pg.dex.get(p) not in used_dex and inrank(p)]
                if not cand: ok = False; break
                nxt = rng.choices(cand, weights=[pg.w[p] for p in cand], k=1)[0]
            picked.append(nxt); used_dex.add(pg.dex.get(nxt))
        if not ok: continue
        megas = max(fixed_mega, 2 if rng.random() < MEGA2_PROB else 1)
        if megas > 2: continue
        holders = set(k for k in fixed_keys if _spec_mega(fixed_map[k]))
        nonfixed = [p for p in picked if p not in fixed_keys]
        need = megas - len(holders)
        cap = [p for p in nonfixed if pg.mega.get(p)]
        if need > 0:
            if len(cap) < need: continue
            holders |= set(rng.sample(cap, need))
        if any(p not in holders and not pg.nonm.get(p) for p in nonfixed): continue
        rb = _role_builds_ext(pg, picked, fixed_map, holders, rng)
        if not rb: continue
        party = _seed_fix(pg, rb, rng, fixed_specs)
        if not pg.is_legal(party, megas_set=(1, 2), seed_exempt=fixed_specs): continue
        key = tuple(sorted(party))
        if key in seen: continue
        seen.add(key); results.append(party)
    print(f"[gen] fixed={len(fixed_specs)} N={N} got={len(results)} try={guard} "
          f"rej={dict(rej.most_common())}", flush=True)
    return results

def main():
    args = sys.argv[1:]
    if not args:
        args = ["サザンドラ", "メタグロス"]   # デモ: サザングロスコア
    _f1._ensure_loaded(SEASON, 8); L = _f1._W["loader"]; net = _f1._W["net"]
    pg = PartyGen(); th = load_threats(L); rng = random.Random(0)
    fixed = resolve_fixed(pg, args)
    print(f"固定コア: {[s.split('@')[0] for s in fixed]}  残り{6-len(fixed)}枠を補完", flush=True)
    cands = complete_core(pg, L, th, fixed, rng, NCAND)
    print(f"補完候補 {len(cands)}体 生成。サロゲート評価...", flush=True)
    panel = [json.load(open('gen_pop_step1.json'))[i]["party"] for i in rng.sample(range(300), 24)]
    P3._score_setup(L, net, panel)
    scored = sorted(((P3.surrogate_score(p), p) for p in cands), key=lambda x: -x[0])
    EVK = ["H", "A", "B", "C", "D", "S"]
    print(f"\n■ 補完結果 上位{TOP}（サロゲートスコア順）")
    for rk, (sc, p) in enumerate(scored[:TOP], 1):
        cov = team_coverage(p, L, th)[0]
        print(f"\n[{rk}] スコア{sc:.3f} 脅威対応{cov*100:.0f}%")
        for s in p:
            head, rest = s.split("@", 1); it, na, mv, ev, ab = rest.split(":")
            evs = " ".join(f"{k}{v}" for k, v in zip(EVK, ev.split("/")) if v != "0")
            fx = "◆" if head in [f.split("@")[0] for f in fixed] else ("★" if _spec_mega(s) else "　")
            print(f"  {fx}{head:<12} @{it:<12} {na:<5} {ab:<9} {evs:<18} {mv.replace('|',' / ')}")

if __name__ == "__main__":
    main()
