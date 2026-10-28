import mcIndex from '../../public/sim-data-mc-meta/index.json';

const basePoName = (n: string) => n.split('（')[0].split('(')[0].trim();

const mcBases = new Set(
	((mcIndex as { subjects?: { party?: string[] }[] }).subjects ?? []).flatMap((s) =>
		(s.party ?? []).map((spec) => basePoName(spec.split('@')[0].split(':')[0])),
	),
);

// SimulatorApp の ?sf= 照合（括弧内のフォーム名を落とした基本名の一致）と同じ規則で M-C の有無を判定する
export function simWatchUrl(pokemonName: string, pfx = ''): string {
	const mode = mcBases.has(basePoName(pokemonName)) ? 'simulator-mc' : 'simulator-mb';
	return `${pfx}/${mode}/?sf=${encodeURIComponent(pokemonName)}`;
}
