import { getCollection } from 'astro:content';
import fs from 'node:fs';
import path from 'node:path';
import { POKEMON_NAME_EN, POKEMON_NAME_KO } from '../i18n/pokemon-names.ts';

export async function GET() {
  const pokemonPages = (await getCollection('pokemon'))
    .filter(p => !p.data.draft)
    .sort((a, b) => (a.data.usageRank ?? 999) - (b.data.usageRank ?? 999));

  const pokemon = pokemonPages.map(p => ({
    t: 'p',
    n: p.data.pokemonName,
    e: POKEMON_NAME_EN[p.data.pokemonName] ?? '',
    k: POKEMON_NAME_KO[p.data.pokemonName] ?? '',
    u: `/pokemon/${p.id}/`,
    ue: `/en/pokemon/${p.id}/`,
    uk: `/ko/pokemon/${p.id}/`,
    i: `/images/pokemon/pokemon-${String(p.data.dexNumber).padStart(4, '0')}-${p.data.imageForm ?? '00'}.webp`,
    r: p.data.usageRank ?? 999,
  }));

  const blogs = (await getCollection('blog'))
    .filter(p => !p.data.draft)
    .sort((a, b) => (b.data.pubDate?.getTime() ?? 0) - (a.data.pubDate?.getTime() ?? 0))
    .map(p => {
      const display = p.data.title
        .replace(/^【[^】]+】\s*/, '')
        .trim();
      const season = p.id.includes('-m4') ? 'M-4' : p.id.includes('-m3') ? 'M-3' : p.id.includes('-m2') ? 'M-2' : '';
      return {
        t: 'b',
        n: display,
        u: `/blog/${p.id}/`,
        s: season,
      };
    });

  const pageByDexForm = {};
  for (const p of pokemonPages) {
    const key = `${String(p.data.dexNumber).padStart(4, '0')}-${p.data.imageForm ?? '00'}`;
    pageByDexForm[key] = { name: p.data.pokemonName, url: `/pokemon/${p.id}/`, rank: p.data.usageRank ?? 999 };
  }

  const monDir = path.join(process.cwd(), 'public', 'builder-data', 'mon');
  const moveUsers = {};
  const itemUsers = {};
  if (fs.existsSync(monDir)) {
    for (const file of fs.readdirSync(monDir)) {
      if (!file.endsWith('.json')) continue;
      const page = pageByDexForm[file.replace('.json', '')];
      if (!page) continue;
      let mon;
      try {
        mon = JSON.parse(fs.readFileSync(path.join(monDir, file), 'utf8'));
      } catch {
        continue;
      }
      for (const mv of mon.moves ?? []) {
        if (mv.pct < 10) continue;
        (moveUsers[mv.n] ??= []).push({ n: page.name, u: page.url, pct: mv.pct, r: page.rank });
      }
      for (const it of mon.items ?? []) {
        if (it.pct < 10) continue;
        (itemUsers[it.n] ??= []).push({ n: page.name, u: page.url, pct: it.pct, r: page.rank });
      }
    }
  }
  const toEntries = (users, t) =>
    Object.entries(users).map(([name, list]) => ({
      t,
      n: name,
      p: list.sort((a, b) => a.r - b.r).slice(0, 3).map(({ n, u, pct }) => ({ n, u, pct })),
    }));
  const moves = toEntries(moveUsers, 'm');
  const items = toEntries(itemUsers, 'i');

  return new Response(JSON.stringify([...pokemon, ...blogs, ...moves, ...items]), {
    headers: { 'Content-Type': 'application/json' },
  });
}
