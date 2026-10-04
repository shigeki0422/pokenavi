"""系統単位の共進化（M-6）。

パーティは6枠の（種, 系統）。共進化が選ぶのは種と系統で、対戦で使う型は毎戦その系統の中から
型プールの重みどおりに引く（系統内の技・持ち物・性格・努力値は使用率どおりに保たれる）。
系統表は _local/ai_work/frozen/type_groups_M-6_v40.json（固定）（arch_view_data.py の GROUPS_OUT）。
評価は Rust の MCTS（本番ネット・既定50sims）、選出は6体から3体を無作為（A/B と同じ）。

使い方:
  venv/bin/python _coevo_groups.py base  N OUT     使用率どおりの集団（系統の割合固定）を N 党
  venv/bin/python _coevo_groups.py evo   POP GENS GAMES OUT
env: GROUPS COEVO_SIMS(50) COEVO_WORKERS(12) SEED(0)
     種の多様性の圧力（既定はすべて OFF＝従来どおり）:
       COEVO_SP_CAP(0)   同じ種を含む党の割合の上限（例 0.3）。生存と子の生成で守る
       COEVO_SHARE(0)    fitness sharing の係数。順位付けの適応度 = 勝率 − 係数×（党の6種の集団内の頻度の平均）
       COEVO_NICHE_SP(0) 1ならニッチの区分に「集団で最も多い種を含むか」を足す
"""
import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from multiprocessing import Pool

import _pop_gen as PG
import seed_rule

HERE = os.path.dirname(os.path.abspath(__file__))
GROUPS = os.environ.get("GROUPS", os.path.join(os.path.dirname(HERE), "_local", "ai_work", "frozen", "type_groups_M-6_v40.json"))
SEASON = "M-6"
SIMS = int(os.environ.get("COEVO_SIMS", "50"))
WORKERS = int(os.environ.get("COEVO_WORKERS", "12"))
SELECT = os.environ.get("COEVO_SELECT", "heur")
BASE = os.environ.get("COEVO_BASE", os.path.join(os.path.dirname(HERE), "_local", "ai_work", "coevo_base_M-6.json"))
SP_CAP = float(os.environ.get("COEVO_SP_CAP", "0"))
SHARE = float(os.environ.get("COEVO_SHARE", "0"))
NICHE_SP = os.environ.get("COEVO_NICHE_SP", "0") == "1"

_G = {}


def load():
    if not _G:
        os.environ.setdefault("POOL_SEASON", SEASON)
        os.environ.setdefault("USAGE_SEASON", SEASON)
        from gen_party_pool import PartyGen
        import _necessity_verify as V
        from simulator.simulate import get_loader
        _G["pg"], _G["V"], _G["L"] = PartyGen(), V, get_loader()
        _G["groups"] = json.load(open(GROUPS))
        _G["D"] = PG.load(season=SEASON)
        stones = _G["D"]["megastones"]
        _G["mega"] = {sp: [sum(b["weight"] for b in g["builds"] if b["item"] in stones) >= 0.5 for g in v["groups"]]
                      for sp, v in _G["groups"].items()}
    return _G


def spec_of(sp, b):
    return "%s@%s:%s:%s:%s:%s" % (sp, b["item"], b["nature"], "|".join(b["moves"]),
                                  "/".join(str(x) for x in b["ev"]), b["ability"])


def _pick_group(sp, rng, mega=None):
    g = load()
    gs = g["groups"][sp]["groups"]
    w = {i: x["share"] for i, x in enumerate(gs) if mega is None or g["mega"][sp][i] == mega}
    return PG._wchoice(w, rng) if w else None


def _species(rng):
    """種の組は _pop_gen.gen_party と同じ（使用率の Zipf＋同居率）。型プールに無い種は外す"""
    g = load()
    back = pool_names(g["groups"])
    for _ in range(50):
        team = [back.get(m["name"], m["name"]) for m in map(_parse_name, PG.gen_party(g["D"], rng))]
        if all(sp in g["groups"] for sp in team):
            return team
    raise RuntimeError("型プールにある種だけでパーティを作れない")


