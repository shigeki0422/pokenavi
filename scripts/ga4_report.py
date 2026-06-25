#!/usr/bin/env python3
"""
GA4 日次レポートスクリプト
使い方: python3 scripts/ga4_report.py [--days 7]
"""
import json
import os
import sys
import argparse
import requests
from datetime import datetime, timedelta


ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env.local")
SECRET_PATH = os.path.join(os.path.dirname(__file__), "ga4_client_secret.json")
PROPERTY_ID = "541423641"


def load_credentials():
    env = {}
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env[k] = v

    with open(SECRET_PATH) as f:
        secret = json.load(f)["installed"]

    return env["GA4_REFRESH_TOKEN"], secret["client_id"], secret["client_secret"]


def get_access_token(refresh_token, client_id, client_secret):
    resp = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    })
    resp.raise_for_status()
    return resp.json()["access_token"]


def run_report(access_token, body, silent=False):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.post(
        f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport",
        headers=headers, json=body
    )
    if not resp.ok:
        return None
    return resp.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7)
    args = parser.parse_args()

    refresh_token, client_id, client_secret = load_credentials()
    access_token = get_access_token(refresh_token, client_id, client_secret)

    today = datetime.now().strftime("%Y-%m-%d")
    start_date = f"{args.days}daysAgo"

    print(f"\n{'='*60}")
    print(f"  ポケナビ GA4 レポート（過去{args.days}日間）  {today}")
    print(f"{'='*60}\n")

    # 1. ページ別アクセス
    data = run_report(access_token, {
        "dateRanges": [{"startDate": start_date, "endDate": "today"}],
        "dimensions": [{"name": "pagePath"}],
        "metrics": [
            {"name": "sessions"},
            {"name": "screenPageViews"},
            {"name": "averageSessionDuration"},
            {"name": "bounceRate"},
        ],
        "limit": 15,
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]
    })

    print(f"【ページ別アクセス TOP15】")
    print(f"{'ページ':<45} {'セッション':>8} {'PV':>6} {'平均滞在(秒)':>12} {'直帰率':>8}")
    print("-" * 83)
    for row in data.get("rows", []):
        path = row["dimensionValues"][0]["value"][:44]
        sessions = row["metricValues"][0]["value"]
        pv = row["metricValues"][1]["value"]
        duration = float(row["metricValues"][2]["value"])
        bounce = float(row["metricValues"][3]["value"]) * 100
        print(f"{path:<45} {sessions:>8} {pv:>6} {duration:>12.0f} {bounce:>7.1f}%")

    # 2. 流入元
    data2 = run_report(access_token, {
        "dateRanges": [{"startDate": start_date, "endDate": "today"}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "sessions"}, {"name": "newUsers"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]
    })

    print(f"\n【流入チャネル別】")
    print(f"{'チャネル':<30} {'セッション':>10} {'新規ユーザー':>12}")
    print("-" * 55)
    for row in data2.get("rows", []):
        channel = row["dimensionValues"][0]["value"]
        sessions = row["metricValues"][0]["value"]
        new_users = row["metricValues"][1]["value"]
        print(f"{channel:<30} {sessions:>10} {new_users:>12}")

    # 3. デバイス別
    data3 = run_report(access_token, {
        "dateRanges": [{"startDate": start_date, "endDate": "today"}],
        "dimensions": [{"name": "deviceCategory"}],
        "metrics": [{"name": "sessions"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]
    })

    print(f"\n【デバイス別】")
    print(f"{'デバイス':<20} {'セッション':>10}")
    print("-" * 32)
    for row in data3.get("rows", []):
        device = row["dimensionValues"][0]["value"]
        sessions = row["metricValues"][0]["value"]
        print(f"{device:<20} {sessions:>10}")

    # 4. 検索クエリ（Search Console連携がある場合）
    data4 = run_report(access_token, {
        "dateRanges": [{"startDate": start_date, "endDate": "today"}],
        "dimensions": [{"name": "pageReferrer"}],
        "metrics": [{"name": "sessions"}],
        "dimensionFilter": {
            "filter": {
                "fieldName": "sessionDefaultChannelGroup",
                "stringFilter": {"value": "Organic Search"}
            }
        },
        "limit": 10,
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]
    })

    print(f"\n【オーガニック検索 流入元ページ TOP10】")
    print(f"{'参照元':<60} {'セッション':>10}")
    print("-" * 72)
    for row in data4.get("rows", []):
        referrer = row["dimensionValues"][0]["value"][:59]
        sessions = row["metricValues"][0]["value"]
        print(f"{referrer:<60} {sessions:>10}")

    # 5. サマリー
    data5 = run_report(access_token, {
        "dateRanges": [
            {"startDate": start_date, "endDate": "today"},
            {"startDate": f"{args.days*2}daysAgo", "endDate": f"{args.days+1}daysAgo"},
        ],
        "metrics": [
            {"name": "sessions"},
            {"name": "activeUsers"},
            {"name": "screenPageViews"},
            {"name": "averageSessionDuration"},
        ],
    })

    rows = data5.get("rows", [{}])
    if rows:
        cur = rows[0]["metricValues"] if rows else None
        prev = rows[1]["metricValues"] if len(rows) > 1 else None

        print(f"\n【サマリー（前期間比較）】")
        metrics = ["セッション", "アクティブユーザー", "ページビュー", "平均滞在時間(秒)"]
        for i, name in enumerate(metrics):
            cur_val = float(cur[i]["value"]) if cur else 0
            prev_val = float(prev[i]["value"]) if prev else 0
            if prev_val > 0:
                diff = (cur_val - prev_val) / prev_val * 100
                arrow = "▲" if diff > 0 else "▼"
                print(f"  {name:<20}: {cur_val:>8.0f}  ({arrow}{abs(diff):.1f}%)")
            else:
                print(f"  {name:<20}: {cur_val:>8.0f}")

    # 6. Search Console 検索クエリ
    data6 = run_report(access_token, {
        "dateRanges": [{"startDate": start_date, "endDate": "today"}],
        "dimensions": [{"name": "searchConsoleQuery"}],
        "metrics": [
            {"name": "searchConsoleClicks"},
            {"name": "searchConsoleImpressions"},
            {"name": "searchConsoleCtr"},
            {"name": "searchConsoleAveragePosition"},
        ],
        "orderBys": [{"metric": {"metricName": "searchConsoleClicks"}, "desc": True}],
        "limit": 20,
    })

    print(f"\n【検索クエリ TOP20（Search Console）】")
    print(f"{'クエリ':<40} {'クリック':>8} {'表示':>8} {'CTR':>8} {'平均順位':>8}")
    print("-" * 78)
    if data6 and data6.get("rows"):
        for row in data6["rows"]:
            query = row["dimensionValues"][0]["value"][:39]
            clicks = int(float(row["metricValues"][0]["value"]))
            impr = int(float(row["metricValues"][1]["value"]))
            ctr = float(row["metricValues"][2]["value"]) * 100
            pos = float(row["metricValues"][3]["value"])
            print(f"{query:<40} {clicks:>8} {impr:>8} {ctr:>7.1f}% {pos:>8.1f}")
    else:
        print("  データなし（連携後24〜48時間で反映されます）")

    # 7. Search Console ランディングページ別
    data7 = run_report(access_token, {
        "dateRanges": [{"startDate": start_date, "endDate": "today"}],
        "dimensions": [{"name": "searchConsoleLandingPagePath"}],
        "metrics": [
            {"name": "searchConsoleClicks"},
            {"name": "searchConsoleImpressions"},
            {"name": "searchConsoleAveragePosition"},
        ],
        "orderBys": [{"metric": {"metricName": "searchConsoleClicks"}, "desc": True}],
        "limit": 15,
    })

    print(f"\n【検索流入 着地ページ TOP15（Search Console）】")
    print(f"{'ページ':<50} {'クリック':>8} {'表示':>8} {'平均順位':>8}")
    print("-" * 78)
    if data7 and data7.get("rows"):
        for row in data7["rows"]:
            path = row["dimensionValues"][0]["value"][:49]
            clicks = int(float(row["metricValues"][0]["value"]))
            impr = int(float(row["metricValues"][1]["value"]))
            pos = float(row["metricValues"][2]["value"])
            print(f"{path:<50} {clicks:>8} {impr:>8} {pos:>8.1f}")
    else:
        print("  データなし（連携後24〜48時間で反映されます）")

    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()
