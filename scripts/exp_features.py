"""特徴量拡張の価値精度検証（教師あり比較）。

現84次元 vs 強化版（能力ランクを5分割＋実ダメージ脅威2＋控え集約）で、
同一データに対する価値予測精度を比較する。強化版が有意に高ければ特徴量が天井の主因。
"""
import random, copy
import numpy as np

from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.damage import calc_damage
from simulator.features import encode_state
from simulator.az_np import PVNetNP

_STAGES = ["stage_attack", "stage_defense", "stage_sp_attack", "stage_sp_defense", "stage_speed"]


def _expected_frac(att, deff, field):
    """att→deff の最大与ダメージをHP割合で（実ダメージ計算・命中/急所無視, ロール平均）。"""
    if not att.is_alive or not deff.is_alive:
        return 0.0
    best = 0.0
    for mv in att.moves:
        if mv and mv.power and mv.category != "status":
            try:
                d = calc_damage(att, deff, mv, field, random_roll=0.925)
                f = d / max(1, deff.max_hp)
            except Exception:
                f = 0.0
            if f > best:
                best = f
    return min(1.5, best)


def _side_v3(side, opp_active, field):
    party = side.party
    alive = [p for p in party if p.is_alive]
    act = side.active
    tcount = [0.0] * len(TYPES)
    for p in alive:
        for t in (p.type1, p.type2):
            if t in _TI:
                tcount[_TI[t]] += 1.0
    tcount = [c / 3.0 for c in tcount]
    team_hp = sum(p.hp / p.max_hp for p in alive) / 3.0
    n_alive = len(alive) / 3.0
    act_hp = (act.hp / act.max_hp) if act.is_alive and act.max_hp else 0.0
    stages = [max(-1.0, min(1.0, getattr(act, s, 0) / 6.0)) for s in _STAGES]   # ★5分割
    status = [0.0] * 5
    if act.status in _STATUS:
        status[_STATUS[act.status]] = 1.0
    off = max(act.attack, act.sp_attack) / 300.0
    deff = (act.defense + act.sp_defense) / 600.0
    spd = act.speed / 300.0
    mega_avail = 1.0 if (act.mega_data is not None and not act.mega_evolved and not side.mega_used) else 0.0
    mega_used = 1.0 if side.mega_used else 0.0
    act_off = _off_pressure(act, opp_active) if (act.is_alive and opp_active) else 0.0
    switch = _best_switch_score(side, opp_active) if opp_active else 0.0
    bench_best_hp = max([p.hp / p.max_hp for i, p in enumerate(party)
                         if i != side.active_idx and p.is_alive] or [0.0])   # ★控え最良HP
    return (tcount + [team_hp, n_alive, act_hp] + stages + status
            + [off, deff, spd, mega_avail, mega_used, act_off, switch, bench_best_hp])


def encode_v3(side1, side2, field):
    a1, a2 = side1.active, side2.active
    f = _side_v3(side1, a2, field) + _side_v3(side2, a1, field)
    w = [0.0] * 5
    w[_WEATHER.get(field.weather, 0)] = 1.0
    f += w
    f.append(1.0 if field.trick_room else 0.0)
    for s in (side1, side2):
        idx = s.field_idx
        f.append(1.0 if field.stealth_rock[idx] else 0.0)
        f.append(field.spikes[idx] / 3.0)
        f.append(field.toxic_spikes[idx] / 2.0)
    f.append(_best_eff(a1, a2) / 4.0)
    f.append(_best_eff(a2, a1) / 4.0)
    s1_fast = a1.get_effective_speed() >= a2.get_effective_speed()
    f.append(1.0 if s1_fast else 0.0)
    f.append(max(-1.0, min(1.0, (a1.get_effective_speed() - a2.get_effective_speed()) / 200.0)))
    f.append(_expected_frac(a1, a2, field))    # ★実ダメージ脅威 s1→s2
    f.append(_expected_frac(a2, a1, field))    # ★実ダメージ脅威 s2→s1
    return f


_CHOICE = {"こだわりハチマキ", "こだわりメガネ", "こだわりスカーフ"}


def _side_v4(side, opp_active, field):
    base = _side_v3(side, opp_active, field)
    party = side.party; act = side.active
    bench = [p for i, p in enumerate(party) if i != side.active_idx and p.is_alive]
    bench_out = max([_expected_frac(p, opp_active, field) for p in bench] or [0.0]) if opp_active else 0.0
    bench_in = max([_expected_frac(opp_active, p, field) for p in bench] or [0.0]) if opp_active else 0.0
    choice = 1.0 if act.item in _CHOICE else 0.0
    turns = min(1.0, getattr(act, "turns_out", 0) / 5.0)
    status_frac = sum(1.0 for p in party if p.is_alive and p.status) / 3.0
    return base + [bench_out, bench_in, choice, turns, status_frac]


