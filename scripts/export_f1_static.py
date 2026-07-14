"""上位環境シミュレーション（feature1）の計算結果を、本番（Cloudflare Pages＋R2）配信用の
静的JSONに書き出す。sim_server を介さず f1_cache/*.json を直接読み、フロントがAPIの代わりに
読み込める形（主役ごと1ファイル＋グローバル4ファイル）にする。

出力先: scripts/sim_export/
  index.json          … {generated, ai_ver, subjects:[{label,file,win_rate,n}]}
  rankers.json        … [{label, party:[spec,...]}]
  saved.json          … {label:{cards:[{label,specs,win_rate,wins,losses,draws,n}]}}（一覧/勝率用・recordsなし）
  icons.json          … {pokemon名: dex画像ID}
  move_types.json     … {技名: タイプ}
  subjects/<safe>.json… {subject, cards(summary), opp:{label:{faults,matchup,replays}}, vs_pokemon}

faults / vs_pokemon は sim_server のendpoint実装と同一ロジック（本番はこのエクスポートが真実源）。
matchup は simulator.matchup_explain.explain_matchup を再利用（メガ後評価込み）。
"""
import glob
import json
import os
import sqlite3

from simulator.simulate import get_loader
from simulator.matchup_explain import explain_matchup
from simulator.pokemon import parse_pokemon_spec

CACHE_DIR = os.environ.get("F1_CACHE_DIR", os.path.join(os.path.dirname(__file__), "f1_cache"))
# META（index/icons/move_types）はサイトに同梱＝public/sim-data/。subjects はR2へ上げるためステージング。
META_DIR = os.environ.get("F1_META_DIR", os.path.join(os.path.dirname(__file__), "..", "public", "sim-data"))
SUBJ_DIR = os.environ.get("F1_SUBJ_DIR", os.path.join(os.path.dirname(__file__), "sim_export", "subjects"))
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")
SEASON = os.environ.get("F1_SEASON", "M-2")
EVK = ["H", "A", "B", "C", "D", "S"]

# 複数シーズンをまとめて出力する場合は F1_CACHE_DIRS="M-2:f1_cache,M-3:f1_cache_m3" のように指定する。
# 未指定時は従来どおり CACHE_DIR/SEASON 単一シーズンのみを出力する（後方互換）。
_CACHE_DIRS_ENV = os.environ.get("F1_CACHE_DIRS", "")
if _CACHE_DIRS_ENV:
    SEASON_CACHE_PAIRS = []
    for pair in _CACHE_DIRS_ENV.split(","):
        season, _, cache_dir = pair.partition(":")
        cache_dir = cache_dir if os.path.isabs(cache_dir) else os.path.join(os.path.dirname(__file__), cache_dir)
        SEASON_CACHE_PAIRS.append((season.strip(), cache_dir.strip()))
else:
    SEASON_CACHE_PAIRS = [(SEASON, CACHE_DIR)]

_loader = get_loader()


def _safe(name):
    return "".join(c if c.isalnum() else "_" for c in name)


def compute_faults(card):
    """sim_server.f1_faults と同一ロジック（敗因要約・選出頻度・勝ち/負け筋・battle_results）。"""
    recs = card["records"]; losses = card["losses"]
    opp_survive = {}; your_dead = {}; setup_loss = 0
    sel_me = {}; sel_opp = {}
    for r in recs:
        for nm in r.get("selected1", []):
            sel_me[nm] = sel_me.get(nm, 0) + 1
        for nm in r.get("selected2", []):
            sel_opp[nm] = sel_opp.get(nm, 0) + 1
    for r in recs:
        if r["result"] == 2:
            swept = False
            for nm, boosts in r["opp_alive"]:
                opp_survive[nm] = opp_survive.get(nm, 0) + 1
                if boosts >= 3:
                    swept = True
            if swept:
                setup_loss += 1
            for nm in r["own_dead"]:
                your_dead[nm] = your_dead.get(nm, 0) + 1
    own_carry = {}; opp_ko = {}
    for r in recs:
        if r["result"] == 1:
            alive_opp = {nm for nm, _ in r.get("opp_alive", [])}
            for nm in r.get("selected2", []):
                if nm not in alive_opp:
                    opp_ko[nm] = opp_ko.get(nm, 0) + 1
            dead_me = set(r.get("own_dead", []))
            for nm in r.get("selected1", []):
                if nm not in dead_me:
                    own_carry[nm] = own_carry.get(nm, 0) + 1
    sl = max(1, losses); wn = max(1, card["wins"])
    survive = sorted(opp_survive.items(), key=lambda x: -x[1])
    dead = sorted(your_dead.items(), key=lambda x: -x[1])
    carry = sorted(own_carry.items(), key=lambda x: -x[1])
    ko = sorted(opp_ko.items(), key=lambda x: -x[1])
    parts = []
    if survive:
        parts.append("敗北時、相手の" + "・".join(f"{n}({round(c/sl*100)}%)" for n, c in survive[:3]) + "が生存（倒し切れていない核）")
    if setup_loss >= max(1, losses * 0.3):
        parts.append(f"積み全抜きでの敗北が{round(setup_loss/sl*100)}%")
    if dead:
        parts.append("自分の" + "・".join(f"{n}({round(c/sl*100)}%)" for n, c in dead[:3]) + "が落ちやすい")
    summary = "。".join(parts) + "。" if parts else "明確な偏りは少ない。"
    return {"n": card["n"], "wins": card["wins"], "losses": card["losses"], "draws": card["draws"],
            "win_rate": card["win_rate"], "summary": summary, "setup_loss_rate": setup_loss / sl,
            "opp_survive_on_loss": [{"name": k, "rate": round(v / sl, 2)} for k, v in survive[:5]],
            "your_dead_on_loss": [{"name": k, "rate": round(v / sl, 2)} for k, v in dead[:5]],
            "own_carry_on_win": [{"name": k, "rate": round(v / wn, 2)} for k, v in carry[:5]],
            "opp_ko_on_win": [{"name": k, "rate": round(v / wn, 2)} for k, v in ko[:5]],
            "battle_results": [r["result"] for r in recs],
            "sel_me": sorted(sel_me.items(), key=lambda x: -x[1]),
            "sel_opp": sorted(sel_opp.items(), key=lambda x: -x[1])}


