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
    # メガ石→メガ後A/C/タイプ（物理/特殊の向き・一致技判定用）
    mega_by_stone = {}; mega_stone_dex = {}
    for r in c.execute("SELECT mega_stone,base_dex,type1,type2,attack,sp_attack,ability FROM pokemon_mega_stats"):
        if r["mega_stone"]:
            mega_by_stone[r["mega_stone"]] = {"a": r["attack"], "c": r["sp_attack"], "ability": r["ability"],
                                              "t": tuple(t for t in (r["type1"], r["type2"]) if t)}
            if r["base_dex"] is not None: mega_stone_dex[r["mega_stone"]] = f"{int(r['base_dex']):04d}"
    # 素体A/C/タイプ（非メガの向き・一致技判定用）
    base = {}
    for r in c.execute("SELECT pokemon_name,dex_number,type1,type2,attack,sp_attack FROM pokemon_base_stats"):
        nm = canon(r["pokemon_name"])
        base[nm] = {"a": r["attack"], "c": r["sp_attack"],
                    "t": tuple(t for t in (r["type1"], r["type2"]) if t)}
        dex.setdefault(nm, f"{int(r['dex_number']):04d}")   # 使用率外の種もdexを補完(valid_megastone用)
    # 技カテゴリ/タイプ/威力/先制攻撃技（先制技は同タイプ重複判定から除外＝通常技と共存正当）
    move_cat = {}; move_type = {}; move_pow = {}; priority_atk = set()
    for r in c.execute("SELECT name_jp,category,type,power,priority FROM move_master"):
        move_cat[r["name_jp"]] = r["category"]; move_type[r["name_jp"]] = r["type"]; move_pow[r["name_jp"]] = r["power"]
        if (r["priority"] or 0) > 0 and r["category"] in ("physical", "special"):
            priority_atk.add(r["name_jp"])
    # 学習攻撃技を種族×カテゴリ別に威力降順（向き補正の補充用）
    # 威力は高いが単体採用が罠の技(反動/溜め/低命中)は補充候補から除外
    _TRAP_ATK = {"ギガインパクト", "はかいこうせん", "ブラストバーン", "ハイドロカノン", "ハードプラント",
                 "すてみタックル", "とっしん", "メガトンキック", "メガトンパンチ", "ばくれつパンチ",
                 "ロケットずつき", "はなびらのまい", "ぶんまわす"}
    learn_atk = defaultdict(list)
    q = ("SELECT ls.pokemon_name p, m.name_jp nm, m.category cat, m.power pw, m.accuracy ac FROM pokemon_learnsets ls "
         "JOIN move_master m ON m.name_jp=ls.move_jp WHERE m.power IS NOT NULL AND m.category IN ('physical','special')")
    tmp = defaultdict(list)
    for r in c.execute(q):
        if r["nm"] in _TRAP_ATK: continue
        ac = r["ac"] if r["ac"] is not None else 100
        if ac < 80: continue                      # 低命中の博打技も除外
        tmp[(canon(r["p"]), r["cat"])].append((r["nm"], r["pw"] or 0))
    for k, lst in tmp.items():
        learn_atk[k] = [nm for nm, _ in sorted(lst, key=lambda x: -x[1])]
    return dict(usage=usage, partners=partners, moves=moves, items=items, natures=natures, abil=abil, evs=evs,
                megastones=megastones, mega_pokemon=mega_pokemon, dex=dex,
                mega_by_stone=mega_by_stone, mega_stone_dex=mega_stone_dex, base=base,
                move_cat=move_cat, move_type=move_type, move_pow=move_pow, priority_atk=priority_atk,
                learn_atk=dict(learn_atk))

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
             "いじっぱり": "ひかえめ", "ようき": "おくびょう", "わんぱく": "ずぶとい", "しんちょう": "おだやか",
             "れいせい": "ゆうかん", "ゆうかん": "れいせい"}
_SPEC_NAT = {"ひかえめ", "おくびょう", "ずぶとい", "おだやか", "れいせい"}
_PHYS_NAT = {"いじっぱり", "ようき", "わんぱく", "しんちょう", "ゆうかん"}

def mega_usage_rate(D, species):
    """その種の使用率に占めるメガ石の割合（≒メガ依存度）。高いほど非メガでは使われない。"""
    d = D["items"].get(species, {}); tot = sum(d.values()) or 1.0
    return sum(v for k, v in d.items() if k in D["megastones"]) / tot

