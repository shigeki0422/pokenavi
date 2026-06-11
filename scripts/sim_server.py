"""
ポケモンシミュレータ Web サーバー
起動: python3 sim_server.py
ブラウザ: http://localhost:8765
"""
import sys, os, json, asyncio, math, random, sqlite3, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import uvicorn

from simulator.data import DataLoader
from simulator.pokemon import parse_pokemon_spec, build_from_spec
from simulator.battle import Battle, BattleSide, BattleField, _entry_effects, _speed_order, MAX_TURNS, Action
from simulator.ai import HeuristicAI, select_party, should_mega_evolve
from simulator.simulate import run_simulation_specs
from simulator.search_ai import SearchAI
from simulator.belief import OpponentBelief
from simulator.az_np import PVNetNP
from simulator.features import encode_state
from simulator.env import template_index, load_registered_parties, build_party
from simulator.train import load_selection_table, make_nash_selection
from simulator.selection import sample_selection, selection_to_party

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

_public_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
app.mount("/images", StaticFiles(directory=os.path.join(_public_dir, "images")), name="images")

loader = DataLoader()
_db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")
_local = threading.local()


def _get_con() -> sqlite3.Connection:
    """スレッドローカルなSQLite接続を返す"""
    if not getattr(_local, "con", None):
        _local.con = sqlite3.connect(_db_path)
        _local.con.row_factory = sqlite3.Row
    return _local.con
AI = HeuristicAI(alpha=0.7)  # 高速フォールバック（モンテカルロ・補助用途）

# ── 学習済みAI（ブラウザ対戦のデフォルト） ──────────────────────────────
# 行動方策: SearchAI（決定化ロールアウト＋belief推定）。観戦・手動対戦で使用。
# サーバ用に予算をやや絞り応答性を確保（rollouts/depth）。
# 学習価値ネットで葉を評価する価値誘導探索（AlphaZero的）。
# ロールアウトは終局勝敗しか見ず決着済み局面で勾配を失うが、価値ネットは局面を評価するため
# 無駄手（設置済みステロ等）も低く評価できる。netが無ければ従来のロールアウトにフォールバック。
_AZ_NET = PVNetNP.load()
if _AZ_NET is not None:
    from simulator.alphazero import legal_actions_indexed as _legal_idx, NetGreedyAI
    def _value_fn(s1, s2, field):
        return _AZ_NET.evaluate(encode_state(s1, s2, field), [0])[1]
    def _policy_fn(s1, s2, field):
        # 学習方策prior（模倣で人間の手筋を反映）を {行動index: prior} で返す
        legal = [ix for _, ix in _legal_idx(s1, s2, field)]
        if not legal:
            return {}
        return _AZ_NET.evaluate(encode_state(s1, s2, field), legal)[0]
    # ロールアウト相手もネット（NetGreedyAI）＝対戦中の読みも「相手は賢い」前提（AlphaZero的）
    LEARNED_AI = SearchAI(loader, rollouts=48, depth=12, seed=0,
                          value_fn=_value_fn, policy_fn=_policy_fn, policy_weight=0.15,
                          rollout_ai=NetGreedyAI(_AZ_NET))
else:
    LEARNED_AI = SearchAI(loader, rollouts=12, depth=40, seed=0)
_SEL_CACHE = load_selection_table()            # 学習済み選出ナッシュ均衡（登録カードのみ）
_TMPL_IDX = template_index(loader)             # 6体spec集合 → party_id
_sel_rng = random.Random(12345)

# 任意パーティ汎化用の蒸留選出ポリシー（あれば使用。ヒューリスティックの上位互換）
def learned_select(my6, opp6, my_specs, opp_specs):
    """登録カードはNash表、それ以外（任意パーティ）はヒューリスティック選出 select_party。
    （蒸留選出ポリシーはCRN評価で実効+0.4pt＝無益のため不採用）"""
    my_id = _TMPL_IDX.get(frozenset(my_specs))
    opp_id = _TMPL_IDX.get(frozenset(opp_specs))
    if my_id is not None and opp_id is not None:
        entry = _SEL_CACHE.get(f"{my_id}-{opp_id}")
        if entry:
            sel = sample_selection([tuple(s) for s in entry["sels"]], entry["mix"], _sel_rng)
            if all(i < len(my6) for i in sel):
                return selection_to_party(my6, sel)
    return select_party(my6, opp6, loader)


# ── リクエストモデル ──────────────────────────────────────────────────

class BattleRequest(BaseModel):
    p1: list[str]   # スペック文字列 x6
    p2: list[str]
    season: str = "M-2"

class SimRequest(BaseModel):
    p1: list[str]
    p2: list[str]
    trials: int = 500
    season: str = "M-2"


class MatchupExplainRequest(BaseModel):
    p1: list[str]
    p2: list[str]
    season: str = "M-2"


# ── ポケモン名一覧（オートコンプリート用） ──────────────────────────────

_REGIONAL_PREFIXES = ("ガラル", "アローラ", "ヒスイ", "パルデア")

# 表記ゆれを正規名に統一するマップ（正規化後に適用）
_NORMALIZE_ALIASES: dict[str, str] = {
    "ケンタロス(水)(パルデア)": "ケンタロス:水",
    "ケンタロス(炎)(パルデア)": "ケンタロス:炎",
    "ケンタロス(闘)(パルデア)": "ケンタロス:格",
}