def pool_names(groups):
    """_pop_gen の種名（「:」の無い正規名。ケンタロス:炎→ケンタロス(炎)）から型プールの種名への表。
    フォルム補正した種（source_species）は元の種名からも引く（監査200 T1: ケンタロス:炎 が生成集団に0体だった）"""
    back = {PG.canon(k): k for k in groups}
    back.update({PG.canon(v["source_species"]): k for k, v in groups.items() if v.get("source_species")})
    return back


def _parse_name(spec):
    return {"name": spec.split("@")[0].split(":")[0]}


# メガを外す枠の種で、メガでない系統の割合がこれ未満なら種ごと入れ替える（2026-10-04・監査40 #23）。
# メガが3枠になった党でメガでない系統へ落とすと、カメックスの しろいハーブ（使用率1.6%）が生成集団で24〜29%、
# ゲンガーの きあいのタスキ（22%）が40% のように、少数派の非メガ系統が膨らんでいた
NONMEGA_MIN = float(os.environ.get("COEVO_NONMEGA_MIN", "0.15"))


def _nonmega_share(sp):
    g = load()
    return sum(x["share"] for x, m in zip(g["groups"][sp]["groups"], g["mega"][sp]) if not m)


def repair(party, rng):
    """メガの系統は1〜2枠（上位構築はメガ石2個が84%、3個は禁止）。外す枠はメガでない系統の割合が大きい種から選び、
    それも NONMEGA_MIN 未満なら種ごとメガでない種へ入れ替える"""
    g = load()
    mg = [i for i, (sp, gi) in enumerate(party) if g["mega"][sp][gi]]
    while len(mg) > 2:
        best = max(_nonmega_share(party[j][0]) for j in mg)
        cand = [j for j in mg if _nonmega_share(party[j][0]) == best]
        i = cand[rng.randrange(len(cand))]
        mg.remove(i)
        gi = _pick_group(party[i][0], rng, mega=False) if best >= NONMEGA_MIN else None
        while gi is None:     # メガの系統しか無い（少ない）種は、メガの無い種へ入れ替える
            sp = _fresh_species(rng, {x for x, _ in party})
            gi = _pick_group(sp, rng, mega=False)
            party[i] = (sp, gi)
        party[i] = (party[i][0], gi)
    if not mg:
        cand = [i for i, (sp, _) in enumerate(party) if any(g["mega"][sp])]
        if cand:
            i = rng.choice(cand)
            party[i] = (party[i][0], _pick_group(party[i][0], rng, mega=True))
    return party


def plausible(specs):
    """パーティ提案と同じ基準（gen_party_pool.PartyGen.is_legal と _necessity_verify.excess）。
    6体・種の重複なし・メガ1〜2・持ち物の重複なし・同じタイプ2体まで、かつ構成の違反（タイプ・役割・弱点の重なり）が無い"""
    g = load()
    return g["pg"].is_legal(specs, megas_set=(1, 2)) and g["V"].excess(specs, g["pg"], g["L"]) == 0


def proto(party):
    """系統ごとの最も重い型で6体を具体化（遺伝子の段階の判定用。持ち物の重複は具体化で引き直すので見ない）"""
    g = load()
    return [spec_of(sp, max(g["groups"][sp]["groups"][gi]["builds"], key=lambda b: b["weight"])) for sp, gi in party]


def ok_genome(party):
    g = load()
    specs = proto(party)
    if len({g["pg"].dexof(x) for x in specs}) != 6:
        return False
    nmega = sum(1 for sp, gi in party if g["mega"][sp][gi])
    if not 1 <= nmega <= 2:
        return False
    from gen_party_pool import TYPEDUP_MAX
    if TYPEDUP_MAX and g["pg"].type_dup_max(specs) > TYPEDUP_MAX:
        return False
    return g["V"].excess(specs, g["pg"], g["L"]) == 0


def _retry(make, rng, tries=60):
    """提案と同じ基準を満たすまで作り直す（満たせなければ最後の案）"""
    x = None
    for _ in range(tries):
        x = make()
        if ok_genome(x):
            return x
    return x


def _fresh_species(rng, exclude):
    g = load()
    uw = {p: 1.0 / rk for p, rk in g["D"]["usage"] if p in g["groups"] and p not in exclude}
    return PG._wchoice(uw, rng)


