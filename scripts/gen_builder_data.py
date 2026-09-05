"""「パーティ構築」ページ/対戦マッチアップ用の静的データ生成。

データ源は pokenavi.db の使用率クロールのみ（旧実装が依存していた人力Markdown
`build_pool_M-3.md` からは完全に切り離した）。出力は public/builder-data/*.json。

使い方: python3 scripts/gen_builder_data.py
        BUILDER_SEASON=M-4 python3 scripts/gen_builder_data.py   # シーズン切替

── 設計（2026-08 改修） ─────────────────────────────────────────────
1. 技は「4技固定のビルド」ではなく **採用率TOP10の技プール(mpool)** として持つ。
   1v1判定は自分・相手ともこのプールから相手に最大打点となる技を選んで打ち合う
   （＝互いに最良の弱点を突いた場合の勝敗）。TS側 damage.ts bestMove() が pool を見る。
2. 型(型1/2/3)のバリエーションは **持ち物 × 性格/EV** で表現する。自分側・相手側とも
   同じ生成ロジック（build_variants）を使い、非対称（自分は1型・相手は3型）を解消する。
   組み合わせは templates（実構築の同時分布）で裏取りし、周辺分布の掛け合わせで生じる
   非実在型（メガ石×物理性格など）を作らない。詳細は「型(バリエーション)の合成」節。
3. クロール欠測への耐性: 「最新 crawled_date」を無条件に使うと、その日だけ行が
   欠けた種で誤った代表型が選ばれる（実例: M-3 2026-07-01 のカイリューはメガ石の行が
   欠落し、採用率2位のラムのみ型が代表型になっていた）。_robust_rows() は
   「採用率の合計が閾値以上の最新日」を採る（同一シーズン内の全日→過去シーズンの順）。
"""
import os
import sqlite3
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DB = os.path.join(HERE, "pokenavi.db")
OUT_DIR = os.path.join(ROOT, "public", "builder-data")
MON_DIR = os.path.join(OUT_DIR, "mon")
SEASON = os.environ.get("BUILDER_SEASON", "M-5")
RULE = "single"

# 新しい順。SEASON が欠測の場合のみ、これより古いシーズンへ順に遡る。
SEASON_ORDER = ["M-5", "M-4", "M-3", "M-2"]

MOVE_POOL_N = 10      # 技プールに入れる採用率上位の技数
MAX_VARIANTS = 3      # 1種あたりの型数（型1/2/3）
MIN_ITEM_PCT = 3.0    # 型として採用する持ち物の最低採用率(%)
MAX_PER_ITEM = 2      # 同一持ち物から作ってよい型の上限（攻撃軸違いの2型まで）
EV_INVEST = 16        # 「そのステに投資している」とみなすEV下限（EVは最大32スケール）
AXIS_MIN_SHARE = 0.15 # 第2の攻撃軸を型として立てる最低シェア
MIN_JOINT_N = 3       # templates の同時分布を「その持ち物の型の根拠」として信頼する最低件数
MIN_JOINT_NATURE_PCT = 3.0 # 観測1件だけの性格を採る場合に要求する周辺採用率(%)（外れ値除け）
NATURE_ALT_PCT = 15.0 # 型間で性格を分けるとき、第2の性格に要求する周辺採用率(%)
MEGA_AXIS_GAP = 15    # メガ後のA/C差がこれ以上なら、その持ち物は物理/特殊のどちらか寄りと見なす

# 性格 -> (上昇stat idx, 下降stat idx)。並びは H,A,B,C,D,S。src/scripts/party-builder/stats.ts と同一。
NATURE_MODS = {
    "いじっぱり": (1, 3), "ゆうかん": (1, 5), "やんちゃ": (1, 4), "さみしがり": (1, 2),
    "わんぱく": (2, 3), "のうてんき": (2, 4), "のんき": (2, 5), "ずぶとい": (2, 1),
    "おくびょう": (5, 1), "せっかち": (5, 2), "ようき": (5, 3), "むじゃき": (5, 4),
    "ひかえめ": (3, 1), "おっとり": (3, 2), "うっかりや": (3, 4), "れいせい": (3, 5),
    "おだやか": (4, 1), "おとなしい": (4, 2), "しんちょう": (4, 3), "なまいき": (4, 5),
}

