import { getCollection } from 'astro:content';
import { POKEMON_NAME_EN, POKEMON_NAME_KO } from '../i18n/pokemon-names.ts';

export async function GET() {
  const pokemon = (await getCollection('pokemon'))
    .filter(p => !p.data.draft)
    .sort((a, b) => (a.data.usageRank ?? 999) - (b.data.usageRank ?? 999))
    .map(p => ({
      t: 'p',
      n: p.data.pokemonName,
      e: POKEMON_NAME_EN[p.data.pokemonName] ?? '',
      k: POKEMON_NAME_KO[p.data.pokemonName] ?? '',
      u: `/pokemon/${p.id}/`,
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
      const season = p.id.includes('-m3') ? 'M-3' : p.id.includes('-m2') ? 'M-2' : '';
      return {
        t: 'b',
        n: display,
        u: `/blog/${p.id}/`,
        s: season,
      };
    });

  return new Response(JSON.stringify([...pokemon, ...blogs]), {
    headers: { 'Content-Type': 'application/json' },
  });
}
