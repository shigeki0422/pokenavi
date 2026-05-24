"""
ポケナビ データベース定義
SQLiteを使用してポケモンチャンピオンズの対戦データを日付単位で蓄積する
"""
import sqlite3
from pathlib import Path
from datetime import date

DB_PATH = Path(__file__).parent / "pokenavi.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def today() -> str:
    return date.today().isoformat()  # "YYYY-MM-DD"


def _create_tables(c: sqlite3.Cursor):
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_usage (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            pokemon      TEXT    NOT NULL,
            pokemon_id   TEXT,
            usage_rate   REAL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_moves (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            pokemon      TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            move         TEXT    NOT NULL,
            usage_rate   REAL    NOT NULL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_items (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            pokemon      TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            item         TEXT    NOT NULL,
            usage_rate   REAL    NOT NULL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_abilities (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            pokemon      TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            ability      TEXT    NOT NULL,
            usage_rate   REAL    NOT NULL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_natures (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            pokemon      TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            nature       TEXT    NOT NULL,
            usage_rate   REAL    NOT NULL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_evs (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            pokemon      TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            ev_spread    TEXT    NOT NULL,
            ev_h         INTEGER NOT NULL DEFAULT 0,
            ev_a         INTEGER NOT NULL DEFAULT 0,
            ev_b         INTEGER NOT NULL DEFAULT 0,
            ev_c         INTEGER NOT NULL DEFAULT 0,
            ev_d         INTEGER NOT NULL DEFAULT 0,
            ev_s         INTEGER NOT NULL DEFAULT 0,
            usage_rate   REAL    NOT NULL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_partners (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            season       TEXT    NOT NULL,
            rule         TEXT    NOT NULL,
            pokemon      TEXT    NOT NULL,
            rank         INTEGER NOT NULL,
            partner      TEXT    NOT NULL,
            source       TEXT    NOT NULL,
            crawled_date TEXT    NOT NULL,
            crawled_at   TEXT    NOT NULL,
            UNIQUE(season, rule, pokemon, rank, source, crawled_date)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS crawl_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            crawled_at  TEXT    NOT NULL,
            source      TEXT    NOT NULL,
            url         TEXT    NOT NULL,
            season      TEXT,
            rule        TEXT,
            pokemon     TEXT,
            status      TEXT    NOT NULL,
            message     TEXT
        )
    """)


def _migrate(conn: sqlite3.Connection):
    """スキーママイグレーション"""
    c = conn.cursor()

    # 旧スキーマ（crawled_dateなし）→ 再作成
    data_tables = [
        "pokemon_usage", "pokemon_moves", "pokemon_items",
        "pokemon_abilities", "pokemon_natures", "pokemon_evs", "pokemon_partners",
    ]
    dropped = []
    for table in data_tables:
        cols = {row[1] for row in c.execute(f"PRAGMA table_info({table})")}
        if not cols or "crawled_date" in cols:
            continue
        c.execute(f"DROP TABLE {table}")
        dropped.append(table)

    if dropped:
        conn.commit()
        _create_tables(c)
        conn.commit()
        print(f"  スキーマ更新（再作成）: {', '.join(dropped)}")
        print("  ※ 旧データは削除されました。再クロールしてください。")

    # pokemon_evs に ev_h/a/b/c/d/s 列を追加（なければ）
    cols = {row[1] for row in c.execute("PRAGMA table_info(pokemon_evs)")}
    for col in ("ev_h", "ev_a", "ev_b", "ev_c", "ev_d", "ev_s"):
        if col not in cols:
            c.execute(f"ALTER TABLE pokemon_evs ADD COLUMN {col} INTEGER NOT NULL DEFAULT 0")
            print(f"  pokemon_evs に {col} 列を追加")
    conn.commit()


def init_db():
    conn = get_conn()
    c = conn.cursor()
    _create_tables(c)
    conn.commit()
    _migrate(conn)
    conn.close()
    print(f"DB初期化完了: {DB_PATH}")


if __name__ == "__main__":
    init_db()
