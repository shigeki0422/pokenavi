"""
各サイドが相手パーティについて持つ情報（情報の非対称性）
"""
import copy
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class PokeKnowledge:
    """相手の1体について知っていること"""
    name: str
    previewed: bool = False   # 対戦前の見せ合いで候補として確認済み（種族・タイプは既知）
    seen: bool = False        # 実際に場に出たのを確認済み
    type1: Optional[str] = None
    type2: Optional[str] = None
    known_moves: List[str] = field(default_factory=list)
    known_item: Optional[str] = None
    known_ability: Optional[str] = None
    threat_alert: bool = False  # きけんよちで「効果抜群/一撃必殺の技を持つ」と察知済み
    hp_fraction: float = 1.0    # 残りHP割合（実数は不可視。HPバーから観測できる割合）
    # 技別の被ダメージ割合履歴（ダメージ計算でEV/性格を逆算する用）
    # 各要素: {"move": 技名, "attacker": 攻撃側名, "fraction": ダメージ/最大HP}
    damage_log: List[dict] = field(default_factory=list)

    def __deepcopy__(self, memo):
        new = self.__class__.__new__(self.__class__)
        memo[id(self)] = new
        nd = new.__dict__
        for k, v in self.__dict__.items():
            nd[k] = copy.deepcopy(v, memo) if type(v) in (list, dict, set) else v
        return new


class OpponentView:
    """一方のサイドが相手パーティについて持つ知識"""

    def __init__(self, viewer: str = ""):
        self.viewer = viewer
        self.pokemon: dict = {}

    def __deepcopy__(self, memo):
        new = OpponentView(self.viewer)
        memo[id(self)] = new
        new.pokemon = {k: copy.deepcopy(v, memo) for k, v in self.pokemon.items()}
        return new

    def _get(self, name: str) -> PokeKnowledge:
        if name not in self.pokemon:
            self.pokemon[name] = PokeKnowledge(name=name)
        return self.pokemon[name]

    def team_preview(self, party) -> List[str]:
        """対戦前の見せ合い：相手の候補6体の種族・タイプを確認する（技/持ち物/特性は未知）。"""
        names = []
        for poke in party:
            k = self._get(poke.name)
            k.previewed = True
            if k.type1 is None:
                k.type1 = poke.base_type1 if poke.base_type1 else poke.type1
                k.type2 = poke.base_type2 if poke.base_type2 else poke.type2
            names.append(poke.name)
        return [f"▷{self.viewer}: 見せ合い — 相手候補{len(names)}体: {'/'.join(names)}"]

    def on_anticipation(self, opp_name: str) -> List[str]:
        """きけんよち：相手が効果抜群/一撃必殺の技を持つと察知（具体技名までは開示しない）。"""
        k = self._get(opp_name)
        if k.threat_alert:
            return []
        k.threat_alert = True
        return [f"▷{self.viewer}: きけんよち — {opp_name} は危険な技を持っていると察知！"]

    def on_enter(self, poke) -> List[str]:
        """ポケモンが場に出た（初見なら登場・タイプを記録）"""
        k = self._get(poke.name)
        if k.seen:
            return []
        k.seen = True
        k.type1 = poke.type1
        k.type2 = poke.type2
        t = poke.type1 + (f"/{poke.type2}" if poke.type2 else "")
        return [f"▷{self.viewer}: {poke.name} 登場（{t}タイプ）"]

    def on_move(self, poke_name: str, move_name: str) -> List[str]:
        """技を使った（初見なら記録）"""
        k = self._get(poke_name)
        if move_name in k.known_moves:
            return []
        k.known_moves.append(move_name)
        return [f"▷{self.viewer}: {poke_name} の技【{move_name}】を確認"]

    def on_item(self, poke_name: str, item: str, reason: str) -> List[str]:
        """持ち物が判明した"""
        k = self._get(poke_name)
        if k.known_item == item:
            return []
        k.known_item = item
        return [f"▷{self.viewer}: {poke_name} の持ち物【{item}】が判明（{reason}）"]

    def on_ability(self, poke_name: str, ability: str) -> List[str]:
        """特性が判明した"""
        k = self._get(poke_name)
        if k.known_ability == ability:
            return []
        k.known_ability = ability
        return [f"▷{self.viewer}: {poke_name} の特性【{ability}】が判明"]

    def on_hp_change(self, poke_name: str, cur_hp: int, max_hp: int,
                     damage: int = 0, move_name: Optional[str] = None,
                     attacker_name: Optional[str] = None) -> List[str]:
        """相手HPの残り割合を更新し、技による被ダメージ割合を記録する。
        実数（HP/最大HP）は開示せず、割合のみを観測情報として保持する。"""
        if max_hp <= 0:
            return []
        k = self._get(poke_name)
        k.hp_fraction = max(0.0, round(cur_hp / max_hp, 3))
        out = []
        if damage > 0 and move_name:
            frac = round(damage / max_hp, 3)
            k.damage_log.append({"move": move_name, "attacker": attacker_name, "fraction": frac})
            out.append(f"▷{self.viewer}: {poke_name} に {move_name} で 約{round(frac*100)}% 減少（残り約{round(k.hp_fraction*100)}%）")
        return out

    def get(self, name: str) -> Optional[PokeKnowledge]:
        return self.pokemon.get(name)

    def known_moves_of(self, name: str) -> List[str]:
        k = self.pokemon.get(name)
        return k.known_moves if k else []
