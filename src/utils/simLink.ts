import mcIndex from '../../public/sim-data-mc-meta/index.json';
import { simNameMatch } from './simName';

const mcNames = [
	...new Set(
		((mcIndex as { subjects?: { party?: string[] }[] }).subjects ?? []).flatMap((s) =>
			(s.party ?? []).map((spec) => spec.split('@')[0].split(':')[0]),
		),
	),
];

export function simWatchUrl(pokemonName: string, pfx = ''): string {
	const mode = mcNames.some((n) => simNameMatch(pokemonName, n)) ? 'simulator-mc' : 'simulator-mb';
	return `${pfx}/${mode}/?sf=${encodeURIComponent(pokemonName)}`;
}
