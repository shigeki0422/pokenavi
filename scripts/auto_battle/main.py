"""
自動対戦 エントリーポイント

使い方:
  python -m scripts.auto_battle.main --team ガブリアス ミミッキュ カイリュー --battles 50

事前準備:
  1. scripts/auto_battle/templates/ に各状態のスクリーンショット画像を配置
  2. config.py の座標をキャリブレーション
  3. pip install opencv-python pytesseract pillow
     + Tesseract本体 + 日本語データ (brew install tesseract tesseract-lang)
"""
import argparse
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

from .strategy import BattleStrategy
from .recorder import BattleRecorder
from .battle_driver import BattleDriver


def main():
    parser = argparse.ArgumentParser(description="ポケモンチャンピオンズ 自動対戦")
    parser.add_argument("--team",    nargs="+", default=["ガブリアス", "ミミッキュ", "カイリュー"],
                        help="使用ポケモン名（先頭が場に出る）")
    parser.add_argument("--battles", type=int, default=30, help="対戦回数")
    parser.add_argument("--depth",   type=int, default=2,  help="シミュレータ探索深さ")
    parser.add_argument("--logdir",  default="/tmp",        help="ログ出力ディレクトリ")
    parser.add_argument("--calibrate", action="store_true",
                        help="座標確認モード: スクリーンショットを撮って領域描画して終了")
    args = parser.parse_args()

    if args.calibrate:
        _run_calibrate()
        return

    my_team = [{"name": n} for n in args.team]
    strategy = BattleStrategy(my_team)
    recorder = BattleRecorder(log_dir=args.logdir)
    driver   = BattleDriver(strategy, recorder, max_battles=args.battles)
    driver.run()


def _run_calibrate():
    """デバッグ用: スクリーンショットを撮って設定領域を重ねた画像を保存"""
    from . import adb
    from .vision import save_regions_debug
    import os

    print("スクリーンショット撮影中...")
    screen = adb.screenshot()
    if screen is None:
        print("ADB接続を確認してください (adb devices)")
        return
    out = "/tmp/calibrate_debug.png"
    save_regions_debug(screen, out)
    print(f"保存先: {out} — 領域がずれていたら config.py を修正してください")


if __name__ == "__main__":
    main()
