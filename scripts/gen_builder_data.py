"""「パーティ構築」ページ用の静的データ生成：pokenavi.db(M-3, single, 各テーブルの最新crawled_date)
+ build_pool_M-3.md(型プリセット) から public/builder-data/*.json を生成する。
使い方: python3 scripts/gen_builder_data.py
"""
import os
import sqlite3
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DB = os.path.join(HERE, "pokenavi.db")
OUT_DIR = os.path.join(ROOT, "public", "builder-data")
MON_DIR = os.path.join(OUT_DIR, "mon")
SEASON = "M-3"
RULE = "single"


def kana_key(s):
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in s)


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))


def _latest_rows(con, table, col, name):
    q = f"""SELECT {col}, usage_rate FROM {table}
            WHERE season=? AND rule=? AND pokemon=?
            AND crawled_date=(SELECT MAX(crawled_date) FROM {table}
                               WHERE season=? AND rule=? AND pokemon=?)
            ORDER BY rank"""
    return con.execute(q, (SEASON, RULE, name, SEASON, RULE, name)).fetchall()


def _latest_ev_rows(con, name):
    q = """SELECT ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, usage_rate FROM pokemon_evs
           WHERE season=? AND rule=? AND pokemon=?
           AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_evs
                              WHERE season=? AND rule=? AND pokemon=?)
           ORDER BY rank"""
    return con.execute(q, (SEASON, RULE, name, SEASON, RULE, name)).fetchall()


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


def _build_bs(nm, item, is_mega, tpl_of, normalize_mega_stone):
    tpl = tpl_of[nm]
    if not is_mega:
        return tpl.type1, tpl.type2, [tpl.base_hp, tpl.base_attack, tpl.base_defense,
                                       tpl.base_sp_attack, tpl.base_sp_defense, tpl.base_speed]
    target = normalize_mega_stone(item)
    for md in tpl.mega_data.values():
        if normalize_mega_stone(md.mega_stone) == target:
            return md.type1, md.type2, [md.hp, md.attack, md.defense, md.sp_attack, md.sp_defense, md.speed]
    # 未解決(データ欠落)時は素の種族値にフォールバック
    return tpl.type1, tpl.type2, [tpl.base_hp, tpl.base_attack, tpl.base_defense,
                                   tpl.base_sp_attack, tpl.base_sp_defense, tpl.base_speed]


def build_targets(L, tpl_of, icon_of):
    from _explain import load_top_builds, _stone_xy
    from simulator.data import normalize_mega_stone

    tb = load_top_builds(L, n=30, k=3)
    out = []
    for nm, builds in tb:
        groups, order = {}, []
        for b in builds:
            f = b["form"]
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

        entries = []
        if len(xy) >= 2:
            used_forms = set()
            for suf in sorted(xy):
                f = xy[suf]
                used_forms.add(f)
                entries.append((f"{nm}{suf}", groups[f]))
            rest = [b for f in order if f not in used_forms for b in groups[f]]
            if rest:
                entries.append((nm, rest))
        else:
            entries.append((nm, builds))

        for label, blds in entries:
            out_builds = []
            for idx, v in enumerate(blds, 1):
                p = v["p"]
                is_mega = v["form"][2]
                t1, t2, bs = _build_bs(nm, v["item"], is_mega, tpl_of, normalize_mega_stone)
                ev = [int(x) for x in v["ev"].split("/")]
                moves = [m.name_jp for m in p.moves]
                ability = p.ability
                spec = f"{nm}@{v['item']}:{v['nature']}:{'|'.join(moves)}:{'/'.join(str(x) for x in ev)}:{ability}"
                out_builds.append({
                    "idx": idx, "item": v["item"], "nature": v["nature"], "ability": ability,
                    "ev": ev, "moves": moves, "t1": t1, "t2": t2, "bs": bs, "spec": spec,
                })
            out.append({"sp": nm, "label": label, "icon": icon_of.get(nm), "builds": out_builds})
    return out


def build_mon_files(con, usage_rows, pool):
    for name, rank, pid in usage_rows:
        items = [{"n": r[0], "pct": r[1]} for r in _latest_rows(con, "pokemon_items", "item", name)]
        abilities = [{"n": r[0], "pct": r[1]} for r in _latest_rows(con, "pokemon_abilities", "ability", name)]
        natures = [{"n": r[0], "pct": r[1]} for r in _latest_rows(con, "pokemon_natures", "nature", name)]
        evs = [{"ev": list(r[:6]), "pct": r[6]} for r in _latest_ev_rows(con, name)]
        moves = [{"n": r[0], "pct": r[1]} for r in _latest_rows(con, "pokemon_moves", "move", name)]
        learnset = sorted(
            {r[0] for r in con.execute("SELECT move_jp FROM pokemon_learnsets WHERE pokemon_name=?", (name,))},
            key=kana_key)
        builds = [name + s[s.index("@"):] if "@" in s else s for s in pool.get(name, [])[:5]]
        mon = {
            "n": name, "items": items, "abilities": abilities, "natures": natures,
            "evs": evs, "moves": moves, "learnset": learnset, "builds": builds,
        }
        write_json(os.path.join(MON_DIR, f"{pid}.json"), mon)


def main():
    os.makedirs(MON_DIR, exist_ok=True)
    con = sqlite3.connect(DB)

    cd = con.execute(
        "SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule=?", (SEASON, RULE)
    ).fetchone()[0]
    usage_rows = con.execute(
        "SELECT pokemon, rank, pokemon_id FROM pokemon_usage WHERE season=? AND rule=? AND crawled_date=? ORDER BY rank",
        (SEASON, RULE, cd)).fetchall()

    from simulator.simulate import get_loader
    L = get_loader()

    species_list, tpl_of = build_species(con, L, usage_rows)
    icon_of = {name: pid for name, rank, pid in usage_rows}
    write_json(os.path.join(OUT_DIR, "species.json"), species_list)

    moves_out = build_moves(con)
    write_json(os.path.join(OUT_DIR, "moves.json"), moves_out)

    items_out = build_items(con)
    write_json(os.path.join(OUT_DIR, "items.json"), items_out)

    targets_out = build_targets(L, tpl_of, icon_of)
    write_json(os.path.join(OUT_DIR, "targets.json"), targets_out)

    from gen_party_pool import parse_pool
    pool, _, _, _ = parse_pool()
    build_mon_files(con, usage_rows, pool)

    con.close()
    print(f"species={len(species_list)} moves={len(moves_out)} items={len(items_out)} "
          f"targets={len(targets_out)} mon={len(usage_rows)}")


if __name__ == "__main__":
    main()
