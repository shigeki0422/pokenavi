"""手動交代の検証UI：Greedy(対面・最大ダメージ) 同士の1戦を、自分(P1)の番だけ手動操作。
毎ターン「Greedyならどの技か」と「各控えへ交代した場合の被ダメ/与ダメ・有利かどうか」を表示し、
 Enter = Greedyの手（対面で殴る） / 数字 = その控えに交代/ピボット
で『中級者の良い交代』を差し込みながら、勝敗がどう動くかを体感する。

使い方:
  venv/bin/python _manual_battle.py                 # ランダムなM-1パーティ同士
  venv/bin/python _manual_battle.py --seed 42       # 再現
相手(P2)は常にGreedy。自分の瀕死後の交代先は自動(最善)。
"""
import sys, os, argparse, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, glob
from simulator.data import DataLoader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import Battle, BattleSide, BattleField, _entry_effects, _speed_order, MAX_TURNS, is_trapped
from simulator.ai import GreedyAI, select_party, Action, _effective_speed
from simulator.features import _expected_frac, switch_wins_1v1, switch_wins_1v1_split
from simulator.damage import calc_damage
from simulator.battle import MULTI_HIT_2, MULTI_HIT_3, MULTI_HIT_RANDOM_25

SEASON = "M-3"
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}

def mega_plus_random(party6, rng, n=3):
    """メガ1体＋非メガをランダムでn-1体（メガ+受け+攻め補完の現実的な選出）。メガ無しなら全ランダム。"""
    if len(party6) <= n:
        return list(party6)
    megas = [p for p in party6 if getattr(p, "mega_data", None) is not None]
    sel = [rng.choice(megas)] if megas else []
    pool = [p for p in party6 if p not in sel and getattr(p, "mega_data", None) is None]
    rng.shuffle(pool)
    sel += pool[:n - len(sel)]
    if len(sel) < n:
        rest = [p for p in party6 if p not in sel]
        rng.shuffle(rest); sel += rest[:n - len(sel)]
    return sel[:n]

def mega_copy(poke, side):
    """メガ可能（メガ石持ち・未進化・その陣営がメガ未使用）ならメガ進化したコピーを返す。
    相手は持ち物=メガ石なら可（メガ権未使用前提）。ダメージ判定をメガ後ステータスで行うため。"""
    if poke is None:
        return poke
    used = getattr(side, "mega_used", False) if side is not None else False
    if getattr(poke, "mega_data", None) is not None and not poke.mega_evolved and not used:
        import copy
        c = copy.deepcopy(poke)
        try:
            c.do_mega_evolve()
            return c
        except Exception:
            return poke
    return poke

def move_pct(att, deff, mv, field):
    """1技の対deff期待ダメ%（連続技は合計ヒット）。変化技はNone。
    へんげんじざいは実戦同様、技使用時に技タイプへ変化する前提で計算（STAB反映）。"""
    if not mv or mv.category == "status" or not mv.power:
        return None
    # へんげんじざい: 未発動なら技タイプに化けてから計算（実戦battle.pyと同じ＝STABが乗る）
    _prot = (getattr(att, "ability", "") == "へんげんじざい"
             and not getattr(att, "_protean_used", False) and mv.type)
    _saved = (att.type1, att.type2) if _prot else None
    if _prot:
        att.type1, att.type2 = mv.type, None
    try:
        d = calc_damage(att, deff, mv, field, random_roll=0.925)
        n = mv.name_jp
        if n in MULTI_HIT_3:
            sv = getattr(att, "_multi_hit_index", 0); d = 0.0
            for hi in range(3):
                att._multi_hit_index = hi; d += calc_damage(att, deff, mv, field, random_roll=0.925)
            att._multi_hit_index = sv
        elif n in MULTI_HIT_2:
            d *= 2
        elif n in MULTI_HIT_RANDOM_25:
            d *= 5 if getattr(att, "ability", "") == "スキルリンク" else 3
        return int(100 * d / max(1, deff.max_hp))
    except Exception:
        return None
    finally:
        if _saved is not None:
            att.type1, att.type2 = _saved