def _normalize_poke_name(name: str) -> str:
    """接頭語リージョン表記 → 括弧表記（スペースなし）に統一"""
    for prefix in _REGIONAL_PREFIXES:
        if name.startswith(prefix) and not name.startswith(prefix + "("):
            normalized = f"{name[len(prefix):]}({prefix})"
            return _NORMALIZE_ALIASES.get(normalized, normalized)
    # スペースあり括弧 → スペースなし括弧
    result = name.replace(" (", "(")
    return _NORMALIZE_ALIASES.get(result, result)

@app.get("/api/pokemon")
def get_pokemon_list():
    rows = _get_con().execute(
        "SELECT DISTINCT pokemon FROM pokemon_usage WHERE rule='single' ORDER BY pokemon"
    ).fetchall()
    seen: dict[str, str] = {}
    for r in rows:
        raw = r["pokemon"]
        key = _normalize_poke_name(raw)
        if key not in seen:
            seen[key] = key
    return sorted(seen.keys())


# ── バトル実行（ターン毎スナップショット） ───────────────────────────────

WEATHER_JP = {
    "sandstorm": "すなあらし", "rain": "あめ",
    "sunny": "はれ",          "hail": "あられ",
}

def poke_snapshot(p) -> dict:
    return {
        "name": p.name,
        "hp": p.hp,
        "max_hp": p.max_hp,
        "type1": p.type1,
        "type2": p.type2,
        "status": p.status,
        "alive": p.is_alive,
        "mega": p.mega_evolved,
        "hero": p.hero_forme,
        "mega_name": p.name if p.mega_evolved else None,
        "confused": p.confused,
        "seeded": p.seeded,
        "taunt": p.taunt_count > 0,
        "encore": p.encore_count > 0,
        "blade_forme": getattr(p, '_in_blade_forme', False),
        "disguise_broken": getattr(p, '_disguise_broken', False),
        "electro_charged": getattr(p, '_electromorphosis_charged', False),
        "substitute_hp": getattr(p, '_substitute_hp', 0),
        "salted": getattr(p, '_salted', False),
        "transformed": getattr(p, '_transformed', False),
        "illusion_name": getattr(p, '_illusion_name', None),
        "moves": [
            {"name": m.name_jp, "pp": p.pp[i], "max_pp": m.pp or 1}
            for i, m in enumerate(p.moves) if m is not None
        ],
        "stages": {
            "A": p.stage_attack,
            "B": p.stage_defense,
            "C": p.stage_sp_attack,
            "D": p.stage_sp_defense,
            "S": p.stage_speed,
        },
    }


def side_snapshot(side: BattleSide, field: BattleField) -> dict:
    return {
        "active_idx": side.active_idx,
        "party": [poke_snapshot(p) for p in side.party],
        "reflect": side.reflect,
        "reflect_count": side.reflect_count,
        "light_screen": side.light_screen,
        "light_screen_count": side.light_screen_count,
        "aurora_veil": side.aurora_veil,
        "aurora_veil_count": side.aurora_veil_count,
        "stealth_rock": field.stealth_rock[side.field_idx],
        "spikes": field.spikes[side.field_idx],
    }


def _fogged_side2(side2: BattleSide, viewer: BattleSide, field: BattleField) -> dict:
    """相手(side2)を viewer(P1) の開示情報だけに絞ったスナップショット。
    未登場のポケモンは「？」で隠し、登場済みでも未開示の技・持ち物は出さない。"""
    snap = side_snapshot(side2, field)
    ov = viewer.opp_view
    fogged = []
    for p in side2.party:
        k = ov.pokemon.get(p.name)
        if k and k.seen:
            ps = poke_snapshot(p)
            known = set(k.known_moves or [])
            ps["moves"] = [m for m in ps["moves"] if m["name"] in known]
            ps["item"] = k.known_item
            ps["ability"] = k.known_ability
            fogged.append(ps)
        else:
            fogged.append({"name": "？", "unknown": True, "hp": 1, "max_hp": 1,
                           "type1": None, "type2": None, "alive": True, "moves": [],
                           "status": None, "mega": False, "stages": {}})
    snap["party"] = fogged
    snap["active_idx"] = side2.active_idx
    return snap


def _random_opponent_party(loader):
    """ランダムな登録パーティ(完全な6体)を返す。"""
    parties = load_registered_parties(loader, complete_only=True)
    rp = parties[random.randrange(len(parties))]
    return build_party(rp, loader)


