// 選出ガイドの描画（簡単構築・工房の診断で共有）と、対戦記録のログ翻訳表（観戦ビューア・工房の診断で共有）。
export const GUIDE_I18N: Record<'ja' | 'en' | 'ko', any> = {
  ja: {
    bandGood: '◎ 有利', bandOk: '○ やや有利', bandMid: '△ 五分', bandSlBad: '▲ やや不利', bandBad: '× 不利',
    gdHead: n => `相手 ${n} 党（使用率・同居率から作った M-6 のパーティ）全体への有利度`,
    gdTrios: 'よく選ぶ3匹', gdTrioShare: p => `選ぶ割合 ${p}`, gdTrioAdv: 'この組の有利度',
    gdMembers: '各ポケモンの選出率・先発率', gdSel: '選出率', gdLead: '先発率',
    gdRules: '相手にこれがいたら', gdOppShare: p => `相手の${p}に入る`, gdAdd: '入れる', gdDrop: '外す',
    gdNoRules: '相手のパーティによって選出を大きく変える必要はありません。',
    gdWeak: '苦手な相手', gdStrong: '得意な相手', gdWhen: p => `いるときの有利度 ${p}`,
    gdLegend: n => `相手は使用率・同居率から作った M-6 のパーティ ${n} 党。選出は相手のパーティを見て AI（学習した選出）が決めたものです。<b>有利度</b>＝その選出で戦ったときの想定勝率（簡易シミュレーションを AI 同士の大量対戦の勝率に合わせて補正した参考値）。◎62%以上 ○56%以上 △50%以上 ▲46%以上 ×それ未満。「入れる／外す」の％は、相手にその種がいないとき→いるときの選出率。表示する傾向は、二つの独立な相手集団の両方で再現したものだけです。`,
  },
  en: {
    bandGood: '◎ Favorable', bandOk: '○ Slight edge', bandMid: '△ Even', bandSlBad: '▲ Slightly behind', bandBad: '× Behind',
    gdHead: n => `Edge against all ${n} opposing teams (M-6 teams generated from usage and teammate rates)`,
    gdTrios: 'Most-picked trios', gdTrioShare: p => `Picked ${p}`, gdTrioAdv: 'Edge with this trio',
    gdMembers: 'Pick rate & lead rate', gdSel: 'Pick rate', gdLead: 'Lead',
    gdRules: 'If the opponent has…', gdOppShare: p => `on ${p} of teams`, gdAdd: 'Bring', gdDrop: 'Leave out',
    gdNoRules: 'No need to change your picks much depending on the opposing team.',
    gdWeak: 'Tough opponents', gdStrong: 'Favorable opponents', gdWhen: p => `Edge when present ${p}`,
    gdLegend: n => `Opponents are ${n} M-6 teams generated from usage and teammate rates. Picks are made by the AI (learned selection) after seeing the opposing team. <b>Edge</b> = estimated win rate with that pick (a quick simulation calibrated to large-scale AI-vs-AI results; for reference only). ◎ 62%+ ○ 56%+ △ 50%+ ▲ 46%+ × below. For Bring / Leave out, the % is the pick rate when that Pokémon is absent → present on the opposing team. Only trends that reproduce in two independent opponent pools are shown.`,
  },
  ko: {
    bandGood: '◎ 유리', bandOk: '○ 약간 유리', bandMid: '△ 반반', bandSlBad: '▲ 약간 불리', bandBad: '× 불리',
    gdHead: n => `상대 ${n}개 파티（사용률・동반율로 만든 M-6 파티） 전체에 대한 유리도`,
    gdTrios: '자주 고르는 3마리', gdTrioShare: p => `고르는 비율 ${p}`, gdTrioAdv: '이 조합의 유리도',
    gdMembers: '포켓몬별 선출률・선봉률', gdSel: '선출률', gdLead: '선봉률',
    gdRules: '상대에게 이 포켓몬이 있으면', gdOppShare: p => `상대의 ${p}에 포함`, gdAdd: '넣기', gdDrop: '빼기',
    gdNoRules: '상대 파티에 따라 선출을 크게 바꿀 필요는 없습니다.',
    gdWeak: '어려운 상대', gdStrong: '유리한 상대', gdWhen: p => `있을 때 유리도 ${p}`,
    gdLegend: n => `상대는 사용률・동반율로 만든 M-6 파티 ${n}개입니다. 선출은 상대 파티를 보고 AI（학습 선출）가 고른 것입니다. <b>유리도</b>＝그 선출로 싸웠을 때의 예상 승률（간이 시뮬레이션을 AI끼리의 대량 대전 승률에 맞춰 보정한 참고값）. ◎62% 이상 ○56% 이상 △50% 이상 ▲46% 이상 ×그 미만. 「넣기／빼기」의 %는 상대에게 그 포켓몬이 없을 때→있을 때의 선출률입니다. 서로 독립된 두 상대 집단 모두에서 재현된 경향만 표시합니다.`,
  },
};

