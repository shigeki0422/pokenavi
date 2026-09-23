"""ポケモン個別ページの「覚える技」セクション用データを生成する。

出力:
  src/data/learnsets.json    … {アイコンID: {"m": [技名, ...]（50音順）, "u": {技名: 採用率}}}
  src/data/move-details.json … {技名: {t,c,p,a,pp,e,en}}（learnsetに出る技のみ）

アイコンID(0681-00形式)はポケモン情報ページのdexNumber/imageFormと同じキー。
pokemon_learnsets テーブルは和名キーだが、フォーム表記がページ側
(「パンプジン（ちいさい）」)とDB側(「パンプジン(こだましゅ)」)で揺れるため、
public/builder-data/mon/*.json が持つ「アイコンID→DB和名」の対応を正本として使う
(party-builderの技プールと同じ集合になるため、ページと工房で食い違わない)。
"""
import json
import os
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "scripts" / "pokenavi.db"
MON_DIR = ROOT / "public" / "builder-data" / "mon"
OUT_DIR = ROOT / "src" / "data"

# mon/*.json の "n" がDBの pokemon_name と一致しないフォームの手当て。
# 0711-01 は「パンプジン (ちいさい)」名義でDBに行が無く、実体は「こだましゅ」。
NAME_ALIAS = {"0711-01": "パンプジン(こだましゅ)"}


def kana_key(s: str):
    """カタカナ→ひらがなに寄せた50音キー(濁点等はそのまま)。"""
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def title_en(slug: str) -> str:
    """PokeAPIのスラッグ(fire-punch)を表示用英名(Fire Punch)にする。"""
    if not slug:
        return ""
    if " " in slug or slug[:1].isupper():
        return slug
    return " ".join(w.capitalize() for w in slug.replace("_", "-").split("-"))


def main() -> int:
    if not DB.exists():
        print(f"[ERROR] DBが見つかりません: {DB}", file=sys.stderr)
        return 1
    con = sqlite3.connect(DB)

    learnsets: dict[str, dict] = {}
    used: set[str] = set()
    empty: list[str] = []

    for path in sorted(MON_DIR.glob("*.json")):
        icon = path.stem
        if "-" not in icon:
            continue  # 旧形式の残骸(711.json 等)は無視
        mon = json.loads(path.read_text(encoding="utf-8"))
        name = NAME_ALIAS.get(icon) or mon.get("n")
        moves = sorted(
            {r[0] for r in con.execute(
                "SELECT move_jp FROM pokemon_learnsets WHERE pokemon_name=?", (name,))},
            key=kana_key,
        )
        if not moves:
            empty.append(f"{icon} ({name})")
            continue
        # u: 一覧のどれが実戦で使われているかを示す採用率バッジ・採用率順ソート用。
        # mon/*.json ではなくDBの最新クロールから引く(mon/*.json は gen_builder_data.py を
        # 回した時点で止まり、同じページの「使用率データ」と数字がずれるため)。
        mset = set(moves)
        usage = {mv: rate for mv, rate in con.execute(
            "SELECT move, usage_rate FROM pokemon_moves WHERE pokemon=? AND rule='single' "
            "AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_moves "
            "WHERE pokemon=? AND rule='single')", (name, name)) if mv in mset}
        learnsets[icon] = {"m": moves, "u": usage}
        used.update(moves)

    details: dict[str, dict] = {}
    for name_jp, name_en, mtype, cat, power, acc, pp, effect in con.execute(
        "SELECT name_jp, name_en, type, category, power, accuracy, pp, effect_text FROM move_master"
    ):
        if name_jp not in used:
            continue
        d = {"t": mtype, "c": cat}
        if power:
            d["p"] = power
        if acc:
            d["a"] = acc
        if pp:
            d["pp"] = pp
        if effect:
            d["e"] = effect
        if name_en:
            d["en"] = title_en(name_en)
        details[name_jp] = d
    con.close()

    missing = sorted(used - set(details))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for fname, data in (("learnsets.json", learnsets), ("move-details.json", details)):
        (OUT_DIR / fname).write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        print(f"  {fname}: {len(data)}件 "
              f"({os.path.getsize(OUT_DIR / fname) / 1024:.0f}KB)")

    print(f"技の総数(ユニーク): {len(used)}")
    if empty:
        print(f"[WARN] learnsetが空のアイコン {len(empty)}件: {', '.join(empty)}")
    if missing:
        print(f"[WARN] move_masterに無い技 {len(missing)}件: {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
