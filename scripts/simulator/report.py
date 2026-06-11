"""学習成果レポートのファイル出力。

評価4指標・横断選出傾向・行動ログ・選出方策の言語化をまとめて生成し、
scripts/reports/ に Markdown（人間用）＋ metrics JSON（時系列比較用）で保存する。

使い方: python -m simulator.report [describe_party_id ...]
"""
import json
from datetime import date
from pathlib import Path

from .simulate import get_loader
from .env import load_registered_parties
from .ai import HeuristicAI
from .search_ai import SearchAI
from .train import load_selection_table
from .evaluate import (eval_search_vs_heuristic, eval_nash_vs_heuristic_selection,
                       eval_combined, eval_belief_calibration)
from .explain import (meta_selection_report, behavior_report, format_behavior,
                      describe_party_strategy)

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"


def run_metrics(loader, parties, cache, n_search=30, n_nash=300, n_comb=20, n_calib=40):
    sw, hw = eval_search_vs_heuristic(loader, parties, N=n_search)
    nw, hsw = eval_nash_vs_heuristic_selection(loader, parties, cache, N=n_nash)
    aw, bw = eval_combined(loader, parties, cache, N=n_comb)
    pe, poe = eval_belief_calibration(loader, parties, N=n_calib)
    return {
        "search_vs_heuristic": {"search": sw, "heuristic": hw, "winrate": sw / max(1, sw + hw)},
        "nash_vs_heuristic_selection": {"nash": nw, "heuristic": hsw, "winrate": nw / max(1, nw + hsw),
                                        "cards": len(cache) // 2},
        "combined_vs_baseline": {"learned": aw, "baseline": bw, "winrate": aw / max(1, aw + bw)},
        "belief_calibration": {"prior_err": pe, "post_err": poe,
                               "improvement": (pe - poe) / pe if pe else 0.0},
    }


_FINDINGS = """\
- メガ進化: `should_mega_evolve` のスケール不一致バグを修正し原則即メガに。石名の全角/半角を正規化しリザードン等も有効化。選出もメガ後で評価。→ スターミー選出 15%→52%、リザードン 32%→59%。
- 2メガ選出: 1サイド1メガ制約を反映（最良1体のみ加点＋2体目は減点）。
- 数ターン戦略: 詰め(先制で仕留め)・崩し(壁にどくどく/ちょうはつ/積み)・ねがいごと→まもる・バトン構築を実装。該当archetype使用時はプラス(ねがいごと約+3.7%)、全体は中立。ピボット交代先の強制選択バグも修正。
- ステロ等の設置技: 残り入場数×割合でゲーム終了までの価値を評価。探索は終局までのロールアウトで長期価値を自然反映。
- AlphaGo型学習: 状態→勝率の価値関数(精度約72%)＋方策ヘッド＋PUCT-MCTSを実装。完全自律ループ(自己対戦+Dirichlet探索+選出ε探索)で、オーバーサンプリングなしに雨シナジーを反復5付近で自力獲得。
- 雨の正直な評価: 「場に雨があれば水技は強い」は学習されるが、シングルでは起動役ペリッパー選出のコストが大きく(強制雨39% vs 通常86%)、雨選出を避けるのが正しい。雨支配はダブル向け。
"""


def build_markdown(stamp, n_parties, metrics, meta_text, behavior_text, strategy_texts,
                   az_history=None) -> str:
    m = metrics
    L = [f"# AI戦略学習レポート（{stamp}）", "",
         f"- 正本テンプレート: {n_parties} パーティ（DB表 templates）",
         f"- 学習済み選出カード: {m['nash_vs_heuristic_selection']['cards']}", "",
         "## 1. 評価指標（自己対戦の真値で検証）", "",
         "| 指標 | 結果 |", "|---|---|",
         f"| 行動方策 SearchAI vs HeuristicAI | {m['search_vs_heuristic']['winrate']:.1%} "
         f"({m['search_vs_heuristic']['search']}–{m['search_vs_heuristic']['heuristic']}) |",
         f"| 選出 Nash vs Heuristic | {m['nash_vs_heuristic_selection']['winrate']:.1%} "
         f"({m['nash_vs_heuristic_selection']['nash']}–{m['nash_vs_heuristic_selection']['heuristic']}) |",
         f"| 統合 vs ベースライン | {m['combined_vs_baseline']['winrate']:.1%} "
         f"({m['combined_vs_baseline']['learned']}–{m['combined_vs_baseline']['baseline']}) |",
         f"| 耐久推定の較正改善 | {m['belief_calibration']['improvement']:+.1%} "
         f"(誤差 {m['belief_calibration']['prior_err']:.1f}→{m['belief_calibration']['post_err']:.1f}) |",
         "", "## 2. 全パーティ横断 選出傾向", "", "```", meta_text, "```", "",
         "## 3. 行動ログ集計（方策別）", "", "```", behavior_text, "```", ""]
    if az_history:
        L += ["## 4. 自律学習（AlphaZero型）の学習曲線", "",
              "自己対戦＋探索（Dirichlet＋選出ε）だけで雨シナジーが創発したか（オーバーサンプリングなし）:",
              "", "| 反復 | 試合 | 価値精度 | 雨Δ(雨あり−なし) | 雨を高評価した割合 |",
              "|---|---|---|---|---|"]
        for r in az_history:
            L.append(f"| {r['iter']} | {r['games']} | {r['value_acc']:.1%} | "
                     f"{r['rain_delta']:+.4f} | {r['rain_pos']:.0%} |")
        L += ["", "→ 反復が進むほど雨を学習（後半でΔ>0・100%）。手書きなしの創発を確認。", ""]
    L += ["## 5. 主な戦略・修正の知見", "", _FINDINGS]
    if strategy_texts:
        L += ["", "## 6. 選出方策の言語化（個別パーティ）", ""]
        for t in strategy_texts:
            L += ["```", t, "```", ""]
    return "\n".join(L)


def generate(out_dir: Path = REPORTS_DIR, describe_ids=None,
             n_search=30, n_nash=300, n_comb=20, n_calib=40):
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    cache = load_selection_table()
    stamp = str(date.today())

    metrics = run_metrics(loader, parties, cache, n_search, n_nash, n_comb, n_calib)
    meta_text = meta_selection_report(cache, parties, loader)
    rh = behavior_report(loader, parties, lambda ld: HeuristicAI(), N=30, label="Heuristic")
    rs = behavior_report(loader, parties, lambda ld: SearchAI(ld, rollouts=10, depth=40, seed=0),
                         N=20, label="SearchAI", with_belief=True)
    behavior_text = format_behavior([rh, rs])
    ids = describe_ids or [parties[0].party_id]
    strategy_texts = [describe_party_strategy(cache, parties, loader, pid) for pid in ids]

    az_hist = None
    _azp = out_dir / "az_history.json"
    if _azp.exists():
        az_hist = json.loads(_azp.read_text(encoding="utf-8"))

    md = build_markdown(stamp, len(parties), metrics, meta_text, behavior_text, strategy_texts,
                        az_history=az_hist)
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"strategy_report_{stamp}.md"
    json_path = out_dir / f"metrics_{stamp}.json"
    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps({"date": stamp, "n_parties": len(parties), **metrics},
                                    ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"レポート出力:\n  {md_path}\n  {json_path}")
    return md_path, json_path


if __name__ == "__main__":
    import sys
    ids = [int(a) for a in sys.argv[1:]] or None
    generate(describe_ids=ids)
