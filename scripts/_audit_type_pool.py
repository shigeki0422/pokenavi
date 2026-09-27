"""型プールの監査。リザードンで起きた「特殊技が物理型に入る」類のバグを機械的に探す。

重みつきで違反率を出し、代表例を添える。目視では198種×数千型を確認できない。
env: TYPES(_local/ai_work/type_pool_M-6.json) SEASON(M-6) TOP(3)
"""
import collections
import json
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pool_versions as PV  # noqa: E402
from _gen_type_pool import MV, MEGA, MEGA_AB, BASE, SETUP, BOOST, PIVOT, RECOVERY, PROTECT, \
    CHOICE, FRAGILE, ATK_X2, _BASE_AB, form_stats, _plain, con  # noqa: E402
from simulator.data import NATURE_MODS  # noqa: E402
import _gen_type_pool as G  # noqa: E402

# 生成器は「使用率と両立しない規則はその種で外す」。監査も同じ判定で、
# 使用率が強制する組み合わせは違反に数えない（数えると意図した挙動を誤りと報告する）。
_REL = {}


def relax(sp):
    if sp in _REL:
        return _REL[sp]
    mg = G.marginals(sp) or {}
    P = mg.get("moves", {})
    items = mg.get("items", {})
    nats = mg.get("natures", {})
    real = [m for m in P if m != G.TAIL]
    must = G.forced_pairs(P, real)
    must |= {(y, x) for x, y in must}
    frag = sum(p for i, p in items.items() if i in G.FRAGILE)
    defn = sum(p for n, p in nats.items()
               if NATURE_MODS.get(n, (None, None))[0] in G.DEF_UP
               or NATURE_MODS.get(n, (None, None))[0] is None)
    atk = sum(p for m, p in P.items() if G.MV.get(m, {}).get("cat", "status") != "status")
    _REL[sp] = (must, frag + defn > 1.02, atk < 1.1)
    return _REL[sp]

TYPES = os.environ.get("TYPES") or PV.path("type_pool", PV.pointer("season"))
SEASON = os.environ.get("SEASON", "M-6")
TOP = int(os.environ.get("TOP", "3"))

USED = collections.defaultdict(set)
for _sp, _m in con.execute("select pokemon,move from pokemon_moves"):
    USED[_sp].add(_m)

LEARN = collections.defaultdict(set)
for _sp, _m in con.execute("select pokemon_name,move_jp from pokemon_learnsets"):
    LEARN[_sp].add(_m)

# 天候・フィールドを作れる特性は ability_master の効果テキストから拾う。
# 表をハードコードすると漏れる（メガメガニウムの「メガソーラー」を見落とした）。
_AB_EFF = {r[0]: (r[1] or "") for r in
           con.execute("select name_jp,effect_text from ability_master")}
# 表記が揺れる（ひでりは「にほんばれ状態にする」、メガソーラーは「晴れ」）ので語を並べる
SUN_AB = {k for k, v in _AB_EFF.items()
          if any(w in v for w in ("にほんばれ", "晴れ", "ひざしがつよい"))}
GRASS_AB = {k for k, v in _AB_EFF.items() if "グラスフィールド" in v}
# 天候・フィールドに依存する技 → それを作る手段（特性の集合 or 技）
WEATHER = {
    "ソーラービーム": (SUN_AB, "にほんばれ"),
    "ソーラーブレード": (SUN_AB, "にほんばれ"),
    "グラススライダー": (GRASS_AB, "グラスフィールド"),
}


def form_of(sp, item):
    """その持ち物で戦う姿の (攻撃, 特攻, 特性)。ちからもち等の攻撃2倍も反映する。"""
    a, c = form_stats(sp, item)
    ab = MEGA_AB.get((sp, item)) or _BASE_AB.get(sp) or ""
    return a, c, ab


