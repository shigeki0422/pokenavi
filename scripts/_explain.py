"""Product3提案の説明情報：役割・パーティ統計・使用率上位との1v1相性。"""
import json, os, sqlite3, statistics, sys, math
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.damage import calc_damage
from simulator.ai import _effective_speed, SETUP_MOVES
from simulator.data import get_type_effectiveness
from simulator.battle import BattleField, _entry_effects
from _party_quality import TYPES, adj_eff



# トレースは入場時に相手の特性をコピーする（abilities.py:90）。コピー先が天候/フィールド特性なら
# 場まで変わるため、場の判定より先に解決する。コピー不可の特性は abilities.py と同じ集合。
_UNCOPYABLE = {"トレース", "かわりもの", "イリュージョン", "ばけのかわ", "かがくへんかガス"}


def _resolved_ability(a, b):
    """a が場に出た直後の実効特性（トレース解決後）。"""
    if a.ability == "トレース" and b.ability not in _UNCOPYABLE:
        return b.ability
    return a.ability


def _enter(a, b):
    """a と b が場に出た直後の (場, aの入場後状態, bの入場後状態) を対戦本体の処理で作る。
    ここで反映されるもの: 天候/フィールド特性、いかく（あまのじゃく/クリアボディ等の無効も含む）、
    トレース、ダウンロード等、すべての入場時効果。
    ハザードは1v1判定の前提（互いに場に出たところから）に無いので設置しない。
    a/b 自体は書き換えず、複製を返す。"""
    import copy
    # メガシンカ済みで渡された個体は、メガ前の姿で入場させてから1ターン目の行動前にメガシンカする（実機・Rust の判定と同じ順）
    def _pre(p):
        if getattr(p, "mega_evolved", False) and getattr(p, "_spec", None) and L_REF[0] is not None:
            q = _build(p._spec, L_REF[0], mega=False)
            return q
        return copy.deepcopy(p)
    A = _pre(a); B = _pre(b)
    f = BattleField()
    from simulator.battle import _entry_and_mega
    _entry_and_mega(A, B, f, [], [A], [B])
    return f, A, B


L_REF = [None]     # 実走版1v1が使う loader（_build が最初の呼び出しで登録）


def _dmg(att, deff, mv, field, critical=False, roll=0.0):
    """副作用を持ち込まない calc_damage。
    calc_damage は半減きのみ消費で defender.item=None、充電技で attacker.charged=False と
    実体を書き換える（対戦本体では正しい）。分析側は同じオブジェクトを何度も使い回すため、
    1列目の計算で相手のきのみが消え、以降の列が「きのみ無し」で判定される事故が起きていた。
    （実測: エンペルト@シュカのみ の相性表で1列目消費・残り28列が誤判定）
    """
    _a = (att.item, getattr(att, "charged", None), getattr(att, "_electromorphosis_charged", None))
    _d = deff.item
    try:
        return calc_damage(att, deff, mv, field, critical, roll)
    finally:
        deff.item = _d
        att.item = _a[0]
        if _a[1] is not None: att.charged = _a[1]
        if _a[2] is not None: att._electromorphosis_charged = _a[2]


HAZ = {"ステルスロック", "まきびし", "どくびし", "スパイク"}
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
SCREEN = {"リフレクター", "ひかりのかべ", "オーロラベール", "おいかぜ", "しんぴのまもり", "すてゼリフ"}
STATUSM = {"おにび", "でんじは", "どくどく", "あくび", "ちょうはつ", "ねむりごな", "キノコのほうし", "やどりぎのタネ"}
RECOV = {"なまける", "はねやすめ", "じこさいせい", "つきのひかり", "こうごうせい", "あさのひざし", "タマゴうみ", "ねむる", "ミルクのみ", "ねがいごと"}
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")

