"""
自動対戦ドライバー（タイミングベース高速版）

スクリーンショットは最小限にとどめ、固定座標タップで COMMAND TIME 内に行動する。
フロー:
  ホーム → バトル → ランクバトル → シングル → マッチング → 選出 → [ターンループ] → 結果
"""
import time
import logging
import subprocess
import numpy as np
from typing import Optional

from . import adb, config as cfg
from .recorder import BattleRecorder
from .strategy import BattleStrategy

logger = logging.getLogger(__name__)

# COMMAND TIME は 7〜8 秒。スクリーンショット1枚 ≒ 1.5秒 かかるため
# ターン中のスクリーンショットは原則禁止。タイミングで制御する。
COMMAND_TIME    = 7.0   # 1ターンの制限時間(秒)
ACT_BY          = 4.0   # この秒数以内に行動を完了させる
ANIM_WAIT       = 2.5   # 技発動アニメーション待ち(秒)
TURN_POLL       = 0.3   # ターン開始検出ポーリング間隔(秒)


class BattleDriver:
    def __init__(
        self,
        strategy: BattleStrategy,
        recorder: BattleRecorder,
        max_battles: int = 30,
        inter_battle_wait: float = 5.0,
        select_slots: list[int] = None,   # 選出スロット番号 (0始まり)
    ):
        self.strategy = strategy
        self.recorder = recorder
        self.max_battles = max_battles
        self.inter_battle_wait = inter_battle_wait
        self.select_slots = select_slots or [0, 1, 2]

        self._battle_count = 0
        self._wins = 0
        self._losses = 0

    # ── メインループ ─────────────────────────────────────────

    def run(self):
        logger.info("自動対戦開始")
        try:
            while self._battle_count < self.max_battles:
                self._run_one_battle()
                logger.info(f"通算 {self._wins}勝 {self._losses}敗 ({self._battle_count}/{self.max_battles})")
                time.sleep(self.inter_battle_wait)
        except KeyboardInterrupt:
            logger.info("中断 (Ctrl+C)")
        logger.info(f"終了: {self._wins}勝 {self._losses}敗")

    # ── 1バトル ──────────────────────────────────────────────

    def _run_one_battle(self):
        self._battle_count += 1
        self.recorder.start_battle(self._battle_count, self.strategy.my_team)
        logger.info(f"=== バトル {self._battle_count} ===")

        self._navigate_to_match()
        if not self._wait_for_match():
            logger.warning("  マッチング失敗 → このバトルをスキップ")
            self.recorder.end_battle("skip")
            return
        self._do_selection()

        result = self._battle_loop()
        self.recorder.end_battle(result)
        if result == "win":
            self._wins += 1
        elif result == "lose":
            self._losses += 1
        self._dismiss_result()

    # ── ナビゲーション ────────────────────────────────────────

    def _navigate_to_match(self):
        """ホーム画面からマッチング開始まで"""
        logger.info("  ナビゲーション開始")
        adb.tap(*cfg.HOME_BATTLE_BTN,   wait=2.0)     # バトル
        adb.tap(*cfg.RANK_BATTLE_BTN,   wait=3.0)     # ランクバトル（NPC登場待ち）
        adb.tap(*cfg.SINGLE_BATTLE_BTN, wait=2.0)     # シングルバトル（NPC選択 or ボタン）
        adb.tap(*cfg.MATCH_START_BTN,   wait=1.0)     # マッチング開始
        logger.info("  マッチング開始")

    def _wait_for_match(self) -> bool:
        """マッチング成立を最大2分待つ。成立したらTrue、タイムアウトはFalse"""
        logger.info("  マッチング待機中...")
        for _ in range(120):
            time.sleep(1.0)
            try:
                screen = adb.screenshot()
                if self._is_selection_screen(screen):
                    logger.info("  マッチング成立")
                    return True
            except Exception:
                pass
        logger.warning("  マッチングタイムアウト")
        return False

    def _is_selection_screen(self, screen: np.ndarray) -> bool:
        """選出画面の簡易判定: 左側1/4に青/紫の縦リストがあるか"""
        roi = screen[:, :600, :]
        hsv_roi = __import__('cv2').cvtColor(roi, __import__('cv2').COLOR_BGR2HSV)
        mask = __import__('cv2').inRange(
            hsv_roi,
            np.array([100, 60, 80]),
            np.array([160, 255, 255])
        )
        return int(mask.sum() // 255) > 5000

    def _do_selection(self):
        """選出: 指定スロットを順にタップして確定"""
        logger.info(f"  選出 slots={self.select_slots}")
        time.sleep(0.5)
        for slot in self.select_slots:
            adb.tap(*cfg.PARTY_SLOTS[slot], wait=0.6)
        adb.tap(*cfg.SELECTION_CONFIRM_TAP, wait=2.0)

    # ── バトルループ ──────────────────────────────────────────

    def _battle_loop(self) -> str:
        """
        COMMAND TIMEが来たら「たたかう→技タップ」を繰り返す。
        勝敗はスクリーンショットで確認（アニメーション後の静止時に1枚）。
        """
        turn = 0
        max_turns = 100

        while turn < max_turns:
            # たたかう ボタンが出るまで短くポーリング
            time.sleep(TURN_POLL)

            # スクリーンショット1枚で状態確認（勝敗 or たたかうボタン）
            try:
                screen = adb.screenshot()
                result = self._check_result(screen)
                if result:
                    logger.info(f"  バトル終了: {result}")
                    return result

                if self._has_fight_btn(screen):
                    turn += 1
                    self._do_move(turn)
                    time.sleep(ANIM_WAIT)
                else:
                    # まだ演出中 or 相手ターン
                    time.sleep(0.8)
            except Exception as e:
                logger.debug(f"  loop error: {e}")
                time.sleep(1.0)

        return "unknown"

    def _has_fight_btn(self, screen: np.ndarray) -> bool:
        """「たたかう」ボタン（右下の紫丸）が存在するか"""
        import cv2
        # たたかうボタンは y=620-780, x=2050-2250 に表示される（実測）
        roi = screen[620:780, 2050:2250, :]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array([120, 60, 80]), np.array([170, 255, 255]))
        return int(mask.sum() // 255) > 500

    def _check_result(self, screen: np.ndarray) -> Optional[str]:
        """
        結果画面を検出。None=継続
        結果画面の特徴: 下部(y>900)に白い3ボタン行が横並びで出る
        (「対戦をやめる」「チームを編成する」「対戦を続ける」)
        """
        import cv2
        if self._has_fight_btn(screen):
            return None  # たたかうボタンが出ていればバトル継続中

        # 下部(y=940-1000, x=200-2200)の白ピクセルが多い → 結果画面の3ボタン行
        bottom = screen[940:1000, 200:2200]
        gray = cv2.cvtColor(bottom, cv2.COLOR_BGR2GRAY)
        white_px = int((gray > 210).sum())
        if white_px > 8000:
            # 勝敗の区別: 中央付近の金色(VP表示)があれば win、なければ lose
            center = screen[200:700, 700:1700]
            hsv_c = cv2.cvtColor(center, cv2.COLOR_BGR2HSV)
            gold = cv2.inRange(hsv_c, np.array([20,120,160]), np.array([35,255,255]))
            if int(gold.sum()//255) > 3000:
                return "win"
            return "lose"

        return None

    def _do_move(self, turn: int):
        """たたかう→技選択を素早く実行"""
        # シミュレータに聞かず、まず固定技（スロット0）を選択
        # 将来的には strategy.choose_move_idx() を使う
        chosen = 0

        adb.tap(*cfg.FIGHT_BTN_TAP, wait=0.4)   # たたかう
        adb.tap(*cfg.MOVE_TAPS[chosen], wait=0.3)  # 技

        self.recorder.record_turn(turn, "move", [], chosen, 1.0, 1.0)
        logger.info(f"  t{turn} → わざ{chosen+1}")

    # ── 結果画面クローズ ─────────────────────────────────────

    def _dismiss_result(self):
        time.sleep(3.0)
        # 「対戦を続ける」ボタン (右下) をタップしてホームに戻る
        # ボタンがなければ中央タップでメッセージ送り
        adb.tap(2000, 1000, wait=1.5)   # 対戦を続ける / 次へ
        adb.tap(1200,  540, wait=1.0)   # フォールバック
