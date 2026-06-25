"""
デバッグ用バトルビューア
使い方:
  python3 debug_battle.py                        # 対話形式でパーティ入力
  python3 debug_battle.py --p1 "ガブリアス,カイリュー,ゲンガー,ギャラドス,ハッサム,ギルガルド" \
                          --p2 "リザードン,アーマーガア,カバルドン,ルカリオ,ミミロップ,ウルガモス"
  python3 debug_battle.py ... --trials 100       # N回シミュレーション集計
  python3 debug_battle.py ... --html out.html    # HTML出力
"""
import sys, os, argparse, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulator.data import DataLoader
from simulator.pokemon import build_from_template, parse_pokemon_spec, build_from_spec
from simulator.battle import Battle, BattleSide, BattleField
from simulator.ai import HeuristicAI, select_party
from simulator.simulate import run_simulation

# ANSI colors
R  = "\033[91m"
G  = "\033[92m"
Y  = "\033[93m"
B  = "\033[94m"
M  = "\033[95m"
C  = "\033[96m"
W  = "\033[97m"
DIM = "\033[2m"
RESET = "\033[0m"
BOLD = "\033[1m"


def hp_bar(hp, max_hp, width=20):
    ratio = hp / max_hp if max_hp > 0 else 0
    filled = int(ratio * width)
    bar = "█" * filled + "░" * (width - filled)
    if ratio > 0.5:
        color = G
    elif ratio > 0.25:
        color = Y
    else:
        color = R
    return f"{color}{bar}{RESET} {hp}/{max_hp}"


def status_str(poke):
    s = poke.status or ""
    STATUS_COLORS = {
        "burn": f"{R}やけど{RESET}", "paralysis": f"{Y}まひ{RESET}",
        "sleep": f"{B}ねむり{RESET}", "freeze": f"{C}こおり{RESET}",
        "poison": f"{M}どく{RESET}", "badpoison": f"{M}どくどく{RESET}",
    }
    return STATUS_COLORS.get(s, "")


def print_state(side1, side2, turn):
    p1, p2 = side1.active, side2.active
    print(f"\n{BOLD}{'─'*60}{RESET}")
    print(f"{BOLD}Turn {turn}{RESET}")
    print(f"  {B}P1{RESET} {p1.name:<12} {hp_bar(p1.hp, p1.max_hp)} {status_str(p1)}")
    bench1 = [p for p in side1.party if p is not p1]
    bench_str1 = "  ".join(
        f"{DIM}{p.name}({p.hp}/{p.max_hp}){RESET}" if p.is_alive
        else f"{DIM}{p.name}[倒]{RESET}"
        for p in bench1
    )
    if bench1:
        print(f"    控: {bench_str1}")
    print(f"  {R}P2{RESET} {p2.name:<12} {hp_bar(p2.hp, p2.max_hp)} {status_str(p2)}")
    bench2 = [p for p in side2.party if p is not p2]
    bench_str2 = "  ".join(
        f"{DIM}{p.name}({p.hp}/{p.max_hp}){RESET}" if p.is_alive
        else f"{DIM}{p.name}[倒]{RESET}"
        for p in bench2
    )
    if bench2:
        print(f"    控: {bench_str2}")


def colorize_log(line: str) -> str:
    if "ダメ" in line:
        return f"  {W}{line}{RESET}"
    if "こうかはばつぐん" in line:
        return f"  {Y}⚡ {line}{RESET}"
    if "こうかはいまひとつ" in line:
        return f"  {DIM}↓ {line}{RESET}"
    if "倒れ" in line or "倒" in line:
        return f"  {R}💀 {line}{RESET}"
    if "メガ進化" in line:
        return f"  {M}★ {line}{RESET}"
    if "まひ" in line or "やけど" in line or "ねむり" in line or "どく" in line:
        return f"  {M}~ {line}{RESET}"
    if "回復" in line or "タスキ" in line or "がんじょう" in line:
        return f"  {G}♥ {line}{RESET}"
    return f"  {line}"