def moves_line(poke, opp, field):
    """覚えている技を『技名(対相手%)』で。変化技は名前のみ。連続技は★。"""
    parts = []
    for mv in poke.moves:
        if not mv:
            continue
        pct = move_pct(poke, opp, mv, field)
        mh = "★" if mv.name_jp in (MULTI_HIT_2 | MULTI_HIT_3 | MULTI_HIT_RANDOM_25) else ""
        if pct is None:
            parts.append(f"{mv.name_jp}{mh}")
        else:
            col = G if pct >= 100 else (Y if pct >= 50 else "")
            parts.append(f"{col}{mv.name_jp}{mh}({pct}%){RESET if col else ''}")
    return " ".join(parts)

import sqlite3
_L = None                     # mainで設定（loader）
_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")
_LIKELY_CACHE = {}
def opp_likely_moves(name):
    """相手種族の採用率上位の攻撃技名（隠れ情報の型読み＝真の手持ちでなく使用率から）。"""
    if name in _LIKELY_CACHE:
        return _LIKELY_CACHE[name]
    out = []
    try:
        con = sqlite3.connect(_DB)
        rows = con.execute(
            "SELECT move,usage_rate FROM pokemon_moves WHERE season=? AND rule='single' AND pokemon=? "
            "AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_moves WHERE season=? AND rule='single' AND pokemon=?) "
            "ORDER BY rank LIMIT 14", (SEASON, name, SEASON, name)).fetchall()
        con.close()
        out = [m for m, u in rows if u and u >= 8.0]   # 採用率8%以上の技を脅威候補に
    except Exception:
        out = []
    _LIKELY_CACHE[name] = out
    return out

def opp_threat_frac(opp_active, deff, field):
    """相手の採用率上位技から deff への最大被ダメ割合を型読みで見積もる（隠れ情報準拠）。
    真の手持ちでの最大も保険で取り、大きい方を返す。"""
    best = 0.0
    if _L is not None:
        for nm in opp_likely_moves(opp_active.name):
            mv = _L.get_move(nm)
            if mv and mv.power and mv.category != "status":
                pct = move_pct(opp_active, deff, mv, field)
                if pct is not None:
                    best = max(best, pct / 100.0)
    true_best = _expected_frac(opp_active, deff, field, None, multi_hit=True)
    return max(best, true_best)

def opp_read_to_bench(opp_active, my_active, bench, field, my_side):
    """相手の『対自分アクティブ最大打点技』(型読み＝採用率上位)を、控えbenchに当てた被ダメ割合。
    相手の攻撃を読んで交代する判断用（例: 相手ガブのげきりんはアシレーヌに0、じしんなら通る）。"""
    if _L is None or opp_active is None or my_active is None or bench is None:
        return 0.0
    best_mv = None; bv = -1.0
    for nm in opp_likely_moves(opp_active.name):
        mv = _L.get_move(nm)
        if mv and mv.power and mv.category != "status":
            v = move_pct(opp_active, my_active, mv, field)   # 自分アクティブへの打点
            if v is not None and v > bv:
                bv = v; best_mv = mv
    if best_mv is None:
        return 0.0
    p = move_pct(opp_active, bench, best_mv, field)           # その技を控えに当てた被ダメ
    return (p or 0) / 100.0

def _act_idx(action, legal):
    """選んだAction を ACTION_DIM index に対応付け（legal=[(Action,idx),...]）。"""
    for act, ix in legal:
        if act.type != getattr(action, "type", None):
            continue
        if action.type == "switch" and getattr(act, "switch_to", None) == action.switch_to:
            return ix
        if action.type == "move" and getattr(act, "move_idx", None) == action.move_idx \
                and bool(getattr(act, "do_mega", False)) == bool(getattr(action, "do_mega", False)):
            return ix
    for act, ix in legal:        # 緩いフォールバック（型一致）
        if act.type == getattr(action, "type", None):
            return ix
    return None

