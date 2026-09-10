"""各ポケモンの使用率(特性/性格/持ち物/技/EV)から「ありそうな型」を列挙し md 出力。
技を役割(攻撃/設置/積み/回復/ピボット/妨害/守る)で分類し、持ち物の役割ごとに役割整合したドラフト型を提示する。
ユーザーが加筆修正してパーティ生成プールを作る土台。出力: build_pool_M-3.md
"""
import sqlite3, os, glob, json, collections

from simulator.data import NATURE_MODS

import os
SEASON = os.environ.get("SEASON", "M-3")   # 環境が変わったら SEASON=M-5 等で切り替える
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")
OUT = os.path.join(os.path.dirname(__file__), f"build_pool_{SEASON}.md")

SETUP = {"つるぎのまい","りゅうのまい","めいそう","わるだくみ","ちょうのまい","てっぺき","からをやぶる","こうそくいどう",
         "ロックカット","ビルドアップ","はらだいこ","コスモパワー","アシッドボム","てっていこうせん","ニトロチャージ",
         "アクアステップ","くさわけ","しんかのきせき","とぐろをまく","めざめるダンス","からにこもる","じこあんじ","バトンタッチ","みがわり"}
HAZARD = {"ステルスロック","どくびし","まきびし","ねばねばネット"}
RECOVERY = {"はねやすめ","じこさいせい","なまける","あさのひざし","つきのひかり","こうごうせい","タマゴうみ","ミルクのみ","ねむる","いやしのねがい","つきのひかり","さいきのいのり"}
PIVOT = {"とんぼがえり","ボルトチェンジ","クイックターン"}
PROTECT = {"まもる","みきり","トーチカ","キングシールド","ニードルガード"}
DISRUPT = {"おにび","でんじは","どくどく","どくのこな","しびれごな","ねむりごな","キノコのほうし","あくび","ちょうはつ",
           "アンコール","かなしばり","いばる","ちょうおんぱ","あやしいひかり","やどりぎのタネ","リフレクター","ひかりのかべ",
           "おいかぜ","トリックルーム","あまごい","にほんばれ","すなあらし","ゆきげしき","でんじふゆう","おきみやげ","すてゼリフ","コートチェンジ"}

OFFENSE_ITEMS = {"こだわりハチマキ","こだわりメガネ","いのちのたま","たつじんのおび","ちからのハチマキ","ものしりメガネ",
                 "もくたん","とけないこおり","しんぴのしずく","じしゃく","くろいメガネ","ようせいのハネ","どくバリ",
                 "やわらかいすな","するどいくちばし","シルクのスカーフ","りゅうのキバ","くろおび","まがったスプーン",
                 "のろいのおふだ","メタルコート","かたいいし","ぎんのこな","ピントレンズ","でんきだま",
                 "ノーマルジュエル","ながねぎ"}
SUPPORT_ITEMS = {"たべのこし","オボンのみ","オレンのみ","しろいハーブ","メンタルハーブ","あついいわ","しめったいわ",
                 "ひかりのこな","おうじゃのしるし","せんせいのツメ","かいがらのすず","きせきのタネ",
                 "ゴツゴツメット","レッドカード","だっしゅつボタン","ふうせん","しめつけバンド",
                 "エレキシード","グラスシード","ミストシード","サイコシード","グランドコート"}

def is_stone(it):
    return any(it.endswith(sfx) for sfx in
               ("ナイト", "ナイトX", "ナイトY", "ナイトZ", "ナイトＸ", "ナイトＹ", "ナイトＺ"))

# 効果が特定の技に依存する持ち物。その技が無いと型として成立しないので必須枠に入れる
BIND_MOVES = {"まとわりつく","まきつく","うずしお","すなじごく","ほのおのうず","マグマストーム","からではさむ"}
ITEM_AFFINITY = {"しめつけバンド": BIND_MOVES, "ノーマルジュエル": None}


