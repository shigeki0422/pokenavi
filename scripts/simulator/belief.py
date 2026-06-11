"""非開示情報の推定器（Phase 1: belief）。

相手1体について「型(EV/性格)・技・持ち物・特性」の確率分布を保持する。

- 技/持ち物/特性: 使用率DBを事前分布とし、opp_view の開示で確定（ダメージ計算は使わない）。
- EV/性格: opp_view.damage_log の被ダメージ割合から、自分の攻撃側を既知としてダメージ式を
  逆算し、各候補スプレッドの尤度（16段階の乱数ロールで観測割合を再現できる割合）でベイズ更新。
  自己対戦では相手の真の型を我々が知っているため、推定精度を直接検証できる。

既知の制約（Phase 1）:
- 候補防御体は ensure() 時点の開示特性/持ち物で1度だけ構築する（途中で持ち物が判明しても再構築しない）。
- 攻撃側・場の状態は観測時点の実値を呼び出し側が渡す前提（battle.py の被ダメージ確定点で更新）。
"""
import math
from typing import List, Optional, Dict

from .data import DataLoader
from .pokemon import build_from_template
from .damage import calc_damage

# ダメージ乱数の16段階（0.85〜1.00）に対応する random_roll（0〜1）
_ROLLS = [k / 15 for k in range(16)]
_EPS = 1e-4  # 尤度の下限（モデル誤差で真の候補を完全消去しないための平滑化）

# 候補数の上限（暴走防止）
_MAX_EVS = 14
_MAX_NATS = 7


