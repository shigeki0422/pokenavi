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
  ja: "互いの最大打点1発を撃ち合う前提の事前計算です。",
  en: "A pre-calculation assuming both sides keep using their strongest move.",
  ko: "서로 최대 위력기 1발을 계속 사용하는 전제의 사전 계산입니다.",
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
    "交代・補助技・相手の反撃は含みません。",
    "命中は必中として扱います（命中率は見ません）。",
    "急所と追加効果は、必ず起きるものだけを反映します（必中急所、りゅうせいぐんの特攻ダウン等）。",
    "連続技は回数を固定します。2〜5回の技は期待値の3回、1発ごとに命中判定がある技（トリプルアクセル・ネズミざん）は必中前提なので最大回数です。",
    "カウンター・ミラーコート・メタルバーストは、相手が出す技の種類と威力に依存しすぎるため対象外です。",
    "「確定n」は最低乱数でも倒せる保証値、「乱数n発」は最高乱数なら倒せる場合の確率です。",
    "個々の計算に効いた条件（天候・フィールド・いかく・耐える効果・回復）は各セルに表示します。",
  ],
  en: [
    "Switching, status moves and the opponent's counterattack are not included.",
    "Moves are treated as always hitting (accuracy is ignored).",
    "Only guaranteed criticals and guaranteed secondary effects apply (e.g. Draco Meteor's Sp. Atk drop).",
    "Multi-hit moves use a fixed count: 3 for 2-5 hit moves (the expected value), and the maximum for moves that roll accuracy per hit (Triple Axel, Population Bomb), since hits always land here.",
    "Counter, Mirror Coat and Metal Burst are excluded: they depend too much on the opponent's move type and power.",
    "\"KO in n\" is guaranteed even at the lowest roll; \"n hits (p%)\" is the chance at higher rolls.",
    "Factors that actually affected each number (weather, terrain, Intimidate, survival abilities, healing) are shown in the cells.",
  ],
  ko: [
    "교체・변화기・상대의 반격은 포함하지 않습니다.",
    "명중은 필중으로 취급합니다(명중률은 보지 않습니다).",
    "급소와 추가 효과는 반드시 발생하는 것만 반영합니다(필중 급소, 유성군의 특공 하락 등).",
    "연속기는 횟수를 고정합니다. 2~5회 기술은 기댓값인 3회, 1발마다 명중 판정이 있는 기술(트리플악셀・쥐어살기)은 필중 전제이므로 최대 횟수입니다.",
    "카운터・미러코트・메탈버스트는 상대가 쓰는 기술의 종류와 위력에 지나치게 의존하므로 제외합니다.",
    "'확정n'은 최저 난수에서도 쓰러뜨리는 보증값, '난수n발'은 최고 난수라면 쓰러뜨리는 확률입니다.",
    "각 계산에 실제로 반영된 조건(날씨・필드・위협・버티기・회복)은 각 칸에 표시됩니다.",
  ],
};