def run_battle_data(specs1, specs2, season="M-2"):
    """バトルを実行してターン毎データを返す"""
    parsed1 = [parse_pokemon_spec(s) for s in specs1]
    parsed2 = [parse_pokemon_spec(s) for s in specs2]

    party1_6 = [build_from_spec(sp, loader, season=season, randomize=True) for sp in parsed1]
    party2_6 = [build_from_spec(sp, loader, season=season, randomize=True) for sp in parsed2]

    selected1 = learned_select(party1_6, party2_6, specs1, specs2)
    selected2 = learned_select(party2_6, party1_6, specs2, specs1)

    side1 = BattleSide(selected1, viewer_label="P1")
    side2 = BattleSide(selected2, viewer_label="P2")
    # 学習AIのEV/性格推定を有効化（被ダメージ割合から相手型をオンライン推定）
    side1.belief = OpponentBelief(loader)
    side2.belief = OpponentBelief(loader)
    field = BattleField()
    battle = Battle(side1, side2, field)  # field_idx を設定

    entry_logs: list = []
    _entry_effects(side1.active, side1.field_idx, field, side2.active, entry_logs, side1.party)
    _entry_effects(side2.active, side2.field_idx, field, side1.active, entry_logs, side2.party)
    turns = []

    def poke_detail(p) -> str:
        item_str    = f" @{p.item}"    if p.item   else ""
        nature_str  = f" [{p.nature}]" if p.nature else ""
        ability_str = f" ({p.ability})" if p.ability else ""
        evs = getattr(p, "evs", {}) or {}
        spread = evs.get("spread", "")
        ev_str = f" EV:{spread}" if spread else ""
        moves_str   = " | ".join(m.name_jp for m in p.moves if m) or "—"
        return f"{p.name}{item_str}{nature_str}{ability_str}{ev_str}  {moves_str}"

    init_logs = [f"P1選出: {', '.join(p.name for p in selected1)}"]
    for p in selected1:
        init_logs.append(f"  {poke_detail(p)}")
    init_logs.append(f"P2選出: {', '.join(p.name for p in selected2)}")
    for p in selected2:
        init_logs.append(f"  {poke_detail(p)}")
    init_logs.extend(side2.opp_view.on_enter(side1.active))
    init_logs.extend(side1.opp_view.on_enter(side2.active))
    init_logs.extend(entry_logs)

    # ターン0: 初期状態
    turns.append({
        "turn": 0,
        "logs": init_logs,
        "side1": side_snapshot(side1, field),
        "side2": side_snapshot(side2, field),
        "weather": field.weather,
        "trick_room": field.trick_room,
    })

    prev_log_len = 0
    result = 0

    for turn in range(1, MAX_TURNS + 1):
        if not side1.has_alive():
            result = 2; break
        if not side2.has_alive():
            result = 1; break

        action1 = LEARNED_AI(side1, side2, field)
        action2 = LEARNED_AI(side2, side1, field)

        # メガ進化
        mega_logs = []
        for _side, _action in [(side1, action1), (side2, action2)]:
            poke = _side.active
            if _action.do_mega and not poke.mega_evolved and not _side.mega_used:
                mega_stone = poke.item
                poke.do_mega_evolve()
                _side.mega_used = True
                battle.logs.append(f"★ {poke.name} はメガ進化した！")
                _opp = side2 if _side is side1 else side1
                if mega_stone:
                    battle.logs.extend(_opp.opp_view.on_item(poke.name, mega_stone, "メガ進化"))
                from simulator.abilities import entry_ability as _entry_ability
                battle.logs.extend(_entry_ability(poke, _opp.active, field,
                                                  weather_duration=MAX_TURNS))

        p1_first = _speed_order(side1, action1, side2, action2, field)

        first_side, first_action, first_opp = (
            (side1, action1, side2) if p1_first else (side2, action2, side1)
        )
        second_side, second_action, second_opp = (
            (side2, action2, side1) if p1_first else (side1, action1, side2)
        )

        second_pre_idx = second_side.active_idx
        battle._do_action(first_side, first_opp, first_action, AI,
                          opp_action=second_action)
        if not first_opp.has_alive():
            result = 1 if first_side is side1 else 2

        if result == 0:
            if second_side.active.flinched:
                battle.logs.append(f"{second_side.active.name} はひるんで動けない！")
                second_side.active.flinched = False
            else:
                # 先攻の攻撃で倒れて強制交代したポケモンはそのターン行動しない
                if second_side.active_idx != second_pre_idx:
                    second_action = Action(type="pass")
                second_side.active._acts_second = True  # type: ignore
                battle._do_action(second_side, second_opp, second_action, AI,
                                  opp_action=first_action)
                if second_side.active.is_alive:
                    second_side.active._acts_second = False  # type: ignore
                if not second_opp.has_alive():
                    result = 1 if second_side is side1 else 2

        battle._end_of_turn()

        new_logs = battle.logs[prev_log_len:]
        prev_log_len = len(battle.logs)

        turns.append({
            "turn": turn,
            "logs": new_logs,
            "side1": side_snapshot(side1, field),
            "side2": side_snapshot(side2, field),
            "weather": field.weather,
            "trick_room": field.trick_room,
            "trick_room_count": field.trick_room_count,
        })

        if result != 0:
            break

    if not side1.has_alive():
        result = 2
    elif not side2.has_alive():
        result = 1

    return {
        "selected1": [p.name for p in selected1],
        "selected2": [p.name for p in selected2],
        "turns": turns,
        "result": result,
        "winner": f"P1 ({selected1[0].name}側)" if result == 1 else
                  f"P2 ({selected2[0].name}側)" if result == 2 else "引き分け",
    }


# ── SSE ストリーミング ────────────────────────────────────────────────

