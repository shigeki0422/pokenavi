"""
シミュレータ連携 - 技・交代選択インターフェース
HeuristicAI + DataLoader を使って実戦判断を行う
"""
import sys
import os
import random
import logging
from typing import Optional

logger = logging.getLogger(__name__)

_sim_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, _sim_dir)

try:
    from simulator.data import DataLoader
    from simulator.battle import BattleField, BattleSide, Action
    from simulator.pokemon import BattlePokemon, build_from_template
    from simulator.ai import HeuristicAI, expected_damage
    _SIM_AVAILABLE = True
except ImportError as e:
    logger.warning(f"simulator import failed: {e}")
    _SIM_AVAILABLE = False


class BattleStrategy:
    """
    実戦バトルの戦略クラス。
    HeuristicAI を BattleSide/BattleField に乗せて技・交代を決定する。
    シミュレータが使えない場合はランダムフォールバック。

    my_team: [{"name": "ガブリアス", "item": "ガブリアスナイト"}, ...]
    season:  使用率データのシーズン（最多採用技・持ち物のベース）
    """

    def __init__(self, my_team: list[dict], season: str = "M-2"):
        self.my_team = my_team
        self.season = season
        self._ai = HeuristicAI() if _SIM_AVAILABLE else None
        self._dl = DataLoader() if _SIM_AVAILABLE else None

        # 自分の BattleSide（シミュレータ内部状態）
        self._my_side: Optional["BattleSide"] = None
        self._opp_side: Optional["BattleSide"] = None
        self._field = BattleField() if _SIM_AVAILABLE else None

    # ── バトル開始時に呼ぶ ──────────────────────────────────

    def init_battle(self, my_active_name: str, opp_active_name: Optional[str] = None):
        """
        バトル開始時にシミュレータの内部状態を初期化。
        my_active_name: 先頭に出すポケモン名
        opp_active_name: 相手の先頭（わかれば渡す。None で汎用ポケモンを仮置き）
        """
        if not _SIM_AVAILABLE:
            return

        my_pokemons = [self._load_poke(e["name"]) for e in self.my_team if e.get("name")]
        if not my_pokemons:
            return

        # 先頭を my_active_name に並べ替え
        idx = next((i for i, p in enumerate(my_pokemons) if p.name == my_active_name), 0)
        my_pokemons.insert(0, my_pokemons.pop(idx))

        opp_poke = self._load_poke(opp_active_name) if opp_active_name else self._dummy_opp("相手")
        opp_team = [opp_poke]

        self._my_side  = BattleSide(my_pokemons,  viewer_label="me")
        self._opp_side = BattleSide(opp_team, viewer_label="opp")
        self._field    = BattleField()

    # ── ターン毎の技選択 ────────────────────────────────────

    def choose_move_idx(
        self,
        move_names: list[str],
        my_hp: float,
        opp_name: Optional[str],
        opp_hp: float,
    ) -> int:
        """
        技スロットインデックス (0-3) を返す。
        move_names: OCR で読んだ技名リスト（空文字は無効スロット）
        my_hp / opp_hp: HPバーから読んだ比率 (0.0〜1.0)
        """
        valid = [i for i, m in enumerate(move_names) if m.strip()]
        if not valid:
            return 0

        if not _SIM_AVAILABLE or self._my_side is None:
            return self._fallback_move(valid, move_names, my_hp)

        try:
            # シミュレータ内部 HP を実測値に同期
            self._sync_hp(my_hp, opp_hp, opp_name)

            action = self._ai(self._my_side, self._opp_side, self._field)

            if action.type == "move" and action.move is not None:
                # シミュレータが選んだ技名で move_names から対応スロットを探す
                chosen_name = action.move.name_jp
                for i in valid:
                    if move_names[i].strip() == chosen_name:
                        return i
                # 名前が見つからなければ期待ダメージ最大のスロットを返す
                return self._best_dmg_slot(valid, move_names)

            if action.type == "switch":
                # 交代指示の場合でも技選択が求められているなら最善技を返す
                return self._best_dmg_slot(valid, move_names)

        except Exception as e:
            logger.warning(f"AI error: {e}")

        return self._fallback_move(valid, move_names, my_hp)

    def choose_switch_slot(self, party_alive: list[bool]) -> int:
        """交代先スロット (0-5)。生きているポケモンの中で最もマッチアップスコアが高い控えを選ぶ"""
        if not _SIM_AVAILABLE or self._my_side is None:
            alive = [i for i, a in enumerate(party_alive) if a and i != 0]
            return alive[0] if alive else 0

        try:
            opp = self._opp_side.active
            benched = [
                (i, p) for i, p in enumerate(self._my_side.party)
                if p.is_alive and i != self._my_side.active_idx
            ]
            if not benched:
                return 0
            from simulator.ai import _matchup_score
            best_i = max(benched, key=lambda ip: _matchup_score(ip[1], opp))[0]
            return best_i
        except Exception as e:
            logger.warning(f"choose_switch error: {e}")
            alive = [i for i, a in enumerate(party_alive) if a and i != 0]
            return alive[0] if alive else 0

    # ── 内部ユーティリティ ────────────────────────────────

    def _load_poke(self, name: str) -> "BattlePokemon":
        tpl = self._dl.get_pokemon_template(name, season=self.season) if self._dl else None
        if tpl is None:
            return self._dummy_opp(name)
        return build_from_template(tpl, self._dl, randomize=False)

    def _dummy_opp(self, name: str) -> "BattlePokemon":
        """シミュレータ用の最低限ダミー BattlePokemon"""
        from simulator.data import MoveData
        p = BattlePokemon(
            name=name, type1="ノーマル", type2=None,
            hp=160, attack=100, defense=100,
            sp_attack=100, sp_defense=100, speed=100,
            ability="", item=None,
            moves=[],
            nature="まじめ", ev_h=16, ev_a=16, ev_b=16, ev_c=16, ev_d=16, ev_s=16,
        )
        return p

    def _sync_hp(self, my_hp: float, opp_hp: float, opp_name: Optional[str]):
        """HPバー読み取り値をシミュレータ内部に反映"""
        me = self._my_side.active
        me.hp = max(1, int(me.max_hp * my_hp))

        opp = self._opp_side.active
        # 相手ポケモンが変わっていたら差し替え
        if opp_name and opp.name != opp_name:
            new_opp = self._load_poke(opp_name)
            self._opp_side.party[self._opp_side.active_idx] = new_opp
            opp = new_opp
        opp.hp = max(1, int(opp.max_hp * opp_hp))

    def _best_dmg_slot(self, valid: list[int], move_names: list[str]) -> int:
        """OCR技名をDBで引いて期待ダメージ最大のスロットを返す"""
        me  = self._my_side.active
        opp = self._opp_side.active
        best_i, best_dmg = valid[0], -1.0
        for i in valid:
            mv = self._dl.get_move(move_names[i].strip()) if move_names[i].strip() else None
            if mv is None:
                continue
            dmg = expected_damage(me, opp, mv, self._field)
            if dmg > best_dmg:
                best_dmg, best_i = dmg, i
        return best_i

    def _fallback_move(self, valid: list[int], move_names: list[str], my_hp: float) -> int:
        """シミュレータ不使用時の簡易選択"""
        priority_moves = {"ねこだまし", "マッハパンチ", "バレットパンチ", "しんそく", "アクアジェット"}
        if my_hp < 0.3:
            for i in valid:
                if move_names[i] in priority_moves:
                    return i
        return random.choice(valid)

    def notify_ko(self, my_poke_fainted: bool, opp_poke_fainted: bool):
        """ひんし発生をシミュレータ内部状態に通知"""
        if not _SIM_AVAILABLE:
            return
        if my_poke_fainted and self._my_side:
            self._my_side.active.hp = 0
        if opp_poke_fainted and self._opp_side:
            self._opp_side.active.hp = 0

    def notify_my_switch(self, new_slot: int):
        """自分の交代を内部状態に通知"""
        if self._my_side and 0 <= new_slot < len(self._my_side.party):
            self._my_side.active_idx = new_slot
