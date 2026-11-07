// 工房の「パーティ診断」パネル（試作・ローカル用）。API 契約は product3_server.py の /diagnose・/diag_battle・/improve。
import { guideBody, gdAdv, gdRound, makeLogTranslator } from './diag-shared';
import { normalizeSuggestSpeciesName } from './spec';
import { makeReplay } from './sim-replay';
import { MATCHUP_SEASON } from '../../consts';
import { track } from '../track';

type Lang = 'ja' | 'en' | 'ko';

export interface DiagHost {
  lang: Lang;
  esc: (s: string) => string;
  tPoke: (n: string) => string;
  tMove: (n: string) => string;
  tItem: (n: string) => string;
  tAbil: (n: string) => string;
  tNature: (n: string) => string;
  maps: { poke: Record<string, string>; move: Record<string, string>; abil: Record<string, string>; item: Record<string, string>; type: Record<string, string> };
  getSpecs: () => { specs: string[] | null; filled: number };
  applySpec: (slotIdx: number, spec: string) => any;
  restoreSlot: (slotIdx: number, prev: any) => void;
}

const API = /(^|\.)pokenavi\.jp$/.test(location.hostname) ? '/api' : 'http://localhost:8899';
const EVK = ['H', 'A', 'B', 'C', 'D', 'S'];