async def battle_stream_generator(req: BattleRequest):
    try:
        result_box = [None]
        error_box  = [None]
        def _run():
            try:
                result_box[0] = run_battle_data(req.p1, req.p2, req.season)
            except Exception as exc:
                error_box[0] = exc
        t = threading.Thread(target=_run, daemon=True)
        t.start()
        t.join(timeout=15)
        if t.is_alive():
            raise TimeoutError("バトル処理がタイムアウト(15秒)")
        if error_box[0]:
            raise error_box[0]
        data = result_box[0]
    except Exception as e:
        import traceback; traceback.print_exc()
        yield f"data: {json.dumps({'type':'error','message':str(e)})}\n\n"
        return

    # ターン0（初期選出）
    first = data["turns"][0]
    yield f"data: {json.dumps({'type':'init', 'turn': first, 'result': None})}\n\n"

    for turn_data in data["turns"][1:]:
        yield f"data: {json.dumps({'type':'turn', 'turn': turn_data})}\n\n"

    yield f"data: {json.dumps({'type':'end', 'result': data['result'], 'winner': data['winner']})}\n\n"


@app.post("/api/battle/stream")
async def battle_stream(req: BattleRequest):
    return StreamingResponse(
        battle_stream_generator(req),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        }
    )


# ── モンテカルロ集計 ──────────────────────────────────────────────────

@app.post("/api/simulate")
def simulate(req: SimRequest):
    try:
        # 総当たり/勝率は学習AI（ネットの方策＝中級志向・高速）で対戦。netが無ければHeuristic。
        _mk = (lambda: NetGreedyAI(_AZ_NET)) if _AZ_NET is not None else None
        r = run_simulation_specs(req.p1, req.p2, trials=req.trials, season=req.season, make_ai=_mk)
        return {
            "trials": r.trials,
            "wins1": r.wins1,
            "wins2": r.wins2,
            "draws": r.draws,
            "win_rate1": r.win_rate1,
            "win_rate2": r.win_rate2,
            "p2_poke_wins": r.p2_poke_wins,
            "p2_poke_losses": r.p2_poke_losses,
        }
    except Exception as e:
        import traceback; traceback.print_exc()
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/matchup_explain")
def matchup_explain(req: MatchupExplainRequest):
    """苦手理由の構造分析: 6×6個体マッチアップ＋穴/脅威＋敗因要約（対戦不要）。"""
    try:
        from simulator.matchup_explain import explain_matchup
        return explain_matchup(req.p1, req.p2, loader, req.season)
    except Exception as e:
        import traceback; traceback.print_exc()
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/matchup_battle")
def matchup_battle(req: MatchupExplainRequest):
    """実戦の敗因（第2層）: n戦の最終状態から、倒せない相手個体・積み全抜き率・落ちやすい自個体を集計。"""
    try:
        from simulator.matchup_explain import battle_explain
        _mk = (lambda: NetGreedyAI(_AZ_NET)) if _AZ_NET is not None else None
        return battle_explain(req.p1, req.p2, loader, n=30, season=req.season, make_ai=_mk)
    except Exception as e:
        import traceback; traceback.print_exc()
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))


# ── ポケモン詳細（持ち物/性格/技/EV） ──────────────────────────────────

_NAME_ALIASES = {
    "フラエッテ(永遠)": "フラエッテ:永遠",
    "ケンタロス:水": "ケンタロス:水",
    "ケンタロス:炎": "ケンタロス:炎",
    "ケンタロス:格": "ケンタロス:格",
    "ケンタロス(水)(パルデア)": "ケンタロス:水",
    "ケンタロス(炎)(パルデア)": "ケンタロス:炎",
    "ケンタロス(闘)(パルデア)": "ケンタロス:格",
    "パルデアケンタロス(水)": "ケンタロス:水",
    "パルデアケンタロス(炎)": "ケンタロス:炎",
    "パルデアケンタロス(闘)": "ケンタロス:格",
}

def _build_name_candidates(name: str) -> list:
    """リージョン・括弧表記ゆれを考慮した候補名リストを返す"""
    cands = [name]
    for prefix in _REGIONAL_PREFIXES:
        if f" ({prefix})" in name:
            base = name.replace(f" ({prefix})", "")
            cands += [f"{prefix}{base}", f"{base}({prefix})"]
        elif f"({prefix})" in name:
            base = name.replace(f"({prefix})", "")
            cands += [f"{base} ({prefix})", f"{prefix}{base}"]
        elif name.startswith(prefix):
            base = name[len(prefix):]
            cands += [f"{base} ({prefix})", f"{base}({prefix})"]
    return cands

def _resolve_usage_name(name: str, con) -> str:
    """括弧表記(スペースなし) → DBの実際のポケモン名に解決"""
    for prefix in _REGIONAL_PREFIXES:
        if name.endswith(f"({prefix})"):
            base = name[:-len(prefix)-2]
            spaced = f"{base} ({prefix})"
            r = con.execute(
                "SELECT 1 FROM pokemon_moves WHERE rule='single' AND pokemon=? LIMIT 1", (spaced,)
            ).fetchone()
            if r:
                return spaced
            prefixed = f"{prefix}{base}"
            r2 = con.execute(
                "SELECT 1 FROM pokemon_moves WHERE rule='single' AND pokemon=? LIMIT 1", (prefixed,)
            ).fetchone()
            if r2:
                return prefixed
    # スペースなし括弧 → スペースあり括弧のフォールバック（例: イダイトウ(オス) → イダイトウ (オス)）
    if "(" in name and " (" not in name:
        spaced = name.replace("(", " (", 1)
        r = con.execute(
            "SELECT 1 FROM pokemon_moves WHERE rule='single' AND pokemon=? LIMIT 1", (spaced,)
        ).fetchone()
        if r:
            return spaced
    return name

