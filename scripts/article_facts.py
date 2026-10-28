#!/usr/bin/env python3
"""記事1本分の「事実ファイル」を決定論的に生成する。LLMは数値を計算・記憶せず、ここから転記する。

入力: scripts/article_specs/<slug>.json（被写体・季節・型カード5要素。コミット対象）
出力: _local/article_facts/<slug>.json（IDつき原子事実）, <slug>.md（事実シート：ライターはこれだけ読む）,
      <slug>.subject_builds.json（エンジンに渡した自分側の型）, <slug>.engine.json（エンジン生出力）

数値の出所は3つだけ：
  - scripts/pokenavi.db（使用率/採用率/種族値/技・特性データ。detail_date = その季節の pokemon_moves 最新日に固定）
  - 型プール type_groups.json（型内の性格×EV×持ち物の分布。pool_versions の page 版）
  - 対戦エンジン（scripts/tests/dump_matchups_facts.ts）。サイトの1v1判定と同じもの
builder-data の採用率(%)はエンジンの多数派フィルタにだけ使い、事実には DB の値を使う。

使い方:
  python3 scripts/article_facts.py garchomp-analysis-m7
  python3 scripts/article_facts.py garchomp-analysis-m7 --skip-engine   # engine.json を再利用
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import matchup_facts as MF  # noqa: E402
import pool_versions  # noqa: E402
from simulator.data import get_type_effectiveness  # noqa: E402

DB_PATH = HERE / "pokenavi.db"
BUILDER = ROOT / "public" / "builder-data"
SPECS = HERE / "article_specs"
RULE = "single"
STAT_LETTERS = ["H", "A", "B", "C", "D", "S"]
STAGE_MULT = {1: 1.5, 2: 2.0, 3: 2.5, 4: 3.0, 5: 3.5, 6: 4.0}
TYPE_NAMES = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん",
              "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"]
ITEM_MULT = {"こだわりスカーフ": 1.5, "いのちのたま": 1.3, "こだわりハチマキ": 1.5, "こだわりメガネ": 1.5}

# 技の継続ターン数：まず move_master.effect_text から自動抽出する（move_duration_from_effect）。
# DBの効果文に数字が無い技（アンコール等、効果が実装側の分岐で決まるもの）だけ、ここに追加する
# （エンジン実装を直接読んで値を確認すること。記憶で追加しない）。
# LLM（ライター）はこの表を増やさない。facts に無い技は「ターン数を書かない」が正しい振る舞い。
MOVE_DURATION = {
    "アンコール": {
        "turns_min": 3, "turns_max": 4,
        "note": "アンコールを使った時点で相手が既にそのターンの行動を終えていれば3ターン、まだ行動していなければ4ターン",
        "source": "engine:scripts/simulator/battle.py:L2229",
    },
}


def die(msg):
    print(f"[article_facts] エラー: {msg}", file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------- spec -----

def load_spec(slug, spec_path=None):
    p = Path(spec_path) if spec_path else SPECS / f"{slug}.json"
    if not p.exists():
        die(f"spec が無い: {p}")
    spec = json.loads(p.read_text(encoding="utf-8"))
    spec.setdefault("slug", slug)
    for k in ("subject", "icon", "season", "cards"):
        if k not in spec:
            die(f"spec に {k} が無い")
    spec.setdefault("prev_season", None)
    spec.setdefault("majority_pct", 20)
    spec.setdefault("aliases", {})
    spec.setdefault("boosts", [])
    spec.setdefault("extra_pokemon", [])
    return spec


def validate_spec(conn, spec, mon):
    learnset = set(mon.get("learnset", []))
    for c in spec["cards"]:
        ev = c["ev"]
        if len(ev) != 6 or any(e < 0 or e > 32 for e in ev) or sum(ev) != 66:
            die(f"card {c['arch']}: EV は各0〜32・合計66 である必要がある: {ev}")
        if c["nature"] not in MF.NATURE_BOOST and c["nature"] not in MF.NEUTRAL_NATURES:
            die(f"card {c['arch']}: 未知の性格 {c['nature']}")
        for mv in c["moves"] + c.get("mpool", []):
            if learnset and mv not in learnset:
                die(f"card {c['arch']}: {mv} は learnset に無い")
        row = conn.execute("SELECT implemented FROM item_master WHERE name_jp=?", (c["item"],)).fetchone()
        if row is None or not row[0]:
            die(f"card {c['arch']}: 持ち物 {c['item']} は item_master で未実装/未登録")


# ---------------------------------------------------------------- db -------

def resolve_dates(conn, subject, season, detail_date=None):
    if detail_date is None:
        r = conn.execute("SELECT MAX(crawled_date) FROM pokemon_moves WHERE season=? AND rule=? AND pokemon=?",
                         (season, RULE, subject)).fetchone()
        detail_date = r[0] if r else None
    if not detail_date:
        die(f"{subject} の {season} 詳細クロール（pokemon_moves）が無い")
    return detail_date


def latest_date_leq(conn, table, pokemon, season, date):
    r = conn.execute(f"SELECT MAX(crawled_date) FROM {table} WHERE season=? AND rule=? AND pokemon=? AND crawled_date<=?",
                     (season, RULE, pokemon, date)).fetchone()
    return r[0] if r else None


def usage_rank(conn, pokemon, season, date):
    d = latest_date_leq(conn, "pokemon_usage", pokemon, season, date)
    if not d:
        return None, None, None
    r = conn.execute("SELECT rank, usage_rate FROM pokemon_usage WHERE season=? AND rule=? AND pokemon=? AND crawled_date=?",
                     (season, RULE, pokemon, d)).fetchone()
    return (r[0], r[1], d) if r else (None, None, None)


ADOPT_TABLES = {"move": ("pokemon_moves", "move"), "item": ("pokemon_items", "item"),
                "nature": ("pokemon_natures", "nature"), "ability": ("pokemon_abilities", "ability"),
                "ev": ("pokemon_evs", "ev_spread")}


MOVE_TABLE_MIN_PCT = 5.0


def adopt_rates(conn, pokemon, season, date):
    """{category: {name: rate}} をその日付（無ければ直近）で返す。"""
    out = {}
    for cat, (table, col) in ADOPT_TABLES.items():
        d = latest_date_leq(conn, table, pokemon, season, date)
        out[cat] = {}
        if not d:
            continue
        for name, rate in conn.execute(f"SELECT {col}, usage_rate FROM {table} WHERE season=? AND rule=? AND pokemon=? AND crawled_date=?",
                                       (season, RULE, pokemon, d)):
            out[cat][name] = rate
    return out


def partners(conn, pokemon, season, date):
    d = latest_date_leq(conn, "pokemon_partners", pokemon, season, date)
    if not d:
        return []
    return conn.execute("SELECT rank, partner FROM pokemon_partners WHERE season=? AND rule=? AND pokemon=? AND crawled_date=? ORDER BY rank",
                        (season, RULE, pokemon, d)).fetchall()


def move_rows(conn, names):
    out = {}
    for n in names:
        r = conn.execute("SELECT name_jp, type, category, power, priority, effect_text FROM move_master WHERE name_jp=?", (n,)).fetchone()
        if r:
            out[n] = dict(zip(["name", "type", "category", "power", "priority", "effect_text"], r))
    return out


def stage_changes(effect_text):
    """effect_text から (stat, n, direction) を抜く。例「自分の攻撃を2段階上げる。」
    「自分の防御を1段階下げ、素早さを1段階上げる。」のように、同一文内の後続の句が
    主体（自分/相手）を省略して前の句から引き継ぐ場合も、文単位で直前の主体を伝播させて拾う。"""
    import re
    out = []
    if not effect_text:
        return out
    stat_map = {"攻撃": "A", "防御": "B", "特攻": "C", "特防": "D", "素早さ": "S", "すばやさ": "S", "こうげき": "A", "ぼうぎょ": "B", "とくこう": "C", "とくぼう": "D"}
    # 「自分の特攻、特防、素早さを1段階上げる」（ちょうのまい）・「特攻と特防が1段階ずつ上がる」（めいそう）のように
    # 能力名を「、」「と」で並べる書き方もある。読点で句を切ると拾えなかった（2026-10-27 ウルガモスで derived_stat が0件）
    stat_list = r"(?:攻撃|防御|特攻|特防|素早さ|すばやさ|こうげき|ぼうぎょ|とくこう|とくぼう)"
    pat = re.compile(rf"(?:(自分|相手)の)?((?:{stat_list}[、・と]?)+)(?:を|が)(\d)段階(?:ずつ)?(上げ|下げ|上が|下が)")
    for sentence in re.split(r"。", effect_text):
        current_who = None
        for m in pat.finditer(sentence):
            current_who = m.group(1) or current_who
            if not current_who:
                continue
            stats, n, dirn = m.group(2), int(m.group(3)), m.group(4)
            for jp, letter in stat_map.items():
                if jp in stats:
                    out.append({"target": "self" if current_who == "自分" else "opp", "stat": letter, "value": n,
                                "direction": "up" if dirn.startswith("上") else "down"})
    return out


def move_duration_from_effect(effect_text):
    """effect_text から継続ターン数を抜く。例「2ターンの間ねむり状態になる。」→(2,2)。
    数値が1つだけなら min=max。DB記載の効果文に数字が無い技（アンコール等）はここでは拾えないので、
    呼び出し側で MOVE_DURATION（エンジン実装を直接確認した表）にフォールバックする。"""
    import re
    if not effect_text:
        return None
    m = re.search(r"(\d+)(?:〜(\d+))?ターン", effect_text)
    if not m:
        return None
    lo = int(m.group(1))
    hi = int(m.group(2)) if m.group(2) else lo
    return (lo, hi)


# ---------------------------------------------------------------- builds ---

def mega_row_for_item(conn, base_name, item):
    return MF.get_mega_stats_by_item(conn, base_name, item)


def species_forms(conn, sp):
    """種の通常形態＋メガ各形態 {name: row}。row は type1/type2/種族値（メガは ability も）。種が無ければ {}。"""
    b = MF.get_base_stats(conn, sp)
    if not b:
        return {}
    forms = {sp: b}
    for mr in conn.execute("SELECT mega_name_jp FROM pokemon_mega_stats WHERE base_pokemon_jp=?", (sp,)):
        mrow = conn.execute("SELECT mega_name_jp, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, ability FROM pokemon_mega_stats WHERE mega_name_jp=?", (mr[0],)).fetchone()
        forms[mr[0]] = dict(zip(["name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "ability"], mrow))
    return forms


def subject_target_builds(conn, spec, pool):
    base = MF.get_base_stats(conn, spec["subject"])
    if not base:
        die(f"{spec['subject']} の種族値が無い")
    entry = pool.get(spec["subject"])
    builds = []
    for i, c in enumerate(spec["cards"], start=1):
        mega = mega_row_for_item(conn, spec["subject"], c["item"])
        row = mega or base
        bs = [row["hp"], row["attack"], row["defense"], row["sp_attack"], row["sp_defense"], row["speed"]]
        share = None
        if entry and c.get("pool_group"):
            for g in entry["groups"]:
                if g["name"] == c["pool_group"]:
                    share = round(g["share"] * 100, 1)
        spec_str = f"{spec['subject']}@{c['item']}:{c['nature']}:{'|'.join(c['moves'])}:{'/'.join(str(e) for e in c['ev'])}:{c['ability']}"
        b = {
            "idx": i, "item": c["item"], "nature": c["nature"], "ability": c["ability"],
            "ev": c["ev"], "moves": c["moves"], "mpool": c.get("mpool", c["moves"]),
            "t1": row["type1"], "t2": row.get("type2"), "bs": bs, "mega": bool(mega),
            "label": row["name"] if mega else spec["subject"], "spec": spec_str,
            "arch": c["arch"], "archNo": i, "archSub": "",
        }
        if mega:
            b["mab"] = mega.get("ability")
        if share is not None:
            b["share"] = share
        builds.append(b)
    return builds


def run_engine(spec, builds_path, out_path):
    env = dict(os.environ, SUBJECT_ICON=spec["icon"], SUBJECT_BUILDS=str(builds_path), MAJORITY_PCT=str(spec["majority_pct"]))
    r = subprocess.run(["npx", "tsx", "scripts/tests/dump_matchups_facts.ts"], cwd=ROOT, env=env, capture_output=True, text=True)
    if r.returncode != 0:
        die(f"エンジン実行失敗:\n{r.stderr[-2000:]}")
    out_path.write_text(r.stdout, encoding="utf-8")
    return json.loads(r.stdout)


# ---------------------------------------------------------------- facts ----

class Facts:
    def __init__(self):
        self.items = []
        self.ids = set()

    def add(self, fid, kind, **kw):
        if fid in self.ids:
            return
        self.ids.add(fid)
        self.items.append({"id": fid, "kind": kind, **kw})


def ev_key(ev):
    return "-".join(str(e) for e in ev)


def build_all(spec, conn, pool, engine, detail_date, prev_date, out_dir, pool_version):
    F = Facts()
    subject = spec["subject"]
    season = spec["season"]
    prev = spec.get("prev_season")

    # --- 種族値（通常・メガ各形態）
    base = MF.get_base_stats(conn, subject)
    forms = {subject: base}
    for c in spec["cards"]:
        m = mega_row_for_item(conn, subject, c["item"])
        if m:
            forms[m["name"]] = m
    for name, row in forms.items():
        total = 0
        for letter, key in zip(STAT_LETTERS, MF.STAT_KEYS):
            F.add(f"base_stat/{name}/{letter}", "base_stat", pokemon=name, stat=letter, value=row[key])
            total += row[key]
        F.add(f"bst/{name}", "bst", pokemon=name, value=total)
        if name != subject:
            for letter, key in zip(STAT_LETTERS, MF.STAT_KEYS):
                F.add(f"mega_delta/{name}/{letter}", "mega_delta", pokemon=name, stat=letter, value=row[key] - base[key])
            F.add(f"bst_delta/{name}", "bst_delta", pokemon=name, value=total - sum(base[k] for k in MF.STAT_KEYS))
        F.add(f"types/{name}", "types", pokemon=name, value=[row["type1"], row.get("type2")])

    # --- 型カードの実数値
    cards = []
    for c in spec["cards"]:
        m = mega_row_for_item(conn, subject, c["item"])
        row = m or base
        real = MF.compute_real_stats(row, c["ev"], c["nature"])
        rs = {MF.STAT_LABEL[k]: v for k, v in real.items()}
        label = row["name"] if m else subject
        cards.append({**c, "real_stats": rs, "label": label, "mab": (m or {}).get("ability")})
        for letter, v in rs.items():
            F.add(f"real_stat/{label}/{c['nature']}/{ev_key(c['ev'])}/{c['item']}/{letter}", "real_stat",
                  pokemon=label, base_pokemon=subject, nature=c["nature"], ev=c["ev"], item=c["item"], arch=c["arch"], stat=letter, value=v, card=True)
        if c["item"] in ITEM_MULT and c["item"] == "こだわりスカーフ":
            F.add(f"derived_stat/{label}/{c['nature']}/{ev_key(c['ev'])}/{c['item']}/S/こだわりスカーフ", "derived_stat",
                  pokemon=label, nature=c["nature"], item=c["item"], arch=c["arch"], stat="S", modifier="こだわりスカーフ",
                  value=MF.derived_stat(rs["S"], "こだわりスカーフ"))
    # 積み技後の実数値（spec.boosts）
    mv_cache = {}
    for b in spec.get("boosts", []):
        card = next((x for x in cards if x["arch"] == b["arch"]), None)
        if not card:
            continue
        mr = move_rows(conn, [b["move"]]).get(b["move"])
        if not mr:
            continue
        for sc in stage_changes(mr["effect_text"]):
            if sc["target"] != "self" or sc["direction"] != "up":
                continue
            v = MF.derived_stat(card["real_stats"][sc["stat"]], f"+{sc['value']}段階")
            F.add(f"derived_stat/{card['label']}/{card['nature']}/{ev_key(card['ev'])}/{card['item']}/{sc['stat']}/{b['move']}", "derived_stat",
                  pokemon=card["label"], nature=card["nature"], item=card["item"], arch=card["arch"], stat=sc["stat"],
                  modifier=f"{b['move']}+{sc['value']}段階", value=v)

    # --- 型内マトリクス（被写体）と型・性格シェア
    arch_by_group = {c.get("pool_group"): c["arch"] for c in spec["cards"] if c.get("pool_group")}
    matrices = {}
    if subject in pool:
        entry = pool[subject]
        for g in entry["groups"]:
            arch = arch_by_group.get(g["name"], g["name"] + "型")
            F.add(f"arch_share/{subject}/{arch}", "arch_share", pokemon=subject, arch=arch, pool_group=g["name"], value=round(g["share"] * 100, 1))
        for gname, parts in MF.nature_shares(entry).items():
            arch = arch_by_group.get(gname, gname + "型")
            for nat, pct in parts:
                F.add(f"nature_share/{subject}/{arch}/{nat}", "nature_share", pokemon=subject, arch=arch, nature=nat, value=pct)
        # 型内の技・持ち物・4技構成のシェア（2026-10-18）。ライターが type_groups を手集計して gate:allow していた値
        # （60.7%が無関係な nature_share と偶然一致して通っていた）を事実として持つ。diff_movers の型帰属にも使う。
        for g in entry["groups"]:
            arch = arch_by_group.get(g["name"], g["name"] + "型")
            for mv, pct in MF.move_shares(entry, g["name"]).items():
                F.add(f"arch_move_share/{subject}/{arch}/{mv}", "arch_move_share", pokemon=subject, arch=arch, move=mv, value=pct)
            for it, pct in MF.item_shares(entry, g["name"]).items():
                F.add(f"arch_item_share/{subject}/{arch}/{it}", "arch_item_share", pokemon=subject, arch=arch, item=it, value=pct)
            for key, pct in MF.build_shares(entry, g["name"]).items():
                F.add(f"arch_build_share/{subject}/{arch}/{key}", "arch_build_share", pokemon=subject, arch=arch, moves=key.split("|"), value=pct)
        mat = MF.build_matrix(conn, pool, subject, 0.03)
        matrices[subject] = mat
        for r in mat:
            arch = arch_by_group.get(r["group"], r["group"] + "型")
            for letter, v in r["real_stats"].items():
                F.add(f"real_stat/{r['species']}/{r['nature']}/{ev_key(r['ev'])}/{r['item']}/{letter}", "real_stat",
                      pokemon=r["species"], base_pokemon=subject, nature=r["nature"], ev=r["ev"], item=r["item"], arch=arch,
                      stat=letter, value=v, share_in_group_pct=r["share_in_group_pct"], share_overall_pct=r["share_overall_pct"])
            if r["item"] == "こだわりスカーフ":
                F.add(f"derived_stat/{r['species']}/{r['nature']}/{ev_key(r['ev'])}/{r['item']}/S/こだわりスカーフ", "derived_stat",
                      pokemon=r["species"], nature=r["nature"], item=r["item"], arch=arch, stat="S", modifier="こだわりスカーフ",
                      value=MF.derived_stat(r["real_stats"]["S"], "こだわりスカーフ"))

    # --- 被写体の使用率・採用率（今季・前季）
    names_known = set(x[0] for x in conn.execute("SELECT DISTINCT pokemon FROM pokemon_usage WHERE season=? AND rule=? AND crawled_date=?", (season, RULE, detail_date)))
    rk, ur, _ = usage_rank(conn, subject, season, detail_date)
    if rk is not None:
        F.add(f"usage_rank/{subject}", "usage_rank", pokemon=subject, value=rk, date=detail_date)
        F.add(f"usage_rate/{subject}", "usage_rate", pokemon=subject, value=ur, date=detail_date)
    cur = adopt_rates(conn, subject, season, detail_date)
    prv = adopt_rates(conn, subject, prev, prev_date) if prev and prev_date else {k: {} for k in ADOPT_TABLES}
    for cat in ADOPT_TABLES:
        for name, rate in cur[cat].items():
            F.add(f"adopt/{cat}/{subject}/{name}/{season}", "adopt_rate", category=cat, pokemon=subject, name=name, season=season, value=rate)
        for name, rate in prv[cat].items():
            F.add(f"adopt/{cat}/{subject}/{name}/{prev}", "adopt_rate", category=cat, pokemon=subject, name=name, season=prev, value=rate)
        for name in set(cur[cat]) | set(prv[cat]):
            a, b = prv[cat].get(name), cur[cat].get(name)
            if a is not None and b is not None:
                F.add(f"adopt_diff/{cat}/{subject}/{name}", "adopt_rate_diff", category=cat, pokemon=subject, name=name,
                      **{"from": prev, "to": season}, value=round(b - a, 1))
    if prev and prev_date:
        # 前季の順位は最終日の値（2026-10-28：詳細クロールの最終日 9/23 の順位を使い、M-6最終 10/7 と69記事で食い違った。
        # 採用率の比較は詳細クロールがある prev_date のまま）
        prk, pur, prd = usage_rank(conn, subject, prev, "9999-12-31")
        if prk is not None:
            F.add(f"usage_rank/{subject}/{prev}", "usage_rank", pokemon=subject, season=prev, value=prk, date=prd)
    partner_list = [p for _, p in partners(conn, subject, season, detail_date)]
    for rank, partner in partners(conn, subject, season, detail_date):
        F.add(f"partner/{subject}/{partner}", "partner_rank", pokemon=subject, partner=partner, value=rank)

    # --- 相手（エンジンの targets ＋ extra_pokemon）
    opp_groups = engine.get("publishable", []) + engine.get("excluded", [])
    opp_sps = []
    aliases = {}
    for g in opp_groups:
        sp, label = g["sp"], g["name"]
        if sp not in opp_sps:
            opp_sps.append(sp)
        if label != sp:
            aliases[label] = sp
    for x in spec.get("extra_pokemon", []):
        if x not in opp_sps:
            opp_sps.append(x)
    canonical = list(forms.keys()) + [g["name"] for g in opp_groups] + opp_sps + list(spec.get("extra_pokemon", [])) + partner_list
    for a, canon in spec.get("aliases", {}).items():
        for al in canon:
            aliases[al] = a
    for mega_name, base_name in conn.execute("SELECT mega_name_jp, base_pokemon_jp FROM pokemon_mega_stats"):
        if base_name in opp_sps or base_name == subject or base_name in partner_list:
            aliases.setdefault(mega_name, base_name)
            canonical.append(mega_name)
    # --- 同居率パートナー（通常＋メガ各形態）のタイプと、メガ石判定用の持ち物採用率（2026-10-18）。
    # partner_cover ブロックの倍率計算に使う。従来はパートナーが相手側（TOP30）に重なっているときだけ
    # 偶然 types が存在していた。
    for partner in partner_list:
        for name, row in species_forms(conn, partner).items():
            F.add(f"types/{name}", "types", pokemon=name, value=[row["type1"], row.get("type2")])
    # メガ石→メガ形態の対応（被写体・相手・パートナー）。partner_cover がメガ石採用率から形態を選ぶのに使う
    for mega_name, base_name, stone in conn.execute("SELECT mega_name_jp, base_pokemon_jp, mega_stone FROM pokemon_mega_stats"):
        if base_name in opp_sps or base_name == subject or base_name in partner_list:
            F.add(f"mega_form/{base_name}/{mega_name}", "mega_form", pokemon=base_name, form=mega_name, stone=stone)
        if partner not in opp_sps:
            for name, rate in adopt_rates(conn, partner, season, detail_date)["item"].items():
                F.add(f"adopt/item/{partner}/{name}/{season}", "adopt_rate", category="item", pokemon=partner, name=name, season=season, value=rate)
    # 「イダイトウ(オス)」→「イダイトウ」のような括弧抜き
    for n in list(canonical):
        if "(" in n:
            aliases.setdefault(n.split("(")[0], n)
    for sp in opp_sps:
        rk, ur, _ = usage_rank(conn, sp, season, detail_date)
        if rk is not None:
            F.add(f"usage_rank/{sp}", "usage_rank", pokemon=sp, value=rk, date=detail_date)
            F.add(f"usage_rate/{sp}", "usage_rate", pokemon=sp, value=ur, date=detail_date)
        rates = adopt_rates(conn, sp, season, detail_date)
        for cat in ADOPT_TABLES:
            for name, rate in rates[cat].items():
                F.add(f"adopt/{cat}/{sp}/{name}/{season}", "adopt_rate", category=cat, pokemon=sp, name=name, season=season, value=rate)
        forms_opp = species_forms(conn, sp)
        if forms_opp:
            for name, row in forms_opp.items():
                for letter, key in zip(STAT_LETTERS, MF.STAT_KEYS):
                    F.add(f"base_stat/{name}/{letter}", "base_stat", pokemon=name, stat=letter, value=row[key])
                F.add(f"types/{name}", "types", pokemon=name, value=[row["type1"], row.get("type2")])
        if sp in pool:
            mat = MF.build_matrix(conn, pool, sp, 0.03)
            matrices[sp] = mat
            for g in pool[sp]["groups"]:
                F.add(f"arch_share/{sp}/{g['name']}型", "arch_share", pokemon=sp, arch=g["name"] + "型", pool_group=g["name"], value=round(g["share"] * 100, 1))
            for gname, parts in MF.nature_shares(pool[sp]).items():
                for nat, pct in parts:
                    F.add(f"nature_share/{sp}/{gname}型/{nat}", "nature_share", pokemon=sp, arch=gname + "型", nature=nat, value=pct)
            for r in mat:
                for letter, v in r["real_stats"].items():
                    F.add(f"real_stat/{r['species']}/{r['nature']}/{ev_key(r['ev'])}/{r['item']}/{letter}", "real_stat",
                          pokemon=r["species"], base_pokemon=sp, nature=r["nature"], ev=r["ev"], item=r["item"], arch=r["group"] + "型",
                          stat=letter, value=v, share_in_group_pct=r["share_in_group_pct"], share_overall_pct=r["share_overall_pct"])
                if r["item"] == "こだわりスカーフ":
                    F.add(f"derived_stat/{r['species']}/{r['nature']}/{ev_key(r['ev'])}/{r['item']}/S/こだわりスカーフ", "derived_stat",
                          pokemon=r["species"], nature=r["nature"], item=r["item"], arch=r["group"] + "型", stat="S", modifier="こだわりスカーフ",
                          value=MF.derived_stat(r["real_stats"]["S"], "こだわりスカーフ"))

    # --- 対面（エンジン行）
    all_moves = set()
    for c in spec["cards"]:
        all_moves |= set(c["moves"]) | set(c.get("mpool", []))
    row_types = {}  # label -> (t1,t2)
    for g in opp_groups:
        sp, label = g["sp"], g["name"]
        F.add(f"verdict/{label}", "verdict", opp=label, opp_sp=sp, value=g["verdict"], reasons=g.get("reasons", []),
              stone=g.get("stone"))
        rep = g.get("representative")
        sp_rates = adopt_rates(conn, sp, season, detail_date)
        for i, r in enumerate(g["allRows"], start=1):
            my, op = r["my"], r["opp"]
            is_rep = rep is not None and rep["my"] == my and rep["opp"] == op and rep["myMove"] == r["myMove"]
            fid = f"mu/{my['arch'] or my['item']}/{label}#{op.get('idx') or i}/{op['item']}/{op['nature']}"
            my_rate = cur["move"].get(r["myMove"]) if r["myMove"] else None
            opp_rate = sp_rates["move"].get(r["oppMove"]) if r["oppMove"] else None
            F.add(fid, "matchup", opp=label, opp_sp=sp, opp_icon=g["icon"], opp_label=op["label"], opp_idx=op.get("idx"),
                  opp_item=op["item"], opp_nature=op["nature"], opp_ev=op["ev"], opp_ability=op["ability"], opp_mega=op["mega"],
                  opp_share=op.get("share"), opp_stats=op["stats"],
                  my_arch=my["arch"], my_item=my["item"], my_nature=my["nature"], my_ev=my["ev"], my_label=my["label"], my_mega=my["mega"],
                  my_move=r["myMove"], my_move_rate=my_rate, my_move_prio=r.get("myMovePrio"), my_hits=r["myHits"], my_certain=r["myCertain"],
                  my_prob=r["myProb"], my_prob_int=r.get("myProbInt"), my_pct_lo=r["myPctLo"], my_pct_hi=r["myPctHi"],
                  my_dmg_lo=r.get("myDmgLo"), my_dmg_hi=r.get("myDmgHi"), my_reason=r["myReason"], my_eff=r.get("myEff"),
                  opp_move=r["oppMove"], opp_move_rate=opp_rate, opp_move_prio=r.get("oppMovePrio"), opp_hits=r["oppHits"], opp_certain=r["oppCertain"],
                  opp_prob=r["oppProb"], opp_prob_int=r.get("oppProbInt"), opp_pct_lo=r["oppPctLo"], opp_pct_hi=r["oppPctHi"],
                  opp_dmg_lo=r.get("oppDmgLo"), opp_dmg_hi=r.get("oppDmgHi"), opp_reason=r["oppReason"], opp_eff=r.get("oppEff"),
                  my_s=r["myS"], opp_s=r["oppS"], fast=r["fast"], ko_first=r["koFirst"], ko_by_priority=r["koByPriority"],
                  my_ko_move=r.get("myKoMove"), my_ko_move_prio=r.get("myKoMovePrio"),
                  opp_ko_move=r.get("oppKoMove"), opp_ko_move_prio=r.get("oppKoMovePrio"),
                  win=r["win"], sym=r["sym"], representative=is_rep, verdict=g["verdict"])
            for mv in (r.get("myKoMove"), r.get("oppKoMove")):
                if mv:
                    all_moves.add(mv)
            for mv in (r["myMove"], r["oppMove"]):
                if mv:
                    all_moves.add(mv)
            # 相手側の実数値も事実に（エンジン計算値。Python側と一致することを consistency_asserts で確認）
            for letter, v in zip(STAT_LETTERS, op["stats"]):
                F.add(f"real_stat/{op['label']}/{op['nature']}/{ev_key(op['ev'])}/{op['item']}/{letter}", "real_stat",
                      pokemon=op["label"], base_pokemon=sp, nature=op["nature"], ev=op["ev"], item=op["item"], stat=letter, value=v, engine=True)
        # 相手の多数派技も技データに
        for n, rate in sp_rates["move"].items():
            if rate >= spec["majority_pct"]:
                all_moves.add(n)

    # 被写体が採用する技（採用率5%以上）も技データに（技表 move_table を生成するため。2026-10-25）
    for n, rate in adopt_rates(conn, subject, spec["season"], detail_date)["move"].items():
        if rate >= MOVE_TABLE_MIN_PCT:
            all_moves.add(n)
    # --- 技データ
    for n, mr in move_rows(conn, sorted(all_moves)).items():
        F.add(f"move_power/{n}", "move_power", move=n, type=mr["type"], category=mr["category"], value=mr["power"])
        F.add(f"move_priority/{n}", "move_priority", move=n, value=mr["priority"])
        for sc in stage_changes(mr["effect_text"]):
            F.add(f"stage_change/{n}/{sc['target']}/{sc['stat']}", "stage_change", move=n, target=sc["target"], stat=sc["stat"],
                  value=sc["value"], direction=sc["direction"], effect_text=mr["effect_text"])
        F.add(f"move_effect/{n}", "move_effect", move=n, value=mr["effect_text"])
        db_dur = move_duration_from_effect(mr["effect_text"])
        if db_dur:
            F.add(f"move_duration/{n}", "move_duration", move=n, turns_min=db_dur[0], turns_max=db_dur[1],
                  note=mr["effect_text"], source="move_master.effect_text")
        elif n in MOVE_DURATION:
            d = MOVE_DURATION[n]
            F.add(f"move_duration/{n}", "move_duration", move=n, turns_min=d["turns_min"], turns_max=d["turns_max"],
                  note=d["note"], source=d["source"])
    # --- 持ち物の効果（DB item_master.effect_text）。被写体の採用持ち物と型カードの持ち物。
    # 2026-10-25 ゴリランダーのグラスシード：効果が事実に無く、型カードで「持ち物が違う」としか書けなかった
    item_names = {c["item"] for c in spec["cards"]} | {f["name"] for f in F.items
                                                        if f["kind"] == "adopt_rate" and f.get("category") == "item" and f.get("pokemon") == subject}
    for n in sorted(i for i in item_names if i):
        row = conn.execute("SELECT effect_text FROM item_master WHERE name_jp=?", (n,)).fetchone()
        if row and row[0]:
            F.add(f"item_effect/{n}", "item_effect", item=n, value=row[0])
    move_types = {n: mr["type"] for n, mr in move_rows(conn, sorted(all_moves)).items()}

    # --- タイプ相性（登場する技タイプ × 防御側の各形態）
    defenders = {}
    for f in F.items:
        if f["kind"] == "types":
            defenders[f["pokemon"]] = f["value"]
    for atk in sorted(set(move_types.values())):
        for dname, (t1, t2) in defenders.items():
            F.add(f"type_eff/{atk}/{dname}", "type_eff", atk_type=atk, defender=dname, value=get_type_effectiveness(atk, t1, t2))
    # タイプ表そのもの（「はがねタイプにはほのお×2」のような防御タイプ名での主張の照合用。2026-10-18）
    for atk in TYPE_NAMES:
        for dt in TYPE_NAMES:
            F.add(f"type_chart/{atk}/{dt}", "type_chart", atk_type=atk, def_type=dt, value=get_type_effectiveness(atk, dt, None))

    # --- 定数
    for n, mult in STAGE_MULT.items():
        F.add(f"const/stage_mult/{n}", "const", name=f"{n}段階", value=mult)
    for item, mult in ITEM_MULT.items():
        F.add(f"const/item_mult/{item}", "const", name=item, value=mult)
    # --- 特性の効果文（被写体の特性）と、効果文中の倍率（「威力が1.3倍」）。2026-10-18
    import re as _re
    ability_names = {f["name"] for f in F.items if f["kind"] == "adopt_rate" and f["category"] == "ability" and f["pokemon"] == subject}
    ability_names |= {c["mab"] for c in cards if c.get("mab")}  # メガ後の特性（かたいツメ等）も
    for ab in sorted(ability_names):
        r = conn.execute("SELECT effect_text FROM ability_master WHERE name_jp=?", (ab,)).fetchone()
        if not r or not r[0]:
            continue
        F.add(f"ability_effect/{ab}", "ability_effect", ability=ab, value=r[0])
        for m in _re.finditer(r"(\d+(?:\.\d+)?)倍", r[0]):
            F.add(f"const/ability_mult/{ab}/{m.group(1)}", "const", name=ab, value=float(m.group(1)), source="ability_master.effect_text")

    names = {
        "canonical": sorted(set(canonical)),
        "aliases": aliases,
        "known": sorted(names_known),
        "moves": sorted(all_moves),
        "items": sorted({f["name"] for f in F.items if f["kind"] == "adopt_rate" and f["category"] == "item"} | {c["item"] for c in spec["cards"]}),
        "arches": sorted({f["arch"] for f in F.items if f.get("arch")}),
        "natures": sorted(MF.NATURE_BOOST.keys() | MF.NEUTRAL_NATURES),
        "abilities": sorted({f["name"] for f in F.items if f["kind"] == "adopt_rate" and f["category"] == "ability"}),
    }
    return F, cards, names, matrices


def consistency_asserts(spec, cards, engine, conn, detail_date, check_builder=True):
    problems = []
    # 1) エンジンの自分側実数値 = Python の実数値
    eng_builds = {b["arch"]: b for b in engine["subject"]["builds"]}
    for c in cards:
        eb = eng_builds.get(c["arch"])
        if not eb:
            problems.append(f"エンジン出力に型 {c['arch']} が無い")
            continue
        py = [c["real_stats"][l] for l in STAT_LETTERS]
        if py != eb["stats"]:
            problems.append(f"{c['arch']}: 実数値がエンジンとPythonで不一致 python={py} engine={eb['stats']}")
    # 2) builder-data の多数派技集合 = DB(detail_date) の多数派技集合
    # --skip-engine で再利用したエンジン出力は当時の builder-data で計算済み（その時点で照合済み）。
    # 現在の builder-data が新しいクロールに進んでいても再利用分とは無関係なので照合しない。
    mon = json.loads((BUILDER / "mon" / f"{spec['icon']}.json").read_text(encoding="utf-8"))
    bd = {e["n"] for e in mon.get("moves", []) if e["pct"] >= spec["majority_pct"]}
    db = {n for n, r in adopt_rates(conn, spec["subject"], spec["season"], detail_date)["move"].items() if r >= spec["majority_pct"]}
    if check_builder and bd != db:
        problems.append(f"多数派技集合が builder-data と DB({detail_date}) で不一致: builder={sorted(bd)} db={sorted(db)}")
    if problems:
        die("整合性チェック失敗:\n  " + "\n  ".join(problems))


# ---------------------------------------------------------------- sheet ----

def write_sheet(path, spec, out, cards, matrices, warnings=()):
    L = []
    s = out["sources"]
    fid = lambda f: f" `{f}`"
    L.append(f"# 事実シート: {spec['slug']}\n")
    L.append("このシートに無い数値は記事に書かない。書きたい数値が無ければ spec を直して再生成する。")
    L.append("苦手/得意表・型ごとの有利不利・パートナーの耐性・採用率変化の型帰属は `render_sections.py` が生成する。本文で言い直さない。\n")
    if warnings:
        L.append("## spec の注意（article_spec_check）")
        for w in warnings:
            L.append(f"- {w}")
        L.append("")
    L.append("## 0. 日付・版")
    L.append(f"- 採用率・使用率の基準日（detail_date）: {s['detail_date']}（本文の「※本記事の…データは{s['detail_date']}時点」と一致させる）")
    L.append(f"- 前シーズン {s['prev_season']} の基準日: {s['prev_detail_date']}")
    L.append(f"- 型プール版: {s['pool_version']} / 多数派しきい値: {s['majority_pct']}%\n")

    facts = out["facts"]
    by_kind = {}
    for f in facts:
        by_kind.setdefault(f["kind"], []).append(f)
    # シートに載せる相手は「表に出る相手（win/lose）」と extra_pokemon だけ（除外30体の全マトリクスを載せると
    # ライターが読めない量になる。ゲート用の JSON には全件入っている）
    keep_opps = {v["opp_sp"] for v in by_kind.get("verdict", []) if v["value"] in ("win", "lose")} | set(spec.get("extra_pokemon", []))
    keep_labels = {v["opp"] for v in by_kind.get("verdict", []) if v["value"] in ("win", "lose")}
    matrices = {k: v for k, v in matrices.items() if k == spec["subject"] or k in keep_opps}

    L.append("## 1. 種族値")
    for pk in out["subject"]["forms"]:
        bs = {f["stat"]: f for f in by_kind.get("base_stat", []) if f["pokemon"] == pk}
        tot = next((f for f in by_kind.get("bst", []) if f["pokemon"] == pk), None)
        L.append(f"- {pk}: " + " ".join(f"{l}{bs[l]['value']}" for l in STAT_LETTERS if l in bs) + (f" 合計{tot['value']}" if tot else "") + fid(f"base_stat/{pk}/*"))
        deltas = [f for f in by_kind.get("mega_delta", []) if f["pokemon"] == pk]
        if deltas:
            L.append("  - 通常との差分: " + " ".join(f"{f['stat']}{f['value']:+d}" for f in deltas) + fid(f"mega_delta/{pk}/*"))
    L.append("")

    L.append("## 2. 型カード（5要素＋実数値）")
    for c in cards:
        rs = c["real_stats"]
        L.append(f"### {c['arch']}（{c['label']}）")
        L.append(f"- 特性 {c['ability']}" + (f"（メガ後 {c['mab']}）" if c.get("mab") else "") + f" / 性格 {c['nature']} / EV {'-'.join(l+str(e) for l,e in zip(STAT_LETTERS, c['ev']) if e)} / 持ち物 {c['item']}")
        L.append(f"- 技 {'・'.join(c['moves'])}（選択候補: {'・'.join(c.get('mpool', []))}）")
        L.append("- 実数値 " + " ".join(f"{l}{rs[l]}" for l in STAT_LETTERS) + fid(f"real_stat/{c['label']}/{c['nature']}/{ev_key(c['ev'])}/{c['item']}/*"))
        for f in by_kind.get("derived_stat", []):
            if f.get("arch") == c["arch"] and f["pokemon"] == c["label"] and f["nature"] == c["nature"]:
                L.append(f"  - {f['modifier']} 後の{f['stat']}: {f['value']}" + fid(f["id"]))
    L.append("")

    # 型シェア・性格シェア・型内技シェア・個体シェアは型プール推定値。記事に書かないので（2026-10-16・10-25）
    # シートにも出さない（出すと書き手が転記する。golisopod「型内技シェア65.2%」で再発）。
    L.append("## 3. 型内マトリクス（性格×EV×持ち物、重み3%以上。型内%/全体%は推定値で記事に書かない）")
    for pk, mat in matrices.items():
        L.append(f"### {pk}")
        for r in mat:
            rs = r["real_stats"]
            L.append(f"- [{r['group']}] {r['nature']} EV{'-'.join(l+str(e) for l,e in zip(STAT_LETTERS, r['ev']) if e)} {r['item']} — 型内{r['share_in_group_pct']}%/全体{r['share_overall_pct']}% — "
                     + " ".join(f"{l}{rs[l]}" for l in STAT_LETTERS))
    L.append("")

    subj = out["subject"]["name"]
    L.append(f"## 4. 採用率（{subj}、{s['detail_date']}時点）")
    for cat, jp in (("move", "技"), ("item", "持ち物"), ("nature", "性格"), ("ability", "特性"), ("ev", "EV")):
        cur = {f["name"]: f["value"] for f in by_kind.get("adopt_rate", []) if f["pokemon"] == subj and f["category"] == cat and f["season"] == spec["season"]}
        prv = {f["name"]: f["value"] for f in by_kind.get("adopt_rate", []) if f["pokemon"] == subj and f["category"] == cat and f["season"] == spec.get("prev_season")}
        dif = {f["name"]: f["value"] for f in by_kind.get("adopt_rate_diff", []) if f["pokemon"] == subj and f["category"] == cat}
        L.append(f"### {jp}")
        for n, v in sorted(cur.items(), key=lambda kv: -kv[1]):
            extra = ""
            if n in prv:
                extra = f"（{spec.get('prev_season')}: {prv[n]}% → {dif.get(n, 0):+.1f}pt）"
            L.append(f"- {n}: {v}%{extra}" + fid(f"adopt/{cat}/{subj}/{n}/{spec['season']}"))
    L.append("")

    L.append("## 5. 使用率順位・同居率")
    for f in by_kind.get("usage_rank", []):
        L.append(f"- {f['pokemon']}" + (f"（{f['season']}）" if f.get("season") else "") + f": {f['value']}位" + fid(f["id"]))
    for f in by_kind.get("partner_rank", []):
        L.append(f"- 同居率{f['value']}位: {f['partner']}" + fid(f["id"]))
    L.append("")

    L.append("## 6. 対面判定（エンジン。苦手/得意表の行は render_matchup_rows.py の出力をそのまま貼る）")
    excluded = [v["opp"] for v in by_kind.get("verdict", []) if v["value"] == "mixed"]
    if excluded:
        L.append("- 表に載せない相手（代表型で勝敗が割れる等。確定数を本文に書かない）: " + "、".join(excluded))
    # mixed（型で勝敗が割れる）相手のうち使用率20位以内は、extra_pokemon に書かなくても個体別の行を出す
    # （2026-10-18。以前は extra_pokemon に書かないと事実シートに出ず、ライターが13回目に自分で追加していた）。
    rank_of = {f["pokemon"]: f["value"] for f in by_kind.get("usage_rank", []) if not f.get("season")}
    extra_opps = {v["opp"] for v in by_kind.get("verdict", [])
                  if v["opp_sp"] in set(spec.get("extra_pokemon", [])) or (v["value"] == "mixed" and (rank_of.get(v["opp_sp"]) or 999) <= 20)}
    if extra_opps:
        L.append("- 上記のうち使用率20位以内または spec.extra_pokemon の相手は、型・個体ごとの全組み合わせを以下に表示する（型によって勝敗が割れる個体は arch_diff ブロックが生成する。本文で個別に書き直さないこと）: " + "、".join(sorted(extra_opps)))
    for v in by_kind.get("verdict", []):
        if v["opp"] not in keep_labels and v["opp"] not in extra_opps:
            continue
        L.append(f"### {v['opp']} — {v['value']}" + (f"（除外理由: {'、'.join(v['reasons'])}）" if v["reasons"] else ""))
        rows = [f for f in by_kind.get("matchup", []) if f["opp"] == v["opp"]]
        for f in rows:
            ko = lambda c, h, p: ("確定" if c else "乱数") + f"{h}発" + ("" if c or p is None else f"（{p}）") if h is not None and h < 999 else "倒せない"
            # 2026-10-18: 技が無い(my_move=None)・採用率が無い(move_rate=None)・倒せない(pct_lo/hi=None)
            # 場合に、そのまま f-string に渡すと「相手:None(None%)」「None〜None%」という事実シートとして
            # 誤読を招く文字列が出ていた（mimikyuのextra_pokemon対面で発覚）。None は言葉で表す。
            def move_txt(move, rate):
                if move is None:
                    return "有効な攻撃技なし"
                return f"{move}({rate}%)" if rate is not None else f"{move}(採用率不明)"
            def pct_txt(lo, hi):
                if lo is None or hi is None:
                    return ""
                return f" {lo}〜{hi}%"
            L.append(f"- {'★' if f['representative'] else '　'}{f['my_arch']} vs {f['opp_label']}({f['opp_nature']}/{f['opp_item']}) "
                     f"自分:{move_txt(f['my_move'], f['my_move_rate'])} {ko(f['my_certain'], f['my_hits'], f.get('my_prob_int'))}{pct_txt(f['my_pct_lo'], f['my_pct_hi'])}{'['+f['my_reason']+']' if f['my_reason'] else ''} / "
                     f"相手:{move_txt(f['opp_move'], f['opp_move_rate'])} {ko(f['opp_certain'], f['opp_hits'], f.get('opp_prob_int'))}{pct_txt(f['opp_pct_lo'], f['opp_pct_hi'])}{'['+f['opp_reason']+']' if f['opp_reason'] else ''} / "
                     f"S{f['my_s']}対S{f['opp_s']} {'先手' if f['fast'] else '後手'}"
                     + (f"(優先度: 自分{f.get('my_ko_move')}/相手{f.get('opp_ko_move')})" if f['ko_by_priority'] else "")
                     + f" {f['sym']}" + fid(f["id"]))
    L.append("")

    L.append("## 7. 相手ごとの採用率・順位（抜粋：多数派しきい値以上）")
    opp_names = sorted({f["pokemon"] for f in by_kind.get("adopt_rate", []) if f["pokemon"] != subj and f["pokemon"] in keep_opps})
    for pk in opp_names:
        rk = next((f for f in by_kind.get("usage_rank", []) if f["pokemon"] == pk and not f.get("season")), None)
        L.append(f"### {pk}" + (f"（使用率{rk['value']}位）" if rk else ""))
        for cat, jp in (("move", "技"), ("item", "持ち物"), ("nature", "性格"), ("ability", "特性")):
            vals = sorted(((f["name"], f["value"]) for f in by_kind.get("adopt_rate", []) if f["pokemon"] == pk and f["category"] == cat), key=lambda kv: -kv[1])
            vals = [(n, v) for n, v in vals if v >= 10]
            if vals:
                L.append(f"- {jp}: " + "、".join(f"{n}{v}%" for n, v in vals) + fid(f"adopt/{cat}/{pk}/<名前>/{spec['season']}"))
    L.append("")

    L.append("## 8. 技データ")
    for f in by_kind.get("move_power", []):
        pr = next((x for x in by_kind.get("move_priority", []) if x["move"] == f["move"]), None)
        sc = [x for x in by_kind.get("stage_change", []) if x["move"] == f["move"]]
        dur = next((x for x in by_kind.get("move_duration", []) if x["move"] == f["move"]), None)
        L.append(f"- {f['move']}: {f['type']} {f['category']} 威力{f['value'] if f['value'] is not None else '（変化技）'} 優先度{pr['value'] if pr else '?'}"
                 + ("".join(f" {('自分' if x['target']=='self' else '相手')}の{x['stat']}{x['value']}段階{'上昇' if x['direction']=='up' else '低下'}" for x in sc))
                 + (f" 継続{dur['turns_min']}〜{dur['turns_max']}ターン（{dur['note']}）" + fid(f"move_duration/{f['move']}") if dur else "")
                 + fid(f"move_power/{f['move']}"))
        ef = next((x for x in by_kind.get("move_effect", []) if x["move"] == f["move"]), None)
        if ef and ef.get("value"):
            L.append(f"  - 効果: {ef['value']}")
    L.append("")

    L.append("## 8b. 持ち物の効果（DB item_master）")
    for f in by_kind.get("item_effect", []):
        L.append(f"- {f['item']}: {f['value']}" + fid(f["id"]))
    L.append("")
    # 特性の効果文が事実シートに無く、書き手が記憶で効果を書いて誤った（2026-10-27 ドドゲザンのそうだいしょう・まけんき）
    L.append("## 8c. 特性の効果（DB ability_master。被写体の特性とメガ後の特性）")
    for f in by_kind.get("ability_effect", []):
        L.append(f"- {f['ability']}: {f['value']}" + fid(f["id"]))
    L.append("")

    L.append("## 9. タイプ相性（技タイプ→防御側）")
    eff = {}
    for f in by_kind.get("type_eff", []):
        eff.setdefault(f["defender"], []).append((f["atk_type"], f["value"]))
    for d, parts in eff.items():
        L.append(f"- {d}: " + "、".join(f"{a}×{v:g}" for a, v in parts if v != 1.0) + fid(f"type_eff/<タイプ>/{d}"))
    L.append("")

    L.append("## 10. 定数")
    L.append("- 能力ランク: " + "、".join(f"{n}段階=×{m:g}" for n, m in STAGE_MULT.items()) + " `const/stage_mult/N`")
    L.append("- 持ち物: " + "、".join(f"{i}=×{m:g}" for i, m in ITEM_MULT.items()) + " `const/item_mult/<持ち物>`")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main -----

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--spec", default=None)
    ap.add_argument("--out-dir", default=str(ROOT / "_local" / "article_facts"))
    ap.add_argument("--skip-engine", action="store_true", help="既存の <slug>.engine.json を再利用する")
    args = ap.parse_args()

    spec = load_spec(args.slug, args.spec)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    pool_version = spec.get("pool_version") or pool_versions.pointer("page")
    pool = MF.load_pool(pool_version)
    mon = json.loads((BUILDER / "mon" / f"{spec['icon']}.json").read_text(encoding="utf-8"))
    validate_spec(conn, spec, mon)
    # spec の構造検証（型名の少数派技・技構成の重複・pool_group の有無）。die なら執筆に入る前に止める（2026-10-18）
    import article_spec_check as ASC
    spec_problems = ASC.check_spec(spec, pool, conn)
    for p in spec_problems:
        print(f"[article_spec_check][{p.level}] {p.code}: {p.msg}", file=sys.stderr)
    if any(p.level == "die" for p in spec_problems):
        die("spec の構造に問題がある（上記 die を直してから再実行）")

    detail_date = resolve_dates(conn, spec["subject"], spec["season"], spec.get("detail_date"))
    prev_date = resolve_dates(conn, spec["subject"], spec["prev_season"]) if spec.get("prev_season") else None

    builds = subject_target_builds(conn, spec, pool)
    builds_path = out_dir / f"{spec['slug']}.subject_builds.json"
    builds_path.write_text(json.dumps(builds, ensure_ascii=False, indent=1), encoding="utf-8")

    engine_path = out_dir / f"{spec['slug']}.engine.json"
    reused = args.skip_engine and engine_path.exists()
    if reused:
        engine = json.loads(engine_path.read_text(encoding="utf-8"))
    else:
        engine = run_engine(spec, builds_path, engine_path)

    F, cards, names, matrices = build_all(spec, conn, pool, engine, detail_date, prev_date, out_dir, pool_version)
    consistency_asserts(spec, cards, engine, conn, detail_date, check_builder=not reused)
    rank_of = {f["pokemon"]: f["value"] for f in F.items if f["kind"] == "usage_rank" and not f.get("season")}
    after = ASC.check_after_engine(spec, engine, lambda sp: rank_of.get(sp))
    for p in after:
        print(f"[article_spec_check][{p.level}] {p.code}: {p.msg}", file=sys.stderr)
    spec_problems += after

    wasm = ROOT / "scripts" / "rust_engine" / "target" / "wasm32-unknown-unknown" / "release-wasm" / "engine_wasm.wasm"
    wasm_sha = hashlib.sha1(wasm.read_bytes()).hexdigest() if wasm.exists() else None
    forms = sorted({f["pokemon"] for f in F.items if f["kind"] == "base_stat" and (f["pokemon"] == spec["subject"] or f["pokemon"] in {c["label"] for c in cards})})
    out = {
        "schema": 1,
        "slug": spec["slug"],
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "subject": {"name": spec["subject"], "icon": spec["icon"], "season": spec["season"], "forms": forms},
        "sources": {"db": str(DB_PATH.relative_to(ROOT)), "detail_date": detail_date, "prev_season": spec.get("prev_season"),
                    "prev_detail_date": prev_date, "pool_version": pool_version, "builder_version": engine.get("builderVersion"),
                    "engine_wasm_sha1": wasm_sha, "majority_pct": spec["majority_pct"]},
        "names": names,
        "cards": cards,
        "facts": F.items,
    }
    json_path = out_dir / f"{spec['slug']}.json"
    json_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    write_sheet(out_dir / f"{spec['slug']}.md", spec, out, cards, matrices,
                warnings=[f"{p.code}: {p.msg}" for p in spec_problems if p.level == "warn"])
    conn.close()
    kinds = {}
    for f in F.items:
        kinds[f["kind"]] = kinds.get(f["kind"], 0) + 1
    print(f"[article_facts] {json_path} に {len(F.items)} 件の事実を書き出した（detail_date={detail_date}）")
    print("  " + ", ".join(f"{k}:{v}" for k, v in sorted(kinds.items())))


if __name__ == "__main__":
    main()
