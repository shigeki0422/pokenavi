import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: z.optional(image()),
			draft: z.boolean().optional().default(false),
		}),
});

const pokemon = defineCollection({
	loader: glob({ base: './src/content/pokemon', pattern: '**/*.{md,mdx}' }),
	schema: z.object({
		title: z.string(),
		description: z.string(),
		pokemonName: z.string(),
		dexNumber: z.number(),
		usageRank: z.number().optional(),
		imageForm: z.string().optional().default('00'),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		draft: z.boolean().optional().default(false),
		analysisSlug: z.string().optional(),
		faq: z.object({
			season: z.string(),
			topMoves: z.array(z.string()),
			topMovePct: z.array(z.number()),
			topItems: z.array(z.string()),
			topItemPct: z.array(z.number()),
			topAbility: z.string(),
			topAbilityPct: z.number(),
			topNature: z.string(),
			topNaturePct: z.number(),
			topNature2: z.string().optional(),
			topNaturePct2: z.number().optional(),
		}).optional(),
	}),
});

export const collections = { blog, pokemon };