@app.get("/api/pokemon/{name}/details")
def get_pokemon_details(name: str, season: str = "M-2"):
    con = _get_con()
    name = _NAME_ALIASES.get(name, name)
    name = _resolve_usage_name(name, con)

    def latest(table):
        row = con.execute(
            f"SELECT MAX(crawled_date) FROM {table} WHERE pokemon=? AND season=? AND rule='single'",
            (name, season)
        ).fetchone()
        return row[0] if row else None

    def fetch(table, cols, limit):
        d = latest(table)
        if not d:
            return []
        rows = con.execute(
            f"SELECT {cols} FROM {table} WHERE pokemon=? AND season=? AND rule='single' AND crawled_date=? ORDER BY rank LIMIT {limit}",
            (name, season, d)
        ).fetchall()
        return [{k: r[k] for k in r.keys()} for r in rows]

    def fetch_abilities():
        # pokemon_abilities はリージョン名のフォーマットが他テーブルと異なる場合があるため
        # 複数の名前形式を試す（例: "ヤドキング (ガラル)" vs "ガラルヤドキング"）
        candidates = [name]
        for prefix in _REGIONAL_PREFIXES:
            if f" ({prefix})" in name:
                base = name.replace(f" ({prefix})", "")
                candidates.append(f"{prefix}{base}")
            elif name.startswith(prefix):
                base = name[len(prefix):]
                candidates.append(f"{base} ({prefix})")
        abl_name = name
        d = None
        for cand in candidates:
            row = con.execute(
                "SELECT MAX(crawled_date) FROM pokemon_abilities WHERE pokemon=? AND season=? AND rule='single'",
                (cand, season)
            ).fetchone()
            if row and row[0]:
                abl_name, d = cand, row[0]
                break
        if not d:
            return []
        rows = con.execute(
            "SELECT ability, usage_rate FROM pokemon_abilities WHERE pokemon=? AND season=? AND rule='single' AND crawled_date=? ORDER BY rank LIMIT 5",
            (abl_name, season, d)
        ).fetchall()
        return [{k: r[k] for k in r.keys()} for r in rows]

    ranked_moves = fetch("pokemon_moves", "move, usage_rate", 20)
    ranked_move_names = {m["move"] for m in ranked_moves}

    # pokemon_learnsets から使用率未収録の技を補完（usage_rate=None）
    learnset_rows = con.execute(
        "SELECT move_jp FROM pokemon_learnsets WHERE pokemon_name=? ORDER BY move_jp",
        (name,)
    ).fetchall()
    if not learnset_rows:
        # リージョン表記ゆれを試す
        for cand in _build_name_candidates(name):
            learnset_rows = con.execute(
                "SELECT move_jp FROM pokemon_learnsets WHERE pokemon_name=? ORDER BY move_jp",
                (cand,)
            ).fetchall()
            if learnset_rows:
                break
    extra_moves = [{"move": r[0], "usage_rate": None}
                   for r in learnset_rows if r[0] not in ranked_move_names]

    all_moves = ranked_moves + extra_moves

    return {
        "items":     fetch("pokemon_items",   "item, usage_rate",                                           10),
        "moves":     all_moves,
        "natures":   fetch("pokemon_natures", "nature, usage_rate",                                          8),
        "evs":       fetch("pokemon_evs",     "ev_spread, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, usage_rate",  8),
        "abilities": fetch_abilities(),
    }


# ── 手動バトル ─────────────────────────────────────────────────────────

_manual_battles: dict = {}
_pending_random: dict = {}  # ランダム対戦の事前プレビュー: preview_id → 相手6体

class ManualStartRequest(BaseModel):
    p1: list[str]
    p2: list[str] = []
    season: str = "M-2"
    p1_indices: Optional[list[int]] = None  # プレイヤー選出順 (0–5)
    random_opponent: bool = False           # 相手をランダムな登録パーティにする
    hidden: bool = False                    # 相手の持ち物/技/選出3匹を開示まで秘匿
    preview_id: Optional[str] = None        # 事前プレビューで確定済みのランダム相手

class ManualActionRequest(BaseModel):
    battle_id: str
    action_type: str   # "move" | "switch"
    move_idx: int = 0
    switch_to: int = -1
    do_mega: bool = False