def encode_v4(side1, side2, field):
    a1, a2 = side1.active, side2.active
    f = _side_v4(side1, a2, field) + _side_v4(side2, a1, field)
    w = [0.0] * 5
    w[_WEATHER.get(field.weather, 0)] = 1.0
    f += w
    f.append(1.0 if field.trick_room else 0.0)
    for s in (side1, side2):
        idx = s.field_idx
        f.append(1.0 if field.stealth_rock[idx] else 0.0)
        f.append(field.spikes[idx] / 3.0)
        f.append(field.toxic_spikes[idx] / 2.0)
    f.append(_best_eff(a1, a2) / 4.0)
    f.append(_best_eff(a2, a1) / 4.0)
    s1_fast = a1.get_effective_speed() >= a2.get_effective_speed()
    f.append(1.0 if s1_fast else 0.0)
    f.append(max(-1.0, min(1.0, (a1.get_effective_speed() - a2.get_effective_speed()) / 200.0)))
    fr12 = _expected_frac(a1, a2, field); fr21 = _expected_frac(a2, a1, field)
    f.append(fr12); f.append(fr21)
    f.append(1.0 if (a2.is_alive and fr12 >= a2.hp / max(1, a2.max_hp)) else 0.0)   # s1がs2をOHKO圏内
    f.append(1.0 if (a1.is_alive and fr21 >= a1.hp / max(1, a1.max_hp)) else 0.0)   # s2がs1をOHKO圏内
    # 全抜き速度: 自分activeが相手の生存最速以上か
    o2 = [p.get_effective_speed() for p in side2.party if p.is_alive]
    o1 = [p.get_effective_speed() for p in side1.party if p.is_alive]
    f.append(1.0 if (o2 and a1.get_effective_speed() >= max(o2)) else 0.0)
    f.append(1.0 if (o1 and a2.get_effective_speed() >= max(o1)) else 0.0)
    return f


class _Rec:
    def __init__(self, base, store):
        self.base = base; self.store = store
    def __call__(self, my_side, opp_side, field):
        s1, s2 = (my_side, opp_side) if my_side.field_idx == 0 else (opp_side, my_side)
        try:
            self.store.append((copy.deepcopy(s1), copy.deepcopy(s2), copy.deepcopy(field)))
        except Exception:
            pass
        return self.base(my_side, opp_side, field)


def gen_data(n_games=200, seed=0, max_snap=10):
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    rng = random.Random(seed); rows = []
    for g in range(n_games):
        pa, pb = rng.sample(parties, 2)
        s1 = BattleSide(heuristic_selection(build_party(pa, loader), build_party(pb, loader), loader))
        s2 = BattleSide(heuristic_selection(build_party(pb, loader), build_party(pa, loader), loader))
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        store = []
        ai = HeuristicAI()
        w = Battle(s1, s2).run(_Rec(ai, store), _Rec(ai, store))
        if w == 0:
            continue
        y = 1.0 if w == 1 else 0.0
        snaps = store if len(store) <= max_snap else rng.sample(store, max_snap)
        for (cs1, cs2, cf) in snaps:
            rows.append((cs1, cs2, cf, y))
    return rows


def train_eval(X, Y, hidden=256, hidden2=128, hidden3=0, epochs=60, seed=1):
    from simulator.alphazero import ACTION_DIM
    X = np.asarray(X, float); Y = np.asarray(Y, float)
    n = len(X); rng = np.random.default_rng(seed); perm = rng.permutation(n)
    ntr = int(n * 0.8); tr, va = perm[:ntr], perm[ntr:]
    net = PVNetNP(X.shape[1], hidden, hidden2, hidden3, seed=seed)
    PI = np.ones((n, ACTION_DIM)) / ACTION_DIM; M = np.ones((n, ACTION_DIM))
    net.train_pi(X[tr], PI[tr], M[tr], Y[tr], epochs=epochs, lr=0.05, batch=256, value_weight=1.0)
    return net.value_acc(X[va], Y[va]), net.value_acc(X[tr], Y[tr])


if __name__ == "__main__":
    print("データ生成中...", flush=True)
    rows = gen_data(n_games=240, seed=7)
    print(f"サンプル数: {len(rows)}", flush=True)
    X_v4 = [encode_state(s1, s2, f) for (s1, s2, f, y) in rows]   # 現encode_state=新v4(218)
    Y = [y for (*_, y) in rows]
    print(f"次元: v4(新)={len(X_v4[0])}", flush=True)
    accs = [train_eval(X_v4, Y, seed=s)[0] for s in (1, 2, 3)]
    print(f"v4新(218): 価値精度(val) = {np.mean(accs):.3f} ± {np.std(accs):.3f}  (3seed) ※v3=0.685", flush=True)
