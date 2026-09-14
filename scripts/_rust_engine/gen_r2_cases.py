"""R2 コーパス（cases/turn_*.jsonl）の再生成。

元の生成スクリプトは消失している。記録は「記録時点の Python」の期待値なので、
仕様変更（必ず急所・バトルスイッチ等）が入ると RNG 消費列ごと変わり、
記録された抽選値での再生自体ができなくなる＝採り直しではなく再生成しか手がない。

既存コーパスのパーティ構成（specsA/B・season・roll_override・見せ合い）を引き継ぐことで
カバレッジ（moves/abilities/items）を保ったまま、行動・抽選列・期待状態だけを現在の Python で
採り直す。行動はシード固定のランダム合法手＝エンジンの分岐を広く踏ませるため。

env: IN(cases/turn_*.jsonl のglob) DRY(1=書かない) MAXB(1ファイルあたりの上限)
"""
import os, sys, json, glob, random

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE)); sys.path.insert(0, _HERE)
import state_codec as SC
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, Battle, BattleField, Action, _entry_effects
import simulator.damage as _dmg

L = get_loader()
DRY = os.environ.get("DRY") == "1"


class _PV:
    def __init__(self, t):
        self.name, self.base_type1, self.base_type2, self.type1, self.type2 = t[0], t[1], t[2], t[3], t[4]


class RecRandom:
    """対戦中の乱数を記録しつつ供給する。draws は [種別, 値] の列。
    種別は gate_r2.rs の parse_draws と一致させる: r/i/c/w。"""

    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.draws = []

    def random(self):
        v = self.rng.random(); self.draws.append(["r", v]); return v

    def randint(self, a, b):
        v = self.rng.randint(a, b); self.draws.append(["i", v]); return v

    def choice(self, seq):
        i = self.rng.randrange(len(seq)); self.draws.append(["c", i]); return seq[i]

    def choices(self, population, weights=None, k=1):
        # w は「選ばれた値」を記録する。gate_r2 の Adapter は choices() の戻り値を
        # そのまま連続ヒット数として使うため、インデックスを記録すると回数が化ける
        # （battle.py:2737 は [2,3,4,5] から回数を引く）。
        v = self.rng.choices(list(population), weights=weights, k=1)[0]
        self.draws.append(["w", v]); return [v]


def _legal_actions(side):
    act = side.active
    out = []
    for i, m in enumerate(act.moves or []):
        if m is not None:
            out.append(Action(type="move", move=m, move_idx=i, switch_to=-1, do_mega=False))
            if getattr(act, "mega_data", None) is not None and not act.mega_evolved and not side.mega_used:
                out.append(Action(type="move", move=m, move_idx=i, switch_to=-1, do_mega=True))
    for j, p in enumerate(side.party):
        if j != side.active_idx and p.is_alive:
            out.append(Action(type="switch", move=None, move_idx=None, switch_to=j, do_mega=False))
    return out


def _enc_action(a):
    if a.type == "switch":
        return ["switch", 0, None, a.switch_to, bool(a.do_mega)]
    m = a.move
    # power/accuracy/pp の None を 0 に潰してはいけない。gate_r2.decode_action は
    # そのまま Some(0) として読むため、必中技(accuracy=None)が命中0%になって全て失敗する。
    md = [m.name_jp, m.type, m.category, m.power, m.accuracy, (m.priority or 0), m.pp] if m else None
    return ["move", a.move_idx, md, -1, bool(a.do_mega)]


