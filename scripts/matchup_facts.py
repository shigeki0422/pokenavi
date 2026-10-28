#!/usr/bin/env python3
"""
型内の性格・EV多様性を手計算・推測で見落とすミスをゼロにするための「事実ファイル」生成ツール。

これまでの失敗パターン：
  レビュー担当が「このポケモンはS169」のように1個体だけ代表値として記事を検算し、
  後から別のレビューが「実は型内にEVの違う個体が34%いて、Sは122だった」と気づく、
  という往復を何ラウンドも繰り返していた（ガブリアスM-7記事で多発）。

このツールは、型プールデータ（type_groups.json）から型内の性格×EVの組み合わせを
重みが一定以上のものは**全て**機械的に列挙し、実数値を計算する。
「代表個体1つだけ見て残りを推測する」ことをそもそも発生させない。

使い方:
  python3 scripts/matchup_facts.py ガブリアス
  python3 scripts/matchup_facts.py ガブリアス --group ステルスロック
  python3 scripts/matchup_facts.py フラエッテ(永遠) --min-weight 0.03
  python3 scripts/matchup_facts.py ガブリアス --json > facts_garchomp.json
  python3 scripts/matchup_facts.py ガブリアス --pool-version M-7/2026-10-15

出力される実数値は、このポケモンの記事を書く・レビューするときに**唯一の正**として使う。
別のPythonで再計算し直して微妙に違う値を出す、ということをやらない。

article_facts.py からは load_pool / build_matrix / nature_shares / derived_stat を import して使う。
"""
import argparse
import json
import math
import os
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pool_versions  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "scripts" / "pokenavi.db"

NATURE_BOOST = {
    "いじっぱり": ("attack", 1.1, "sp_attack", 0.9),
    "ようき": ("speed", 1.1, "sp_attack", 0.9),
    "おくびょう": ("speed", 1.1, "attack", 0.9),
    "ひかえめ": ("sp_attack", 1.1, "attack", 0.9),
    "わんぱく": ("defense", 1.1, "sp_attack", 0.9),
    "しんちょう": ("sp_defense", 1.1, "sp_attack", 0.9),
    "おだやか": ("sp_defense", 1.1, "attack", 0.9),
    "ずぶとい": ("defense", 1.1, "attack", 0.9),  # 攻撃↓防御↑系（簡易）
    "むじゃき": ("speed", 1.1, "sp_defense", 0.9),
    "てれや": ("defense", 1.1, "speed", 0.9),
    "のんき": ("defense", 1.1, "speed", 0.9),
    "ゆうかん": ("attack", 1.1, "speed", 0.9),
    "やんちゃ": ("attack", 1.1, "sp_defense", 0.9),
    "れいせい": ("sp_attack", 1.1, "speed", 0.9),
    "なまいき": ("sp_defense", 1.1, "speed", 0.9),
    "せっかち": ("speed", 1.1, "defense", 0.9),
    "さみしがり": ("attack", 1.1, "defense", 0.9),
    "うっかりや": ("sp_attack", 1.1, "sp_defense", 0.9),
    "おっとり": ("sp_attack", 1.1, "defense", 0.9),
    "おとなしい": ("sp_defense", 1.1, "defense", 0.9),
    "のうてんき": ("defense", 1.1, "sp_defense", 0.9),
    "ゆうかん": ("attack", 1.1, "speed", 0.9),
}
NEUTRAL_NATURES = {"がんばりや", "すなお", "てれや", "きまぐれ", "まじめ"}
STAT_KEYS = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]
STAT_LABEL = {"hp": "H", "attack": "A", "defense": "B", "sp_attack": "C", "sp_defense": "D", "speed": "S"}
EV_ORDER = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]  # type_groups.json の ev 配列順


def calc_stat(base, ev, nature_mod, is_hp=False):
    if is_hp:
        return math.floor((base * 2 + 31 + ev * 2) * 50 / 100) + 60
    # 公式どおり、性格補正をかける前に一度floorする（ここを省略すると.5の端数で
    # 1違う値が出ることがある。例：イエッサン(オス)基礎S95・EV32・おくびょうは
    # 161が正しいが、floorを1回しか挟まないと162になる誤りが実際に発生した）
    pre_nature = math.floor((base * 2 + 31 + ev * 2) * 50 / 100) + 5
    return math.floor(pre_nature * nature_mod)


def derived_stat(value, modifier):
    """実数値に持ち物/能力ランクの補正を掛けた値。modifier: 'こだわりスカーフ' | '+N段階' | '-N段階'"""
    if modifier == "こだわりスカーフ":
        return math.floor(value * 1.5)
    if modifier.endswith("段階"):
        n = int(modifier[:-2])
        if n >= 0:
            return math.floor(value * (2 + n) / 2)
        return math.floor(value * 2 / (2 - n))
    raise ValueError(f"unknown modifier: {modifier}")