class PokemonBelief:
    """相手1体の型・技・持ち物・特性の信念。"""

    def __init__(self, tpl, loader: DataLoader, season: str = "M-2",
                 known_ability: Optional[str] = None, known_item: Optional[str] = None,
                 extra_spreads: Optional[list] = None):
        self.name = tpl.name
        self.tpl = tpl

        # ── 技/持ち物/特性: 使用率を周辺確率とする事前分布（開示で上書き） ──
        self.move_prior: Dict[str, float] = {m: r for m, r in tpl.top_moves}
        self.item_prior: Dict[str, float] = {i: r for i, r in tpl.top_items}
        self.ability_prior: Dict[str, float] = {a: r for a, r in tpl.top_abilities}
        self.known_moves: set = set()
        self.known_item: Optional[str] = known_item
        self.known_ability: Optional[str] = known_ability

        # ── EV/性格の候補と事前確率 ──
        natures = (tpl.top_natures or [("まじめ", 1.0)])[:_MAX_NATS]
        evs = (tpl.top_evs or [({"H": 0, "A": 0, "B": 0, "C": 0, "D": 0, "S": 0,
                                 "spread": "無振り"}, 1.0)])[:_MAX_EVS]
        self.cands = []   # 各候補: {"ev","nature","label","defender"}
        priors = []
        for ev, er in evs:
            for nat, nr in natures:
                defender = build_from_template(
                    tpl, loader, randomize=False,
                    override_evs={k: ev.get(k, 0) for k in ("H", "A", "B", "C", "D", "S")},
                    override_nature=nat,
                    override_ability=known_ability,
                    override_item=known_item)
                self.cands.append({
                    "ev": ev, "nature": nat,
                    "label": f"{ev.get('spread', '')}/{nat}",
                    "defender": defender,
                })
                priors.append(max(er, 1e-9) * max(nr, 1e-9))

        # 登録パーティの実スプレッドを候補に追加（このメタは登録パーティ同士のため、
        # 真の型を候補に含めることで推定の的中・耐久較正を強化する）。
        if extra_spreads:
            keys = {(tuple(c["ev"].get(k, 0) for k in "HABCDS"), c["nature"]) for c in self.cands}
            avg = (sum(priors) / len(priors)) if priors else 1.0
            for ev, nat in extra_spreads:
                key = (tuple(ev.get(k, 0) for k in "HABCDS"), nat)
                if key in keys:
                    continue
                keys.add(key)
                defender = build_from_template(
                    tpl, loader, randomize=False,
                    override_evs={k: ev.get(k, 0) for k in ("H", "A", "B", "C", "D", "S")},
                    override_nature=nat, override_ability=known_ability, override_item=known_item)
                self.cands.append({"ev": dict(ev), "nature": nat,
                                   "label": f"{ev.get('spread', '登録')}/{nat}", "defender": defender})
                priors.append(avg)

        s = sum(priors) or 1.0
        self.prior = [p / s for p in priors]
        self.post = list(self.prior)

    # ── 開示情報の反映 ───────────────────────────────────────────────
    def observe_disclosure(self, knowledge) -> None:
        """opp_view の PokeKnowledge から確定情報を取り込む。"""
        if knowledge is None:
            return
        for mv in knowledge.known_moves:
            self.known_moves.add(mv)
        if knowledge.known_item:
            self.known_item = knowledge.known_item
        if knowledge.known_ability:
            self.known_ability = knowledge.known_ability

    # ── ダメージ割合からのEV/性格ベイズ更新 ──────────────────────────
    def observe_damage(self, attacker, move, observed_fraction: float,
                       field, critical: bool = False) -> bool:
        """観測した被ダメージ割合で候補の事後確率を更新する。
        更新できた（いずれかの候補が観測を再現できた）場合 True。"""
        liks = []
        for c in self.cands:
            d = c["defender"]
            hit = 0
            for rr in _ROLLS:
                dmg = calc_damage(attacker, d, move, field, critical=critical, random_roll=rr)
                if round(dmg / d.max_hp, 3) == observed_fraction:
                    hit += 1
            liks.append(hit / len(_ROLLS))
        if sum(liks) == 0:
            return False  # どの候補も再現不可（モデル外要因）→更新しない
        new = [p * (lik * (1 - _EPS) + _EPS) for p, lik in zip(self.post, liks)]
        s = sum(new) or 1.0
        self.post = [x / s for x in new]
        return True

    # ── クエリ ───────────────────────────────────────────────────────
    def spread_posterior(self):
        """(label, ev, nature, prob) を確率降順で返す。"""
        out = [(c["label"], c["ev"], c["nature"], p) for c, p in zip(self.cands, self.post)]
        out.sort(key=lambda x: x[3], reverse=True)
        return out

    def map_spread(self):
        i = max(range(len(self.post)), key=lambda j: self.post[j])
        return self.cands[i]["ev"], self.cands[i]["nature"]

    def prob_of_spread(self, ev: dict, nature: str) -> float:
        keys = ("H", "A", "B", "C", "D", "S")
        total = 0.0
        for c, p in zip(self.cands, self.post):
            if c["nature"] == nature and all(c["ev"].get(k, 0) == ev.get(k, 0) for k in keys):
                total += p
        return total

    def expected_stat(self, attr: str) -> float:
        return sum(getattr(c["defender"], attr) * p for c, p in zip(self.cands, self.post))

    # ── サンプリング（決定化ロールアウト用） ───────────────────────
    @staticmethod
    def _weighted(rng, items):
        """items=[(value, weight),...] から重み付き抽選。空なら None。"""
        items = [(v, w) for v, w in items if w > 0]
        if not items:
            return None
        total = sum(w for _, w in items)
        r = rng.random() * total
        for v, w in items:
            r -= w
            if r <= 0:
                return v
        return items[-1][0]

    def sample_spread(self, rng):
        """事後分布に従いEV/性格を1つサンプリング → (ev, nature)。"""
        i = self._weighted(rng, list(zip(range(len(self.cands)), self.post)))
        if i is None:
            i = 0
        return self.cands[i]["ev"], self.cands[i]["nature"]

    def sample_item(self, rng):
        if self.known_item is not None:
            return self.known_item
        return self._weighted(rng, list(self.item_prior.items()))

    def sample_ability(self, rng):
        if self.known_ability is not None:
            return self.known_ability
        return self._weighted(rng, list(self.ability_prior.items())) or ""

    def sample_moves(self, rng, n: int = 4):
        """既知技を確定で含め、残り枠を使用率事前から非復元抽選で埋める。"""
        chosen = list(dict.fromkeys(self.known_moves))[:n]
        pool = [(m, r) for m, r in self.move_prior.items() if m not in chosen]
        while len(chosen) < n and pool:
            m = self._weighted(rng, pool)
            if m is None:
                break
            chosen.append(m)
            pool = [(x, r) for x, r in pool if x != m]
        return chosen

    def prob_has_move(self, move_name: str) -> float:
        if move_name in self.known_moves:
            return 1.0
        return min(1.0, self.move_prior.get(move_name, 0.0))

    def prob_item(self, item_name: str) -> float:
        if self.known_item is not None:
            return 1.0 if self.known_item == item_name else 0.0
        return self.item_prior.get(item_name, 0.0)

    def prob_ability(self, ability_name: str) -> float:
        if self.known_ability is not None:
            return 1.0 if self.known_ability == ability_name else 0.0
        return self.ability_prior.get(ability_name, 0.0)


