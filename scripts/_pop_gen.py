"""確率的パーティ生成器（M-3共進化の試作Step1）。
使用率(ランク)＋同居率(ランク)＋条件付き分布(技/持ち物/性格/特性/EV)からパーティをサンプル。
合法性：6種別重複なし・メガ石は最大1。データが薄い項目は省略→build_from_spec のテンプレ既定にフォールバック。
"""
import sqlite3, random
from collections import defaultdict

DB = "pokenavi.db"; SEASON = "M-2"; RULE = "single"

def canon(name):
    """DBの揺れた表記を colon-free の正規名へ。'X:Y'→'X(Y)'、'X (Y)'→'X(Y)'。
    specの区切り':'と名前内':'の衝突を防ぎ、同一ポケモンの分断データを統合する。"""
    if not name: return name
    name = name.strip().replace(" (", "(")
    if ":" in name:
        b, f = name.split(":", 1); name = f"{b}({f})"
    return name

def load(db=DB, season=SEASON, rule=RULE):
    c = sqlite3.connect(db); c.row_factory = sqlite3.Row
    ubest = {}; dex = {}
    for r in c.execute("SELECT pokemon,rank,pokemon_id FROM pokemon_usage WHERE season=? AND rule=? ORDER BY rank", (season, rule)):
        p = canon(r["pokemon"])
        if p not in ubest: ubest[p] = r["rank"]           # 最良ランクで統合
        if p not in dex and r["pokemon_id"]: dex[p] = r["pokemon_id"][:4]   # 図鑑番号4桁(リージョン違いは同dex)
    usage = sorted(ubest.items(), key=lambda x: x[1])
    partners = defaultdict(dict)
    for r in c.execute("SELECT pokemon,partner,rank FROM pokemon_partners WHERE season=? AND rule=? ORDER BY rank", (season, rule)):
        pk, pt = canon(r["pokemon"]), canon(r["partner"])
        if pt not in partners[pk]: partners[pk][pt] = r["rank"]
    partners = {k: sorted(v.items(), key=lambda x: x[1]) for k, v in partners.items()}
    def dist(table, key):
        d = defaultdict(dict)
        for r in c.execute(f"SELECT pokemon,{key} v,usage_rate u FROM {table} WHERE season=? AND rule=?", (season, rule)):
            if r["v"] is None: continue
            p = canon(r["pokemon"])
            d[p][r["v"]] = max(d[p].get(r["v"], 0.0), r["u"] or 0.0)
        return d
    moves = dist("pokemon_moves", "move"); items = dist("pokemon_items", "item")
    natures = dist("pokemon_natures", "nature"); abil = dist("pokemon_abilities", "ability")
    evs = defaultdict(list)
    for r in c.execute("SELECT pokemon,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate u FROM pokemon_evs WHERE season=? AND rule=?", (season, rule)):
        evs[canon(r["pokemon"])].append(((r["ev_h"], r["ev_a"], r["ev_b"], r["ev_c"], r["ev_d"], r["ev_s"]), r["u"] or 0.0))
    megastones = set(r["mega_stone"] for r in c.execute("SELECT mega_stone FROM pokemon_mega_stats") if r["mega_stone"])
    mega_pokemon = set(p for p, idist in items.items() if any(k in megastones for k in idist))
    # メガ石→メガ後A/C（物理/特殊の向き判定用）
    mega_by_stone = {}
    for r in c.execute("SELECT mega_stone,attack,sp_attack FROM pokemon_mega_stats"):
        if r["mega_stone"]: mega_by_stone[r["mega_stone"]] = {"a": r["attack"], "c": r["sp_attack"]}
    # 技カテゴリ（physical/special/status）
    move_cat = {r["name_jp"]: r["category"] for r in c.execute("SELECT name_jp,category FROM move_master")}
    # 学習攻撃技を種族×カテゴリ別に威力降順（向き補正の補充用）
    learn_atk = defaultdict(list)
    q = ("SELECT ls.pokemon_name p, m.name_jp nm, m.category cat, m.power pw FROM pokemon_learnsets ls "
         "JOIN move_master m ON m.name_jp=ls.move_jp WHERE m.power IS NOT NULL AND m.category IN ('physical','special')")
    tmp = defaultdict(list)
    for r in c.execute(q):
        tmp[(canon(r["p"]), r["cat"])].append((r["nm"], r["pw"] or 0))
    for k, lst in tmp.items():
        learn_atk[k] = [nm for nm, _ in sorted(lst, key=lambda x: -x[1])]
    return dict(usage=usage, partners=partners, moves=moves, items=items, natures=natures, abil=abil, evs=evs,
                megastones=megastones, mega_pokemon=mega_pokemon, dex=dex,
                mega_by_stone=mega_by_stone, move_cat=move_cat, learn_atk=dict(learn_atk))

