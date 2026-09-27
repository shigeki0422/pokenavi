"""型プールの版のチェックと差分レポート（週次の型生成 update_type_pool.py から自動で呼ぶ。単体でも使える）。

エラー（終了コード1）: 生成ルールの違反・型命名/系統分けの規則の違反・出力（想定型と1v1）の不整合
警告（一覧にしてレポートに入れる）: 前の版との統計の変化・DB の使用率との差・ランキングの網羅・監査（_audit_type_pool）の違反率
規則は生成側（_gen_type_pool・arch_groups・gen_builder_data）の関数と定数を import して使い、ここに二重に書かない。

使い方: python3 scripts/pool_checks.py <前の版> <新しい版> [出力.md]      例: M-6/v41 M-6/2026-09-27
        STAGE=pool（生成物を作る前: プール・系統表だけ）/ all（既定: 想定型・builder-data も）  DIST=<astro の出力>（en/ko の型名漏れを見る）
"""
import collections
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pool_versions as PV  # noqa: E402

# ---- 閾値 ----
SHIFT_PT = 5.0          # 差分レポートに載せる系統の割合の変化
SHARE_WARN_PT = 10.0    # 警告: 系統の割合の前の版からの変化
MARG_SHIFT_PT = 10.0    # 警告: プール上の採用率（技・持ち物・性格・努力値・特性）の前の版からの最大差
DB_QUIET_PT = 3.0       # DB の使用率の変化がこれ未満なのにプールが MARG_SHIFT_PT 以上動いた → 生成側が原因の疑い
KL_WARN = 0.10          # 警告: 技の組（型の技4つ）の分布の前の版からの KL（nats）
MARG_TOL = {"moves": 10.0, "items": 5.0, "natures": 5.0, "evs": 10.0, "abilities": 15.0}   # 警告: DB の使用率との差(pt)
CHOICE_STATUS2_MAX = 0.05   # 警告: こだわりの型のうち変化技（トリック/すりかえ以外）2本以上の割合（上位構築は1.2%）
AUDIT_WARN = 0.005      # 警告: _audit_type_pool の違反率（[参考] を除く）
WEIGHT_TOL = 1e-3
PRUNE_W_FLOOR = 0.999   # エラー: 重みが PRUNE_W 未満の型（丸めの分だけ許す）
CATS = ("moves", "items", "natures", "evs", "abilities")
CAT_JA = {"moves": "技", "items": "持ち物", "natures": "性格", "evs": "努力値", "abilities": "特性"}


def arch_name(n):
    return n if n.endswith("型") else n + "型"


def ordered(v):
    return [(arch_name(g["name"]), g["share"] * 100) for g in sorted(v["groups"], key=lambda g: -g["share"])]


def load(version):
    pool_p, grp_p, meta_p = (PV.path(n, version) for n in ("type_pool", "type_groups", "meta"))
    pool = {r["species"]: r for r in json.load(open(pool_p))} if os.path.exists(pool_p) else {}
    return pool, json.load(open(grp_p)), (json.load(open(meta_p)) if os.path.exists(meta_p) else {})


# ════════ 生成ルール（エラー） ════════
def natures(G):
    from simulator.data import NATURE_MODS
    return set(NATURE_MODS) | {r[0] for r in G.con.execute("select distinct nature from pokemon_natures")}


