"""
ポケモンチャンピオンズ 使用率ランキング クローラー（全件）
・詳細→バックでリストはn+1位が最下段になる（n>=4）
・n<=3はトップ(1-5位)に戻る
・slot_for_rank()でスクロール不要のナビゲーション

【止まる原因と対策】
- adbサイレント失敗: stderr をログに出力
- screencap空ファイル: サイズ検証＋リトライ
- どこで止まったか不明: タイムスタンプ＋経過秒ログ
- 再開ポイント: last_rank.txt に最後に完了したrankを保存
"""

import subprocess
import time
import os
import hashlib
import sys
from datetime import date
from PIL import Image

OUTPUT_DIR    = f"/Users/shigeki/work/pokenavi/crawl_data/champ_crawl_{date.today().isoformat()}"
TOTAL_POKEMON = 200

LIST_X        = 1600
LIST_ENTRY_Y  = [350, 482, 614, 746, 878]

PANEL_X       = 1200
PANEL_BOT     = 720
ARROW_RIGHT   = (2330, 540)
ARROW_LEFT    = (70, 540)
BACK_BTN      = (308, 49)

PANELS = ["move"]
PANEL_MAX_SCROLL = {"move": 0, "item": 1, "partner": 1, "nature": 1, "ev": 8, "ability": 0}

PROGRESS_FILE = f"{OUTPUT_DIR}/last_rank.txt"


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def adb(cmd, check=False):
    result = subprocess.run(f"adb {cmd}", shell=True, capture_output=True, text=True)
    if result.returncode != 0 and check:
        log(f"⚠️ adb失敗: adb {cmd}")
        log(f"   stderr: {result.stderr.strip()}")
    return result


def check_adb():
    result = adb("devices")
    lines = [l for l in result.stdout.strip().splitlines() if "device" in l and "List" not in l]
    if not lines:
        log("❌ ADB接続なし。デバイスを確認してください。")
        sys.exit(1)
    log(f"ADB接続OK: {lines[0].split()[0]}")


def tap(x, y, wait=1.0):
    adb(f"shell input tap {x} {y}", check=True)
    time.sleep(wait)


def swipe(x1, y1, x2, y2, dur=800, wait=1.0):
    adb(f"shell input swipe {x1} {y1} {x2} {y2} {dur}", check=True)
    time.sleep(wait)


def screenshot(path, retries=3):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    for attempt in range(retries):
        subprocess.run(f"adb exec-out screencap -p > {path}", shell=True)
        size = os.path.getsize(path) if os.path.exists(path) else 0
        if size > 50_000:
            return True
        log(f"⚠️ screencap異常({size}bytes, attempt {attempt+1}/{retries}): {os.path.basename(path)}")
        time.sleep(1.5)
    log(f"❌ screencap失敗(3回リトライ後): {path}")
    return False


def img_hash(path):
    img = Image.open(path).crop((900, 200, 1600, 900))
    return hashlib.md5(img.tobytes()).hexdigest()


def scroll_to_top():
    for _ in range(8):
        swipe(LIST_X, 400, LIST_X, 800, 600, wait=0.4)


def slot_for_rank(rank):
    return rank - 1 if rank <= 4 else 4


def capture_panel(save_dir, panel):
    max_s = PANEL_MAX_SCROLL.get(panel, 1)
    hashes = []
    for page in range(max_s + 1):
        path = f"{save_dir}/{panel}_{page:02d}.png"
        time.sleep(0.8)
        ok = screenshot(path)
        if not ok:
            break
        h = img_hash(path)
        if h in hashes:
            os.remove(path)
            break
        hashes.append(h)
        if page < max_s:
            if panel == "ev":
                swipe(PANEL_X, PANEL_BOT, PANEL_X, PANEL_BOT - 320, 800, wait=0.8)
            else:
                swipe(PANEL_X, PANEL_BOT, PANEL_X, PANEL_BOT - 400, 400, wait=0.5)
    return len(hashes)


def crawl_detail(rank):
    save_dir = f"{OUTPUT_DIR}/detail/{rank:03d}"
    os.makedirs(save_dir, exist_ok=True)
    counts = {}
    for i, panel in enumerate(PANELS):
        n = capture_panel(save_dir, panel)
        counts[panel] = n
        if i < len(PANELS) - 1:
            tap(*ARROW_RIGHT, wait=1.0)
    return counts


def save_progress(rank):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(rank))


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log(f"保存先: {OUTPUT_DIR}")
    check_adb()

    scroll_to_top()
    time.sleep(1)

    for rank in range(1, TOTAL_POKEMON + 1):
        slot = slot_for_rank(rank)
        t0 = time.time()
        log(f"[{rank:3d}位] slot={slot} 開始")
        tap(LIST_X, LIST_ENTRY_Y[slot], wait=2.0)

        counts = crawl_detail(rank)
        elapsed = time.time() - t0
        log(f"[{rank:3d}位] 完了 {elapsed:.0f}s {counts}")

        save_progress(rank)
        tap(*BACK_BTN, wait=2.0)

    log(f"完了: {TOTAL_POKEMON}件")


if __name__ == "__main__":
    main()