export interface GuideCtx {
  lang: 'ja' | 'en' | 'ko';
  ico: (name: string, cls: string) => string;
  tPoke: (name: string) => string;
  esc: (s: string) => string;
  legend: (html: string) => string;
}

export const gdPct = (p: number) => (p > 0 && p < 0.1 ? (p * 100).toFixed(1) : Math.round(p * 100)) + '%';
export const gdRound = (p: number) => Math.round(p * 100) + '%';
export function gdBand(w: number, lang: 'ja' | 'en' | 'ko'): [string, string] {
  const I = GUIDE_I18N[lang];
  return w >= 0.62 ? [I.bandGood, 'gd-b-good'] : w >= 0.56 ? [I.bandOk, 'gd-b-ok'] : w >= 0.5 ? [I.bandMid, 'gd-b-mid'] : w >= 0.46 ? [I.bandSlBad, 'gd-b-slbad'] : [I.bandBad, 'gd-b-bad'];
}
export function gdAdv(w: number, lang: 'ja' | 'en' | 'ko'): string {
  const [bl, bc] = gdBand(w, lang);
  return `<span class="gd-band ${bc}">${bl}</span><b class="gd-adv">${gdRound(w)}</b>`;
}

export function guideBody(g: any, ctx: GuideCtx): string {
  const I = GUIDE_I18N[ctx.lang];
  const { ico, tPoke, esc } = ctx;
  const adv = (w: number) => gdAdv(w, ctx.lang);
  const gdMon = (n: string, cls = 'gd-ico') => `<span class="gd-mon">${ico(n, cls)}<span class="gd-nm">${esc(tPoke(n))}</span></span>`;
  const trios = (g.trios || []).map((t: any) => `<div class="gd-row"><div class="gd-mons">${t.my.map((n: string) => gdMon(n)).join('')}</div>
    <div class="gd-meta"><span class="gd-sub">${I.gdTrioShare(gdPct(t.share))}</span><span class="gd-sub">${I.gdTrioAdv}</span>${adv(t.adv)}</div></div>`).join('');
  const members = (g.members || []).map((m: any) => `<div class="gd-mrow">${gdMon(m.name)}
    <div class="gd-selc"><span class="gd-bar"><i style="width:${gdRound(m.sel)}"></i></span><b>${gdRound(m.sel)}</b></div><div class="gd-leadc">${gdRound(m.lead)}</div></div>`).join('');
  const chg = (x: any, cls: string, lbl: string) => `<span class="gd-chg ${cls}">${lbl}: ${ico(x.mon, 'gd-ico-s')}<b>${esc(tPoke(x.mon))}</b> ${gdRound(x.without)}→${gdRound(x.with)}</span>`;
  const rules = (g.rules || []).length ? g.rules.map((r: any) => `<div class="gd-row"><div class="gd-cond">${gdMon(r.opp)}<span class="gd-sub">${I.gdOppShare(gdPct(r.share))}</span></div>
    <span class="gd-arr">▶</span><div class="gd-acts">${(r.add || []).map((x: any) => chg(x, 'gd-in', I.gdAdd)).join('')}${(r.drop || []).map((x: any) => chg(x, 'gd-out', I.gdDrop)).join('')}</div></div>`).join('')
    : `<div class="muted gd-none">${I.gdNoRules}</div>`;
  const opps = (arr: any[], hd: string) => (arr || []).length ? `<div class="gd-h">${hd}</div>` + arr.map((o: any) => {
    const d = o.diff * 100;
    return `<div class="gd-row">${gdMon(o.opp)}<span class="gd-diff ${d < 0 ? 'gd-neg' : 'gd-posi'}">${d < 0 ? '−' : '+'}${Math.abs(d).toFixed(1)}pt</span>
      <span class="gd-sub">${I.gdWhen(gdRound(o.adv))}</span><span class="gd-sub">${I.gdOppShare(gdPct(o.share))}</span></div>`;
  }).join('') : '';
  return `${ctx.legend(I.gdLegend(g.n))}
    <div class="gd-base"><div class="gd-base-sub">${I.gdHead(g.n)}</div>${adv(g.adv)}</div>
    ${trios ? `<div class="gd-h">${I.gdTrios}</div>${trios}` : ''}
    <div class="gd-h">${I.gdMembers}</div>
    <div class="gd-mtab"><div class="gd-mrow gd-mhd"><span></span><span>${I.gdSel}</span><span>${I.gdLead}</span></div>${members}</div>
    <div class="gd-h">${I.gdRules}</div>${rules}
    ${opps(g.weak, I.gdWeak)}${opps(g.strong, I.gdStrong)}`;
}

