#!/usr/bin/env python3
"""持ち物（アイテム）仕様マスタの付録生成（move_master/ability_master と同構造）。

- 環境出現アイテム（pokemon_items の DISTINCT）を権威リストとする。
- 効果文は gamewith ポケモンチャンピオンズ持ち物一覧 + REQUIREMENTS.md を真実源として seed。
- メガストーン（〜ナイト/ナイトＸ/ナイトＹ）は一律機構（endswith判定）で実装されるため
  カテゴリ MEGA としてまとめ、共通効果文を持たせる。
- 実装状況は simulator/*.py のコード参照から判定（メガ石は機構実装済み＝True）。
- item_master テーブル（name_jp/effect_text/implemented/category）に保存し appendix_c.md を生成。
"""
import sqlite3
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/
DB = ROOT / "pokenavi.db"

MEGA_EFFECT = "対応するポケモンがバトル中にメガシンカできる。"


def is_mega(name: str) -> bool:
    return name.endswith("ナイト") or name.endswith("ナイトＸ") or name.endswith("ナイトＹ")


# 非メガ環境アイテムの効果文（真実源）
EFFECTS = {
    # タイプ強化（×1.2）
    "もくたん": "ほのおタイプの技の威力が1.2倍になる。",
    "とけないこおり": "こおりタイプの技の威力が1.2倍になる。",
    "しんぴのしずく": "みずタイプの技の威力が1.2倍になる。",
    "じしゃく": "でんきタイプの技の威力が1.2倍になる。",
    "くろいメガネ": "あくタイプの技の威力が1.2倍になる。",
    "ようせいのハネ": "フェアリータイプの技の威力が1.2倍になる。",
    "どくバリ": "どくタイプの技の威力が1.2倍になる。",
    "やわらかいすな": "じめんタイプの技の威力が1.2倍になる。",
    "するどいくちばし": "ひこうタイプの技の威力が1.2倍になる。",
    "シルクのスカーフ": "ノーマルタイプの技の威力が1.2倍になる。",
    "りゅうのキバ": "ドラゴンタイプの技の威力が1.2倍になる。",
    "くろおび": "かくとうタイプの技の威力が1.2倍になる。",
    "まがったスプーン": "エスパータイプの技の威力が1.2倍になる。",
    "のろいのおふだ": "ゴーストタイプの技の威力が1.2倍になる。",
    "メタルコート": "はがねタイプの技の威力が1.2倍になる。",
    "かたいいし": "いわタイプの技の威力が1.2倍になる。",
    "ぎんのこな": "むしタイプの技の威力が1.2倍になる。",
    "きせきのタネ": "くさタイプの技の威力が1.2倍になる。",
    "でんきだま": "ピカチュウが持つとでんきタイプの技の威力が2倍になる。",
    # HP回復
    "たべのこし": "ターン終わりに最大HPの1/16回復する。",
    "オボンのみ": "HPが最大HPの1/2以下になった時、最大HPの1/4回復する。1度使うと無くなる。",
    "オレンのみ": "HPが最大HPの1/2以下になった時、10回復する。1度使うと無くなる。",
    "かいがらのすず": "技でダメージを与えた時、そのダメージの1/8自分のHPを回復する。",
    # 状態異常回復きのみ
    "ラムのみ": "状態異常・こんらん状態を回復する。1度使うと無くなる。",
    "カゴのみ": "ねむり状態を回復する。1度使うと無くなる。",
    "モモンのみ": "どく・もうどく状態を回復する。1度使うと無くなる。",
    "チーゴのみ": "やけど状態を回復する。1度使うと無くなる。",
    "ヒメリのみ": "PPが0になった技のPPを10回復する。1度使うと無くなる。",
    # タイプ半減きのみ（効果バツグン被弾時ダメージ半減）
    "オッカのみ": "ほのおタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "イトケのみ": "みずタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ソクノのみ": "でんきタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "リンドのみ": "くさタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ヤチェのみ": "こおりタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ヨプのみ": "かくとうタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ビアーのみ": "どくタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "シュカのみ": "じめんタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "バコウのみ": "ひこうタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ウタンのみ": "エスパータイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "タンガのみ": "むしタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ヨロギのみ": "いわタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "カシブのみ": "ゴーストタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ハバンのみ": "ドラゴンタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ナモのみ": "あくタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "リリバのみ": "はがねタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ロゼルのみ": "フェアリータイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる。",
    "ホズのみ": "ノーマルタイプの技で受けるダメージを常に半減する。1度使うと無くなる。",
    # 耐久・補正・その他
    "きあいのタスキ": "HPが満タンの時、一撃でひんしになる技のダメージを受けてもHPを1残して耐える。1度使うと無くなる。",
    "きあいのハチマキ": "ひんしになる技のダメージを受けると10%の確率でHPを1残して耐える。",
    "せんせいのツメ": "20%の確率で同じ優先度の技の中で先制できる。",
    "ひかりのこな": "相手の技の命中率が0.9倍になる。",
    "こだわりスカーフ": "素早さが1.5倍になるが、同じ技しか出せなくなる。",
    "しろいハーブ": "能力の低下を1度だけ回復する。1度使うと無くなる。",
    "メンタルハーブ": "メロメロ・ちょうはつ・連続不可・わざふうじ・かいふくふうじ・アンコール状態を回復する。1度使うと無くなる。",
    "おうじゃのしるし": "技でダメージを与えた時、10%の確率で相手をひるませる。",
    "ピントレンズ": "急所に当たりやすくなる（急所ランク+1）。",
}


