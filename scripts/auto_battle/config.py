"""
画面座標・領域の設定 (実測値: 2400x1080 横持ち)
"""

# ── 画面サイズ ──────────────────────────────────────────────
SCREEN_W = 2400
SCREEN_H = 1080

# ── ホーム画面ナビゲーション ────────────────────────────────
HOME_BATTLE_BTN      = (1416, 452)   # ホーム「バトル」ボタン
RANK_BATTLE_BTN      = (1800, 125)   # バトルメニュー「ランクバトル」(実測)
SINGLE_BATTLE_BTN    = (1800, 437)   # シングルバトル (実測)
MATCH_START_BTN      = (1800, 900)   # マッチング開始 (実測)

# ── 選出画面 ────────────────────────────────────────────────
PARTY_SLOTS = [
    (300, 195),   # slot 1
    (300, 295),   # slot 2
    (300, 395),   # slot 3
    (300, 495),   # slot 4
    (300, 595),   # slot 5
    (300, 695),   # slot 6
]
SELECTION_CONFIRM_TAP = (430, 1020)

# ── バトル画面 ──────────────────────────────────────────────
FIGHT_BTN_TAP  = (2130, 670)    # 「たたかう」(実測)
SWITCH_BTN_TAP = (2130, 850)    # 「ポケモン」(交代)(実測)
OBSERVE_BTN_TAP = (2200, 200)   # 「様子を見る」
MEGA_BTN_TAP   = (1200, 530)    # メガシンカ

# 技ボタン4つ（右側縦並び、実測）
MOVE_TAPS = [
    (2030, 290),   # わざ1
    (2030, 400),   # わざ2
    (2030, 510),   # わざ3
    (2030, 620),   # わざ4
]

# チーム確定・結果画面
TEAM_CONFIRM_TAP = (1200, 950)
RESULT_TAP       = (1200, 900)

# ── テンプレートマッチング ──────────────────────────────────
TEMPLATE_THRESH = 0.80
import os
_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(_DIR, "templates")
TEMPLATES = {
    "move_select":    os.path.join(TEMPLATE_DIR, "move_select.png"),
    "opponent_turn":  os.path.join(TEMPLATE_DIR, "opponent_turn.png"),
    "win":            os.path.join(TEMPLATE_DIR, "win.png"),
    "lose":           os.path.join(TEMPLATE_DIR, "lose.png"),
    "matchmaking":    os.path.join(TEMPLATE_DIR, "matchmaking.png"),
    "battle_start":   os.path.join(TEMPLATE_DIR, "battle_start.png"),
    "switch_select":  os.path.join(TEMPLATE_DIR, "switch_select.png"),
    "team_select":    os.path.join(TEMPLATE_DIR, "team_select.png"),
}

# ── HP/名前領域（スクリーンショット使用時のみ）──────────────
MY_NAME_REGION    = (50,   980, 600, 1050)
MY_HP_BAR_REGION  = (50,  1030, 600, 1060)
OPP_NAME_REGION   = (1700,  20, 2350,   80)
OPP_HP_BAR_REGION = (1700,  80, 2350,  120)
MOVE_REGIONS      = [
    (1700, 240, 2380, 340),
    (1700, 350, 2380, 450),
    (1700, 460, 2380, 560),
    (1700, 570, 2380, 670),
]
MOVE_TEXT_REGIONS = MOVE_REGIONS
HP_GREEN  = ([40, 120, 40],  [100, 255, 100])
HP_YELLOW = ([40, 180, 180], [100, 255, 255])
HP_RED    = ([40, 40, 150],  [100, 100, 255])
