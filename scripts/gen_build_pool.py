"""各ポケモンの使用率(特性/性格/持ち物/技/EV)から「ありそうな型」を列挙し md 出力。
技を役割(攻撃/設置/積み/回復/ピボット/妨害/守る)で分類し、持ち物の役割ごとに役割整合したドラフト型を提示する。
ユーザーが加筆修正してパーティ生成プールを作る土台。出力: build_pool_M-3.md
"""
import sqlite3, os, glob, json, collections

SEASON = "M-3"
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")
OUT = os.path.join(os.path.dirname(__file__), f"build_pool_{SEASON}.md")

SETUP = {"つるぎのまい","りゅうのまい","めいそう","わるだくみ","ちょうのまい","てっぺき","からをやぶる","こうそくいどう",
         "ロックカット","ビルドアップ","はらだいこ","コスモパワー","アシッドボム","てっていこうせん","ニトロチャージ",
         "アクアステップ","くさわけ","しんかのきせき","とぐろをまく","めざめるダンス","からにこもる","じこあんじ","バトンタッチ","みがわり"}
HAZARD = {"ステルスロック","どくびし","まきびし","ねばねばネット"}
RECOVERY = {"はねやすめ","じこさいせい","なまける","あさのひざし","つきのひかり","こうごうせい","タマゴうみ","ミルクのみ","ねむる","いやしのねがい","つきのひかり"}
PIVOT = {"とんぼがえり","ボルトチェンジ","クイックターン"}
PROTECT = {"まもる","みきり","トーチカ","キングシールド","ニードルガード"}
DISRUPT = {"おにび","でんじは","どくどく","どくのこな","しびれごな","ねむりごな","キノコのほうし","あくび","ちょうはつ",
           "アンコール","かなしばり","いばる","ちょうおんぱ","あやしいひかり","やどりぎのタネ","リフレクター","ひかりのかべ",
           "おいかぜ","トリックルーム","あまごい","にほんばれ","すなあらし","ゆきげしき","でんじふゆう","おきみやげ","すてゼリフ"}

OFFENSE_ITEMS = {"こだわりハチマキ","こだわりメガネ","いのちのたま","たつじんのおび","ちからのハチマキ","ものしりメガネ",
                 "もくたん","とけないこおり","しんぴのしずく","じしゃく","くろいメガネ","ようせいのハネ","どくバリ",
                 "やわらかいすな","するどいくちばし","シルクのスカーフ","りゅうのキバ","くろおび","まがったスプーン",
                 "のろいのおふだ","メタルコート","かたいいし","ぎんのこな","ピントレンズ","でんきだま"}
SUPPORT_ITEMS = {"たべのこし","オボンのみ","オレンのみ","しろいハーブ","メンタルハーブ","あついいわ","しめったいわ",
                 "ひかりのこな","おうじゃのしるし","せんせいのツメ","かいがらのすず","きせきのタネ"}

def is_stone(it):
    return it.endswith("ナイト") or it.endswith("ナイトX") or it.endswith("ナイトY") or it.endswith("ナイトＸ") or it.endswith("ナイトＹ")

def item_role(it):
    if is_stone(it): return "メガ"
    if it == "こだわりスカーフ": return "スカーフ"
    if it == "きあいのタスキ": return "タスキ"
    if it == "ひかりのねんど": return "壁"
    if it in OFFENSE_ITEMS: return "アタッカー"
    if it in SUPPORT_ITEMS or it.endswith("のみ"): return "耐久/支援"
    return "その他"

def role_of_move(name, cat):
    if name in HAZARD: return "設置"
    if name in RECOVERY: return "回復"
    if name in PIVOT: return "ピボット"
    if name in PROTECT: return "守"
    if name in SETUP: return "積"
    if name in DISRUPT: return "妨害"
    if cat == "status": return "変化"
    return "攻撃"