# 持ち物が要求する型の性質。None は制約なし。
ITEM_AXIS = {"こだわりハチマキ": "A", "ちからのハチマキ": "A", "こだわりメガネ": "C", "ものしりメガネ": "C"}
SPEED_ITEMS = {"こだわりスカーフ"}


def kana_key(s):
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in s)


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))


def _season_chain():
    if SEASON in SEASON_ORDER:
        return SEASON_ORDER[SEASON_ORDER.index(SEASON):]
    return [SEASON] + SEASON_ORDER


# テーブルごとの「このクロール日は使い物になる」判定閾値（採用率の合計%）。
# items/natures/abilities は総和100%が期待値、evs/moves は分布が細かいため低め。
_MIN_SUM = {"pokemon_items": 50.0, "pokemon_natures": 50.0, "pokemon_abilities": 50.0,
            "pokemon_evs": 20.0, "pokemon_moves": 150.0}


def _robust_rows(con, table, cols, name):
    """種 name の table 行を「採用率合計が閾値以上の最新クロール日」から取る。

    無条件に MAX(crawled_date) を使う旧実装は、部分的に失敗したクロール日に当たると
    代表型を取り違える（カイリュー/カイリュナイト欠落バグ）。同一シーズン内の日を新しい順に
    見て閾値を満たす最初の日を採用し、どの日も満たさなければ過去シーズンへ遡る。
    それでも見つからない場合は「合計が最大の日」を返す（無いよりはまし）。
    """
    min_sum = _MIN_SUM[table]
    best = []
    best_sum = -1.0
    for season in _season_chain():
        dates = [r[0] for r in con.execute(
            f"SELECT DISTINCT crawled_date FROM {table} WHERE season=? AND rule=? AND pokemon=? "
            f"ORDER BY crawled_date DESC", (season, RULE, name))]
        for d in dates:
            rows = con.execute(
                f"SELECT {cols}, usage_rate FROM {table} WHERE season=? AND rule=? AND pokemon=? "
                f"AND crawled_date=? ORDER BY rank", (season, RULE, name, d)).fetchall()
            total = sum((r[-1] or 0) for r in rows)
            if total >= min_sum:
                return rows
            if total > best_sum:
                best, best_sum = rows, total
    return best


def _items_of(con, name):
    return [(r[0], r[1] or 0.0) for r in _robust_rows(con, "pokemon_items", "item", name)]


def _natures_of(con, name):
    return [(r[0], r[1] or 0.0) for r in _robust_rows(con, "pokemon_natures", "nature", name)]


def _abilities_of(con, name):
    return [(r[0], r[1] or 0.0) for r in _robust_rows(con, "pokemon_abilities", "ability", name)]


def _moves_of(con, name):
    return [(r[0], r[1] or 0.0) for r in _robust_rows(con, "pokemon_moves", "move", name)]


def _evs_of(con, name):
    rows = _robust_rows(con, "pokemon_evs", "ev_h, ev_a, ev_b, ev_c, ev_d, ev_s", name)
    return [([int(x or 0) for x in r[:6]], r[6] or 0.0) for r in rows]


def build_species(con, L, usage_rows):
    tpl_of = {}
    species_list = []
    for name, rank, pid in usage_rows:
        tpl = L.get_pokemon_template(name, season=SEASON)
        if tpl is None:
            continue
        tpl_of[name] = tpl
        megas = []
        for md in sorted(tpl.mega_data.values(), key=lambda m: m.mega_stone):
            megas.append({
                "name": md.mega_name, "stone": md.mega_stone,
                "t1": md.type1, "t2": md.type2,
                "bs": [md.hp, md.attack, md.defense, md.sp_attack, md.sp_defense, md.speed],
                "ability": md.ability,
            })
        species_list.append({
            "n": name, "rank": rank, "icon": pid,
            "t1": tpl.type1, "t2": tpl.type2,
            "bs": [tpl.base_hp, tpl.base_attack, tpl.base_defense,
                   tpl.base_sp_attack, tpl.base_sp_defense, tpl.base_speed],
            "mega": megas,
        })
    return species_list, tpl_of


