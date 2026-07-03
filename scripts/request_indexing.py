#!/usr/bin/env python3
"""
Google Indexing API でURLをインデックス登録リクエストする。
使用例:
  # 特定URL
  python3 scripts/request_indexing.py https://pokenavi.jp/blog/garchomp-analysis-m3/

  # 全ブログ記事（公開済みのみ）
  python3 scripts/request_indexing.py --all-posts

  # サイトマップ全URL
  python3 scripts/request_indexing.py --sitemap
"""
import sys
import re
import glob
import os
import json
import time
import argparse
import urllib.request
import requests

SITE_BASE = "https://pokenavi.jp"
BLOG_DIR  = os.path.join(os.path.dirname(__file__), "..", "src", "content", "blog")
DAILY_LIMIT = 200
ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env.local")
SECRET_PATH = os.path.join(os.path.dirname(__file__), "ga4_client_secret.json")


def get_access_token():
    refresh_token = os.environ.get("GA4_REFRESH_TOKEN")
    if not refresh_token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GA4_REFRESH_TOKEN="):
                    refresh_token = line.split("=", 1)[1]
                    break

    if not refresh_token:
        raise RuntimeError("GA4_REFRESH_TOKEN が見つかりません。ga4_auth.py で再認証してください。")

    with open(SECRET_PATH) as f:
        secret = json.load(f)["installed"]

    resp = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": secret["client_id"],
        "client_secret": secret["client_secret"],
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    })
    resp.raise_for_status()
    return resp.json()["access_token"]


def notify(access_token, url, action="URL_UPDATED"):
    resp = requests.post(
        "https://indexing.googleapis.com/v3/urlNotifications:publish",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"url": url, "type": action},
    )
    resp.raise_for_status()
    return resp.json()


def get_published_blog_urls():
    urls = []
    for path in sorted(glob.glob(os.path.join(BLOG_DIR, "*.md"))):
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if "draft: true" in content:
            continue
        slug = os.path.basename(path).replace(".md", "")
        urls.append(f"{SITE_BASE}/blog/{slug}/")
    return urls


def get_sitemap_urls():
    sitemap_url = f"{SITE_BASE}/sitemap-0.xml"
    try:
        with urllib.request.urlopen(sitemap_url, timeout=10) as r:
            xml = r.read().decode()
        return re.findall(r"<loc>(https?://[^<]+)</loc>", xml)
    except Exception as e:
        print(f"[ERROR] サイトマップ取得失敗: {e}")
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="*", help="送信するURL")
    parser.add_argument("--all-posts", action="store_true", help="公開済みブログ記事を全件送信")
    parser.add_argument("--sitemap",   action="store_true", help="サイトマップ全URLを送信")
    args = parser.parse_args()

    if args.all_posts:
        urls = get_published_blog_urls()
    elif args.sitemap:
        urls = get_sitemap_urls()
    else:
        urls = args.urls

    if not urls:
        print("URLを指定してください。")
        parser.print_help()
        sys.exit(1)

    urls = urls[:DAILY_LIMIT]
    access_token = get_access_token()

    ok, ng = 0, 0
    for url in urls:
        try:
            result = notify(access_token, url)
            notify_time = result.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "")
            print(f"[OK] {url}  →  {notify_time}")
            ok += 1
        except Exception as e:
            print(f"[NG] {url}  →  {e}")
            ng += 1
        time.sleep(0.5)

    print(f"\n完了: {ok}件成功 / {ng}件失敗")


if __name__ == "__main__":
    main()
