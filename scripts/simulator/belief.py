"""非開示情報の推定器（Phase 1: belief）。

相手1体について「型(EV/性格)・技・持ち物・特性」の確率分布を保持する。

- 技/持ち物/特性: 使用率DBを事前分布とし、opp_view の開示で確定（ダメージ計算は使わない）。
- EV/性格: opp_view.damage_log の被ダメージ割合から、自分の攻撃側を既知としてダメージ式を
  逆算し、各候補スプレッドの尤度（16段階の乱数ロールで観測割合を再現できる割合）でベイズ更新。
  自己対戦では相手の真の型を我々が知っているため、推定精度を直接検証できる。

観測チャネル（どれも「実機で見える情報」だけを使う）:
- 被ダメージ割合 → 防御側の EV/性格（observe_damage）
- 与ダメージ割合 → 攻撃側の EV/性格（observe_damage_dealt）。相手が自分を殴った量から
  A/C を絞る。これが無いと「今のじしんで6割減った＝A全振り」が働かない。
- 行動順 → 実効速度の上下限（observe_order）。こだわりスカーフは M-6 TOP50 で使用率
  485%pt の3位で、最速の相手に抜かれたら人間は即座にスカーフを疑う。
- 発動しなかったこと → 持ち物の否定（observe_absent_item）。ターン終了で回復しなければ
  たべのこしではない、状態異常が治らなければラムのみではない。

既知の制約（Phase 1）:
- 候補防御体は ensure() 時点の開示特性/持ち物で1度だけ構築する（途中で持ち物が判明しても再構築しない）。
- 攻撃側・場の状態は観測時点の実値を呼び出し側が渡す前提（battle.py の被ダメージ確定点で更新）。
"""
import math
import os
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


def _eff_speed_of(p, field, item_mult: float) -> int:
    """実効速度。倍率は battle._speed_order / ai._effective_speed に揃える。
    持ち物は候補ごとに差し替えたいので、掛ける倍率を引数で受ける。"""
    spd = math.floor(p.get_effective_speed() * item_mult)
    w = getattr(field, "weather", None)
    ab = p.ability
    if (w == "rain" and ab == "すいすい") or (w == "sunny" and ab == "ようりょくそ") \
            or (w == "sandstorm" and ab == "すなかき") or (w in ("hail", "snow") and ab == "ゆきかき"):
        spd *= 2
    if getattr(field, "electric_terrain", False) and ab == "サーフテール":
        spd *= 2
    return int(spd)


def _default_belief_season() -> str:
    """信念の既定シーズン。BELIEF_SEASON > POOL_SEASON > M-6 の順で解決する。
    以前は M-2 固定で、M-6 の対戦でも M-2 の使用率分布から相手の型を引いていた。"""
    return (os.environ.get("BELIEF_SEASON")
            or os.environ.get("POOL_SEASON")
            or "M-6")


