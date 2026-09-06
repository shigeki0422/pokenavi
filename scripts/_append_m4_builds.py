"""M-4上位構築の実型を build_pool_M-4_extra.md として書き出す。

型プールはドラフト（機械列挙）だと品質に難があるので、実際に使われた構築から
そのまま型を取る。build_pool_M-3_extra.md（M-3上位88構築から抽出）と同じ書式・
同じ扱いで gen_party_pool がマージする。

既に本体(build_pool_M-3.md)やM-3のextraにある型と同一のものは書かない（重複防止）。
順位見出し(#N)は本体mdの順位を引き継ぐ。本体に無い種は末尾にまとめる。

env: SRC(m4_top74.json) OUT(build_pool_M-4_extra.md)
"""
import collections
import json
import os
import re

D = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("SRC", os.path.join(D, "m4_top74.json"))
OUT = os.environ.get("OUT", os.path.join(D, "build_pool_M-4_extra.md"))
BASE = [os.path.join(D, "build_pool_M-3.md"), os.path.join(D, "build_pool_M-3_extra.md")]
EVK = ["H", "A", "B", "C", "D", "S"]
HEADER = re.compile(r"^## ([^#]+?)\s+#(\d+)")
TYPE_LINE = re.compile(r"^\s*-\s*(?:\*\*[^*]+\*\*\s*)?\[([^/]*)/([^/]*)/([^/]*)/([^\]]*)\]\s*(.+)$")


def ev_str(ev: str) -> str:
    """spec の "2/32/0/0/0/32" を md の "H2 A32 S32" に直す。"""
    try:
        v = [int(x) for x in ev.split("/")]
    except ValueError:
        return ev
    return " ".join(f"{k}{n}" for k, n in zip(EVK, v) if n) or "なし"


def key(item, nature, ability, moves, evs):
    """同一型の判定。技は順不同、EVは表記を揃えて比べる。"""
    return (item.strip(), nature.strip(), ability.strip(),
            frozenset(m.strip() for m in moves), evs.strip())


def main() -> None:
    known = collections.defaultdict(set)   # 種 -> 既出の型
    ranks = {}
    cur = None
    for path in BASE:
        if not os.path.exists(path):
            continue
        for ln in open(path, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if ln.startswith("## "):
                h = HEADER.match(ln)
                cur = h.group(1).strip() if h and not ln[3:].startswith("（") else None
                if h and cur:
                    ranks.setdefault(cur, int(h.group(2)))
                continue
            if cur is None:
                continue
            m = TYPE_LINE.match(ln)
            if m:
                it, na, ab, ev, mv = (x.strip() for x in m.groups())
                known[cur].add(key(it, na, ab, mv.split("/"), ev))

    parties = json.load(open(SRC, encoding="utf-8"))
    add = collections.defaultdict(list)
    seen = collections.defaultdict(set)
    n_party = 0
    for entry in parties:
        n_party += 1
        for spec in entry.get("party", []):
            head, rest = spec.split("@", 1)
            it, na, mv, ev, ab = rest.split(":")
            moves = [m for m in mv.split("|") if m]
            evs = ev_str(ev)
            k = key(it, na, ab, moves, evs)
            if k in known[head] or k in seen[head]:
                continue
            seen[head].add(k)
            add[head].append(f"- [{it}/{na}/{ab}/{evs}] " + "/".join(moves))

    known_sp = [s for s in sorted(add, key=lambda s: ranks.get(s, 9999)) if s in ranks]
    new_sp = [s for s in sorted(add) if s not in ranks]
    out = [f"# M-4 追加型プール（上位{n_party}構築から抽出。ドラフト型は含まない）", ""]
    for sp in known_sp:
        out.append(f"## {sp}  #{ranks[sp]}  -/-")
        out += add[sp]
        out.append("")
    if new_sp:
        out.append("## （M-4上位のみ・本体mdに項目なし）")
        for sp in new_sp:
            out.append(f"### {sp}")
            out += add[sp]
            out.append("")
    open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"{OUT}: {sum(len(v) for v in add.values())}型 / {len(add)}種 "
          f"（{n_party}構築から。既出と重複する型は除外）")


if __name__ == "__main__":
    main()
