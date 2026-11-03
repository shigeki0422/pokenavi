// 対戦の1ターン表示。SimulatorApp.astro の再生（renderMon/renderExplain/summarizeTurn ほか）の移植で、見た目と読み方を揃える。
import { SIM_LOG_TERM } from './diag-shared';

type Lang = 'ja' | 'en' | 'ko';

const I18N: Record<Lang, Record<string, string>> = {
  ja: { steMega: '<span class="rp-mega">メガ</span>', steBlade: '<span class="rp-forme">ブレード</span>', steHero: '<span class="rp-forme">マイティ</span>', steDisg: '<span class="rp-disg">皮破れ</span>', steCharge: '<span class="rp-charge">充電</span>', steConfused: '<span class="rp-vol">😵こんらん</span>', steSeeded: '<span class="rp-vol">🌱やどりぎ</span>', steTaunt: '<span class="rp-vol">😈ちょうはつ</span>', steEncore: '<span class="rp-vol">🔄アンコール</span>', steSalted: '<span class="rp-vol">🧂しおづけ</span>', steTrans: '<span class="rp-vol">🎭へんしん</span>', steSubPfx: '<span class="rp-vol">🪆みがわり(', steSubSfx: ')</span>', steIlluPfx: '<span class="rp-vol">イリュージョン:', steIlluSfx: '</span>', steUnknown: 'Unknown', steNotAppeared: '未登場', wSunny: '☀ 晴れ', wRain: '🌧 あめ', wSand: '🌪 すなあらし', wHail: '❄ あられ', wSnow: '❄ ゆき', stBurn: 'やけど', stPoison: 'どく', stBadPoison: 'もうどく', stParalysis: 'まひ', stSleep: 'ねむり', stFreeze: 'こおり', hazSR: 'ステルスロック', hazSpikes: 'まきびし', hazToxicSpikes: 'どくびし', hazReflect: 'リフレクター', hazLightScreen: 'ひかりのかべ', hazAuroraVeil: 'オーロラベール', remPfx: '（あと', remSfx: '）', swBadge: '交代', mine: '自分', opp: '相手', sideMe: '自分', sideOpp: '相手', logTitle: '📜 バトルログ', logDetail: '詳細ログを見る', noAction: '行動なし', aiTitle: '🧠 この手番のAIの読み', candidateMove: '候補手', winRateLabel: '勝率', honmei: '本命', lowconf: '自信×' },
  en: { steMega: '<span class="rp-mega">Mega</span>', steBlade: '<span class="rp-forme">Blade</span>', steHero: '<span class="rp-forme">Hero</span>', steDisg: '<span class="rp-disg">Disguise broken</span>', steCharge: '<span class="rp-charge">Charged</span>', steConfused: '<span class="rp-vol">😵Confused</span>', steSeeded: '<span class="rp-vol">🌱Seeded</span>', steTaunt: '<span class="rp-vol">😈Taunt</span>', steEncore: '<span class="rp-vol">🔄Encore</span>', steSalted: '<span class="rp-vol">🧂Salt Cure</span>', steTrans: '<span class="rp-vol">🎭Transformed</span>', steSubPfx: '<span class="rp-vol">🪆Substitute(', steSubSfx: ')</span>', steIlluPfx: '<span class="rp-vol">Illusion:', steIlluSfx: '</span>', steUnknown: 'Unknown', steNotAppeared: 'Not yet seen', wSunny: '☀ Sun', wRain: '🌧 Rain', wSand: '🌪 Sandstorm', wHail: '❄ Hail', wSnow: '❄ Snow', stBurn: 'BRN', stPoison: 'PSN', stBadPoison: 'TOX', stParalysis: 'PAR', stSleep: 'SLP', stFreeze: 'FRZ', hazSR: 'Stealth Rock', hazSpikes: 'Spikes', hazToxicSpikes: 'Toxic Spikes', hazReflect: 'Reflect', hazLightScreen: 'Light Screen', hazAuroraVeil: 'Aurora Veil', remPfx: ' (', remSfx: ' left)', swBadge: 'Switch', mine: 'You', opp: 'Opponent', sideMe: 'You', sideOpp: 'Opp', logTitle: '📜 Battle log', logDetail: 'Show detailed log', noAction: 'No action', aiTitle: "🧠 AI's read this turn", candidateMove: 'Candidate', winRateLabel: 'Win rate', honmei: 'Top pick', lowconf: 'Low conf.' },
  ko: { steMega: '<span class="rp-mega">메가</span>', steBlade: '<span class="rp-forme">블레이드</span>', steHero: '<span class="rp-forme">마이티</span>', steDisg: '<span class="rp-disg">탈 벗겨짐</span>', steCharge: '<span class="rp-charge">충전</span>', steConfused: '<span class="rp-vol">😵혼란</span>', steSeeded: '<span class="rp-vol">🌱씨뿌리기</span>', steTaunt: '<span class="rp-vol">😈도발</span>', steEncore: '<span class="rp-vol">🔄앙코르</span>', steSalted: '<span class="rp-vol">🧂소금절이</span>', steTrans: '<span class="rp-vol">🎭변신</span>', steSubPfx: '<span class="rp-vol">🪆대타출동(', steSubSfx: ')</span>', steIlluPfx: '<span class="rp-vol">일루전:', steIlluSfx: '</span>', steUnknown: 'Unknown', steNotAppeared: '미등장', wSunny: '☀ 쾌청', wRain: '🌧 비', wSand: '🌪 모래바람', wHail: '❄ 싸라기눈', wSnow: '❄ 설경', stBurn: '화상', stPoison: '독', stBadPoison: '맹독', stParalysis: '마비', stSleep: '잠듦', stFreeze: '얼음', hazSR: '스텔스록', hazSpikes: '압정뿌리기', hazToxicSpikes: '독압정', hazReflect: '리플렉터', hazLightScreen: '빛의장막', hazAuroraVeil: '오로라베일', remPfx: '(남은 ', remSfx: ')', swBadge: '교체', mine: '내 쪽', opp: '상대', sideMe: '나', sideOpp: '상대', logTitle: '📜 배틀 로그', logDetail: '상세 로그 보기', noAction: '행동 없음', aiTitle: '🧠 이번 턴 AI의 판단', candidateMove: '후보 수', winRateLabel: '승률', honmei: '본명', lowconf: '신뢰×' },
};

