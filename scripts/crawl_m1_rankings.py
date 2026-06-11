"""
M-1ランクマ上位構築記事クロール
https://gamewith.jp/pokemon-champions/560474 のJSバンドルからデータ取得
"""
import sys, os, re, json, sqlite3, requests
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), 'pokenavi.db')
JS_URL = 'https://gamewith-tool.s3.ap-northeast-1.amazonaws.com/assets/js/pokemon-champions-top-builds.min.js'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://gamewith.jp/pokemon-champions/560474',
}


def fetch_js():
    # バージョン番号を取得するため元ページも確認
    page_res = requests.get('https://gamewith.jp/pokemon-champions/560474', headers=HEADERS, timeout=15)
    m = re.search(r'top-builds\.min\.js\?(\d+)', page_res.text)
    ver = m.group(1) if m else '5'
    url = f'{JS_URL}?{ver}'
    print(f'JS URL: {url}')
    res = requests.get(url, headers=HEADERS, timeout=30)
    res.raise_for_status()
    return res.text


def extract_json_array(js, pos):
    q = js.find("'", pos) + 1
    buf = []
    i = q
    while i < len(js):
        c = js[i]
        if c == '\\':
            buf.append(js[i:i+2])
            i += 2
        elif c == "'":
            break
        else:
            buf.append(c)
            i += 1
    return ''.join(buf)


def parse_masters(js):
    # 性格 ss=[...]
    idx = js.find('ss=[{id:"-1"')
    ctx = js[idx:idx+3000]
    raw = re.search(r'ss=(\[.*?\])', ctx, re.DOTALL)
    fixed = re.sub(r'(\{|,)\s*([a-zA-Z_]+)\s*:', r'\1"\2":', raw.group(1))
    natures = {n['id']: n['n'] for n in json.loads(fixed)}

    def find_pos(keyword):
        return js.find(keyword)

    pokemon_pos = find_pos("JSON.parse('[{\"id\":\"-1\",\"n\":\"不明\",\"i\":\"\",\"a\":")
    item_pos    = find_pos("JSON.parse('[{\"id\":\"0\",\"n\":\"なし\",\"i\":\"i_item\"}")
    ability_pos = find_pos("JSON.parse('[{\"id\":\"-1\",\"n\":\"不明\"},{\"id\":\"1\",\"n\":\"アイスボディ\"}")
    move_pos    = find_pos("JSON.parse('[{\"id\":\"0\",\"n\":\"なし\",\"t\":\"\"}")

    pokemon   = {p['id']: p['n'] for p in json.loads(extract_json_array(js, pokemon_pos))}
    items     = {i['id']: i['n'] for i in json.loads(extract_json_array(js, item_pos))}
    abilities = {a['id']: a['n'] for a in json.loads(extract_json_array(js, ability_pos))}
    moves     = {m['id']: m['n'] for m in json.loads(extract_json_array(js, move_pos))}

    return {'pokemon': pokemon, 'items': items, 'abilities': abilities, 'natures': natures, 'moves': moves}


def parse_rankings(js):
    pos = js.find("JSON.parse('[{\"un\":")
    return json.loads(extract_json_array(js, pos))


def decode_entry(entry, masters):
    def decode_party(po):
        result = []
        for p in po:
            result.append({
                'pokemon': masters['pokemon'].get(str(p['id']), f'不明({p["id"]})'),
                'item': masters['items'].get(str(p.get('i', '')), '不明'),
                'nature': masters['natures'].get(str(p.get('na', -1)), '不明'),
                'ability': masters['abilities'].get(str(p.get('a', '')), '不明'),
                'moves': [masters['moves'].get(str(m), f'技{m}') for m in p.get('mo', [])],
                'evs_raw': p.get('e', []),
            })
        return result

    return {
        'rank': int(entry['r']),
        'username': entry['un'],
        'user_id': entry.get('ui', ''),
        'season': entry['s'],
        'score': entry.get('p', ''),
        'url': entry.get('url', ''),
        'twitter': entry.get('tw', ''),
        'youtube': entry.get('yt', ''),
        'twitch': entry.get('tc', ''),
        'party': decode_party(entry.get('po', [])),
    }


