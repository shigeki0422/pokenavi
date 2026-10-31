// SimulatorApp の is:inline スクリプトへ toString() で渡すため、外部の変数を参照しない自己完結の関数にする
export function simNameKey(name: string): string {
	const ALIASES: Record<string, string> = {
		'ケンタロス(炎)': 'パルデアケンタロス(炎)',
		'ケンタロス(水)': 'パルデアケンタロス(水)',
		'ケンタロス(格)': 'パルデアケンタロス(格)',
		'パルデアケンタロス(闘)': 'パルデアケンタロス(格)',
		'ルガルガン(黄昏)': 'ルガルガン(たそがれ)',
		'ルガルガン(昼)': 'ルガルガン(まひる)',
		'ルガルガン(夜)': 'ルガルガン(まよなか)',
	};
	let n = name.trim().replace(/（/g, '(').replace(/）/g, ')').replace(/\s+\(/g, '(');
	n = ALIASES[n] ?? n;
	const m = n.match(/^(.+)\((アローラ|ガラル|ヒスイ|パルデア)\)$/);
	return m ? m[2] + m[1] : n;
}

export function simNameMatch(filterName: string, specName: string): boolean {
	const a = simNameKey(filterName);
	const b = simNameKey(specName);
	if (a === b) return true;
	return a.split('(')[0] === b.split('(')[0] && (!a.includes('(') || !b.includes('('));
}

export const SIM_NAME_FN_SRC = `${simNameKey.toString()}\n${simNameMatch.toString()}`;