const T: Record<Lang, any> = {
  ja: {
    head: 'パーティ診断', badge: '試作', run: '診断する', rerun: 'もう一度診断する',
    needSix: (n: number) => `6体そろうと診断できます（いま${n}体）`,
    stale: '編集中のパーティが診断時から変わっています。結果は診断したときのパーティのものです。',
    loading: '診断中…（数十秒かかります）',
    legend: `相手は使用率・同居率から生成した ${MATCHUP_SEASON} のパーティ。有利度は本番の対戦AI（探索を減らした版）同士の勝率、選出率・選出の傾向・苦手/得意は簡易AIで 3000 党を集計した値です。すべてシミュレーションによる参考値です。`,
    advNote: (n: number, k: number) => `相手 ${n} 党×${k} 戦`,
    approx: '概算（簡易AI）', approxRun: (d: number, t: number) => `本番AIで計算中…${t ? ` ${Math.round((d / t) * 100)}%` : ''}`,
    refGreedy: '（比較対象は簡易AIでの値）',
    tabSum: '概要', tabGuide: '選出ガイド', tabSim: '対戦シミュレーション', tabImp: '改善案',
    overall: '全体の有利度', rank: (n: number, p: number) => `生成した ${MATCHUP_SEASON} のパーティ ${n} 党の中で <b>${p <= 50 ? `上位 ${p}%` : `下位 ${101 - p}%`}</b>`,
    strong: '強み', weak: '弱み・注意点', none: '特になし',
    sStrong: (m: string, d: string) => `${m} がいる相手に強い（${d}）`,
    sWeak: (m: string, d: string) => `${m} がいる相手に弱い（${d}）`,
    oppHd: '対戦相手の候補', whyWeak: (m: string) => `苦手な ${m} を含む相手`, whyMeta: 'よくある相手',
    advVs: '有利度', selHd: '自分の選出', selAuto: '自動（AI）', selManual: '自分で3匹選ぶ',
    selHint: 'タップした順に選出（1番目が先発）', lead: '先発',
    fight: '対戦する', fightRandom: 'ランダムな相手（3000党から）', pickOpp: '上の候補から相手を選んでください', pick3: '3匹選んでください',
    fighting: '対戦中…（1戦 数秒）', battles: '対戦の記録', nth: (n: number) => `第${n}戦`,
    win: '勝ち', lose: '負け', draw: '引き分け', randomTag: 'ランダム',
    mySel: '自分の選出', oppSel: '相手の選出', autoTag: 'AI', manualTag: '手動',     prev: '◀ 前へ', next: '次へ ▶', auto: '▶ 自動再生', stop: '■ 停止', turn: (t: number, n: number) => `ターン ${t} / ${n}`,
        rdSeen: '判明', rdGuess: '推定', rdEv: (s: string) => `${s} 振り`, rdEvMix: '振り方はばらつく',         impBtn: '改善案を計算', impLoading: (s: number) => `計算中…（数分〜十数分かかります・${s}秒経過）`,
    impProg: (d: number, t: number, eta: number | null) => `本番AIで対戦中… ${d}/${t}${eta != null ? `（残り約 ${Math.max(1, Math.round(eta / 60))} 分）` : ''}`,
    impCands: '入れ替え候補を作成中…',
    impNone: '有利度が 3pt 以上・有意に上がる1枠の入れ替えは見つかりませんでした。',
    impBase: (b: string, n: number, k: number) => `今のパーティ: 有利度 ${b}（相手 ${n} 党×${k} 戦）`, impTried: (n: number) => `${n} 通りの入れ替えを本番AIで試算`,
    mega2: 'メガシンカは1試合に1体だけなので、2体目のメガストーンは同時には選出されません（控えの選択肢として効く案です）',
    impFix: '効く相手', impTry: 'この入れ替えを試す', impStale: 'パーティが変わったため試せません（もう一度診断してください）',
    applied: (o: string, i: string) => `${o} を ${i} に入れ替えました`, undo: '入れ替え前に戻す',
    quotaDiag: (n: number) => `本日の無料の診断（${n}パーティ）を使い切りました。日本時間の0時に戻ります。`, quotaBattle: (n: number) => `本日の無料の対戦（${n}戦）を使い切りました。日本時間の0時に戻ります。`, battleLeft: (n: number) => `今日の無料枠: あと ${n} 戦`, errOld: 'サーバ未対応です（API サーバがパーティ診断に対応していません）', errNet: 'サーバに接続できませんでした', errPfx: 'エラー: ',
      },
  en: {
    head: 'Team Checkup', badge: 'Beta', run: 'Run checkup', rerun: 'Run again',
    needSix: (n: number) => `Add all 6 Pokémon to run the checkup (now ${n})`,
    stale: 'Your team has changed since the checkup. Results below are for the team at that time.',
    loading: 'Checking… (takes tens of seconds)',
    legend: `Opponents are ${MATCHUP_SEASON} teams generated from usage and teammate rates. Edge is the win rate between our battle AI (reduced search); pick rates, tendencies and strengths/weaknesses come from a fast AI over 3,000 teams. All numbers are simulations for reference only.`,
    advNote: (n: number, k: number) => `${n} teams × ${k} battles`,
    approx: 'Estimate (fast AI)', approxRun: (d: number, t: number) => `Computing with the battle AI…${t ? ` ${Math.round((d / t) * 100)}%` : ''}`,
    refGreedy: ' (reference measured with the fast AI)',
    tabSum: 'Overview', tabGuide: 'Pick guide', tabSim: 'Battle sim', tabImp: 'Improvements',
    overall: 'Overall edge', rank: (n: number, p: number) => `<b>${p <= 50 ? `Top ${p}%` : `Bottom ${101 - p}%`}</b> among ${n} generated ${MATCHUP_SEASON} teams`,
    strong: 'Strengths', weak: 'Weaknesses', none: 'Nothing notable',
    sStrong: (m: string, d: string) => `Strong against teams with ${m} (${d})`,
    sWeak: (m: string, d: string) => `Weak against teams with ${m} (${d})`,
    oppHd: 'Opponent candidates', whyWeak: (m: string) => `Has ${m} (a tough matchup)`, whyMeta: 'Common team',
    advVs: 'Edge', selHd: 'Your picks', selAuto: 'Auto (AI)', selManual: 'Pick 3 yourself',
    selHint: 'Tap in order (1st = lead)', lead: 'Lead',
    fight: 'Battle', fightRandom: 'Random opponent (from 3,000 teams)', pickOpp: 'Choose an opponent above', pick3: 'Pick 3 Pokémon',
    fighting: 'Battling… (a few seconds per battle)', battles: 'Battle log', nth: (n: number) => `Battle ${n}`,
    win: 'Win', lose: 'Loss', draw: 'Draw', randomTag: 'Random',
    mySel: 'Your picks', oppSel: 'Opponent picks', autoTag: 'AI', manualTag: 'Manual',     prev: '◀ Prev', next: 'Next ▶', auto: '▶ Auto', stop: '■ Stop', turn: (t: number, n: number) => `Turn ${t} / ${n}`,
        rdSeen: 'Seen', rdGuess: 'Likely', rdEv: (s: string) => `EVs in ${s}`, rdEvMix: 'EV spread varies',         impBtn: 'Find improvements', impLoading: (s: number) => `Calculating… (takes several minutes, ${s}s)`,
    impProg: (d: number, t: number, eta: number | null) => `Battling with the battle AI… ${d}/${t}${eta != null ? ` (about ${Math.max(1, Math.round(eta / 60))} min left)` : ''}`,
    impCands: 'Building swap candidates…',
    impNone: 'No single-slot swap raises the edge by 3pt or more with significance.',
    impBase: (b: string, n: number, k: number) => `Current team: edge ${b} (${n} teams × ${k} battles)`, impTried: (n: number) => `${n} swaps tested with the battle AI`,
    mega2: 'Only one Pokémon can Mega Evolve per battle, so a second Mega Stone is never brought together with the first (it works as a back-up option).',
    impFix: 'Helps against', impTry: 'Try this swap', impStale: 'Team has changed; run the checkup again to try this',
    applied: (o: string, i: string) => `Swapped ${o} for ${i}`, undo: 'Undo swap',
    quotaDiag: (n: number) => `You've used today's free checkups (${n} teams). Resets at midnight JST.`, quotaBattle: (n: number) => `You've used today's free battles (${n}). Resets at midnight JST.`, battleLeft: (n: number) => `Free today: ${n} battles left`, errOld: 'Not supported by the server (API server has no checkup endpoints)', errNet: 'Could not connect to the server', errPfx: 'Error: ',
      },
  ko: {
    head: '파티 진단', badge: '시험판', run: '진단하기', rerun: '다시 진단하기',
    needSix: (n: number) => `6마리를 모두 채우면 진단할 수 있습니다（현재 ${n}마리）`,
    stale: '진단한 뒤 파티가 바뀌었습니다. 아래 결과는 진단 당시 파티 기준입니다.',
    loading: '진단 중…（수십 초 걸립니다）',
    legend: `상대는 사용률・동반율로 생성한 ${MATCHUP_SEASON} 파티입니다. 유리도는 실전 대전 AI(탐색 축소판)끼리의 승률, 선출률・선출 경향・강점/약점은 간이 AI로 3000개 파티를 집계한 값입니다. 모든 수치는 시뮬레이션에 의한 참고값입니다.`,
    advNote: (n: number, k: number) => `상대 ${n}개×${k}전`,
    approx: '개산（간이 AI）', approxRun: (d: number, t: number) => `실전 AI로 계산 중…${t ? ` ${Math.round((d / t) * 100)}%` : ''}`,
    refGreedy: '（비교 대상은 간이 AI 값）',
    tabSum: '개요', tabGuide: '선출 가이드', tabSim: '대전 시뮬레이션', tabImp: '개선안',
    overall: '전체 유리도', rank: (n: number, p: number) => `생성한 ${MATCHUP_SEASON} 파티 ${n}개 중 <b>${p <= 50 ? `상위 ${p}%` : `하위 ${101 - p}%`}</b>`,
    strong: '강점', weak: '약점・주의점', none: '특별히 없음',
    sStrong: (m: string, d: string) => `${m}이(가) 있는 상대에게 강함（${d}）`,
    sWeak: (m: string, d: string) => `${m}이(가) 있는 상대에게 약함（${d}）`,
    oppHd: '대전 상대 후보', whyWeak: (m: string) => `어려운 ${m}을(를) 포함한 상대`, whyMeta: '자주 보이는 상대',
    advVs: '유리도', selHd: '내 선출', selAuto: '자동（AI）', selManual: '직접 3마리 고르기',
    selHint: '탭한 순서대로 선출（1번째가 선봉）', lead: '선봉',
    fight: '대전하기', fightRandom: '랜덤 상대（3000팀 중）', pickOpp: '위 후보에서 상대를 고르세요', pick3: '3마리를 고르세요',
    fighting: '대전 중…（1전 몇 초）', battles: '대전 기록', nth: (n: number) => `제${n}전`,
    win: '승리', lose: '패배', draw: '무승부', randomTag: '랜덤',
    mySel: '내 선출', oppSel: '상대 선출', autoTag: 'AI', manualTag: '수동',     prev: '◀ 이전', next: '다음 ▶', auto: '▶ 자동 재생', stop: '■ 정지', turn: (t: number, n: number) => `턴 ${t} / ${n}`,
        rdSeen: '판명', rdGuess: '추정', rdEv: (s: string) => `${s} 투자`, rdEvMix: '투자 분산',         impBtn: '개선안 계산', impLoading: (s: number) => `계산 중…（수 분 걸립니다・${s}초 경과）`,
    impProg: (d: number, t: number, eta: number | null) => `실전 AI로 대전 중… ${d}/${t}${eta != null ? `（약 ${Math.max(1, Math.round(eta / 60))}분 남음）` : ''}`,
    impCands: '교체 후보 작성 중…',
    impNone: '유리도가 3pt 이상・유의미하게 좋아지는 1칸 교체를 찾지 못했습니다.',
    impBase: (b: string, n: number, k: number) => `현재 파티: 유리도 ${b}（상대 ${n}개×${k}전）`, impTried: (n: number) => `교체 ${n}가지를 실전 AI로 시산`,
    mega2: '메가진화는 한 시합에 1마리뿐이라 2번째 메가스톤은 동시에 선출되지 않습니다（후보 교체 요원으로서 효과가 있는 안입니다）',
    impFix: '효과 있는 상대', impTry: '이 교체 시험하기', impStale: '파티가 바뀌어 시험할 수 없습니다（다시 진단해 주세요）',
    applied: (o: string, i: string) => `${o}을(를) ${i}(으)로 교체했습니다`, undo: '교체 전으로 되돌리기',
    quotaDiag: (n: number) => `오늘의 무료 진단(${n}파티)을 모두 사용했습니다. 일본 시간 0시에 초기화됩니다.`, quotaBattle: (n: number) => `오늘의 무료 대전(${n}전)을 모두 사용했습니다. 일본 시간 0시에 초기화됩니다.`, battleLeft: (n: number) => `오늘 무료: ${n}전 남음`, errOld: '서버 미지원（API 서버가 파티 진단에 대응하지 않습니다）', errNet: '서버에 연결할 수 없습니다', errPfx: '오류: ',
      },
};

