import subprocess
import time
import os
import hashlib
from datetime import date
from PIL import Image

OUTPUT_DIR    = "/tmp/champ_crawl_2026-06-17"
START_RANK    = 131
END_RANK      = 150

LIST_X        = 1600
LIST_ENTRY_Y  = [350, 482, 614, 746, 878]
PANEL_X       = 1200
PANEL_BOT     = 720
ARROW_RIGHT   = (2330, 540)
BACK_BTN      = (308, 49)

PANELS = ["move", "item", "partner", "nature", "ev", "ability"]
PANEL_MAX_SCROLL = {"move": 1, "item": 1, "partner": 1, "nature": 1, "ev": 8, "ability": 0}

def adb(cmd):
    subprocess.run(f"adb {cmd}", shell=True, capture_output=True)

def tap(x, y, wait=1.0):
    adb(f"shell input tap {x} {y}")
    time.sleep(wait)

def swipe(x1, y1, x2, y2, dur=800, wait=1.0):
    adb(f"shell input swipe {x1} {y1} {x2} {y2} {dur}")
    time.sleep(wait)

def screenshot(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    subprocess.run(f"adb exec-out screencap -p > {path}", shell=True)

def img_hash(path):
    img = Image.open(path).crop((900, 200, 1600, 900))
    return hashlib.md5(img.tobytes()).hexdigest()

def slot_for_rank(rank):
    return rank - 1 if rank <= 4 else 4

def capture_panel(save_dir, panel):
    max_s = PANEL_MAX_SCROLL.get(panel, 1)
    hashes = []
    for page in range(max_s + 1):
        path = f"{save_dir}/{panel}_{page:02d}.png"
        time.sleep(0.8)
        screenshot(path)
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

def main():
    print("3秒後に開始します。先に戻るボタンでリストに戻ってください...")
    time.sleep(3)

    for rank in range(START_RANK, END_RANK + 1):
        slot = slot_for_rank(rank)
        print(f"[{rank:3d}位] slot={slot}", end=" ", flush=True)
        tap(LIST_X, LIST_ENTRY_Y[slot], wait=2.0)
        counts = crawl_detail(rank)
        print({p: counts[p] for p in PANELS})
        tap(*BACK_BTN, wait=2.0)

    print(f"\n完了: {START_RANK}〜{END_RANK}位")

if __name__ == "__main__":
    main()