const TYPEICON: Record<string, [string, string]> = { ノーマル: ['00', 'normal'], かくとう: ['01', 'fighting'], ひこう: ['02', 'flying'], どく: ['03', 'poison'], じめん: ['04', 'ground'], いわ: ['05', 'rock'], むし: ['06', 'bug'], ゴースト: ['07', 'ghost'], はがね: ['08', 'steel'], ほのお: ['09', 'fire'], みず: ['10', 'water'], くさ: ['11', 'grass'], でんき: ['12', 'electric'], エスパー: ['13', 'psychic'], こおり: ['14', 'ice'], ドラゴン: ['15', 'dragon'], あく: ['16', 'dark'], フェアリー: ['17', 'fairy'] };
const TERRAIN: Record<string, [string, string]> = { psychic: ['🔮', 'サイコフィールド'], electric: ['⚡', 'エレキフィールド'], grassy: ['🌿', 'グラスフィールド'], misty: ['🌫', 'ミストフィールド'] };
const EXPL_REASON_TXT: Record<Lang, Record<string, string>> = {
  ja: { pfx: '実行した手: ', lp: '（', rp: '）', certain_ko: '確定で倒せる手に差し替え。探索の選択: ', encore: 'アンコールで固定。選んだ手: ', downside_guard: '最悪のケースを避けるため交代に差し替え。探索の選択: ' },
  en: { pfx: 'Executed: ', lp: ' (', rp: ')', certain_ko: 'replaced with a guaranteed KO; search picked ', encore: 'locked by Encore; picked ', downside_guard: 'switched out to avoid the worst case; search picked ' },
  ko: { pfx: '실행한 수: ', lp: ' (', rp: ')', certain_ko: '확정 KO 기술로 교체. 탐색의 선택: ', encore: '앙코르로 고정. 고른 수: ', downside_guard: '최악의 경우를 피하려고 교체로 변경. 탐색의 선택: ' },
};
const TAGS: Record<string, [string, string]> = { 外し: ['Miss', '빗나감'], 効果抜群: ['Super eff.', '효과 굉장'], いまひとつ: ['Resisted', '효과 별로'], 急所: ['Crit', '급소'], 相手耐え: ['Endured', '버팀'], 展開: ['Setup', '전개'], 設置: ['Hazard', '설치'], ばけのかわ: ['Disguise', '탈'], 防がれた: ['Blocked', '막힘'], ひるみで動けない: ['Flinch', '풀죽음'], 守り: ['Protect', '방어'] };

export interface ReplayCtx {
  lang: Lang;
  tPoke: (n: string) => string;
  tMove: (m: string) => string;
  tItem: (i: string) => string;
  tAbil: (a: string) => string;
  typeName: (t: string) => string;
  iconUrl: (n: string) => string | null;
  moveType: (m: string) => string | undefined;
  logTr: (l: string) => string;
  /** 相手の個体カードの下に足す HTML（型の読みなど） */
  oppExtra?: (name: string) => string;
}