def rule_errors(G, sp, builds, used=None, nats=None):
    """1種の型プールの生成ルール違反。used: その種が使用率に出た技（覚える技の表の漏れを補う。_audit_type_pool と同じ扱い）。
    PRUNE_W 未満の型は生成器が最後に落とす（v41 の固定版には残っている）"""
    err = []
    z = sum(b["weight"] for b in builds)
    if abs(z - 1.0) > WEIGHT_TOL:
        err.append(f"重みの合計 {z:.4f}")
    low = [b for b in builds if b["weight"] / (z or 1) < G.PRUNE_W * PRUNE_W_FLOOR]
    if low:
        err.append(f"PRUNE_W 未満の型 {len(low)}件（最小 {min(b['weight'] / z for b in low):.2e}）")
    ls = G.learnset(sp)
    stones = {it for (s2, it) in G.MEGA if s2 == sp}
    for b in builds:
        mv, it, ev = b["moves"], b["item"], b["ev"]
        tag = f"{it}:{b['nature']}:{'|'.join(mv)}:{'/'.join(map(str, ev))}"
        if len(ev) != 6 or any(not isinstance(x, int) or x < 0 or x > 32 for x in ev) or sum(ev) > 66:
            err.append(f"EV（H/A/B/C/D/S・各≤32・合計≤66） {tag}")
        if nats is not None and b["nature"] not in nats:
            err.append(f"性格が不明 {tag}")
        if len(mv) > 4 or len(set(mv)) != len(mv):
            err.append(f"技の数・重複 {tag}")
        bad = [m for m in mv if m not in G.MV]
        if bad:
            err.append(f"技マスタに無い技 {bad} {tag}")
        if ls:
            nl = [m for m in mv if m not in ls and m not in (used or ())]
            if nl:
                err.append(f"覚えない技（没収技を含む） {nl} {tag}")
        if not G.item_ok(mv, it):
            why = ("ジュエルに同タイプの攻撃技が無い" if it.endswith("ジュエル") else
                   "こだわり×積み/守る/回復" if it in G.CHOICE else "持ち物と技の規則(item_ok)")
            err.append(f"{why} {tag}")
        if it in G._STONES and it not in stones:
            err.append(f"他の種のメガ石 {tag}")
    return err


def choice_status2(G, builds):
    ch = [b for b in builds if b["item"] in G.CHOICE]
    tot = sum(b["weight"] for b in ch)
    bad = sum(b["weight"] for b in ch
              if sum(1 for m in b["moves"] if G.MV.get(m, {}).get("cat") == "status" and m not in G.TRICK) >= 2)
    return bad / tot if tot else 0.0


# ════════ 型命名・系統分け（エラー） ════════
def naming_errors(G, A, sp, groups):
    """1種の系統表（系統の name・kind・share・builds）の規則違反"""
    err = []
    stones = {it for (s2, it) in G.MEGA if s2 == sp}

    def cls(b):
        if A.GIMMICK & set(b["moves"]):
            return None
        return b["item"] if b["item"] in stones else A.CHOICE_SHORT.get(b["item"])

    names = [g["name"] for g in groups]
    dup = sorted(n for n, c in collections.Counter(names).items() if c > 1)
    if dup:
        err.append(f"同名の系統 {dup}")
    if len(groups) > A.MAX_GROUPS:
        err.append(f"系統が{len(groups)}個（≤{A.MAX_GROUPS}）")
    gcls = []
    for g in groups:
        gb = g["builds"]
        n = g["name"]
        z = sum(b["weight"] for b in gb) or 1.0
        mv = collections.Counter()
        for b in gb:
            for m in b["moves"]:
                mv[m] += b["weight"] / z
        cs = collections.Counter()
        for b in gb:
            cs[cls(b)] += b["weight"]
        c0 = cs.most_common(1)[0][0]
        gcls.append(c0)
        if len(cs) > 1:
            err.append(f"{n}: 持ち物の区分（メガ石・こだわり系・その他）をまたいでいる {dict(cs)}")
        head = ("メガ" if len(stones) < 2 else c0) if c0 in stones else c0
        body = n[len(head) + 1:] if head and n.startswith(head + "・") else ("" if head and n == head else n)
        toks = [t for t in re.split(r"[＋／]", body) if t]
        for t in toks:
            if t in G.MV:
                th = 0.2 if t in G.BOOST else 0.5 if t in A.GIMMICK else A.CORE
                if mv.get(t, 0.0) < th - 1e-9:
                    err.append(f"{n}: 名前の技 {t} が系統内 {mv.get(t, 0.0) * 100:.0f}%（≥{th * 100:.0f}%）")
        for m, p in mv.items():
            if m in G.BOOST and p >= 0.5 and m not in toks and not ("フルアタ" in toks and G.MV.get(m, {}).get("cat") != "status"):
                err.append(f"{n}: 積み技 {m}（系統内 {p * 100:.0f}%）が名前に無い")
        if A.full_attack(gb) and "フルアタ" not in toks and body != "フルアタ":
            err.append(f"{n}: 攻撃技4本が{A.CORE * 100:.0f}%以上なのにフルアタ型でない")
        if "フルアタ" in toks and not A.full_attack(gb, 0.5):
            err.append(f"{n}: フルアタ型なのに攻撃技4本が半分未満")
        baton = sum(b["weight"] for b in gb if A.GIMMICK & set(b["moves"])) / z
        if any(t in A.GIMMICK for t in toks) and baton < 0.5:
            err.append(f"{n}: バトンの系統なのにバトンの型が {baton * 100:.0f}%")
        if not any(t in A.GIMMICK for t in toks) and baton >= 0.5:
            err.append(f"{n}: バトンの型が {baton * 100:.0f}% なのに名前にバトンタッチが無い（バトンは単独の系統）")
        for suf, kc in (("物理技", "physical"), ("特殊技", "special")):
            atk = [t for t in toks if t in G.MV and G.MV[t]["cat"] != "status" and t not in G.BOOST]
            want = g["kind"] == suf[:2] and atk and not any(G.MV[t]["cat"] == kc for t in atk)
            if (suf in toks) != bool(want):
                err.append(f"{n}: 「＋{suf}」の付け方（向き {g['kind']}・名前の攻撃技 {atk}）")
        if body == "単一の型" and len(groups) != 1:
            err.append(f"{n}: 「単一の型」は系統が1つの種だけ")
    if len(groups) == 1:
        g = groups[0]
        head_less = gcls[0] is None
        toks = [t for t in re.split(r"[＋／・]", g["name"]) if t]
        plain = [t for t in toks if t in G.MV and t not in G.BOOST and t not in A.GIMMICK]
        if head_less and plain:
            err.append(f"{g['name']}: 系統が1つの種の名前に技 {plain}（単一の型・フルアタ・積み技で名付ける）")
    for g, c in zip(groups, gcls):
        if g["share"] < 0.05 and any(o is not g and oc == c and o["share"] >= 0.05 for o, oc in zip(groups, gcls)):
            err.append(f"{g['name']}: 5%未満（{g['share'] * 100:.1f}%）なのに同じ持ち物の区分の系統に統合されていない")
    return err


