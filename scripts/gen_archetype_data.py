"""ポケモン情報ページの「想定型」データ（src/data/archetypes.json）を作る。

採用率は「使用率データ」の表で見られるので、ここでは型のかたまり（技4つ・持ち物・性格・努力値・特性がどう一緒に使われるか）を出す。
元は型プールを系統にまとめた系統表（scripts/arch_groups.py の出力）。版は scripts/pool_versions.json の page（1v1 の public/builder-data と同じ版）。
各系統で、まず完全な型の例を重みの大きい順に TOP_SETS 件、次に型の中での技・持ち物・性格・努力値の傾向を出す。
キーはページ側のアイコンID（例: 0681-00）。"_version" に元の版を書く。env: POOL_VERSION GROUPS TOP_SETS
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pool_versions as PV   # noqa: E402
from arch_groups import order_moves   # noqa: E402  表示順（タイプ一致→不一致→変化技）を確認ページと揃える
VERSION = os.environ.get("POOL_VERSION") or PV.pointer("page")
GROUPS = os.environ.get("GROUPS") or PV.path("type_groups", VERSION)
OUT = os.path.join(ROOT, "src", "data", "archetypes.json")
TOP_SETS = int(os.environ.get("TOP_SETS", "3"))
TEND_MIN = 0.05   # 傾向に出す最低の採用率（型の中）


def arch_name(n):
    """型名は「〜型」に統一する（ガブリアスナイトZ・フルアタ型）。すでに「型」で終わる名前（単一の型・物理型）はそのまま"""
    return n if n.endswith("型") else n + "型"


def ev_text(ev):
    return " ".join(f"{k}{v}" for k, v in zip("HABCDS", ev) if v) or "無振り"


def main():
    icon = {s["n"]: s["icon"] for s in json.load(open(os.path.join(ROOT, "public", "builder-data", "species.json")))}
    out, miss = {"_version": VERSION}, []
    import ev_fill
    for sp, v in ev_fill.fill_groups(json.load(open(GROUPS)), PV.season_of(VERSION)).items():
        ic = icon.get(sp)
        if not ic:
            miss.append(sp)
            continue
        share = collections.Counter()
        for g in v["groups"]:
            for b in g["builds"]:
                for m in b["moves"]:
                    share[m] += g["share"] * b["weight"]
        groups = []
        for g in sorted(v["groups"], key=lambda g: -g["share"]):
            # 代表的な型: 完全な型（技4つ・持ち物・性格・努力値）の重みの大きい順に TOP_SETS 件
            agg = collections.defaultdict(lambda: [0.0, collections.Counter()])
            for b in g["builds"]:
                k = (frozenset(b["moves"]), b["item"], b["nature"], tuple(b["ev"]))
                agg[k][0] += b["weight"]
                agg[k][1][b.get("ability", "")] += b["weight"]
            sets = [{"moves": order_moves(sp, it, list(mv), share), "item": it, "nature": na, "ev": ev_text(ev),
                     "ability": abc.most_common(1)[0][0], "p": round(w * 100, 1)}
                    for (mv, it, na, ev), (w, abc) in sorted(agg.items(), key=lambda kv: -kv[1][0])[:TOP_SETS]]
            # 技の並びを型の例どうしで揃える: 1つ目の例の並びを基準に、同じ技は同じ位置、入れ替わった技は抜けた位置へ
            for x in sets[1:]:
                base, rest = sets[0]["moves"], [m for m in x["moves"] if m not in sets[0]["moves"]]
                x["moves"] = [m if m in x["moves"] else (rest.pop(0) if rest else m) for m in base] + rest
            # 傾向: 型の中での技・持ち物・性格・努力値の採用率（いつも同じ並び）
            tend = {k: collections.Counter() for k in ("moves", "items", "natures", "evs")}
            for b in g["builds"]:
                for m in b["moves"]:
                    tend["moves"][m] += b["weight"]
                tend["items"][b["item"]] += b["weight"]
                tend["natures"][b["nature"]] += b["weight"]
                tend["evs"][ev_text(b["ev"])] += b["weight"]
            mv_order = order_moves(sp, sets[0]["item"], [m for m, w in tend["moves"].items() if w >= TEND_MIN], share)
            trend = {"moves": [[m, round(tend["moves"][m] * 100)] for m in sorted(mv_order, key=lambda m: -tend["moves"][m])]}
            for k in ("items", "natures", "evs"):
                trend[k] = [[x, round(w * 100)] for x, w in tend[k].most_common(3) if w >= TEND_MIN]
            groups.append({"name": arch_name(g["name"]), "kind": g["kind"], "share": round(g["share"] * 100, 1),
                           "sets": sets, "trend": trend})
        out[ic] = {"season": v.get("season") or PV.season_of(VERSION), "groups": groups}
    json.dump(out, open(OUT, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"{OUT}: {len(out) - 1}種（{VERSION}）" + (f"  アイコン無し {miss}" if miss else ""))


if __name__ == "__main__":
    main()
