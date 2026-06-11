#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GameWithの全わざ一覧をスクレイピングして、DBと比較する
"""
import urllib.request
import re
import sqlite3
import json
from pathlib import Path

URL = "https://gamewith.jp/pokemon-champions/546417"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")

# HTMLから技データを含む部分を抽出
# スクリプトタグのJSONデータを探す
json_matches = re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"JSON blocks found: {len(json_matches)}")

# テキスト全体から技名パターンを探す
# 技名が2回繰り返され、その後に数値が続くパターン
# 例: タネマシンガンタネマシンガン2510020弾
raw_text = re.sub(r'<[^>]+>', '', html)

# ページ内の全技データセクションを探す
# 技名の前にはタイプがある: でんき でんき など
# 構造確認
with open("/tmp/gamewith_raw.txt", "w", encoding="utf-8") as f:
    f.write(raw_text)

print(f"Raw text length: {len(raw_text)}")
print("Saved to /tmp/gamewith_raw.txt")
