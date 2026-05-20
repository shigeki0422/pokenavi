"""
ポケナビ データベース定義
SQLiteを使用してポケモンチャンピオンズの対戦データを蓄積する
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "pokenavi.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()

    # ポケモン使用率ランキング
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_usage (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,  -- 'single' / 'double'
            rank        INTEGER NOT NULL,
            pokemon     TEXT    NOT NULL,
            pokemon_id  TEXT,
            usage_rate  REAL,
            source      TEXT    NOT NULL,  -- 'pokedb' / 'gamewith'
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, rank, source)
        )
    """)

    # 技採用率
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_moves (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,
            pokemon     TEXT    NOT NULL,
            rank        INTEGER NOT NULL,
            move        TEXT    NOT NULL,
            usage_rate  REAL    NOT NULL,
            source      TEXT    NOT NULL,
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source)
        )
    """)

    # 持ち物採用率
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_items (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,
            pokemon     TEXT    NOT NULL,
            rank        INTEGER NOT NULL,
            item        TEXT    NOT NULL,
            usage_rate  REAL    NOT NULL,
            source      TEXT    NOT NULL,
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source)
        )
    """)

    # 特性採用率
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_abilities (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,
            pokemon     TEXT    NOT NULL,
            rank        INTEGER NOT NULL,
            ability     TEXT    NOT NULL,
            usage_rate  REAL    NOT NULL,
            source      TEXT    NOT NULL,
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source)
        )
    """)

    # 性格採用率
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_natures (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,
            pokemon     TEXT    NOT NULL,
            rank        INTEGER NOT NULL,
            nature      TEXT    NOT NULL,
            usage_rate  REAL    NOT NULL,
            source      TEXT    NOT NULL,
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source)
        )
    """)

    # 努力値配分採用率
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_evs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,
            pokemon     TEXT    NOT NULL,
            rank        INTEGER NOT NULL,
            ev_spread   TEXT    NOT NULL,
            usage_rate  REAL    NOT NULL,
            source      TEXT    NOT NULL,
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source)
        )
    """)

    # 一緒に使われるポケモン（同居率）
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_partners (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            season      TEXT    NOT NULL,
            rule        TEXT    NOT NULL,
            pokemon     TEXT    NOT NULL,
            rank        INTEGER NOT NULL,
            partner     TEXT    NOT NULL,
            source      TEXT    NOT NULL,
            crawled_at  TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source)
        )
    """)

    # クロールログ
    c.execute("""
        CREATE TABLE IF NOT EXISTS crawl_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            crawled_at  TEXT    NOT NULL,
            source      TEXT    NOT NULL,
            url         TEXT    NOT NULL,
            season      TEXT,
            rule        TEXT,
            pokemon     TEXT,
            status      TEXT    NOT NULL,  -- 'success' / 'error' / 'skip'
            message     TEXT
        )
    """)

    conn.commit()
    conn.close()
    print(f"DB初期化完了: {DB_PATH}")


if __name__ == "__main__":
    init_db()