def compute_vs_pokemon(cards, season=SEASON):
    """sim_server.f1_vs_pokemon と同一ロジック（相手ポケモン別の実戦勝敗＋型別内訳）。"""
    def outcome_key(res):
        return "wins" if res == 1 else ("losses" if res == 2 else "draws")
    agg = {}
    for card in cards:
        name2build = {}
        for s in card.get("specs", []):
            p = parse_pokemon_spec(s); nm = p["name"]
            tpl = _loader.get_pokemon_template(nm, season)
            if tpl is not None:
                nm = tpl.name
            ev = p.get("evs") or {}
            evt = tuple(ev.get(k, 0) for k in EVK)
            sig = (p.get("item"), p.get("nature"), p.get("ability"), tuple(sorted(p.get("moves") or [])))
            name2build[nm] = {"sig": sig, "spec": s, "item": p.get("item"), "nature": p.get("nature"),
                              "ability": p.get("ability"), "moves": p.get("moves") or [], "evt": evt}
        for rec in card.get("records", []):
            k = outcome_key(rec.get("result"))
            for nm in rec.get("selected2", []):
                e = agg.setdefault(nm, {"wins": 0, "losses": 0, "draws": 0, "builds": {}})
                e[k] += 1
                bi = name2build.get(nm)
                if bi is None:
                    continue
                b = e["builds"].setdefault(bi["sig"], {"wins": 0, "losses": 0, "draws": 0,
                                                       "labels": set(), "info": bi, "evc": {}})
                b[k] += 1; b["labels"].add(card["label"])
                b["evc"][bi["evt"]] = b["evc"].get(bi["evt"], 0) + 1
    out = []
    for nm, e in agg.items():
        tot = e["wins"] + e["losses"] + e["draws"]
        builds = []
        for sig, b in e["builds"].items():
            bt = b["wins"] + b["losses"] + b["draws"]; info = b["info"]
            rep = max(b["evc"], key=b["evc"].get) if b["evc"] else tuple([0] * 6)
            evs = {EVK[i]: rep[i] for i in range(6)} if any(rep) else None
            builds.append({"spec": info["spec"], "item": info["item"], "nature": info["nature"],
                           "ability": info["ability"], "moves": info["moves"], "evs": evs,
                           "ev_variants": len(b["evc"]), "labels": sorted(b["labels"]),
                           "wins": b["wins"], "losses": b["losses"], "draws": b["draws"],
                           "n": bt, "win_rate": (b["wins"] / bt) if bt else 0.0, "_evt": list(rep)})
        builds.sort(key=lambda x: ((x["item"] or ""), (x["nature"] or ""),
                                   tuple(sorted(x["moves"])), tuple(x["_evt"]), (x["ability"] or "")))
        for x in builds:
            x.pop("_evt", None)
        out.append({"name": nm, "wins": e["wins"], "losses": e["losses"], "draws": e["draws"],
                    "n": tot, "win_rate": (e["wins"] / tot) if tot else 0.0, "builds": builds})
    out.sort(key=lambda x: (x["win_rate"], -x["n"]))
    return {"pokemon": out}


def _slim_poke(p):
    """リプレイ描画が実際に使う項目だけ残す（moves/各種volatile/mega_name等は未使用なので捨てる）。
    falsyな状態・フォルム・能力変化は省略してさらに圧縮。"""
    o = {"name": p.get("name"), "hp": p.get("hp"), "max_hp": p.get("max_hp"),
         "type1": p.get("type1"), "type2": p.get("type2"), "alive": p.get("alive")}
    if p.get("status"):
        o["status"] = p["status"]
    for k in ("mega", "hero", "blade_forme", "disguise_broken", "electro_charged",
              "confused", "seeded", "taunt", "encore", "salted", "transformed"):
        if p.get(k):
            o[k] = True
    for k in ("substitute_hp", "illusion_name"):
        if p.get(k):
            o[k] = p[k]
    st = {k: v for k, v in (p.get("stages") or {}).items() if v}
    if st:
        o["stages"] = st
    return o