def _build(spec, L, mega=True):
    p = build_from_spec(parse_pokemon_spec(spec), L, season=os.environ.get("POOL_SEASON", "M-6"), randomize=False)
    if mega and p.mega_data is not None: p.do_mega_evolve()
    p._spec = spec        # 実走版1v1（_mu_engine）が spec を必要とするため保持
    if L_REF[0] is None: L_REF[0] = L
    return p

def role_of(spec, L):
    p = build_from_spec(parse_pokemon_spec(spec), L, season=os.environ.get("POOL_SEASON", "M-6"), randomize=False)
    mvs = {m.name_jp for m in p.moves}
    it = spec.split("@", 1)[1].split(":")[0]
    evp = spec.split("@", 1)[1].split(":")[3].split("/")
    evh, eva, evc = int(evp[0]), int(evp[1]), int(evp[3])
    ismega = p.mega_data is not None
    nph = sum(1 for m in p.moves if m.category == "physical")
    nsp = sum(1 for m in p.moves if m.category == "special")
    prim = []
    # 勝ち筋・主役
    if it == "こだわりスカーフ": prim.append("スカーフ掃除役")
    elif mvs & SETUP_MOVES and (nph + nsp) >= 2: prim.append(("メガ" if ismega else "") + "積みエース")
    elif ismega and (eva >= 16 or evc >= 16): prim.append("メガエース")
    elif eva >= 16 and nph >= 1: prim.append("物理アタッカー")
    elif evc >= 16 and nsp >= 1: prim.append("特殊アタッカー")
    # 補助役
    util = []
    if "トリックルーム" in mvs: util.append("トリル始動")
    if mvs & HAZ: util.append("設置")
    if mvs & SCREEN: util.append("壁/サポート")
    if mvs & PIVOT: util.append("対面操作")
    if (mvs & RECOV) and evh >= 16 and eva < 16 and evc < 16: util.append("受け")
    if mvs & STATUSM: util.append("状態異常撒き" if evh >= 16 else "妨害")
    roles = prim + util
    if not roles:
        roles = ["物理アタッカー" if nph >= nsp else "特殊アタッカー"]
    return roles[:2]

def party_stats(specs, L, pg, th):
    from _threat_coverage import team_coverage
    from _construction_gap import team_features
    tf = team_features(specs, L, os.environ.get("POOL_SEASON", "M-6"))
    cov = team_coverage(specs, L, th)[0]
    mons = [_build(s, L) for s in specs]
    wc = {}
    for A in TYPES:
        wc[A] = sum(1 for p in mons if adj_eff(A, p.type1, p.type2, p.ability) >= 2)
    worst = max(wc, key=wc.get)
    atk = set()
    for p in mons:
        for m in p.moves:
            if m.category in ("physical", "special") and m.type:
                atk |= {T for T in TYPES if get_type_effectiveness(m.type, T, None) >= 2}
    spds = [_effective_speed(p, BattleField()) for p in mons]
    return {
        "脅威対応率": f"{cov*100:.0f}%",
        "攻撃カバー": f"{len(atk)}/18型を抜群",
        "防御相補": f"{tf['def_cover']*100:.0f}% を半減以下で受け",
        "最大弱点重複": f"{worst} に{wc[worst]}体",
        "メガ数": sum(1 for s in specs if "ナイト" in s.split("@")[1].split(":")[0]),
        "設置技": "有" if tf["hazard"] else "無",
        "天候": "有" if tf["weather"] else "無",
        "スカーフ": sum(1 for s in specs if s.split("@")[1].split(":")[0] == "こだわりスカーフ"),
        "物理/特殊": f"{tf['phys_cnt']}/{tf['spec_cnt']}",
        "平均素早さ": f"{statistics.mean(spds):.0f}（最速{max(spds)}）",
    }

