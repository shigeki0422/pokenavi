"""
ポケナビ クローラー実行スクリプト
使い方:
    python3 scripts/crawl.py              # 全ソース・全ルール
    python3 scripts/crawl.py --source pokedb
    python3 scripts/crawl.py --source gamewith --limit 20
    python3 scripts/crawl.py --season M-1
"""
import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from db import init_db
from crawlers.pokedb import crawl_season as pokedb_crawl
from crawlers.gamewith import crawl_season as gamewith_crawl


def main():
    parser = argparse.ArgumentParser(description="ポケナビ データ収集")
    parser.add_argument("--source",  choices=["pokedb", "gamewith", "all"], default="all")
    parser.add_argument("--season",  default="M-2", help="シーズン名 例: M-1, M-2")
    parser.add_argument("--rule",    choices=["single", "double", "all"], default="single")
    parser.add_argument("--limit",   type=int, default=None, help="クロール上限（テスト用）")
    args = parser.parse_args()

    # DB初期化（テーブルがなければ作成）
    init_db()

    rules_pokedb = []
    rules_gamewith = []
    if args.rule in ("single", "all"):
        rules_pokedb.append(0)
        rules_gamewith.append("single")
    if args.rule in ("double", "all"):
        rules_pokedb.append(1)
        rules_gamewith.append("double")

    if args.source in ("pokedb", "all"):
        print(f"\n▶ pokedb クロール開始 (season={args.season})")
        pokedb_crawl(season=args.season, rules=rules_pokedb, limit=args.limit)

    if args.source in ("gamewith", "all"):
        print(f"\n▶ gamewith クロール開始")
        gamewith_crawl(rules=rules_gamewith, limit=args.limit)

    print("\n✅ クロール完了")


if __name__ == "__main__":
    main()