def record_turn(side1, side2, field, action, det, buf):
    """P1の決定時状態(相手はbelief決定化でマスク)＋選んだ行動を訓練形式で buf に記録。"""
    import copy
    from simulator.alphazero import legal_actions_indexed
    from simulator.features import encode_state
    belief = side1.belief
    if belief is None:
        return
    belief.observe_disclosure(side1.opp_view)
    legal = legal_actions_indexed(side1, side2, field)
    if len(legal) <= 1:
        return
    idx = _act_idx(action, legal)
    if idx is None:
        return
    cs1, cs2, cf = copy.deepcopy((side1, side2, field))
    if os.environ.get("HIDDEN_SELECTION") != "0":
        det._resample_hidden_bench(cs2, side1.opp_view)
    cfg = det._sample_opp_config(cs2, belief)
    for poke, c in zip(cs2.party, cfg):
        if c is not None:
            det._determinize(poke, c)
    feat = encode_state(cs1, cs2, cf)
    buf.append({"feat": [round(x, 5) for x in feat], "idx": idx,
                "legal": [ix for _, ix in legal]})

R="\033[91m"; G="\033[92m"; Y="\033[93m"; B="\033[94m"; C="\033[96m"; W="\033[97m"; DIM="\033[2m"; RESET="\033[0m"; BOLD="\033[1m"

def hp_bar(hp, mx, width=16):
    r = hp/mx if mx else 0; f = int(r*width)
    col = G if r > 0.5 else (Y if r > 0.25 else R)
    return f"{col}{'█'*f}{'░'*(width-f)}{RESET} {hp}/{mx}"

def hp_pct_bar(hp, mx, width=16):
    r = hp/mx if mx else 0; f = int(r*width)
    col = G if r > 0.5 else (Y if r > 0.25 else R)
    return f"{col}{'█'*f}{'░'*(width-f)}{RESET} {int(round(r*100))}%"

def show_side(label, side, col):
    p = side.active
    print(f"  {col}{label}{RESET} {p.name:<11} {hp_bar(p.hp,p.max_hp)} {DIM}{p.type1}/{p.type2 or '-'}{RESET}")
    bench = [(i,x) for i,x in enumerate(side.party) if i != side.active_idx]
    bs = "  ".join((f"{x.name}({x.hp})" if x.is_alive else f"{DIM}{x.name}[倒]{RESET}") for _,x in bench)
    if bs: print(f"      控: {bs}")

def show_p2(side2, ov):
    """相手は不完全情報で表示：HPは%（実数不可視）、選出は伏せ＝6体候補のうち未登場は不明。"""
    p = side2.active
    print(f"  {R}P2{RESET} {p.name:<11} {hp_pct_bar(p.hp,p.max_hp)} {DIM}{p.type1}/{p.type2 or '-'}{RESET} {DIM}(登場済){RESET}")
    seen = {n for n, k in ov.pokemon.items() if getattr(k, "seen", False)} if ov else set()
    seen.add(p.name)
    fainted = {x.name for x in side2.party if not x.is_alive}
    cand = [pk.name for pk in side2.source6 if pk.name not in seen and pk.name not in fainted]
    if cand:
        print(f"      {DIM}未登場候補(6体中・どれを選出したかは不明): {', '.join(cand)}{RESET}")
    if fainted:
        print(f"      {DIM}撃破済: {', '.join(sorted(fainted))}{RESET}")

def fmt_action(act, side):
    """Actionを読みやすい文字列に（技/メガ/交代先）。"""
    if act is None:
        return "-"
    t = getattr(act, "type", None)
    if t == "switch" and 0 <= getattr(act, "switch_to", -1) < len(side.party):
        return f"交代→{side.party[act.switch_to].name}"
    if t == "move" and getattr(act, "move", None):
        return f"技 {act.move.name_jp}{'(メガ)' if getattr(act,'do_mega',False) else ''}"
    return str(t)