export const SIM_LOG_TERM: Record<string, [string, string]> = {こうげき:['Attack','공격'],ぼうぎょ:['Defense','방어'],とくこう:['Sp. Atk','특수공격'],とくぼう:['Sp. Def','특수방어'],すばやさ:['Speed','스피드'],めいちゅう:['accuracy','명중률'],かいひ:['evasiveness','회피율'],かいひりつ:['evasiveness','회피율'],
  攻撃:['Attack','공격'],防御:['Defense','방어'],特攻:['Sp. Atk','특수공격'],特防:['Sp. Def','특수방어'],素早さ:['Speed','스피드'],
  やけど:['burn','화상'],まひ:['paralysis','마비'],どく:['poison','독'],もうどく:['bad poison','맹독'],ねむり:['sleep','잠듦'],こおり:['freeze','얼음'],こんらん:['confusion','혼란'],
  すなあらし:['sandstorm','모래바람'],あられ:['hail','싸라기눈'],ゆき:['snow','설경'],にほんばれ:['harsh sunlight','쾌청'],あめ:['rain','비'],
  ブレードフォルム:['Blade Forme','블레이드폼'],シールドフォルム:['Shield Forme','실드폼'],マイティフォルム:['Hero Form','마이티폼'],misty:['Misty','미스트'],
  守り:['Protect','방어'],ひるみで動けない:['Flinched','풀죽음'],バインド:['Bind','조이기']};
export const SIM_LOG_REASON: Record<string, [string, string]> = {ターン終了回復:['end-of-turn recovery','턴 종료 시 회복'],反動ダメから判明:['from recoil damage','반동 데미지로 판명'],HP回復から判明:['from HP recovery','HP 회복으로 판명'],タスキ発動:['Focus Sash activated','기합의띠 발동'],はたきおとした:['knocked off','탁쳐서떨구기'],
  持ち物なし:['no held item','지닌 물건 없음'],HP満タン:['HP is full','HP가 가득'],メガストーン:['Mega Stone','메가스톤'],連続使用:['used in succession','연속 사용'],きのみを食べていない:['no Berry eaten','나무열매를 먹지 않음'],相手が先制技を使っていない:['target used no priority move','상대가 선제기를 쓰지 않음'],ゆき状態でない:['not snowing','설경 상태가 아님']};
