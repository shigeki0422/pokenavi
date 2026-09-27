// 1v1判定の前提文。3つのポップアップ（静的ページ・工房・簡単構築）で共有する。
//
// 前提には性質の違う2種類があり、置き場所を分けている。
//   対面ごとに変わるもの（天候・いかく・連続回数・ばけのかわ・回復）… 各セルに「効いたときだけ」出す
//   常に同じ前提（下記）………………………………………………………… ヘッダーに畳んで置く
// ヘッダーに列挙を直書きすると、前提が増えるたびに長くなって破綻する
// （実際に「タスキ/がんじょう/ばけのかわ・マルチスケイル・回復・天候を考慮」まで伸びた）。
// 既定は1行、詳しく知りたい人だけ開く形にして、文言はここ1箇所に持つ。
export type Lang = "ja" | "en" | "ko";

/** ヘッダーの1行。既定で表示される。 */
export const MATCHUP_LEAD: Record<Lang, string> = {
  ja: "互いの代表型（4技）で1対1を戦わせた事前計算です。準備の1手（積み技・ねこだまし）、反動・持ち物・特性も対戦どおりに入ります。",
  en: "A pre-computed 1v1 battle between each side's representative build (4 moves), including one setup move (stat boost or Fake Out), recoil, items and abilities as in a real battle.",
  ko: "서로의 대표 빌드(4기술)로 1대1을 싸우게 한 사전 계산입니다. 준비 1수(랭크업기・속이다), 반동・도구・특성도 실제 대전대로 반영됩니다.",
};

/** 開閉ラベル。 */
export const ASSUMPTIONS_LABEL: Record<Lang, string> = {
  ja: "計算の前提",
  en: "Assumptions",
  ko: "계산 전제",
};

/** 展開したときに出す前提の一覧。 */
export const MATCHUP_ASSUMPTIONS: Record<Lang, string[]> = {
  ja: [
    "両者が同時に行動する対戦を回し、先後は毎ターンの素早さと優先度で決めます。交代と、積み技1回・ねこだまし以外の補助技は使いません。",
    "各側は「最大打点の技を撃ち続ける／毎ターン最善の技を選ぶ／準備の1手→攻撃」から、相手の最善の応手に対して最も有利なものを選びます。同じターン数で倒せるなら、反動や能力低下の無い技を優先します。",
    "相手を技で倒した行動の反動等で自分も倒れたときは相打ち（引き分け）です。",
    "判定（記号・勝敗・経過・確定数）はダメージ乱数の中央値で回した対戦で決めます。技ごとのダメージは最低〜最高乱数の幅で表示します。",
    "命中は必中として扱います（命中率は見ません）。",
    "急所と追加効果は、必ず起きるものだけを反映します（必中急所、りゅうせいぐんの特攻ダウン等）。",
    "連続技は回数を固定します。2〜5回の技は期待値の3回、1発ごとに命中判定がある技（トリプルアクセル・ネズミざん）は必中前提なので最大回数です。",
    "カウンター・ミラーコート・メタルバーストは、相手が出す技の種類と威力に依存しすぎるため対象外です。",
    "発数は中央乱数で数えます。最低乱数でも同じ発数なら「確定n」、そうでなければ「乱数n発（その発数以内に倒せる確率）」です。技ごとのダメージは最低〜最高乱数の幅で示します。",
    "個々の計算に効いた条件（天候・フィールド・いかく・耐える効果・回復）は各セルに表示します。",
  ],
  en: [
    "Both sides act each turn in a simulated battle; turn order follows Speed and priority every turn. No switching, and no status moves except one setup move or Fake Out.",
    "Each side picks, against the opponent's best reply, the best of: keep using its strongest move / pick the best move each turn / one setup move then attack. Among moves that KO in the same number of turns, ones without recoil or stat drops are preferred.",
    "If a Pokémon KOs its opponent and faints from that move's recoil etc., it is a double KO (draw).",
    "The verdict (symbol, result, turn-by-turn view and hits to KO) uses a battle at the middle damage roll. Move damage is shown as the min-max roll range.",
    "Moves are treated as always hitting (accuracy is ignored).",
    "Only guaranteed criticals and guaranteed secondary effects apply (e.g. Draco Meteor's Sp. Atk drop).",
    "Multi-hit moves use a fixed count: 3 for 2-5 hit moves (the expected value), and the maximum for moves that roll accuracy per hit (Triple Axel, Population Bomb), since hits always land here.",
    "Counter, Mirror Coat and Metal Burst are excluded: they depend too much on the opponent's move type and power.",
    "Hits to KO are counted at the middle roll: \"KO in n\" if the lowest roll needs the same number, otherwise \"n hits (p%)\" with the chance to KO within n hits. Move damage is shown as the min-max roll range.",
    "Factors that actually affected each number (weather, terrain, Intimidate, survival abilities, healing) are shown in the cells.",
  ],
  ko: [
    "양측이 동시에 행동하는 대전을 돌리며, 선후는 매 턴의 스피드와 우선도로 정합니다. 교체와, 랭크업기 1회・속이다 이외의 변화기는 사용하지 않습니다.",
    "각 측은 '최대 위력기를 계속 사용 / 매 턴 최선의 기술 선택 / 준비 1수 후 공격' 중 상대의 최선의 대응에 대해 가장 유리한 것을 고릅니다. 같은 턴 수로 쓰러뜨릴 수 있다면 반동이나 능력 하락이 없는 기술을 우선합니다.",
    "상대를 쓰러뜨린 기술의 반동 등으로 자신도 쓰러지면 상쇄(무승부)입니다.",
    "판정(기호・승패・경과・확정 수)은 대미지 난수 중앙값으로 돌린 대전으로 정합니다. 기술별 대미지는 최저~최고 난수의 폭으로 표시합니다.",
    "명중은 필중으로 취급합니다(명중률은 보지 않습니다).",
    "급소와 추가 효과는 반드시 발생하는 것만 반영합니다(필중 급소, 유성군의 특공 하락 등).",
    "연속기는 횟수를 고정합니다. 2~5회 기술은 기댓값인 3회, 1발마다 명중 판정이 있는 기술(트리플악셀・쥐어살기)은 필중 전제이므로 최대 횟수입니다.",
    "카운터・미러코트・메탈버스트는 상대가 쓰는 기술의 종류와 위력에 지나치게 의존하므로 제외합니다.",
    "발수는 중앙 난수로 셉니다. 최저 난수에서도 같으면 '확정n', 아니면 '난수n발(그 발수 이내에 쓰러뜨릴 확률)'입니다. 기술별 대미지는 최저~최고 난수 폭으로 표시합니다.",
    "각 계산에 실제로 반영된 조건(날씨・필드・위협・버티기・회복)은 각 칸에 표시됩니다.",
  ],
};
