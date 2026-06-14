"""Feature 1（対戦評価）の中核。

総当たり＝各ランカー3戦を tree d2（戦略温度0＝決定的最良手）で実行、選出は温度維持。
本物の engine（Battle.run の on_turn フック）でターン毎スナップショットを取り、全対戦の記録を保存。
リプレイは保存記録の再生（再シミュレーションしない）。fork並列で全戦を一括実行。
"""
import os
import random
import multiprocessing as mp

from simulator.battle import Battle, BattleSide, BattleField, _entry_effects

_W = {}


def _ensure_loaded(season, det):
    if "net" not in _W:
        from simulator.simulate import get_loader
        from simulator.az_np import PVNetNP
        _W["loader"] = get_loader()
        _W["net"] = PVNetNP.load()
    _W["season"] = season
    _W["det"] = det


def poke_snapshot(p) -> dict:
    return {
        "name": p.name, "hp": p.hp, "max_hp": p.max_hp, "type1": p.type1, "type2": p.type2,
        "status": p.status, "alive": p.is_alive, "mega": p.mega_evolved, "hero": p.hero_forme,
        "mega_name": p.name if p.mega_evolved else None,
        "confused": p.confused, "seeded": p.seeded, "taunt": p.taunt_count > 0, "encore": p.encore_count > 0,
        "blade_forme": getattr(p, "_in_blade_forme", False),
        "disguise_broken": getattr(p, "_disguise_broken", False),
        "electro_charged": getattr(p, "_electromorphosis_charged", False),
        "substitute_hp": getattr(p, "_substitute_hp", 0),
        "salted": getattr(p, "_salted", False),
        "transformed": getattr(p, "_transformed", False),
        "illusion_name": getattr(p, "_illusion_name", None),
        "moves": [{"name": m.name_jp, "pp": p.pp[i], "max_pp": m.pp or 1}
                  for i, m in enumerate(p.moves) if m is not None],
        "stages": {"A": p.stage_attack, "B": p.stage_defense, "C": p.stage_sp_attack,
                   "D": p.stage_sp_defense, "S": p.stage_speed},
    }


def side_snapshot(side, field) -> dict:
    return {
        "active_idx": side.active_idx,
        "party": [poke_snapshot(p) for p in side.party],
        "reflect": side.reflect, "reflect_count": side.reflect_count,
        "light_screen": side.light_screen, "light_screen_count": side.light_screen_count,
        "aurora_veil": side.aurora_veil, "aurora_veil_count": side.aurora_veil_count,
        "stealth_rock": field.stealth_rock[side.field_idx], "spikes": field.spikes[side.field_idx],
        "toxic_spikes": field.toxic_spikes[side.field_idx],
    }


def play_and_record(specs1, specs2, season="M-2", det=8, sel_temp=0.6, seed=0) -> dict:
    """1戦を tree d2 で実行し、ターン毎記録（turns）＋勝敗＋最終状態を返す。"""
    random.seed(seed)
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from simulator.belief import OpponentBelief
    from train_az2 import _net_ai
    L = _W["loader"]; net = _W["net"]
    P1 = [build_from_spec(parse_pokemon_spec(sp), L, season=season, randomize=True) for sp in specs1]
    P2 = [build_from_spec(parse_pokemon_spec(sp), L, season=season, randomize=True) for sp in specs2]
    sel1 = select_party(P1, P2, L, n=min(3, len(P1)), temperature=sel_temp)
    sel2 = select_party(P2, P1, L, n=min(3, len(P2)), temperature=sel_temp)
    s1 = BattleSide(sel1, viewer_label="P1"); s2 = BattleSide(sel2, viewer_label="P2")
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    field = BattleField(); battle = Battle(s1, s2, field)
    # 戦略AIは tree d2・温度0（policyサンプリングなし＝最良手）。tree_k=4＝高採用率＋抜群を両立
    ai1 = _net_ai(net, L, 0, 12, seed, tree=True, tree_depth=2, tree_k=4, tree_det=det)
    ai2 = _net_ai(net, L, 0, 12, seed ^ 0x5bd1e995, tree=True, tree_depth=2, tree_k=4, tree_det=det)
    # run() 相当の前処理（見せ合い＋入場時効果）→ turn0 を記録
    battle.logs.extend(s1.opp_view.team_preview(s2.party))
    battle.logs.extend(s2.opp_view.team_preview(s1.party))
    _entry_effects(s1.active, 0, field, s2.active, battle.logs, s1.party)
    _entry_effects(s2.active, 1, field, s1.active, battle.logs, s2.party)
    turns = []
    init_logs = [f"P1選出: {', '.join(p.name for p in sel1)}",
                 f"P2選出: {', '.join(p.name for p in sel2)}"] + list(battle.logs)
    turns.append({"turn": 0, "logs": init_logs,
                  "side1": side_snapshot(s1, field), "side2": side_snapshot(s2, field),
                  "weather": field.weather, "weather_count": getattr(field, "weather_count", 0),
                  "trick_room": field.trick_room,
                  "trick_room_count": getattr(field, "trick_room_count", 0)})
    prev = [len(battle.logs)]

    def cb(b):
        nl = b.logs[prev[0]:]; prev[0] = len(b.logs)
        turns.append({"turn": b.turn, "logs": nl,
                      "side1": side_snapshot(b.side1, b.field), "side2": side_snapshot(b.side2, b.field),
                      "weather": b.field.weather, "weather_count": getattr(b.field, "weather_count", 0),
                      "trick_room": b.field.trick_room,
                      "trick_room_count": getattr(b.field, "trick_room_count", 0)})

    result = battle._turn_loop(ai1, ai2, on_turn=cb)
    if not s1.has_alive():
        result = 2
    elif not s2.has_alive():
        result = 1
    winner = (f"P1 ({sel1[0].name}側)" if result == 1
              else f"P2 ({sel2[0].name}側)" if result == 2 else "引き分け")
    opp_alive = []
    for p in s2.party:
        if p.is_alive:
            boosts = sum(getattr(p, a, 0) for a in
                         ("stage_attack", "stage_sp_attack", "stage_speed", "stage_defense", "stage_sp_defense"))
            opp_alive.append((p.name, boosts))
    own_dead = [p.name for p in s1.party if not p.is_alive]
    return {"selected1": [p.name for p in sel1], "selected2": [p.name for p in sel2],
            "turns": turns, "result": result, "winner": winner,
            "opp_alive": opp_alive, "own_dead": own_dead}