const _STAT='(こうげき|ぼうぎょ|とくこう|とくぼう|すばやさ|めいちゅう|かいひりつ|かいひ)';
const LOG_RULES: [RegExp, string, string][] = [
  [/^(.+?) に (.+?) で 約(-?\d+)% 減少（残り約(-?\d+)%）$/,'$1 lost ~$3% to $2 (~$4% left)','$1: $2(으)로 약 $3% 감소 (남은 HP 약 $4%)'],
  [/^(.+?) の (.+?) → (.+?) に (\d+) ?ダメ \((\d+)回\)$/,'$1\'s $2 → $3: $4 dmg ($5 hits)','$1의 $2 → $3에게 $4 데미지 ($5회)'],
  [/^(.+?) の (.+?) → (.+?) に (\d+) ?ダメ$/,'$1\'s $2 → $3: $4 dmg','$1의 $2 → $3에게 $4 데미지'],
  [/^(.+?) の技【(.+?)】を確認$/,'$1\'s move [$2] revealed','$1의 기술【$2】 확인'],
  [/^(.+?) の持ち物【(.+?)】が判明（(.+?)）$/,'$1\'s item [$2] revealed ($R3)','$1의 지닌 물건【$2】 판명 ($R3)'],
  [/^(.+?) の特性【(.+?)】が判明$/,'$1\'s ability [$2] revealed','$1의 특성【$2】 판명'],
  [/^(.+?) 登場（(.+?)タイプ）$/,'$1 appeared ($2 type)','$1 등장 ($2 타입)'],
  [/^P(\d)選出: (.+)$/,'P$1 picks: $2','P$1 선출: $2'],
  [/^見せ合い — 相手候補(\d+)体: (.+)$/,'Team preview — $1 opposing candidates: $2','팀 프리뷰 — 상대 후보 $1마리: $2'],
  [/^こうかはばつぐんだ！$/,'It\'s super effective!','효과가 굉장했다!'],
  [/^こうかはいまひとつ…$/,'It\'s not very effective...','효과가 별로인 듯하다...'],
  [/^急所に当たった！$/,'A critical hit!','급소에 맞았다!'],
  [/^天候がおわった！$/,'The weather returned to normal.','날씨가 원래대로 돌아왔다.'],
  [/^雨が降り出した！$/,'It started to rain!','비가 내리기 시작했다!'],
  [/^(.+?) で (\d+) ダメ！ (.+?) は倒れた！$/,'$1: $2 dmg! $3 fainted!','$1: $2 데미지! $3 쓰러짐!'],
  [/^一撃必殺！ (.+?) は倒れた！$/,'It\'s a one-hit KO! $1 fainted!','일격필살! $1 쓰러짐!'],
  [/^(.+?) は倒れた！$/,'$1 fainted!','$1 쓰러짐!'],
  [/^(.+?) が登場した！$/,'$1 was sent out!','$1 등장!'],
  [/^(.+?) が出てきた！$/,'$1 came out!','$1 등장!'],
  [/^(.+?) は引っ込んだ！$/,'$1 was withdrawn!','$1 교체되어 돌아감!'],
  [/^(.+?) はメガ進化した！$/,'$1 Mega Evolved!','$1 메가진화!'],
  [/^(.+?) は体力を回復した！$/,'$1 restored its HP!','$1 체력 회복!'],
  [/^(.+?) はねむって体力を回復した！$/,'$1 slept and restored its HP!','$1 잠들어서 체력 회복!'],
  [new RegExp('^(.+?) の (.+?)！ (.+?) の '+_STAT+' が下がった！$'),'$1\'s $2! $3\'s $4 fell!','$1의 $2! $3의 $4 하락!'],
  [/^(.+?) の (.+?)！ (.+?) の攻撃が下がった！$/,'$1\'s $2! $3\'s Attack fell!','$1의 $2! $3의 공격 하락!'],
  [/^(.+?) の (.+?)！ (.+?) の素早さが下がった！$/,'$1\'s $2! $3\'s Speed fell!','$1의 $2! $3의 스피드 하락!'],
  [/^(.+?) の (.+?)！ しかし (.+?) の (.+?) で攻撃が上がった！$/,'$1\'s $2! But $3\'s $4 raised its Attack!','$1의 $2! 하지만 $3의 $4(으)로 공격 상승!'],
  [new RegExp('^(.+?) の '+_STAT+' が上がった！$'),'$1\'s $2 rose!','$1의 $2 상승!'],
  [new RegExp('^(.+?) の '+_STAT+' が下がった！$'),'$1\'s $2 fell!','$1의 $2 하락!'],
  [new RegExp('^(.+?) は (.+?) で '+_STAT+' が下がった！$'),'$1\'s $3 fell due to $2!','$1: $2(으)로 $3 하락!'],
  [/^(.+?) の能力が上がった！$/,'$1\'s stats rose!','$1의 능력 상승!'],
  [/^(.+?) の (.+?)！ (攻撃|防御|特攻|特防|素早さ)が上がった！$/,'$1\'s $2! $3 rose!','$1의 $2! $3 상승!'],
  [/^(.+?) の (.+?)！ (攻撃|防御|特攻|特防|素早さ)が大きく上がった！$/,'$1\'s $2! $3 rose sharply!','$1의 $2! $3 크게 상승!'],
  [/^(.+?) の (.+?)！ (攻撃|防御|特攻|特防|素早さ)が大幅に上がった！$/,'$1\'s $2! $3 rose drastically!','$1의 $2! $3 매우 크게 상승!'],
  [new RegExp('^(.+?) の (.+?)！ '+_STAT+'↑↑ '+_STAT+'↓$'),'$1\'s $2! $3↑↑ $4↓','$1의 $2! $3↑↑ $4↓'],
  [/^(.+?) の (.+?)！ (防御|攻撃|特攻|特防|素早さ)↓ (防御|攻撃|特攻|特防|素早さ)↑↑$/,'$1\'s $2! $3↓ $4↑↑','$1의 $2! $3↓ $4↑↑'],
  [/^(.+?) は (.+?)！こうげきとぼうぎょが上がり、すばやさが下がった！$/,'$1 used $2! Attack and Defense rose, Speed fell!','$1의 $2! 공격과 방어 상승, 스피드 하락!'],
  [/^(.+?) は (.+?) した！急所に当たりやすくなった！$/,'$1 used $2! It\'s getting pumped!','$1의 $2! 급소에 맞히기 쉬워졌다!'],
  [/^(.+?) の (.+?) で能力が下がらなかった！$/,'$1\'s $2 prevents its stats from being lowered!','$1의 $2(으)로 능력이 떨어지지 않았다!'],
  [/^(.+?) の (.+?) で攻撃が下がらなかった！$/,'$1\'s $2 prevents its Attack from being lowered!','$1의 $2(으)로 공격이 떨어지지 않았다!'],
  [/^(.+?) の (.+?) で HPが (\d+) 回復した！$/,'$1 restored $3 HP with $2!','$1: $2(으)로 HP $3 회복!'],
  [/^(.+?) の (.+?) が発動！ HPが (\d+) 回復した！$/,'$1\'s $2 activated! Restored $3 HP!','$1의 $2 발동! HP $3 회복!'],
  [/^(.+?) の (.+?)！ HPが (\d+) 回復した！$/,'$1\'s $2! Restored $3 HP!','$1의 $2! HP $3 회복!'],
  [/^(.+?) の (.+?)！ (\d+)回復$/,'$1\'s $2! Restored $3 HP','$1의 $2! $3 회복'],
  [/^(.+?) は (.+?) で (\d+) 回復した！$/,'$1 restored $3 HP from $2!','$1: $2(으)로 $3 회복!'],
  [/^(.+?) の (.+?) が叶った！（\+(\d+)HP）$/,'$1\'s $2 came true! (+$3 HP)','$1의 $2 실현! (+$3 HP)'],
  [/^(.+?) は (\d+)HP (?:を)?吸収した！$/,'$1 drained $2 HP!','$1: HP $2 흡수!'],
  [/^(.+?) は わるあがき の反動を受けた！\((\d+)\)$/,'$1 is damaged by recoil from Struggle! ($2)','$1: 발버둥 반동 데미지! ($2)'],
  [/^(.+?) は反動を受けた！\((\d+)\)$/,'$1 is damaged by recoil! ($2)','$1: 반동 데미지! ($2)'],
  [/^(.+?) は ?(.+?)の効果を受けた！\((\d+)\)$/,'$1 is hurt by $2! ($3)','$1: $2 데미지! ($3)'],
  [/^(.+?) は (.+?) の攻撃を受けた！\((\d+)\)$/,'$1 took the $2 attack! ($3)','$1: $2 공격을 받았다! ($3)'],
  [/^(.+?) は (.+?) のダメージを受けた！\((\d+)\)$/,'$1 is hurt by $2! ($3)','$1: $2 데미지! ($3)'],
  [/^(.+?) は (.+?) で (\d+) のダメージを受けた！$/,'$1 took $3 damage from $2!','$1: $2(으)로 $3 데미지!'],
  [/^(.+?) は激しく地面に叩きつけられた！\((\d+)\)$/,'$1 kept going and crashed! ($2)','$1: 기세 좋게 땅에 부딪쳤다! ($2)'],
  [/^(.+?) の (.+?)！ (.+?) に (\d+) のダメージ！$/,'$1\'s $2! $3 took $4 damage!','$1의 $2! $3에게 $4 데미지!'],
  [/^(.+?) の (.+?) が破れた！\((\d+)\)$/,'$1\'s $2 was busted! ($3)','$1의 $2 해제! ($3)'],
  [/^(.+?) の (.+?) で (.+?) タイプになった！$/,'$1\'s $2 changed it to the $3 type!','$1의 $2! $3 타입이 되었다!'],
  [/^(.+?) は (.+?) で (.+?) タイプになった！$/,'$1 became the $3 type due to $2!','$1: $2(으)로 $3 타입이 되었다!'],
  [/^(.+?) は (.+?) タイプなので (.+?) は効かない！$/,'$1 is $2 type, so $3 has no effect!','$1: $2 타입이라 $3 효과 없음!'],
  [/^(.+?) の ?(.+?) で耐えた！$/,'$1 hung on using its $2!','$1: $2 덕분에 버텼다!'],
  [/^(.+?) の (.+?) は外れた！$/,'$1\'s $2 missed!','$1의 $2 빗나감!'],
  [/^(.+?) の ?(.+?) は失敗した！（(.+?)）$/,'$1\'s $2 failed! ($R3)','$1의 $2 실패! ($R3)'],
  [/^(.+?) の ?(.+?) は失敗した！$/,'$1\'s $2 failed!','$1의 $2 실패!'],
  [/^しかし (.+?) は失敗した！（(.+?)）$/,'But $1 failed! ($R2)','하지만 $1 실패! ($R2)'],
  [/^わるあがき は (.+?) に効かない…$/,'Struggle doesn\'t affect $1...','발버둥: $1에게는 효과가 없다...'],
  [/^(.+?) は (.+?) に効かない…$/,'$1 doesn\'t affect $2...','$1: $2에게는 효과가 없다...'],
  [/^しかし (.+?) には効かなかった…$/,'But it doesn\'t affect $1...','하지만 $1에게는 효과가 없었다...'],
  [/^(.+?) には効かない！$/,'It doesn\'t affect $1!','$1에게는 효과가 없다!'],
  [/^(.+?) には (.+?) が効かない！$/,'$2 doesn\'t affect $1!','$1에게는 $2 효과가 없다!'],
  [/^(.+?) の (.+?) は (.+?) に効かなかった！$/,'$1\'s $2 didn\'t affect $3!','$1의 $2: $3에게는 효과가 없었다!'],
  [/^(.+?) の (.+?)！ (.+?) は効かない！$/,'$1\'s $2! $3 has no effect!','$1의 $2! $3 효과 없음!'],
  [/^(.+?) の (.+?) は (.+?) に防がれた！$/,'$1\'s $2 was blocked by $3!','$1의 $2 → $3에게 막혔다!'],
  [/^(.+?) の (.+?) で防いだ！$/,'$1 blocked it with $2!','$1: $2(으)로 막았다!'],
  [/^(.+?) は身を守っている！$/,'$1 protected itself!','$1: 방어 태세!'],
  [/^(.+?) は (.+?) ?に変化した！$/,'$1 changed to $2!','$1: $2(으)로 변화!'],
  [/^(.+?) は (.+?) を使った！$/,'$1 used $2!','$1의 $2!'],
  [/^(.+?) は (.+?) をした！$/,'$1 used $2!','$1의 $2!'],
  [/^(.+?) は (.+?) にした！$/,'$1 used $2!','$1의 $2!'],
  [/^(.+?) は (.+?) を放った！$/,'$1 foresaw an attack with $2!','$1의 $2!'],
  [/^(.+?) は (.+?) を聞いた！$/,'$1 heard the $2!','$1: $2(을)를 들었다!'],
  [/^(.+?) は (.+?) を使って倒れた！$/,'$1 used $2 and fainted!','$1: $2 사용 후 쓰러짐!'],
  [/^(.+?) は (.+?) で倒れた！$/,'$1 fainted due to $2!','$1: $2(으)로 쓰러짐!'],
  [/^(.+?) は (.+?) に巻き込まれた！$/,'$1 was taken down by $2!','$1: $2에 휘말렸다!'],
  [/^(.+?) は (.+?) を繰り返すことになった！$/,'$1 is locked into $2!','$1: $2만 쓸 수 있게 되었다!'],
  [/^(.+?) は (.+?) を作った！（HP -(\d+)）$/,'$1 put in a $2! (HP -$3)','$1: $2 생성! (HP -$3)'],
  [/^(.+?) は HP が足りなくて (.+?) を作れない！$/,'$1 doesn\'t have enough HP to make a $2!','$1: HP가 부족해서 $2(을)를 만들 수 없다!'],
  [/^(.+?) には すでに (.+?) がある！$/,'$1 already has a $2!','$1에게는 이미 $2(이)가 있다!'],
  [/^(.+?) の (.+?) で (.+?) が壊れた！$/,'$1\'s $2 broke $3!','$1의 $2(으)로 $3 파괴!'],
  [/^(.+?) の (.+?) が壊れた！$/,'$1\'s $2 broke!','$1의 $2 파괴!'],
  [/^(.+?) の (.+?) で (.+?) が吹き飛んだ！$/,'$1\'s $2 blew away $3!','$1의 $2(으)로 $3 제거!'],
  [/^(.+?) の (.+?) で場が綺麗になった！$/,'$1\'s $2 cleared the field!','$1의 $2(으)로 필드가 깨끗해졌다!'],
  [/^(.+?) で全ての能力変化がリセットされた！$/,'All stat changes were eliminated by $1!','$1(으)로 모든 능력 변화가 원래대로 돌아왔다!'],
  [/^(.+?) ?が ?まき散らされた！（(\d+)層）$/,'$1 were scattered! (layer $2)','$1 설치! ($2층)'],
  [/^(.+?)を まき散らした！$/,'$1 was set!','$1 설치!'],
  [/^(.+?)はすでに設置されている！$/,'$1 is already set!','$1 이미 설치됨!'],
  [/^(.+?) の (.+?)！ (.+?) の足元に(.+?)がまかれた！$/,'$1\'s $2! $4 were scattered at $3\'s feet!','$1의 $2! $3의 발밑에 $4 설치!'],
  [/^(.+?) が張られた！$/,'$1 went up!','$1 발동!'],
  [/^(.+?) が発動した！$/,'$1 took effect!','$1 발동!'],
  [/^(.+?) の (.+?) が発動！$/,'$1\'s $2 activated!','$1의 $2 발동!'],
  [/^(.+?) が解除された！$/,'$1 ended!','$1 해제!'],
  [/^(.+?) の効果が切れた！$/,'$1 wore off!','$1 효과 종료!'],
  [/^(.+?) はすでに効果中！$/,'$1 is already in effect!','$1 이미 효과 중!'],
  [/^(.+?)が広がった！$/,'$1 spread!','$1 전개!'],
  [/^(.+?) フィールドが終わった！$/,'$1 Terrain ended!','$1필드 종료!'],
  [/^(.+?) が吹き始めた！（(\d+)ターン）$/,'$1 began to blow! ($2 turns)','$1 시작! ($2턴)'],
  [/^(.+?)！ 雪が降り始めた！$/,'$1! It started to snow!','$1! 눈이 내리기 시작했다!'],
  [/^(.+?)！ お互いのHPが均等になった$/,'$1! The battlers shared their pain','$1! 서로의 HP를 나눠 가졌다'],
  [/^(.+?)！ (.+?) と (.+?) のアイテムが入れ替わった！$/,'$1! $2 and $3 swapped items!','$1! $2와(과) $3의 도구가 바뀌었다!'],
  [/^(.+?) の (.+?) カウント：(\d+)$/,'$1\'s $2 count: $3','$1의 $2 카운트: $3'],
  [/^(.+?) 追撃！ (\d+)ダメ$/,'$1 extra hit! $2 dmg','$1 추가타! $2 데미지'],
  [/^(.+?) で (\d+) 追加ダメ！$/,'$1: $2 extra dmg!','$1: 추가 $2 데미지!'],
  [/^(.+?) で (\d+) ダメ！$/,'$1: $2 dmg!','$1: $2 데미지!'],
  [/^(.+?) は (.+?) で (.+?) に呪いをかけた！$/,'$1 used $2 and laid a curse on $3!','$1의 $2! $3에게 저주를 걸었다!'],
  [/^(.+?) に (.+?) が刺さった！$/,'$1 was hit by $2!','$1에게 $2!'],
  [/^(.+?) の (.+?) が叩き落とされた！$/,'$1\'s $2 was knocked off!','$1의 $2 떨어뜨림!'],
  [/^(.+?) の (.+?) は叩き落とせなかった！$/,'$1\'s $2 couldn\'t be knocked off!','$1의 $2(은)는 떨어뜨릴 수 없었다!'],
  [/^(.+?) の (.+?)！ (.+?) がやけどを負った！$/,'$1\'s $2! $3 was burned!','$1의 $2! $3 화상!'],
  [/^(.+?) の (.+?)！ (.+?) (?:は|が) (.+?) (?:した|になった)！$/,'$1\'s $2! $3: $4!','$1의 $2! $3: $4!'],
  [/^(.+?) の (.+?)！ (.+?) の (.+?) が封じられた！$/,'$1\'s $2! $3\'s $4 was disabled!','$1의 $2! $3의 $4 봉인!'],
  [/^(.+?) の (.+?) が (.+?) された！$/,'$1\'s $2 was $3!','$1의 $2: $3!'],
  [/^(.+?) の (.+?) は封じられている！$/,'$1\'s $2 is disabled!','$1의 $2(은)는 봉인되어 있다!'],
  [/^(.+?) の (.+?)！ 能力低下がリセットされた$/,'$1\'s $2! Lowered stats were restored','$1의 $2! 떨어진 능력이 원래대로 돌아왔다'],
  [/^(.+?) の (.+?)！ 目を覚ました$/,'$1\'s $2! It woke up','$1의 $2! 눈을 떴다'],
  [/^(.+?) の (.+?)！ 状態異常が治った$/,'$1\'s $2! Its status was cured','$1의 $2! 상태 이상이 나았다'],
  [/^(.+?) の (.+?)！ 行動制限が解除された$/,'$1\'s $2! Move restrictions were lifted','$1의 $2! 행동 제한이 풀렸다'],
  [/^(.+?) の (.+?)！ (.+?)技がチャージされた！$/,'$1\'s $2! $3-type move charged!','$1의 $2! $3 타입 기술 충전!'],
  [/^(.+?) の (.+?) で (.+?) を跳ね返した！$/,'$1\'s $2 bounced back $3!','$1의 $2(으)로 $3(을)를 튕겨냈다!'],
  [/^(.+?) は (.+?)！ (.+?) の (.+?) になった！$/,'$1\'s $2! It copied $3\'s $4!','$1의 $2! $3의 $4(을)를 복사했다!'],
  [/^(.+?) は (.+?)！ (.+?) に変身した！$/,'$1\'s $2! It transformed into $3!','$1의 $2! $3(으)로 변신했다!'],
  [/^(.+?)が解けた！(.+?) の正体は (.+?) だった！$/,'$1 wore off! $2 was actually $3!','$1 해제! $2의 정체는 $3였다!'],
  [/^(.+?) は (.+?)！(.+?)を残して交代！$/,'$1 used $2! It left a $3 and switched out!','$1의 $2! $3(을)를 남기고 교체!'],
  [/^(.+?) の (.+?) が解けた！$/,'$1 was freed from $2!','$1의 $2 해제!'],
  [/^(.+?) の (.+?) が治った！$/,'$1\'s $2 was cured!','$1의 $2 회복!'],
  [/^(.+?) は (.+?) で ?(.+?)がとけた！$/,'$1\'s $2 thawed it out!','$1: $2(으)로 얼음이 녹았다!'],
  [/^(.+?) の ?(.+?)がとけた！$/,'$1 thawed out!','$1의 얼음이 녹았다!'],
  [/^(.+?) は かいふくふうじ で (.+?) に失敗した！$/,'$1 can\'t use $2 due to Heal Block!','$1: 회복봉인으로 $2 실패!'],
  [/^(.+?) は かいふくふうじ で回復できない！$/,'$1 can\'t heal due to Heal Block!','$1: 회복봉인으로 회복할 수 없다!'],
  [/^(.+?) は (.+?) (?:中|状態)で (.+?) が使えない！$/,'$1 can\'t use $3 due to $2!','$1: $2 때문에 $3(을)를 쓸 수 없다!'],
  [/^(.+?) は (.+?) 状態になった！$/,'$1 is now affected by $2!','$1: $2 상태가 되었다!'],
  [/^(.+?) は (.+?) で (.+?) になった！$/,'$1 got $3 from $2!','$1: $2(으)로 $3 상태!'],
  [/^(.+?) は ねむって しまった！$/,'$1 fell asleep!','$1 잠들었다!'],
  [/^(.+?) は (.+?) になった！$/,'$1: $2!','$1: $2 상태!'],
  [/^(.+?) はやけどを負った！$/,'$1 was burned!','$1 화상!'],
  [/^(.+?) はねむっている…$/,'$1 is fast asleep.','$1: 쿨쿨 잠들어 있다.'],
  [/^(.+?) は目を覚ました！$/,'$1 woke up!','$1 눈을 떴다!'],
  [/^(.+?) はこおっている！$/,'$1 is frozen solid!','$1: 꽁꽁 얼어 있다!'],
  [/^(.+?) はからだがしびれて うごけない！$/,'$1 is paralyzed! It can\'t move!','$1: 몸이 저려서 움직일 수 없다!'],
  [/^(.+?) はひるんで動けない！$/,'$1 flinched and couldn\'t move!','$1: 풀이 죽어 움직일 수 없다!'],
  [/^(.+?) はひるんだ！$/,'$1 flinched!','$1 풀이 죽었다!'],
  [/^(.+?) は動けない！$/,'$1 can\'t move!','$1 움직일 수 없다!'],
  [/^(.+?) はこんらんした！$/,'$1 became confused!','$1 혼란!'],
  [/^(.+?) は疲れてこんらんした！$/,'$1 became confused due to fatigue!','$1 지쳐서 혼란!'],
  [/^(.+?) はこんらんして自分を傷つけた！$/,'$1 hurt itself in its confusion!','$1 혼란으로 자신을 공격!'],
  [/^(.+?) は強制交代させられた！$/,'$1 was forced out!','$1 강제 교체!'],
  [/^(.+?) は 跳ね返されて追い払われた！$/,'$1 was bounced back and blown away!','$1 튕겨져서 날아갔다!'],
  [/^(.+?) は 追い払われた！$/,'$1 was blown away!','$1 날아갔다!'],
  [/^(.+?) は こうげきしようとしたが 相手がいない！$/,'$1 attacked, but there was no target!','$1: 공격하려 했지만 상대가 없다!'],
  [/^(.+?) は エネルギーをチャージした！$/,'$1 absorbed energy!','$1 에너지 충전!'],
  [/^(.+?) は エネルギーを溜めている！$/,'$1 is storing energy!','$1 에너지를 모으고 있다!'],
  [/^(.+?) は地面に落とされた！$/,'$1 fell straight down!','$1 땅으로 떨어졌다!'],
  [/^(.+?) が (.+?) を吸収した！$/,'$1 absorbed the $2!','$1: $2 흡수!'],
  [/^(.+?) の (.+?)！$/,'$1\'s $2!','$1의 $2!'],
  [/^(.+?) は (.+?)！$/,'$1 used $2!','$1의 $2!'],
];
export const SIM_LOG_RULES_SRC: [string, string, string][] = LOG_RULES.map(([re, en, ko]) => [re.source, en, ko]);

