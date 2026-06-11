"""学習価値関数の自己対戦学習（AlphaZero的な value 学習の第一段）。

自己対戦で各ターンの状態特徴と最終勝敗を集め、価値ネット（小型MLP）を学習する。
コンボは一切手書きせず、状態→勝率の写像を学習するため、天候×タイプ等の長期戦略の価値が
自然に重みに現れる（未知のシナジーも原理的に学習対象）。

使い方: python -m simulator.train_value [games] [epochs] [hidden]
"""
import random
import sys

from .simulate import get_loader
from .env import load_registered_parties, build_party, heuristic_selection
from .battle import Battle, BattleSide
from .ai import HeuristicAI
from .features import encode_state, feature_dim
from .value_net import ValueNet, WEIGHTS_PATH


class _Recorder:
    """各ターン、自分視点の状態特徴を記録する AI ラッパー。"""
    def __init__(self, inner):
        self.inner = inner
        self.states = []

    def __call__(self, my_side, opp_side, field):
        self.states.append(encode_state(my_side, opp_side, field))
        return self.inner(my_side, opp_side, field)


def gen_selfplay_samples(loader, parties, n_games: int, policy_factory=None, seed: int = 0):
    policy_factory = policy_factory or (lambda: HeuristicAI())
    rng = random.Random(seed)
    samples = []
    for g in range(n_games):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        r1 = _Recorder(policy_factory()); r2 = _Recorder(policy_factory())
        w = Battle(s1, s2).run(r1, r2)
        if w == 0:
            continue  # 引き分けは除外
        for st in r1.states:
            samples.append((st, 1.0 if w == 1 else 0.0))
        for st in r2.states:
            samples.append((st, 1.0 if w == 2 else 0.0))
    return samples


def rain_probe(net, loader):
    """学習した価値が「雨＋水ポケ」を雨なしより高く評価するか（雨シナジーの学習確認）。"""
    from .battle import BattleField
    # 水主体の側 vs 中立。スターミーを先頭に、控えにブリジュラス/ペリッパー
    def mk(name):
        from .pokemon import build_from_template
        return build_from_template(loader.get_pokemon_template(name), loader, randomize=False,
                                   override_moves=["なみのり"] if name != "ガブリアス" else ["じしん"])
    s1 = BattleSide([mk("スターミー"), mk("ブリジュラス"), mk("ペリッパー")])
    s2 = BattleSide([mk("ガブリアス"), mk("ガブリアス"), mk("ガブリアス")])
    s1.field_idx, s2.field_idx = 0, 1
    f = BattleField()
    v_none = net.predict(encode_state(s1, s2, f))
    f.weather = "rain"
    v_rain = net.predict(encode_state(s1, s2, f))
    return v_none, v_rain


def _party_with(loader, name):
    for p in load_registered_parties(loader, complete_only=True):
        if name in [s["name"] for s in p.specs]:
            return p
    return None


def selfplay_value_iteration(loader, parties, iters: int = 2, games_per: int = 400,
                             hidden: int = 24, epochs: int = 12, seed: int = 0):
    """AlphaZero的な反復: 価値誘導の自己対戦でデータ生成→価値再学習 を繰り返す。

    各反復で、現在の価値関数で導いた SearchAI（浅い探索＋価値葉評価）が自己対戦し、
    より良い手・探索でコンボを試す→その勝敗で価値を更新。反復ごとに方策と価値が共に向上する。
    （pure Python・価値誘導の自己対戦は低速なため既定は小規模。本格収束には多反復＋計算資源が要る）
    """
    from .search_ai import SearchAI
    from .value_net import make_value_fn
    net = ValueNet(feature_dim(), hidden=hidden, seed=seed)
    for it in range(iters):
        vf = make_value_fn(net)
        fac = (lambda: SearchAI(loader, rollouts=6, depth=8, seed=seed, value_fn=vf))
        print(f"[反復 {it+1}/{iters}] 価値誘導の自己対戦でデータ生成...", flush=True)
        samples = gen_selfplay_samples(loader, parties, games_per, policy_factory=fac, seed=seed + it)
        net = ValueNet(feature_dim(), hidden=hidden, seed=seed)  # 毎回フィッティングし直し
        net.train(samples, epochs=epochs, lr=0.05)
        print(f"  サンプル {len(samples)} / logloss {net.logloss(samples):.4f}", flush=True)
    net.save()
    return net


def main():
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 14
    hidden = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    print(f"自己対戦 {games} 試合でデータ生成中...", flush=True)
    samples = gen_selfplay_samples(loader, parties, games)
    random.Random(1).shuffle(samples)
    cut = int(len(samples) * 0.85)
    train, test = samples[:cut], samples[cut:]
    print(f"  サンプル数 {len(samples)} (train {len(train)} / test {len(test)})", flush=True)

    net = ValueNet(feature_dim(), hidden=hidden)
    print(f"価値ネット学習中 (dim={feature_dim()}, hidden={hidden}, epochs={epochs})...", flush=True)
    net.train(train, epochs=epochs, lr=0.05, verbose=True)
    print(f"\n held-out: logloss={net.logloss(test):.4f}  accuracy={net.accuracy(test):.1%}")
    base = sum(1 for _, y in test if y >= 0.5) / max(1, len(test))
    print(f" ベースライン(多数派): {max(base, 1-base):.1%}")
    vn, vr = rain_probe(net, loader)
    print(f" 雨プローブ: 水主体側の価値  雨なし={vn:.3f} → 雨あり={vr:.3f} ({'雨を高評価' if vr>vn else '差なし/逆'})")
    net.save()
    print(f"保存: {WEIGHTS_PATH}")


if __name__ == "__main__":
    main()
