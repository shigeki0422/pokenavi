"""完全movepool取り込み: 各環境ポケモンのPokeAPI movepoolを pokemon_learnsets に投入。
使用率駆動learnsetの取りこぼし(物理/ニッチ技。例ボルテッカー/ひっくりかえす)を一掃する根治策。
PokeAPIのmove slug を move_master.name_en(=slug形式)で name_jp に突合し、move_masterに在る技のみ追加
(=Championsに在る技に限定。main-seriesのサブセット近似)。INSERT OR IGNOREで使用率backfillと共存。
スラッグ解決は pokemon_base_stats.pokeapi_name(英字)→それ / 数値/空→dex。キャッシュ .pokeapi_moves_cache.json。
"""
import sys, os, json, sqlite3, urllib.request, time
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "pokenavi.db"
CACHE = ROOT / ".pokeapi_moves_cache.json"
UA = {"User-Agent": "pokenavi-bot/1.0"}

def slug_for(dex, pokeapi_name):
    if pokeapi_name and any(ch.isalpha() and ch.isascii() for ch in pokeapi_name):
        return pokeapi_name
    return str(dex)

def fetch_moves(slug, cache):
    if slug in cache:
        return cache[slug]
    try:
        req = urllib.request.Request(f"https://pokeapi.co/api/v2/pokemon/{slug}", headers=UA)
        d = json.load(urllib.request.urlopen(req, timeout=25))
        moves = sorted({m["move"]["name"] for m in d.get("moves", [])})
    except Exception as e:
        moves = {"_error": str(e)}
        moves = []
    cache[slug] = moves
    CACHE.write_text(json.dumps(cache, ensure_ascii=False))
    return moves

def main():
    dry = "--dry" in sys.argv
    c = sqlite3.connect(DB)
    en2jp = {en: jp for jp, en in c.execute("SELECT name_jp, name_en FROM move_master WHERE name_en IS NOT NULL AND name_en<>''")}
    rows = c.execute("SELECT DISTINCT pokemon_name, dex_number, pokeapi_name FROM pokemon_base_stats").fetchall()
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    added = 0; nofetch = []; per = {}
    t0 = time.time()
    for i, (name, dex, papi) in enumerate(rows):
        slug = slug_for(dex, papi)
        moves = fetch_moves(slug, cache)
        if not moves:
            nofetch.append((name, slug)); continue
        jp_moves = {en2jp[m] for m in moves if m in en2jp}
        before = added
        for mv in jp_moves:
            if dry:
                exists = c.execute("SELECT 1 FROM pokemon_learnsets WHERE pokemon_name=? AND move_jp=?", (name, mv)).fetchone()
                if not exists: added += 1
            else:
                c.execute("INSERT OR IGNORE INTO pokemon_learnsets(pokemon_name, move_jp) VALUES(?,?)", (name, mv))
                added += c.execute("SELECT changes()").fetchone()[0]
        per[name] = added - before
        if (i + 1) % 40 == 0:
            print(f"  {i+1}/{len(rows)} 処理 (+{added}技) {time.time()-t0:.0f}秒", flush=True)
    if not dry:
        c.commit()
    top = sorted(per.items(), key=lambda x: -x[1])[:10]
    print(f"\n{'[DRY]' if dry else ''} 取り込み完了: {len(rows)}種 / 追加{added}件 / fetch失敗{len(nofetch)}種 {time.time()-t0:.0f}秒", flush=True)
    if nofetch: print("fetch失敗:", nofetch[:15], flush=True)
    print("追加が多い種top10:", top, flush=True)
    c.close()

if __name__ == "__main__":
    main()
