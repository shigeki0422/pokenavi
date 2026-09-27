"""系統表: 型プールの型を、型の意図ごとの系統（最大6つ）にまとめて名前を付ける。
想定型（gen_archetype_data.py）と 1v1 の代表型（gen_builder_data.py）の元になる。
確認ページ（_local/ai_work/scripts/arch_view_data.py）もここを使う。
env: TYPES（型プール） GROUPS_OUT（系統表の出力）"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_type_pool as G   # noqa: E402

con = G.con


def kind(moves):
    """系統: 主力の攻撃技は生成器と同じ判定（G._plain: 先制技・ピボット技・積み技・強制交代・
    素早さを下げる技・イカサマ/ボディプレス等の効果技・威力50未満の効果技を除く）。
    補助＝積み技なし・主力技と先制技が合わせて1本以下・守る/みがわり以外の変化技2本以上。向きは主力の攻撃技で決め、無ければ攻撃技全体で決める"""
    mv = [m for m in moves if m in G.MV]
    status = [m for m in mv if G.MV[m]["cat"] == "status"]
    setup = [m for m in mv if m in G.BOOST]
    main = [m for m in mv if G._plain(m)]
    support = [m for m in status if m not in G.PROTECT and m != "みがわり"]
    prio = [m for m in mv if G.MV[m]["cat"] != "status" and G.MV[m]["pri"] > 0]
    if not setup and len(main) + len(prio) <= 1 and len(support) >= 2:
        return "補助"
    basis = main or [m for m in mv if G.MV[m]["cat"] != "status"]
    ph = any(G.MV[m]["cat"] == "physical" for m in basis)
    sp = any(G.MV[m]["cat"] == "special" for m in basis)
    if ph and sp:
        return "両刀"
    return "物理" if ph else "特殊" if sp else "補助"


def evc(e):
    """努力値の実数（振った能力だけ。例: A32 S32 H2）"""
    return " ".join(f"{k}{v}" for k, v in zip("HABCDS", e) if v) or "無振り"


def setup_class(moves):
    """積み技の区分: 攻撃を上げる／特攻を上げる／その他（防御・素早さ）。つるぎのまい と ビルドアップ は同じ「攻撃を積む型」"""
    cls = set()
    for m in moves:
        if m not in G.BOOST:
            continue
        e = G.MV.get(m, {}).get("eff", "")
        if "特攻" in e:
            cls.add("C")
        elif "攻撃" in e:
            cls.add("A")
        else:
            cls.add("他")
    return "".join(sorted(cls))
SETUP_LABEL = {"A": "攻撃を積む", "C": "特攻を積む", "他": "耐久・素早さを積む", "AC": "攻撃・特攻を積む", "A他": "攻撃と耐久・素早さを積む", "C他": "特攻と耐久・素早さを積む", "AC他": "攻撃・特攻・耐久を積む"}
CHOICE_SHORT = {"こだわりスカーフ": "スカーフ", "こだわりハチマキ": "ハチマキ", "こだわりメガネ": "メガネ"}


_TYPES = {}


def sp_types(sp, item):
    """実際に戦う姿のタイプ（メガ石ならメガ後）"""
    key = (sp, item if (sp, item) in G.MEGA else None)
    if key not in _TYPES:
        r = None
        if key[1]:
            r = con.execute("select type1,type2 from pokemon_mega_stats where mega_stone=?", (item,)).fetchone()
        if r is None:
            r = con.execute("select type1,type2 from pokemon_base_stats where pokemon_name=?", (sp,)).fetchone()
        _TYPES[key] = {t for t in (r or ()) if t}
    return _TYPES[key]


def order_moves(sp, item, moves, share):
    """表示順: タイプ一致の攻撃技 → タイプ不一致の攻撃技 → 変化技。同じ区分の中は種全体の採用率が高い順"""
    ts = sp_types(sp, item)
    def rank(m):
        v = G.MV.get(m, {})
        if v.get("cat") == "status" or not v.get("power"):
            grp = 2
        else:
            grp = 0 if v.get("type") in ts else 1
        return (grp, -share.get(m, 0.0), m)
    return sorted(moves, key=rank)


CORE = 0.85
MAX_GROUPS = 6


def full_attack(gb, th=None):
    """系統のほぼ全部（共通の技と同じ85%以上）が攻撃技4本＝フルアタ"""
    z = sum(b["weight"] for b in gb) or 1.0
    return sum(b["weight"] for b in gb
               if all(G.MV.get(m, {}).get("cat", "status") != "status" for m in b["moves"])) / z >= (CORE if th is None else th)


def group_name(sp, item, mv, sibs, mshare):
    """系統名: 同じ持ち物区分（メガ石・こだわり系・その他）のほかの系統と見分けられるだけの技を選ぶ。
    候補は系統内でほぼ必ず入る技（85%以上。種の共通の技は見出しへ回すので除く）で、
    相手の系統での採用率が半分以下ならその系統と見分けられるとみなす。見分けられる系統が多い技から順に、
    見分けられる系統が残らなくなるまで（最大3つ）足し、表示順で並べる"""
    cand = [m for m, p in mv.items() if p >= CORE and mshare.get(m, 0) < 0.85]
    sep = {m: {i for i, o in enumerate(sibs) if o.get(m, 0.0) <= mv[m] / 2} for m in cand}
    left = set().union(*sep.values()) if sep else set()
    feats = []
    while left and len(feats) < 3:
        m = max((m for m in cand if m not in feats),
                key=lambda m: (len(sep[m] & left), -max((o.get(m, 0.0) for o in sibs), default=0.0)))
        if not sep[m] & left:
            break
        feats.append(m)
        left -= sep[m]
    return "＋".join(order_moves(sp, item, feats, mshare))


def slot_alts(sp, item, mv, mshare):
    """入れ替わる枠: 系統内で2割以上・85%未満の技（種の共通の技を除く）の上位2つ"""
    return [[m, round(mv[m] * 100)] for m in order_moves(sp, item, [m for m, p in mv.most_common()
            if 0.2 <= p < CORE and mshare.get(m, 0) < 0.85][:2], mshare)]


FLAG_ROLES = {"設置", "強制交代", "守る", "変化"}   # 系統を分ける補助の役割（回復・ピボット・吸収は4つ目の枠の選択になりやすいので分けない）
KEY_ATTACKS = {"ボディプレス", "イカサマ"}
GIMMICK = {"バトンタッチ"}   # 型の狙いそのものを決める技（積んだ能力を控えへ渡す）。積むかどうかと同じく必ず分け、名前にも入れる


def key_moves(moves):
    return frozenset(m for m in moves if m in KEY_ATTACKS or G.move_role(m) in FLAG_ROLES)


def jac(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0



def group_species(sp, bs):
    """系統: メガ石・こだわり系の持ち物・積むかどうか（上げる能力）・向き（物理/特殊/両刀/補助）で必ず分け、
    その中は補助の役割の技（設置・強制交代・守る・変化技、ボディプレス/イカサマ）の組が半分以上重なればまとめる。
    こだわりの型はトリックかどうかだけで分ける。5%未満は同じ区分で重なりが最大の系統へ寄せ、名前が同じ系統はまとめる。
    返り値: (確認ページ用の系統の一覧（割合の降順）, 系統表の系統)"""
    z = sum(b["weight"] for b in bs)
    stones = {it for (s2, it) in G.MEGA if s2 == sp}
    mshare = collections.Counter()
    for b in bs:
        for m in b["moves"]:
            mshare[m] += b["weight"] / z
    raw = collections.defaultdict(list)
    for b in bs:
        tag = (b["item"] if b["item"] in stones else CHOICE_SHORT.get(b["item"]), setup_class(b["moves"]), kind(b["moves"]),
               frozenset(GIMMICK & set(b["moves"])))
        if tag[3]:
            tag = (None, "", "", tag[3])   # バトンタッチの型は持ち物・積むかどうか・向きで分けず1つにまとめる
        keys = frozenset({"トリック"} & set(b["moves"])) if tag[0] in CHOICE_SHORT.values() else key_moves(b["moves"])
        if tag[3]:
            keys = tag[3]
        raw[(tag, keys)].append(b)
    clusters = []
    for (tag, keys), gb in sorted(raw.items(), key=lambda kv: -sum(b["weight"] for b in kv[1])):
        best = next((c for c in clusters if c["tag"] == tag and jac(c["keys"], keys) >= 0.5), None)
        if best is None:
            clusters.append({"tag": tag, "keys": keys, "builds": list(gb)})
        else:
            best["builds"] += gb
    big = [c for c in clusters if sum(b["weight"] for b in c["builds"]) / z >= 0.05]
    for c in clusters:
        if c in big:
            continue
        cand = [x for x in big if x["tag"] == c["tag"]]
        if cand:
            max(cand, key=lambda x: jac(x["keys"], c["keys"]))["builds"] += c["builds"]
        else:
            big.append(c)

    def shares(gb):
        gz = sum(b["weight"] for b in gb) or 1.0
        cc = collections.Counter()
        for b in gb:
            for m in b["moves"]:
                cc[m] += b["weight"] / gz
        return cc

    def other(gb):
        ids = {id(b) for b in gb}
        return shares([b for b in bs if id(b) not in ids])

    def sibs(c, cs):
        return [shares(x["builds"]) for x in cs if x is not c and x["tag"][0] == c["tag"][0]]

    def nm(c):
        gb = c["builds"]
        return (c["tag"][0], c["tag"][1], c["tag"][3], "フルアタ" if full_attack(gb) else group_name(sp, max(gb, key=lambda b: b["weight"])["item"], shares(gb), sibs(c, big), mshare))
    # 名前が同じ系統（区分の細部だけが違う）は1つにまとめる。まとめると名前が変わりうるので落ち着くまで繰り返す
    for _ in range(5):
        merged = {}
        for c in sorted(big, key=lambda c: -sum(b["weight"] for b in c["builds"])):
            k = nm(c)
            if k in merged:
                merged[k]["builds"] += c["builds"]
            else:
                merged[k] = c
        if len(merged) == len(big):
            break
        big = list(merged.values())
    # 型の数は実態に合わせて多くて6つ。5%未満は同じ持ち物の区分（メガ石・こだわり系・その他）で最も近い系統へ寄せ、
    # それでも6つを超えれば同じ区分で最も近い2つをまとめる。区分はまたがない（メガ石の系統にスカーフが混ざった）
    # 近さ＝技の採用率の差（半分に割った L1）。持ち物の区分（メガ石・こだわり系・その他）と積むかどうかが違えば遠ざける
    def dist(a, b):
        sa, sb = shares(a["builds"]), shares(b["builds"])
        d = sum(abs(sa.get(m, 0.0) - sb.get(m, 0.0)) for m in set(sa) | set(sb)) / 2
        return d + (1.0 if a["tag"][0] != b["tag"][0] else 0.0) + (0.5 if bool(a["tag"][1]) != bool(b["tag"][1]) else 0.0) \
            + (0.5 if a["tag"][3] != b["tag"][3] else 0.0)
    wt = lambda c: sum(b["weight"] for b in c["builds"])
    for c in sorted([c for c in big if wt(c) / z < 0.05], key=wt):
        rest = [x for x in big if x is not c and wt(x) / z >= 0.05 and x["tag"][0] == c["tag"][0]]
        if rest:
            min(rest, key=lambda x: dist(c, x))["builds"] += c["builds"]
            big.remove(c)
    while len(big) > MAX_GROUPS:
        same = [(a, b) for i, a in enumerate(big) for b in big[i + 1:] if a["tag"][0] == b["tag"][0]]
        if not same:
            break
        a, b = min(same, key=lambda ab: dist(*ab))
        keep, drop = (a, b) if wt(a) >= wt(b) else (b, a)
        keep["builds"] += drop["builds"]
        big.remove(drop)
    # 名前が同じになった系統は見分けられないのでまとめ、名前を付け直す（向きだけが違う同名の系統も残さない。バチンウニのグランドコート×2）
    for _ in range(5):
        arr = []
        gtab = []
        for c in big:
            gb = c["builds"]
            gz = sum(b["weight"] for b in gb)
            if gz / z < 0.01:
                continue
            def top(key, n):
                cc = collections.Counter()
                for b in gb:
                    cc[key(b)] += b["weight"] / gz
                return [[x, round(v * 100, 1)] for x, v in cc.most_common(n)]
            mv = collections.Counter()
            for b in gb:
                for m in b["moves"]:
                    mv[m] += b["weight"] / gz
            tag = c["tag"][0]
            head = ("メガ" if len(stones) < 2 else tag) if tag in stones else tag
            item0 = max(gb, key=lambda b: b["weight"])["item"]
            kind0 = collections.Counter()
            for b in gb:
                kind0[kind(b["moves"])] += b["weight"]
            kind0 = kind0.most_common(1)[0][0]
            # 名前に載る技が無ければ型の性質（向き・積み技）で名付ける。横の区分表示と重なるので、そのときは区分表示を省く
            # 積み技は区分名ではなく技名で示す（系統内2割以上の積み技を多い順に「／」で並べる）
            setup_nm = "／".join(m for m, p in mv.most_common() if m in G.BOOST and p >= 0.2) if c["tag"][1] or c["tag"][3] else ""
            gname = group_name(sp, item0, mv, sibs(c, [x for x in big if sum(b["weight"] for b in x["builds"]) / z >= 0.01]), mshare)
            by_tag = not full_attack(gb) and not gname
            # 名前の攻撃技が系統の向きと逆の分類だけ（特殊の系統に しんそく）だと型を表さないので、向きの技を添える
            kc = {"物理": "physical", "特殊": "special"}.get(kind0)
            atk = [m for m in gname.split("＋") if m in G.MV and G.MV[m]["cat"] != "status" and m not in G.BOOST]
            if kc and atk and not any(G.MV[m]["cat"] == kc for m in atk):
                gname += "＋" + kind0 + "技"
            # 積み技は必ず主の名前に入れる（名前の技に無い分を後ろに足す）
            extra = "／".join(m for m in setup_nm.split("／") if m and m not in gname.split("＋"))
            extra = "＋".join(x for x in [m for m in sorted(c["tag"][3]) if m not in gname.split("＋")] + [extra] if x)
            gname = "＋".join(x for x in (gname, extra) if x)
            # 技で見分けられない系統は持ち物で見分ける（系統内2割以上の持ち物を多い順に2つまで）
            itc = collections.Counter()
            for b in gb:
                itc[b["item"]] += b["weight"] / gz
            items_nm = "／".join(i for i, p in itc.most_common(2) if p >= 0.2 and i)
            # 持ち物は同じ区分のほかの系統と見分けるための名前なので、型が1つの種では使わない
            if len([x for x in big if sum(b["weight"] for b in x["builds"]) / z >= 0.01]) == 1:
                items_nm = "単一の型"
            # 見分ける技も積み技も無い系統は、攻撃技4本が過半ならフルアタ、そうでなければ持ち物（メガ石などの区分名が付く系統は区分名だけ）
            if not gname and head:
                # 区分名（メガ・スカーフ）だけで同じ区分の相手がいない系統は、区分名だけでは中身が分からないので、
                # ほぼ必ず入り（85%以上）ほかの系統全体の2倍以上ある技を2つまで添える
                mo = other(gb)
                ch = [m for m, p in mv.items() if p >= CORE and mshare.get(m, 0) < 0.85 and p >= 2 * max(mo.get(m, 0.0), 0.05)]
                ch = sorted(ch, key=lambda m: -(mv[m] / max(mo.get(m, 0.0), 0.05)))[:2]
                gname = "＋".join(order_moves(sp, item0, ch, mshare))
            name = "フルアタ" if full_attack(gb) else (gname or ("フルアタ" if full_attack(gb, 0.5) else
                                                        ("" if head else (items_nm or f"{kind0}型"))))
            alts = slot_alts(sp, item0, mv, mshare)
            if head:
                name = f"{head}・{name}" if name else head
            kk = collections.Counter()
            for b in gb:
                kk[kind(b["moves"])] += b["weight"]
            gw = sum(b["weight"] for b in gb)
            gtab.append({"name": name, "kind": kk.most_common(1)[0][0], "share": gz / z,
                         "builds": [dict(b, weight=b["weight"] / gw) for b in gb]})
            arr.append({"_c": c, "name": name, "alts": alts, "kind": kk.most_common(1)[0][0], "setup": "", "by_tag": by_tag, "mega": tag in stones,
                        "share": round(gz / z * 100, 1),
                        "moves": [[m, round(p * 100)] for m, p in mv.most_common(8) if p >= 0.01],
                        "sets": top(lambda b: "｜".join(order_moves(sp, b["item"], b["moves"], mshare)), 3),
                        "items": top(lambda b: b["item"], 3), "abilities": top(lambda b: b.get("ability") or "不明", 3), "natures": top(lambda b: b["nature"], 3),
                        "evs": top(lambda b: evc(b["ev"]), 4)})

        lab = collections.defaultdict(list)
        for x in arr:
            lab[x["name"]].append(x["_c"])
        dups = [cs for cs in lab.values() if len(cs) > 1]
        if not dups:
            break
        for cs in dups:
            for c2 in cs[1:]:
                cs[0]["builds"] += c2["builds"]
                big.remove(c2)
    for x in arr:
        x.pop("_c")
    arr.sort(key=lambda x: -x["share"])
    return arr, gtab


def main():
    pool = json.load(open(os.environ["TYPES"]))
    d = G.latest("pokemon_usage", None)
    rank = dict(con.execute("select pokemon,rank from pokemon_usage where season=? and crawled_date=?", (G.SEASON, d)))
    out = {}
    for r in pool:
        _, gtab = group_species(r["species"], r["builds"])
        out[r["species"]] = {"rank": rank.get(r["species"]), "groups": gtab}
        if r.get("season"):
            out[r["species"]]["season"] = r["season"]
    json.dump(out, open(os.environ["GROUPS_OUT"], "w"), ensure_ascii=False)
    print(f"{os.environ['GROUPS_OUT']}: {len(out)}種", file=sys.stderr)


if __name__ == "__main__":
    main()
