"""Product3本体：コア固定・残り枠補完。
任意のポケ(コア)を固定→残り枠を同居率＋役割＋脅威カバレッジで補完→サロゲートで強い順にランキング。
使い方: venv/bin/python _product3_complete.py "サザンドラ@..." "メタグロス@..."   (specは簡略名でも可)
env NCAND(150) TOP(5)
"""
import os, sys, re, sqlite3, json, random, collections, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1
from gen_party_pool import (PartyGen, _spec_mega, _item_of, _ROLE_TARGET, _moves_of,
                             sample_role_targets, ROLE_W, ITEM_USAGE_W, IU_FLOOR, DBPATH)
from _threat_coverage import load_threats, team_coverage
import _product3 as P3

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
    for a in args:
        if isinstance(a, dict):
            sp, mega = a.get("sp"), a.get("mega")
            blds = pg.pool.get(sp)
            if not blds:
                raise SystemExit(f"プールに種 '{sp}' が無い")
            if mega is None:
                out.append(blds[0])
            elif mega == "":
                nm = [s for s in blds if not _spec_mega(s)]
                if not nm:
                    raise SystemExit(f"'{sp}' の非メガ型は使用率が低く未収録です（低使用率型の対応は準備中）")
                out.append(nm[0])
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
            out.append(blds[0])
    return out

def complete_core(pg, L, th, fixed_specs, rng, N):
    fixed_keys = [pg.keyof(s) or s.split("@")[0] for s in fixed_specs]
    fixed_map = dict(zip(fixed_keys, fixed_specs))
    fixed_dex = {pg.dex.get(k) for k in fixed_keys}
    fixed_mega = sum(_spec_mega(s) for s in fixed_specs)
    results = []; seen = set()
    guard = 0
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
        # 2メガをほぼ強制（前提ルール・2026-07-12）: 総当たり実勝率は1メガ/2メガでほぼ拮抗(0.502/0.495)だが、
        # これは両者フルインフォメーションの対戦AIによる測定＝「相手がどちらのメガ軸で来るか」という
        # チームプレビュー時の読み合い（1メガは相手に軸を確定させ対策を容易にする）を原理的に測れない。
        # 選出柔軟性＋読み合い優位（ユーザー判断）を前提ルールとして反映し、A/Bゲートは適用しない。
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
        rb = pg._role_builds(picked, holders, rng)
        if not rb: continue
        party = [fixed_map[k] if k in fixed_map else rb[i] for i, k in enumerate(picked)]
        if not pg.is_legal(party, megas_set=(1, 2)): continue
        if not _synergy_ok(party): continue
        key = tuple(sorted(party))
        if key in seen: continue
        seen.add(key); results.append(party)
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
    targets = targets or sample_role_targets(rng)
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
            iu = pg.item_usage.get(p, {})
            wts = [(iu.get(_item_of(b), 0) + 1) * pg._mvw(p, b) * (1 + ROLE_W * gain(b)) * payoff(b) for b in builds]
            if sum(wts) <= 0: wts = [(iu.get(_item_of(b), 0) + 1) * pg._mvw(p, b) * (1 + ROLE_W * gain(b)) for b in builds]
            chosen = rng.choices(builds, weights=wts, k=1)[0]
            party[p] = chosen; used_items.add(_item_of(chosen))
            for t in pg.build_roles.get(chosen, ()):
                if need.get(t, 0) > 0: need[t] -= 1
        if not ok: continue
        roles = sum(targets[t] - max(0, need[t]) for t in targets)
        usage = sum((pg.item_usage.get(p, {}).get(_item_of(party[p]), 0) + IU_FLOOR) * pg._mvw(p, party[p]) for p in picked) / 100.0
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
        party = rb
        if not pg.is_legal(party, megas_set=(1, 2)): continue
        key = tuple(sorted(party))
        if key in seen: continue
        seen.add(key); results.append(party)
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