def generate(rec, seed):
    bt_rng = RecRandom(seed)
    pol = random.Random(seed ^ 0x5bd1e995)
    _orig_roll = _dmg._ROLL_OVERRIDE
    # Rust 側 Field.roll_override と等価。掛けないと Python だけがダメージ乱数を引いてずれる。
    _dmg._ROLL_OVERRIDE = rec.get("roll_override")
    _orig = (random.random, random.randint, random.choice, random.choices)
    random.random, random.randint, random.choice, random.choices = (
        bt_rng.random, bt_rng.randint, bt_rng.choice, bt_rng.choices)
    try:
        A = [build_from_spec(parse_pokemon_spec(s), L, season=rec["seasonA"], randomize=False) for s in rec["specsA"]]
        B = [build_from_spec(parse_pokemon_spec(s), L, season=rec["seasonB"], randomize=False) for s in rec["specsB"]]
        s1 = BattleSide(A, viewer_label="P1"); s2 = BattleSide(B, viewer_label="P2")
        s1.field_idx = 0; s2.field_idx = 1
        fld = BattleField()
        # roll_override は Rust 側 Field のフィールドで Python には無い。Python では
        # damage._ROLL_OVERRIDE（乱数指定なしの呼び出しを固定ロールに置換）が等価。
        # これを掛けないと Python だけがダメージ乱数を引き、抽選列が Rust とずれる。
        b = Battle(s1, s2, fld)
        s1.opp_view.team_preview([_PV(t) for t in rec["pv1"]])
        s2.opp_view.team_preview([_PV(t) for t in rec["pv2"]])
        _entry_effects(s1.active, 0, fld, s2.active, b.logs, s1.party)
        _entry_effects(s2.active, 1, fld, s1.active, b.logs, s2.party)
        bt_rng.draws = []                 # start までの抽選は rng0 扱い（既存記録も空）
        s0 = SC.encode_battle(b).vals

        turns = []
        chosen = {}
        # 方策: 既定は合法手の一様抽選（POLICY=random）。
        # GreedyAI を使ってはいけない: AI の手評価は calc_damage を呼び、その副作用で
        # 相手の半減きのみを消費してしまう（damage.py:745 defender.item = None）。
        # ゲートは行動をリプレイするので Rust 側は AI を呼ばず消費しない＝再現不能になる。
        # （Rust の ai.rs もこの副作用を意図的に再現しているが、replay 経路では走らない）
        # 一様抽選は副作用が無く、かつエンジンの分岐を広く踏める。
        use_random = os.environ.get("POLICY", "random") == "random"
        from simulator.ai import GreedyAI
        g1, g2 = GreedyAI(), GreedyAI()

        def pick(side, other, f, g):
            if use_random:
                la = _legal_actions(side)
                if la:
                    return pol.choice(la)
            return g(side, other, f)

        def ai1(m, o, f):
            a = pick(m, o, f, g1); chosen[0] = a; return a

        def ai2(m, o, f):
            a = pick(m, o, f, g2); chosen[1] = a; return a

        def on_turn(bt):
            turns.append({"t": bt.turn,
                          "acts": [_enc_action(chosen[0]), _enc_action(chosen[1])],
                          "rng": bt_rng.draws,
                          "S": SC.encode_battle(bt).vals})
            bt_rng.draws = []

        res = b._turn_loop(ai1, ai2, on_turn=on_turn)
    finally:
        random.random, random.randint, random.choice, random.choices = _orig
        _dmg._ROLL_OVERRIDE = _orig_roll
    return s0, turns, res


def main():
    pats = os.environ.get("IN", os.path.join(_HERE, "cases", "turn_*.jsonl"))
    files = sorted(glob.glob(pats))
    if not files:
        sys.exit(f"対象なし: {pats}")
    maxb = int(os.environ.get("MAXB", "0"))
    tot = ok = 0
    for path in files:
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
        hdr = json.loads(lines[0])
        out = [None]
        nbad = 0
        for li in range(1, len(lines)):
            if maxb and li > maxb:
                break
            rec = json.loads(lines[li]); tot += 1
            try:
                s0, turns, res = generate(rec, 7_000_000_000 + rec["b"] * 1009)
            except Exception as ex:
                nbad += 1
                print(f"  [skip] {os.path.basename(path)} b={rec['b']}: {type(ex).__name__} {ex}", flush=True)
                continue
            rec["S0"] = s0; rec["turns"] = turns; rec["result"] = res
            rec["nturn"] = len(turns); rec["rng0"] = []
            ok += 1
            out.append(json.dumps(rec, ensure_ascii=False))
        out[0] = json.dumps(hdr, ensure_ascii=False)
        if not DRY:
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(out) + "\n")
        print(f"{os.path.basename(path)}: {len(out)-1}件 生成 (失敗{nbad})", flush=True)
    print(f"■ 再生成完了: {ok}/{tot}" + ("  [DRY]" if DRY else ""), flush=True)


if __name__ == "__main__":
    main()