def stat_details(specs, L, th):
    """攻撃カバー・防御相補（タイプ相性）の内訳。"""
    names = [s.split("@")[0] for s in specs]
    mons = [_build(s, L) for s in specs]

    # タイプ相性：攻撃(各タイプへの最大打点倍率)と防御(被弾倍率)を別々に持つ
    atk_mult = []
    for m in mons:
        has = any(mv.category in ("physical", "special") and mv.type for mv in m.moves)
        mm = {A: 0.0 for A in TYPES} if has else None
        if has:
            for mv in m.moves:
                if mv.category in ("physical", "special") and mv.type:
                    for A in TYPES:
                        e = get_type_effectiveness(mv.type, A, None)
                        if e > mm[A]: mm[A] = e
        atk_mult.append(mm)
    type_rows = []
    for A in TYPES:
        cells = [{"atk": (atk_mult[i][A] if atk_mult[i] is not None else None),
                  "def": adj_eff(A, m.type1, m.type2, m.ability)}
                 for i, m in enumerate(mons)]
        type_rows.append({"type": A, "cells": cells})
    atk_cov = sum(1 for A in TYPES if any(atk_mult[i] and atk_mult[i][A] >= 2 for i in range(len(mons))))
    def_cov = sum(1 for A in TYPES if any(adj_eff(A, m.type1, m.type2, m.ability) < 1 for m in mons))

    return {
        "members": names,
        "typematrix": {"atk_cov": atk_cov, "def_cov": def_cov, "rows": type_rows},
    }

# 1v1判定は Rust エンジン（工房・ポケモン情報ページが使う wasm と同じ analysis）に委ねる。
# ここに判定式を持っていた頃は、score の刻み(0.5/1)・先制技での決着・最短手順・
# 確定1の扱いが工房側だけ更新され、同じ対面で記号が食い違っていた。
_RUST = None
_RUST_WARNED = False


def _season():
    """判定に渡すシーズン。サーバの POOL_SEASON に追従する（型プールと揃える）。"""
    return os.environ.get("POOL_SEASON", "M-3")


def _rust():
    """pokenavi_engine（PyO3）。未導入なら None を返し、呼び出し側が旧実装に落ちる。"""
    global _RUST, _RUST_WARNED
    if _RUST is None:
        try:
            import pokenavi_engine as _E
            _RUST = _E
        except Exception as e:                     # noqa: BLE001 (理由を問わず旧実装に落とす)
            _RUST = False
            if not _RUST_WARNED:
                _RUST_WARNED = True
                print(f"[_explain] pokenavi_engine を読めないため旧判定にフォールバック: {e}",
                      file=sys.stderr)
    return _RUST or None


def _score_sym(s):
    r = _rust()
    if r is not None:
        return r.mu_sym(float(s))
    return "◎" if s >= 2 else "○" if s >= 1 else "△" if s > -1 else "▲" if s > -2 else "×"

# 1v1判定の実装切替。既定=engine（対戦本体で実走）。
# 静的評価は「対戦本体では正しい仕様が分析側では抜ける」バグを繰り返し出した
# （天候・フィールド・いかく・トレース・ばけのかわ・マルチスケイル・半減きのみ・ロール引数）。
# 実測の一致率は72.6%だった。MU_MODE=static で旧実装に戻せる（比較検証用）。
MU_MODE = os.environ.get("MU_MODE", "engine")