def _wchoice(weights, rng):
    items = [(k, w) for k, w in weights.items() if w > 0]
    if not items: return None
    tot = sum(w for _, w in items); r = rng.random() * tot; acc = 0.0
    for k, w in items:
        acc += w
        if r <= acc: return k
    return items[-1][0]

def _wsample_dict(d, k, rng):  # d: {value: weight}; 上位kを重み付き非復元抽出
    out = []; pool = dict(d)
    for _ in range(k):
        ch = _wchoice(pool, rng)
        if ch is None: break
        out.append(ch); pool.pop(ch, None)
    return out

# 性格の同軸swap（特殊↔物理。素早さ補正/補正なしの軸は保つ）
_NAT_SWAP = {"ひかえめ": "いじっぱり", "おくびょう": "ようき", "ずぶとい": "わんぱく", "おだやか": "しんちょう",
             "いじっぱり": "ひかえめ", "ようき": "おくびょう", "わんぱく": "ずぶとい", "しんちょう": "おだやか"}
_SPEC_NAT = {"ひかえめ", "おくびょう", "ずぶとい", "おだやか"}
_PHYS_NAT = {"いじっぱり", "ようき", "わんぱく", "しんちょう"}

def mega_orient(D, item):
    """メガ石→'phys'/'spec'（メガ後A>Cなら物理）。非メガ/不明はNone。"""
    m = D.get("mega_by_stone", {}).get(item)
    if not m or m["a"] is None or m["c"] is None: return None
    return "phys" if m["a"] > m["c"] else "spec"

def orient_set(D, p, item, mv, nat, ev):
    """選んだメガ石の物理/特殊の向きに、技・性格・EVを合わせ直す。
    使用率は種族単位で支配的フォルム(例メガライチュウY特殊)に偏るため、別石(メガX物理)に
    その型が乗る誤ビルドを是正。反対カテゴリ攻撃技を除去→学習技で補充、性格/EVを同軸へ。"""
    o = mega_orient(D, item)
    if o is None: return mv, nat, ev
    cat = D.get("move_cat", {}); want = "physical" if o == "phys" else "special"
    other = "special" if o == "phys" else "physical"
    kept = [x for x in (mv or []) if cat.get(x) != other]
    if sum(1 for x in kept if cat.get(x) == want) < 2:
        for cand in D.get("learn_atk", {}).get((p, want), []):
            if cand not in kept: kept.append(cand)
            if len(kept) >= 4: break
    kept = kept[:4] if kept else mv
    if nat in _NAT_SWAP and ((o == "phys" and nat in _SPEC_NAT) or (o == "spec" and nat in _PHYS_NAT)):
        nat = _NAT_SWAP[nat]
    if ev:
        h, a, b, c, d, s = ev
        if (o == "phys" and c > a) or (o == "spec" and a > c): a, c = c, a
        ev = (h, a, b, c, d, s)
    return kept, nat, ev