def _get_available_actions(side: BattleSide, opp_active=None, field=None) -> dict:
    from simulator.data import get_type_effectiveness
    from simulator.damage import _effective_move_type
    p = side.active
    moves = []

    class _FakeField:
        weather = None
    _field = field if field is not None else _FakeField()

    for i, mv in enumerate(p.moves):
        if mv is None:
            continue
        disabled = bool(
            p.disabled_move == mv.name_jp
            or (p.choice_locked_move and p.choice_locked_move != mv.name_jp)
            or (p.encore_count > 0 and p.locked_move and p.locked_move != mv.name_jp)
            or (p.lock_count > 0 and p.locked_move and p.locked_move != mv.name_jp)
            or (p.taunt_count > 0 and mv.category == "status")
        )
        eff_type = _effective_move_type(p, mv, _field)
        # ウェザーボールの威力
        if mv.name_jp == "ウェザーボール":
            disp_power = 100 if (_field.weather or p.ability == "メガソーラー") else 50
        else:
            disp_power = mv.power
        eff = None
        if opp_active and mv.category in ("physical", "special") and mv.power:
            eff = get_type_effectiveness(eff_type, opp_active.type1, opp_active.type2)
        moves.append({
            "idx": i,
            "name": mv.name_jp,
            "type": eff_type,
            "category": mv.category,
            "power": disp_power,
            "pp": p.pp[i] if i < len(p.pp) else 0,
            "max_pp": mv.pp or 1,
            "disabled": disabled,
            "eff": eff,
        })
    switches = []
    for i, sp in enumerate(side.party):
        if i != side.active_idx and sp.is_alive:
            switches.append({
                "idx": i,
                "name": sp.name,
                "hp": sp.hp,
                "max_hp": sp.max_hp,
                "type1": sp.type1,
                "type2": sp.type2,
            })
    can_mega = (
        not side.mega_used
        and not p.mega_evolved
        and bool(p.item and "ナイト" in p.item)
    )
    return {"moves": moves, "switches": switches, "can_mega": can_mega}


def _exec_manual_turn(side1, side2, field, battle, action1):
    """1ターン実行。戻り値: (result, awaiting, p2_entry_pending, mid_turn_ctx)
    mid_turn_ctx: P1先行ピボット時 {"action2": Action, "second_pre_idx": int}、通常は None"""
    from simulator.abilities import entry_ability as _entry_ability
    side1._manual_switch = True  # type: ignore
    try:
        action2 = LEARNED_AI(side2, side1, field)

        # メガ進化
        for _side, _action in [(side1, action1), (side2, action2)]:
            poke = _side.active
            if _action.do_mega and not poke.mega_evolved and not _side.mega_used:
                mega_stone = poke.item
                poke.do_mega_evolve()
                _side.mega_used = True
                battle.logs.append(f"★ {poke.name} はメガ進化した！")
                _opp = side2 if _side is side1 else side1
                if mega_stone:
                    battle.logs.extend(_opp.opp_view.on_item(poke.name, mega_stone, "メガ進化"))
                battle.logs.extend(_entry_ability(poke, _opp.active, field, weather_duration=MAX_TURNS))

        p1_first = _speed_order(side1, action1, side2, action2, field)
        first_side,  first_action,  first_opp  = (side1, action1, side2) if p1_first else (side2, action2, side1)
        second_side, second_action, second_opp = (side2, action2, side1) if p1_first else (side1, action1, side2)

        result = 0
        second_pre_idx = second_side.active_idx
        battle._do_action(first_side, first_opp, first_action, AI, opp_action=second_action)
        if not first_opp.has_alive():
            result = 1 if first_side is side1 else 2

        # P1先行ピボット: P2の行動前に手動交代を待つ（中断して返す）
        if (result == 0 and p1_first
                and side1.active.is_alive
                and getattr(side1.active, '_pivot_out', False)):
            p2_ep = getattr(side2, '_entry_effects_pending', False)
            if p2_ep:
                side2._entry_effects_pending = False  # type: ignore
            return result, True, p2_ep, {"action2": action2, "second_pre_idx": second_pre_idx}

        if result == 0:
            if second_side.active.flinched:
                battle.logs.append(f"{second_side.active.name} はひるんで動けない！")
                second_side.active.flinched = False
            elif not second_side.active.is_alive:
                pass  # 先攻技で倒れたため後攻行動をスキップ
            else:
                if second_side.active_idx != second_pre_idx:
                    second_action = Action(type="pass")
                second_side.active._acts_second = True  # type: ignore
                battle._do_action(second_side, second_opp, second_action, AI, opp_action=first_action)
                if second_side.active.is_alive:
                    second_side.active._acts_second = False  # type: ignore
                if not second_opp.has_alive():
                    result = 1 if second_side is side1 else 2

        battle._end_of_turn()

        if not side1.has_alive():
            result = 2
        elif not side2.has_alive():
            result = 1
    finally:
        side1._manual_switch = False  # type: ignore

    awaiting = result == 0 and (
        (not side1.active.is_alive and side1.has_alive())
        or getattr(side1.active, '_pivot_out', False)
    )
    p2_entry_pending = awaiting and getattr(side2, '_entry_effects_pending', False)
    if p2_entry_pending:
        side2._entry_effects_pending = False  # type: ignore
    return result, awaiting, p2_entry_pending, None


@app.get("/api/manual/random_preview")
def manual_random_preview():
    """ランダム相手の見せ合い6体（公開情報＝種族・タイプのみ）を返す。同じ相手で対戦するためのpreview_id付き。"""
    import uuid
    party2_6 = _random_opponent_party(loader)
    pid = str(uuid.uuid4())[:8]
    _pending_random[pid] = party2_6
    if len(_pending_random) > 200:  # 古いプレビューを掃除
        for k in list(_pending_random)[:100]:
            _pending_random.pop(k, None)
    return {"preview_id": pid,
            "opponent": [{"name": p.name, "type1": p.type1, "type2": p.type2} for p in party2_6]}