def _mu_score(M, O, field):
    """1v1の内訳：互いの最大打点1発の確定数・素早さから勝敗スコアを算出。
    既定では対戦本体で1v1を実走して数える（追加効果・自己ランク低下・反動・回復・
    特性の発動など engine が実装している全てが反映される）。"""
    field, Me, Oe = _enter(M, O)
    sa, sb = getattr(M, "_spec", None), getattr(O, "_spec", None)
    r = _rust()
    if MU_MODE == "engine" and r is not None and sa and sb:
        d = json.loads(r.mu_analyze(sa, sb, _season()))
        v = d["verdict"]
        # HP比は Rust の firstLo(1ターン目のHP減少)/相手の最大HP。
        # _mu_engine を別に走らせても同値だが、同じ対面を2回実走することになる。
        def _ratio(side, other, name):
            m = next((x for x in d[side]["moves"] if x.get("n") == name), None)
            f = m.get("firstLo") if m else None
            return 0.0 if f is None else f / max(1, d[other]["hp"])
        ar = _ratio("a", "b", v["myMove"])
        br = _ratio("b", "a", v["oppMove"])

        def _steps(side, other, names):
            """手順の各手を表示用にする。%は技そのものの値（単発行と基準を揃える）。"""
            out = []
            for n in names:
                m = next((x for x in d[side]["moves"] if x.get("n") == n), None)
                hp = max(1, d[other]["hp"])
                lo, hi = (m or {}).get("dmgLo"), (m or {}).get("dmgHi")
                out.append({"n": n,
                            "pctLo": None if lo is None else lo / hp * 100,
                            "pctHi": None if hi is None else hi / hp * 100})
            return out

        def _turns(side, other):
            """毎ターンの与ダメージ(2ターン以上かかる対面のみ)。%は相手の最大HP比。"""
            ts = d[side].get("turns") or []
            hp = max(1, d[other]["hp"])
            if len(ts) < 2:
                return []
            return [{"n": t["n"], "pctLo": t["lo"] / hp * 100, "pctHi": t["hi"] / hp * 100,
                     "healPct": (t.get("heal", 0) / hp * 100) if t.get("heal") else None} for t in ts]
        return {"myh": v["myHits"], "thh": v["oppHits"], "myr": ar, "thr": br,
                "fast": v["koFirst"], "my_s": v["myS"], "op_s": v["oppS"],
                "my_move": v["myMove"], "th_move": v["oppMove"],
                "my_seq": v["mySeq"], "ko_by_priority": v["koByPriority"],
                "my_steps": _steps("a", "b", v["mySeq"]),
                "opp_steps": _steps("b", "a", v.get("oppSeq") or []),
                "my_turns": _turns("a", "b"), "opp_turns": _turns("b", "a"),
                "sym": v["sym"], "score": v["score"], "win": v["win"],
                "draw": v.get("draw", False), "stall": v.get("stall"), "plans": v.get("plans")}
    if MU_MODE == "engine" and sa and sb:
        import _mu_engine as _ME
        ah, ar, am, bh, br, bm = _ME.mu_engine(sa, sb, L_REF[0])
        my_s = _effective_speed(Me, field); op_s = _effective_speed(Oe, field)
        fast = my_s > op_s
        score = (bh - ah) + (0.5 if fast else -0.5)
        return {"myh": ah, "thh": bh, "myr": ar, "thr": br, "fast": fast,
                "my_s": my_s, "op_s": op_s, "my_move": am, "th_move": bm,
                "score": score, "win": (ah < bh) or (ah == bh and fast)}
    return _mu_score_inner(Me, Oe, field)


def set_loader(L):
    """実走版1v1が使う loader を明示登録する（通常は _build が自動で入れる）。"""
    L_REF[0] = L


def _mu_score_inner(M, O, field):
    def best(a, b):
        bm, bd = None, 0.0
        for mv in a.moves:
            if mv.category == "status" or not (mv.power or 0): continue
            d = _dmg(a, b, mv, field, False, 0.0)   # 最低ロール（0.85は実効0.9775＝ほぼ最高値）
            if d > bd: bd, bm = d, mv
        return bm, bd
    mbm, md = best(M, O); tbm, td = best(O, M)
    myr = md / max(1, O.max_hp); thr = td / max(1, M.max_hp)
    myh, _ = _apply_survive(_hits(myr), O, myr,
                            _hurt_ratio(M, O, mbm, field, 0.0) if mbm else None)
    thh, _ = _apply_survive(_hits(thr), M, thr,
                            _hurt_ratio(O, M, tbm, field, 0.0) if tbm else None)
    my_s = _effective_speed(M, field); op_s = _effective_speed(O, field)
    fast = my_s > op_s
    score = (thh - myh) + (0.5 if fast else -0.5)
    win = (myh < thh) or (myh == thh and fast)
    return {"myh": myh, "thh": thh, "myr": myr, "thr": thr, "fast": fast, "my_s": my_s, "op_s": op_s,
            "my_move": mbm.name_jp if mbm else "—", "th_move": tbm.name_jp if tbm else "—",
            "score": score, "win": win}

