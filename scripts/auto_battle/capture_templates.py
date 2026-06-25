"""
テンプレート画像収集ツール
各ゲーム状態の画面を撮影して templates/ に保存する

使い方:
  python -m scripts.auto_battle.capture_templates

キー操作 (Enterで撮影→保存、q/Ctrl+Cで終了):
  ゲームを目的の状態にしてからEnterを押す
"""
import os
import sys
import subprocess
import time

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

STATES = [
    ("move_select",   "技選択画面 (わざを選んでくださいが出ている状態)"),
    ("opponent_turn", "相手ターン中の画面"),
    ("win",           "勝利画面"),
    ("lose",          "敗北画面"),
    ("matchmaking",   "マッチング中の画面"),
    ("battle_start",  "バトル開始演出中の画面"),
    ("switch_select", "交代選択画面"),
    ("team_select",   "チーム選択画面"),
]

# テンプレートとして使う部分領域 (None = 全画面)
# 全画面より「特徴的なUI部分だけ」を切り出した方がマッチングが安定する
CROP_HINT = {
    "move_select":   (0, 750, 2400, 980),   # 技ボタンエリア
    "opponent_turn": (800, 0, 1600, 200),   # 相手ターン表示エリア
    "win":           (700, 300, 1700, 700),
    "lose":          (700, 300, 1700, 700),
    "matchmaking":   (700, 400, 1700, 700),
    "battle_start":  (700, 400, 1700, 700),
    "switch_select": (0,   300, 2400, 980),
    "team_select":   (0,   0,   2400, 500),
}


def capture_one(key: str, desc: str):
    path = os.path.join(TEMPLATE_DIR, f"{key}.png")
    print(f"\n[{key}] {desc}")
    print(f"  ゲームを上記状態にしてから Enter を押してください (スキップ: s+Enter)")
    line = input("  > ").strip().lower()
    if line == "s":
        print("  スキップ")
        return

    import cv2
    import numpy as np

    raw = subprocess.run("adb exec-out screencap -p", shell=True, capture_output=True).stdout
    img_arr = np.frombuffer(raw, dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    if img is None:
        print("  ! スクリーンショット取得失敗 (adb devices で接続確認)")
        return

    crop = CROP_HINT.get(key)
    if crop:
        x1, y1, x2, y2 = crop
        img = img[y1:y2, x1:x2]

    cv2.imwrite(path, img)
    print(f"  保存: {path} ({img.shape[1]}x{img.shape[0]})")


def main():
    print("=== テンプレート収集ツール ===")
    print(f"保存先: {TEMPLATE_DIR}")
    for key, desc in STATES:
        path = os.path.join(TEMPLATE_DIR, f"{key}.png")
        if os.path.exists(path):
            ans = input(f"[{key}] は既に存在します。上書きしますか? (y/N): ").strip().lower()
            if ans != "y":
                continue
        capture_one(key, desc)
    print("\n完了。templates/ に保存されたテンプレートでマッチングが行われます。")
    print("ずれがあれば config.py の CROP_HINT または TEMPLATE_THRESH を調整してください。")


if __name__ == "__main__":
    main()