class PokemonBelief:
    """相手1体の型・技・持ち物・特性の信念。"""

    def __init__(self, tpl, loader: DataLoader, season: Optional[str] = None,
                 known_ability: Optional[str] = None, known_item: Optional[str] = None,
                 extra_spreads: Optional[list] = None):
        season = season or _default_belief_season()
        self.name = tpl.name
        self.tpl = tpl

        # ── 技/持ち物/特性: 使用率を周辺確率とする事前分布（開示で上書き） ──
        self.move_prior: Dict[str, float] = {m: r for m, r in tpl.top_moves}
        self.item_prior: Dict[str, float] = {i: r for i, r in tpl.top_items}
        self.ability_prior: Dict[str, float] = {a: r for a, r in tpl.top_abilities}
        self.known_moves: set = set()
        # 型まるごとの候補（登録テンプレート由来）。JOINT_BUILD=1 のとき決定化で使う
        self.builds: list = []
        # この確率で最尤型を返す（0=常にサンプリング・従来）
        self.map_rate: float = float(os.environ.get("BUILD_MAP_RATE", "0") or 0)
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

    def observe_damage_dealt(self, defender, move, observed_fraction: float,
                             field, critical: bool = False) -> bool:
        """相手（この信念の主）が自分に与えたダメージ割合で事後確率を更新する。
        観測できるのは自分のHPが減った割合＝実機で見える情報だけ。攻撃側の候補を
        取り替えてダメージ式を回し、観測を再現できた候補の尤度でベイズ更新する。
        被ダメージ(observe_damage)は相手の耐久を絞るが、こちらは相手の攻撃を絞る。"""
        liks = []
        for c in self.cands:
            a = c["defender"]          # 同じ個体を攻撃側として使う（実数値は全ステ入っている）
            hit = 0
            for rr in _ROLLS:
                dmg = calc_damage(a, defender, move, field, critical=critical, random_roll=rr)
                if round(dmg / defender.max_hp, 3) == observed_fraction:
                    hit += 1
            liks.append(hit / len(_ROLLS))
        if sum(liks) == 0:
            return False
        new = [p * (lik * (1 - _EPS) + _EPS) for p, lik in zip(self.post, liks)]
        t = sum(new) or 1.0
        self.post = [x / t for x in new]
        return True

    def observe_order(self, my_eff_speed: int, opp_first: bool, field) -> bool:
        """行動順から相手の実効速度の上下限を絞る。優先度が同じ場合のみ呼ぶこと。
        候補ごとに「持ち物なし」と「こだわりスカーフ」の両方を試し、観測と矛盾しない
        組み合わせが1つも無い候補を落とす。スカーフでしか説明できなければスカーフを確定する。"""
        from .items import get_speed_item_multiplier
        scarf_p = self.item_prior.get("こだわりスカーフ", 0.0)
        liks = []
        need_scarf = True
        for c in self.cands:
            d = c["defender"]
            base = _eff_speed_of(d, field, 1.0)
            ok_plain = (base >= my_eff_speed) if opp_first else (base <= my_eff_speed)
            ok_scarf = False
            if scarf_p > 0 and self.known_item in (None, "こだわりスカーフ"):
                sc = _eff_speed_of(d, field, get_speed_item_multiplier("こだわりスカーフ"))
                ok_scarf = (sc >= my_eff_speed) if opp_first else (sc <= my_eff_speed)
            if ok_plain:
                need_scarf = False
            liks.append(1.0 if (ok_plain or ok_scarf) else 0.0)
        if sum(liks) == 0:
            return False                      # どの候補でも説明できない＝モデル外（更新しない）
        new = [p * (lik * (1 - _EPS) + _EPS) for p, lik in zip(self.post, liks)]
        t = sum(new) or 1.0
        self.post = [x / t for x in new]
        if need_scarf and scarf_p > 0 and self.known_item is None:
            self.known_item = "こだわりスカーフ"   # スカーフ以外では速度を説明できない
            self.item_prior = {"こだわりスカーフ": 100.0}
        elif not opp_first and self.known_item is None and scarf_p > 0:
            pass                               # 遅かっただけではスカーフを否定できない
        return True

    def observe_absent_item(self, items) -> bool:
        """「発動しなかった」ことから持ち物を否定する。
        例: ターン終了で回復しなかった→たべのこし/くろいヘドロではない。
        開示済みなら何もしない（確定情報が優先）。"""
        if self.known_item is not None:
            return False
        drop = [i for i in items if i in self.item_prior]
        if not drop:
            return False
        for i in drop:
            self.item_prior.pop(i, None)
        if not self.item_prior:
            self.item_prior = {"": 100.0}      # 全否定は起こりうる（未収録持ち物）
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

    def sample_build(self, rng):
        """型まるごとを1つ引く（技・持ち物・性格・努力値の同時性が保たれる）。
        既知情報（判明した技・持ち物・特性）と矛盾する型は候補から外すので、
        技が1本分かっただけで持ち物や努力値の候補まで絞れる。候補が無ければ None。"""
        if not self.builds:
            return None
        ok = []
        for b in self.builds:
            if self.known_item is not None and b["item"] != self.known_item:
                continue
            if self.known_ability is not None and b.get("ability") and b["ability"] != self.known_ability:
                continue
            if not self.known_moves.issubset(set(b["moves"])):
                continue
            ok.append(b)
        if not ok:
            return None
        w = [(b, max(self._build_weight(b), 1e-6)) for b in ok]
        # 情報は超加法的（実測: 持ち物だけ/技だけの開示は +0〜1.7pt、全部揃うと +10.0pt）。
        # 毎回ランダムに引くと「どれも少しずつ違う相手」ばかりになる。最尤型に寄せると
        # 「完全に正しい相手」でのシミュレーションが一定割合生まれる。
        if self.map_rate > 0.0 and rng.random() < self.map_rate:
            return max(w, key=lambda x: x[1])[0]
        return self._weighted(rng, w)

    def _build_weight(self, b) -> float:
        """型の重み＝持ち物と技の使用率の積（同時分布が無いので周辺で近似する）。"""
        w = self.item_prior.get(b["item"], 0.01) if b["item"] else 0.01
        for m in b["moves"]:
            w *= max(self.move_prior.get(m, 0.01), 0.01)
        return w

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


_REG_BUILD_CACHE: Dict[int, Dict[str, list]] = {}