# ════════ 出力の整合（エラー） ════════
def output_errors(arch, mons, version, bversion):
    """arch: archetypes.json、mons: {アイコンID: mon/*.json}、bversion: builder-data/version.json の pool"""
    err = []
    if arch.get("_version") != version or bversion != version:
        err.append(f"版の記録: 想定型 {arch.get('_version')}・builder-data {bversion}・この版 {version}")
    ent = {k: v for k, v in arch.items() if not k.startswith("_")}
    for k, v in ent.items():
        for g in v["groups"]:
            if not g["name"].endswith("型"):
                err.append(f"{k} 系統名が「〜型」でない: {g['name']}")
        if len(v["groups"]) > 6:
            err.append(f"{k} 系統が{len(v['groups'])}個")
    for k, m in mons.items():
        mu = [b for b in m.get("mu", []) if b.get("archNo")]
        gs = ent.get(k, {}).get("groups", [])
        byno = collections.defaultdict(list)
        for b in mu:
            byno[b["archNo"]].append(b)
        for no, bs in byno.items():
            if no > len(gs):
                err.append(f"{k} {bs[0]['arch']}: archNo {no} が想定型の系統数 {len(gs)} を超える")
                continue
            g = gs[no - 1]
            for b in bs:
                if not b["arch"].startswith(g["name"]):
                    err.append(f"{k} {b['arch']}: archNo {no} の想定型は {g['name']}")
                if not b["arch"].endswith("型") and "（" not in b["arch"]:
                    err.append(f"{k} {b['arch']}: 「〜型」でない")
            subs = [b.get("archSub", "") for b in bs]
            if len(bs) == 1 and subs != [""] or len(bs) > 1 and sorted(subs) != list("abcdefghij"[:len(bs)]):
                err.append(f"{k} archNo {no}: archSub {subs}")
            tot = sum(b["share"] for b in bs)
            if abs(tot - g["share"]) > 0.15 * len(bs):
                err.append(f"{k} archNo {no}: 1v1 の割合 {tot:.1f} ≠ 想定型 {g['share']}")
            if len(bs) > 1:
                parts = [re.findall(r"（(.*)）$", b["arch"])[0].split("・") if "（" in b["arch"] else [] for b in bs]
                short = [[x for x in p if x not in g["name"]] for p in parts]
                if all(short) and len({tuple(p) for p in short}) == len(short) and short != parts:
                    err.append(f"{k} archNo {no}: 分割ラベルの括弧内で系統名の語を繰り返している {[b['arch'] for b in bs]}")
    return err


