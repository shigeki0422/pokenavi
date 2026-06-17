import base64
import sys
import json
from datetime import datetime
from pathlib import Path

import anthropic

sys.path.insert(0, str(Path(__file__).parent))
from db import get_conn, init_db

SEASON = 'M-3'
RULE = 'single'
SOURCE = 'champions_adb'
CRAWLED_DATE = '2026-06-17'
INPUT_DIR = Path('/tmp/champ_crawl_2026-06-17/detail')

client = anthropic.Anthropic()


def encode_image(path: Path) -> str:
    return base64.standard_b64encode(path.read_bytes()).decode('utf-8')


def ask_vision(prompt: str, image_paths: list[Path]) -> str:
    content = []
    for p in image_paths:
        content.append({
            'type': 'image',
            'source': {'type': 'base64', 'media_type': 'image/png', 'data': encode_image(p)}
        })
    content.append({'type': 'text', 'text': prompt})
    msg = client.messages.create(
        model='claude-haiku-4-5-20251001',
        max_tokens=1024,
        messages=[{'role': 'user', 'content': content}]
    )
    return msg.content[0].text


def parse_ranked_panel(images: list[Path], panel_label: str) -> list[tuple[int, str, float]]:
    if not images:
        return []
    prompt = (
        f'これはポケモンゲームの{panel_label}パネルのスクリーンショットです。'
        '複数枚の場合は続きのページです。'
        '各行の「順位 名前 使用率%」をJSONリストで返してください。'
        '形式: [{"rank":1,"name":"じしん","rate":98.6}, ...]\n'
        'JSON以外は出力しないでください。'
    )
    text = ask_vision(prompt, images)
    try:
        start = text.find('[')
        end = text.rfind(']') + 1
        return [(r['rank'], r['name'], r['rate']) for r in json.loads(text[start:end])]
    except Exception:
        return []


def parse_partner_panel(images: list[Path]) -> list[tuple[int, str]]:
    if not images:
        return []
    prompt = (
        'これはポケモンゲームの「同じチームのポケモン」パネルです。'
        '各行の「順位 ポケモン名」をJSONリストで返してください。'
        '形式: [{"rank":1,"name":"ブリジュラス"}, ...]\n'
        'JSON以外は出力しないでください。'
    )
    text = ask_vision(prompt, images)
    try:
        start = text.find('[')
        end = text.rfind(']') + 1
        return [(r['rank'], r['name']) for r in json.loads(text[start:end])]
    except Exception:
        return []


def parse_ev_panel(images: list[Path]) -> list[tuple[int, float, int, int, int, int, int, int]]:
    if not images:
        return []
    prompt = (
        'これはポケモンゲームの「能力ポイント」パネルです。'
        '各行の順位・使用率・H・A・B・C・D・S（6列の数値）をJSONリストで返してください。'
        '形式: [{"rank":1,"rate":57.9,"h":2,"a":32,"b":0,"c":0,"d":0,"s":32}, ...]\n'
        'JSON以外は出力しないでください。'
    )
    text = ask_vision(prompt, images)
    try:
        start = text.find('[')
        end = text.rfind(']') + 1
        rows = []
        for r in json.loads(text[start:end]):
            rows.append((r['rank'], r['rate'], r['h'], r['a'], r['b'], r['c'], r['d'], r['s']))
        return rows
    except Exception:
        return []


def parse_header(images: list[Path]) -> str | None:
    if not images:
        return None
    prompt = (
        'このポケモンゲームのスクリーンショットの上部に「1位 ガブリアス」のように順位とポケモン名が表示されています。'
        'ポケモン名だけを返してください。他は何も出力しないでください。'
    )
    name = ask_vision(prompt, [images[0]]).strip()
    return name if name else None


def process_folder(folder: Path, conn, now: str):
    try:
        rank = int(folder.name)
    except ValueError:
        return

    move_imgs = sorted(folder.glob('move_*.png'))
    item_imgs = sorted(folder.glob('item_*.png'))
    partner_imgs = sorted(folder.glob('partner_*.png'))
    nature_imgs = sorted(folder.glob('nature_*.png'))
    ev_imgs = sorted(folder.glob('ev_*.png'))
    ability_imgs = sorted(folder.glob('ability_*.png'))

    pokemon = parse_header(move_imgs or item_imgs or ability_imgs)
    if not pokemon:
        print(f'  [{folder.name}] ポケモン名取得失敗')
        return

    print(f'  [{rank:3d}位] {pokemon}', flush=True)

    conn.execute(
        'INSERT OR IGNORE INTO pokemon_usage (season,rule,rank,pokemon,pokemon_id,usage_rate,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?,?)',
        (SEASON, RULE, rank, pokemon, None, None, SOURCE, CRAWLED_DATE, now)
    )

    for rank_e, name, rate in parse_ranked_panel(move_imgs, '技'):
        conn.execute(
            'INSERT OR IGNORE INTO pokemon_moves (season,rule,pokemon,rank,move,usage_rate,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?,?)',
            (SEASON, RULE, pokemon, rank_e, name, rate, SOURCE, CRAWLED_DATE, now)
        )

    for rank_e, name, rate in parse_ranked_panel(item_imgs, '持ち物'):
        conn.execute(
            'INSERT OR IGNORE INTO pokemon_items (season,rule,pokemon,rank,item,usage_rate,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?,?)',
            (SEASON, RULE, pokemon, rank_e, name, rate, SOURCE, CRAWLED_DATE, now)
        )

    for rank_e, name, rate in parse_ranked_panel(ability_imgs, '特性'):
        conn.execute(
            'INSERT OR IGNORE INTO pokemon_abilities (season,rule,pokemon,rank,ability,usage_rate,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?,?)',
            (SEASON, RULE, pokemon, rank_e, name, rate, SOURCE, CRAWLED_DATE, now)
        )

    for rank_e, name, rate in parse_ranked_panel(nature_imgs, '能力補正（性格）'):
        conn.execute(
            'INSERT OR IGNORE INTO pokemon_natures (season,rule,pokemon,rank,nature,usage_rate,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?,?)',
            (SEASON, RULE, pokemon, rank_e, name, rate, SOURCE, CRAWLED_DATE, now)
        )

    for rank_e, rate, h, a, b, c, d, s in parse_ev_panel(ev_imgs):
        spread = f'H{h}A{a}B{b}C{c}D{d}S{s}'
        conn.execute(
            'INSERT OR IGNORE INTO pokemon_evs (season,rule,pokemon,rank,ev_spread,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (SEASON, RULE, pokemon, rank_e, spread, h, a, b, c, d, s, rate, SOURCE, CRAWLED_DATE, now)
        )

    for rank_e, name in parse_partner_panel(partner_imgs):
        conn.execute(
            'INSERT OR IGNORE INTO pokemon_partners (season,rule,pokemon,rank,partner,source,crawled_date,crawled_at) VALUES (?,?,?,?,?,?,?,?)',
            (SEASON, RULE, pokemon, rank_e, name, SOURCE, CRAWLED_DATE, now)
        )

    conn.commit()


def main():
    init_db()
    conn = get_conn()
    now = datetime.now().isoformat()

    folders = sorted([f for f in INPUT_DIR.iterdir() if f.is_dir()], key=lambda p: int(p.name))
    total = len(folders)
    for i, folder in enumerate(folders, 1):
        print(f'[{i}/{total}]', end=' ', flush=True)
        process_folder(folder, conn, now)

    conn.close()
    print('完了')


if __name__ == '__main__':
    main()
