"""numpy版 方策＋価値ネットの大規模自己対戦学習（雨コンボの創発を狙う）。

雨パ（ペリッパー始動）を含む対戦をオーバーサンプリングして「雨×水ポケが勝つ」状態を十分に
経験させ、価値関数が雨の長期的価値を自分で学習するかを厳密なプローブで検証する。

使い方: python -m simulator.train_az_np [games] [epochs] [hidden] [rain_p]
"""
import random
import sys

import numpy as np

from .simulate import get_loader
from .env import load_registered_parties, build_party, heuristic_selection
from .battle import Battle, BattleSide, BattleField
from .ai import HeuristicAI
from .features import encode_state, feature_dim
from .alphazero import legal_actions_indexed, action_to_index, ACTION_DIM
from .az_np import PVNetNP, AZNP_PATH
from .pokemon import build_from_template

RAIN_PARTY_IDS = [8, 32]


class _Rec:
    def __init__(self, inner):
        self.inner = inner; self.rec = []

    def __call__(self, my, opp, field):
        legal = [ix for _, ix in legal_actions_indexed(my, opp, field)]
        act = self.inner(my, opp, field)
        ai = action_to_index(act)
        if ai is not None and ai in legal and len(legal) > 1:
            self.rec.append((encode_state(my, opp, field), ai, legal))
        return act


def gen_samples(loader, parties, n_games, rain_p=0.5, seed=0):
    by_id = {p.party_id: p for p in parties}
    rain = [by_id[i] for i in RAIN_PARTY_IDS if i in by_id]
    rng = random.Random(seed)
    samples = []
    for _ in range(n_games):
        if rain and rng.random() < rain_p:
            pa = rng.choice(rain)
            pb = rng.choice([p for p in parties if p.party_id != pa.party_id])
            if rng.random() < 0.5:
                pa, pb = pb, pa
        else:
            pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        r1 = _Rec(HeuristicAI()); r2 = _Rec(HeuristicAI())
        w = Battle(s1, s2).run(r1, r2)
        if w == 0:
            continue
        for feat, ai, legal in r1.rec:
            samples.append((feat, ai, legal, 1.0 if w == 1 else 0.0))
        for feat, ai, legal in r2.rec:
            samples.append((feat, ai, legal, 1.0 if w == 2 else 0.0))
    return samples


def to_arrays(samples):
    X = np.array([s[0] for s in samples], float)
    A = np.array([s[1] for s in samples], int)
    Y = np.array([s[3] for s in samples], float)
    M = np.zeros((len(samples), ACTION_DIM))
    for k, s in enumerate(samples):
        for ix in s[2]:
            M[k, ix] = 1.0
    return X, A, M, Y


def rain_probe(net, loader, n=40, seed=0):
    """水主体側の価値が、雨ありで雨なしより高いか（多状態平均）。"""
    rng = random.Random(seed)
    waters = ["スターミー", "ゲッコウガ", "アシレーヌ", "ブリジュラス", "ペリッパー"]
    others = ["ガブリアス", "ドリュウズ", "ハッサム", "ルカリオ", "デカヌチャン"]

    def mk(name, mv):
        return build_from_template(loader.get_pokemon_template(name), loader, randomize=False,
                                   override_moves=[mv])
    deltas = []
    for _ in range(n):
        w3 = rng.sample(waters, 3)
        s1 = BattleSide([mk(w3[0], "なみのり"), mk(w3[1], "なみのり"), mk(w3[2], "なみのり")])
        o3 = rng.sample(others, 3)
        s2 = BattleSide([mk(o3[0], "じしん"), mk(o3[1], "じしん"), mk(o3[2], "じしん")])
        s1.field_idx, s2.field_idx = 0, 1
        f = BattleField()
        leg = [ix for _, ix in legal_actions_indexed(s1, s2, f)]
        _, v_none = net.evaluate(encode_state(s1, s2, f), leg)
        f.weather = "rain"
        _, v_rain = net.evaluate(encode_state(s1, s2, f), leg)
        deltas.append(v_rain - v_none)
    return sum(deltas) / len(deltas), sum(1 for d in deltas if d > 0) / len(deltas)


def main():
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    hidden = int(sys.argv[3]) if len(sys.argv) > 3 else 96
    rain_p = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    print(f"自己対戦 {games} 試合（雨パ率 {rain_p:.0%}）でデータ生成中...", flush=True)
    samples = gen_samples(loader, parties, games, rain_p=rain_p)
    random.Random(1).shuffle(samples)
    cut = int(len(samples) * 0.9)
    Xtr, Atr, Mtr, Ytr = to_arrays(samples[:cut])
    Xte, Ate, Mte, Yte = to_arrays(samples[cut:])
    print(f"  サンプル {len(samples)} / 特徴次元 {feature_dim()}", flush=True)
    net = PVNetNP(feature_dim(), hidden=hidden)
    print(f"学習中 (hidden={hidden}, epochs={epochs})...", flush=True)
    net.train(Xtr, Atr, Mtr, Ytr, epochs=epochs, lr=0.08, batch=256, verbose=True)
    print(f"\n held-out: 価値精度={net.value_acc(Xte,Yte):.1%}  方策top1={net.policy_acc(Xte,Ate,Mte):.1%}")
    d, pos = rain_probe(net, loader)
    print(f" 雨プローブ(水主体側): 平均Δ(雨あり-なし)={d:+.4f}  正の割合={pos:.0%}  → {'雨を学習' if d>0.01 and pos>0.7 else '不十分'}")
    net.save()
    print(f"保存: {AZNP_PATH}")


if __name__ == "__main__":
    main()
