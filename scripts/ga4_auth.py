#!/usr/bin/env python3
"""
GA4認証スクリプト - ブラウザでGoogleアカウントにログインしてリフレッシュトークンを取得する
"""
import json
import os
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRET_FILE = os.path.join(os.path.dirname(__file__), "ga4_client_secret.json")
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

def main():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=SCOPES)
    creds = flow.run_local_server(port=8080, open_browser=True)

    print("\n認証成功！")
    print(f"Refresh Token: {creds.refresh_token[:30]}...")

    env_path = os.path.join(os.path.dirname(__file__), "../.env.local")
    lines = []
    if os.path.exists(env_path):
        with open(env_path) as f:
            lines = [l for l in f.readlines() if not l.startswith("GA4_REFRESH_TOKEN=")]

    lines.append(f"GA4_REFRESH_TOKEN={creds.refresh_token}\n")
    with open(env_path, "w") as f:
        f.writelines(lines)

    print(f"リフレッシュトークンを .env.local に保存しました")

if __name__ == "__main__":
    main()
