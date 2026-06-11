"""方策＋価値ネット(AlphaZero型)の自己対戦学習。

自己対戦の各ターンで (状態特徴, 取った行動index, 合法index, 最終勝敗) を集め、
方策ヘッド=行動の模倣(交差エントロピー)、価値ヘッド=勝敗(BCE) を同時学習する。
学習後の方策は PUCT-MCTS の prior に、価値は葉評価に使う（完全なAlphaZero構造）。

使い方: python -m simulator.train_alphazero [games] [epochs] [hidden]
"""
import random
import sys
from pathlib import Path

from .simulate import get_loader
from .env import load_registered_parties, build_party, heuristic_selection
from .battle import Battle, BattleSide
from .ai import HeuristicAI
from .features import encode_state, feature_dim
from .alphazero import PolicyValueNet, legal_actions_indexed, action_to_index

AZ_PATH = Path(__file__).resolve().parent.parent / "az_net.json"


class _Recorder:
    def __init__(self, inner):
        self.inner = inner
        self.rec = []  # (features, action_idx, legal_idxs)

    def __call__(self, my_side, opp_side, field):
        legal = [ix for _, ix in legal_actions_indexed(my_side, opp_side, field)]
        act = self.inner(my_side, opp_side, field)
        ai = action_to_index(act)
        if ai is not None and ai in legal and len(legal) > 1:
            self.rec.append((encode_state(my_side, opp_side, field), ai, legal))
        return act


def gen_samples(loader, parties, n_games, policy_factory=None, seed=0):
    policy_factory = policy_factory or (lambda: HeuristicAI())
    rng = random.Random(seed)
    samples = []
    for _ in range(n_games):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        r1 = _Recorder(policy_factory()); r2 = _Recorder(policy_factory())
        w = Battle(s1, s2).run(r1, r2)
        if w == 0:
            continue
        for feat, ai, legal in r1.rec:
            samples.append((feat, ai, legal, 1.0 if w == 1 else 0.0))
        for feat, ai, legal in r2.rec:
            samples.append((feat, ai, legal, 1.0 if w == 2 else 0.0))
    return samples


def main():
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
    epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    hidden = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    print(f"自己対戦 {games} 試合でデータ生成中...", flush=True)
    samples = gen_samples(loader, parties, games)
    random.Random(1).shuffle(samples)
    cut = int(len(samples) * 0.85)
    train, test = samples[:cut], samples[cut:]
    print(f"  サンプル {len(samples)} (train {len(train)} / test {len(test)})", flush=True)
    net = PolicyValueNet(feature_dim(), hidden=hidden)
    print(f"方策＋価値ネット学習中 (dim={feature_dim()}, hidden={hidden}, epochs={epochs})...", flush=True)
    net.train(train, epochs=epochs, lr=0.05, verbose=True)
    print(f"\n held-out: 価値精度={net.value_acc(test):.1%}  方策top1一致={net.policy_top1_acc(test):.1%}")
    net.save(AZ_PATH)
    print(f"保存: {AZ_PATH}")


if __name__ == "__main__":
    main()
