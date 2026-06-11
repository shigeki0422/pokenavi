"""学習した戦略の言語化（説明可能性）。

- 選出方策: 学習済み選出テーブル（混合戦略）を自然言語に要約。
  どの3体を選ぶ傾向か（コア/状況/不採用）、誰を先頭にするか、相手別の使い分け、
  混合（要ランダム化）か単一（固定選出）かを言語化する。
- 行動方策: SearchAI の各候補行動の推定勝率を出力し「なぜその手か」を説明する。
"""
import math
import random
from collections import Counter
from typing import List

from .env import RegisteredParty, build_party, heuristic_selection
from .ai import HeuristicAI, expected_damage
from .battle import Battle, BattleSide


def _entropy(mix: List[float]) -> float:
    return -sum(p * math.log(p + 1e-12) for p in mix if p > 0)


def _action_label(action, my_side) -> str:
    if action.type == "switch":
        return f"交代→{my_side.party[action.switch_to].name}"
    if action.type == "move":
        return f"わざ「{action.move.name_jp}」" + ("＋メガ進化" if action.do_mega else "")
    return action.type


def describe_party_strategy(cache: dict, parties: List[RegisteredParty], loader,
                            party_id: int, season: str = "M-2") -> str:
    """1パーティの選出方策を言語化する。"""
    by_id = {p.party_id: p for p in parties}
    if party_id not in by_id:
        return f"パーティ{party_id} は未登録です。"
    members = [p.name for p in build_party(by_id[party_id], loader, season)]
    n = len(members)

    sel_rate = [0.0] * n
    lead_rate = [0.0] * n
    matchups = []
    for key, entry in cache.items():
        a, b = key.split("-")
        if int(a) != party_id:
            continue
        opp_id = int(b)
        sels, mix = entry["sels"], entry["mix"]
        for s, p in zip(sels, mix):
            for idx in s:
                sel_rate[idx] += p
            lead_rate[s[0]] += p
        ti = max(range(len(mix)), key=lambda i: mix[i])
        matchups.append((opp_id, sels[ti], mix[ti], _entropy(mix)))

    m = len(matchups)
    if m == 0:
        return f"パーティ{party_id} の学習済みカードがありません。"
    sel_rate = [r / m for r in sel_rate]
    lead_rate = [r / m for r in lead_rate]

    order = sorted(range(n), key=lambda i: -sel_rate[i])
    core = [i for i in order if sel_rate[i] >= 0.8]
    situational = [i for i in order if 0.2 <= sel_rate[i] < 0.8]
    rare = [i for i in order if sel_rate[i] < 0.2]
    lead_order = sorted(range(n), key=lambda i: -lead_rate[i])

    L = []
    L.append(f"=== パーティ{party_id} の選出方策（学習済み {m} カード）===")
    L.append(f"構成6体: {' / '.join(members)}")
    L.append("")
    L.append("■ 採用傾向（相手平均の選出率）")
    if core:
        L.append("  ・コア（ほぼ常に選出）: " + ", ".join(f"{members[i]}({sel_rate[i]:.0%})" for i in core))
    if situational:
        L.append("  ・状況選出（相手次第）: " + ", ".join(f"{members[i]}({sel_rate[i]:.0%})" for i in situational))
    if rare:
        L.append("  ・ほぼ不採用: " + ", ".join(f"{members[i]}({sel_rate[i]:.0%})" for i in rare))
    L.append("")
    L.append("■ 先頭（リード）傾向")
    L.append("  " + ", ".join(f"{members[i]}({lead_rate[i]:.0%})" for i in lead_order if lead_rate[i] > 0.05))
    L.append("")
    L.append("■ 相手別の推奨選出（最有力＋混合度）")
    for opp_id, sel, prob, ent in sorted(matchups, key=lambda x: x[0]):
        names = " / ".join(members[i] for i in sel)
        opp_lead = by_id[opp_id].names[:3]
        kind = "固定選出" if prob >= 0.85 else ("やや混合" if prob >= 0.55 else "要混合(複数択)")
        L.append(f"  vs P{opp_id}({'/'.join(opp_lead)}…): 先頭【{members[sel[0]]}】+ {members[sel[1]]}/{members[sel[2]]} "
                 f"(採用{prob:.0%}, {kind})")
    return "\n".join(L)


def meta_selection_report(cache: dict, parties: List[RegisteredParty], loader,
                          season: str = "M-2") -> str:
    """全パーティ横断の選出傾向を分析する。
    「種族がチームに入っているとき、どれだけ選出されるか」を集計し、
    環境的に強い選出ピース／見せポケ（実選出されない）を抽出する。"""
    by_id = {p.party_id: p for p in parties}
    members_cache = {}

    def members(pid):
        if pid not in members_cache:
            members_cache[pid] = [p.name for p in build_party(by_id[pid], loader, season)]
        return members_cache[pid]

    sel_sum: Counter = Counter()
    sel_cnt: Counter = Counter()
    lead_sum: Counter = Counter()
    for key, entry in cache.items():
        a, _ = key.split("-")
        names = members(int(a))
        sels, mix = entry["sels"], entry["mix"]
        prob_in = [0.0] * len(names)
        prob_lead = [0.0] * len(names)
        for s, p in zip(sels, mix):
            for idx in s:
                prob_in[idx] += p
            prob_lead[s[0]] += p
        for idx, nm in enumerate(names):
            sel_sum[nm] += prob_in[idx]
            sel_cnt[nm] += 1
            lead_sum[nm] += prob_lead[idx]

    rows = []
    for nm in sel_cnt:
        rate = sel_sum[nm] / sel_cnt[nm]
        lead = lead_sum[nm] / sel_cnt[nm]
        rows.append((nm, rate, lead, sel_cnt[nm]))
    rows.sort(key=lambda x: -x[1])

    L = ["=== 全パーティ横断 選出傾向（学習済みカードの集計）==="]
    L.append("（種族がチームに入っているとき平均でどれだけ選出/先頭になるか）")
    L.append("")
    L.append("■ 環境的に強い選出ピース（選出率 上位）")
    for nm, rate, lead, c in rows[:8]:
        L.append(f"  {nm}: 選出{rate:.0%} / 先頭{lead:.0%}（{c}カードで採用候補）")
    L.append("")
    L.append("■ ほぼ見せポケ（選出率 下位）")
    for nm, rate, lead, c in [r for r in rows if r[1] < 0.25][:8]:
        L.append(f"  {nm}: 選出{rate:.0%}（{c}カードで採用候補）")
    return "\n".join(L)


