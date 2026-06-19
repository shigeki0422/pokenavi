"""機能2 商品プロトタイプ: 確定提案構築の全型＋選出運用ガイド（どの相手にどの3体）＋メタ勝率。
func2_teams_{SEASON}.json の指定構築について、型ダンプ＋ヒューリスティック選出(本番既定)の運用ログを実測出力。
"""
import sys, os, random, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
from _xarticle import parse_set

SEASON = os.environ.get("COEVO_SEASON", "M-3")
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    _W["ai"] = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    seed, team_specs, opp_specs = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; ai = _W["ai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    T = team(team_specs); O = team(opp_specs)
    sa = select_party(T, O, L, n=3, temperature=0.0, rng=rng)
    osel = select_party(O, T, L, n=3, temperature=0.0, rng=rng)
    oursel = [p.name for p in sa]; ismega = [getattr(p, "mega_data", None) is not None for p in sa]
    opp3 = [(p.name, int(p.speed)) for p in osel]
    w = l = 0
    for k in range(2):
        T2 = team(team_specs); O2 = team(opp_specs)
        sa2 = select_party(T2, O2, L, n=3, temperature=0.0, rng=rng)
        sb2 = select_party(O2, T2, L, n=3, temperature=0.0, rng=rng)
        ton1 = (k == 0)
        s1 = BattleSide(sa2 if ton1 else sb2); s2 = BattleSide(sb2 if ton1 else sa2)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        try: r = Battle(s1, s2).run(ai, ai)
        except Exception: r = 0
        if r == 0: pass
        elif (r == 1) == ton1: w += 1
        else: l += 1
    return {"opp3": opp3, "oursel": oursel, "ismega": ismega, "w": w, "l": l}

def _team_block(idx, team, gn, out):
    team_specs = team["specs"]; winrate = team["winrate"]
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader(); D = G.load(season=SEASON); rng = random.Random(11 + idx)
    out.append(f"## 提案構築 #{idx}（pipeline勝率{winrate*100:.1f}%）\n")
    out.append("| ポケモン | 持ち物 | 特性 | 性格 | EV(H/A/B/C/D/S) | 技 |")
    out.append("|---|---|---|---|---|---|")
    for s in team_specs:
        st = parse_set(s); mon = build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False)
        ab = mon.ability or st["ability"] or "?"; mv = [m.name_jp for m in mon.moves if m] or st["moves"]
        h, a, b, c, dd, sp = st["ev"]; nm = st["name"]
        if getattr(mon, "mega_data", None):
            m = mon.mega_data; nm += f"（→メガ{m.type1}{'/'+m.type2 if m.type2 else ''}・{m.ability}）"
        out.append(f"| {nm} | {st['item'] or '-'} | {ab} | {st['nature'] or '?'} | {h}/{a}/{b}/{c}/{dd}/{sp} | {' '.join(mv)} |")
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    jobs = [(800 + idx * 100 + i, team_specs, gauntlet[i]) for i in range(gn)]
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    W = sum(r["w"] for r in res); Lo = sum(r["l"] for r in res); dec = W + Lo
    if team.get("confirmed_wr") is not None:
        out.append(f"\n**メタ勝率 {team['confirmed_wr']*100:.1f}%（独立大標本確認・z={team['confirmed_z']:+.2f} p={team['confirmed_p']:.3f}／単一ガントレットでは±10〜20pt変動）**\n")
    else:
        out.append(f"\n**メタ勝率 {W/dec*100:.1f}%（ガントレット{gn}・n={dec}・参考値）**\n")
    out.append("選出運用ガイド（相手の選出 → 推奨3体／★=メガ進化させる枠）:\n")
    for r in res:
        opp = ", ".join(f"{n}(S{s})" for n, s in r["opp3"])
        ours = ", ".join((("★" if m else "") + n) for n, m in zip(r["oursel"], r["ismega"]))
        wl = "○" if r["w"] > r["l"] else ("●" if r["l"] > r["w"] else "△")
        out.append(f"- [{wl}] 相手: {opp} → **{ours}**")
    out.append("")

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "auto"
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    d = json.load(open(f"func2_teams_{SEASON}.json", encoding="utf-8"))
    if arg == "auto":   # 確定検証でp<0.05かつ勝率>0.5の構築だけ採用
        idxs = [i for i, t in enumerate(d["teams"])
                if t.get("confirmed_wr", 0) > 0.5 and t.get("confirmed_p", 1) < 0.05]
        idxs.sort(key=lambda i: -d["teams"][i]["confirmed_wr"])
    else:
        idxs = [int(x) for x in arg.split(",")]
    import time; t0 = time.time()
    out = [f"# 機能2 提案パック（{SEASON}・MCTS@{SIMS}検証）\n",
           "AI(共進化生成→MCTS実メタ勝率ランク→独立大標本確認)が選んだ、使用率メタに有意勝ち越しの構築。\n"]
    for idx in idxs:
        _team_block(idx, d["teams"][idx], gn, out)
    text = "\n".join(out)
    open(f"func2_proposals_{SEASON}.md", "w", encoding="utf-8").write(text)
    print(text)
    print(f"\n（{time.time()-t0:.0f}秒・func2_proposals_{SEASON}.md に保存）")

if __name__ == "__main__":
    main()
