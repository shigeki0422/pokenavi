#!/usr/bin/env python3
"""
ブログ記事MDファイルをスキャンしてarticle-meta.jsonに未登録エントリを自動追加する。
npm run build の prebuild として実行される。
"""
import json
import sqlite3
import re
import glob
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), 'pokenavi.db')
META_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'article-meta.json')
BLOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'blog')


def parse_frontmatter(md_path):
    with open(md_path, encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return {}
    end = content.find('---', 3)
    if end == -1:
        return {}
    result = {}
    for line in content[3:end].splitlines():
        m = re.match(r"^(\w+):\s*'?(.+?)'?\s*$", line)
        if m:
            result[m.group(1)] = m.group(2).strip("'\"")
    return result


def get_season_from_slug(slug):
    m = re.search(r'-m(\d+)(?:-|$)', slug)
    return f'M-{m.group(1)}' if m else None


def get_pokemon_name_from_title(title):
    m = re.search(r'】(.+?)\s*考察', title)
    return m.group(1).strip() if m else None


def lookup_rank(cur, season, name):
    cur.execute(
        "SELECT rank FROM pokemon_usage WHERE season=? AND rule='single' AND pokemon=? "
        "ORDER BY crawled_date DESC LIMIT 1",
        (season, name)
    )
    row = cur.fetchone()
    return row[0] if row else None


def lookup_base_stats(cur, name):
    cur.execute(
        "SELECT dex_number, form_index, type1, type2 FROM pokemon_base_stats "
        "WHERE pokemon_name=? LIMIT 1",
        (name,)
    )
    return cur.fetchone()


def main():
    if not os.path.exists(DB_PATH):
        print(f'[sync_article_meta] DB not found at {DB_PATH}, skipping.')
        return

    with open(META_PATH, encoding='utf-8') as f:
        meta = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    added = []

    for md_file in sorted(glob.glob(os.path.join(BLOG_DIR, '*.md'))):
        slug = os.path.basename(md_file).replace('.md', '')
        if slug in meta:
            continue

        fm = parse_frontmatter(md_file)
        title = fm.get('title', '')
        if not title:
            continue

        pokemon_name = get_pokemon_name_from_title(title)
        if not pokemon_name:
            print(f'[sync_article_meta] SKIP {slug}: pokemon name not found in title')
            continue

        season = get_season_from_slug(slug)
        if not season:
            print(f'[sync_article_meta] SKIP {slug}: season not found in slug')
            continue

        # ランク検索（まず記事名、次にメガ除去で再試行）
        # 事実ファイルがあれば本文と同じ日の順位（使用率は毎日クロールされ、最新日だと本文の順位と食い違う。2026-10-28 ヒスイゾロアーク 73位/74位）
        facts_path = os.path.join(os.path.dirname(__file__), '..', '_local', 'article_facts', f'{slug}.json')
        rank = None
        icon_form = None
        if os.path.exists(facts_path):
            with open(facts_path, encoding='utf-8') as ff:
                fx = json.load(ff)
            subj = fx['subject']['name']
            icon = fx['subject'].get('icon') or ''
            icon_form = icon.split('-')[1] if '-' in icon else None
            rank = next((x['value'] for x in fx['facts'] if x['kind'] == 'usage_rank' and not x.get('season') and x['pokemon'] == subj), None)
        if rank is None:
            rank = lookup_rank(cur, season, pokemon_name)
        match_key = pokemon_name
        if rank is None:
            stripped = re.sub(r'^メガ', '', pokemon_name)
            if stripped != pokemon_name:
                rank = lookup_rank(cur, season, stripped)
                if rank is not None:
                    match_key = stripped

        # 種族値検索
        row = lookup_base_stats(cur, match_key)
        if row is None and match_key != pokemon_name:
            row = lookup_base_stats(cur, pokemon_name)
        if row is None:
            print(f'[sync_article_meta] SKIP {slug}: "{match_key}" not found in pokemon_base_stats')
            continue

        dex, form_index, type1, type2 = row
        types = [t for t in [type1, type2] if t]

        entry = {
            'name': pokemon_name,
            'rank': rank,
            'types': types,
            'matchKey': match_key,
            'dex': dex,
            # DB の form_index はリージョン形が 99（画像は -01 等）。事実ファイルの被写体アイコンを正とする
            # （2026-10-28 アローラキュウコン・ヒスイダイケンキの一覧カードの画像切れ）
            'form': icon_form or str(form_index or 0).zfill(2),
        }
        meta[slug] = entry
        added.append(slug)
        print(f'[sync_article_meta] ADD {slug}: {pokemon_name} (rank={rank}, dex={dex})')

    conn.close()

    if added:
        with open(META_PATH, 'w', encoding='utf-8') as f:
            json.dump(meta, f, ensure_ascii=False, indent=4)
        print(f'[sync_article_meta] Updated article-meta.json (+{len(added)} entries)')
    else:
        print('[sync_article_meta] No new entries.')


if __name__ == '__main__':
    main()
