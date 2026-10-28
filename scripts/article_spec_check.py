#!/usr/bin/env python3
"""spec（型カード定義）を執筆前に検証する（2026-10-18）。

ミミッキュM-7記事で、型名に少数派の技を使っていた（「ウッドハンマー型」：型内27%）こと、
2つの型の技構成が同一でEVだけ違っていたことが、執筆後8〜12回目のレビューで発覚し、
事実ファイルの作り直しと多段落の書き直しになった。どちらも spec と型プールだけで機械的に分かる。

使い方（article_facts.py が自動で呼ぶ。単体でも使える）:
  python3 scripts/article_spec_check.py <slug>
die が1件でもあれば article_facts.py は中断する。warn は事実シートの先頭に出す。
"""
import argparse
import json
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import matchup_facts as MF  # noqa: E402
import pool_versions  # noqa: E402

CARD_GROUP_MIN_PCT = 5.0    # 型プールでこの重み未満の型はカードにしない
ARCH_TOKEN_MIN_PCT = 50.0   # 型名に含まれる技/持ち物は型内でこの割合以上
CARD_MOVE_WARN_PCT = 20.0   # カードの表示技が型内でこの割合未満なら die
CARD_ITEM_RATIO = 0.98      # カードの持ち物は型内最多（2%以内の僅差は許す）。2026-10-27 バシャーモ：いのちのたま49.2%の型をタスキ48.2%で代表
CARD_NATURE_RATIO = 0.5     # 性格は型内最多の半分未満で die（速攻/耐久を性格で分ける型があるため最多までは求めない）
MIXED_TOP_RANK = 20         # extra_pokemon に入れるべき mixed 相手の使用率順位


@dataclass
class Problem:
    level: str    # "die" | "warn"
    code: str
    msg: str


def arch_name_tokens(arch, names):
    """型名に含まれる技名・持ち物名（長い名前優先。短い名前が長い名前に含まれる場合は捨てる）。"""
    found = []
    covered = []
    for nm in sorted(names, key=len, reverse=True):
        idx = arch.find(nm)
        while idx != -1:
            if not any(not (idx + len(nm) <= a or idx >= b) for a, b in covered):
                covered.append((idx, idx + len(nm)))
                found.append(nm)
            idx = arch.find(nm, idx + 1)
    return found


