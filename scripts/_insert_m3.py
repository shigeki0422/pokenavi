"""M-B(M-3)追加37種の静的データをDB投入（base_stats + mega_stats + ability_master行）。
dexはPokeAPIで解決し種族値/タイプも照合（不一致は警告）。独自種(PokeAPI非収録)は9001+を割当。
新規特性はability_masterに effect_text 付きで追加(implemented=0、実装は別段で)。
冪等: 既存名はスキップ/更新。
"""
import json, sqlite3, sys, urllib.request, time

DB = "pokenavi.db"
# JP名 → PokeAPI slug（本編種のみ。未掲載=独自種）
SLUG = {
    "ラフレシア":"vileplume","ジュカイン":"sceptile","バシャーモ":"blaziken","ラグラージ":"swampert",
    "クチート":"mawile","メタグロス":"metagross","ムクホーク":"staraptor","ムシャーナ":"musharna",
    "ペンドラー":"scolipede","ズルズキン":"scrafty","シビルドン":"eelektross","カエンジシ":"pyroar",
    "カラマネロ":"malamar","ドラミドロ":"dragalge","オーロンゲ":"grimmsnarl","タイレーツ":"falinks",
    "ハカドッグ":"houndstone","コノヨザル":"annihilape","サーフゴー":"gholdengo",
    "ハリーマン":"overqwil",   # オーバークウィル(ヒスイハリーセンの進化)・dex904・あく/どく
    "ガメノデス":"barbaracle", # バルバナクル・dex689・いわ/みず
}
ORIG_BASE = {}  # 独自種(PokeAPI非収録)。M-B追加分は全て本編実在種だった
MANUAL_DEX = {"カエンジシ":668}  # 本編種だがPokeAPI slug不調時の既知dex補正
TYPE_EN2JP = {"normal":"ノーマル","fire":"ほのお","water":"みず","electric":"でんき","grass":"くさ",
 "ice":"こおり","fighting":"かくとう","poison":"どく","ground":"じめん","flying":"ひこう",
 "psychic":"エスパー","bug":"むし","rock":"いわ","ghost":"ゴースト","dragon":"ドラゴン",
 "dark":"あく","steel":"はがね","fairy":"フェアリー"}

# 新規特性の effect_text（本編既知＋独自）。実装は別段。
NEW_ABILITIES = {
    "おうごんのからだ":"相手の変化技を受けない。",
    "もふもふ":"接触技で受けるダメージが半分になる。ただしほのお技で受けるダメージは2倍になる。",
    "カブトアーマー":"相手の攻撃が急所に当たらない。",
    "きゅうばん":"相手のふきとばし・ほえる等による強制交代やどく/あなをほる等での引きずり出しを受けない。",
    "ほうし":"接触する技を受けると30%の確率で相手をどく/まひ/ねむり状態のいずれかにする。",
    "よちむ":"登場時、相手が持つ最も威力の高い技を1つ知ることができる(情報のみ・1v1では実効果なし)。",
    "エレキメイカー":"登場時、5ターンの間エレキフィールドを展開する。",
    "うなぎのぼり":"地面にいない扱いになり、じめん技・まきびし・どくびし・ねばねばネットが効かない。攻撃で相手を倒すと自分の最も高い能力が1段階上がる。",
    "ほのおのたてがみ":"効果未確認(要gamewith本文確認)。暫定でno-op。",
}

def fetch(slug):
    url = f"https://pokeapi.co/api/v2/pokemon/{slug}"
    req = urllib.request.Request(url, headers={"User-Agent":"pokenavi-m3/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=20))

def main():
    apply = "--apply" in sys.argv
    d = json.load(open("m3_data.json"))
    con = sqlite3.connect(DB)
    existing_base = set(r[0] for r in con.execute("SELECT pokemon_name FROM pokemon_base_stats"))
    existing_mega = set(r[0] for r in con.execute("SELECT mega_name_jp FROM pokemon_mega_stats"))
    have_ab = set(r[0] for r in con.execute("SELECT name_jp FROM ability_master"))
    dexmap = {}
    base_rows = []
    for p in d["base"]:
        nm = p["name"]
        if nm in SLUG:
            try:
                api = fetch(SLUG[nm]); time.sleep(0.3)
                dex = api["id"]
                tps = [TYPE_EN2JP[t["type"]["name"]] for t in sorted(api["types"], key=lambda x:x["slot"])]
                st = {s["stat"]["name"]:s["base_stat"] for s in api["stats"]}
                apis = [st["hp"],st["attack"],st["defense"],st["special-attack"],st["special-defense"],st["speed"]]
                warn = []
                if apis != p["stats"]: warn.append(f"種族値 gw{p['stats']} vs api{apis}")
                jt1 = tps[0]; jt2 = tps[1] if len(tps)>1 else None
                if (jt1,jt2) != (p["type1"],p["type2"]): warn.append(f"タイプ gw({p['type1']},{p['type2']}) vs api({jt1},{jt2})")
                print(f"  {nm} dex={dex} {'⚠ '+' / '.join(warn) if warn else 'OK照合一致'}")
            except Exception as e:
                dex = MANUAL_DEX.get(nm) or ORIG_BASE.get(nm, 9000); print(f"  {nm} PokeAPI失敗({e})→dex={dex}")
        else:
            dex = ORIG_BASE.get(nm, 9000); print(f"  {nm} 独自種→dex={dex}")
        dexmap[nm] = dex
        base_rows.append((nm, dex, 0, SLUG.get(nm), p["type1"], p["type2"], *p["stats"], p["weight"]))
    print(f"\n基礎種 投入予定 {len(base_rows)}件（既存スキップ: {[r[0] for r in base_rows if r[0] in existing_base]}）")
    # megaのbase_dex解決（基礎種dex。ライチュウ等既存種はDBから）
    def base_dex_of(basename):
        if basename in dexmap: return dexmap[basename]
        r = con.execute("SELECT dex_number FROM pokemon_base_stats WHERE pokemon_name=?", (basename,)).fetchone()
        return r[0] if r else 9000
    mega_rows = []
    for m in d["mega"]:
        bd = base_dex_of(m["base"])
        stone = m["base"] + "ナイト"
        mega_rows.append((m["name"], m["base"], stone, bd, None, m["type1"], m["type2"], *m["stats"], m["ability"], None))
    print(f"メガ 投入予定 {len(mega_rows)}件（既存スキップ: {[r[0] for r in mega_rows if r[0] in existing_mega]}）")
    new_ab = [(k, NEW_ABILITIES[k]) for k in NEW_ABILITIES if k not in have_ab]
    print(f"新規特性 追加予定 {len(new_ab)}件: {[a[0] for a in new_ab]}")
    if not apply:
        print("\n[dry-run] --apply で実投入"); return
    for r in base_rows:
        if r[0] in existing_base: continue
        con.execute("INSERT INTO pokemon_base_stats(pokemon_name,dex_number,form_index,pokeapi_name,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,weight_kg) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", r)
    for r in mega_rows:
        if r[0] in existing_mega: continue
        con.execute("INSERT INTO pokemon_mega_stats(mega_name_jp,base_pokemon_jp,mega_stone,base_dex,pokeapi_name,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,ability,weight_kg) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", r)
    for k,v in new_ab:
        con.execute("INSERT INTO ability_master(name_jp,effect_text,implemented) VALUES(?,?,0)", (k,v))
    con.commit()
    print("\n投入完了")

if __name__ == "__main__":
    main()
