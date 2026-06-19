"""X記事用データ出力: 検証済み X+リザードン 構築の全型(特性/性格/EV/持ち物/技)と、
メタ各構築に対する選出運用ログ(どの相手にどの3体を選び・どちらをメガ枠にするか)を実測で出す。
選出はMCTS探索(max_mega=2=2メガ選出許容)、プレイMCTS@400。記事の考察素材。
"""
import sys, os, random, json, sqlite3
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
import _calib_probe as CP
from _xteam_search import _dexmap
from _xmega_search import _mega_species, build_team

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
SEL_SIMS = int(os.environ.get("SEL_SIMS", "100"))
PARTNER = os.environ.get("PARTNER", "リザードン")
_W = {}

def article_team(D, dexmap):
    megas = _mega_species(dexmap)
    order = [p for p, _ in D["usage"] if p in megas]
    idx = order.index(PARTNER)
    return build_team(PARTNER, megas[PARTNER], D, dexmap, random.Random(600 + idx))

def parse_set(spec):
    left, _, right = spec.partition(":")
    name, _, item = left.partition("@")
    f = right.split(":")
    nature = f[0] if len(f) > 0 else ""
    moves = f[1].split("|") if len(f) > 1 and f[1] else []
    ev = f[2].split("/") if len(f) > 2 and f[2] else []
    ability = f[3] if len(f) > 3 else ""
    ev = [int(x) for x in ev] if ev else [0] * 6
    return {"name": name, "item": item, "ability": ability, "nature": nature, "moves": moves, "ev": ev}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    net = PVNetNP.load()
    _W["play"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["sel"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SEL_SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    seed, team_specs, opp_specs = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_mcts
    L = _W["L"]; play = _W["play"]; sel_ai = _W["sel"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    T = team(team_specs); O = team(opp_specs)
    sa = select_mcts(T, O, L, sel_ai, n=3, rng=rng, topk=8, max_mega=2)
    oursel = [p.name for p in sa]
    ismega = [getattr(p, "mega_data", None) is not None for p in sa]
    osel = select_party(O, T, L, n=3, temperature=0.0, rng=rng)
    opp3 = [(p.name, p.speed, p.type1 + ("/" + p.type2 if p.type2 else "")) for p in osel]
    w = l = 0
    for k in range(2):
        T2 = team(team_specs); O2 = team(opp_specs)
        sa2 = select_mcts(T2, O2, L, sel_ai, n=3, rng=random.Random(seed + 100 + k), topk=8, max_mega=2)
        sb2 = select_party(O2, T2, L, n=3, temperature=0.0, rng=rng)
        ton1 = (k == 0)
        s1 = BattleSide(sa2 if ton1 else sb2); s2 = BattleSide(sb2 if ton1 else sa2)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        try: r = Battle(s1, s2).run(play, play)
        except Exception: r = 0
        if r == 0: continue
        if (r == 1) == ton1: w += 1
        else: l += 1
    return {"opp3": opp3, "oursel": oursel, "ismega": ismega, "w": w, "l": l}

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    D = G.load(season=SEASON); dexmap = _dexmap(); rng = random.Random(3)
    team_specs = article_team(D, dexmap)
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader()
    print(f"=== 記事用構築: メガライチュウX + {PARTNER}（2メガ選出前提）===")
    for s in team_specs:
        st = parse_set(s); h, a, b, c, d, sp = st["ev"]
        mon = build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False)
        ability = mon.ability or st["ability"] or "?"
        moves = [mv.name_jp for mv in mon.moves if mv] or st["moves"]
        mega = ""
        if getattr(mon, "mega_data", None) is not None:
            md = mon.mega_data
            mega = f"  → メガ後: {md.type1}{'/'+md.type2 if md.type2 else ''} 特性{md.ability} (H{md.hp}/A{md.attack}/B{md.defense}/C{md.sp_attack}/D{md.sp_defense}/S{md.speed})"
        print(f"\n■ {st['name']}  @{st['item'] or '-'}")
        print(f"  特性: {ability} / 性格: {st['nature'] or '?'}")
        print(f"  EV(H/A/B/C/D/S・最大32): {h}/{a}/{b}/{c}/{d}/{sp}")
        print(f"  技: {' / '.join(moves) if moves else '?'}")
        if mega: print(mega)
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    jobs = [(700 + i, team_specs, gauntlet[i]) for i in range(gn)]
    import time; t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    W = sum(r["w"] for r in res); Lo = sum(r["l"] for r in res)
    xin = sum(1 for r in res if "ライチュウ" in r["oursel"])
    pin = sum(1 for r in res if PARTNER in r["oursel"])
    twom = sum(1 for r in res if sum(r["ismega"]) >= 2)
    print(f"\n=== 検証: vs 使用率メタ {gn}構築 (各2戦・MCTS@{SIMS}・{time.time()-t0:.0f}秒) ===")
    dec = W + Lo
    print(f"勝率 {W}/{dec} = {W/dec*100:.1f}%  | X選出率 {xin}/{gn} | {PARTNER}選出率 {pin}/{gn} | 2メガ選出 {twom}/{gn}")
    print(f"\n=== 選出運用ログ（相手選出3体 → 自分の選出3体／先頭=リード, ★=メガ枠）===")
    for r in res:
        opp = ", ".join(f"{n}(S{int(s)})" for n, s, t in r["opp3"])
        ours = ", ".join((("★" if m else "") + n) for n, m in zip(r["oursel"], r["ismega"]))
        wl = "○" if r["w"] > r["l"] else ("●" if r["l"] > r["w"] else "△")
        print(f"  [{wl}] 相手: {opp}")
        print(f"        自分: {ours}")
    json.dump({"partner": PARTNER, "team": team_specs}, open("/tmp/xarticle_team.json", "w"), ensure_ascii=False)

if __name__ == "__main__":
    main()