def build_items(con):
    """item_master 由来の全アイテム名(五十音順)。category='item'(持ち物として選べる一般アイテム)かつ
    implemented=1(このサイトのシミュレータで効果が実装済み)のみに絞る。
    category='mega'/'megastone' は個別ポケモン専用のメガストーンで、対象種の species.json.mega に
    実際に使われた場合は使用率データ経由で既にその種の持ち物選択肢に含まれるため、
    ここでは一般アイテムの「その他」候補としては対象外とする（他種のメガストーンを無関係に出さないため）。
    implemented=0(フォーカスレンズ/メトロノーム/きれいなぬけがら等)はダメージ計算/耐久判定に
    効果が反映されないため選択肢から除外する。"""
    rows = con.execute("SELECT name_jp FROM item_master WHERE category='item' AND implemented=1").fetchall()
    return sorted((r[0] for r in rows), key=kana_key)


def build_moves(con):
    rows = con.execute("SELECT name_jp, type, category, power, priority FROM move_master").fetchall()
    rows.sort(key=lambda r: r[0])
    return {r[0]: [r[1], r[2], r[3], r[4]] for r in rows}


# ── 型(バリエーション)の合成 ────────────────────────────────────────
# 使用率クロール(pokemon_items/natures/evs)は持ち物・性格・EVそれぞれの周辺分布しか持たない。
# 「持ち物 × 攻撃軸(A/C/耐久)」で型を合成するが、周辺分布の単純な掛け合わせは実在しない型を
# 作る（例: メガカイリューはC145/非メガはA134なので物理型はあえてメガ進化しないのに
# 「カイリュナイト×いじっぱり」が出る）。これを次の2段で防ぐ:
#   (a) templates（実構築の6匹分の型＝持ち物と性格/EVの同時分布）で観測された組み合わせに絞る
#   (b) templates に無い種は、軸シェアを「型を採るたびその持ち物の採用率ぶん消費する」ことで
#       配分し、さらにメガ後の種族値(A/C差)と矛盾する軸をメガ石から除く
# 技は型に紐付けず全型共通の採用率TOP10プールとするため、技については情報損失が無い。

def _ev_axis(ev):
    """EV配分の攻撃軸。'A'=物理投資、'C'=特殊投資、'D'=どちらでもない(耐久/補助)。"""
    a, c = ev[1], ev[3]
    if a >= EV_INVEST and a > c:
        return "A"
    if c >= EV_INVEST and c > a:
        return "C"
    return "D"


def _ev_axis_groups(evs):
    """EV分布を攻撃軸ごとにまとめ、[(軸, 代表EV, シェア)] をシェア降順で返す。"""
    total = sum(p for _, p in evs) or 1.0
    groups = {}
    for ev, pct in evs:
        ax = _ev_axis(ev)
        g = groups.setdefault(ax, {"share": 0.0, "ev": ev, "top": -1.0})
        g["share"] += pct
        if pct > g["top"]:
            g["top"], g["ev"] = pct, ev
    out = [(ax, g["ev"], g["share"] / total) for ax, g in groups.items()]
    out.sort(key=lambda t: -t[2])
    return out


def _nature_fits(nature, ev):
    """性格がEV配分と噛み合うか＝上昇ステに投資あり かつ 下降ステに投資なし。"""
    m = NATURE_MODS.get(nature)
    if m is None:
        return False                          # 無補正五性は「噛み合う」とは見なさない
    up, dn = m
    return ev[up] >= EV_INVEST and ev[dn] < EV_INVEST