def leak_errors(dist, arch, keys_by_name):
    """en/ko のページの表示テキストに日本語の型名が出ていないか（<template>・<script> の中は見ない）"""
    err = []
    names = {k: {g["name"] for g in v["groups"]} for k, v in arch.items() if not k.startswith("_")}
    for lang in ("en", "ko"):
        for f in glob.glob(os.path.join(dist, lang, "pokemon", "*", "index.html")):
            html = re.sub(r"<(template|script|style)\b.*?</\1>", "", open(f).read(), flags=re.S)
            m = re.search(r"pokemon-(\d{4}-\d{2})\.webp", html)
            if not m or m.group(1) not in names:
                continue
            hit = [n for n in names[m.group(1)] if n in html]
            if hit:
                err.append(f"{lang} {os.path.relpath(f, dist)}: 型名 {hit[:3]}")
    return err


# ════════ 警告 ════════
def pool_marg(G, builds):
    out = {c: collections.Counter() for c in CATS}
    z = sum(b["weight"] for b in builds) or 1.0
    for b in builds:
        w = b["weight"] / z
        for m in b["moves"]:
            out["moves"][m] += w
        out["items"][b["item"]] += w
        out["natures"][b["nature"]] += w
        out["evs"][G._ev_key(tuple(b["ev"]))] += w
        out["abilities"][b.get("ability") or ""] += w
    return out


def db_marg(G, sp, season, date):
    """DB の使用率（生成器の marginals と同じ読み方。date はシーズンの詳細の日）"""
    s0, d0 = G.SEASON, G._DATE.get("d")
    G.SEASON, G._DATE["d"] = season, date
    try:
        mg = G.marginals(sp) or {}
    finally:
        G.SEASON = s0
        if d0 is None:
            G._DATE.pop("d", None)
        else:
            G._DATE["d"] = d0
    return {c: mg.get(c, {}) for c in CATS}


def maxdiff(a, b):
    return max((abs(a.get(k, 0.0) - b.get(k, 0.0)) * 100, k) for k in set(a) | set(b)) if (a or b) else (0.0, "")


def kl(p, q, eps=1e-4):
    import math
    ks = set(p) | set(q)
    return sum(p.get(k, 0.0) * math.log((p.get(k, 0.0) + eps) / (q.get(k, 0.0) + eps)) for k in ks if p.get(k, 0.0) > 0)


def combo(builds):
    z = sum(b["weight"] for b in builds) or 1.0
    c = collections.Counter()
    for b in builds:
        c[frozenset(b["moves"])] += b["weight"] / z
    return c


def stat_warnings(G, prev, new):
    """前の版との統計の変化。DB の使用率の変化と並べて、プールだけが動いたもの（生成側の疑い）を分ける"""
    (pp, pg, pm), (np_, ng, nm) = prev, new
    W = []
    for sp in ng:
        if sp not in pg:
            continue
        a, b = dict(ordered(pg[sp])), dict(ordered(ng[sp]))
        if len(a) != len(b):
            W.append(("系統数", sp, f"{len(a)}→{len(b)}"))
        for n in b:
            if n in a and abs(b[n] - a[n]) >= SHARE_WARN_PT:
                W.append(("系統の割合", sp, f"{n} {a[n]:.1f}→{b[n]:.1f}"))
        for n in set(a) ^ set(b):
            W.append(("系統の消滅" if n in a else "系統の新規", sp, f"{n} {(a.get(n) or b.get(n)):.1f}%"))
    sd_p, sd_n = pm.get("detail_date"), nm.get("detail_date")
    for sp in np_:
        if sp not in pp:
            continue
        ma, mb = pool_marg(G, pp[sp]["builds"]), pool_marg(G, np_[sp]["builds"])
        da = db = None
        if sd_p and sd_n:
            da = db_marg(G, sp, pp[sp].get("season") or PV.season_of(pm.get("version", "M-6/x")), sd_p)
            db = db_marg(G, sp, np_[sp].get("season") or PV.season_of(nm["version"]), sd_n)
        for c in CATS:
            d, k = maxdiff(ma[c], mb[c])
            if d < MARG_SHIFT_PT:
                continue
            dd = maxdiff(da[c], db[c])[0] if da is not None else None
            why = "（DB の変化 " + (f"{dd:.1f}pt" if dd is not None else "不明") + ("・生成側の疑い）" if dd is not None and dd < DB_QUIET_PT else "）")
            W.append((f"プールの{CAT_JA[c]}の変化", sp, f"{k} {ma[c].get(k, 0) * 100:.1f}→{mb[c].get(k, 0) * 100:.1f}% {why}"))
        ta, tb = ma["items"].most_common(1), mb["items"].most_common(1)
        if ta and tb and ta[0][0] != tb[0][0]:
            W.append(("上位の持ち物の入れ替わり", sp, f"{ta[0][0]}→{tb[0][0]}"))
        k2 = kl(combo(np_[sp]["builds"]), combo(pp[sp]["builds"]))
        if k2 >= KL_WARN:
            W.append(("技の組の分布（KL）", sp, f"{k2:.3f}"))
    return W


