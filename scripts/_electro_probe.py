"""メガライチュウX軸パのブリジュラスが エレクトロビーム を実戦でどう使っているか計測。
雨なし=常に溜め必要。AIの選択技・天候・溜め→発射の成否を対戦ログから集計し、活きる場面を可視化。
"""
import sys, os, random, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
import _pop_gen as G

SEASON = "M-3"

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from simulator.damage import effective_weather
    from train_az2 import _net_ai
    L = get_loader(); D = G.load(season=SEASON)
    play = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=250, mcts_select="regret", mcts_fast=True)
    party = next(p for p in json.load(open("func1_pool_M-3.json", encoding="utf-8"))["parties"]
                 if p.get("theme") == "メガ軸:ライチュウ(X)")
    specs = party["specs"]
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]

    log = {"sel": {}, "eb_charge": 0, "eb_instant_rain": 0, "eb_fired": 0, "eb_wasted": 0, "brij_selected": 0}
    class LogAI:
        def __init__(self, ai, side_label): self.ai = ai; self.side = side_label; self.pending_eb = {}
        def __call__(self, my, opp, field):
            act = self.ai(my, opp, field)
            mon = my.active
            if mon and getattr(mon, "name", "") == "ブリジュラス" and act.type == "move" and act.move:
                mv = act.move.name_jp
                log["sel"][mv] = log["sel"].get(mv, 0) + 1
                log["brij_selected"] += 1
                if mv == "エレクトロビーム":
                    w = effective_weather(field, mon)
                    charging = getattr(mon, "charged", False) or getattr(mon, "_charging_move", None)
                    if w == "rain":
                        log["eb_instant_rain"] += 1
                    elif not charging:
                        log["eb_charge"] += 1            # 溜め開始(雨でない)
                    else:
                        log["eb_fired"] += 1             # 溜め後の発射
            return act
    rng = random.Random(7)
    gaunt = [G.gen_party(D, random.Random(5000 + k)) for k in range(n)]
    for i in range(n):
        try:
            T = team(specs); O = team(gaunt[i])
            sa = ([T[0]] + select_party(T[1:], O, L, n=2, temperature=0.3, rng=rng))[:3]
            sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
            if not any(getattr(p, "name", "") == "ブリジュラス" for p in sa):
                # ブリジュラスが選出されない場合は次へ(計測対象外)
                pass
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            Battle(s1, s2).run(LogAI(play, "A"), play)
        except Exception as e:
            pass
    print(f"=== メガライチュウX軸パ ブリジュラスの技選択 ({n}戦) ===")
    print("選択技内訳:", dict(sorted(log["sel"].items(), key=lambda x: -x[1])))
    print(f"ブリジュラス総行動: {log['brij_selected']}")
    print(f"エレクトロビーム: 溜め開始(雨なし) {log['eb_charge']} / 雨で即時 {log['eb_instant_rain']} / 溜め後発射 {log['eb_fired']}")
    elec = log["sel"].get("エレクトロビーム", 0); jav = log["sel"].get("10まんボルト", 0)
    print(f"でんき技比較: エレクトロビーム {elec} vs 10まんボルト {jav}")

if __name__ == "__main__":
    main()