def check_spec(spec, pool, conn):
    out = []
    cards = spec["cards"]
    entry = pool.get(spec["subject"])
    if entry is None:
        out.append(Problem("die", "pool_missing", f"型プールに {spec['subject']} が無い"))
        return out
    group_names = {g["name"] for g in entry["groups"]}
    # (i) カードの重複
    sigs = {}
    for c in cards:
        sig = (frozenset(c["moves"]), c["item"], c["nature"], tuple(c["ev"]))
        if sig in sigs:
            out.append(Problem("die", "card_duplicate", f"{c['arch']} と {sigs[sig]} は技・持ち物・性格・EVが完全に同じ"))
        sigs[sig] = c["arch"]
    for i, a in enumerate(cards):
        for b in cards[i + 1:]:
            if frozenset(a["moves"]) == frozenset(b["moves"]) and a["item"] == b["item"] and (a["ev"] != b["ev"] or a["nature"] != b["nature"]):
                out.append(Problem("warn", "card_same_moves",
                                   f"{a['arch']} と {b['arch']} は技構成が同じでEV/性格だけ違う。型名にその差（速攻/耐久等）が現れているか確認し、本文で「技構成で分かれる」と書かない"))
    # (ii) 型名トークンの型内シェア
    move_names = {m for c in cards for m in c["moves"] + c.get("mpool", [])}
    for g in entry["groups"]:
        move_names |= {m for b in g["builds"] for m in b["moves"]}
    item_names = set()
    for g in entry["groups"]:
        item_names |= {b["item"] for b in g["builds"] if b.get("item")}
    mega_names = {}
    for mega, stone in conn.execute("SELECT mega_name_jp, mega_stone FROM pokemon_mega_stats WHERE base_pokemon_jp=?", (spec["subject"],)):
        mega_names[mega] = stone
    for c in cards:
        pg = c.get("pool_group")
        if not pg:
            out.append(Problem("warn", "no_pool_group", f"{c['arch']}: pool_group が無い（型シェア・型内シェアが出ない）"))
            continue
        if pg not in group_names:
            out.append(Problem("die", "pool_group_missing", f"{c['arch']}: pool_group「{pg}」が型プールに無い。候補: {sorted(group_names)}"))
            continue
        # 型そのものが少数派（型プールの重み CARD_GROUP_MIN_PCT 未満）なら型カードにしない（2026-10-27 ブラッキーのめいそう型2.3%）
        gshare = next((g.get("share", 0) * 100 for g in entry["groups"] if g["name"] == pg), None)
        if gshare is not None and gshare < CARD_GROUP_MIN_PCT:
            out.append(Problem("die", "card_group_minority", f"{c['arch']}: 型（{pg}）が型プール全体の{gshare:.1f}%しかない（{CARD_GROUP_MIN_PCT:g}%未満は型カードにしない）"))
        mv_sh = MF.move_shares(entry, pg)
        it_sh = MF.item_shares(entry, pg)
        tokens = arch_name_tokens(c["arch"], move_names | item_names | set(mega_names))
        for t in tokens:
            if t in mega_names:
                pct = it_sh.get(mega_names[t], 0.0)
                kind = "メガ石"
            elif t in it_sh or t in item_names:
                pct = it_sh.get(t, 0.0)
                kind = "持ち物"
            else:
                pct = mv_sh.get(t, 0.0)
                kind = "技"
            if pct < ARCH_TOKEN_MIN_PCT:
                other = {m for d in cards if d is not c and d.get("pool_group") for m, p in MF.move_shares(entry, d["pool_group"]).items() if p >= ARCH_TOKEN_MIN_PCT}
                cand = [m for m, p in mv_sh.items() if p >= ARCH_TOKEN_MIN_PCT and m not in other][:3]
                out.append(Problem("die", "arch_name_minority",
                                   f"{c['arch']}: 型名の{kind}「{t}」は型内{pct}%で少数派（{ARCH_TOKEN_MIN_PCT:g}%未満）。この型だけが多数派で持つ技の候補: {cand or '無し（EV/性格/持ち物で命名する）'}"))
        # 代表個体が型の少数派だと、カード・arch_grid・苦手/得意表の判定がその型の実態とずれる（2026-10-27 ウルガモスのおにび型：
        # サイコキネシス9.8%・ゴツゴツメット14.6%・おくびょう36.7%を代表にしていた）。warn では直されなかったので die
        for m in c["moves"]:
            if mv_sh.get(m, 0.0) < CARD_MOVE_WARN_PCT:
                cand = [x for x, p in mv_sh.items() if p >= CARD_MOVE_WARN_PCT and x not in c["moves"]][:3]
                out.append(Problem("die", "card_move_minority", f"{c['arch']}: 表示技「{m}」は型内{mv_sh.get(m, 0.0)}%（{CARD_MOVE_WARN_PCT:g}%未満）。候補: {cand}"))
        if it_sh and c.get("item") and it_sh.get(c["item"], 0.0) < max(it_sh.values()) * CARD_ITEM_RATIO:
            top = next(iter(it_sh.items()))
            out.append(Problem("die", "card_item_minority", f"{c['arch']}: 持ち物「{c['item']}」は型内{it_sh.get(c['item'], 0.0)}%（最多は{top[0]} {top[1]}%）"))
        ns = dict(MF.nature_shares(entry, pg).get(pg, []))
        if ns and c.get("nature") and ns.get(c["nature"], 0.0) < max(ns.values()) * CARD_NATURE_RATIO:
            top = max(ns.items(), key=lambda kv: kv[1])
            out.append(Problem("die", "card_nature_minority", f"{c['arch']}: 性格「{c['nature']}」は型内{ns.get(c['nature'], 0.0)}%（最多は{top[0]} {top[1]}%）"))
    return out


def check_after_engine(spec, engine, usage_rank_of):
    """エンジン実行後：mixed かつ使用率上位で extra_pokemon に無い相手を提案する（自動追記はしない）。"""
    out = []
    missing = []
    for g in engine.get("excluded", []):
        rk = usage_rank_of(g["sp"])
        if rk is not None and rk <= MIXED_TOP_RANK and g["sp"] not in spec.get("extra_pokemon", []):
            missing.append(g["sp"])
    if missing:
        out.append(Problem("warn", "extra_pokemon_suggest",
                           "型によって勝敗が割れる使用率上位の相手が extra_pokemon に無い（事実シートには出る。本文で名指しして採用率等を書くなら追加）: "
                           + json.dumps(sorted(set(missing)), ensure_ascii=False)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    args = ap.parse_args()
    spec = json.loads((HERE / "article_specs" / f"{args.slug}.json").read_text(encoding="utf-8"))
    pool = MF.load_pool(spec.get("pool_version") or pool_versions.pointer("page"))
    conn = sqlite3.connect(HERE / "pokenavi.db")
    probs = check_spec(spec, pool, conn)
    for p in probs:
        print(f"[{p.level}] {p.code}: {p.msg}")
    if not probs:
        print("[article_spec_check] 問題なし")
    sys.exit(2 if any(p.level == "die" for p in probs) else 0)


if __name__ == "__main__":
    main()