def marg_warnings(G, pool, meta):
    """プールの採用率と DB の使用率（生成器の目標）の差"""
    W = []
    for sp, r in pool.items():
        raw = {}
        season = r.get("season") or meta.get("season") or G.SEASON
        s0 = G.SEASON
        G.SEASON = season
        try:
            mg = G.marginals(sp) or {}
            dbm = {c: v for c, v in mg.items() if c in CATS}
            if mg.get("moves") and mg.get("natures"):
                # 技の目標は生成器と同じく上位10の率を4枠（400%）へ伸ばしたもの（generate の past_fill・ITEM_NEEDS）
                P = {m: p for m, p in mg["moves"].items() if m != G.TAIL}
                sides = G.side_weights(mg["natures"])
                cap = {m: max(p, sum(sides[k] for k in sides if G.gate(m, k))) for m, p in P.items()}
                Q, _ = G.past_fill(sp, P, cap, sides, mg["items"])
                for it, m in G.ITEM_NEEDS.items():
                    if mg["items"].get(it, 0) > 0 and m not in Q and m in G.MV and Q:
                        Q[m] = min(mg["items"][it], min(Q.values()))
                dbm["moves"] = {m: q for m, q in Q.items() if m in P}
                raw = P
        finally:
            G.SEASON = s0
        pm = pool_marg(G, r["builds"])
        for c in CATS:
            ref = dbm.get(c) or {}
            if not ref:
                continue
            keys = [k for k in ref if k != G.TAIL] if c == "moves" else set(ref) | set(pm[c])
            d = max(((abs(pm[c].get(k, 0.0) - ref.get(k, 0.0)) * 100, k) for k in keys), default=(0.0, ""))
            if d[0] > MARG_TOL[c]:
                extra = f"（DB {raw.get(d[1], 0) * 100:.1f}% を4枠へ伸ばした目標）" if c == "moves" else ""
                W.append((f"DB との差（{CAT_JA[c]}）", sp, f"{d[1]} プール {pm[c].get(d[1], 0) * 100:.1f}% / DB {ref.get(d[1], 0) * 100:.1f}%{extra}（許容 {MARG_TOL[c]:.0f}pt）"))
    return W


def audit_warnings(pool):
    import _audit_type_pool as AU
    tally, ex = collections.Counter(), {}
    for sp, r in pool.items():
        z = sum(b["weight"] for b in r["builds"]) or 1.0
        for b in r["builds"]:
            for v in AU.check(sp, b):
                if v.startswith("[参考]"):
                    continue
                key = v.split(" ")[0] if v.startswith("非習得技") else v
                tally[key] += b["weight"] / z / len(pool)
                ex.setdefault(key, f"{sp} {b['item']} {'|'.join(b['moves'])}")
    return [("監査の違反率", k, f"{v * 100:.2f}%（例 {ex[k]}）") for k, v in tally.most_common() if v >= AUDIT_WARN]


