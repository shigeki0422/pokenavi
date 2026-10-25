import { getCollection } from 'astro:content';

// 公開記事の slug（〜-m7 等）からシーズン一覧を新しい順に返す。一覧ページに季節を手で書くと、
// 新シーズンの記事を出しても /blog/ が「M-6（最新）」のまま残る（2026-10-25）ため、記事から引く。
export async function blogSeasons(): Promise<string[]> {
	const showDrafts = import.meta.env.INCLUDE_DRAFTS === 'true';
	const posts = (await getCollection('blog')).filter((p) => showDrafts || !p.data.draft);
	const nums = new Set<number>();
	for (const p of posts) {
		const m = p.id.match(/-m(\d+)$/);
		if (m) nums.add(Number(m[1]));
	}
	return [...nums].sort((a, b) => b - a).map((n) => `m${n}`);
}

export const seasonLabel = (s: string) => s.toUpperCase().replace('M', 'M-');