def _slim_side(s):
    o = {"active_idx": s.get("active_idx", 0),
         "party": [_slim_poke(p) for p in s.get("party", [])]}
    for k in ("reflect", "light_screen", "aurora_veil", "stealth_rock", "spikes", "toxic_spikes"):
        if s.get(k):
            o[k] = s[k]
    return o


def _slim_turn(t):
    o = {"turn": t.get("turn"), "logs": t.get("logs", []),
         "side1": _slim_side(t.get("side1", {})), "side2": _slim_side(t.get("side2", {}))}
    if t.get("weather"):
        o["weather"] = t["weather"]; o["weather_count"] = t.get("weather_count", 0)
    if t.get("trick_room"):
        o["trick_room"] = True; o["trick_room_count"] = t.get("trick_room_count", 0)
    if t.get("expl1"):
        o["expl1"] = t["expl1"]
    if t.get("expl2"):
        o["expl2"] = t["expl2"]
    return o


def _replay(rec):
    return {"selected1": rec["selected1"], "selected2": rec["selected2"],
            "turns": [_slim_turn(t) for t in rec.get("turns", [])],
            "result": rec["result"], "winner": rec["winner"]}


def _normalize_poke_name(n):
    return n.replace(" (", "(")


def export_icons(con):
    rows = con.execute(
        "SELECT DISTINCT pokemon, pokemon_id FROM pokemon_usage "
        "WHERE rule='single' AND pokemon_id GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]'").fetchall()
    out = {}
    for r in rows:
        out[_normalize_poke_name(r["pokemon"])] = r["pokemon_id"]
        if ":" in r["pokemon"]:
            base, _, form = r["pokemon"].partition(":")
            out[f"{base}({form})"] = r["pokemon_id"]
    return out


def main():
    os.makedirs(META_DIR, exist_ok=True)
    os.makedirs(SUBJ_DIR, exist_ok=True)
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row

    rankers = {}; saved = {}; index_subjects = []; ai_ver = None
    for season, cache_dir in SEASON_CACHE_PAIRS:
        files = sorted(glob.glob(os.path.join(cache_dir, "*.json")))
        print(f"[{season}] 対象: {len(files)} 主役ファイル ({cache_dir})")
        for i, fp in enumerate(files, 1):
            with open(fp, encoding="utf-8") as f:
                d = json.load(f)
            subj = d["subject_label"]; party = d["subject_party"]; cards = d["cards"]
            ai_ver = d.get("ai_ver")
            rankers[subj] = party
            # cards summary（recordsを除く）
            summary = [{"label": c["label"], "specs": c["specs"], "win_rate": c["win_rate"],
                        "wins": c["wins"], "losses": c["losses"], "draws": c["draws"], "n": c["n"]} for c in cards]
            saved[subj] = {"cards": summary}
            wr = (sum(c["win_rate"] for c in cards) / len(cards)) if cards else None
            index_subjects.append({"label": subj, "file": _safe(subj) + ".json",
                                   "win_rate": wr, "n": cards[0]["n"] if cards else 0,
                                   "party": party})
            # per-subject 詳細
            opp = {}
            for c in cards:
                opp[c["label"]] = {
                    "faults": compute_faults(c),
                    "matchup": explain_matchup(party, c["specs"], _loader, season),
                    "replays": [_replay(r) for r in c.get("records", [])],
                }
            vp = compute_vs_pokemon(cards, season)
            for p in vp["pokemon"]:   # VSポケモン代表型の1v1表（静的配信で計算できないため事前生成）
                if p["builds"]:
                    p["matchup"] = explain_matchup(party, [p["builds"][0]["spec"]], _loader, season)
            out = {"subject": {"label": subj, "party": party}, "cards": summary,
                   "opp": opp, "vs_pokemon": vp}
            with open(os.path.join(SUBJ_DIR, _safe(subj) + ".json"), "w", encoding="utf-8") as f:
                json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
            print(f"  [{i}/{len(files)}] {subj}")

    # rankers は全登録パーティ（相手の構成表示用）。cacheに無い主役も含めるため env から補完
    try:
        from simulator.env import load_registered_parties, spec_to_string
        for p in load_registered_parties(_loader, complete_only=True):
            rankers.setdefault(p.label, [spec_to_string(s) for s in p.specs])
    except Exception as e:
        print("  (rankers env補完スキップ:", e, ")")

    def w(name, obj):   # META はサイト同梱（public/sim-data/）
        with open(os.path.join(META_DIR, name), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
    w("rankers.json", [{"label": k, "party": v} for k, v in sorted(rankers.items())])
    w("saved.json", saved)
    w("icons.json", export_icons(con))
    w("move_types.json", {r["name_jp"]: r["type"]
                          for r in con.execute("SELECT name_jp, type FROM move_master").fetchall()})
    w("index.json", {"ai_ver": ai_ver, "subjects": index_subjects})
    print(f"完了: META→{META_DIR}（同梱）/ subjects→{SUBJ_DIR}（R2へアップロード）  主役{len(files)}/rankers{len(rankers)}")


if __name__ == "__main__":
    main()