def init_db(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS m1_rankings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rank INTEGER,
        username TEXT,
        user_id TEXT,
        season TEXT,
        score TEXT,
        url TEXT,
        twitter TEXT,
        youtube TEXT,
        twitch TEXT,
        crawled_date TEXT,
        UNIQUE(user_id, season)
    );

    CREATE TABLE IF NOT EXISTS m1_party (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ranking_id INTEGER REFERENCES m1_rankings(id),
        slot INTEGER,
        pokemon TEXT,
        item TEXT,
        nature TEXT,
        ability TEXT,
        move1 TEXT, move2 TEXT, move3 TEXT, move4 TEXT,
        ev_h INTEGER, ev_a INTEGER, ev_b INTEGER, ev_c INTEGER, ev_d INTEGER, ev_s INTEGER
    );
    """)
    con.commit()


def save_to_db(con, entries, crawled_date):
    inserted = 0
    updated = 0

    for e in entries:
        cur = con.execute("""
            INSERT INTO m1_rankings (rank, username, user_id, season, score, url, twitter, youtube, twitch, crawled_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_id, season) DO UPDATE SET
                rank=excluded.rank, score=excluded.score, url=excluded.url,
                twitter=excluded.twitter, youtube=excluded.youtube, twitch=excluded.twitch,
                crawled_date=excluded.crawled_date
        """, (e['rank'], e['username'], e['user_id'], e['season'],
              e['score'], e['url'], e['twitter'], e['youtube'], e['twitch'], crawled_date))

        rid = cur.lastrowid or con.execute(
            "SELECT id FROM m1_rankings WHERE user_id=? AND season=?",
            (e['user_id'], e['season'])
        ).fetchone()[0]

        if cur.rowcount == 1:
            inserted += 1
        else:
            updated += 1
            con.execute("DELETE FROM m1_party WHERE ranking_id=?", (rid,))

        for slot, p in enumerate(e['party']):
            evs = p['evs_raw']
            ev = [evs[i] if i < len(evs) else 0 for i in range(6)]
            con.execute("""
                INSERT INTO m1_party (ranking_id, slot, pokemon, item, nature, ability,
                    move1, move2, move3, move4, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (rid, slot, p['pokemon'], p['item'], p['nature'], p['ability'],
                  p['moves'][0] if len(p['moves']) > 0 else '',
                  p['moves'][1] if len(p['moves']) > 1 else '',
                  p['moves'][2] if len(p['moves']) > 2 else '',
                  p['moves'][3] if len(p['moves']) > 3 else '',
                  ev[0], ev[1], ev[2], ev[3], ev[4], ev[5]))

    con.commit()
    return inserted, updated


def main():
    print('=== M-1ランクマ上位構築クロール ===')

    print('JSバンドル取得中...')
    js = fetch_js()
    print(f'  取得完了 ({len(js):,} bytes)')

    print('マスターデータ解析中...')
    masters = parse_masters(js)
    print(f'  ポケモン:{len(masters["pokemon"])} アイテム:{len(masters["items"])} '
          f'特性:{len(masters["abilities"])} 性格:{len(masters["natures"])} 技:{len(masters["moves"])}')

    print('ランキングデータ解析中...')
    raw_rankings = parse_rankings(js)
    entries = [decode_entry(e, masters) for e in raw_rankings]
    entries.sort(key=lambda x: x['rank'])

    with_url   = sum(1 for e in entries if e['url'])
    with_party = sum(1 for e in entries if e['party'])
    print(f'  エントリ数:{len(entries)} (パーティあり:{with_party} URL付き:{with_url})')

    print('DB保存中...')
    con = sqlite3.connect(DB_PATH)
    init_db(con)
    crawled_date = str(date.today())
    ins, upd = save_to_db(con, entries, crawled_date)
    con.close()
    print(f'  新規:{ins}件 更新:{upd}件')

    print('\n=== URL付き構築記事 ===')
    for e in entries:
        if e['url']:
            party_str = ', '.join(p['pokemon'] for p in e['party'])
            print(f'  {e["rank"]:3}位 {e["username"]:12} {e["url"]}')
            if party_str:
                print(f'       [{party_str}]')

    print('\n=== 上位20位のパーティ ===')
    for e in entries[:20]:
        if e['party']:
            party_str = ', '.join(p['pokemon'] for p in e['party'])
            tw = f' @{e["twitter"]}' if e['twitter'] else ''
            print(f'  {e["rank"]:3}位 {e["username"]}{tw}: {party_str}')
        else:
            print(f'  {e["rank"]:3}位 {e["username"]} (パーティ非公開)')


if __name__ == '__main__':
    main()