def affinity_move(it, mv_roles):
    """持ち物が要求する技のうち、その種が最も使う1本。無ければ None。"""
    want = ITEM_AFFINITY.get(it)
    if not want:
        return None
    for n, u, r, c in mv_roles:
        if n in want:
            return n
    return None


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

        # ドラフト型（持ち物役割 × 攻撃分類）
        # 性格/EVを「使用率最上位の1組」で全型に流用すると、物理と特殊が混在する種で
        # 特殊型が一切生成されない（ガブリアスの C32 22% / ミミッキュのようきが落ちた実例）。
        # 型ごとに攻撃分類を決め、その分類と矛盾しない性格・EVを選ぶ。
        out.append("### ドラフト型（要修正）")
        ab0 = ab[0]["ability"] if ab else "—"
        atk_ph = [(n, u) for n, u, r, c in mv_roles if r == "攻撃" and c == "physical"]
        atk_sp = [(n, u) for n, u, r, c in mv_roles if r == "攻撃" and c == "special"]
        sup_n = [(n, r) for n, u, r, c in mv_roles if r != "攻撃"]

        def pick_nature(cat):
            """その分類を下げない性格のうち、攻撃実数値か素早さを上げるものを優先する。"""
            atk_stat = "attack" if cat == "physical" else "sp_attack"
            ok = [(r["nature"], NATURE_MODS.get(r["nature"], (None, None))) for r in na]
            ok = [(n, m) for n, m in ok if m[1] != atk_stat]
            for want in (atk_stat, "speed"):
                for n, (up, dn) in ok:
                    if up == want:
                        return n
            return ok[0][0] if ok else (na[0]["nature"] if na else "—")

        def pick_ev(cat):
            key = "ev_a" if cat == "physical" else "ev_c"
            for r in ev:
                if r[key]:
                    return evfmt(r)
            if ev:
                return evfmt(ev[0])
            # 下位種はEVがクロールされないことがある。無印の「—」を吐くと spec が作れないので
            # 分類に応じた標準振り（max32スケール）を置く。
            return "H2 A32 S32" if cat == "physical" else "H2 C32 S32"

        # 採用率50%以上の変化技（さいきのいのり・はねやすめ等）。型を定義するので必ず入れる
        must = [n for n, u, r, c in mv_roles if r != "攻撃" and (u or 0) >= 50.0][:2]

        def compose(role, cat):
            prim = atk_ph if cat == "physical" else atk_sp
            other = atk_sp if cat == "physical" else atk_ph
            atk_n = [n for n, u in prim] + [n for n, u in other]
            if role in ("メガ", "スカーフ", "アタッカー", "タスキ"):
                # 分類内の攻撃技→高採用の変化技→積み/守る/ピボット→分類外の攻撃技 の順で埋める。
                # 先に分類外で埋めると、特殊型に物理技が混ざって性格/EVと矛盾する。
                own = [n for n, u in prim]
                fill = must + [n for n, r in sup_n if r in ("積", "守", "ピボット", "設置")]
                keep = max(0, 4 - len(must))
                moves = must + own[:keep]
                if len(moves) < 4:
                    moves += [n for n in fill + [x for x, _ in other] if n not in moves]
                moves = moves[:4]
            else:
                pri = must + [n for n, r in sup_n
                              if r in ("設置", "回復", "妨害", "守", "積", "ピボット") and n not in must]
                pri = pri[:3]
                moves = pri + atk_n[:max(0, 4 - len(pri))]
            return (moves + atk_n + [n for n, _ in sup_n])[:4]

        # 主分類＝採用率合計が大きい側。副分類は攻撃技が2本以上あるときだけ型を立てる
        u_ph = sum(u for _, u in atk_ph)
        u_sp = sum(u for _, u in atk_sp)
        main_cat = "physical" if u_ph >= u_sp else "special"
        sub_cat = "special" if main_cat == "physical" else "physical"
        # 副分類を立てるのは「攻撃技2本以上」かつ「EVか性格に裏付けがある」ときだけ。
        # 技本数だけで立てると、特殊アタッカーに先制物理技2本があるだけで
        # 物理型が生えてしまう（インテレオンのこおりのつぶて＋アクアジェット）。
        _sub_key = "ev_c" if sub_cat == "special" else "ev_a"
        _sub_stat = "sp_attack" if sub_cat == "special" else "attack"
        _main_stat = "attack" if sub_cat == "special" else "sp_attack"
        _ev_backs = any(r[_sub_key] and (r["usage_rate"] or 0) >= 8.0 for r in ev)
        _na_backs = any((r["usage_rate"] or 0) >= 8.0
                        and (NATURE_MODS.get(r["nature"], (None, None))[0] == _sub_stat
                             or NATURE_MODS.get(r["nature"], (None, None))[1] == _main_stat)
                        for r in na)
        sub_ok = (len(atk_sp if sub_cat == "special" else atk_ph) >= 2
                  and (_ev_backs or _na_backs))

        seen = set()
        for i in it:
            if (i["usage_rate"] or 0) < 3.0:
                continue
            role = item_role(i["item"])
            cats = [main_cat]
            # 攻撃役の持ち物は物理/特殊で別型になるので両方立てる
            if sub_ok and role in ("メガ", "スカーフ", "アタッカー", "タスキ"):
                cats.append(sub_cat)
            aff = affinity_move(i["item"], mv_roles)
            for cat in cats:
                if (i["item"], cat) in seen:
                    continue
                seen.add((i["item"], cat))
                tag = "物理" if cat == "physical" else "特殊"
                moves = compose(role, cat)
                if aff and aff not in moves:
                    moves = moves[:3] + [aff]
                if not moves:
                    continue
                out.append(f"- **{role}型({tag})** [{i['item']}/{pick_nature(cat)}/{ab0}/{pick_ev(cat)}] "
                           + " / ".join(moves))

        # 採用率20%以上なのにどの型にも入らなかった技は、主分類アタッカー型の4枠目を
        # 差し替えた変種で拾う（新技が上位4本の外に落ちて学習対象から消えるのを防ぐ）
        drafted = set()
        for line in out:
            if isinstance(line, str) and line.startswith("- **"):
                drafted.update(x.strip() for x in line.split("] ")[-1].split(" / "))
        missing = [n for n, u, r, c in mv_roles if (u or 0) >= 20.0 and n not in drafted][:2]
        if missing and it:
            base_item = it[0]["item"]
            base = compose(item_role(base_item), main_cat)
            for mm in missing:
                var = base[:3] + [mm] if mm not in base[:3] else base
                out.append(f"- **変種({'物理' if main_cat=='physical' else '特殊'}/{mm})** "
                           f"[{base_item}/{pick_nature(main_cat)}/{ab0}/{pick_ev(main_cat)}] "
                           + " / ".join(var))

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
