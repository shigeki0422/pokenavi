// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig, fontProviders } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: 'https://pokenavi.jp',
	integrations: [
		mdx(),
		sitemap({
			// matchup は1v1計算の雛形でページ間の差分が数値だけ。
			// en/ko は翻訳済みの第1階層(/en/ ・/en/ranking/ 等)だけ載せる。
			// 下位(/en/pokemon/<slug>/)はUIラベルが未翻訳で BaseHead が noindex にする。
			filter: (page) => {
				const segs = new URL(page).pathname.split('/').filter(Boolean);
				if (segs[0] === 'matchup') return false;
				if (segs[0] === 'en' || segs[0] === 'ko') return segs.length <= 2;
				return true;
			},
		}),
	],
	fonts: [
		{
			provider: fontProviders.local(),
			name: 'Atkinson',
			cssVariable: '--font-atkinson',
			fallbacks: ['sans-serif'],
			options: {
				variants: [
					{
						src: ['./src/assets/fonts/atkinson-regular.woff2'],
						weight: 400,
						style: 'normal',
						display: 'swap',
					},
					{
						src: ['./src/assets/fonts/atkinson-bold.woff2'],
						weight: 700,
						style: 'normal',
						display: 'swap',
					},
				],
			},
		},
	],
});