export interface LogMaps { poke: Record<string, string>; move: Record<string, string>; abil: Record<string, string>; item: Record<string, string>; type: Record<string, string>; tPoke: (n: string) => string; tItem: (n: string) => string; }
export function makeLogTranslator(lang: 'ja' | 'en' | 'ko', M: LogMaps): (l: string) => string {
  if (lang === 'ja') return (l) => l;
  const KO = lang === 'ko' ? 1 : 0;
  const tX = (x: string): string => {
    if (x == null || x === '') return x;
    if (x.includes('/')) return x.split('/').map(tX).join('/');
    if (x.includes(', ')) return x.split(', ').map(tX).join(', ');
    if (SIM_LOG_TERM[x]) return SIM_LOG_TERM[x][KO];
    if (M.poke[x] || x.startsWith('メガ')) { const p = M.tPoke(x); if (p !== x) return p; }
    return M.move[x] || M.abil[x] || M.item[x] || M.type[x] || M.tItem(x) || x;
  };
  const rs = (r: string) => {
    if (SIM_LOG_REASON[r]) return SIM_LOG_REASON[r][KO];
    const m = r.match(/^(\d+)ターン目以降$/);
    return m ? (KO ? `${m[1]}턴째 이후` : `turn ${m[1]} or later`) : tX(r);
  };
  return (l) => {
    if (!l) return l;
    const pm = l.match(/^(▷P\d+: ?)/); const pre = pm ? pm[1] : ''; const body = l.slice(pre.length);
    for (const [re, en, ko] of LOG_RULES) { const m = body.match(re); if (m) return pre + (KO ? ko : en).replace(/\$(R?)(\d)/g, (_, r, i) => r ? rs(m[+i]) : tX(m[+i])); }
    return pre + body;
  };
}