def fallback_item(D, species, used=()):
    """アイテム無しを防ぐ。種の非メガ使用率アイテム→汎用の順でフォールバック。"""
    cands = {k: v for k, v in D["items"].get(species, {}).items()
             if k and k not in D["megastones"] and k not in used}
    if cands:
        return max(cands, key=cands.get)
    for g in ("たべのこし", "オボンのみ", "きあいのタスキ", "ラムのみ"):
        if g not in used: return g
    return "たべのこし"

def valid_megastone(D, name, item):
    """そのメガ石が種族に正規対応するか（他種石の混入＝クロール誤りを弾く）。"""
    return item in D.get("mega_stone_dex", {}) and D.get("dex", {}).get(name) == D["mega_stone_dex"][item]

def mega_orient(D, item):
    """メガ石→'phys'/'spec'（メガ後A>Cなら物理）。非メガ/不明はNone。"""
    m = D.get("mega_by_stone", {}).get(item)
    if not m or m["a"] is None or m["c"] is None: return None
    a = m["a"] * (2 if m.get("ability") in ("ちからもち", "ヨガパワー") else 1)   # 攻撃2倍特性を反映(例メガスターミーちからもち)
    return "phys" if a >= m["c"] else "spec"   # A==C(例メガリザードンX130/130・かたいツメ)は物理寄せ

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

# コヒーレント技構成用の役割技/罠/溜め技（_moveset_opt.py と同一の方針）
_ROLE_ATK = {"ボルトチェンジ", "とんぼがえり", "クイックターン", "ニトロチャージ", "でんこうせっか",
             "しんそく", "バレットパンチ", "アクアジェット", "ねこだまし"}
# 性格の物理/特殊判定で除外する攻撃技（役割技＋イカサマ＝自分のAに依存しない物理技）
_NAT_NEUTRAL = _ROLE_ATK | {"イカサマ"}
_TRAP = {"ギガインパクト", "はかいこうせん", "ブラストバーン", "ハイドロカノン", "ハードプラント",
         "すてみタックル", "とっしん", "メガトンキック", "メガトンパンチ", "ばくれつパンチ",
         "ロケットずつき", "はなびらのまい", "ぶんまわす"}
_SUN_CHARGE = {"ソーラービーム", "ソーラーブレード"}; _RAIN_CHARGE = {"エレクトロビーム"}
_ALWAYS_CHARGE = {"あなをほる", "そらをとぶ", "ダイビング", "ゴッドバード", "とびはねる", "メテオビーム", "ゴーストダイブ"}
_WSET = {"あめふらし": "rain", "あまごい": "rain", "ひでり": "sun", "にほんばれ": "sun",
         "すなおこし": "sand", "ゆきふらし": "snow", "メガソーラー": "sun"}
# こだわり系＝1技ロック。積み技/非ピボット変化技は死に技になる（トリック/すりかえで石を渡す型のみ例外）
_CHOICE_ITEMS = {"こだわりスカーフ", "こだわりハチマキ", "こだわりメガネ"}
_SETUP_MOVES = {"つるぎのまい", "りゅうのまい", "わるだくみ", "ちょうのまい", "めいそう", "てっぺき",
                "からをやぶる", "こうそくいどう", "ロックカット", "ビルドアップ", "コスモパワー",
                "とぐろをまく", "アシッドボム", "はらだいこ", "コットンガード", "せいちょう"}
_PIVOT_TRICK = {"とんぼがえり", "ボルトチェンジ", "クイックターン", "トリック", "すりかえ"}

# シナジーアイテム＝特定の技/特性が無いと無意味（持ち手自身が条件を満たす必要がある）
_SYNERGY_ITEM = {
    "ひかりのねんど": ({"リフレクター", "ひかりのかべ", "オーロラベール"}, set()),
    "しめったいわ": ({"あまごい"}, {"あめふらし"}),
    "さらさらいわ": ({"すなあらし"}, {"すなおこし"}),
    "あついわ": ({"にほんばれ", "晴れ"}, {"ひでり", "メガソーラー"}),
    "つめたいいわ": ({"ゆきげしき", "あられ"}, {"ゆきふらし"}),
}