_REG_SPREAD_CACHE: Dict[int, Dict[str, list]] = {}


def registered_spreads_by_species(loader: DataLoader) -> Dict[str, list]:
    """登録テンプレート（UIと同一源）から種族ごとの実スプレッド一覧
    [(ev_dict, nature), ...] を取得（重複除去・キャッシュ）。"""
    ck = id(loader)
    if ck in _REG_SPREAD_CACHE:
        return _REG_SPREAD_CACHE[ck]
    from .env import load_templates
    out: Dict[str, list] = {}
    seen: Dict[str, set] = {}
    for party in load_templates():
        for spec in party.specs:
            ev = {k: spec["evs"].get(k, 0) for k in "HABCDS"}
            ev["spread"] = "登録"
            key = (tuple(ev[k] for k in "HABCDS"), spec["nature"])
            s = seen.setdefault(spec["name"], set())
            if key in s:
                continue
            s.add(key)
            out.setdefault(spec["name"], []).append((ev, spec["nature"]))
    _REG_SPREAD_CACHE[ck] = out
    return out


class OpponentBelief:
    """一方のサイドが相手パーティ全体について持つ信念（種族名→PokemonBelief）。"""

    def __init__(self, loader: DataLoader, season: str = "M-2", use_registered: bool = True):
        self.loader = loader
        self.season = season
        self.species: Dict[str, PokemonBelief] = {}
        # このメタ（登録パーティ同士）では真の型を候補に含めて推定精度を上げる
        self._reg = registered_spreads_by_species(loader) if use_registered else {}

    def __deepcopy__(self, memo):
        # 信念は対戦状態の一部ではない（意思決定者の知識）。
        # Battle.clone()（決定化ロールアウト）には引き継がず、実信念の汚染も防ぐ。
        return None

    def ensure(self, name: str, known_ability: Optional[str] = None,
               known_item: Optional[str] = None) -> Optional[PokemonBelief]:
        if name not in self.species:
            tpl = self.loader.get_pokemon_template(name, self.season)
            if tpl is None:
                return None
            self.species[name] = PokemonBelief(
                tpl, self.loader, self.season,
                known_ability=known_ability, known_item=known_item,
                extra_spreads=self._reg.get(name))
        return self.species[name]

    def get(self, name: str) -> Optional[PokemonBelief]:
        return self.species.get(name)

    def observe_disclosure(self, opp_view) -> None:
        """opp_view 全体の開示情報を信念に取り込む。"""
        for name, knowledge in opp_view.pokemon.items():
            b = self.ensure(name, known_ability=knowledge.known_ability,
                            known_item=knowledge.known_item)
            if b is not None:
                b.observe_disclosure(knowledge)

    def observe_damage(self, defender_name: str, attacker, move,
                       observed_fraction: float, field, critical: bool = False) -> bool:
        b = self.ensure(defender_name)
        if b is None:
            return False
        return b.observe_damage(attacker, move, observed_fraction, field, critical)