def _worker(args):
    ci, specs1, specs2, season, det, sel_temp, seed = args
    return ci, play_and_record(specs1, specs2, season, det, sel_temp, seed)


def _card_summary(label, specs, recs, n):
    wins = sum(1 for r in recs if r["result"] == 1)
    losses = sum(1 for r in recs if r["result"] == 2)
    draws = sum(1 for r in recs if r["result"] == 0)
    return {"label": label, "specs": specs, "n": n, "wins": wins, "losses": losses,
            "draws": draws, "win_rate": wins / max(1, n), "records": recs}


def _battle_seed(label: str, bi: int) -> int:
    """カード×戦番号で安定なシード。対戦数を後から増やす際、既存戦を再現/再利用できる
    （bi=0..2 は3戦時と同一、bi=3.. を追記すれば10戦・20戦へ拡張可能）。"""
    import zlib
    return (zlib.crc32(label.encode("utf-8")) % 1_000_000) * 64 + bi


def run_roundrobin(my_specs, ranker_cards, n=3, season="M-2", det=8, sel_temp=0.6,
                   on_battle=None, on_card=None, existing=None) -> list:
    """ranker_cards=[(label, specs6),...]。各カードを n 戦まで tree d2 で並列実行し記録保存。
    existing={label: [record,...]} を渡すと既存戦を再利用し、不足分(bi=len..n-1)だけ実行＝
    対戦数の段階拡張（3→10→20）に対応。シードは _battle_seed(label,bi) で安定。
    on_battle(done,total): 新規1戦完了毎。 on_card(card_idx,card): カード完成毎（保存用）。"""
    _ensure_loaded(season, det)
    existing = existing or {}
    per_card = {ci: list(existing.get(label, []))[:n] for ci, (label, _) in enumerate(ranker_cards)}
    cards = [None] * len(ranker_cards)
    jobs = []
    for ci, (label, specs) in enumerate(ranker_cards):
        have = len(per_card[ci])
        if have >= n:   # 既に充足→そのまま集計
            cards[ci] = _card_summary(label, specs, per_card[ci][:n], n)
            if on_card:
                on_card(ci, cards[ci])
            continue
        for bi in range(have, n):
            jobs.append((ci, my_specs, specs, season, det, sel_temp, _battle_seed(label, bi)))
    if not jobs:
        return cards
    workers = min(len(jobs), max(1, (os.cpu_count() or 2) - 2))
    done = 0
    ctx = mp.get_context("fork")
    with ctx.Pool(workers) as pool:
        for ci, rec in pool.imap_unordered(_worker, jobs):
            per_card[ci].append(rec); done += 1
            if on_battle:
                on_battle(done, len(jobs))
            if len(per_card[ci]) == n:
                label, specs = ranker_cards[ci]
                card = _card_summary(label, specs, per_card[ci], n)
                cards[ci] = card
                if on_card:
                    on_card(ci, card)
    return cards