def gen_party(rng):
    return _retry(lambda: repair([(sp, _pick_group(sp, rng)) for sp in _species(rng)], rng), rng)


def instantiate(party, rng, tries=200):
    """系統から型を引く。同じ持ち物はパーティに1つ（重複したら引き直す）。
    シードの型は設置役がいるときだけ（いなければ同じ系統の別の持ち物の型に替える＝seed_rule）"""
    g = load()
    for _ in range(tries):
        used, out, dup = set(), [], False
        for sp, gi in party:
            bs = g["groups"][sp]["groups"][gi]["builds"]
            pick = [b for b in bs if b["item"] not in used]
            if not pick:
                pick, dup = bs, True
            b = rng.choices(pick, weights=[x["weight"] for x in pick])[0]
            used.add(b["item"])
            out.append(spec_of(sp, b))
        if dup:
            continue
        fixed = seed_rule.fix(out, lambda i: [(spec_of(party[i][0], b), b["weight"])
                                              for b in g["groups"][party[i][0]]["groups"][party[i][1]]["builds"]], rng)
        if fixed is not None:
            out = fixed
            if plausible(out):
                return out
    return out


def mutate(party, rng):
    return _retry(lambda: _mutate(party, rng), rng, 30)


def _mutate(party, rng):
    party = list(party)
    i = rng.randrange(6)
    r = rng.random()
    if r < 0.4:
        sp = _fresh_species(rng, {s for s, _ in party})
        party[i] = (sp, _pick_group(sp, rng))
    else:
        sp = party[i][0]
        n = len(load()["groups"][sp]["groups"])
        if n > 1:
            party[i] = (sp, rng.choice([x for x in range(n) if x != party[i][1]]))
    return repair(party, rng)


def crossover(a, b, rng):
    return _retry(lambda: _crossover(a, b, rng), rng, 30)


def _crossover(a, b, rng):
    idx = set(rng.sample(range(6), 3))
    child, seen = [], set()
    for i in range(6):
        sp, gi = a[i] if i in idx else b[i]
        if sp in seen:
            sp = _fresh_species(rng, seen | {s for s, _ in a} | {s for s, _ in b})
            gi = _pick_group(sp, rng)
        seen.add(sp)
        child.append((sp, gi))
    return repair(child, rng)


def _sp_freq(pop):
    """種ごとの「その種を含む党」の割合"""
    c = defaultdict(int)
    for p in pop:
        for sp in {s for s, _ in p}:
            c[sp] += 1
    return {sp: n / max(1, len(pop)) for sp, n in c.items()}


def _cap_ok(counts, party, limit):
    return all(counts.get(sp, 0) + 1 <= limit for sp in {s for s, _ in party})


def _cap_fix(party, counts, limit, rng, tries=30):
    """上限を超える種を、上限に余裕のある種へ差し替える（提案と同じ判定を満たすまで）"""
    x = party
    for _ in range(tries):
        over = [i for i, (sp, _) in enumerate(x) if counts.get(sp, 0) + 1 > limit]
        if not over:
            return x
        y = list(x)
        for i in over:
            ex = {s for s, _ in y} | {sp for sp, n in counts.items() if n + 1 > limit}
            sp = _fresh_species(rng, ex)
            y[i] = (sp, _pick_group(sp, rng))
        y = repair(y, rng)
        if ok_genome(y):
            x = y
    return x


def niche(party, top_sp=None):
    g = load()
    names = [g["groups"][sp]["groups"][gi]["name"] for sp, gi in party]
    txt = " ".join(names)
    nmega = sum(1 for sp, gi in party if g["mega"][sp][gi])
    key = (nmega, "トリックルーム" in txt, "バトンタッチ" in txt,
           any(x in txt for x in ("ステルスロック", "まきびし", "どくびし")),
           sum(1 for n in names if "フルアタ" in n) >= 3)
    if NICHE_SP and top_sp:
        key += (any(sp == top_sp for sp, _ in party),)
    return key


_W = {}


def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    import pokenavi_engine as E
    _W["E"] = E
    load()