def gen_party(D, rng, usage_floor=0.15):
    uw = {p: 1.0 / rk for p, rk in D["usage"]}      # ランク→Zipf重み
    if not uw: raise RuntimeError("usageデータ無し")
    dexmap = D.get("dex", {})
    def dx(p): return dexmap.get(p, p)               # 図鑑番号(無ければ名前)＝同種判定キー
    team = [_wchoice(uw, rng)]
    used_dex = {dx(team[0])}
    while len(team) < 6:
        cw = defaultdict(float)
        for picked in team:                          # 同居率（相方ランク）で synergy
            for partner, rk in D["partners"].get(picked, []):
                if partner not in team and dx(partner) not in used_dex: cw[partner] += 1.0 / rk
        for p, w in uw.items():                       # 使用率フロア（探索）
            if p not in team and dx(p) not in used_dex: cw[p] += usage_floor * w
        nxt = _wchoice(cw, rng)
        if nxt is None:
            for p, _ in D["usage"]:
                if p not in team and dx(p) not in used_dex: nxt = p; break
        if nxt is None or nxt in team or dx(nxt) in used_dex: break
        team.append(nxt); used_dex.add(dx(nxt))
    # --- メガ可能個体を最低1体は含める（0なら最下位を差替え＝必ず1〜2メガ可能に） ---
    if not any(p in D["mega_pokemon"] for p in team):
        keep_dex = {dx(p) for p in team[:-1]}        # 差替え対象(team[-1])以外の同種は避ける
        cands = {p: uw.get(p, 0.01) for p in D["mega_pokemon"] if p not in team and dx(p) not in keep_dex}
        if cands: team[-1] = _wchoice(cands, rng)
    # --- 持ち物：重複禁止＋メガは最大2（3メガ禁止） ---
    used_items = set(); mega = 0; mons = []
    for p in team:
        idist = {k: v for k, v in D["items"].get(p, {}).items() if k not in used_items}
        if mega >= 2:
            idist = {k: v for k, v in idist.items() if k not in D["megastones"]}
        item = _wchoice(idist, rng) if idist else None
        if item in D["megastones"]: mega += 1
        if item: used_items.add(item)
        mons.append({"p": p, "item": item})
    # --- メガ最低1体（0なら可能な個体を1体メガ石に差替え） ---
    if mega == 0:
        for m in mons:
            stones = {k: D["items"][m["p"]][k] for k in D["items"].get(m["p"], {})
                      if k in D["megastones"] and k not in used_items}
            if stones:
                if m["item"]: used_items.discard(m["item"])
                m["item"] = _wchoice(stones, rng); used_items.add(m["item"]); mega = 1; break
    # --- 残り属性 & spec ---
    specs = []
    for m in mons:
        p = m["p"]
        nat = _wchoice(D["natures"].get(p, {}), rng)
        ab = _wchoice(D["abil"].get(p, {}), rng)
        mv = _wsample_dict(D["moves"].get(p, {}), 4, rng)
        evpairs = D["evs"].get(p, [])
        ev = None
        if evpairs:
            i = _wchoice({i: w for i, (sp, w) in enumerate(evpairs)}, rng)
            ev = evpairs[i][0] if i is not None else None
        mv, nat, ev = orient_set(D, p, m["item"], mv, nat, ev)   # メガ石の物理/特殊に型を合わせる
        specs.append(_spec(p, m["item"], nat, mv, ev, ab))
    return specs

def _spec(name, item, nature, moves, ev, ability):
    s = canon(name)
    if item: s += f"@{item}"
    s += ":" + (nature or "")
    s += ":" + ("|".join(moves) if moves else "")
    s += ":" + ("/".join(str(x or 0) for x in ev) if ev else "")
    s += ":" + (ability or "")
    return s.rstrip(":")

if __name__ == "__main__":
    import sys
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    D = load(); L = get_loader(); rng = random.Random(0)
    ok = fail = 0; megacnt = defaultdict(int); species = defaultdict(int); errs = []
    arche = {"メタモン": 0, "バトンタッチ": 0, "あまごい/雨特性": 0}
    for _ in range(N):
        specs = gen_party(D, rng)
        nm = 0; names = []
        try:
            mons = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
            ok += 1
            for s, mon in zip(specs, mons):
                names.append(mon.name); species[mon.name] += 1
                if getattr(mon, "mega_data", None) is not None and (mon.item in D["megastones"]): nm += 1
                if "バトンタッチ" in s: arche["バトンタッチ"] += 1
            jn = " ".join(names)
            if "メタモン" in jn: arche["メタモン"] += 1
            if "あまごい" in " ".join(specs) or any(getattr(m, "ability", "") == "あめふらし" for m in mons): arche["あまごい/雨特性"] += 1
            megacnt[nm] += 1
        except Exception as e:
            fail += 1
            if len(errs) < 5: errs.append(str(e)[:80])
    print(f"生成 {N}  build成功 {ok}  失敗 {fail}")
    print(f"メガ数分布(チーム内): {dict(megacnt)}  ← 2以上が0であるべき")
    print(f"種族多様性: {len(species)}種が出現  上位: {sorted(species.items(),key=lambda x:-x[1])[:8]}")
    print(f"アーキタイプ出現(パーティ数): {arche}")
    if errs: print("エラー例:", errs)
