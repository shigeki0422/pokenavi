"""特性をeffect_textから効果カテゴリへ機械割当し、ネット入力用 ability_categories.py を生成。
impact主観を排し「効果タイプ」で分類。1特性が複数カテゴリに属してよい。
母集合=環境出現+メガ特性 − NO_SINGLE_BATTLE_EFFECT。
"""
import sqlite3, re
from simulator.abilities import NO_SINGLE_BATTLE_EFFECT

DB = "pokenavi.db"

# (カテゴリ名, effect_text正規表現)。順序=ビット位置。
CATS = [
    ("weather_set",        r"ターンの間.*(あめ|すなあらし|ゆき|にほんばれ)状態にする|天気が常に晴れ"),
    ("weather_speed",      r"(あめ|にほんばれ|すなあらし|ゆき)状態の時.*素早さが2倍"),
    ("weather_cond",       r"(あめ|にほんばれ|すなあらし|ゆき|ひざし|天気|天候)"),
    ("terrain",            r"フィールド"),
    ("status_immune",      r"状態(異常)?にならない|状態にならず"),
    ("status_cure",        r"状態(異常)?が治る"),
    ("type_absorb_immune", r"タイプの技が効か(ず|ない)|地面にいない|寄せつけ"),
    ("contact_punish",     r"接触.*受けると"),
    ("contact_negate",     r"接触技ではなくなる"),
    ("crit_immune",        r"急所に当たらない"),
    ("crit_boost",         r"急所(に当て|アップ)|きゅうしょ"),
    ("statdrop_immune",    r"下げられない|能力ランクが下がらない|下がらない|下げる効果を受け(ず|ない)"),
    ("statdrop_retaliate", r"下げられると.*上がる"),
    ("damage_boost",       r"威力が(1\.\d+|[2-9](\.\d+)?)倍|[\d.]+倍の威力|威力が\d+%"),
    ("damage_reduce",      r"受けるダメージが(半減|1/2|3/4)|ダメージを(半分|3/4|半減)|ダメージが半分"),
    ("pinch_boost",        r"1/3以下になると.*威力が1\.5倍"),
    ("priority_up",        r"優先度が1(段階)?上がる|最初に行動"),
    ("priority_last",      r"最後に行動"),
    ("priority_block",     r"先制技(を)?使えない"),
    ("trap",               r"交代できなくなる"),
    ("intimidate",         r"相手の攻撃を1段階下げる"),
    ("intimidate_immune",  r"いかく」?(も)?効かない"),
    ("flinch_immune",      r"ひるま(ず|ない)"),
    ("inflict_on_hit",     r"(接触技を当て|攻撃すると|攻撃を当て|攻撃で相手).*?(状態|急所)"),
    ("heal_eot",           r"ターン終わり.*回復|HPが減らず.*回復|ターン終わりにHPが"),
    ("heal_switch",        r"手持ちに戻ると.*回復"),
    ("ground_immune",      r"地面にいない|じめん技.*効かない"),
    ("accuracy_evasion",   r"命中率(が|を|が0)|回避率(が|を)"),
    ("ability_change",     r"特性を.*(入れ替|にする|同じ)|特性になる|変身"),
    ("form_type_change",   r"タイプ(に|が).*(変化|変わる|なり|なる)|タイプになる|フォルム"),
    ("indirect_immune",    r"攻撃以外ではダメージ|粉の技|音の技が効かない|弾の技が効かない|ダメージが効かない|ダメージを受けない"),
    ("multi_hit",          r"連続(攻撃|技|攻撃になる)|2回の連続"),
    ("ko_boost",           r"倒すと.*上がる"),
    ("ko_retaliate",       r"ひんしになっ?た?時|ひんしになると.*ダメージ"),
    ("item_interact",      r"道具"),
    ("berry_interact",     r"きのみ"),
    ("setup_each_turn",    r"ターン(の)?終わりに.*上がる|ターン終わりに能力"),
    ("recoil_immune",      r"ダメージを受ける技を出してもHPが減らない|反動"),
    ("stat_on_damaged",   r"(技の)?ダメージを受けると.*(上がる|下がる|状態)|急所に当たると.*上がる|HPが1/2以下になると.*上がる|ひるむと.*上がる"),
    ("status_move_block",  r"変化技を受け(ない|ず)|変化技.*跳ね返す"),
    ("ignore_ability",     r"特性に関係なく|特性を無視"),
    ("ignore_protect",     r"守りの効果を無視|まもる.*無視|みがわりを無視|リフレクター.*無視|ひかりのかべ.*無視|守りを無視|守る.*貫通"),
    ("ignore_stat_change", r"能力変化を無視|能力ランクを無視"),
    ("status_cond_boost",  r"状態異常の(時|とき).*(倍|上がる)|状態異常になると.*(倍|上がる)"),
    ("block_secondary",    r"追加効果が(効かない|なくなる)"),
    ("weight_mod",         r"重さが"),
    ("stat_reversal_copy", r"能力変化が逆転|同じように能力が上がる|どれかが2段階上がり"),
    ("durability_endure",  r"HPを1残して耐える|ダメージの代わりに|満タンの時(に)?受けるダメージが半減|満タンの時.*耐える"),
    ("screen_remove",      r"(かべ|リフレクター|オーロラベール).*(解除)"),
    ("explosion_block",    r"爆発技"),
    ("inflict_flinch",     r"ひるませる"),
    ("inflict_special",    r"状態.*にできる|相手も同じ状態にする"),
    ("illusion",           r"姿で現れる|姿で"),
    ("form_morph",         r"姿を変える"),
]