def _play(args):
    seed, pairs, pop = args
    E = _W["E"]
    rng = random.Random(seed)
    out = []
    for i, j in pairs:
        pa, pb = instantiate(pop[i], rng), instantiate(pop[j], rng)
        if SELECT == "heur":    # 本番と同じ選出（ヒューリスティック・温度0.3）
            sa = list(E.select_party_rng_probe(pb, pa, rng.randrange(1 << 30), SEASON)[0])
            sb = list(E.select_party_rng_probe(pa, pb, rng.randrange(1 << 30), SEASON)[0])
        else:
            sa, sb = rng.sample(range(6), 3), rng.sample(range(6), 3)
        r = E.mcts_3v3(pa, sa, pb, sb, rng.randrange(1 << 30), SIMS, SEASON)
        out.append((i, j, 1 if r == 1 else (-1 if r == 2 else 0)))
    return out


def _elo(elo, i, j, w, K=24):
    ea = 1.0 / (1.0 + 10 ** ((elo[j] - elo[i]) / 400))
    sa = 0.5 if w == 0 else (1.0 if w == 1 else 0.0)
    elo[i] += K * (sa - ea)
    elo[j] += K * ((1 - sa) - (1 - ea))


def _games(pool, pop, pairs, seed):
    ch = [pairs[k::WORKERS] for k in range(WORKERS)]
    res = []
    for r in pool.map(_play, [(seed + k, c, pop) for k, c in enumerate(ch)]):
        res += r
    return res


def dump(pop, elo, path, extra=None):
    g = load()
    rows = [{"elo": elo[i] if elo else None,
             "groups": [[sp, gi, g["groups"][sp]["groups"][gi]["name"]] for sp, gi in pop[i]]}
            for i in (sorted(range(len(pop)), key=lambda i: -elo[i]) if elo else range(len(pop)))]
    json.dump(dict(extra or {}, season=SEASON, parties=rows), open(path, "w"), ensure_ascii=False, indent=1)


def _load_base():
    return [[(x[0], x[1]) for x in p["groups"]] for p in json.load(open(BASE))["parties"]]


def _wr(res, idx):
    w = sum(1 for *_, x in res if x == 1)
    l = sum(1 for *_, x in res if x == -1)
    z = (w - (w + l) / 2) / math.sqrt((w + l) / 4) if w + l else 0.0
    return w, l, (w / (w + l) if w + l else 0.0), z