def build_team(loader, specs, season):
    """スペック文字列リストから BattlePokemon リストを生成"""
    team = []
    for s in specs:
        spec = parse_pokemon_spec(s)
        try:
            poke = build_from_spec(spec, loader, season=season, randomize=True)
        except ValueError as e:
            print(f"{R}ERROR: {e}{RESET}")
            sys.exit(1)
        team.append(poke)
    return team


def run_single_battle(loader, p1_specs, p2_specs, step=False, season="M-2"):
    """1試合をターン毎に表示"""
    party1_6 = build_team(loader, p1_specs, season)
    party2_6 = build_team(loader, p2_specs, season)

    dummy_field = BattleField()
    selected1 = select_party(party1_6, party2_6, loader)
    selected2 = select_party(party2_6, party1_6, loader)

    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{B}P1選出{RESET}: {', '.join(p.name for p in selected1)}")
    print(f"{R}P2選出{RESET}: {', '.join(p.name for p in selected2)}")

    side1 = BattleSide(selected1)
    side2 = BattleSide(selected2)
    field = BattleField()
    ai = HeuristicAI(alpha=0.7)

    # Battleクラスを使い、ターン毎にログを出力するカスタムループ
    from simulator.battle import _entry_effects, _speed_order, MAX_TURNS

    _entry_effects(side1.active, 0, field, side2.active, [])
    _entry_effects(side2.active, 1, field, side1.active, [])

    battle = Battle(side1, side2, field)

    prev_log_len = 0
    turn = 0
    result = 0

    print_state(side1, side2, 0)

    while turn < MAX_TURNS:
        turn += 1
        if not side1.has_alive():
            result = 2; break
        if not side2.has_alive():
            result = 1; break

        action1 = ai(side1, side2, field)
        action2 = ai(side2, side1, field)
        # 行動を選んだ本体を記録（先攻で倒され交代した場合、後攻の行動権を失わせる）
        chooser1, chooser2 = side1.active, side2.active

        # メガ進化（行動前）
        for _side, _action in [(side1, action1), (side2, action2)]:
            poke = _side.active
            if _action.do_mega and not poke.mega_evolved:
                poke.do_mega_evolve()
                battle.logs.append(
                    f"{poke.name} はメガ進化した！ → {poke.type1}/{poke.type2 or '-'} "
                    f"BST={poke.attack+poke.defense+poke.sp_attack+poke.sp_defense+poke.speed+poke.max_hp}"
                )

        # 先攻/後攻
        p1_first = _speed_order(side1, action1, side2, action2, field)

        first_side, first_action, first_opp = (
            (side1, action1, side2) if p1_first else (side2, action2, side1)
        )
        second_side, second_action, second_opp = (
            (side2, action2, side1) if p1_first else (side1, action1, side2)
        )
        second_chooser = chooser1 if second_side is side1 else chooser2

        battle._do_action(first_side, first_opp, first_action, ai)
        new_logs = battle.logs[prev_log_len:]
        prev_log_len = len(battle.logs)

        if not first_opp.has_alive():
            result = 1 if first_side is side1 else 2
            _print_turn(turn, side1, side2, new_logs)
            break

        if second_side.active is second_chooser and not second_side.active.flinched:
            battle._do_action(second_side, second_opp, second_action, ai)
        new_logs2 = battle.logs[prev_log_len:]
        prev_log_len = len(battle.logs)

        if not second_opp.has_alive():
            result = 1 if second_side is side1 else 2

        battle._end_of_turn()
        new_logs_eot = battle.logs[prev_log_len:]
        prev_log_len = len(battle.logs)

        all_new = new_logs + new_logs2 + new_logs_eot
        _print_turn(turn, side1, side2, all_new)

        if result != 0:
            break

        if step:
            try:
                input(f"  {DIM}[Enter で次のターンへ / Ctrl+C で終了]{RESET}")
            except KeyboardInterrupt:
                print("\n中断")
                return

    if not side1.has_alive():
        result = 2
    elif not side2.has_alive():
        result = 1

    winner_str = (f"{B}P1({selected1[0].name}側)勝利{RESET}" if result == 1
                  else f"{R}P2({selected2[0].name}側)勝利{RESET}" if result == 2
                  else f"{Y}引き分け{RESET}")
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"  結果: {winner_str}  ({turn}ターン)")
    print()
    return result


