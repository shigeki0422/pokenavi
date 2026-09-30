import { getCollection } from 'astro:content';
import rankingData from '../../../data/ranking.json';
import { NAME_MAP } from '../../../data/ranking-name-map';

/** シーズン切り替え用の順位データ。全シーズン分をランキングページのHTMLに直接埋め込むと
 * 600KB近くになりモバイルの表示速度を損なうため、切り替え時に取得する形にしている。 */
const CHART_ROWS = 200;
const LANGS = ['ja', 'en', 'ko'];

export function getStaticPaths() {
  const seasons = Object.keys(rankingData.seasons);
  return LANGS.flatMap((lang) => seasons.map((season) => ({ params: { lang, season } })));
}

export async function GET({ params }) {
  const showDrafts = import.meta.env.INCLUDE_DRAFTS === 'true';
  const pokemonPages = await getCollection('pokemon', (p) => showDrafts || !p.data.draft);
  const pageById = {};
  for (const p of pokemonPages) pageById[p.data.pokemonName] = p.id;

  const sd = rankingData.seasons[params.season];
  const prefix = params.lang === 'ja' ? '' : `/${params.lang}`;
  const pokemon = sd.pokemon
    .filter((p) => Object.values(p.dates).some((d) => d.rank <= CHART_ROWS))
    .map((p) => {
      const lookupName = NAME_MAP[p.name] ?? p.name;
      const ranksByDate = {};
      for (const [d, info] of Object.entries(p.dates)) ranksByDate[d] = info.rank;
      return {
        name: p.name,
        id: p.id,
        url: pageById[lookupName] ? `${prefix}/pokemon/${pageById[lookupName]}/` : null,
        ranksByDate,
      };
    });

  return new Response(JSON.stringify({ dates: sd.dates, pokemon }), {
    headers: { 'Content-Type': 'application/json' },
  });
}
