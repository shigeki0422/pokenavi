import { getCollection } from 'astro:content';

export async function GET() {
  const pokemon = await getCollection('pokemon');
  const map = {};
  for (const p of pokemon) {
    if (p.data.dexNumber == null) continue;
    const dex = String(p.data.dexNumber).padStart(4, '0');
    const form = p.data.imageForm ?? '00';
    map[`${dex}-${form}`] = `/pokemon/${p.id}/`;
  }
  return new Response(JSON.stringify(map), {
    headers: { 'Content-Type': 'application/json' },
  });
}