export function makeReplay(ctx: ReplayCtx) {
  const { lang, tPoke, tMove, tItem, tAbil } = ctx;
  const I = I18N[lang];
  const JA = lang === 'ja';
  const KO = lang === 'ko' ? 1 : 0;
  const L = (ja: string, en: string, ko: string) => (lang === 'en' ? en : lang === 'ko' ? ko : ja);
  const WEATHER: Record<string, string> = { sunny: I.wSunny, rain: I.wRain, sandstorm: I.wSand, hail: I.wHail, snow: I.wSnow };
  const STATUS: Record<string, string> = { burn: I.stBurn, poison: I.stPoison, badpoison: I.stBadPoison, paralysis: I.stParalysis, sleep: I.stSleep, freeze: I.stFreeze };
  const EXEC = EXPL_REASON_TXT[lang];
  const hpColor = (f: number) => (f > 0.5 ? '#22c55e' : f > 0.2 ? '#eab308' : '#ef4444');

  function tX(x: string): string {
    if (JA || x == null || x === '') return x;
    if (x.includes('/')) return x.split('/').map(tX).join('/');
    if (x.includes(', ')) return x.split(', ').map(tX).join(', ');
    if (SIM_LOG_TERM[x]) return SIM_LOG_TERM[x][KO];
    const p = tPoke(x);
    if (p !== x) return p;
    const m = tMove(x); if (m !== x) return m;
    const a = tAbil(x); if (a !== x) return a;
    const t = ctx.typeName(x); if (t !== x) return t;
    return tItem(x) || x;
  }
  function translateTag(t: string) {
    if (JA) return t;
    const ko = t.match(/^(.+?)を倒した$/); if (ko) return KO ? `${tPoke(ko[1])} 쓰러뜨림` : `KO'd ${tPoke(ko[1])}`;
    const st = t.match(/^(こうげき|ぼうぎょ|とくこう|とくぼう|すばやさ)([↑↓])$/);
    if (st) { const S: Record<string, string> = KO ? { こうげき: '공격', ぼうぎょ: '방어', とくこう: '특공', とくぼう: '특방', すばやさ: '스피드' } : { こうげき: 'Atk', ぼうぎょ: 'Def', とくこう: 'SpAtk', とくぼう: 'SpDef', すばやさ: 'Spd' }; return `${S[st[1]]}${st[2]}`; }
    return TAGS[t] ? TAGS[t][KO] : t;
  }
  function translateCandAction(a: string) {
    if (JA || !a) return a;
    const hasMega = a.startsWith('メガ+'); const base = hasMega ? a.slice(3) : a; const mg = hasMega ? (KO ? '메가+' : 'Mega+') : '';
    const sw = base.match(/^(.+?)に交代$/); if (sw) return mg + (KO ? '교체 → ' : 'Switch → ') + tPoke(sw[1]);
    return mg + tMove(base);
  }
  const typeIconImg = (t: string | undefined, cls: string) => {
    const e = t ? TYPEICON[t] : undefined; const n = t ? ctx.typeName(t) : '';
    return e ? `<img class="${cls}" src="/images/types/type-${e[0]}-${e[1]}.png" alt="${n}" title="${n}">` : '';
  };
  const typeIcon = (move: string) => typeIconImg(ctx.moveType(move), 'tic');
  const typeIconName = (t: string) => typeIconImg(t, 'rp-tic');

  // 盤面の行動表示。技の所属側を「確認(相手の技=3-n)」「減少(自分の与ダメ=n)」から判定する（SimulatorApp と同じ）
  function parseActions(logs: string[], actives: Record<string, number>, ls: number[] | undefined) {
    const m: Record<number, Record<string, { move: string; order: number }>> = { 1: {}, 2: {} }; let ord = 0; const moveSide: Record<string, number> = {};
    (logs || []).forEach((raw) => {
      const pm = raw.match(/^▷P(\d+):\s*/); if (!pm) return; const obs = +pm[1]; if (obs !== 1 && obs !== 2) return; const l = raw.slice(pm[0].length); let r;
      if ((r = l.match(/^(.+?) の技【(.+?)】を確認/))) moveSide[r[2]] = 3 - obs;
      else if ((r = l.match(/^(.+?) に (.+?) で (?:約)?-?\d+% 減少/))) { if (moveSide[r[2]] == null) moveSide[r[2]] = obs; }
    });
    const put = (side: number, name: string, move: string, force?: boolean) => { if (side !== 1 && side !== 2) return; if (force || !m[side][name]) m[side][name] = { move, order: m[side][name] ? m[side][name].order : ++ord }; };
    (logs || []).forEach((raw, i) => {
      const l = raw.replace(/^▷P\d+:\s*/, ''); let r; const ss = ls && !/^▷/.test(raw) ? ls[i] : 0;
      if ((r = l.match(/^(.+?) の (.+?) → .+? に \d+ダメ/))) put(ss || moveSide[r[2]], r[1], r[2], !!ss);
      else if ((r = l.match(/^(.+?) の (.+?) は外れた/))) put(moveSide[r[2]], r[1], r[2]);
      else if ((r = l.match(/^(.+?) の技【(.+?)】を確認/))) put(moveSide[r[2]], r[1], r[2]);
      else if (actives) {
        if ((r = l.match(/^(.+?) の (キングシールド|トーチカ|ニードルガード|まもる|みきり|こらえる)！/))) put(actives[r[1]], r[1], r[2], true);
        else if ((r = l.match(/^(.+?) は身を守っている/))) put(actives[r[1]], r[1], '守り');
        else if ((r = l.match(/^(.+?) の (.+?) は .+? に防がれた/))) put(actives[r[1]], r[1], r[2]);
        else if ((r = l.match(/^(.+?) は (.+?) を使った/))) put(actives[r[1]], r[1], r[2]);
      }
    });
    return m;
  }
  function reorderLogs(pairs: [string, number][]) {
    const a = [...pairs];
    for (let i = 0; i < a.length - 1; i++) {
      if (/おやこあい 追撃！/.test(a[i][0]) && / → .+ に \d+ダメ/.test(a[i + 1][0])) { const t = a[i]; a[i] = a[i + 1]; a[i + 1] = t; i++; }
    }
    return a;
  }
  function summarizeTurn(logs: string[], actives: Record<string, number>, ls: number[] | undefined): string[] {
    const events: any[] = []; const megaed = new Set<string>(); let ord = 0, last: any = null, pendingOut: string | null = null;
    const moveOwner: Record<string, any> = {}; const sideName: Record<string, any> = {}; const protectAct: Record<string, any> = {}; const SIDEJP: Record<number, string> = { 1: I.sideMe, 2: I.sideOpp };
    const newAct = (side: number, name: string, move: string) => { const e = { kind: 'act', side: side || 0, order: ++ord, name, move, target: null as any, dmg: null as any, tags: [] as string[], pb: 0 }; if (side) sideName[side + '|' + name] = e; if (move) moveOwner[move] = e; events.push(e); last = e; return e; };
    const findActor = (name: string, move: string | null, sd?: number) => { if (move && sd) { const e = moveOwner[sd + '|' + move]; if (e) return e; const f = moveOwner[move]; return f && (!f.side || f.side === sd) ? f : null; } return move && moveOwner[move] ? moveOwner[move] : null; };
    const tag = (t: string) => { if (last && last.kind === 'act' && !last.tags.includes(t)) last.tags.push(t); };
    const push = (kind: string, text: string) => events.push({ kind, order: ++ord, text });
    (logs || []).forEach((raw, i) => {
      const pm = raw.match(/^▷P(\d+):\s*/); const obs = pm ? +pm[1] : 0; const side = obs ? 3 - obs : (ls && ls[i]) || 0; const l = pm ? raw.slice(pm[0].length) : raw; let m;
      if (/^P[12]選出:|見せ合い/.test(l)) return;
      if (obs && (m = l.match(/^(.+?) に (.+?) で (?:約)?-?\d+% 減少/))) { const e = moveOwner[m[2]]; if (e && !e.side) { e.side = obs; sideName[obs + '|' + e.name] = e; } return; }
      if ((m = l.match(/^(.+?) はメガ進化した！/))) { megaed.add(m[1]); return; }
      if ((m = l.match(/^(.+?) の (.+?) → (.+?) に (\d+)ダメ/))) { const e = findActor(m[1], m[2], side) || newAct(side, m[1], m[2]); if (side && !e.side) e.side = side; if (side) moveOwner[side + '|' + m[2]] = e; e.move = e.move || m[2]; e.target = m[3]; e.dmg = +m[4]; last = e; return; }
      if ((m = l.match(/^おやこあい 追撃！ (\d+)ダメ/))) { if (last && last.kind === 'act') last.pb = (last.pb || 0) + +m[1]; return; }
      if ((m = l.match(/^(.+?) は (.+?) を使った/))) { const e = findActor(m[1], m[2]); if (!e) newAct(side, m[1], m[2]); else { if (side && !e.side) { e.side = side; sideName[side + '|' + m[1]] = e; } last = e; } return; }
      if ((m = l.match(/^(.+?) の技【(.+?)】を確認/))) { let e = side ? sideName[side + '|' + m[1]] : null; if (!e) e = newAct(side, m[1], m[2]); else last = e; if (m[2]) moveOwner[m[2]] = e; return; }
      if ((m = l.match(/^(.+?) の (.+?) は外れた/))) { const e = findActor(m[1], m[2]) || newAct(side, m[1], m[2]); e.tags.push('外し'); last = e; return; }
      if ((m = l.match(/^(.+?) はひるんで動けない/))) { const e = findActor(m[1], null) || newAct(side, m[1], 'ひるみで動けない'); last = e; return; }
      if ((m = l.match(/^(.+?) は身を守っている/))) { const nm = m[1]; let e = events.find((x) => x.kind === 'act' && x.name === nm); if (!e) e = newAct((actives && actives[nm]) || 0, nm, '守り'); protectAct[nm] = e; last = e; return; }
      if ((m = l.match(/^(.+?) の (キングシールド|トーチカ|ニードルガード|まもる|みきり|こらえる)！/))) { const e = protectAct[m[1]]; if (e) { e.move = m[2]; last = e; } return; }
      if ((m = l.match(/^(.+?) は疲れてこんらんした/))) { push('dmg', L(`${m[1]}：こんらん（あばれ終了）`, `${tPoke(m[1])}: Confusion (rampage ended)`, `${tPoke(m[1])}: 혼란 (난동 종료)`)); return; }
      if ((m = l.match(/^(.+?) はこんらんして自分を傷つけた/))) { push('dmg', L(`${m[1]}：こんらんで自傷`, `${tPoke(m[1])}: Confusion self-hit`, `${tPoke(m[1])}: 혼란으로 자해`)); return; }
      if ((m = l.match(/^(.+?) はこんらんした/))) { push('dmg', L(`${m[1]}：こんらんになった`, `${tPoke(m[1])}: Confused`, `${tPoke(m[1])}: 혼란 상태`)); return; }
      if ((m = l.match(/^(.+?) は引っ込んだ/))) { pendingOut = m[1]; return; }
      if ((m = l.match(/^(.+?) が出てきた/))) { push('sw', pendingOut ? `${tPoke(pendingOut)} → ${tPoke(m[1])}` : L(`${m[1]} 繰り出し`, `${tPoke(m[1])} sent out`, `${tPoke(m[1])} 등장`)); pendingOut = null; last = null; return; }
      if ((m = l.match(/^(.+?) が登場した/))) { push('sw', L(`${m[1]}（瀕死後）`, `${tPoke(m[1])} (after KO)`, `${tPoke(m[1])} (기절 후)`)); last = null; return; }
      if ((m = l.match(/^(.+?) は強制交代させられ/))) { push('sw', L(`${m[1]} が強制交代`, `${tPoke(m[1])} forced out`, `${tPoke(m[1])} 강제 교체`)); return; }
      if ((m = l.match(/^(.+?) の (.+?)！ (.+?) に (\d+) のダメージ/))) { push('dmg', L(`${m[2]}：${m[3]}に${m[4]}`, `${tX(m[2])}: ${tPoke(m[3])} ${m[4]}`, `${tX(m[2])}: ${tPoke(m[3])}에게 ${m[4]}`)); return; }
      if ((m = l.match(/^(.+?) はステルスロックの効果を受けた！\((\d+)\)/))) { push('dmg', L(`${m[1]}：ステルスロック ${m[2]}`, `${tPoke(m[1])}: ${tMove('ステルスロック')} ${m[2]}`, `${tPoke(m[1])}: ${tMove('ステルスロック')} ${m[2]}`)); return; }
      if ((m = l.match(/^(.+?) は (.+?) で (\d+) のダメージを受けた/))) { push('dmg', L(`${m[1]}：${m[2]} ${m[3]}`, `${tPoke(m[1])}: ${tX(m[2])} ${m[3]}`, `${tPoke(m[1])}: ${tX(m[2])} ${m[3]}`)); return; }
      if ((m = l.match(/^(.+?) は (.+?) のダメージを受けた！\((\d+)\)/))) { push('dmg', L(`${m[1]}：${m[2]} ${m[3]}`, `${tPoke(m[1])}: ${tX(m[2])} ${m[3]}`, `${tPoke(m[1])}: ${tX(m[2])} ${m[3]}`)); return; }
      if ((m = l.match(/^(.+?) は (?:.+? の )?反動を受けた！\((\d+)\)/))) { push('dmg', L(`${m[1]}：反動 ${m[2]}`, `${tPoke(m[1])}: Recoil ${m[2]}`, `${tPoke(m[1])}: 반동 ${m[2]}`)); return; }
      if ((m = l.match(/^(.+?) の (.+?) が叩き落とされた！/))) { push('dmg', L(`${m[1]} の ${m[2]} を落とした`, `Knocked off ${tPoke(m[1])}'s ${tItem(m[2])}`, `${tPoke(m[1])}의 ${tItem(m[2])} 떨어뜨림`)); return; }
      if ((m = l.match(/^(.+?) の ばけのかわ が破れた！\((\d+)\)/))) { const e = last && last.kind === 'act' ? last : null; if (e) { e.target = m[1]; e.dmg = +m[2]; if (!e.tags.includes('ばけのかわ')) e.tags.push('ばけのかわ'); } else push('dmg', L(`${m[1]}：ばけのかわ が破れた（${m[2]}）`, `${tPoke(m[1])}: ${tAbil('ばけのかわ')} busted (${m[2]})`, `${tPoke(m[1])}: ${tAbil('ばけのかわ')} 해제 (${m[2]})`)); return; }
      if ((m = l.match(/^(.+?) は (.+?) に効かない/))) { push('dmg', L(`${m[1]} は ${m[2]} に無効（効果なし）`, `${tX(m[1])} → ${tPoke(m[2])} (no effect)`, `${tX(m[1])} → ${tPoke(m[2])} (효과 없음)`)); return; }
      if ((m = l.match(/^(.+?) の (.+?) は (.+?) に防がれた/))) { let e = findActor(m[1], m[2]); if (!e) e = newAct((actives && actives[m[1]]) || 0, m[1], m[2]); if (!e.tags.includes('防がれた')) e.tags.push('防がれた'); last = e; return; }
      if ((m = l.match(/^(.+?) の オボンのみ が発動！ HPが (\d+) 回復/))) { push('dmg', L(`${m[1]}：オボンのみ +${m[2]}回復`, `${tPoke(m[1])}: ${tItem('オボンのみ')} +${m[2]} HP`, `${tPoke(m[1])}: ${tItem('オボンのみ')} +${m[2]} 회복`)); return; }
      if ((m = l.match(/^(.+?) の でんきにかえる！/))) { push('dmg', L(`${m[1]}：でんきにかえる（充電）`, `${tPoke(m[1])}: ${tAbil('でんきにかえる')} (charged)`, `${tPoke(m[1])}: ${tAbil('でんきにかえる')} (충전)`)); return; }
      if ((m = l.match(/^(.+?) (?:の|は) (.+?) で HPが (\d+) 回復/))) { push('dmg', L(`${m[1]}：${m[2]} +${m[3]}回復`, `${tPoke(m[1])}: ${tX(m[2])} +${m[3]} HP`, `${tPoke(m[1])}: ${tX(m[2])} +${m[3]} 회복`)); return; }
      if (/ばつぐん/.test(l)) { tag('効果抜群'); return; }
      if (/いまひとつ/.test(l)) { tag('いまひとつ'); return; }
      if (/急所に当たった/.test(l)) { tag('急所'); return; }
      if (/(タスキ|がんじょう).*耐え/.test(l)) { tag('相手耐え'); return; }
      if ((m = l.match(/^(サイコフィールド|エレキフィールド|グラスフィールド|ミストフィールド)が広がった！/))) { push('fld', L(`${m[1]} が張られた`, `${tMove(m[1])} set`, `${tMove(m[1])} 전개`)); return; }
      if ((m = l.match(/^(.+?) の (サイコメイカー|エレキメイカー|グラスメイカー|こぼれダネ)！/))) { const f = ({ サイコメイカー: 'サイコフィールド', エレキメイカー: 'エレキフィールド', グラスメイカー: 'グラスフィールド', こぼれダネ: 'グラスフィールド' } as Record<string, string>)[m[2]]; push('fld', L(`${m[1]} の ${m[2]}：${f} が張られた`, `${tPoke(m[1])}'s ${tAbil(m[2])}: ${tMove(f)} set`, `${tPoke(m[1])}의 ${tAbil(m[2])}: ${tMove(f)} 전개`)); return; }
      if ((m = l.match(/^トリックルーム が(発動した|解除された)！/))) { const on = m[1] === '発動した'; push('fld', L(`トリックルーム が${on ? '発動した' : '解除された'}`, `${tMove('トリックルーム')} ${on ? 'set' : 'ended'}`, `${tMove('トリックルーム')} ${on ? '발동' : '해제'}`)); return; }
      if ((m = l.match(/^(psychic|electric|grassy|misty) フィールドが終わった！/))) { const f = TERRAIN[m[1]][1]; push('fld', L(`${f} が切れた`, `${tMove(f)} ended`, `${tMove(f)} 종료`)); return; }
      if ((m = l.match(/^(.+?) の効果が切れた！/))) { push('fld', L(`${m[1]} が切れた`, `${tX(m[1])} ended`, `${tX(m[1])} 종료`)); return; }
      if ((m = l.match(/^(.+?) は フィールド を解除した！/))) { push('fld', L(`${m[1]} がフィールドを解除した`, `${tPoke(m[1])} cleared the terrain`, `${tPoke(m[1])} 필드 해제`)); return; }
      if (/吹き始めた/.test(l)) { tag('展開'); return; }
      if (/まき散らされ|ステルスロックを/.test(l)) { tag('設置'); return; }
      if ((m = l.match(/^(.+?) は倒れた/))) { tag(`${m[1]}を倒した`); return; }
      if ((m = l.match(/(こうげき|ぼうぎょ|とくこう|とくぼう|すばやさ) が.*?(上が|下が)/))) { tag(`${m[1]}${m[2] === '上が' ? '↑' : '↓'}`); return; }
    });
    if (actives) events.forEach((e) => { if (e.kind === 'act' && !e.side && actives[e.name]) e.side = actives[e.name]; });
    const circ = ['①', '②', '③', '④']; let an = 0;
    return events.sort((a, b) => a.order - b.order).map((e) => {
      if (e.kind === 'sw') return `<span class="rlog-sw">${I.swBadge}</span> ${e.text}`;
      if (e.kind === 'dmg') return `<span class="rlog-dmg">↳ ${e.text}</span>`;
      if (e.kind === 'fld') return `<span class="rlog-fld">◆ ${e.text}</span>`;
      an++; const sl = e.side ? `<span class="rlog-side s${e.side}">${SIDEJP[e.side]}</span> ` : '';
      const sep = JA ? '：' : ': '; const megaBadge = `<span class="rlog-mega">${L('メガ', 'Mega', '메가')}</span> `;
      let s = `${circ[an - 1] || an} ${sl}${megaed.has(e.name) ? megaBadge : ''}${tPoke(e.name)}${sep}${tX(e.move) || '—'}`;
      if (e.dmg != null) s += JA ? ` → ${e.target} に ${e.dmg}${e.pb ? '+' + e.pb : ''}` : ` → ${tPoke(e.target)} ${e.dmg}${e.pb ? '+' + e.pb : ''}`;
      if (e.tags.length) s += JA ? `（${e.tags.join('・')}）` : ` (${e.tags.map(translateTag).join(' · ')})`;
      return s;
    });
  }

  function renderMon(p: any, active: boolean, mine: boolean, action: any, hidden: boolean, extra: string) {
    if (hidden) return `<div class="rp-mon unknown"><div class="rp-mon-ico"><span class="rp-unknown-q">？</span></div>
      <div class="rp-mon-body"><div class="rp-mon-name muted">${I.steUnknown}</div><div class="muted" style="font-size:.68rem">${I.steNotAppeared}</div></div></div>`;
    const f = p.max_hp ? p.hp / p.max_hp : 0; const u = ctx.iconUrl(p.name);
    const boosts = Object.entries(p.stages || {}).filter(([, v]) => v).map(([k, v]: any) => `<span class="${v > 0 ? 'bup' : 'bdn'}">${k}${v > 0 ? '▲' : '▼'}${Math.abs(v)}</span>`).join(' ');
    const b = `${p.mega ? I.steMega : ''}${p.blade_forme ? I.steBlade : ''}${p.hero ? I.steHero : ''}${p.status ? `<span class="rp-status">${STATUS[p.status] || p.status}</span>` : ''}${p.disguise_broken ? I.steDisg : ''}${p.electro_charged ? I.steCharge : ''}${p.confused ? I.steConfused : ''}${p.seeded ? I.steSeeded : ''}${p.taunt ? I.steTaunt : ''}${p.encore ? I.steEncore : ''}${p.salted ? I.steSalted : ''}${p.transformed ? I.steTrans : ''}${p.substitute_hp ? I.steSubPfx + p.substitute_hp + I.steSubSfx : ''}${p.illusion_name ? I.steIlluPfx + p.illusion_name + I.steIlluSfx : ''}`;
    return `<div class="rp-mon ${active ? 'act' : ''} ${p.alive ? '' : 'dead'}">
      <div class="rp-mon-ico">${u ? `<img src="${u}" alt="${tPoke(p.name)}" onerror="this.style.display='none'">` : ''}${active ? `<span class="rp-active-badge">${mine ? '🔵' : '🔴'}</span>` : ''}${p.alive ? '' : '<span class="rp-x">×</span>'}</div>
      <div class="rp-mon-body">
        <div class="rp-mon-name">${tPoke(p.name)}${typeIconName(p.type1)}${p.type2 ? typeIconName(p.type2) : ''}</div>
        ${b ? `<div class="rp-badges">${b}</div>` : ''}
        <div class="row" style="gap:.3rem"><div class="hpbar"><div class="hpfill" style="width:${Math.round(f * 100)}%;background:${hpColor(f)}"></div></div><span class="rp-hp">${p.hp}/${p.max_hp}</span></div>
        ${boosts ? `<div class="rp-boost">${boosts}</div>` : ''}
        ${action ? `<div class="rp-move"><span class="rp-order ${action.order === 1 ? 'first' : ''}">${action.order}</span>${typeIcon(action.move) || '➤'} ${tX(action.move)}</div>` : ''}
      </div>${extra}
    </div>`;
  }
  function hazardBar(sd: any) {
    const h: string[] = [];
    if (sd.stealth_rock) h.push(I.hazSR);
    if (sd.spikes) h.push(I.hazSpikes + (sd.spikes > 1 ? `×${sd.spikes}` : ''));
    if (sd.toxic_spikes) h.push(I.hazToxicSpikes + (sd.toxic_spikes > 1 ? `×${sd.toxic_spikes}` : ''));
    if (sd.sticky_web) h.push(tMove('ねばねばネット'));
    const rem = (c: number) => (c ? `${I.remPfx}${c}${I.remSfx}` : '');
    if (sd.reflect) h.push(I.hazReflect + rem(sd.reflect_count));
    if (sd.light_screen) h.push(I.hazLightScreen + rem(sd.light_screen_count));
    if (sd.aurora_veil) h.push(I.hazAuroraVeil + rem(sd.aurora_veil_count));
    if (sd.tailwind) h.push('🍃 ' + tMove('おいかぜ') + rem(sd.tailwind_count));
    return `<div class="rp-haz">${h.map((x) => `<span class="hazchip">${x}</span>`).join('')}</div>`;
  }
  function renderExplain(t: any, played: string | null) {
    const e1 = t.expl1; if (!e1) return '';
    const pc = (x: number | null) => (x == null ? '—' : Math.round(x * 100) + '%');
    const cands = e1.cands.slice();
    let hon: string | null = null, mv = -1; for (const c of cands) { if (c.v > mv) { mv = c.v; hon = c.a; } }
    const thr = 0.1 * mv;
    const norm = (s: string) => (s || '').replace('メガ+', '');
    let chosen = e1.chosen;
    if (e1.exec) { if (!cands.some((c: any) => c.a === e1.exec)) cands.push({ a: e1.exec, v: null, q: null }); chosen = e1.exec; }
    else if (played) { const h = cands.find((c: any) => norm(c.a) === played); if (h) chosen = h.a; }
    cands.sort((a: any, b: any) => (b.q == null ? -1 : b.q) - (a.q == null ? -1 : a.q));
    const rows = cands.map((c: any) => {
      const weak = (c.v || 0) < thr && c.a !== chosen;
      return `<tr class="${c.a === chosen ? 'chosen' : ''}${weak ? ' weak' : ''}"><td>${c.a === chosen ? '▶ ' : ''}${translateCandAction(c.a)}${c.a === hon ? `<span class="honmei">${I.honmei}</span>` : ''}${weak ? `<span class="lowconf">${I.lowconf}</span>` : ''}</td><td>${pc(c.q)}</td></tr>`;
    }).join('');
    const ex = e1.exec && e1.exec !== e1.chosen && EXEC[e1.reason] ? `<div class="expl-note">${EXEC.pfx}${translateCandAction(e1.exec)}${EXEC.lp}${EXEC[e1.reason]}${translateCandAction(e1.chosen)}${EXEC.rp}</div>` : '';
    return `<div class="expl"><div class="expl-h">${I.aiTitle}</div><div class="expl-side"><table class="expl-tbl"><tr><th>${I.candidateMove}</th><th>${I.winRateLabel}</th></tr>${rows}</table>${ex}</div></div>`;
  }
  function renderColumn(sd: any, mine: boolean, act: any, revealed: Set<number> | null) {
    return `<div class="rp-col ${mine ? 'mine' : 'opp'}"><div class="rp-label">${mine ? I.mine : I.opp}</div>${hazardBar(sd)}
      ${sd.party.map((p: any, i: number) => {
        const hidden = !!revealed && !revealed.has(i);
        return renderMon(p, i === sd.active_idx, mine, (act || {})[p.name], hidden, !mine && !hidden && ctx.oppExtra ? ctx.oppExtra(p.name) : '');
      }).join('')}</div>`;
  }

  /** turns[idx] の盤面・AIの読み・バトルログ（SimulatorApp の renderReplay と同じ並び） */
  function turnHtml(turns: any[], idx: number) {
    const t = turns[idx];
    const acn: Record<string, number> = {}; const a1 = t.side1.party[t.side1.active_idx], a2 = t.side2.party[t.side2.active_idx];
    if (a1 && a2 && a1.name !== a2.name) { acn[a1.name] = 1; acn[a2.name] = 2; }
    const rem = (c: number) => (c ? `${I.remPfx}${c}${I.remSfx}` : '');
    const wx = t.weather && WEATHER[t.weather] ? `${WEATHER[t.weather]}${rem(t.weather_count)}　` : '';
    const tr = t.trick_room ? `🌀 ${tMove('トリックルーム')}${rem(t.trick_room_count)}　` : '';
    const tf = t.terrain && TERRAIN[t.terrain] ? `${TERRAIN[t.terrain][0]} ${tMove(TERRAIN[t.terrain][1])}${rem(t.terrain_count)}` : '';
    const ACT = parseActions(t.logs, acn, t.log_sides);
    const banner = wx || tr || tf ? `<div class="rp-banner">${wx}${tf ? tf + '　' : ''}${tr}</div>` : '';
    const seenOpp = new Set<number>(); for (let k = 0; k <= idx; k++) { const ai = turns[k].side2.active_idx; if (ai != null) seenOpp.add(ai); }
    const simple = summarizeTurn(t.logs, acn, t.log_sides);
    const full = reorderLogs((t.logs || []).map((l: string, i: number) => [l, t.log_sides && !/^▷/.test(l) ? t.log_sides[i] : 0] as [string, number]))
      .map(([l, sd]) => `<div>${sd ? `<span class="rlog-side s${sd}">${sd === 1 ? I.sideMe : I.sideOpp}</span> ` : ''}${ctx.logTr(l)}</div>`).join('') || '—';
    return `${banner}<div class="rp-grid">${renderColumn(t.side1, true, ACT[1], null)}${renderColumn(t.side2, false, ACT[2], seenOpp)}</div>
      ${renderExplain(t, a1 && ACT[1] && ACT[1][a1.name] ? ACT[1][a1.name].move : null)}
      <div class="expl"><div class="expl-h" style="margin-bottom:.35em">${I.logTitle}</div>
        <div class="rlog-simple">${simple.length ? simple.map((s) => `<div>${s}</div>`).join('') : `<div class="muted">${I.noAction}</div>`}</div>
        <details class="rlog-detail"><summary>${I.logDetail}</summary><div class="rlog-full">${full}</div></details></div>`;
  }

  return { turnHtml };
}