def check(sp, b):
    """1つの型に対する違反のリスト。"""
    out = []
    mv = b["moves"]
    it = b["item"]
    na = b["nature"]
    ev = b["ev"]
    a, c, mega_ab = form_of(sp, it)
    plain = [m for m in mv if m in MV and _plain(m)]
    ph = [m for m in plain if MV[m]["cat"] == "physical"]
    spc = [m for m in plain if MV[m]["cat"] == "special"]

    # 1. 実際に戦う姿の能力と主力技の向きが逆
    # 実数値の大小だけで型は決まらない（メガスターミーはA100C130だが使用は物理89.5%）。
    # 明確に不合理な差（2倍以上）だけを見る。
    if ph and not spc and c > a * 2.0:
        out.append("特殊型の姿に物理主力のみ")
    if spc and not ph and a > c * 2.0:
        out.append("物理型の姿に特殊主力のみ")
    # 2. 努力値が主力の向きと逆
    if ph and not spc and ev[1] == 0 and ev[3] > 0:
        out.append("物理主力なのにC振りのみ")
    if spc and not ph and ev[3] == 0 and ev[1] > 0:
        out.append("特殊主力なのにA振りのみ")
    # 3. 性格が主力を下げている
    _u, dn = NATURE_MODS.get(na, (None, None))
    if dn == "attack" and ph and not spc:
        out.append("性格がAを下げるのに物理主力")
    if dn == "sp_attack" and spc and not ph:
        out.append("性格がCを下げるのに特殊主力")
    # 4. 天候・フィールド依存技に起動手段が無い
    # 天候・フィールドは味方が張る前提の構築がある（オオニューラ＋イエッサンのサイコシード等）。
    # 単体の型としては違反にできないので、参考値として自力起動できない割合だけ数える。
    for m, (abils, setter) in WEATHER.items():
        if m in mv and mega_ab not in abils and setter not in mv:
            out.append(f"[参考] {m}を自力起動できない")
    # 5. 既存の硬制約が破られていないか（実装の回帰チェック）
    if it in CHOICE and (set(mv) & (SETUP | PROTECT | RECOVERY)):
        out.append("こだわり＋変化技")
    if G._boost_clash(mv):
        out.append("同じ攻撃能力の積み技2本")
    must, frag_off, noatk_ok = relax(sp)
    if it in FRAGILE and not frag_off and not (it in CHOICE and set(mv) & G.PASS_ITEM):
        up, _d = NATURE_MODS.get(na, (None, None))
        if up in ("defense", "sp_defense") or up is None:
            out.append("耐久を捨てる持ち物＋防御性格")
    if not noatk_ok and not any(m in MV and MV[m]["cat"] != "status" for m in mv):
        out.append("攻撃技0本")
    t = collections.Counter(MV[m]["type"] for m in mv if m in MV and _plain(m))
    if any(v >= 3 for v in t.values()):
        out.append("同タイプ主力3本")
    # 重複の判定は生成器と同じ（同効果・威力比）。使用率が併用を強制する対は除く
    for i, x in enumerate(plain):
        for y in plain[i + 1:]:
            if MV[x]["type"] != MV[y]["type"] or (x, y) in must:
                continue
            pa, pb = G.eff_power(x), G.eff_power(y)
            if (MV[x]["cat"] == MV[y]["cat"] and MV[x]["eff"] == MV[y]["eff"]) or \
                    max(pa, pb) / min(pa, pb) < G.POWER_RATIO:
                out.append("同タイプ火力の重複")
                break
    # 6. 習得できない技
    # learnset テーブルは登録漏れが多い（メタグロス60件のみ）。
    # 使用率データにも learnset にも無い技だけを違反とする。
    if LEARN.get(sp):
        for m in mv:
            if m not in LEARN[sp] and m not in USED.get(sp, ()):
                out.append(f"非習得技 {m}")
                break
    # 6b. メガ石が2種類ある種で、技の向きと石の向きが逆（物理技だけにガブリアスナイトZ 等）
    if not G.mega_orient_ok(sp, it, mv):
        out.append("技の向きと逆のメガ石（石が2種類ある種）")
        # 7. メガ石が他種のもの
    if it.endswith("ナイト") or it.endswith("ナイトX") or it.endswith("ナイトY") \
            or it.endswith("ナイトZ"):
        if (sp, it) not in MEGA:
            out.append("他種のメガ石")
    return out