type ErrKind = 'old' | 'net' | 'srv' | 'quota';
class ApiError extends Error { kind: ErrKind; quota: any; constructor(kind: ErrKind, msg = '', quota: any = null) { super(msg); this.kind = kind; this.quota = quota; } }

async function post(path: string, body: unknown): Promise<any> {
  let r: Response;
  try {
    r = await fetch(API + path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  } catch (e) { throw new ApiError('net'); }
  if (r.status === 404 || r.status === 405 || r.status === 501) throw new ApiError('old');
  if (r.status === 429) {
    const q = await r.json().catch(() => null);
    throw new ApiError(q && q.quota ? 'quota' : 'srv', (q && q.error) || 'HTTP 429', q && q.quota);
  }
  if (!r.ok) throw new ApiError('srv', `HTTP ${r.status}`);
  let d: any;
  try { d = await r.json(); } catch (e) { throw new ApiError('srv', 'bad json'); }
  if (d && d.error) throw new ApiError('srv', String(d.error));
  return d;
}

let ICONS: Record<string, string> | null = null;
let iconsP: Promise<void> | null = null;
function loadIcons(): Promise<void> {
  if (!iconsP) iconsP = fetch('/sim-data/icons.json').then((r) => r.json()).then((d) => { ICONS = d; }).catch(() => { ICONS = {}; });
  return iconsP;
}
const REGIONAL: [string, number][] = [['ヒスイ', 3], ['ガラル', 3], ['アローラ', 4], ['パルデア', 4]];
function iconId(name: string): string | null {
  if (!ICONS || !name) return null;
  let n = normalizeSuggestSpeciesName(name).replace(' (', '(');
  if (ICONS[n]) return ICONS[n];
  if (n.startsWith('メガ')) n = n.slice(2).replace(/[XYZ]$/, '');
  const base = n.split(/[(:]/)[0].trim();
  if (ICONS[n] || ICONS[base]) return ICONS[n] || ICONS[base];
  for (const [p, l] of REGIONAL) if (n.startsWith(p)) { const id = ICONS[n.slice(l) + '(' + p + ')'] || ICONS[n.slice(l).split('(')[0]]; if (id) return id; }
  const k = Object.keys(ICONS).find((kk) => kk.split('(')[0].trim() === base);
  return k ? ICONS[k] : null;
}

export function initDiag(el: HTMLElement, host: DiagHost) {
  const { lang, esc } = host;
  const I = T[lang];
  const tP = (n: string) => host.tPoke(normalizeSuggestSpeciesName(n));
  const ico = (n: string, cls = 'dg-ico') => {
    const id = iconId(n);
    const dn = esc(tP(n));
    return id ? `<img class="${cls}" src="/images/pokemon/pokemon-${id}.webp" alt="${dn}" title="${dn}" onerror="this.style.display='none'">` : '';
  };
  const mon = (n: string, cls = 'dg-ico') => `<span class="dg-mon">${ico(n, cls)}<span>${esc(tP(n))}</span></span>`;
  const logTr = makeLogTranslator(lang, { ...host.maps, tPoke: host.tPoke, tItem: host.tItem });
  const paren = (s: string) => (lang === 'en' ? ` (${esc(s)})` : `（${esc(s)}）`);
  const pt = (d: number) => `${d < 0 ? '−' : '+'}${Math.abs(d * 100).toFixed(1)}pt`;
  const errMsg = (e: any) => (e && e.kind === 'quota' ? esc(e.quota.kind === 'diag' ? I.quotaDiag(e.quota.limit) : I.quotaBattle(e.quota.limit))
    : e && e.kind === 'old' ? I.errOld : e && e.kind === 'net' ? I.errNet : I.errPfx + esc((e && e.message) || ''));
  const evShort = (ev: string) => ev.split('/').map((v, i) => (+v ? `${EVK[i]}${v}` : '')).filter(Boolean).join(' ') || '—';
  const specName = (spec: string) => spec.split('@')[0];
  function specSummary(spec: string) {
    const at = spec.indexOf('@');
    const [item, nature, moves, ev, abil] = spec.slice(at + 1).split(':');
    return `${esc(host.tItem(item) || '—')}・${esc(host.tNature(nature))}・${esc(host.tAbil(abil))}・${evShort(ev)}<br>${moves.split('|').map((m) => esc(host.tMove(m))).join(' / ')}`;
  }

  const st: any = {
    specs: null, key: '', data: null, loading: false, err: null, tab: 'sum',
    opp: null, selMode: 'auto', mySel: [], battles: [], cur: -1, turn: 0, timer: null, fighting: false,
    imp: null, impLoading: false, impErr: null, impT0: 0, impTimer: null, impJob: null, applied: null, advTimer: null, advJob: null,
  };
  const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
  async function pollJob(job: any, key: string, onTick: (j: any) => void): Promise<any> {
    let j = job;
    while (j && j.state !== 'done' && j.state !== 'error') {
      onTick(j);
      if (key !== st.key) return null;
      // サーバは終わるか wait 秒経つまで返さない（その間だけ本番の CPU が割り当てられる）
      const t0 = Date.now();
      j = await post('/job_status', { job: j.job, wait: 5 });
      if (Date.now() - t0 < 1000 && j && j.state !== 'done' && j.state !== 'error') await sleep(1000);
    }
    if (j && j.state === 'error') throw new ApiError('srv', String(j.error || ''));
    return j ? j.result : null;
  }

  el.innerHTML = `<div class="dg">
    <div class="dg-top"><h2 class="dg-h2">${esc(I.head)}<span class="dg-badge">${esc(I.badge)}</span></h2>
      <button type="button" class="btn" id="dg-run">${esc(I.run)}</button></div>
    <div class="muted dg-reason" id="dg-reason"></div>
    <div class="dg-stale" id="dg-stale" hidden>${esc(I.stale)}</div>
    <div id="dg-body"></div></div>`;
  const $ = (id: string) => el.querySelector('#' + id) as HTMLElement;
  $('dg-run').addEventListener('click', () => runDiagnose());

  function refresh() {
    const { specs, filled } = host.getSpecs();
    const btn = $('dg-run') as HTMLButtonElement;
    btn.disabled = !specs || st.loading;
    btn.textContent = st.data ? I.rerun : I.run;
    $('dg-reason').textContent = specs ? '' : I.needSix(filled);
    const key = specs ? specs.join('\n') : '';
    $('dg-stale').hidden = !(st.data && key !== st.key);
    const tryBtns = el.querySelectorAll<HTMLButtonElement>('.dg-try');
    tryBtns.forEach((b) => { b.disabled = key !== st.key; b.title = key !== st.key ? I.impStale : ''; });
  }

  async function runDiagnose() {
    const { specs } = host.getSpecs();
    if (!specs || st.loading) return;
    stopAuto();
    if (st.impTimer) clearInterval(st.impTimer);
    Object.assign(st, { specs, key: specs.join('\n'), loading: true, err: null, data: null, opp: null, mySel: [], battles: [], cur: -1, imp: null, impErr: null, impLoading: false, impJob: null, advJob: null, applied: null });
    renderBody(); refresh();
    track('diag_run', { again: !!st.ranOnce });
    st.ranOnce = true;
    const t0 = performance.now();
    try {
      const [d] = await Promise.all([post('/diagnose', { specs }), loadIcons()]);
      if (st.key !== specs.join('\n')) return;
      st.data = d;
      if (d.quota) st.quota = d.quota;
      const pct = d.rank && typeof d.rank.pct === 'number' ? Math.max(1, Math.round(d.rank.pct * 100)) : null;
      track('diag_result', { ms: Math.round(performance.now() - t0), approx: !!(d.adv && d.adv.approx), top_pct: pct === null ? -1 : pct <= 10 ? 10 : pct <= 30 ? 30 : pct <= 50 ? 50 : 100 });
    } catch (e: any) { st.err = e; track('diag_error', { at: 'diagnose', kind: (e && e.kind) || 'js' }); }
    st.loading = false;
    renderBody(); refresh();
    if (st.data && st.data.adv_job) pollAdv(st.data.adv_job);
    if (st.data && st.data.opps_job) pollOpps(st.data.opps_job);
  }

  // 相手候補の有利度は簡易AIの概算で先に出し、精密AIの測り直しが終わったら差し替える（診断の待ち時間の7割）
  async function pollOpps(job: any) {
    const key = st.key;
    st.oppsFailed = false;
    try {
      const r = await pollJob(job, key, () => {});
      if (!r || key !== st.key) return;
      st.data.opps = r.opps;
    } catch (e: any) { if (key === st.key) st.oppsFailed = true; track('diag_error', { at: 'opps', kind: (e && e.kind) || 'js' }); }
    if (key === st.key && st.tab === 'sim' && $('dg-pane') && !st.fighting) renderSim();
  }

  async function pollAdv(job: any) {
    const key = st.key;
    const tick = (j: any) => { st.advJob = j; const m = el.querySelector('#dg-adv-run'); if (m) m.textContent = I.approxRun(j.done || 0, j.total || 0); };
    const t0 = performance.now();
    try {
      const r = await pollJob(job, key, tick);
      if (!r || key !== st.key) return;
      Object.assign(st.data, { adv: r.adv, rank: r.rank });
      st.data.guide.adv = r.adv.adv;
      track('diag_adv_done', { ms: Math.round(performance.now() - t0) });
    } catch (e: any) { if (key === st.key && st.data) st.data.adv.failed = true; track('diag_error', { at: 'adv', kind: (e && e.kind) || 'js' }); }
    if (key === st.key && (st.tab === 'sum' || st.tab === 'guide') && $('dg-pane')) renderPane();
  }

  function renderBody() {
    const body = $('dg-body');
    if (st.loading) { body.innerHTML = `<div class="ps-loading"><div class="ps-spinner"></div><div class="ps-lmsg">${esc(I.loading)}</div></div>`; return; }
    if (st.err) { body.innerHTML = `<div class="dg-err">${errMsg(st.err)}</div>`; return; }
    if (!st.data) { body.innerHTML = ''; return; }
    // 改善案（renderImp・/improve）は計算が重いので一旦タブから外している
    const tabs: [string, string][] = [['sum', I.tabSum], ['guide', I.tabGuide], ['sim', I.tabSim]];
    body.innerHTML = `<div class="mtx-legend dg-legend"><span>${esc(I.legend)}</span></div>
      <div class="tabbar dg-tabs">${tabs.map(([k, l]) => `<button type="button" class="tb${st.tab === k ? ' active' : ''}" data-dt="${k}">${esc(l)}</button>`).join('')}</div>
      <div class="dg-pane" id="dg-pane"></div>`;
    body.querySelectorAll<HTMLElement>('[data-dt]').forEach((b) => b.addEventListener('click', () => {
      st.tab = b.dataset.dt;
      track('diag_tab', { tab: st.tab });
      body.querySelectorAll<HTMLElement>('[data-dt]').forEach((x) => x.classList.toggle('active', x === b));
      renderPane();
    }));
    renderPane();
  }

  function renderPane() {
    const pane = $('dg-pane');
    if (!pane) return;
    if (st.tab !== 'sim') stopAuto();
    if (st.tab === 'sum') pane.innerHTML = summaryHtml();
    else if (st.tab === 'guide') pane.innerHTML = guideBody(st.data.guide, { lang, ico, tPoke: tP, esc, legend: (h) => `<div class="mtx-legend"><span>${h}</span></div>` });
    else if (st.tab === 'sim') renderSim();
    else renderImp();
  }

  function summaryHtml() {
    const g = st.data.guide, rk = st.data.rank;
    const strong: string[] = [], weak: string[] = [];
    for (const o of g.strong || []) strong.push(I.sStrong(mon(o.opp, 'dg-ico-s'), pt(o.diff)));
    for (const o of g.weak || []) weak.push(I.sWeak(mon(o.opp, 'dg-ico-s'), pt(o.diff)));
    const list = (arr: string[], cls: string) => arr.length ? `<ul class="dg-ul ${cls}">${arr.map((x) => `<li>${x}</li>`).join('')}</ul>` : `<div class="muted">${esc(I.none)}</div>`;
    const pct = rk && typeof rk.pct === 'number' ? Math.max(1, Math.round(rk.pct * 100)) : null;
    const a = st.data.adv || {};
    const aj = st.advJob || st.data.adv_job || {};
    const advSub = a.approx ? `<span class="dg-sub">${esc(I.approx)}${a.failed ? '' : ` ・<span id="dg-adv-run">${esc(I.approxRun(aj.done || 0, aj.total || 0))}</span>`}</span>`
      : a.n_opp ? `<span class="dg-sub">${esc(I.advNote(a.n_opp, a.k))}${a.se ? ` ±${(a.se * 100).toFixed(1)}pt` : ''}</span>` : '';
    return `<div class="dg-overall"><div class="dg-ov-lb">${esc(I.overall)}</div><div class="dg-ov-v">${gdAdv(g.adv, lang)}</div>${advSub}
        ${pct !== null ? `<div class="dg-rank">${I.rank(rk.ref_n, pct)}${rk.method === 'greedy' ? esc(I.refGreedy) : ''}</div>` : ''}</div>
      <div class="dg-h3">${esc(I.strong)}</div>${list(strong, 'dg-good')}
      <div class="dg-h3">${esc(I.weak)}</div>${list(weak, 'dg-bad')}`;
  }

  // ---- 対戦シミュレーション ----
  function renderSim() {
    const pane = $('dg-pane');
    const opps = st.data.opps || [];
    const oppRows = opps.map((o: any) => `<button type="button" class="dg-opp${st.opp === o.id ? ' sel' : ''}" data-opp="${o.id}">
        <span class="dg-opp-icons">${o.names.map((n: string) => ico(n, 'dg-ico-s')).join('')}</span>
        <span class="dg-opp-meta"><span class="dg-why ${o.why === 'weak' ? 'dg-why-w' : ''}">${o.why === 'weak' && o.focus ? I.whyWeak(esc(tP(o.focus))) : esc(I.whyMeta)}</span>
        <span class="dg-sub">${esc(I.advVs)} ${o.k ? gdAdv(o.adv, lang) : st.oppsFailed ? `${gdAdv(o.adv, lang)} <span class="dg-approx">${esc(I.approx)}</span>` : `<span class="dg-approx">${esc(I.approxRun(0, 0))}</span>`}</span></span></button>`).join('');
    const names = st.specs.map(specName);
    const selChips = names.map((n: string, i: number) => {
      const k = st.mySel.indexOf(i);
      return `<button type="button" class="dg-pick${k >= 0 ? ' on' : ''}" data-pick="${i}">${k >= 0 ? `<span class="dg-ord">${k + 1}</span>` : ''}${ico(n, 'dg-ico-s')}<span>${esc(tP(n))}</span>${k === 0 ? `<span class="dg-lead">${esc(I.lead)}</span>` : ''}</button>`;
    }).join('');
    const manual = st.selMode === 'manual';
    const ready = !st.fighting && (!manual || st.mySel.length === 3);
    const hint = st.fighting ? '' : manual && st.mySel.length < 3 ? I.pick3 : st.opp === null ? I.pickOpp : '';
    const rndRow = `<button type="button" class="dg-opp${st.opp === -1 ? ' sel' : ''}" data-opp="-1"><span class="dg-opp-icons">?</span>
        <span class="dg-opp-meta"><span class="dg-why">${esc(I.fightRandom)}</span></span></button>`;
    const left = st.quota && typeof st.quota.battle_left === 'number' ? st.quota.battle_left : null;
    pane.innerHTML = `<div class="dg-h3">${esc(I.oppHd)}</div><div class="dg-opps">${oppRows}${rndRow}</div>
      <div class="dg-h3">${esc(I.selHd)}</div>
      <div class="dg-mode"><label><input type="radio" name="dg-mode" value="auto" ${manual ? '' : 'checked'}> ${esc(I.selAuto)}</label>
        <label><input type="radio" name="dg-mode" value="manual" ${manual ? 'checked' : ''}> ${esc(I.selManual)}</label></div>
      ${manual ? `<div class="muted">${esc(I.selHint)}</div><div class="dg-picks">${selChips}</div>` : ''}
      <div class="dg-fight-row"><button type="button" class="btn" id="dg-fight" ${ready && st.opp !== null && left !== 0 ? '' : 'disabled'}>${esc(I.fight)}</button>
        <span class="muted">${esc(left === 0 ? I.quotaBattle(st.quota.battle_limit) : hint)}</span></div>
      ${left != null && left > 0 ? `<div class="muted dg-quota">${esc(I.battleLeft(left))}</div>` : ''}
      <div id="dg-blist"></div><div id="dg-replay"></div>`;
    pane.querySelectorAll<HTMLElement>('[data-opp]').forEach((b) => b.addEventListener('click', () => { st.opp = +b.dataset.opp!; renderSim(); }));
    pane.querySelectorAll<HTMLInputElement>('input[name="dg-mode"]').forEach((r) => r.addEventListener('change', () => { st.selMode = r.value; renderSim(); }));
    pane.querySelectorAll<HTMLElement>('[data-pick]').forEach((b) => b.addEventListener('click', () => {
      const i = +b.dataset.pick!, k = st.mySel.indexOf(i);
      if (k >= 0) st.mySel.splice(k, 1); else if (st.mySel.length < 3) st.mySel.push(i);
      renderSim();
    }));
    $('dg-fight').addEventListener('click', () => {
      if (st.opp === -1) fight(Math.floor(Math.random() * ((st.data.guide && st.data.guide.n) || 3000)), true);
      else if (st.opp !== null) fight(st.opp, false);
    });
    renderBattleList();
    renderReplay();
  }

  async function fight(oppId: number, random: boolean) {
    if (st.fighting) return;
    const o = (st.data.opps || []).find((x: any) => x.id === oppId);
    track('diag_fight', { random, why: random ? 'random' : (o && o.why) || 'other', sel: st.selMode, n: st.battles.length + 1 });
    const t0 = performance.now();
    const b: any = { opp: oppId, random, names: o ? o.names : null, seed: Math.floor(Math.random() * 2147483647), mySel: st.selMode === 'manual' ? [...st.mySel] : null, rec: null, err: null };
    st.battles.push(b);
    st.cur = st.battles.length - 1; st.turn = 0; st.fighting = true;
    stopAuto();
    if (st.tab === 'sim') renderSim();
    const key = st.key;
    try {
      const d = await post('/diag_battle', { specs: st.specs, opp: oppId, seed: b.seed, my_sel: b.mySel });
      b.rec = d.record || d;
      if (d.quota) st.quota = d.quota;
      b.names = d.opp_names || b.names;
      b.mySelReal = d.my_sel || b.mySel;
      b.auto = d.auto !== undefined ? d.auto : b.mySel === null;
      track('diag_fight_done', { ms: Math.round(performance.now() - t0), result: b.rec.result === 1 ? 'win' : b.rec.result === 2 ? 'lose' : 'draw', turns: (b.rec.turns || []).length - 1 });
    } catch (e: any) {
      b.err = e; track('diag_error', { at: 'battle', kind: (e && e.kind) || 'js' });
      if (e && e.kind === 'quota') st.quota = { ...(st.quota || {}), battle_left: 0, battle_limit: e.quota.limit };
    }
    st.fighting = false;
    if (key === st.key && st.tab === 'sim' && $('dg-pane')) renderSim();
  }

  function resultOf(b: any) {
    if (!b.rec) return null;
    return b.rec.result === 1 ? ['win', I.win] : b.rec.result === 2 ? ['lose', I.lose] : ['draw', I.draw];
  }

  function renderBattleList() {
    const box = $('dg-blist');
    if (!box || !st.battles.length) { if (box) box.innerHTML = ''; return; }
    const rows = st.battles.map((b: any, i: number) => {
      const r = resultOf(b);
      const tag = b.err ? `<span class="dg-res dg-res-err">!</span>` : r ? `<span class="dg-res dg-res-${r[0]}">${esc(r[1])}</span>` : `<span class="dg-res">${esc(I.fighting)}</span>`;
      return `<button type="button" class="dg-brow${i === st.cur ? ' cur' : ''}" data-b="${i}"><span class="dg-bn">${esc(I.nth(i + 1))}</span>${tag}
        <span class="dg-opp-icons">${(b.names || []).map((n: string) => ico(n, 'dg-ico-xs')).join('')}</span>${b.random ? `<span class="dg-sub">${esc(I.randomTag)}</span>` : ''}</button>`;
    }).reverse().join('');
    box.innerHTML = `<div class="dg-h3">${esc(I.battles)}</div><div class="dg-blist">${rows}</div>`;
    box.querySelectorAll<HTMLElement>('[data-b]').forEach((x) => x.addEventListener('click', () => {
      stopAuto(); st.cur = +x.dataset.b!; st.turn = 0; renderBattleList(); renderReplay();
    }));
  }

  const EV_AX = ['H', 'A', 'B', 'C', 'D', 'S'];
  // 相手の個体カードに足す型の読み：見えたもの（特性・持ち物・技）と、まだ見えていない持ち物・努力値の目安だけ
  function readHtml(pr: any) {
    if (!pr) return '';
    const kn = pr.known || {}, pool = pr.pool;
    const seen = [kn.ability ? esc(host.tAbil(kn.ability)) : '', kn.item ? esc(host.tItem(kn.item)) : '', ...(kn.moves || []).map((m: string) => esc(host.tMove(m)))].filter(Boolean);
    const guess: string[] = [];
    const items = (pool && pool.item) || (pr.marginal && pr.marginal.item) || [];
    if (!kn.item && items.length) guess.push(`${esc(host.tItem(items[0][0]) || '—')} ${Math.round(items[0][1] * 100)}%`);
    const sp: [string, number][] = (pool && pool.spread) || [];
    if (sp.length) {
      const tot = sp.reduce((a, x) => a + x[1], 0) || 1;
      const ax = EV_AX.filter((_, k) => sp.reduce((a, [s, p]) => a + (+s.split(' ')[0].split('/')[k] >= 16 ? p : 0), 0) / tot >= 0.5);
      const nat: Record<string, number> = {};
      for (const [s, p] of sp) { const n = s.split(' ')[1]; nat[n] = (nat[n] || 0) + p; }
      const nb = Object.entries(nat).sort((a, b) => b[1] - a[1])[0];
      guess.push(`${ax.length ? I.rdEv(ax.join('・')) : I.rdEvMix}${nb ? paren(host.tNature(nb[0])) : ''}`);
    }
    if (!seen.length && !guess.length) return '';
    return `<div class="dg-read">${seen.length ? `<div><span class="dg-read-k">${esc(I.rdSeen)}</span>${seen.join(' / ')}</div>` : ''}${guess.length ? `<div><span class="dg-read-k">${esc(I.rdGuess)}</span>${guess.join('・')}</div>` : ''}</div>`;
  }
  let MOVET: Record<string, string> | null = null;
  let movetP: Promise<void> | null = null;
  const loadMoveTypes = () => (movetP ||= fetch('/sim-data/move_types.json').then((r) => r.json()).then((d) => { MOVET = d; }).catch(() => { MOVET = {}; }));
  let curPred: any = null;
  const RP = makeReplay({
    lang, tPoke: tP, tMove: host.tMove, tItem: host.tItem, tAbil: host.tAbil,
    typeName: (x: string) => host.maps.type[x] || x,
    iconUrl: (n: string) => { const id = iconId(n); return id ? `/images/pokemon/pokemon-${id}.webp` : null; },
    moveType: (m: string) => (MOVET ? MOVET[m] : undefined),
    logTr,
    oppExtra: (n: string) => readHtml(curPred && curPred[n]),
  });

  function renderReplay() {
    const box = $('dg-replay');
    if (!box) return;
    const b = st.battles[st.cur];
    if (!b) { box.innerHTML = ''; return; }
    if (b.err) { box.innerHTML = `<div class="dg-err">${errMsg(b.err)}</div>`; return; }
    if (!b.rec) { box.innerHTML = `<div class="ps-loading"><div class="ps-spinner"></div><div class="ps-lmsg">${esc(I.fighting)}</div></div>`; return; }
    if (!MOVET) { loadMoveTypes().then(() => { if ($('dg-replay')) renderReplay(); }); }
    const rec = b.rec, turns = rec.turns || [];
    if (!turns.length) { box.innerHTML = ''; return; }
    st.turn = Math.max(0, Math.min(st.turn, turns.length - 1));
    const t = turns[st.turn], lastIdx = turns.length - 1;
    if (st.turn === lastIdx && lastIdx > 0 && !b.ended) { b.ended = true; track('diag_replay_end', { turns: lastIdx }); }
    const r = resultOf(b)!;
    const selRow = (arr: string[]) => (arr || []).map((n, i) => `${mon(n, 'dg-ico-s')}${i === 0 ? `<span class="dg-lead">${esc(I.lead)}</span>` : ''}`).join('');
    curPred = t.predict && t.predict.side1;
    box.innerHTML = `<div class="dg-rp">
      <div class="dg-selrow"><span class="dg-sub">${esc(I.mySel)}${paren(b.auto ? I.autoTag : I.manualTag)}</span>${selRow(rec.selected1)}</div>
      <div class="dg-selrow"><span class="dg-sub">${esc(I.oppSel)}</span>${selRow(rec.selected2)}</div>
      <div class="dg-ctl"><button type="button" class="pb-btn-sub" data-rp="-1" ${st.turn <= 0 ? 'disabled' : ''} aria-label="${esc(I.prev)}">◀</button>
        <span class="dg-turn">${esc(I.turn(t.turn, turns[lastIdx].turn))}</span>
        <button type="button" class="pb-btn-sub" data-rp="1" ${st.turn >= lastIdx ? 'disabled' : ''} aria-label="${esc(I.next)}">▶</button>
        <button type="button" class="btn" data-rp="auto">${esc(st.timer ? I.stop : I.auto)}</button>
        ${st.turn === lastIdx ? `<span class="dg-res dg-res-${r[0]}">${esc(r[1])}</span>` : ''}</div>
      ${RP.turnHtml(turns, st.turn)}</div>`;
    box.querySelectorAll<HTMLElement>('[data-rp]').forEach((x) => x.addEventListener('click', () => {
      const v = x.dataset.rp;
      const bb = st.battles[st.cur];
      if (bb && !bb.watched) { bb.watched = true; track('diag_replay', { how: v === 'auto' ? 'auto' : 'step' }); }
      if (v === 'auto') { if (st.timer) stopAuto(); else startAuto(); renderReplay(); return; }
      stopAuto(); st.turn += +v!; renderReplay();
    }));
  }
  function startAuto() {
    const b = st.battles[st.cur];
    if (!b || !b.rec) return;
    if (st.turn >= b.rec.turns.length - 1) st.turn = 0;
    st.timer = setInterval(() => {
      const bb = st.battles[st.cur];
      if (!bb || !bb.rec || st.turn >= bb.rec.turns.length - 1 || !$('dg-replay')) { stopAuto(); if ($('dg-replay')) renderReplay(); return; }
      st.turn++; renderReplay();
    }, 1400);
  }
  function stopAuto() { if (st.timer) { clearInterval(st.timer); st.timer = null; } }

  // ---- 改善案 ----
  function renderImp() {
    const pane = $('dg-pane');
    if (!pane) return;
    const undo = st.applied ? `<div class="dg-applied"><span>${esc(I.applied(tP(st.applied.out), tP(st.applied.in)))}</span><button type="button" class="pb-btn-sub" id="dg-undo">${esc(I.undo)}</button></div>` : '';
    let main = '';
    if (st.impLoading) main = `<div class="ps-loading"><div class="ps-spinner"></div><div class="ps-lmsg" id="dg-imp-msg">${esc(impMsg())}</div></div>`;
    else if (st.impErr) main = `<div class="dg-err">${errMsg(st.impErr)}</div>`;
    else if (st.imp) {
      const d = st.imp;
      const cands = (d.cands || []).map((c: any, i: number) => `<div class="dg-imp">
          <div class="dg-imp-hd">${mon(c.out)}<span class="dg-arr">→</span>${mon(c.in)}<span class="dg-gain">${esc(I.advVs)} ${pt(c.diff)}</span><span class="dg-sub">±${(c.se * 100).toFixed(1)}pt</span><span class="dg-sub">${gdRound(d.base)}→${gdRound(c.adv)}</span></div>
          <div class="dg-spec">${specSummary(c.spec)}</div>
          ${c.mega2 ? `<div class="dg-sub">※ ${esc(I.mega2)}</div>` : ''}
          ${(c.fixes || []).length ? `<div class="dg-fix"><span class="dg-sub">${esc(I.impFix)}:</span> ${c.fixes.map((f: any) => `${mon(f.opp, 'dg-ico-xs')} <b class="dg-gain-s">${pt(f.diff)}</b>`).join(' ')}</div>` : ''}
          <button type="button" class="pb-btn-sub dg-try" data-try="${i}">${esc(I.impTry)}</button></div>`).join('');
      main = `<div class="dg-sub">${esc(I.impBase(gdRound(d.base), d.n_opp, d.k))}${d.n_cand ? `・${esc(I.impTried(d.n_cand))}` : ''}</div>${cands || `<div class="muted dg-imp-none">${esc(I.impNone)}</div>`}`;
    }
    pane.innerHTML = `${undo}<div class="dg-fight-row"><button type="button" class="btn" id="dg-imp-run" ${st.impLoading ? 'disabled' : ''}>${esc(I.impBtn)}</button></div>${main}`;
    $('dg-imp-run').addEventListener('click', runImprove);
    const u = el.querySelector('#dg-undo');
    if (u) u.addEventListener('click', () => { const a = st.applied; st.applied = null; host.restoreSlot(a.slot, a.prev); renderImp(); refresh(); });
    pane.querySelectorAll<HTMLElement>('[data-try]').forEach((b) => b.addEventListener('click', () => {
      const c = st.imp.cands[+b.dataset.try!];
      const prev = host.applySpec(c.slot, c.spec);
      if (prev) st.applied = { slot: c.slot, prev, out: c.out, in: c.in };
      renderImp(); refresh();
    }));
    refresh();
  }
  function impMsg() {
    const j = st.impJob;
    if (j && j.state === 'cands') return I.impCands;
    if (j && j.state === 'run' && j.total) return I.impProg(j.done, j.total, j.eta != null ? j.eta : null);
    return I.impLoading(Math.round((Date.now() - st.impT0) / 1000));
  }
  async function runImprove() {
    if (st.impLoading) return;
    track('diag_improve');
    Object.assign(st, { impLoading: true, impErr: null, imp: null, impJob: null, impT0: Date.now() });
    const key = st.key;
    st.impTimer = setInterval(() => { const m = el.querySelector('#dg-imp-msg'); if (m) m.textContent = impMsg(); }, 1000);
    if (st.tab === 'imp') renderImp();
    try {
      const d = await post('/improve', { specs: st.specs });
      st.imp = d.cands ? d : await pollJob(d, key, (j) => { st.impJob = j; });
    } catch (e) { st.impErr = e; }
    clearInterval(st.impTimer);
    if (key !== st.key) return;
    st.impLoading = false;
    if (st.tab === 'imp' && $('dg-pane')) renderImp();
  }

  refresh();
  return { refresh };
}
