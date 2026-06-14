"""
モンテカルロシミュレーション本体
6匹パーティ2つを受け取り、N回試行して勝率を返す
"""
from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import List, Optional, Callable
from .data import DataLoader
from .pokemon import BattlePokemon, build_from_template, parse_pokemon_spec, build_from_spec
from .battle import Battle, BattleSide, BattleField
from .ai import HeuristicAI, select_party

DEFAULT_LOADER: Optional[DataLoader] = None


def get_loader() -> DataLoader:
    global DEFAULT_LOADER
    if DEFAULT_LOADER is None:
        DEFAULT_LOADER = DataLoader()
    return DEFAULT_LOADER


@dataclass
class SimResult:
    party1_names: List[str]
    party2_names: List[str]
    trials: int
    wins1: int
    wins2: int
    draws: int
    p2_poke_wins: dict = field(default_factory=dict)
    p2_poke_losses: dict = field(default_factory=dict)

    @property
    def win_rate1(self) -> float:
        return self.wins1 / self.trials

    @property
    def win_rate2(self) -> float:
        return self.wins2 / self.trials

    def __str__(self):
        p1 = ", ".join(self.party1_names)
        p2 = ", ".join(self.party2_names)
        return (
            f"【パーティ1】{p1}\n"
            f"【パーティ2】{p2}\n"
            f"試行: {self.trials}回\n"
            f"  P1勝利: {self.wins1}回 ({self.win_rate1:.1%})\n"
            f"  P2勝利: {self.wins2}回 ({self.win_rate2:.1%})\n"
            f"  引き分け: {self.draws}回"
        )


def run_simulation(
    party1_names: List[str],
    party2_names: List[str],
    trials: int = 1000,
    ai_alpha: float = 0.7,
    season: str = "M-2",
    loader: Optional[DataLoader] = None,
    verbose: bool = False,
) -> SimResult:
    """
    6匹×2パーティでN試合シミュレーション。

    Args:
        party1_names: パーティ1のポケモン名リスト（最大6匹）
        party2_names: パーティ2のポケモン名リスト（最大6匹）
        trials: シミュレーション回数
        ai_alpha: AI戦略パラメータ (0=ランダム, 1=最大ダメ重視)
        season: データ取得シーズン
    """
    if loader is None:
        loader = get_loader()

    # テンプレート取得
    tpl1 = []
    for name in party1_names:
        t = loader.get_pokemon_template(name, season)
        if t is None:
            raise ValueError(f"ポケモン '{name}' のデータが見つかりません")
        tpl1.append(t)

    tpl2 = []
    for name in party2_names:
        t = loader.get_pokemon_template(name, season)
        if t is None:
            raise ValueError(f"ポケモン '{name}' のデータが見つかりません")
        tpl2.append(t)

    ai = HeuristicAI(alpha=ai_alpha)
    wins1 = wins2 = draws = 0

    for i in range(trials):
        # 毎試合: 型を確率的にサンプリング（randomize=True）
        party1 = [build_from_template(t, loader, randomize=True) for t in tpl1]
        party2 = [build_from_template(t, loader, randomize=True) for t in tpl2]

        # 選出（6匹→3匹）
        selected1 = select_party(party1, party2, loader, n=min(3, len(party1)))
        selected2 = select_party(party2, party1, loader, n=min(3, len(party2)))

        side1 = BattleSide(selected1)
        side2 = BattleSide(selected2)

        battle = Battle(side1, side2)
        result = battle.run(ai, ai, verbose=verbose)

        if result == 1:
            wins1 += 1
        elif result == 2:
            wins2 += 1
        else:
            draws += 1

        if verbose and (i + 1) % 100 == 0:
            print(f"  {i+1}/{trials}: P1 {wins1/(i+1):.1%} | P2 {wins2/(i+1):.1%}")

    return SimResult(
        party1_names=party1_names,
        party2_names=party2_names,
        trials=trials,
        wins1=wins1,
        wins2=wins2,
        draws=draws,
    )


def run_simulation_specs(
    party1_specs: List[str],
    party2_specs: List[str],
    trials: int = 1000,
    ai_alpha: float = 0.7,
    season: str = "M-2",
    loader: Optional[DataLoader] = None,
    make_ai=None,
    sel_temp: float = 0.0,
) -> SimResult:
    """
    スペック文字列（ポケモン名[@持ち物][:性格][:技][:EV]）のリストでシミュレーション。
    名前だけ指定すれば run_simulation と同等。
    make_ai: 対戦AIを返す callable（未指定でHeuristicAI）。学習AI(NetGreedyAI等)を渡すと
             表示勝率が「中級志向の学習AI」基準になる（リリース用）。
    sel_temp: 選出の温度。>0で確定選出でなくスコアのsoftmaxから確率的に3体選ぶ（多様性付与）。
    """
    if loader is None:
        loader = get_loader()

    specs1 = [parse_pokemon_spec(s) for s in party1_specs]
    specs2 = [parse_pokemon_spec(s) for s in party2_specs]

    ai = make_ai() if make_ai else HeuristicAI(alpha=ai_alpha)
    wins1 = wins2 = draws = 0
    p2_poke_wins: dict = {}
    p2_poke_losses: dict = {}

    for _ in range(trials):
        party1 = [build_from_spec(sp, loader, season=season, randomize=True) for sp in specs1]
        party2 = [build_from_spec(sp, loader, season=season, randomize=True) for sp in specs2]

        selected1 = select_party(party1, party2, loader, n=min(3, len(party1)), temperature=sel_temp)
        selected2 = select_party(party2, party1, loader, n=min(3, len(party2)), temperature=sel_temp)

        result = Battle(BattleSide(selected1), BattleSide(selected2)).run(ai, ai)

        if result == 1:
            wins1 += 1
            for p in selected2:
                p2_poke_wins[p.name] = p2_poke_wins.get(p.name, 0) + 1
        elif result == 2:
            wins2 += 1
            for p in selected2:
                p2_poke_losses[p.name] = p2_poke_losses.get(p.name, 0) + 1
        else:
            draws += 1

    return SimResult(
        party1_names=[s["name"] for s in specs1],
        party2_names=[s["name"] for s in specs2],
        trials=trials, wins1=wins1, wins2=wins2, draws=draws,
        p2_poke_wins=p2_poke_wins, p2_poke_losses=p2_poke_losses,
    )


if __name__ == "__main__":
    party1 = ["ガブリアス", "カイリュー", "ゲンガー", "カビゴン", "ハッサム", "バンギラス"]
    party2 = ["リザードン", "フシギバナ", "カメックス", "ピカチュウ", "ゲンガー", "カイリュー"]

    print("シミュレーション開始...")
    result = run_simulation(party1, party2, trials=500, verbose=True)
    print()
    print(result)