def registered_builds_by_species(loader: DataLoader) -> Dict[str, list]:
    """登録テンプレートから種族ごとの**型まるごと**の一覧を取得する。

    `registered_spreads_by_species` は努力値と性格しか取らず、技・持ち物との同時性を捨てていた。
    技4本を周辺分布から独立に引くと、実在しない組み合わせができる（実測: 事前のみで全一致7%）。
    型単位で引けば組み合わせが保たれ、技が1本判明しただけで持ち物や努力値の候補まで絞れる。
    """
    ck = id(loader)
    if ck in _REG_BUILD_CACHE:
        return _REG_BUILD_CACHE[ck]
    from .env import load_templates
    out: Dict[str, list] = {}
    seen: Dict[str, set] = {}
    for party in load_templates():
        for spec in party.specs:
            moves = tuple(sorted(m for m in (spec.get("moves") or []) if m))
            if not moves:
                continue
            ev = {k: spec["evs"].get(k, 0) for k in "HABCDS"}
            ev["spread"] = "登録"
            key = (spec.get("item"), spec["nature"], moves, spec.get("ability"))
            st = seen.setdefault(spec["name"], set())
            if key in st:
                continue
            st.add(key)
            out.setdefault(spec["name"], []).append({
                "item": spec.get("item"), "nature": spec["nature"], "ev": ev,
                "ability": spec.get("ability"), "moves": list(moves),
            })
    _REG_BUILD_CACHE[ck] = out
    return out


class OpponentBelief:
    """一方のサイドが相手パーティ全体について持つ信念（種族名→PokemonBelief）。"""

    def __init__(self, loader: DataLoader, season: Optional[str] = None, use_registered: bool = True):
        self.loader = loader
        self.season = season or _default_belief_season()
        self.species: Dict[str, PokemonBelief] = {}
        # このメタ（登録パーティ同士）では真の型を候補に含めて推定精度を上げる
        self._reg = registered_spreads_by_species(loader) if use_registered else {}
        # 型まるごとの候補。JOINT_BUILD=1 で決定化が型単位のサンプリングになる
        self.joint = os.environ.get("JOINT_BUILD", "0") == "1"
        self._builds = registered_builds_by_species(loader) if (use_registered and self.joint) else {}

    def __deepcopy__(self, memo):
        # 信念は対戦状態の一部ではない（意思決定者の知識）。
        # Battle.clone()（決定化ロールアウト）には引き継がず、実信念の汚染も防ぐ。
        return None

    # 使用率行のあるシーズンを新しい順に探す（事前分布が空だと型リークになるため）。
    _FALLBACK_SEASONS = ("M-6", "M-5", "M-4", "M-3", "M-2")

    def _tpl_with_prior(self, name: str):
        """事前分布を持つテンプレート。self.season に使用率行が無い種は、行のある
        最新シーズンへフォールバックする。

        空の事前分布は「相手を弱いと見なす」のではなく **型リーク** を生む。
        SearchAI._determinize は falsy を上書きしない実装（`if c.get("item") is not None:`）
        なので、prior が空だと相手の真の持ち物・特性・技がそのまま探索に残ってしまう。
        M-6の200種のうち53種、上位40種のうち14種が M-2 に行を持たない。"""
        tpl = self.loader.get_pokemon_template(name, self.season)
        if tpl is not None and (tpl.top_moves or tpl.top_items or tpl.top_abilities):
            return tpl, self.season
        for s in self._FALLBACK_SEASONS:
            if s == self.season:
                continue
            alt = self.loader.get_pokemon_template(name, s)
            if alt is not None and (alt.top_moves or alt.top_items or alt.top_abilities):
                return alt, s
        return tpl, self.season

    def ensure(self, name: str, known_ability: Optional[str] = None,
               known_item: Optional[str] = None) -> Optional[PokemonBelief]:
        if name not in self.species:
            tpl, season = self._tpl_with_prior(name)
            if tpl is None:
                return None
            pb = PokemonBelief(
                tpl, self.loader, season,
                known_ability=known_ability, known_item=known_item,
                extra_spreads=self._reg.get(name))
            pb.builds = self._builds.get(name, [])
            if getattr(self, "_map_rate", None) is not None:
                pb.map_rate = self._map_rate
            self.species[name] = pb
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

    def observe_damage_dealt(self, attacker_name: str, defender, move,
                             observed_fraction: float, field, critical: bool = False) -> bool:
        b = self.ensure(attacker_name)
        if b is None:
            return False
        return b.observe_damage_dealt(defender, move, observed_fraction, field, critical)

    def observe_order(self, opp_name: str, my_eff_speed: int, opp_first: bool, field) -> bool:
        b = self.ensure(opp_name)
        if b is None:
            return False
        return b.observe_order(my_eff_speed, opp_first, field)

    def observe_absent_item(self, opp_name: str, items) -> bool:
        b = self.ensure(opp_name)
        if b is None:
            return False
        return b.observe_absent_item(items)