# ════════ 差分レポート ════════
def diff_lines(prev, new, pg, ng, nm):
    L = [f"# 型プールの差分とチェック {prev} → {new}", ""]
    if nm:
        L += [f"- 使用率の順位の日 {nm.get('usage_rank_date')}・詳細（技・持ち物…）の日 {nm.get('detail_date')}・{nm.get('species')}種・"
              f"生成器 {nm.get('git', {}).get('commit', '')[:9]}{'（未コミットの変更あり）' if nm.get('git', {}).get('dirty') else ''}",
              f"- 所要時間（秒） {nm.get('seconds')}"]
        if nm.get("older_detail_date"):
            L.append("- 詳細の日に圏外だった種（その種の最新の詳細の日で作成）: " + "、".join(f"{k}({v})" for k, v in nm["older_detail_date"].items()))
        if nm.get("fallback_season"):
            L.append("- 今シーズンの詳細が無く前のシーズンで作成: " + "、".join(f"{k}({v})" for k, v in nm["fallback_season"].items()))
        if nm.get("simple_product"):
            L.append(f"- 技が4つ未満で周辺分布の積で作成: {'、'.join(nm['simple_product'])}")
        if nm.get("not_generated"):
            L.append(f"- 作れなかった種: {'、'.join(nm['not_generated'])}")
    added, removed = sorted(set(ng) - set(pg)), sorted(set(pg) - set(ng))
    both = [sp for sp in ng if sp in pg]
    same = [sp for sp in both if [n for n, _ in ordered(pg[sp])] == [n for n, _ in ordered(ng[sp])]]
    close = [sp for sp in same if all(abs(x - y) < 1.0 for (_, x), (_, y) in zip(ordered(pg[sp]), ordered(ng[sp])))]
    L += ["", "## 差分のまとめ", "",
          f"- 種: 前 {len(pg)} → 新 {len(ng)}（増えた {len(added)}・消えた {len(removed)}）",
          f"- 両方にある {len(both)}種のうち、系統名と並び（系統番号）が同じ {len(same)}種、さらに全系統の割合の差が1pt未満 {len(close)}種"]
    if added:
        L += ["", f"## 増えた種（{len(added)}）", "", "| 種 | 系統（割合%） |", "|---|---|"]
        L += [f"| {sp} | {' / '.join(f'{n} {s:.1f}' for n, s in ordered(ng[sp]))} |" for sp in added]
    if removed:
        L += ["", f"## 消えた種（{len(removed)}）", "", "、".join(removed)]
    chg, mv, sw = [], [], []
    for sp in both:
        pa, pb = dict(ordered(pg[sp])), dict(ordered(ng[sp]))
        gone, new_ = [n for n in pa if n not in pb], [n for n in pb if n not in pa]
        if gone or new_:
            chg.append(f"| {sp} | {' / '.join(f'{n} {pa[n]:.1f}' for n in gone)} | {' / '.join(f'{n} {pb[n]:.1f}' for n in new_)} |")
        for n in pb:
            if n in pa and abs(pb[n] - pa[n]) >= SHIFT_PT:
                mv.append((abs(pb[n] - pa[n]), f"| {sp} | {n} | {pa[n]:.1f} | {pb[n]:.1f} | {pb[n] - pa[n]:+.1f} |"))
        ia = {n: i + 1 for i, n in enumerate(pa)}
        ib = {n: i + 1 for i, n in enumerate(pb)}
        moved = [f"{n} {ia[n]}→{ib[n]}" for n in ib if n in ia and ia[n] != ib[n]]
        if moved:
            sw.append(f"| {sp} | {' / '.join(moved)} |")
    L += ["", f"## 系統名が変わった種（系統が消えた/増えた。{len(chg)}種）", "",
          "| 種 | 消えた系統（前の割合%） | 増えた系統（新しい割合%） |", "|---|---|---|"] + chg
    L += ["", f"## 割合が{SHIFT_PT:.0f}pt以上動いた系統（{len(mv)}件）", "", "| 種 | 系統 | 前% | 新% | 差 |", "|---|---|---|---|---|"]
    L += [x for _, x in sorted(mv, key=lambda t: -t[0])]
    L += ["", f"## 系統番号（Set N）が入れ替わった種（{len(sw)}種）", "", "| 種 | 系統 前→新 |", "|---|---|"] + sw
    return L


def page_keys():
    """ポケモン情報ページ（src/content/pokemon）の 名前 → アイコンID（想定型のキー）"""
    out = {}
    for f in glob.glob(os.path.join(ROOT, "src", "content", "pokemon", "*.md")):
        head = open(f).read().split("---")[1]
        g = {k: v.strip().strip("'\"") for k, v in re.findall(r"^(\w+):\s*(.*)$", head, re.M)}
        if g.get("pokemonName") and g.get("dexNumber"):
            out[g["pokemonName"]] = f"{int(g['dexNumber']):04d}-{g.get('imageForm') or '00'}"
    for s in json.load(open(os.path.join(ROOT, "public", "builder-data", "species.json"))):
        out.setdefault(s["n"], s["icon"])
    return out


