"""
画像認識モジュール
OpenCV テンプレートマッチング + pytesseract OCR
"""
import os
import re
import numpy as np
import cv2
from enum import Enum, auto
from typing import Optional
from . import config as cfg


class GameState(Enum):
    UNKNOWN        = auto()
    MATCHMAKING    = auto()   # マッチング待ち
    TEAM_SELECT    = auto()   # チーム選択
    BATTLE_START   = auto()   # バトル開始演出
    MOVE_SELECT    = auto()   # 技選択
    SWITCH_SELECT  = auto()   # 交代選択
    OPPONENT_TURN  = auto()   # 相手ターン処理中
    WIN            = auto()   # 勝利
    LOSE           = auto()   # 敗北
    RESULT_WAIT    = auto()   # 結果後 次へ待ち


# ── テンプレート読み込みキャッシュ ────────────────────────────
_tmpl_cache: dict[str, Optional[np.ndarray]] = {}


def _load_template(key: str) -> Optional[np.ndarray]:
    if key not in _tmpl_cache:
        path = cfg.TEMPLATES.get(key, "")
        if os.path.exists(path):
            _tmpl_cache[key] = cv2.imread(path)
        else:
            _tmpl_cache[key] = None
    return _tmpl_cache[key]


def match_template(screen: np.ndarray, key: str, thresh: float = cfg.TEMPLATE_THRESH) -> bool:
    """テンプレートが画面に存在するか"""
    tmpl = _load_template(key)
    if tmpl is None:
        return False
    result = cv2.matchTemplate(screen, tmpl, cv2.TM_CCOEFF_NORMED)
    _, maxval, _, _ = cv2.minMaxLoc(result)
    return maxval >= thresh


def detect_state(screen: np.ndarray) -> GameState:
    """
    画面からゲーム状態を判定。
    テンプレート画像があればそちらを優先。なければピクセル色ヒューリスティックにフォールバック。
    """
    checks = [
        (GameState.WIN,           "win"),
        (GameState.LOSE,          "lose"),
        (GameState.SWITCH_SELECT, "switch_select"),
        (GameState.MOVE_SELECT,   "move_select"),
        (GameState.OPPONENT_TURN, "opponent_turn"),
        (GameState.BATTLE_START,  "battle_start"),
        (GameState.TEAM_SELECT,   "team_select"),
        (GameState.MATCHMAKING,   "matchmaking"),
    ]
    # テンプレートが1枚以上存在する場合のみテンプレートマッチングを使う
    has_any_template = any(_load_template(k) is not None for _, k in checks)
    if has_any_template:
        for state, key in checks:
            if match_template(screen, key):
                return state
        return GameState.UNKNOWN

    return _detect_state_by_color(screen)


def _detect_state_by_color(screen: np.ndarray) -> GameState:
    """
    テンプレートなし時のフォールバック: 特定ピクセル領域の色で状態を推定。
    ゲーム UI の色は比較的安定しているため簡易判定に使える。
    正確な座標は calibrate モードで確認して config.py を調整すること。
    """
    h, w = screen.shape[:2]

    def mean_bgr(x1, y1, x2, y2):
        roi = screen[y1:y2, x1:x2]
        return roi.mean(axis=(0, 1)) if roi.size else np.zeros(3)

    # 技ボタンエリア (y=780〜960) の明るさ: ボタンが表示されていると白っぽい
    move_area = mean_bgr(1200, 780, 2380, 960)
    move_area_bright = float(move_area.mean()) > 180

    # 画面中央上 (勝利/敗北テキストが出る領域) の赤み・青み
    center_top = mean_bgr(700, 200, 1700, 500)
    is_reddish  = float(center_top[2]) > 180 and float(center_top[0]) < 100  # BGR: B低R高
    is_bluish   = float(center_top[0]) > 150 and float(center_top[2]) < 100

    if is_reddish:
        return GameState.WIN
    if is_bluish:
        return GameState.LOSE
    if move_area_bright:
        return GameState.MOVE_SELECT

    return GameState.UNKNOWN


# ── OCR ──────────────────────────────────────────────────────

def _crop(img: np.ndarray, region: tuple) -> np.ndarray:
    x1, y1, x2, y2 = region
    return img[y1:y2, x1:x2]


def _ocr_region(img: np.ndarray, region: tuple) -> str:
    """指定領域をOCR（pytesseract）"""
    try:
        import pytesseract
    except ImportError:
        return ""
    crop = _crop(img, region)
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, binarized = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 日本語認識
    text = pytesseract.image_to_string(
        binarized,
        lang="jpn",
        config="--psm 7 --oem 3",
    )
    return text.strip()


def read_move_names(screen: np.ndarray) -> list[str]:
    """技名4つをOCRで読む（空欄はempty string）"""
    return [_ocr_region(screen, r) for r in cfg.MOVE_TEXT_REGIONS]


def read_pokemon_name(screen: np.ndarray, region: tuple) -> str:
    return _ocr_region(screen, region)


# ── HP バー読み取り ─────────────────────────────────────────

def _hp_ratio_from_bar(screen: np.ndarray, region: tuple) -> float:
    """HP バー領域の色から残りHP割合を推定 (0.0〜1.0)"""
    crop = _crop(screen, region)
    h, w = crop.shape[:2]
    # 赤・黄・緑のマスク合計で「HPバー全幅」「残りピクセル数」を計算
    def mask_ratio(lower, upper):
        lo = np.array(lower, dtype=np.uint8)
        hi = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(crop, lo, hi)
        return np.count_nonzero(mask)

    total = w * h
    filled = (mask_ratio(*cfg.HP_GREEN)
              + mask_ratio(*cfg.HP_YELLOW)
              + mask_ratio(*cfg.HP_RED))
    if total == 0:
        return 1.0
    return min(filled / total, 1.0)


def read_my_hp(screen: np.ndarray) -> float:
    return _hp_ratio_from_bar(screen, cfg.MY_HP_BAR_REGION)


def read_opp_hp(screen: np.ndarray) -> float:
    return _hp_ratio_from_bar(screen, cfg.OPP_HP_BAR_REGION)


# ── キャリブレーション補助 ─────────────────────────────────

def save_regions_debug(screen: np.ndarray, out_path: str = "/tmp/debug_regions.png"):
    """設定済み領域を矩形で描画してデバッグ用に保存"""
    vis = screen.copy()
    for reg in cfg.MOVE_TEXT_REGIONS:
        x1, y1, x2, y2 = reg
        cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(vis, cfg.MY_HP_BAR_REGION[:2], cfg.MY_HP_BAR_REGION[2:], (0, 0, 255), 2)
    cv2.rectangle(vis, cfg.OPP_HP_BAR_REGION[:2], cfg.OPP_HP_BAR_REGION[2:], (255, 0, 0), 2)
    cv2.imwrite(out_path, vis)
    print(f"debug image saved: {out_path}")