class _RecordingAI:
    """行動を記録するAIラッパー（行動ログ集計用）。"""
    def __init__(self, inner):
        self.inner = inner
        self.total = 0
        self.c: Counter = Counter()

    def __call__(self, my_side, opp_side, field):
        act = self.inner(my_side, opp_side, field)
        self.total += 1
        self.c[act.type] += 1
        if act.type == "move" and act.move is not None:
            if act.move.category == "status":
                self.c["status_move"] += 1
            else:
                self.c["damage_move"] += 1
            if getattr(act.move, "priority", 0) > 0:
                self.c["priority_move"] += 1
            if getattr(act, "do_mega", False):
                self.c["mega"] += 1
            opp = opp_side.active
            if opp.is_alive and act.move.category != "status" and act.move.power:
                if expected_damage(my_side.active, opp, act.move, field) >= opp.hp:
                    self.c["ko_attempt"] += 1
        elif act.type == "switch":
            if my_side.active.is_alive and my_side.active.hp / my_side.active.max_hp < 0.35:
                self.c["low_hp_switch"] += 1
        return act


def behavior_report(loader, parties, make_ai, N: int = 30, label: str = "AI",
                    with_belief: bool = False, season: str = "M-2", seed: int = 0) -> dict:
    """N試合で行動傾向（交代率・KO確保率・先制技率など）を集計する。
    make_ai(loader)→AI。両サイドに同じ方策を使い記録する。"""
    from .belief import OpponentBelief
    rng = random.Random(seed)
    rec1 = _RecordingAI(make_ai(loader))
    rec2 = _RecordingAI(make_ai(loader))
    for _ in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader, season); a2 = build_party(pb, loader, season)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        if with_belief:
            s1.belief = OpponentBelief(loader, season); s2.belief = OpponentBelief(loader, season)
        Battle(s1, s2).run(rec1, rec2)
    tot = rec1.total + rec2.total
    c = rec1.c + rec2.c
    moves = c["move"] or 1
    return {
        "label": label, "decisions": tot,
        "switch_rate": c["switch"] / max(1, tot),
        "move_rate": c["move"] / max(1, tot),
        "status_move_rate": c["status_move"] / moves,
        "priority_move_rate": c["priority_move"] / moves,
        "ko_attempt_rate": c["ko_attempt"] / moves,
        "low_hp_switch": c["low_hp_switch"] / max(1, c["switch"]),
        "mega_rate": c["mega"] / max(1, tot),
    }


def format_behavior(reports: List[dict]) -> str:
    L = ["=== 行動ログ集計（方策別の傾向）==="]
    hdr = f"{'指標':<22}" + "".join(f"{r['label']:>14}" for r in reports)
    L.append(hdr)
    def row(name, key, pct=True):
        cells = "".join((f"{r[key]:>13.0%}" if pct else f"{r[key]:>13}") + " " for r in reports)
        L.append(f"{name:<22}{cells}")
    row("総判断回数", "decisions", pct=False)
    row("交代率", "switch_rate")
    row("わざ率", "move_rate")
    row("├ 変化技率(わざ中)", "status_move_rate")
    row("├ 先制技率(わざ中)", "priority_move_rate")
    row("└ KO狙い率(わざ中)", "ko_attempt_rate")
    row("低HP時の交代率", "low_hp_switch")
    row("メガ進化率", "mega_rate")
    return "\n".join(L)


def explain_turn(search_ai, my_side, opp_side, field, top: int = 6) -> str:
    """SearchAI の1手を、候補行動ごとの推定勝率付きで説明する。"""
    scored = search_ai.score_actions(my_side, opp_side, field)
    if not scored:
        return f"{my_side.active.name}: 候補が1つ以下のため自動選択。"
    scored.sort(key=lambda x: -x[1])
    L = [f"局面: {my_side.active.name}（自分）vs {opp_side.active.name}（相手）",
         f"  相手HP残り: 約{round(opp_side.active.hp / opp_side.active.max_hp * 100)}%"]
    for act, s in scored[:top]:
        L.append(f"  {_action_label(act, my_side)}: 推定勝率 {s:.0%}")
    best = scored[0]
    L.append(f"→ 選択: {_action_label(best[0], my_side)}（推定勝率 {best[1]:.0%}＝最も負けにくい手）")
    return "\n".join(L)