def coherent_item(D, name, item, moves, ability=None, used=()):
    """アイテムを使用率・整合で是正。①シナジーアイテムが活きないなら差し替え
    ②使用率<2%の珍アイテム（メガ石/シナジー/きのみ系除く）は種の主要アイテムへ寄せる
    （例: ひかりのこな等の<1%ノイズが「強い結果」のように残るのを防ぐ）。"""
    req = _SYNERGY_ITEM.get(item)
    if req and not (set(moves or ()) & req[0]) and ability not in req[1]:
        return fallback_item(D, name, used)
    if item and item not in D["megastones"] and item not in _SYNERGY_ITEM and not item.endswith("のみ"):
        rate = D["items"].get(name, {}).get(item, 0.0)
        if rate < 2.0:                                 # usage_rate は%。<2%は採用実態の薄いノイズ
            top = {k: v for k, v in D["items"].get(name, {}).items()
                   if k not in D["megastones"] and k not in used and v >= 2.0}
            if top: return max(top, key=top.get)
    return item

def species_orient(D, name, item):
    """個体の物理/特殊の向き。メガ石ありはメガ後A/C、なければ素体A/C。"""
    if valid_megastone(D, name, item):
        return mega_orient(D, item)
    b = D.get("base", {}).get(name)
    if not b or b["a"] is None or b["c"] is None: return None
    return "phys" if b["a"] >= b["c"] else "spec"

def eff_types(D, name, item):
    """実効タイプ（メガ後 or 素体）。一致技判定用。"""
    if valid_megastone(D, name, item):
        return set(D.get("mega_by_stone", {}).get(item, {}).get("t", ()))
    return set(D.get("base", {}).get(name, {}).get("t", ()))

def _bad_charge(m, weather):
    return (m in _SUN_CHARGE and "sun" not in weather) or (m in _RAIN_CHARGE and "rain" not in weather) or (m in _ALWAYS_CHARGE)

def coherent_set(D, name, item, mv, nat, ev, weather=None):
    """フィラーの技構成をコヒーレントに整える（軸はオプティマイザ管轄で対象外）。
    役割技/変化技/積み/壁は温存。純攻撃技は同タイプ重複を排除（向き一致→高威力を残す）、
    罠技/文脈外の溜め技を除去、一致技ゼロなら補充、性格/EVを攻撃の主カテゴリへ合わせる。"""
    weather = weather or set()
    mv = list(mv or [])
    if not mv: return mv, nat, ev
    cat = D["move_cat"]; mtype = D["move_type"]; mpow = D["move_pow"]
    role = _ROLE_ATK | D.get("priority_atk", set())   # 先制技は同タイプ重複判定から除外（通常技と共存正当）
    etypes = eff_types(D, name, item)
    o = species_orient(D, name, item)
    want = "physical" if o == "phys" else ("special" if o == "spec" else None)
    n = len(mv)
    # こだわり系で積み・非ピボット変化技は構造的に死に＝除去（トリック/すりかえ型は例外）
    choice_lock = item in _CHOICE_ITEMS and not (set(mv) & {"トリック", "すりかえ"})
    pure, others = [], []
    for m in mv:
        if cat.get(m) in ("physical", "special") and m not in role:
            pure.append(m)
        elif choice_lock and (m in _SETUP_MOVES or (cat.get(m) == "status" and m not in _PIVOT_TRICK)):
            continue                               # こだわり下の死に技は捨てる（後で攻撃技で補充）
        else:
            others.append(m)                       # 役割技/変化/積み/壁/状態技は温存
    # 罠技・文脈外溜め技を純攻撃から除去
    pure = [m for m in pure if m not in _TRAP and not _bad_charge(m, weather)]
    # 同タイプ純攻撃の重複排除（向き一致を優先、次に高威力）
    by_type = {}
    for m in pure:
        t = mtype.get(m)
        cur = by_type.get(t)
        if cur is None:
            by_type[t] = m; continue
        def score(x):
            om = 1 if (want and cat.get(x) == want) else 0
            return (om, mpow.get(x) or 0)
        if score(m) > score(cur): by_type[t] = m
    pure = [m for m in pure if by_type.get(mtype.get(m)) == m]
    seen = set()                                    # 順序保持の重複除去
    pure = [m for m in pure if not (m in seen or seen.add(m))]
    # 一致技ゼロなら補充（向き一致・高威力・罠/溜め以外）。枠が埋まっていれば最弱の純攻撃と差し替え
    if etypes and pure and want and not any(mtype.get(m) in etypes for m in pure):
        cand = next((x for x in D.get("learn_atk", {}).get((name, want), [])
                     if mtype.get(x) in etypes and x not in pure and x not in others
                     and x not in _TRAP and not _bad_charge(x, weather)), None)
        if cand:
            if len(pure) + len(others) >= n:
                pure.remove(min(pure, key=lambda m: mpow.get(m) or 0))
            pure.insert(0, cand)
    keep = set(pure) | set(others)
    out = []                                         # 元の並び順を保ちつつ生存技を再構成（完全重複も除去）
    for m in mv:
        if m in keep and m not in out: out.append(m)
    for m in pure + others:                          # 差し替え/補充した技を追加
        if m not in out: out.append(m)
    # 欠けた枠を学習技（向き一致・タイプ多様・罠/溜め以外）で補充
    if len(out) < n and want:
        have_types = {mtype.get(m) for m in out if cat.get(m) in ("physical", "special")}
        for cand in D.get("learn_atk", {}).get((name, want), []):
            if len(out) >= n: break
            if cand in out or cand in _TRAP or _bad_charge(cand, weather): continue
            if mtype.get(cand) in have_types: continue
            out.append(cand); have_types.add(mtype.get(cand))
    out = out[:n]
    # シグネチャ技（使用率>=85%＝ほぼ確定採用。例ミミッキュのかげうち96%）が欠けていれば注入。
    # こだわり下の積み/死に技や溜め技は注入しない。最も使用率の低い非シグネチャ技と差し替え。
    umoves = D.get("moves", {}).get(name, {})
    sig = [m for m, r in sorted(umoves.items(), key=lambda x: -x[1]) if r >= 85.0]
    for sm in sig:
        if sm in out: continue
        if sm in _TRAP or _bad_charge(sm, weather): continue
        if choice_lock and (sm in _SETUP_MOVES or (cat.get(sm) == "status" and sm not in _PIVOT_TRICK)): continue
        # メガ等で向きが決まっている個体に、逆カテゴリの攻撃シグネチャ技は注入しない
        if want and cat.get(sm) in ("physical", "special") and cat.get(sm) != want and sm not in role:
            continue
        repl = min((m for m in out if m not in sig), key=lambda m: umoves.get(m, 0.0), default=None)
        if repl is not None:
            out[out.index(repl)] = sm
    nat, ev = align_nat_ev(D, out, nat, ev, fallback=o)
    return out, nat, ev