@app.post("/api/manual/start")
def manual_start(req: ManualStartRequest):
    import uuid
    battle_id = str(uuid.uuid4())[:8]

    parsed1 = [parse_pokemon_spec(s) for s in req.p1]
    party1_6 = [build_from_spec(sp, loader, season=req.season, randomize=True) for sp in parsed1]
    if req.preview_id and req.preview_id in _pending_random:
        party2_6 = _pending_random.pop(req.preview_id)  # プレビューで見せた相手をそのまま使う
    elif req.random_opponent:
        party2_6 = _random_opponent_party(loader)
    else:
        parsed2 = [parse_pokemon_spec(s) for s in req.p2]
        party2_6 = [build_from_spec(sp, loader, season=req.season, randomize=True) for sp in parsed2]
    if req.p1_indices:
        valid = [i for i in req.p1_indices if 0 <= i < len(party1_6)][:3]
        selected1 = [party1_6[i] for i in valid]
    else:
        selected1 = select_party(party1_6, party2_6, loader)
    # P2（AI側）は学習済みナッシュ均衡で選出（ランダム相手は select_party 相当にフォールバック）
    selected2 = learned_select(party2_6, party1_6, req.p2, req.p1)

    side1 = BattleSide(selected1, viewer_label="P1")
    side2 = BattleSide(selected2, viewer_label="P2")
    # AI側(P2)に belief を付与：人間(P1)の被ダメージ割合からEV/性格を推定
    side2.belief = OpponentBelief(loader)
    field = BattleField()
    battle = Battle(side1, side2, field)

    entry_logs: list = []
    _entry_effects(side1.active, 0, field, side2.active, entry_logs, side1.party)
    _entry_effects(side2.active, 1, field, side1.active, entry_logs, side2.party)

    def poke_detail(p) -> str:
        item_str = f"@{p.item}" if p.item else ""
        moves_str = " | ".join(m.name_jp for m in p.moves if m) or "—"
        return f"  {p.name}{item_str} ({p.ability})  {moves_str}"

    init_logs = [f"▶ P1選出: {', '.join(p.name for p in selected1)}"]
    for p in selected1: init_logs.append(poke_detail(p))
    if req.hidden:
        # 見せ合い：相手候補6体の種族のみ開示。選出3匹・持ち物・技は対戦中に判明。
        init_logs += side1.opp_view.team_preview(party2_6)
        init_logs += side1.opp_view.on_enter(side2.active)  # 先頭は登場＝開示
        init_logs.append("▶ P2選出: ？（持ち物・技・残り2匹は判明するまで不明）")
    else:
        init_logs.append(f"▶ P2選出: {', '.join(p.name for p in selected2)}")
        for p in selected2: init_logs.append(poke_detail(p))
    init_logs.extend(entry_logs)

    _manual_battles[battle_id] = {
        "side1": side1, "side2": side2, "field": field,
        "battle": battle, "turn": 0, "phase": "action",
        "p2_entry_pending": False, "mid_turn_ctx": None,
        "hidden": req.hidden,
    }

    side2_snap = _fogged_side2(side2, side1, field) if req.hidden else side_snapshot(side2, field)
    return {
        "battle_id": battle_id,
        "logs": init_logs,
        "side1": side_snapshot(side1, field),
        "side2": side2_snap,
        "weather": field.weather,
        "trick_room": field.trick_room,
        "trick_room_count": field.trick_room_count,
        "actions": _get_available_actions(side1, side2.active, field),
        "turn": 0,
        "done": False,
        "winner": 0,
    }


IMITATION_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imitation_data.jsonl")


def _human_action_index(req):
    """手動対戦のリクエストを方策のACTION_DIMインデックスに変換（move=idx[+4でメガ]/switch=8+slot）。"""
    if req.action_type == "switch":
        return 8 + req.switch_to if 0 <= req.switch_to < 3 else None
    idx = req.move_idx
    return idx + (4 if req.do_mega else 0) if 0 <= idx < 4 else None


def _record_human(sess, side1, side2, field, req):
    """人間(side1)の意思決定を (局面特徴, 行動index, 合法マスク) で記録（模倣学習用）。"""
    try:
        from simulator.alphazero import legal_actions_indexed
        ai = _human_action_index(req)
        if ai is None:
            return
        feat = encode_state(side1, side2, field)
        mask = [ix for _, ix in legal_actions_indexed(side1, side2, field)]
        sess.setdefault("imitation", []).append({"x": feat, "a": ai, "m": mask})
    except Exception:
        pass


def _flush_imitation(sess, result):
    """終局時に勝敗ラベル付きで保存（人間=side1が勝てば1.0）。"""
    recs = sess.get("imitation")
    if not recs or result == 0:
        return
    y = 1.0 if result == 1 else 0.0
    try:
        with open(IMITATION_PATH, "a", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps({**r, "y": y}, ensure_ascii=False) + "\n")
    except Exception:
        pass
    sess["imitation"] = []


