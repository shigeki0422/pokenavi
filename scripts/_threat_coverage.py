"""脅威対応カバレッジ特徴：上位メタ各脅威に『受け(STAB半減以下で受け)×撃ち返し(SE or 上取り)』が
あるかでチームの対応率を測る。人間構築論の核。人間テンプレ vs 生成 で妥当性検証。
"""
import os, sys, json, sqlite3, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.data import get_type_effectiveness
from _party_quality import TYPES, adj_eff

NTHREAT = int(os.environ.get("NTHREAT", "30"))

def _spd_stat(base, ev=32, nat=1.0):
    return int(((2 * base + 31 + ev) * 50 // 100 + 5) * nat)

def load_threats(L, n=NTHREAT):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "pokenavi.db"))
    # 相手パネル（_explain.USAGE_SEASON）と同じシーズンを見る。片方だけ古いと
    # 「脅威は旧環境・相性表は新環境」というちぐはぐな評価になる。
    season = os.environ.get("USAGE_SEASON", "M-5")
    cd = con.execute("SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule='single'",
                     (season,)).fetchone()[0]
    names = [r[0] for r in con.execute(
        "SELECT pokemon FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=? "
        "ORDER BY rank LIMIT ?", (season, cd, n))]
    con.close()
    threats = []
    for nm in names:
        t = L.get_pokemon_template(nm, "M-3")
        if t is None: continue
        t1, t2, spe = t.type1, t.type2, t.base_speed
        # よく使うメガ石ならメガ型で脅威評価
        items = t.top_items or []
        if t.mega_data is not None and any("ナイト" in (i[0] if isinstance(i, (list, tuple)) else i) for i in items[:2]):
            md = t.mega_data
            g = (lambda o, *ks: next((o[k] for k in ks if isinstance(o, dict) and k in o), None)) if isinstance(t.mega_data, dict) else (lambda o, *ks: next((getattr(o, k) for k in ks if hasattr(o, k)), None))
            t1 = g(md, "type1", "t1") or t1
            t2 = g(md, "type2", "t2") if g(md, "type2", "t2") is not None else t2
            spe = g(md, "speed", "spe", "base_speed") or spe
        # 攻撃タイプ＝常用ダメージ技のタイプ（無ければSTAB）
        atk = set()
        for mv in (t.top_moves or [])[:6]:
            mn = mv[0] if isinstance(mv, (list, tuple)) else mv
            m = L.get_move(mn)
            if m and m.category in ("physical", "special") and m.type: atk.add(m.type)
        if not atk:
            atk = {x for x in (t1, t2) if x}
        threats.append({"name": nm, "t1": t1, "t2": t2, "spe": _spd_stat(spe), "atk": atk})
    return threats

def team_coverage(specs, L, threats):
    mons = []
    for s in specs:
        p = build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
        if p.mega_data is not None: p.do_mega_evolve()
        mons.append(p)
    handled = 0; miss = []
    for T in threats:
        wall = any(all(adj_eff(a, m.type1, m.type2, m.ability) <= 1 for a in T["atk"]) for m in mons)
        offense = any(
            any(get_type_effectiveness(mv.type, T["t1"], T["t2"]) >= 2 for mv in m.moves if mv.category in ("physical", "special"))
            or (m.speed > T["spe"] and any(mv.category in ("physical", "special") and get_type_effectiveness(mv.type, T["t1"], T["t2"]) >= 1 for mv in m.moves))
            for m in mons)
        if wall and offense: handled += 1
        else: miss.append(T["name"])
    return handled / len(threats), miss

def team_depth(specs, L, threats):
    """各脅威を「1体で完結して」対応できる駒の数（wall と offense を同一個体が満たす）。
    team_coverage は wall と offense を別々の駒が満たしてもよい二値判定なので、
    「1体しか対応できない＝その駒が落ちたら答えがない」という脆弱性を区別できない。
    実測: 平均の厚みはガイド勝率と相関+0.257（二値の対応率は+0.134、ENSサロゲートは+0.180）。
    returns (平均の厚み, 各脅威の厚みリスト)
    """
    mons = []
    for s in specs:
        p = build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
        if p.mega_data is not None: p.do_mega_evolve()
        mons.append(p)
    out = []
    for T in threats:
        c = 0
        for m in mons:
            wall = all(adj_eff(a, m.type1, m.type2, m.ability) <= 1 for a in T["atk"])
            off = (any(get_type_effectiveness(mv.type, T["t1"], T["t2"]) >= 2
                       for mv in m.moves if mv.category in ("physical", "special"))
                   or (m.speed > T["spe"] and any(mv.category in ("physical", "special")
                       and get_type_effectiveness(mv.type, T["t1"], T["t2"]) >= 1 for mv in m.moves)))
            if wall and off: c += 1
        out.append(c)
    return (sum(out) / len(out) if out else 0.0), out


PRIORITY = {"メタグロス", "ブリジュラス", "ゲンガー", "ギャラドス", "クチート"}

def covered_sample(pg, L, threats, rng, min_cov=0.9, tries=6, base=None):
    """数回サンプル(またはbaseを変異)し、脅威対応率が最も高い合法構築を返す。優先脅威の穴を重く減点。"""
    best = None; best_score = -1e9
    for _ in range(tries):
        p = pg.mutate_cooc(base, rng) if base is not None else pg.sample_cooc(rng)
        if not p: continue
        cov, miss = team_coverage(p, L, threats)
        pri = sum(1 for m in miss if m in PRIORITY)
        score = cov - 0.15 * pri
        if score > best_score:
            best_score = score; best = p
            if cov >= min_cov and pri == 0: break
    return best

def main():
    _f1._ensure_loaded("M-3", 8); L = _f1._W["loader"]
    threats = load_threats(L)
    print(f"上位脅威 {len(threats)}体: {[t['name'] for t in threats][:12]}...\n")
    from simulator.env import load_registered_parties, spec_to_string
    hum = [[spec_to_string(s) for s in p.specs] for p in load_registered_parties(L, complete_only=True, season="M-2")]
    ga = [e["party"] for e in json.load(open("gen_pop.json"))]
    import collections
    def report(pop, label):
        cov = []; missc = collections.Counter()
        for party in pop:
            c, miss = team_coverage(party, L, threats); cov.append(c)
            for mn in miss: missc[mn] += 1
        print(f"[{label}] {len(pop)}チーム 平均脅威対応率 {statistics.mean(cov)*100:.1f}%  (min{min(cov)*100:.0f}/max{max(cov)*100:.0f})")
        return cov, missc
    hc, hm = report(hum, "人間テンプレ")
    gc, gm = report(ga, "生成(QD)")
    # サザングロス
    sz = json.load(open("seed_sazangross.json"))[0]
    sc, sm = team_coverage(sz, L, threats)
    print(f"[サザングロス] 脅威対応率 {sc*100:.1f}%")
    print("\n■ 生成でよく取りこぼす脅威TOP10（この脅威への対応を強化すべき）")
    for nm, c in gm.most_common(10):
        print(f"  {nm}: {c}/{len(ga)}チームが未対応")

if __name__ == "__main__":
    main()