def _pick_nature(natures, ev):
    """EV配分と噛み合う性格を採用率順に選ぶ。該当が無ければ採用率1位。"""
    for nm, _ in natures:
        if _nature_fits(nm, ev):
            return nm
    return natures[0][0] if natures else "まじめ"


def _pick_nature_joint(g, axis, natures, ev):
    """性格は「その持ち物・その攻撃軸で実際に使われた性格」を最頻で採る。
    件数が少なくても「その軸で観測された」性格ならEV配分と矛盾しないので採用する
    （軸を跨ぐ観測は使わない）。観測が無ければ従来通り周辺分布(採用率順)から選ぶ。
    返り値: (性格, 実構築の観測に裏付けられているか)。裏付けの無い推定だけを
    後段の「型間で性格を散らす」処理の対象にするためのフラグ。"""
    if g:
        pct = dict(natures)
        obs = [(c, nm) for (ax, nm), c in g["natures"].items()
               if ax == axis and _nature_fits(nm, ev)
               and (c >= 2 or pct.get(nm, 0.0) >= MIN_JOINT_NATURE_PCT)]
        if obs:
            return max(obs)[1], True
    return _pick_nature(natures, ev), False


def _nature_alt(natures, ev, used):
    """既出の性格と重なったときの差し替え候補（周辺採用率 NATURE_ALT_PCT 以上の未使用性格）。

    _nature_fits は「上昇ステに投資あり」を要求するため、耐久EV(H/B全振り)の特殊アタッカーが
    採る『ひかえめ』のような性格（上げたいCには投資せず、不要なAを下げるだけ）を弾いてしまい、
    採用率2割の実在型が型1/2/3から丸ごと消えていた（例: ニンフィア ひかえめ20.7%）。
    ここでは条件を「下降ステに投資が無い」だけに緩め、周辺採用率が十分大きい性格に限って採る。
    """
    for nm, pct in natures:
        if pct < NATURE_ALT_PCT or nm in used:
            continue
        m = NATURE_MODS.get(nm)
        if m and ev[m[1]] < EV_INVEST:
            return nm
    return None


def _joint_of(con, name):
    """templates(実際に使われた構築の6匹分の型)から、種 name の「持ち物×性格×EV」同時分布を取る。

    使用率クロール(pokemon_items/natures/evs)は周辺分布しか持たないため、それらを機械的に
    掛け合わせると実在しない型が出る（例: カイリューは非メガ時A134/メガ時C145で、物理性格は
    あえてメガ進化しない構築に付くのに「カイリュナイト×いじっぱり」が合成されてしまう）。
    templates は実構築の同時分布なので、観測された組み合わせのみに絞る根拠に使える。
    返り値: {持ち物: {"n": 件数, "axes": {軸: 件数}, "natures": {(軸,性格): 件数}}}
    """
    out = {}
    for item, nature, *ev in con.execute(
            "SELECT item, nature, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s FROM templates WHERE pokemon=?",
            (name,)):
        if not item or not nature:
            continue
        ev = [int(x or 0) for x in ev]
        ax = _ev_axis(ev)
        g = out.setdefault(item, {"n": 0, "axes": {}, "natures": {}})
        g["n"] += 1
        g["axes"][ax] = g["axes"].get(ax, 0) + 1
        k = (ax, nature)
        g["natures"][k] = g["natures"].get(k, 0) + 1
    return out


def _mega_axis(tpl, item, normalize_mega_stone):
    """メガストーンなら、メガ後の種族値が示す攻撃軸('A'/'C')。差が小さければ None(制約なし)。

    templates に実構築が無い種のための保険。メガ後にA<Cとなる種（カイリュー/リザードンY等）で
    物理型を、逆にA>Cとなる種で特殊型を合成してしまうのを防ぐ。
    """
    md = _mega_of(tpl, item, normalize_mega_stone)
    if md is None:
        return None
    if md.attack - md.sp_attack >= MEGA_AXIS_GAP:
        return "A"
    if md.sp_attack - md.attack >= MEGA_AXIS_GAP:
        return "C"
    return None