# 簡単構築の一覧の相手＝工房・情報ページ・相性ダイアログと同じ page の版の代表型（gen_builder_data.py が targets.json と同時に書く）
BUILDER_TARGETS = os.environ.get("BUILDER_TARGETS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "builder_targets.json"))
_BTG = None


def load_builder_targets():
    global _BTG
    if _BTG is None:
        with open(BUILDER_TARGETS, encoding="utf-8") as f:
            _BTG = json.load(f)
    return _BTG


def mu_agg(scores, shares):
    """src/scripts/party-builder/matchup.ts judgeVsBuildsMulti と同じ集約（割合の重み付き平均・割合の無い型があれば等しく）。"""
    w = shares if all(x and x > 0 for x in shares) else [1] * len(scores)
    mean = sum(a * b for a, b in zip(scores, w)) / sum(w)
    return {"v": _score_sym(mean), "dep": _score_sym(min(scores)) != _score_sym(max(scores))}


# 1v1 の spec は全項目指定なので使用率表（シーズン）を引かない（ブラウザの wasm.ts と同じくシーズン無し）
MU_GRID_SEASON = ""


def _spec_score(sa, sb, L):
    r = _rust()
    if r is not None:
        return json.loads(r.mu_analyze(sa, sb, MU_GRID_SEASON))["verdict"]["score"]
    return _mu_score(_build(sa, L), _build(sb, L), BattleField())["score"]


def matchup_grid(specs, L):
    """味方×相手の種（page の版の代表型。メガX/Yは別列）の1v1相性。記号と「*」は相性ダイアログ側と同じ集約。
    spec はそのまま渡す（技を外さない・メガ石持ちはメガ前の特性で入場）＝ブラウザ（matchup.ts _pair）と同じ"""
    if L is None:
        from simulator.data import DataLoader
        L = DataLoader()
    cols = load_builder_targets()
    rows = []
    for s in specs:
        cells = []
        for g in cols:
            bs = [b for b in g["builds"] if b.get("spec")]
            cells.append(mu_agg([_spec_score(s, b["spec"], L) for b in bs], [b.get("share") for b in bs]))
        rows.append({"mon": s.split("@")[0], "cells": cells})
    return {"tops": [{"label": g["label"], "sp": g["sp"]} for g in cols], "rows": rows}

EVK6 = ["H", "A", "B", "C", "D", "S"]
def _ev_str(ev):
    return " ".join(f"{k}{x}" for k, x in zip(EVK6, ev.split("/")) if x != "0")

def _hits(ratio):
    return 999 if ratio <= 0 else math.ceil(1 / ratio)

# 満タン時のみダメージを半減する特性。2撃目以降は半減しないので、満タン時の1発ぶんを
# 全撃に当てはめると確定数を多く見積もる（例: カイリューHP168 に 満タン45/非満タン91 で確4→実際は確3）。
_FULLHP_HALVE = ("マルチスケイル", "ファントムガード")


def _hurt_ratio(M, O, mv, field, roll):
    """非満タン時（マルチスケイル等が乗らない状態）の1発あたりHP割合。
    該当特性でなければ None（呼び出し側は満タン時の値だけで計算する）。"""
    if getattr(O, "ability", None) not in _FULLHP_HALVE:
        return None
    _hp = O.hp
    try:
        O.hp = max(1, O.max_hp - 1)
        return _dmg(M, O, mv, field, False, roll) / max(1, O.max_hp)
    finally:
        O.hp = _hp


def _apply_survive(n, O, ratio, ratio_hurt=None):
    """ばけのかわ/がんじょう/きあいのタスキの『1発耐え』と、マルチスケイル系の
    『満タン時のみ半減』を確定数に反映。(n, note)。
    ばけのかわは1発目のダメージを無効化するが最大HPの1/8を消費する（battle.py:992と同仕様）。
    単純な n+1 だと削りぶんを無視して1手多く見積もる（例: 44%×3発=132%なら確3のはずが確4になる）。
    ratio=満タン時の1発あたりHP割合（必須）。ratio_hurt=非満タン時の1発あたりHP割合。"""
    if O.ability in _FULLHP_HALVE and ratio_hurt and ratio_hurt > ratio:
        # 初撃は半減、以降は等倍
        rest = 1.0 - ratio
        return (1 if rest <= 0 else 1 + math.ceil(rest / ratio_hurt)), O.ability
    if O.ability == "ばけのかわ":
        if ratio <= 0: return n + 1, "ばけのかわ"
        rest = 1.0 - 1.0 / 8.0
        return 1 + math.ceil(rest / ratio), "ばけのかわ"
    if O.ability == "がんじょう": return (2 if n == 1 else n), "がんじょう"
    if O.item == "きあいのタスキ": return (2 if n == 1 else n), "きあいのタスキ"
    return n, ""

_TOPB = None
# 提案の必然性リペアの穴判定（_necessity_verify.hole_mons）の相手パネル＝season の版。画面の一覧・素早さタブの相手は builder_targets（page の版）。
# 型は gen_party_pool.PartyGen の出どころ（POOL_SEASON が season の版のシーズンなら型プール、過去シーズンは build_pool_*.md）。
USAGE_SEASON = os.environ.get("USAGE_SEASON", "M-5")


def load_top_builds(L, n=30, k=3):
    """上位n体それぞれの『あり得る型』最大k個（採用率順・型区別＝持ち物/性格/特性/EV）。"""
    global _TOPB
    if _TOPB is not None: return _TOPB
    con = sqlite3.connect(DB)
    cd = con.execute("SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule='single'",
                     (USAGE_SEASON,)).fetchone()[0]
    names = [r[0] for r in con.execute(
        "SELECT pokemon FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=? "
        "ORDER BY rank LIMIT ?", (USAGE_SEASON, cd, n))]
    con.close()
    from gen_party_pool import PartyGen, _spec_mega
    pg = PartyGen()
    _TOPB = []
    for nm in names:
        specs = pg.pool.get(nm) or []
        seen, cand = set(), []
        for s in specs:
            it, na, mv, ev, ab = s.split("@", 1)[1].split(":")
            key = (it, na, ab, ev)              # 防御・素早さを決める要素で型を区別（技は受け側では無関係）
            if key in seen: continue
            seen.add(key)
            p = _build(s, L)
            cand.append({"p": p, "item": it, "nature": na, "ability": ab, "ev": ev,
                         "form": (p.type1, p.type2, _spec_mega(s))})   # X/Y/非メガはタイプ・ステが別＝別フォルム
        # 持ち物使用率の高い順に「持ち物ごと代表1型」を上位k（低使用率の持ち物=メガ石等は出さない）
        iu = pg.item_usage.get(nm, {})
        by_item = {}
        for c in cand:
            by_item.setdefault(c["item"], c)
        builds = [by_item[it] for it in sorted(by_item, key=lambda i: -iu.get(i, 0))[:k]]
        if builds: _TOPB.append((nm, builds))
    return _TOPB

def _stone_xy(item):
    if item.endswith(("X", "Ｘ")): return "X"
    if item.endswith(("Y", "Ｙ")): return "Y"
    return ""

def _opp_columns(L):
    """マトリクスの相手列。メガX/Y両方が存在する種のみX/Yで別列。それ以外は主流フォルム1列。"""
    cols = []
    for nm, variants in load_top_builds(L):
        groups, order = {}, []
        for v in variants:
            f = v["form"]
            if f not in groups: groups[f] = []; order.append(f)
            groups[f].append(v)
        xy_forms = [f for f in order if f[2] and _stone_xy(groups[f][0]["item"])]
        if len(xy_forms) >= 2:                              # メガX・Y両方あり＝タイプが別物なので分割
            for f in xy_forms:
                vs = groups[f]
                cols.append({"label": f"{nm}{_stone_xy(vs[0]['item'])}", "sp": nm, "variants": vs})
        else:                                               # それ以外は主流(最頻)フォルムのみ1列
            cols.append({"label": nm, "sp": nm, "variants": groups[order[0]]})
    return cols

_SPC = None


def _speed_cols(L):
    """素早さタブの相手列＝ポケモン相性の一覧・相性ダイアログと同じ page の版の代表型（列・順番・メガX/Y）。メガは素早さもメガ後"""
    global _SPC
    if _SPC is not None:
        return _SPC
    field = BattleField()
    out = []
    for g in load_builder_targets():
        bs = []
        for i, b in enumerate(g["builds"]):
            if not b.get("spec"):
                continue
            bs.append({"idx": i + 1, "s": _effective_speed(_build(b["spec"], L), field), "item": b["item"],
                       "nature": b["nature"], "ev": _ev_str("/".join(str(x) for x in b["ev"])),
                       "scarf": b["item"] == "こだわりスカーフ"})
        if bs:
            out.append({"label": g["label"], "sp": g["sp"], "builds": bs})
    _SPC = out
    return out


def speed_info(specs, L):
    """味方×相手の種（page の版の代表型）の素早さ相性。型ごとの素早さの差で『抜く／型次第／遅い』。"""
    field = BattleField()
    cols = _speed_cols(L)
    mons = [(s.split("@")[0], _build(s, L), s) for s in specs]
    rows = []
    for nm, M, s in mons:
        sp = _effective_speed(M, field)
        scarf = s.split("@", 1)[1].split(":")[0] == "こだわりスカーフ"
        cells, sure, maybe = [], 0, 0
        for c in cols:
            spds = [b["s"] for b in c["builds"]]
            mx, mn = max(spds), min(spds)
            if sp > mx: st = "win"; sure += 1
            elif sp > mn: st = "may"; maybe += 1
            else: st = "lose"
            cells.append(st)
        rows.append({"mon": nm, "spd": sp, "scarf": scarf, "cells": cells,
                     "sure": sure, "maybe": maybe})
    rows.sort(key=lambda r: -r["spd"])
    return {"tops": [{"label": c["label"], "sp": c["sp"]} for c in cols], "total": len(cols), "rows": rows}


def speed_detail(specs, mon_name, opp_name, L, label=None):
    """1マスの内訳：相手の代表型のS実数値を速い順で、自分のSと比較（どこから抜けるか）。label はメガX/Yの列の区別（無ければ種の最初の列）"""
    field = BattleField()
    mi = next((i for i, s in enumerate(specs) if s.split("@")[0] == mon_name), 0)
    M = _build(specs[mi], L)
    my_s = _effective_speed(M, field)
    my_scarf = specs[mi].split("@", 1)[1].split(":")[0] == "こだわりスカーフ"
    cols = [c for c in _speed_cols(L) if c["sp"] == opp_name]
    col = next((c for c in cols if c["label"] == label), cols[0] if cols else None)
    builds = sorted(col["builds"] if col else [], key=lambda b: -b["s"])
    return {"mon": mon_name, "opp": opp_name, "my_s": my_s, "my_scarf": my_scarf, "builds": builds}


def atk_detail(specs, mon_name, type_name, L):
    """攻撃相性セルの内訳：その味方の技一覧と、各技の指定タイプへの倍率。"""
    mi = next((i for i, s in enumerate(specs) if s.split("@")[0] == mon_name), 0)
    M = _build(specs[mi], L)
    moves = []
    for mv in M.moves:
        atk = mv.category in ("physical", "special") and bool(mv.type) and (mv.power or 0) > 0
        moves.append({"name": mv.name_jp, "type": mv.type or "", "atk": atk,
                      "eff": get_type_effectiveness(mv.type, type_name, None) if atk else None})
    return {"mon": mon_name, "type": type_name, "moves": moves}