def main():
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    mtype = {r["name_jp"]: (r["type"], r["category"], r["power"]) for r in con.execute("SELECT name_jp,type,category,power FROM move_master")}
    from simulator.simulate import get_loader
    L = get_loader()
    def get_types(poke):
        t = L.get_pokemon_template(poke)
        return (t.type1, t.type2) if t else ("?", None)

    sp = [(r["rank"], r["pokemon"]) for r in con.execute(
        "SELECT rank,pokemon FROM pokemon_usage WHERE season=? AND rule='single' "
        "AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule='single') "
        "ORDER BY rank", (SEASON, SEASON))]

    # M-1上位73構築の実採用型（種別）を収集
    M1_DIR = os.path.join(os.path.dirname(__file__), os.environ.get("M1_TEAMS_DIR", "f1_cache"))
    def _parse_spec(spec):
        head, *rest = spec.split("@"); seg = rest[0].split(":") if rest else []
        g = lambda i: seg[i] if len(seg) > i else ""
        return head, g(0), g(1), g(2), g(3), g(4)
    def _ev_str(ev):
        try: v = [int(x) for x in ev.split("/")]
        except Exception: return ev
        return " ".join(f"{k}{n}" for k, n in zip(["H","A","B","C","D","S"], v) if n) or "なし"
    m1 = collections.defaultdict(collections.Counter)
    for fp in glob.glob(os.path.join(M1_DIR, "*.json")):
        try: party = json.load(open(fp, encoding="utf-8")).get("subject_party", [])
        except Exception: continue
        for spec in set(party):
            m1[_parse_spec(spec)[0]][spec] += 1
    def m1_lines(name):
        if name not in m1: return []
        ls = ["### M-1上位実型"]
        for spec, cnt in m1[name].most_common():
            _, it_, na_, mv_, ev_, ab_ = _parse_spec(spec)
            ls.append(f"- [{it_}/{na_}/{ab_}/{_ev_str(ev_)}] " + mv_.replace("|", " / ") + (f" ×{cnt}" if cnt > 1 else ""))
        return ls

    def top(table, col, poke, lim, extra=""):
        q = (f"SELECT {col} FROM {table} WHERE season=? AND rule='single' AND pokemon=? "
             f"AND crawled_date=(SELECT MAX(crawled_date) FROM {table} WHERE season=? AND rule='single' AND pokemon=?) "
             f"ORDER BY rank LIMIT {lim}")
        return [dict(r) for r in con.execute(q, (SEASON, poke, SEASON, poke))]

    out = [f"# {SEASON} 型プール候補（使用率ベース・要加筆修正）\n",
           "各ポケモンの使用率から型を機械列挙したドラフト。技は役割で分類（攻=攻撃 / 設=設置 / 積=積み / 回=回復 / ピ=ピボット / 妨=妨害 / 守=守る / 変=その他変化）。\n",
           "ドラフト型は「持ち物の役割×役割整合した技」で自動生成。性格/EVは使用率最上位の値（型ごとの実配分は要修正）。\n"]

    for rank, poke in sp:
        t1, t2 = get_types(poke)
        tstr = t1 + ("/" + t2 if t2 else "")
        ab = top("pokemon_abilities","ability,usage_rate",poke,3)
        na = top("pokemon_natures","nature,usage_rate",poke,4)
        it = top("pokemon_items","item,usage_rate",poke,6)
        mv = top("pokemon_moves","move,usage_rate",poke,14)
        ev = top("pokemon_evs","ev_spread,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate",poke,4)

        def evfmt(r):
            parts = [f"{k}{r['ev_'+k.lower()]}" for k in ["H","A","B","C","D","S"] if r["ev_"+k.lower()]]
            return " ".join(parts) or "なし"

        # 技を役割分類
        mv_roles = []
        for m in mv:
            nm = m["move"]; cat = mtype.get(nm, ("?","?",None))[1]
            mv_roles.append((nm, m["usage_rate"], role_of_move(nm, cat), cat))
        atk = [(n,u,r) for n,u,r,c in mv_roles if r == "攻撃"]
        sup = [(n,u,r) for n,u,r,c in mv_roles if r != "攻撃"]

        out.append(f"\n## {poke}  #{rank}  {tstr}")
        out.append(f"- 特性: " + " / ".join(f"{a['ability']}({(a['usage_rate'] or 0):.0f})" for a in ab))
        out.append(f"- 性格: " + " / ".join(f"{n['nature']}({(n['usage_rate'] or 0):.0f})" for n in na))
        out.append(f"- 持ち物: " + " / ".join(f"{i['item']}({(i['usage_rate'] or 0):.0f})" for i in it))
        out.append(f"- EV: " + " / ".join(f"[{evfmt(e)}]({(e['usage_rate'] or 0):.0f})" for e in ev))
        out.append(f"- 攻撃技: " + " / ".join(f"{n}({u:.0f})" for n,u,r in atk))
        out.append(f"- 変化技: " + " / ".join(f"{n}({u:.0f}){r}" for n,u,r in sup) if sup else "- 変化技: —")

        # ドラフト型（持ち物役割ごと）
        out.append("### ドラフト型（要修正）")
        nat0 = na[0]["nature"] if na else "—"
        ev0 = evfmt(ev[0]) if ev else "—"
        ab0 = ab[0]["ability"] if ab else "—"
        seen_roles = set()
        for i in it:
            if (i["usage_rate"] or 0) < 5.0: continue
            role = item_role(i["item"])
            if role in seen_roles: continue
            seen_roles.add(role)
            atk_n = [n for n,u,r in atk]
            sup_n = [(n,r) for n,u,r in sup]
            if role in ("メガ","スカーフ","アタッカー","タスキ"):
                moves = atk_n[:4]
                # 高採用の積みがあれば4枠目を置換
                setups = [n for n,r in sup_n if r == "積" ]
                if setups and len(moves) >= 4:
                    moves = atk_n[:3] + setups[:1]
            else:  # 耐久/支援/壁
                pri = [n for n,r in sup_n if r in ("設置","回復","妨害","守","積","ピボット")][:3]
                moves = pri + atk_n[:max(0, 4-len(pri))]
            moves = (moves + atk_n + [n for n,_ in sup_n])[:4]
            out.append(f"- **{role}型** [{i['item']}/{nat0}/{ab0}/{ev0}] " + " / ".join(moves))

        out += m1_lines(poke)   # この種の M-1上位実型を項目末尾に追加

    covered = {p for _, p in sp}
    extra = sorted(n for n in m1 if n not in covered)
    if extra:
        out.append("\n## （M-1上位のみ・M-3使用率圏外）")
        for n in extra:
            out.append(f"\n### {n}")
            out += m1_lines(n)[1:]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"完了: {len(sp)}種 → {OUT}")

if __name__ == "__main__":
    main()