def _item_ok(item, ev):
    ax = ITEM_AXIS.get(item)
    if ax and _ev_axis(ev) != ax:
        return False
    if item in SPEED_ITEMS and ev[5] < EV_INVEST:
        return False
    return True


def _mega_of(tpl, item, normalize_mega_stone):
    if tpl is None:
        return None
    target = normalize_mega_stone(item)
    for md in tpl.mega_data.values():
        if normalize_mega_stone(md.mega_stone) == target:
            return md
    return None


CHOICE_ITEMS = {"こだわりスカーフ", "こだわりハチマキ", "こだわりメガネ"}
# こだわり系は最初に使った技に固定されるため、積み技・補助技を入れると機能しない。
# 相手に押し付けるトリック/すりかえと、変身後に固定が外れるへんしんだけは併用が成立する。
CHOICE_OK_STATUS = {"トリック", "すりかえ", "へんしん"}
_MOVE_CAT = {}


def _move_cats(con):
    if not _MOVE_CAT:
        _MOVE_CAT.update({r[0]: r[1] for r in con.execute("SELECT name_jp, category FROM move_master")})
    return _MOVE_CAT


def _moves_for_item(item, mpool, cats):
    if item not in CHOICE_ITEMS:
        return mpool[:4]
    ok = [m for m in mpool if cats.get(m) != "status" or m in CHOICE_OK_STATUS]
    return (ok or mpool)[:4]


def build_variants(con, name, tpl_of, normalize_mega_stone, max_variants=MAX_VARIANTS):
    """種 name の代表型(最大 max_variants)を作る。自分側・相手側の共通の唯一の入口。

    返す各型: {idx,item,nature,ability,ev,moves(表示用TOP4),mpool(技プールTOP10),
              t1,t2,bs,mega,label,spec}
    """
    tpl = tpl_of.get(name)
    if tpl is None:
        return []
    items = _items_of(con, name)
    natures = _natures_of(con, name)
    abilities = _abilities_of(con, name)
    evs = _evs_of(con, name)
    move_rows = _moves_of(con, name)
    if not evs or not move_rows:
        return []

    mpool = [m for m, _ in move_rows[:MOVE_POOL_N]]
    top_moves = mpool[:4]
    cats = _move_cats(con)
    base_ability = abilities[0][0] if abilities else ""

    axes = _ev_axis_groups(evs)
    if not axes:
        return []
    main_axes = [axes[0]] + [a for a in axes[1:] if a[2] >= AXIS_MIN_SHARE]

    cand_items = [(it, p) for it, p in items if p >= MIN_ITEM_PCT][:4]
    if not cand_items and items:
        cand_items = items[:1]

    joint = _joint_of(con, name)

    cands = []
    for item, ipct in cand_items:
        usable = [a for a in main_axes if _item_ok(item, a[1])]
        g = joint.get(item)
        if g and g["n"] >= MIN_JOINT_N:
            # 実構築でこの持ち物に付いた攻撃軸だけに絞る（周辺分布の掛け合わせによる偽の型を排除）
            obs = [a for a in usable if a[0] in g["axes"]]
            if obs:
                usable = obs
        else:
            mx = _mega_axis(tpl, item, normalize_mega_stone)
            if mx:
                obs = [a for a in usable if a[0] != ("C" if mx == "A" else "A")]
                if obs:
                    usable = obs
        if not usable:
            usable = main_axes[:1]           # 制約に合う軸が無くても持ち物自体は落とさない
        for ax, ev, share in usable[:MAX_PER_ITEM]:
            cands.append({"item": item, "ipct": ipct, "ev": ev, "share": share,
                          "axis": ax, "score": ipct * share})
    cands.sort(key=lambda c: -c["score"])

    # 攻撃軸のシェアは「使用者全体のうち何%がその軸か」なので、型を1つ採るたびに
    # その軸のシェアをその持ち物の採用率ぶん消費する。こうしないと、採用率80%のメガ石が
    # 特殊軸を占めている種で、残りの持ち物にも特殊軸を重複して割り当ててしまう
    # （カイリュー: メガ=特殊が全体の8割 → 残りの物理16%はいのちのたま等が担っている）。
    axis_left = {ax: share * 100.0 for ax, _, share in main_axes}

    out = []
    per_item = {}
    seen = set()
    used_natures = set()
    while len(out) < max_variants:
        avail = [c for c in cands
                 if per_item.get(c["item"], 0) < MAX_PER_ITEM
                 and (c["item"], tuple(c["ev"])) not in seen]
        if not avail:
            break
        c = max(avail, key=lambda c: c["ipct"] * max(axis_left.get(c["axis"], 0.0), 0.0))
        seen.add((c["item"], tuple(c["ev"])))
        axis_left[c["axis"]] = max(0.0, axis_left.get(c["axis"], 0.0) - c["ipct"])
        per_item[c["item"]] = per_item.get(c["item"], 0) + 1

        item, ev = c["item"], c["ev"]
        md = _mega_of(tpl, item, normalize_mega_stone)
        if md is not None:
            t1, t2 = md.type1, md.type2
            bs = [md.hp, md.attack, md.defense, md.sp_attack, md.sp_defense, md.speed]
            ability = md.ability or base_ability
            label = md.mega_name
        else:
            t1, t2 = tpl.type1, tpl.type2
            bs = [tpl.base_hp, tpl.base_attack, tpl.base_defense,
                  tpl.base_sp_attack, tpl.base_sp_defense, tpl.base_speed]
            ability = base_ability
            label = name
        nature, backed = _pick_nature_joint(joint.get(item), _ev_axis(ev), natures, ev)
        if not backed and nature in used_natures:
            nature = _nature_alt(natures, ev, used_natures) or nature
        used_natures.add(nature)
        mv4 = _moves_for_item(item, mpool, cats)
        spec = (f"{name}@{item}:{nature}:{'|'.join(mv4)}:"
                f"{'/'.join(str(x) for x in ev)}:{ability}")
        out.append({
            "idx": len(out) + 1, "item": item, "nature": nature, "ability": ability,
            "ev": list(ev), "moves": mv4, "mpool": mpool,
            "t1": t1, "t2": t2, "bs": bs, "mega": md is not None,
            "label": label, "spec": spec,
        })
    return out


