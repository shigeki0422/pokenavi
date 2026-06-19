"""物理メガライチュウX(正しい型)で組んだ整合チームを検証＋選出運用ログ。
過去評価は使用率(=人気のメガYの特殊型)をXの石に乗せた誤ビルドだったため組み直し。
天候衝突(雨)除去。Xは物理(ワイルドボルト/じゃれつく/アイアンテール/ねこだまし)。"""
import sys, os, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
import _calib_probe as CP
from _xarticle import _winit, _job, parse_set
import _xarticle

SEASON = "M-3"

def phys_x():
    return G._spec("ライチュウ", "ライチュウナイトX", "ようき",
                   ["ワイルドボルト", "じゃれつく", "アイアンテール", "ねこだまし"], (0, 32, 0, 0, 0, 32), "せいでんき")

def build_coherent(D):
    x = phys_x()
    # 整合フィラー(天候衝突なし・対メタ): リザードンY(晴/特殊) + マンムー + ドドゲザン + アーマーガア + サザンドラ
    riza = CP.forced(D, "リザードン", "リザードナイトY", "もうか")
    mam = CP.usf(D, "マンムー"); dodo = CP.usf(D, "ドドゲザン")
    arma = CP.usf(D, "アーマーガア"); sazan = CP.usf(D, "サザンドラ")
    return [x, riza, mam, dodo, arma, sazan]

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    D = G.load(season=SEASON); rng = random.Random(3)
    team_specs = build_coherent(D)
    _xarticle.PARTNER = "リザードン"
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader()
    print("=== 物理メガライチュウX軸 整合チーム ===")
    for s in team_specs:
        st = parse_set(s); mon = build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False)
        ab = mon.ability or st["ability"] or "?"; mv = [m.name_jp for m in mon.moves if m] or st["moves"]
        h, a, b, c, d, sp = st["ev"]
        mega = ""
        if getattr(mon, "mega_data", None):
            m = mon.mega_data; mega = f"  →メガ後 {m.type1}{'/'+m.type2 if m.type2 else ''} 特性{m.ability} S{m.speed} A{m.attack} C{m.sp_attack}"
        print(f"■{st['name']} @{st['item'] or '-'} | {ab} | {st['nature'] or '?'} | EV {h}/{a}/{b}/{c}/{d}/{sp} | {' '.join(mv)}{mega}")
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    jobs = [(700 + i, team_specs, gauntlet[i]) for i in range(gn)]
    import time; t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    W = sum(r["w"] for r in res); Lo = sum(r["l"] for r in res); dec = W + Lo
    xin = sum(1 for r in res if "ライチュウ" in r["oursel"])
    pin = sum(1 for r in res if "リザードン" in r["oursel"])
    twom = sum(1 for r in res if sum(r["ismega"]) >= 2)
    print(f"\n=== 検証 vs 使用率メタ {gn}構築(各2戦・MCTS@400・{time.time()-t0:.0f}秒) ===")
    print(f"勝率 {W}/{dec}={W/dec*100:.1f}% | X選出 {xin}/{gn} | リザードン選出 {pin}/{gn} | 2メガ選出 {twom}/{gn}")
    print("\n=== 選出運用ログ（★=メガ枠・先頭=リード）===")
    for r in res:
        opp = ", ".join(f"{n}(S{int(s)})" for n, s, t in r["opp3"])
        ours = ", ".join((("★" if m else "") + n) for n, m in zip(r["oursel"], r["ismega"]))
        wl = "○" if r["w"] > r["l"] else ("●" if r["l"] > r["w"] else "△")
        print(f"  [{wl}] 相手:{opp}\n        自分:{ours}")

if __name__ == "__main__":
    main()