def get_base_stats(conn, name):
    row = conn.execute(
        "SELECT pokemon_name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed "
        "FROM pokemon_base_stats WHERE pokemon_name = ?",
        (name,),
    ).fetchone()
    if row:
        return dict(zip(
            ["name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed"],
            row,
        ))
    return None


def get_mega_stats_by_item(conn, base_name, item):
    row = conn.execute(
        "SELECT mega_name_jp, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, ability "
        "FROM pokemon_mega_stats WHERE base_pokemon_jp = ? AND mega_stone = ?",
        (base_name, item),
    ).fetchone()
    if row:
        return dict(zip(
            ["name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "ability"],
            row,
        ))
    return None


def compute_real_stats(base_row, ev_list, nature):
    """ev_list は EV_ORDER の順（H,A,B,C,D,S）。戻り値は実数値dict。"""
    mods = {k: 1.0 for k in STAT_KEYS}
    boost = NATURE_BOOST.get(nature)
    if boost:
        up_stat, up_mul, down_stat, down_mul = boost
        mods[up_stat] = up_mul
        mods[down_stat] = down_mul
    out = {}
    for i, key in enumerate(EV_ORDER):
        base = base_row[key]
        ev = ev_list[i] if i < len(ev_list) else 0
        if key == "hp":
            out[key] = calc_stat(base, ev, 1.0, is_hp=True)
        else:
            out[key] = calc_stat(base, ev, mods[key])
    return out


def pool_path(version=None):
    version = version or pool_versions.pointer("page")
    return Path(pool_versions.path("type_groups", version)), version


def load_pool(version=None):
    p, _ = pool_path(version)
    if not p.exists():
        print(f"エラー: 型プールデータが見つかりません: {p}", file=sys.stderr)
        sys.exit(1)
    return json.loads(p.read_text(encoding="utf-8"))


def enumerate_builds(pokemon_entry, group_filter, min_group_share, min_weight_in_group):
    """型プールのgroupsから、閾値以上の(性格,EV,持ち物)組を列挙する。"""
    results = []
    for grp in pokemon_entry["groups"]:
        if group_filter and grp["name"] != group_filter:
            continue
        gshare = grp["share"]
        if gshare < min_group_share:
            continue
        builds = grp["builds"]
        total_w = sum(b["weight"] for b in builds) or 1.0
        buckets = {}
        for b in builds:
            key = (b["nature"], tuple(b["ev"]), b["item"])
            if key not in buckets:
                buckets[key] = {"weight": 0.0, "moves_votes": {}, "ability": b.get("ability")}
            buckets[key]["weight"] += b["weight"]
            mv = tuple(b["moves"])
            buckets[key]["moves_votes"][mv] = buckets[key]["moves_votes"].get(mv, 0) + b["weight"]
        for (nature, ev, item), info in buckets.items():
            frac_in_group = info["weight"] / total_w
            if frac_in_group < min_weight_in_group:
                continue
            best_moves = max(info["moves_votes"].items(), key=lambda kv: kv[1])[0]
            results.append({
                "group": grp["name"],
                "group_share": round(gshare * 100, 1),
                "nature": nature,
                "ev": list(ev),
                "item": item,
                "ability": info["ability"],
                "share_in_group_pct": round(frac_in_group * 100, 1),
                "share_overall_pct": round(gshare * frac_in_group * 100, 2),
                "representative_moves": list(best_moves),
            })
        results.sort(key=lambda r: -r["share_overall_pct"])
    return results


def nature_shares(pokemon_entry, group_filter=None, min_group_share=0.0):
    """型（系統）ごとの性格シェア（EVの違いを無視して集計）。{group: [(nature, pct), ...]}"""
    out = {}
    for grp in pokemon_entry["groups"]:
        if group_filter and grp["name"] != group_filter:
            continue
        if grp["share"] < min_group_share:
            continue
        builds = grp["builds"]
        total_w = sum(b["weight"] for b in builds) or 1.0
        nat_w = {}
        for b in builds:
            nat_w[b["nature"]] = nat_w.get(b["nature"], 0.0) + b["weight"]
        out[grp["name"]] = [(n, round(w / total_w * 100, 1)) for n, w in sorted(nat_w.items(), key=lambda kv: -kv[1])]
    return out


def _group(pokemon_entry, group_name):
    for grp in pokemon_entry["groups"]:
        if grp["name"] == group_name:
            return grp
    return None


def move_shares(pokemon_entry, group_name):
    """型内の技ごとの重み合計（%）。{move: pct}。型名の妥当性チェックと diff_movers の型帰属に使う。"""
    grp = _group(pokemon_entry, group_name)
    if not grp:
        return {}
    total_w = sum(b["weight"] for b in grp["builds"]) or 1.0
    w = {}
    for b in grp["builds"]:
        for mv in set(b["moves"]):
            w[mv] = w.get(mv, 0.0) + b["weight"]
    return {m: round(x / total_w * 100, 1) for m, x in sorted(w.items(), key=lambda kv: -kv[1])}


def item_shares(pokemon_entry, group_name):
    grp = _group(pokemon_entry, group_name)
    if not grp:
        return {}
    total_w = sum(b["weight"] for b in grp["builds"]) or 1.0
    w = {}
    for b in grp["builds"]:
        w[b["item"]] = w.get(b["item"], 0.0) + b["weight"]
    return {i: round(x / total_w * 100, 1) for i, x in sorted(w.items(), key=lambda kv: -kv[1])}


def build_shares(pokemon_entry, group_name):
    """型内の4技構成ごとの重み合計（%）。{"技|技|技|技"（ソート済み）: pct}。"""
    grp = _group(pokemon_entry, group_name)
    if not grp:
        return {}
    total_w = sum(b["weight"] for b in grp["builds"]) or 1.0
    w = {}
    for b in grp["builds"]:
        key = "|".join(sorted(b["moves"]))
        w[key] = w.get(key, 0.0) + b["weight"]
    return {k: round(x / total_w * 100, 1) for k, x in sorted(w.items(), key=lambda kv: -kv[1])}


def build_matrix(conn, pool, name, min_weight=0.03, group=None, min_group_share=0.0):
    """型プールの name について、閾値以上の(性格,EV,持ち物)組ごとの実数値付きレコードを返す。"""
    entry = pool[name]
    combos = enumerate_builds(entry, group, min_group_share, min_weight)
    base_normal = get_base_stats(conn, name)
    facts = []
    for c in combos:
        is_mega = "ナイト" in (c["item"] or "") or "メガ" in (c["item"] or "")
        base_row = base_normal
        species_label = name
        if is_mega:
            mega_row = get_mega_stats_by_item(conn, name, c["item"])
            if mega_row:
                base_row = mega_row
                species_label = mega_row["name"]
        if base_row is None:
            c["error"] = "base_stats_not_found"
            facts.append(c)
            continue
        real = compute_real_stats(base_row, c["ev"], c["nature"])
        c["species"] = species_label
        c["mega"] = bool(is_mega and species_label != name)
        c["types"] = [base_row["type1"], base_row.get("type2")]
        c["ability_actual"] = base_row.get("ability") or c["ability"]
        c["real_stats"] = {STAT_LABEL[k]: v for k, v in real.items()}
        facts.append(c)
    return facts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pokemon", help="type_groups.json のキー名（例: ガブリアス、フラエッテ(永遠)）")
    ap.add_argument("--group", default=None, help="特定の型（系統）名だけに絞る")
    ap.add_argument("--min-group-share", type=float, default=0.0, help="型（系統）share の下限（0-1）。既定0=全型")
    ap.add_argument("--min-weight", type=float, default=0.03, help="型内での(性格,EV,持ち物)組の重み下限（0-1、既定3%%）")
    ap.add_argument("--pool-version", default=None, help="型プールの版（例: M-7/2026-10-15）。既定は pool_versions.json の page")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    pool = load_pool(args.pool_version)
    if args.pokemon not in pool:
        print(f"エラー: '{args.pokemon}' は型プールに無い（新シーズン未クロール or 名称不一致）。", file=sys.stderr)
        print("利用可能な名前の例:", ", ".join(list(pool.keys())[:20]), "...", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    facts = build_matrix(conn, pool, args.pokemon, args.min_weight, args.group, args.min_group_share)
    conn.close()

    if args.json:
        print(json.dumps(facts, ensure_ascii=False, indent=2))
        return

    print(f"=== {args.pokemon} の型内(性格×EV×持ち物)全列挙（重み{args.min_weight*100:.0f}%以上） ===\n")
    for c in facts:
        rs = c.get("real_stats", {})
        stat_str = " ".join(f"{k}{v}" for k, v in rs.items())
        print(f"[{c['group']}（型share {c['group_share']}%）] "
              f"{c['nature']} EV{c['ev']} {c['item']} "
              f"— 型内{c['share_in_group_pct']}%/全体{c['share_overall_pct']}% "
              f"— {c.get('species','?')} {stat_str}")
    print(f"\n合計 {len(facts)} 組。この一覧に出てこない性格・EVの組み合わせは、")
    print("重み{:.0f}%未満なので記事中で代表値として扱わなくてよい（言及する場合は「少数派」であることを明記）。".format(args.min_weight * 100))

    print("\n--- 型ごとの性格シェア（EVの違いを無視して集計。個々のEV組が3%未満でも性格単位では大きい場合がある） ---")
    for grp_name, parts in nature_shares(pool[args.pokemon], args.group, args.min_group_share).items():
        parts_str = ", ".join(f"{n}{w:.1f}%" for n, w in parts)
        print(f"[{grp_name}] {parts_str}")


if __name__ == "__main__":
    main()