@app.post("/api/manual/action")
def manual_action(req: ManualActionRequest):
    from fastapi import HTTPException
    sess = _manual_battles.get(req.battle_id)
    if not sess:
        raise HTTPException(status_code=404, detail="バトルセッションが見つかりません")

    side1, side2, field, battle = sess["side1"], sess["side2"], sess["field"], sess["battle"]
    prev_log_len = len(battle.logs)

    # ── 交代先選択フェーズ ──────────────────────────────────────────────
    if sess.get("phase") == "awaiting_switch":
        if req.action_type != "switch" or req.switch_to < 0:
            raise HTTPException(status_code=400, detail="交代先を選んでください")
        active = side1.active
        if getattr(active, '_pivot_out', False):
            active._pivot_out = False  # type: ignore
        side1.switch_to(req.switch_to, battle.logs, field)
        battle.logs.append(f"{side1.active.name} が出てきた！")
        if sess.get("p2_entry_pending"):
            # 相打ち: P2 の登場時効果を P1 の新ポケモンに対して発動
            _entry_effects(side2.active, 1, field, side1.active, battle.logs, side2.party)
            battle.logs.extend(side1.opp_view.on_enter(side2.active))
            _entry_effects(side1.active, 0, field, side2.active, battle.logs, side1.party)
            battle.logs.extend(side2.opp_view.on_enter(side1.active))
            sess["p2_entry_pending"] = False
        else:
            _entry_effects(side1.active, 0, field, side2.active, battle.logs, side1.party)
            battle.logs.extend(side2.opp_view.on_enter(side1.active))

        # P1先行ピボット後: P2の残り行動を実行してターン終了
        mid_ctx = sess.pop("mid_turn_ctx", None)
        result = 0
        awaiting = False
        if mid_ctx:
            side1._manual_switch = True  # type: ignore
            try:
                action2 = mid_ctx["action2"]
                second_pre_idx = mid_ctx["second_pre_idx"]
                if side2.active.flinched:
                    battle.logs.append(f"{side2.active.name} はひるんで動けない！")
                    side2.active.flinched = False
                else:
                    if side2.active_idx != second_pre_idx:
                        action2 = Action(type="pass")
                    side2.active._acts_second = True  # type: ignore
                    battle._do_action(side2, side1, action2, AI, opp_action=None)
                    if side2.active.is_alive:
                        side2.active._acts_second = False  # type: ignore
                battle._end_of_turn()
                if not side1.has_alive():
                    result = 2
                elif not side2.has_alive():
                    result = 1
            finally:
                side1._manual_switch = False  # type: ignore
            awaiting = result == 0 and (
                (not side1.active.is_alive and side1.has_alive())
                or getattr(side1.active, '_pivot_out', False)
            )
        else:
            if not side2.has_alive():
                result = 1
            elif not side1.has_alive():
                result = 2

        if awaiting:
            sess["phase"] = "awaiting_switch"
            sess["mid_turn_ctx"] = None
        else:
            sess["phase"] = "action"

        new_logs = battle.logs[prev_log_len:]
        done = (result != 0 or sess["turn"] >= MAX_TURNS) and not awaiting
        if done:
            _flush_imitation(sess, result)
            del _manual_battles[req.battle_id]
        return {
            "logs": new_logs,
            "side1": side_snapshot(side1, field),
            "side2": (_fogged_side2(side2, side1, field) if sess.get("hidden") else side_snapshot(side2, field)),
            "weather": field.weather,
            "trick_room": field.trick_room,
            "trick_room_count": field.trick_room_count,
            "turn": sess["turn"],
            "actions": None if done else _get_available_actions(side1, side2.active, field),
            "done": done,
            "winner": result,
            "awaiting_switch": awaiting,
        }

    # ── 通常ターン ──────────────────────────────────────────────────────
    p1 = side1.active
    if req.action_type == "switch":
        action1 = Action(type="switch", switch_to=req.switch_to)
    else:
        idx = max(0, min(req.move_idx, len(p1.moves) - 1))
        mv = p1.moves[idx]
        if mv is None:
            mv = next((m for m in p1.moves if m), None)
        action1 = Action(type="move", move=mv, move_idx=idx, do_mega=req.do_mega)

    _record_human(sess, side1, side2, field, req)  # 模倣学習用に人間の意思決定を記録
    sess["turn"] += 1
    result, awaiting, p2_entry_pending, mid_turn_ctx = _exec_manual_turn(side1, side2, field, battle, action1)
    new_logs = battle.logs[prev_log_len:]

    if awaiting:
        sess["phase"] = "awaiting_switch"
        sess["p2_entry_pending"] = p2_entry_pending
        sess["mid_turn_ctx"] = mid_turn_ctx

    done = (result != 0 or sess["turn"] >= MAX_TURNS) and not awaiting
    if done:
        _flush_imitation(sess, result)
        del _manual_battles[req.battle_id]

    return {
        "logs": new_logs,
        "side1": side_snapshot(side1, field),
        "side2": (_fogged_side2(side2, side1, field) if sess.get("hidden") else side_snapshot(side2, field)),
        "weather": field.weather,
        "trick_room": field.trick_room,
        "trick_room_count": field.trick_room_count,
        "turn": sess["turn"],
        "actions": None if done else _get_available_actions(side1, side2.active, field),
        "done": done,
        "winner": result,
        "awaiting_switch": awaiting,
    }


# ── HTML UI ──────────────────────────────────────────────────────────

@app.get("/")
def index():
    html_path = os.path.join(os.path.dirname(__file__), "sim_ui", "index.html")
    with open(html_path, encoding="utf-8") as f:
        return HTMLResponse(f.read(), headers={"Cache-Control": "no-cache, no-store"})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8888))
    print(f"シミュレータ起動: http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