def evolve(pop_size, gens, games_per, out, seed=0, log=print):
    """適応度＝その世代の勝率。相手は 現集団50%・殿堂（過去世代の上位）25%・使用率どおりの土台25%。
    Elo の持ち越し（子に平均を与える）は数字が膨らむだけなので使わない。
    流行りを倒すだけの党ではなく、土台にも過去の強豪にも勝てる党が残る"""
    rng = random.Random(seed)
    base = _load_base()
    pop = [gen_party(rng) for _ in range(pop_size)]
    gen0 = [list(p) for p in pop]
    hof = []
    pool = Pool(WORKERS, initializer=_winit)
    for gnum in range(gens):
        t0 = time.time()
        opp = pop + hof + base
        nh, nb = len(hof), len(base)
        pairs = []
        for i in range(pop_size):
            for _ in range(games_per):
                r = rng.random()
                if r < 0.5 or not hof and r < 0.75:
                    j = rng.randrange(pop_size)
                    if j == i:
                        continue
                elif r < 0.75:
                    j = pop_size + rng.randrange(nh)
                else:
                    j = pop_size + nh + rng.randrange(nb)
                pairs.append((i, j))
        win, n = [0.0] * pop_size, [0] * pop_size
        for i, j, w in _games(pool, opp, pairs, seed + gnum * 1000):
            win[i] += 1.0 if w == 1 else (0.5 if w == 0 else 0.0)
            n[i] += 1
            if j < pop_size:
                win[j] += 1.0 if w == -1 else (0.5 if w == 0 else 0.0)
                n[j] += 1
        raw = [win[i] / n[i] if n[i] else 0.0 for i in range(pop_size)]
        freq = _sp_freq(pop)
        # fitness sharing: 集団に多い種ばかりの党を割り引く（順位付け・生存・親選びに使う。記録する勝率は raw）
        fit = [raw[i] - SHARE * (sum(freq[sp] for sp, _ in pop[i]) / 6.0) for i in range(pop_size)] if SHARE > 0 else raw
        order = sorted(range(pop_size), key=lambda i: -fit[i])
        top_sp = max(freq, key=freq.get) if freq else None
        niches = defaultdict(list)
        for i in order:
            niches[niche(pop[i], top_sp)].append(i)
        limit = int(pop_size * SP_CAP) if SP_CAP > 0 else pop_size + 1
        scount = defaultdict(int)
        def _take(i):
            for sp in {s for s, _ in pop[i]}:
                scount[sp] += 1
        surv = []
        for ix in niches.values():
            if raw[ix[0]] >= 0.5 and len(surv) < int(pop_size * 0.3) and _cap_ok(scount, pop[ix[0]], limit):
                surv.append(ix[0]); _take(ix[0])
        for i in order:
            if len(surv) >= int(pop_size * 0.6):
                break
            if i not in surv and _cap_ok(scount, pop[i], limit):
                surv.append(i); _take(i)
        for i in order[:2]:
            if pop[i] not in hof:
                hof.append(list(pop[i]))
        hof = hof[-64:]
        topf = sorted(freq.items(), key=lambda kv: -kv[1])[:3]
        log(f"[gen{gnum}] 勝率 最大{max(raw) * 100:.1f}% 生存平均{sum(raw[i] for i in surv) / len(surv) * 100:.1f}% "
            f"ニッチ={len(niches)} 殿堂{len(hof)} 対戦{len(pairs)} 多い種={' '.join(f'{k}{v*100:.0f}%' for k, v in topf)} "
            f"{time.time() - t0:.0f}秒", flush=True)
        if gnum == gens - 1:
            break
        newpop = [list(pop[i]) for i in surv]
        topw = {k: max(0.01, fit[i] - 0.4) for k, i in enumerate(surv)}
        while len(newpop) < pop_size:
            r = rng.random()
            if r < 0.5:
                child = mutate(newpop[PG._wchoice(topw, rng)], rng)
            elif r < 0.85:
                child = crossover(newpop[PG._wchoice(topw, rng)], newpop[PG._wchoice(topw, rng)], rng)
            else:
                child = gen_party(rng)
            if SP_CAP > 0:
                ncount = defaultdict(int)
                for p in newpop:
                    for sp in {s for s, _ in p}:
                        ncount[sp] += 1
                if not _cap_ok(ncount, child, limit):
                    child = _cap_fix(child, ncount, limit, rng)
            newpop.append(child)
        pop = newpop
    # 検証: 最終集団 vs 初期集団 / vs 使用率どおりの土台
    comb = pop + gen0 + base
    c1 = [(a, pop_size + rng.randrange(pop_size)) for a in range(pop_size) for _ in range(24)]
    c2 = [(a, 2 * pop_size + rng.randrange(len(base))) for a in range(pop_size) for _ in range(24)]
    r1 = _games(pool, comb, c1, seed + 99000)
    r2 = _games(pool, comb, c2, seed + 98000)
    pool.close()
    w1 = _wr(r1, None)
    w2 = _wr(r2, None)
    log(f"最終 vs 初期 {len(r1)}戦: 勝率{w1[2] * 100:.1f}% z={w1[3]:+.2f}", flush=True)
    log(f"最終 vs 土台 {len(r2)}戦: 勝率{w2[2] * 100:.1f}% z={w2[3]:+.2f}", flush=True)
    dump(pop, fit, out, {"winrate_vs_init": w1[2], "winrate_vs_base": w2[2],
                         "sp_cap": SP_CAP, "share": SHARE, "niche_sp": NICHE_SP, "sims": SIMS, "seed": seed})
    dump(gen0, None, out.replace(".json", "_gen0.json"))
    return w1[2]


def main():
    mode = sys.argv[1]
    if mode == "base":
        rng = random.Random(int(os.environ.get("SEED", "0")))
        n, out = int(sys.argv[2]), sys.argv[3]
        dump([gen_party(rng) for _ in range(n)], None, out)
        print(out)
    else:
        evolve(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], int(os.environ.get("SEED", "0")))


if __name__ == "__main__":
    main()