def main():
    d = json.load(open(TYPES))
    tally = collections.Counter()
    ex = collections.defaultdict(list)
    tot = 0.0
    for r in d:
        sp = r["species"]
        z = sum(b["weight"] for b in r["builds"]) or 1.0
        for b in r["builds"]:
            w = b["weight"] / z / len(d)
            tot += w
            for v in check(sp, b):
                key = v.split(" ")[0] if v.startswith("非習得技") else v
                tally[key] += w
                if len(ex[key]) < TOP and b["weight"] / z > 0.005:
                    ex[key].append(f"{sp} {b['weight']/z*100:.1f}% @{b['item']} "
                                   f"{b['nature']} {'|'.join(b['moves'])} "
                                   f"{'/'.join(map(str, b['ev']))}")
    print(f"型プール監査  {len(d)}種   （違反率は種ごとに重みを正規化した平均）\n")
    if not tally:
        print("  違反なし")
        return
    for k, v in tally.most_common():
        print(f"  {v/tot*100:6.2f}%  {k}")
        for e in ex[k]:
            print(f"            {e}")


def gen_rules(sp, mv, it, na, season):
    """生成器が型に課す規則を実型1件に当て、弾かれる規則の名前を返す。
    規則の緩和（使用率が強制する対など）はその実型のシーズンの使用率で判定する。"""
    G.SEASON = season
    must, frag_off, noatk_ok = relax_at(sp, season)
    G._MUST.clear()
    G._MUST.update(must)
    G._FRAGILE_OFF[0] = frag_off
    G._NOATK_OK[0] = noatk_ok
    op = open_at(sp, season)
    core = [m for m in mv if m not in op]
    out = []
    if not G.valid(tuple(mv)):
        out.append("技の硬制約(valid)")
    elif not G.item_ok(mv, it):
        out.append("こだわり＋変化技")
    side = G.nature_side(na)
    bad = [m for m in core if not G.gate(m, side)]
    if bad:
        out.append(f"性格の層に入らない技({side})")
    if not G.natures_for(core, {na: 1.0}):
        out.append("性格が主力を下げる")
    if not G.nature_item_ok(it, na, mv):
        out.append("耐久を捨てる持ち物＋防御性格")
    if it not in G.items_for(sp, side, {it: 1.0}):
        out.append("層に合わないメガ石")
    if not G.mega_orient_ok(sp, it, core, season):
        out.append("技の向きと逆のメガ石（石が2種類ある種）")
    return out


_RELS = {}
_OPEN = {}


def open_at(sp, season):
    """生成器と同じく、層の容量を使用率が超える技（全層に開放される技）。"""
    key = (sp, season)
    if key not in _OPEN:
        mg = G.marginals(sp) or {}
        P = mg.get("moves", {})
        sides = G.side_weights(mg.get("natures", {})) if mg.get("natures") else {}
        _OPEN[key] = {m for m in P if m != G.TAIL and
                      P[m] > sum(sides[k] for k in sides if G.gate(m, k)) + 0.02}
    return _OPEN[key]


def relax_at(sp, season):
    key = (sp, season)
    if key not in _RELS:
        _REL.pop(sp, None)
        _RELS[key] = relax(sp)
        _REL.pop(sp, None)
    return _RELS[key]


def audit_templates():
    """上位構築（templates）を生成器の規則に通し、実在する型を弾く規則がないか調べる。"""
    usage_seasons = {r[0] for r in con.execute("select distinct season from pokemon_usage")}
    tally = collections.Counter()
    ex = collections.defaultdict(list)
    n = 0
    for sp, lab, it, na, *mv in con.execute(
            "select pokemon,label,item,nature,move1,move2,move3,move4 from templates"):
        mv = [m for m in mv if m]
        season = lab.split("#")[0]
        if season not in usage_seasons:
            season = "M-2"
        n += 1
        for v in gen_rules(sp, mv, it, na, season):
            tally[v] += 1
            ex[v].append(f"{lab.split(' ')[0]} {sp} @{it} {na} {'|'.join(mv)}")
    print(f"上位構築 {n}型 を生成器の規則に通した結果\n")
    for k, v in tally.most_common():
        print(f"  {v:4d}型 ({v/n*100:.2f}%)  {k}")
        for e in ex[k][:TOP]:
            print(f"            {e}")


if __name__ == "__main__" and os.environ.get("SRC") == "templates":
    audit_templates()
elif __name__ == "__main__":
    main()