def implemented_items(all_names) -> set:
    """simulator/*.py のコード中にアイテム名が文字列リテラルで現れる＝実装/参照ありとみなす。
    メガストーンは endswith 機構で一律実装されるため category=MEGA は実装済み扱い。"""
    src = ""
    for f in glob.glob(str(ROOT / "simulator" / "*.py")):
        if f.endswith("generate_appendix_c.py"):
            continue
        for line in open(f, encoding="utf-8"):
            if line.lstrip().startswith("#"):
                continue
            src += line
    impl = set()
    for n in all_names:
        if is_mega(n):
            impl.add(n)  # メガシンカ機構（endswith）で一律対応
        elif f'"{n}"' in src or f"'{n}'" in src:
            impl.add(n)
    return impl


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    items = [r[0] for r in cur.execute(
        "SELECT DISTINCT item FROM pokemon_items WHERE season='M-2' AND rule='single' "
        "ORDER BY item").fetchall()]

    impl = implemented_items(items)

    cur.execute("""CREATE TABLE IF NOT EXISTS item_master (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_jp TEXT NOT NULL UNIQUE,
        effect_text TEXT,
        category TEXT NOT NULL DEFAULT 'item',
        implemented INTEGER NOT NULL DEFAULT 0
    )""")
    for name in items:
        cat = "mega" if is_mega(name) else "item"
        eff = MEGA_EFFECT if cat == "mega" else EFFECTS.get(name, "")
        cur.execute("""INSERT INTO item_master (name_jp, effect_text, category, implemented)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(name_jp) DO UPDATE SET effect_text=excluded.effect_text,
                category=excluded.category, implemented=excluded.implemented""",
                    (name, eff, cat, 1 if name in impl else 0))
    conn.commit()

    n_mega = sum(1 for i in items if is_mega(i))
    n_nonmega = len(items) - n_mega
    n_impl = sum(1 for i in items if i in impl)
    n_eff = sum(1 for i in items if (is_mega(i) or EFFECTS.get(i)))

    rows = []
    for name in items:
        if is_mega(name):
            continue  # メガ石は本文末でまとめ
        mark = "✅" if name in impl else "—"
        eff = EFFECTS.get(name, "（効果未取得・要確認）")
        rows.append(f"| {name} | {mark} | {eff} |")

    mega_names = [i for i in items if is_mega(i)]
    out = f"""# 付録C. 持ち物（アイテム）一覧

> **ソース**: 環境出現アイテムは `pokemon_items` の DISTINCT（M-2 single で {len(items)}種、うちメガストーン {n_mega}種）。
> 効果文は gamewith ポケモンチャンピオンズ持ち物一覧 + REQUIREMENTS.md を真実源とする。
> **実装**: ✅ = `simulator/*.py` で効果を確認（実装済み {n_impl}/{len(items)}）。メガストーンは endswith 機構で一律対応。
> **注意**: effect_text を仕様の真実源とし、`item_deep_audit.py` でテスト網羅を監査する。

## 非メガアイテム（{n_nonmega}種）

| アイテム | 実装 | 効果（仕様） |
|------|------|------|
{chr(10).join(rows)}

## メガストーン（{n_mega}種・共通効果）

{MEGA_EFFECT}（endswith「ナイト/ナイトＸ/ナイトＹ」で一律判定。道具奪取・交換・はたきおとすは無効）

{', '.join(mega_names)}
"""
    (ROOT / "simulator" / "appendix_c.md").write_text(out, encoding="utf-8")
    conn.close()
    print(f"アイテム総数: {len(items)}（非メガ{n_nonmega}/メガ{n_mega}）/ 実装: {n_impl} / 効果収録: {n_eff}")
    print(f"出力: {ROOT / 'simulator' / 'appendix_c.md'}")


if __name__ == "__main__":
    main()