def coverage_warnings(arch):
    rk = json.load(open(os.path.join(ROOT, "src", "data", "ranking.json")))["seasons"]
    last = list(rk)[-1]
    keys = page_keys()
    ent = {k: v for k, v in arch.items() if not k.startswith("_")}
    W = [("ランキングの網羅", p["name"], f"{last} のランキングにあるが想定型が無い")
         for p in rk[last]["pokemon"] if (keys.get(p["name"]) or p.get("id")) not in ent]
    W += [("最新シーズン以外のデータ", k, f"{v['season']}（最新 {last}）") for k, v in ent.items() if v["season"] != last]
    return W


def run(prev, new, stage="all", dist=None):
    import _gen_type_pool as G
    import arch_groups as A
    P, N = load(prev), load(new)
    npool, ngroups, nmeta = N
    E, W = [], []
    used = collections.defaultdict(set)
    for sp, m in G.con.execute("select pokemon, move from pokemon_moves"):
        used[sp].add(m)
    nats = natures(G)
    for sp, r in npool.items():
        E += [("生成ルール", sp, e) for e in rule_errors(G, sp, r["builds"], used[sp], nats)]
        cs = choice_status2(G, r["builds"])
        if cs > CHOICE_STATUS2_MAX:
            W.append(("こだわり×変化技2本以上", sp, f"こだわりの型の {cs * 100:.1f}%（上限 {CHOICE_STATUS2_MAX * 100:.0f}%）"))
    for sp, v in ngroups.items():
        E += [("命名・系統分け", sp, e) for e in naming_errors(G, A, sp, v["groups"])]
    W += stat_warnings(G, P, N)
    W += marg_warnings(G, npool, nmeta)
    W += audit_warnings(npool)
    if stage == "all":
        arch = json.load(open(os.path.join(ROOT, "src", "data", "archetypes.json")))
        bd = os.path.join(ROOT, "public", "builder-data")
        vp = os.path.join(bd, "version.json")
        bver = json.load(open(vp)).get("pool") if os.path.exists(vp) else None
        mons = {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob(os.path.join(bd, "mon", "*.json"))}
        E += [("出力の整合", "", e) for e in output_errors(arch, mons, new, bver)]
        if dist:
            E += [("en/ko の型名漏れ", "", e) for e in leak_errors(dist, arch, page_keys())]
        W += coverage_warnings(arch)
    L = diff_lines(prev, new, P[1], ngroups, nmeta)

    def table(title, rows):
        out = ["", f"## {title}（{len(rows)}件）", ""]
        if rows:
            cnt = collections.Counter(r[0] for r in rows)
            out += ["- 内訳: " + "、".join(f"{k} {v}" for k, v in cnt.most_common()), "", "| 区分 | 種 | 内容 |", "|---|---|---|"]
            out += [f"| {a} | {b} | {c} |" for a, b, c in rows]
        return out
    L[2:2] = [f"- **エラー {len(E)}件・警告 {len(W)}件**（段階 {stage}{'・DIST ' + dist if dist else ''}）"]
    L += table("エラー", E) + table("警告", W)
    L += ["", "## 閾値", "", f"- 系統の割合の変化 ≥{SHARE_WARN_PT:.0f}pt・プールの採用率の変化 ≥{MARG_SHIFT_PT:.0f}pt（DB の変化 <{DB_QUIET_PT:.0f}pt なら生成側の疑い）"
          f"・技の組の KL ≥{KL_WARN}・DB との差 {MARG_TOL}・こだわり×変化技2本以上 >{CHOICE_STATUS2_MAX * 100:.0f}%・監査の違反率 ≥{AUDIT_WARN * 100:.1f}%"]
    return E, W, L


def main():
    prev, new = sys.argv[1], sys.argv[2]
    E, W, L = run(prev, new, os.environ.get("STAGE", "all"), os.environ.get("DIST"))
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 3:
        with open(sys.argv[3], "w") as f:
            f.write(text)
        print(f"→ {sys.argv[3]}")
    print(f"エラー {len(E)}件・警告 {len(W)}件")
    for a, b, c in E[:30]:
        print(f"  ERROR [{a}] {b} {c}")
    cnt = collections.Counter(r[0] for r in W)
    for k, v in cnt.most_common():
        print(f"  WARN  {k}: {v}件")
    sys.exit(1 if E else 0)


if __name__ == "__main__":
    main()