def manual_action(side, opp, field, gai, rec_ai=None):
    from simulator.ai import _forced_charging_action, should_mega_evolve
    me = side.active; o = opp.active
    if not me.is_alive:
        return Action(type="pass")
    forced = _forced_charging_action(me)    # 溜め技2ターン目など＝選択の余地なし
    if forced:
        print(f"\n{DIM}（{me.name} は {forced.move.name_jp if forced.move else '行動'} で拘束中＝自動）{RESET}")
        return forced
    g = gai(side, opp, field)               # Greedyの推奨
    if g.type != "move" or g.move is None:
        return g
    print(f"\n{BOLD}── あなた(P1)の番 ──{RESET}")
    # メガ考慮：現役は両者メガ後で計算（自分=メガ石所持で自明、相手=メガ権未使用＋メガ可種なら）
    me_m = mega_copy(me, side); o_m = mega_copy(o, opp)
    opp_mega = o_m is not o
    gp = move_pct(me_m, o_m, g.move, field)
    print(f"  {C}Enter{RESET} = Greedy推奨: {BOLD}{g.move.name_jp}{RESET} (対 {o.name}{'(メガ後)' if opp_mega else ''} {gp if gp is not None else '-'}%)")
    if rec_ai is not None:
        try:
            from simulator.ai import certain_ko_override
            ra = certain_ko_override(rec_ai(side, opp, field), side, opp, field)
            print(f"  {G}★905模倣エンジンの推奨: {BOLD}{fmt_action(ra, side)}{RESET}")
        except Exception:
            pass
    my_in = opp_threat_frac(o_m, me_m, field)   # 型読み：相手(メガ後)の採用率上位技からの最大被ダメ
    can_mega = me.mega_data is not None and not me.mega_evolved and not side.mega_used
    do_mega = can_mega   # 技を選んだら自動でメガ進化（メガ可能な場合）
    notes = []
    if can_mega: notes.append("技選択で自動メガ進化")
    if opp_mega: notes.append(f"相手{o.name}はメガ可（メガ後で想定）")
    note = (f" {C}/ {' / '.join(notes)}{RESET}") if notes else ""
    print(f"  {DIM}対面: {me.name}{'(メガ後)' if me_m is not me else ''} は {o.name} から被ダメ {int(my_in*100)}% 想定（型読み）。★=連続技{RESET}{note}")
    # ── 技（1-4で選択） ── ※%は自分メガ後・相手メガ後で計算
    move_opts = {}
    for i, mv in enumerate(me.moves):
        if not mv: continue
        usable = me.pp[i] > 0 and (not me.choice_locked_move or me.choice_locked_move == mv.name_jp)
        pct = move_pct(me_m, o_m, mv, field)
        ptxt = (f"{pct}%" if pct is not None else "変化")
        mh = "★" if mv.name_jp in (MULTI_HIT_2 | MULTI_HIT_3 | MULTI_HIT_RANDOM_25) else ""
        mark = "" if usable else f" {R}[使用不可]{RESET}"
        key = str(i + 1)
        if usable: move_opts[key] = (i, mv)
        col = G if (pct is not None and pct >= 100) else (Y if (pct is not None and pct >= 50) else "")
        print(f"  {C}{key}{RESET} = 技 {col}{mv.name_jp}{mh}({ptxt}){RESET if col else ''}{mark}")
    # ── 交代（c1-で選択） ── ※着地はメガ前で被弾、次ターンからメガ後で1v1
    trapped = is_trapped(me, o)
    ospd = _effective_speed(o_m, field)
    sw_opts = {}
    if not trapped:
        k = 0
        for j, b in enumerate(side.party):
            if j == side.active_idx or not b.is_alive: continue
            k += 1
            in_land = opp_threat_frac(o_m, b, field)          # 着地の1発はメガ前で被弾（最大想定）
            read_in = opp_read_to_bench(o_m, me_m, b, field, side)   # 相手の対自アクティブ最大打点技を控えに当てた被ダメ（読み）
            b_m = mega_copy(b, side)                           # 次ターン以降はメガ後
            in_after = opp_threat_frac(o_m, b_m, field)
            out_f = _expected_frac(b_m, o_m, field, opp, multi_hit=True)
            hp = b.hp/max(1,b.max_hp); faster = _effective_speed(b_m, field) > ospd
            adv = switch_wins_1v1_split(in_land, in_after, out_f, hp, faster)
            tag = f"{G}← 有利交代{RESET}" if adv else ""
            spd_txt = "速い" if faster else "遅い"
            megab = "(メガ後)" if b_m is not b else ""
            in_txt = f"{int(in_land*100)}%" if abs(in_land-in_after) < 0.01 else f"{int(in_land*100)}→{int(in_after*100)}%"
            sw_opts[f"c{k}"] = (j, b)
            print(f"  {C}c{k}{RESET} = 交代→ {b.name}{megab} 被(最大){in_txt} / 被(読み){int(read_in*100)}% / 与{int(out_f*100)}% / {spd_txt} {tag}")
            print(f"        {DIM}技:{RESET} {moves_line(b_m, o_m, field)}")
    else:
        print(f"  {DIM}（交代不可：{me.name} は拘束されている）{RESET}")
    while True:
        try:
            s = input(f"  {Y}選択 [Enter=Greedy / 1-4=技 / c1-{len(sw_opts)}=交代]:{RESET} ").strip().lower()
        except EOFError:
            return g
        if s == "":
            return g
        if s in move_opts:
            i, mv = move_opts[s]
            return Action(type="move", move=mv, move_idx=i, do_mega=do_mega)
        if s in sw_opts:
            j, b = sw_opts[s]
            print(f"  {DIM}→ ハード交代 {b.name}{RESET}")
            return Action(type="switch", switch_to=j)
        print(f"  {R}無効な入力（技は 1-4、交代は c1-{len(sw_opts)}、Enterで Greedy）{RESET}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    global _L
    L = DataLoader(); _L = L
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in sp]
    a, b = rng.sample(range(len(parties)), 2)
    PA = team(parties[a]); PB = team(parties[b])
    sa = mega_plus_random(PA, rng); sb = mega_plus_random(PB, rng)   # メガ1+非メガ2ランダム（現実形）
    side1 = BattleSide(sa, source6=PA); side2 = BattleSide(sb, source6=PB)
    field = BattleField()
    gai = GreedyAI()
    from simulator.belief import OpponentBelief
    from simulator.search_ai import SearchAI
    side1.belief = OpponentBelief(L); side2.belief = OpponentBelief(L)   # 記録時の相手マスク用
    det = SearchAI(L, season=SEASON, seed=0)                            # 決定化ヘルパー
    rec_buf = []
    # 相手AI: 既定Greedy(対面的・予測しやすく交代価値の検証向き)。OPP=net で本番MCTSネット(隠れ選出)。
    opp_kind = os.environ.get("OPP", "greedy")
    if opp_kind == "net":
        from simulator.az_np import PVNetNP
        from train_az2 import _net_ai
        _netpath = os.environ.get("NET", "/tmp/az_switch_imit.json")   # 既定=905模倣(交代する中級者AI)。NET=az_net_np.json で現行
        import os.path as _op
        if not _op.exists(_netpath): _netpath = "az_net_np.json"
        _net = PVNetNP.load(_netpath)
        print(f"{DIM}相手AIネット: {_netpath}{RESET}")
        opp_ai = _net_ai(_net, L, 0, 12, 0, mcts=True, mcts_sims=int(os.environ.get("MCTS_SIMS", "300")),
                         mcts_select="regret", mcts_fast=True)
    else:
        opp_ai = gai
    # あなた(P1=新側)の局面で「905模倣エンジンならどう指すか」を毎ターン表示する推奨AI
    rec_ai = None
    if os.environ.get("REC", "1") != "0":
        from simulator.az_np import PVNetNP as _PV
        from train_az2 import _net_ai as _mkai
        import os.path as _op2
        _recpath = os.environ.get("REC_NET", "az_net_np.json")   # 既定=本番(905模倣)
        if _op2.exists(_recpath):
            rec_ai = _mkai(_PV.load(_recpath), L, 0, 12, 0, mcts=True,
                           mcts_sims=int(os.environ.get("REC_SIMS", "300")), mcts_select="regret", mcts_fast=True)
            print(f"{DIM}推奨表示: 905模倣エンジン({_recpath}){RESET}")
    _entry_effects(side1.active, 0, field, side2.active, [])
    _entry_effects(side2.active, 1, field, side1.active, [])
    battle = Battle(side1, side2, field)
    print(f"\n{BOLD}{'='*56}{RESET}")
    print(f"{B}あなた(P1) 選出{RESET}: {', '.join(p.name for p in sa)}")
    print(f"{R}相手(P2) 見せ合い 6体候補（選出3体は不明）{RESET}: {', '.join(p.name for p in PB)}")
    print(f"{DIM}※本sim仕様(隠れ選出)：相手は6体提示・どの3体を選出したかは場に出るまで不明。型/持ち物/正確なHPも未知。{RESET}")
    if opp_kind == "net":
        print(f"{DIM}相手=905模倣ネット(交代する中級者AI)。NET=az_net_np.json で現行に / OPP=greedy でGreedyに変更可。{RESET}")
    else:
        print(f"{DIM}相手=Greedy(常に対面で最大ダメージ・交代しない)。OPP=net で本番AIに変更可。{RESET}")
    prev = 0; turn = 0; result = 0; my_switches = 0
    while turn < MAX_TURNS:
        turn += 1
        if not side1.has_alive(): result = 2; break
        if not side2.has_alive(): result = 1; break
        print(f"\n{BOLD}{'─'*56}\nTurn {turn}{RESET}")
        show_side("P1", side1, B); show_p2(side2, side1.opp_view)
        a1 = manual_action(side1, side2, field, gai, rec_ai)
        try:
            record_turn(side1, side2, field, a1, det, rec_buf)
        except Exception:
            pass
        if a1.type == "switch" or (a1.type=="move" and a1.move and a1.move.name_jp in PIVOT): my_switches += 1
        a2 = opp_ai(side2, side1, field)
        # 行動を選んだ本体を記録（先攻で倒され交代した場合、後攻の行動権を失わせる＝本番_turn_loopと同じガード）
        chooser1, chooser2 = side1.active, side2.active
        for _s, _a in [(side1,a1),(side2,a2)]:
            poke = _s.active
            if getattr(_a,"do_mega",False) and not poke.mega_evolved:
                poke.do_mega_evolve()
                battle.logs.append(f"{poke.name} はメガ進化した！ → {poke.type1}/{poke.type2 or '-'}")
        p1f = _speed_order(side1, a1, side2, a2, field)
        fs, fa, fo = (side1,a1,side2) if p1f else (side2,a2,side1)
        ss, sa2, so = (side2,a2,side1) if p1f else (side1,a1,side2)
        second_chooser = chooser1 if ss is side1 else chooser2
        battle._do_action(fs, fo, fa, gai, opp_action=sa2)
        if not fo.has_alive(): result = 1 if fs is side1 else 2
        if result == 0:
            if ss.active is not second_chooser:
                battle.logs.append(f"{second_chooser.name} は倒れて行動できなかった！")
            elif ss.active.flinched:
                ss.active.flinched = False
            else:
                battle._do_action(ss, so, sa2, gai, opp_action=fa)
                if not so.has_alive(): result = 1 if ss is side1 else 2
        if result == 0:
            battle._end_of_turn()
        logs = battle.logs[prev:]; prev = len(battle.logs)
        if logs:
            print(f"  {DIM}── ログ ──{RESET}")
            for ln in logs: print(f"    {ln}")
        if not side1.has_alive(): result = 2
        elif not side2.has_alive(): result = 1
        if result: break
    rs = (f"{B}あなたの勝ち！{RESET}" if result==1 else f"{R}あなたの負け{RESET}" if result==2 else f"{Y}引き分け{RESET}")
    print(f"\n{BOLD}{'='*56}{RESET}\n  結果: {rs}  ({turn}ターン / あなたの自発交代 {my_switches}回)\n")
    # 記録保存（引分は学習価値が曖昧なので除外）。訓練形式: {feat, idx(=選んだ行動), legal, y(=勝1/負0)}
    if result in (1, 2) and rec_buf:
        recfile = os.environ.get("REC_FILE", "manual_records.jsonl")
        y = 1.0 if result == 1 else 0.0
        meta = {"p1": [str(p.name) for p in sa], "p2_source6": [str(p.name) for p in PB],
                "opp": opp_kind, "switches": my_switches}
        with open(recfile, "a") as f:
            for r in rec_buf:
                f.write(json.dumps({**r, "y": y, "meta": meta}, ensure_ascii=False) + "\n")
        print(f"{DIM}記録を {recfile} に追記: {len(rec_buf)}手 / 結果={'勝' if result==1 else '負'} / 自主交代{my_switches}回{RESET}")

if __name__ == "__main__":
    main()