def main():
    con = sqlite3.connect(DB)
    envab = set(r[0] for r in con.execute("SELECT DISTINCT ability FROM pokemon_abilities"))
    megaab = set(r[0] for r in con.execute("SELECT DISTINCT ability FROM pokemon_mega_stats WHERE ability IS NOT NULL"))
    singles = sorted(a for a in (envab | megaab) if a not in NO_SINGLE_BATTLE_EFFECT)
    em = {r[0]: (r[1] or "") for r in con.execute("SELECT name_jp,effect_text FROM ability_master")}
    pats = [(n, re.compile(p)) for n, p in CATS]
    mapping = {}
    uncovered = []
    for a in singles:
        txt = em.get(a, "")
        bits = [1 if rx.search(txt) else 0 for _, rx in pats]
        mapping[a] = bits
        if not any(bits):
            uncovered.append(a)
    # 書き出し
    with open("simulator/ability_categories.py", "w", encoding="utf-8") as f:
        f.write('"""自動生成（gen_ability_categories.py）: 特性→効果カテゴリのビット。手編集しない。"""\n')
        f.write("CATEGORIES = [\n")
        for n, _ in CATS:
            f.write(f"    {n!r},\n")
        f.write("]\n\n")
        f.write("ABILITY_CAT_BITS = {\n")
        for a in singles:
            f.write(f"    {a!r}: {mapping[a]},\n")
        f.write("}\n")
    # 種族ごとの「特性 事前分布」加重カテゴリ（相手の未知特性のマスク用＝不完全情報）
    # pokemon_abilities の使用率で重み付け。判明前はこの分布をネットに与える（真値は与えない）。
    rows2 = con.execute("""SELECT pokemon, ability, AVG(usage_rate) FROM pokemon_abilities
                           GROUP BY pokemon, ability""").fetchall()
    sp_rates = {}
    for pk, ab, rate in rows2:
        if ab in mapping:  # シングル有効特性のみ
            sp_rates.setdefault(pk, {})[ab] = (rate or 0.0)
    species_prior = {}
    for pk, ar in sp_rates.items():
        tot = sum(ar.values()) or 1.0
        soft = [0.0] * len(CATS)
        for ab, r in ar.items():
            w = r / tot
            for i, b in enumerate(mapping[ab]):
                if b:
                    soft[i] += w
        species_prior[pk] = [round(x, 4) for x in soft]
    with open("simulator/ability_categories.py", "a", encoding="utf-8") as f:
        f.write("\n# 種族→特性事前分布の加重カテゴリ（相手の未知特性マスク用）\n")
        f.write("SPECIES_PRIOR_CATS = {\n")
        for pk in sorted(species_prior):
            f.write(f"    {pk!r}: {species_prior[pk]},\n")
        f.write("}\n")
    print(f"カテゴリ数: {len(CATS)} / 特性数: {len(singles)} / 種族事前分布: {len(species_prior)}")
    print(f"未被覆(0カテゴリ): {len(uncovered)}件: {uncovered}")
    # カテゴリ別件数
    for i, (n, _) in enumerate(CATS):
        c = sum(mapping[a][i] for a in singles)
        print(f"  {n}: {c}")

if __name__ == "__main__":
    main()