def align_nat_ev(D, moves, nat, ev, fallback=None):
    """技構成は触らず、性格/EVを攻撃の主カテゴリへ合わせる（純攻撃が2本以上ある向きにのみ）。
    役割技/イカサマは自分のAに依存しないので物理/特殊判定から除外。学習済み軸の整合にも使う。"""
    cat = D["move_cat"]; neutral = _NAT_NEUTRAL | D.get("priority_atk", set())
    nph = sum(1 for m in moves if cat.get(m) == "physical" and m not in neutral)
    nsp = sum(1 for m in moves if cat.get(m) == "special" and m not in neutral)
    majo = "phys" if nph > nsp else ("spec" if nsp > nph else fallback)
    if majo and (nph + nsp) >= 2:
        if nat in _NAT_SWAP and ((majo == "phys" and nat in _SPEC_NAT) or (majo == "spec" and nat in _PHYS_NAT)):
            nat = _NAT_SWAP[nat]
        if ev:
            h, a, b, c, d, s = ev
            if (majo == "phys" and c > a) or (majo == "spec" and a > c): a, c = c, a
            ev = (h, a, b, c, d, s)
    return nat, ev

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
        if item is None: item = fallback_item(D, p, used_items)   # アイテム無しを防ぐ
        if item in D["megastones"]: mega += 1
        if item: used_items.add(item)
        mons.append({"p": p, "item": item})
    # --- メガ最低1体（0なら可能な個体を1体メガ石に差替え） ---
    if mega == 0:
        for m in mons:
            stones = {k: D["items"][m["p"]][k] for k in D["items"].get(m["p"], {})
                      if k in D["megastones"] and k not in used_items and valid_megastone(D, m["p"], k)}
            if stones:
                if m["item"]: used_items.discard(m["item"])
                m["item"] = _wchoice(stones, rng); used_items.add(m["item"]); mega = 1; break
    # --- 残り属性 ---
    attrs = []
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
        attrs.append({"p": p, "item": m["item"], "nat": nat, "ab": ab, "mv": mv, "ev": ev})
    weather = set()                                  # チームの天候源（特性/技）
    for a in attrs:
        for x in [a["ab"]] + (a["mv"] or []):
            if x in _WSET: weather.add(_WSET[x])
    specs = []
    for a in attrs:                                  # 技/性格/EVをコヒーレントに整える
        mv, nat, ev = coherent_set(D, a["p"], a["item"], a["mv"], a["nat"], a["ev"], weather=weather)
        specs.append(_spec(a["p"], a["item"], nat, mv, ev, a["ab"]))
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