def _stone_xy(item):
    if item.endswith(("X", "Ｘ")):
        return "X"
    if item.endswith(("Y", "Ｙ")):
        return "Y"
    return ""


def build_targets(con, usage_rows, tpl_of, variants_of, n=30):
    """使用率上位n体の「想定相手」。メガ進化が複数系統(X/Y)ある種は系統ごとに別エントリ。"""
    out = []
    for name, rank, pid in usage_rows[:n]:
        blds = variants_of.get(name) or []
        if not blds:
            continue
        # フォルム(タイプ+メガ有無)でグルーピング
        groups, order = {}, []
        for b in blds:
            f = (b["t1"], b["t2"], b["mega"])
            if f not in groups:
                groups[f] = []
                order.append(f)
            groups[f].append(b)

        xy = {}
        for f in order:
            if f[2]:
                suf = _stone_xy(groups[f][0]["item"])
                if suf:
                    xy.setdefault(suf, f)

        # stone: 同じiconで複数エントリに分かれる場合の識別子(TS側 preferItem)。
        entries = []
        if len(xy) >= 2:
            used_forms = set()
            for suf in sorted(xy):
                f = xy[suf]
                used_forms.add(f)
                # 表示名はメガ名(例: メガリザードンX)。X/Yでタイプ・種族値が別物なので
                # 「リザードン」1列にまとめず系統ごとに出す。
                entries.append((groups[f][0]["label"], groups[f], groups[f][0]["item"]))
            rest = [b for f in order if f not in used_forms for b in groups[f]]
            if rest:
                entries.append((name, rest, None))
        else:
            entries.append((name, blds, None))

        for label, bs, stone in entries:
            g = {"sp": name, "label": label, "icon": pid,
                 "builds": [dict(b, idx=i + 1) for i, b in enumerate(bs)]}
            if stone:
                g["stone"] = stone
            out.append(g)
    return out