def _print_turn(turn, side1, side2, logs):
    print_state(side1, side2, turn)
    if logs:
        print(f"  {DIM}--- ターン{turn}のログ ---{RESET}")
        for line in logs:
            print(colorize_log(line))


def run_multi_trials(loader, p1_specs, p2_specs, trials, season="M-2"):
    """N回シミュレーション集計"""
    from simulator.simulate import run_simulation_specs
    print(f"\n{BOLD}シミュレーション: {trials}試行{RESET}")
    start = time.time()
    result = run_simulation_specs(p1_specs, p2_specs, trials=trials, season=season)
    elapsed = time.time() - start
    draws = result.trials - result.wins1 - result.wins2

    print(f"\n  P1 勝率: {B}{result.win_rate1:.1%}{RESET}  ({result.wins1}勝)")
    print(f"  P2 勝率: {R}{result.win_rate2:.1%}{RESET}  ({result.wins2}勝)")
    print(f"  引き分け: {draws/result.trials:.1%}  ({draws}回)")
    print(f"  {DIM}{elapsed:.1f}秒 / {result.trials/elapsed:.0f}試行/秒{RESET}")
    print()


def interactive_input(loader, season="M-2"):
    """対話形式でパーティ入力"""
    print(f"\n{BOLD}ポケモンチャンピオンズ バトルシミュレータ (デバッグモード){RESET}")
    print(f"{DIM}書式: ポケモン名[@持ち物][:性格][:技1|技2|技3|技4][:H/A/B/C/D/S]{RESET}")
    print(f"{DIM}例(フル): ガブリアス@ガブリアスナイト:いじっぱり:じしん|げきりん|ステルスロック|がんせきふうじ:2/32/0/0/0/32{RESET}")
    print(f"{DIM}例(名前のみ): ガブリアス,カイリュー,ゲンガー,ギャラドス,ハッサム,ギルガルド{RESET}\n")

    def get_party(player):
        while True:
            line = input(f"{player}のパーティ(6匹カンマ区切り): ").strip()
            specs_raw = [s.strip() for s in line.split(",") if s.strip()]
            if len(specs_raw) < 1:
                print("  1匹以上入力してください")
                continue
            missing = []
            for s in specs_raw:
                name = parse_pokemon_spec(s)["name"]
                if loader.get_pokemon_template(name, season) is None:
                    missing.append(name)
            if missing:
                print(f"  見つかりません: {', '.join(missing)}")
                continue
            return specs_raw

    p1 = get_party("P1")
    p2 = get_party("P2")
    return p1, p2


def main():
    parser = argparse.ArgumentParser(description="デバッグ用バトルビューア")
    parser.add_argument("--p1", help="P1パーティ(カンマ区切り6匹)")
    parser.add_argument("--p2", help="P2パーティ(カンマ区切り6匹)")
    parser.add_argument("--trials", type=int, default=1,
                        help="シミュレーション回数(1=1試合詳細表示, N>1=集計)")
    parser.add_argument("--step", action="store_true",
                        help="ターン毎に一時停止(trials=1時のみ有効)")
    parser.add_argument("--season", default="M-2", help="シーズン(デフォルト: M-2)")
    parser.add_argument("--no-color", action="store_true", help="カラー出力を無効化")
    args = parser.parse_args()

    if args.no_color:
        # ANSIコードを空文字に
        for var in ["R","G","Y","B","M","C","W","DIM","RESET","BOLD"]:
            globals()[var] = ""

    loader = DataLoader()

    if args.p1 and args.p2:
        p1_names = [n.strip() for n in args.p1.split(",")]
        p2_names = [n.strip() for n in args.p2.split(",")]
    else:
        p1_names, p2_names = interactive_input(loader, args.season)

    if args.trials == 1:
        run_single_battle(loader, p1_names, p2_names, step=args.step, season=args.season)
    else:
        run_multi_trials(loader, p1_names, p2_names, args.trials, season=args.season)


if __name__ == "__main__":
    main()
