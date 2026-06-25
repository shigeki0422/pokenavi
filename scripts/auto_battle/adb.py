"""
ADB操作ユーティリティ
crawl_champions.py から抽出・共通化
"""
import subprocess
import time
import numpy as np
from PIL import Image
import io


def run(cmd: str) -> str:
    r = subprocess.run(f"adb {cmd}", shell=True, capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")


def tap(x: int, y: int, wait: float = 0.5):
    run(f"shell input tap {x} {y}")
    time.sleep(wait)


def swipe(x1: int, y1: int, x2: int, y2: int, dur: int = 500, wait: float = 0.5):
    run(f"shell input swipe {x1} {y1} {x2} {y2} {dur}")
    time.sleep(wait)


def screenshot() -> np.ndarray:
    """スクリーンショットを numpy 配列 (H,W,3) BGR で返す"""
    import cv2
    raw = subprocess.run("adb exec-out screencap -p", shell=True, capture_output=True).stdout
    img = np.frombuffer(raw, dtype=np.uint8)
    return cv2.imdecode(img, cv2.IMREAD_COLOR)


def screenshot_pil() -> Image.Image:
    raw = subprocess.run("adb exec-out screencap -p", shell=True, capture_output=True).stdout
    return Image.open(io.BytesIO(raw)).convert("RGB")


def save_screenshot(path: str) -> np.ndarray:
    import cv2
    img = screenshot()
    cv2.imwrite(path, img)
    return img