def build_mon_files(con, usage_rows, variants_of):
    for name, rank, pid in usage_rows:
        items = [{"n": n, "pct": p} for n, p in _items_of(con, name)]
        abilities = [{"n": n, "pct": p} for n, p in _abilities_of(con, name)]
        natures = [{"n": n, "pct": p} for n, p in _natures_of(con, name)]
        evs = [{"ev": ev, "pct": p} for ev, p in _evs_of(con, name)]
        moves = [{"n": n, "pct": p} for n, p in _moves_of(con, name)]
        learnset = sorted(
            {r[0] for r in con.execute("SELECT move_jp FROM pokemon_learnsets WHERE pokemon_name=?", (name,))},
            key=kana_key)
        mu = variants_of.get(name) or []
        mon = {
            "n": name, "items": items, "abilities": abilities, "natures": natures,
            "evs": evs, "moves": moves, "learnset": learnset,
            # mu: 1v1判定に使う代表型(型1/2/3)。相手側(targets.json builds)と同一スキーマ。
            "mu": mu,
            # builds: 工房の「型プリセット」用spec文字列。muから生成(技はTOP4)。
            "builds": [b["spec"] for b in mu],
        }
        write_json(os.path.join(MON_DIR, f"{pid}.json"), mon)


def main():
    os.makedirs(MON_DIR, exist_ok=True)
    con = sqlite3.connect(DB)

    cd = con.execute(
        "SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule=?", (SEASON, RULE)
    ).fetchone()[0]
    # pokemon_id(アイコン/ファイル名キー)は日によっては全行NULLで入る(M-5 2026-08-11以降)。
    # 使用率順位は最新日から取りつつ、idは全期間の非NULL行から名前で補完する。
    icon_fix = {n: p for n, p in con.execute(
        "SELECT pokemon, pokemon_id FROM pokemon_usage WHERE pokemon_id IS NOT NULL ORDER BY crawled_date")}
    usage_rows = [(n, rk, pid or icon_fix.get(n)) for n, rk, pid in con.execute(
        "SELECT pokemon, rank, pokemon_id FROM pokemon_usage WHERE season=? AND rule=? AND crawled_date=? ORDER BY rank",
        (SEASON, RULE, cd)).fetchall()]
    missing = [n for n, _, pid in usage_rows if not pid]
    if missing:
        print("WARN pokemon_id未解決:", ", ".join(missing))
    usage_rows = [r for r in usage_rows if r[2]]

    from simulator.simulate import get_loader
    from simulator.data import normalize_mega_stone
    L = get_loader()

    species_list, tpl_of = build_species(con, L, usage_rows)
    write_json(os.path.join(OUT_DIR, "species.json"), species_list)

    moves_out = build_moves(con)
    write_json(os.path.join(OUT_DIR, "moves.json"), moves_out)

    items_out = build_items(con)
    write_json(os.path.join(OUT_DIR, "items.json"), items_out)

    variants_of = {}
    for name, rank, pid in usage_rows:
        variants_of[name] = build_variants(con, name, tpl_of, normalize_mega_stone)

    targets_out = build_targets(con, usage_rows, tpl_of, variants_of)
    write_json(os.path.join(OUT_DIR, "targets.json"), targets_out)

    build_mon_files(con, usage_rows, variants_of)

    con.close()
    nv = sum(len(v) for v in variants_of.values())
    empty = [n for n, v in variants_of.items() if not v]
    print(f"season={SEASON} species={len(species_list)} moves={len(moves_out)} items={len(items_out)} "
          f"targets={len(targets_out)} mon={len(usage_rows)} 型合計={nv} 型0件={len(empty)}")
    if empty:
        print("  型0件:", ", ".join(empty[:20]))


if __name__ == "__main__":
    main()
