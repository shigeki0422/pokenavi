"""使用率マージナルと対戦の常識的制約から型プールを生成する。

実型（templates）を一切使わないので、過去データの無い新規ポケモンにも使える。

仕組み:
  1. 技の使用率(上位10)をそのまま目標包含確率にし、4枠に足りない分は
     「10位以下の技」枠として learnset の残りから補う（正規化して上位10技に
     背負わせると、特殊技の合計が特殊型の枠容量を超えて解が消える種が出る）
  2. 非復元抽出は「確率に比例」させても包含確率が目標に一致しない（実測で最大14pt ずれる）。
     抽出重みを不動点反復で較正し、制約による棄却も込みで包含確率を目標へ合わせる
  3. 実型でほぼ発火しない硬制約だけで棄却する（発火率は REQUIREMENTS 参照）

検証: 実型を正解として妥当性(生成型が実在する率)とマージナル誤差を測ると
  素朴 26.6%/14.3pt → 較正のみ 36.8%/0.9pt → 較正＋制約 41.0%/1.6pt

env: SEASON(M-6) SPECIES(カンマ区切り・空で使用率上位TOPN) TOPN(40) N(24) OUT(空で標準出力)
"""
import collections
import itertools
import json
import math
import os
import random
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_build_pool import SETUP_A, SETUP_C, SETUP as SETUP_ALL, RECOVERY, PROTECT, PIVOT, HAZARD
from simulator.data import NATURE_MODS
from simulator.battle import MULTI_HIT_2, MULTI_HIT_RANDOM_25

SEASON = os.environ.get("SEASON") or os.environ.get("POOL_SEASON", "M-6")
TOPN = int(os.environ.get("TOPN", "40"))
NBUILD = int(os.environ.get("N", "24"))
OUT = os.environ.get("OUT", "")
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")

# gen_build_pool の SETUP を取り込む。A/C だけにしていたため、ニトロチャージ（素早さ上昇）
# などが素の物理火力技と判定され、特殊型で引けなかった。
# てっていこうせんは能力を上げない（反動つきの火力技）。積み扱いだと主力から外れ、
# こだわり＋変化技・積み技2本の規則で上位構築（ヒスイヌメルゴン・サーフゴー）を弾いていた。
SETUP = (SETUP_ALL | SETUP_A | SETUP_C) - {"てっていこうせん"}
# gen_build_pool の一覧に無い自己強化技。漏れていて こだわりスカーフ＋ビルドアップ が出ていた。
# のろいはゴーストでは積みではなく、スカーフ＋のろいのミミッキュが上位構築にあるので入れない。
SETUP |= {"ビルドアップ", "ソウルビート", "はいすいのじん", "おかたづけ", "せいちょう", "つぼをつく",
          "たくわえる", "ドわすれ", "とける", "コットンガード", "たてこもる", "ほおばる", "じゅうでん",
          "とおぼえ", "ちいさくなる", "かげぶんしん", "きあいだめ"}
# 「積み技2本」の判定に使う集合。みがわり・バトンタッチ・じこあんじは能力上昇ではなく、
# 実型で わるだくみ+みがわり 等が普通に共存する（これらを含めると発火率4.03%）。
BOOST = SETUP - {"みがわり", "バトンタッチ", "じこあんじ"}
RECOVERY = RECOVERY | {"ちからをすいとる", "ねがいごと"}
PROTECT = PROTECT | {"こらえる"}
CHOICE = {"こだわりハチマキ", "こだわりメガネ", "こだわりスカーフ"}
# 耐久を捨てて攻撃に振る持ち物。防御上昇の性格とは噛み合わない
# （きあいのタスキは一撃を必ず耐えるので、そもそも防御に振る意味がない）。
# 実型1,842件での発火は4件=0.22%。
FRAGILE = CHOICE | {"きあいのタスキ", "いのちのたま", "たつじんのおび"}
POWER_RATIO = float(os.environ.get("POWER_RATIO", "1.4"))
DEF_UP = {"defense", "sp_defense"}
FORCE = {"ドラゴンテール", "ともえなげ", "ふきとばし", "ほえる"}
EV_KEYS = ("ev_h", "ev_a", "ev_b", "ev_c", "ev_d", "ev_s")

con = sqlite3.connect(DB)
MV = {r[0]: {"type": r[1], "cat": r[2], "power": r[3] or 0, "acc": r[4] or 0,
             "pri": r[5] or 0, "eff": r[6] or ""}
      for r in con.execute(
          "select name_jp,type,category,power,accuracy,priority,effect_text from move_master")}


# 効果テキストにこれらが出る技は「素の火力技」ではない。威力の優劣や性格の整合で
# 他の技と比べてはいけない（グラススライダーは条件付き先制、キラースピンは設置解除）。
# 広く取ると制約が効かなくなり妥当性が落ちた（37.6%→33.6%）。実害の出た4語だけに絞る。
#   優先度 … グラススライダー（グラスフィールドで先制）
#   解除/取り除 … キラースピン（設置解除が目的で威力30）
#   威力が … おはかまいり（味方の瀕死数で威力が変わる）
#   相手の攻撃 … イカサマ（相手の攻撃実数値でダメージが決まる＝特殊型でも使える）
# 除外の目的は「攻撃能力を使わない／火力以外の役割を持つ技」を層のゲートから外すこと。
# 威力が変動するだけの技を除外すると、特殊技のソーラービーム・ウェザーボールが
# 物理型にも配分される（メガリザードンX がソーラービームを持つ型が18.4%できた）。
# "HP" を入れると反動技・残HP依存技14本（とびひざげり・てっていこうせん・きしかいせい等）
# まで巻き込む。回復技はすべて「回復する」を含むので "回復" だけで足りる。
# 「道具」だけだと、道具の有無が発動条件なだけの火力技（ポルターガイスト・アクロバット）
# まで除外してしまう。除きたいのは相手の道具を奪う／失わせる技。
# 「防御の数値」… ボディプレス（攻撃ではなく防御でダメージが決まる＝ずぶとい等の耐久性格と組む）
# 「ひんしにする」「ダメージを与える」「返す」… 一撃必殺・固定ダメージ・カウンター系。
#   攻撃/特攻を使わないので性格・努力値の向きと無関係（ずぶとい＋がむしゃら は正当）。
# 「必ず命中」は外した。ヘビーボンバーの「ちいさくなる相手には必ず命中」や
#   つばめがえし（必中の普通の攻撃技）まで巻き込む。トリックフラワーは「必ず急所」で拾える。
# 語は役割そのものを指す言い回しに限る。「相手の攻撃」「回復」「解除」「ダメージを与える」「必ず急所」だと
# じゃれつく（10%で攻撃↓）・せいなるつるぎ・サイコファング・トリックフラワーまで主力から外れていた。
# ドレイン技（回復）は役割技のまま：主力にするとムーンフォース＋ドレインキッスの実型が同タイプ重複で弾かれる。
_ROLE_WORDS = ("優先度", "味方の場にかかっている", "取り除", "回復", "相手の攻撃の能力値", "防御の数値",
               "道具を奪う", "道具を失わせる",
               "ひんしにする", "数値のダメージ", "HP分のダメージ", "の1/2のダメージ", "返す")


def _plain(m):
    """付加価値のない純粋な火力技か。先制・ピボット・積み・回復・強制交代は役割が違う。
    条件付き先制や設置解除のように、効果テキストで役割が決まる技も除く。"""
    v = MV[m]
    # 威力50未満で効果を持つ技は火力ではなく補助（ほっぺすりすり威力20＝まひ撒き）。
    # 主力扱いすると特殊型で引けず、ストリンダーで使用率55%→生成0%になった。
    # 連続技（スケイルショット等）は表示威力が低いだけの火力なので除く。
    weak_util = (0 < v["power"] < 50 and v["eff"]
                 and "連続" not in v["eff"] and "回攻撃" not in v["eff"])
    # 確実に素早さを下げる技は削り役（がんせきふうじ・こごえるかぜ）。特殊型ブリジュラスも持つ
    speed_ctrl = v["eff"].startswith("相手の素早さを")
    return not (v["cat"] == "status" or v["pri"] > 0 or m in PIVOT or m in SETUP
                or m in FORCE or weak_util or speed_ctrl
                or any(w in v["eff"] for w in _ROLE_WORDS))


def orientation(moves):
    """その技構成が要求する攻撃方面。主力火力技だけを見る（先制・ピボット・搦め手は除く）。"""
    ph = sp = False
    for m in moves:
        if m not in MV:
            continue
        if m in SETUP_A:
            ph = True
        if m in SETUP_C:
            sp = True
        if not _plain(m):
            continue
        if MV[m]["cat"] == "physical":
            ph = True
        elif MV[m]["cat"] == "special":
            sp = True
    return ph, sp


def nature_side(na):
    """性格がどちらの攻撃方面を意図しているか。物理/特殊/どちらでも。

    判定は**下げた能力**だけで行う。上げた能力で決めると、攻撃を一切下げない性格
    （れいせい C↑S↓、ゆうかん A↑S↓）が片方の層に閉じ込められ、両刀型が作れない。
    ギルガルドは実型の31%が両刀で、れいせい32%・ゆうかん12%はその受け皿。
    """
    _up, down = NATURE_MODS.get(na, (None, None))
    if down == "sp_attack":
        return "phys"
    if down == "attack":
        return "spec"
    return "mix"


def side_weights(nats):
    """性格の使用率から攻撃方面の構成比を出す。これが型の層構造そのものになる。"""
    w = collections.Counter()
    for na, p in nats.items():
        w[nature_side(na)] += p
    tot = sum(w.values()) or 1.0
    return {k: v / tot for k, v in w.items() if v > 0}


MEGA = {}
MEGA_AB = {}
for _r in con.execute(
        "select base_pokemon_jp,mega_stone,attack,sp_attack,ability from pokemon_mega_stats"):
    MEGA[(_r[0], _r[1])] = (_r[2], _r[3])
    MEGA_AB[(_r[0], _r[1])] = _r[4]
BASE = {r[0]: (r[1], r[2]) for r in
        con.execute("select pokemon_name,attack,sp_attack from pokemon_base_stats")}


# 攻撃実数値を倍にする特性。素の実数値だけで物理/特殊を判断すると誤る
# （メガスターミーは A100 C130 だがちからもちで実効A200＝物理型。使用も物理89.5%）。
ATK_X2 = {"ちからもち", "ヨガパワー"}
_BASE_AB = {}
for _r in con.execute(
        "select pokemon,ability,max(usage_rate) from pokemon_abilities "
        "where season=? group by pokemon", (SEASON,)):
    _BASE_AB[_r[0]] = _r[1]


def form_stats(sp, item):
    """その持ち物で実際に戦う姿の (攻撃, 特攻)。メガ石なら A/C が入れ替わる種があり、
    ちからもち/ヨガパワーなら攻撃が2倍になる。"""
    a, c = MEGA.get((sp, item)) or BASE.get(sp) or (0, 0)
    ab = MEGA_AB.get((sp, item))
    if ab is None:
        ab = _BASE_AB.get(sp)
    if ab in ATK_X2:
        a *= 2
    # かたいツメは接触技1.3倍。メガリザードンXは A130 C130 の同値だが物理型しかいない
    if ab == "かたいツメ":
        a = int(a * 1.3)
    return a, c





# 生成中の種で、使用率が層の容量を超えるため全層に開放する持ち物。
# メガシビルドンは A145 C135 とほぼ同等で、A>C を理由に特殊層から締め出すと
# シビルドナイト83%・ひかえめ50%（特殊メガが主流）と両立せず、持ち物が40pt崩れた。
_ITEM_OPEN = set()
# 1.1だとガブリアスナイトZ（A130 C141・特殊が主流）が物理型にも付いた
MEGA_TIE = 1.05


_SSTONES = {}


def season_stones(sp, season=None):
    """そのシーズンにその種で使われているメガ石（使用率の持ち物に載っているもの）。
    ルカリオナイトZ が無かったシーズンの特殊メガルカリオは、通常のルカリオナイトを選ぶしかない"""
    key = (sp, season or SEASON)
    if key not in _SSTONES:
        have = {r[0] for r in con.execute(
            "select distinct item from pokemon_items where season=? and pokemon=?", (season or SEASON, sp))}
        _SSTONES[key] = [it for (s2, it) in MEGA if s2 == sp and it in have]
    return _SSTONES[key]


def mega_orient_ok(sp, item, moves, season=None):
    """メガ石が2種類ある種（ガブリアスナイト/ナイトZ、リザードナイトX/Y）は、技の向きに合う石を選ぶ。
    物理技だけの型に特殊寄りの石（ガブリアスナイトZ）が付いていた。石が1種類の種はどちらの向きもありうる
    （ボーマンダの特殊メガ、シビルドンの特殊メガは実在）のでデータに任せる"""
    stones = season_stones(sp, season)
    if item not in stones or len(stones) < 2:
        return True
    # 石を選べる種で、付けた石の姿の向きがはっきりしているなら、逆向きの主力技は1本も持たない
    # （メガガブリアスZ に じしん。上位構築の石2種の種のメガ108型で0件。努力値で辻褄を合わせると A32 S32 の特殊型が出た）
    fa, fc = form_stats(sp, item)
    off = "physical" if fc > fa * MEGA_TIE else "special" if fa > fc * MEGA_TIE else None
    if off and any(m in MV and _plain(m) and MV[m]["cat"] == off for m in moves):
        return False
    ph, spc = orientation(moves)
    if ph == spc:
        return True
    # 技の向きに対する姿の適性（物理なら A/C、特殊なら C/A）。もう一方の石が明らかに（1割以上）向いているなら、この石は選ばない。
    # メガルカリオ（A145 C140）は拮抗しているが、特殊の型ならルカリオナイトZ（C164 A100）を選ぶ（M-6 で Z が出てからの話）
    def fit(it):
        a, c = form_stats(sp, it)
        return (a / c) if ph else (c / a)
    # この石の姿が技の向きに向いている（1.05倍超）なら、特性目的もありうるので残す（通常メガアブソル A150 C115 の物理型）
    if fit(item) > MEGA_TIE:
        return True
    return not any(fit(it) >= fit(item) * 1.1 for it in stones if it != item)


def items_for(sp, side, items):
    """層と噛み合う持ち物だけ残す。物理型に特殊メガの石を付けない。"""
    if side == "mix":
        return items
    # 制限するのはメガ石（姿が変わって攻撃方面が決まる持ち物）だけ。
    # 非メガの持ち物を素の A/C で締め出すと、補助型（ヤミラミ A75 C65 でずぶとい主体）の
    # 特殊層にメガ石しか入れず、持ち物の周辺分布が28pt崩れた。
    out = {}
    for it, p in items.items():
        if (sp, it) in MEGA and it not in _ITEM_OPEN:
            a, cc = form_stats(sp, it)
            # 拮抗する姿は両方の型がある（メガルカリオ A145 C140 は上位構築で特殊が主流）
            if side == "phys" and cc > a * MEGA_TIE:
                continue
            if side == "spec" and a > cc * MEGA_TIE:
                continue
        out[it] = p
    return out


def gate(m, side):
    """その方面の型が採らない技を落とす。先制・ピボット・搦め手は火力を当てにしないので残す。"""
    if m == TAIL:
        return True
    if m not in MV:
        return False
    if side == "mix":
        return True
    if m in SETUP_A:
        return side == "phys"
    if m in SETUP_C:
        return side == "spec"
    if not _plain(m):
        return True
    cat = MV[m]["cat"]
    if cat == "physical":
        return side == "phys"
    if cat == "special":
        return side == "spec"
    return True


PASS_ITEM = {"トリック", "すりかえ"}


def nature_item_ok(item, nature, moves=()):
    """耐久を捨てる持ち物に防御上昇の性格を組ませない。
    ただし トリック/すりかえ でこだわりを相手に押し付ける補助型は耐久性格で組む
    （アローラペルシアンはスカーフ55%・耐久性格72%で、この規則と矛盾していた）。"""
    if item not in FRAGILE or _FRAGILE_OFF[0]:
        return True
    if item in CHOICE and set(moves) & PASS_ITEM:
        return True
    up, _dn = NATURE_MODS.get(nature, (None, None))
    return up is not None and up not in DEF_UP


def natures_for(moves, nats):
    """技構成と噛み合う性格だけを残す。性格が下げた能力の主力火力は持たない。"""
    ph, sp = orientation(moves)
    out = {}
    for na, p in nats.items():
        _up, down = NATURE_MODS.get(na, (None, None))
        if ph and down == "attack":
            continue
        if sp and down == "sp_attack":
            continue
        out[na] = p
    return out


TRICK = {"トリック", "すりかえ"}
SEEDS = {"サイコシード", "グラスシード", "エレキシード", "ミストシード"}
ITEM_NEEDS = {"カゴのみ": "ねむる"}     # 持ち物の型が必ず持つ技（上位構築 28/28）


def item_ok(moves, item):
    """こだわり系は変化技と両立しない。実型での発火率0.00%。
    持ち物と技のセット（上位構築）: カゴのみの型は必ず ねむる を持つ（28/28）、トリック/すりかえの型は必ずこだわり系（29/29）"""
    mv = set(moves)
    if item in CHOICE and (mv & (SETUP | PROTECT | RECOVERY)):
        return False
    if item in ITEM_NEEDS and ITEM_NEEDS[item] not in mv:
        return False
    # メガの型は ねむる を持たない（上位構築のメガ805型で0件）
    if item in _STONES and "ねむる" in mv:
        return False
    if mv & TRICK and item not in CHOICE:
        return False
    # タスキは満タンからの一撃を耐える持ち物で、回復技の型とは噛み合わない（上位構築のタスキ253型で0件。さいきのいのり は味方の復活なので別）
    if item == "きあいのタスキ" and mv & (RECOVERY - {"さいきのいのり"}):
        return False
    # シードは場に出たとき1回だけ能力を上げ、交代すると消える。ピボット技とは噛み合わない（M-6 からの持ち物で上位構築に例なし）
    if item in SEEDS and mv & (PIVOT | {"すてゼリフ"}):
        return False
    return True


def rest_item_w(moves, item):
    """ねむる の型は カゴのみ（上位構築 28/32）。ねごと が無いのに カゴ/ラム 以外を持つ型は大きく減らす（例外は4/32）。
    こだわり系は技を出し分けられないので、トリック/すりかえ以外の変化技を2本以上持つ型は大きく減らす（上位構築 3/259）。
    禁止にしないのは、使用率がそれを強いる種があるため（アローラペルシアン スカーフ55%・技はほぼ変化技）"""
    if "ねむる" in moves and "ねごと" not in moves and item not in ("カゴのみ", "ラムのみ"):
        return 0.1
    if item in CHOICE and sum(1 for m in moves if MV.get(m, {}).get("cat") == "status" and m not in TRICK) >= 2:
        return 0.1
    return 1.0


# 生成中の種で「使用率が併用を強制する技の対」（P[a]+P[b]>1）。鳩の巣原理で最低
# P[a]+P[b]-1 の型が両方を持つので、重複規則で禁止すると周辺分布と両立しない
# （グレイシア フリーズドライ94.6%＋れいとうビーム27.0%、ネギガナイト スターアサルト＋インファイト）。
_MUST = set()
# 生成中の種で「耐久を捨てる持ち物＋防御性格」の規則を外すか（使用率と両立しない種）
_FRAGILE_OFF = [False]
# 生成中の種で「攻撃技0本は禁止」を外すか。攻撃技の使用率の合計が1体あたり1本に
# 届かない補助型（ヤミラミ）では、攻撃技を持たない型が使用率上必ず存在する。
# 禁止すると残りの型に攻撃技を押し込み、イカサマが72%→89%に膨らんだ。
_NOATK_OK = [False]


def eff_power(m):
    """1回の使用で出る威力の期待値。連続技は表示威力×期待回数（battle._calc_hits と同じ表）。
    表示威力で比べると つららばり25 と つららおとし85 が別役割に見え、重複を弾けなかった。"""
    v = MV[m]
    p = v["power"] or 1
    if m in MULTI_HIT_2:
        return p * 2
    if m == "トリプルアクセル":
        return 120
    if m in MULTI_HIT_RANDOM_25:
        return p * 3.0
    if m == "ネズミざん":
        return p * 6.5
    return p


def _boost_clash(moves):
    """同じ攻撃能力（攻撃どうし・特攻どうし）を上げる変化技の積み技が2本。
    異なる能力の積みは実型にある（てっぺき＋こうそくいどう、コスモパワー＋めいそう、
    つるぎのまい＋ニトロチャージ）ので、「積み技2本」一律の禁止はやめた。"""
    seen = collections.Counter()
    for m in set(moves) & BOOST:
        v = MV.get(m)
        if not v or v["cat"] != "status":
            continue
        e = v["eff"].replace("特攻", "Ｃ")
        for key in ("攻撃", "Ｃ"):
            if key in e:
                seen[key] += 1
    return any(c >= 2 for c in seen.values())


def redundant(x, y):
    """同タイプ火力の重複（valid と同じ判定）。併用しないはずの2技か"""
    if x not in MV or y not in MV or not (_plain(x) and _plain(y)):
        return False
    a, b = MV[x], MV[y]
    if a["type"] != b["type"]:
        return False
    if a["cat"] == b["cat"] and a["eff"] == b["eff"]:
        return True
    pa, pb = eff_power(x), eff_power(y)
    return max(pa, pb) / min(pa, pb) < POWER_RATIO


def forced_pairs(P, real):
    """使用率が併用を強制する技の対。
    2技の合計が100%を超える対に加え、併用しないはずの技どうしのまとまりの合計が100%を超えるときは、
    まとまりで最も使われる技と他の技の対を認める（ヒスイバクフーン: ふんか76.6+もえつきる18.1+
    オーバーヒート13.3=108% で、対ごとの判定では両立できず ふんかが 7pt ずれた）"""
    out = set()
    for x, y in itertools.combinations(real, 2):
        if P[x] + P[y] > 1.0 + 0.02:
            out.add((x, y))
    adj = collections.defaultdict(set)
    for x, y in itertools.combinations(real, 2):
        if redundant(x, y):
            adj[x].add(y)
            adj[y].add(x)
    seen = set()
    for x in real:
        if x in seen or x not in adj:
            continue
        comp, stack = set(), [x]
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u)
            stack.extend(adj[u] - comp)
        seen |= comp
        if sum(P[m] for m in comp) > 1.0 + 0.02:
            top = max(comp, key=lambda m: P[m])
            for m in comp:
                if m != top:
                    out.add((top, m))
    return out


def valid(moves, item=None):
    """実型でほぼ発火しない硬制約だけ。性格との整合は valid ではなく生成順序で担保する。
    item を渡さなければ技だけのルールを見る（列挙時は持ち物を後で決めるため）。"""
    atk = [m for m in moves if m in MV and _plain(m)]
    for i, x in enumerate(atk):
        for j, y in enumerate(atk):
            if i == j:
                continue
            a, b = MV[x], MV[y]
            # 分類が違っても同タイプなら打点の範囲は同じ。実型で同タイプ2本が起きるのは
            # 威力差が大きいとき（比1.44倍以上が大半）で、分類の違いは条件になっていない。
            if a["type"] != b["type"]:
                continue
            if (x, y) in _MUST or (y, x) in _MUST:
                continue
            # 「威力も命中も勝てない＝劣位」の判定は削除した。効果の違い（反動・能力下降）を
            # 無視しており、スターアサルト170＋インファイト120 を弾いた。M-6の使用率では
            # 83.5%＋45.6%＝129%で、最低29%の型が両方を持つ（鳩の巣原理）ので両立しない。
            # 重複は下の「効果が同一」と「威力比」で判定する。
            # 効果まで同一＝純粋な上位互換（かえんほうしゃ＋だいもんじ）。実型で0.05%しか出ない
            if a["cat"] == b["cat"] and a["eff"] == b["eff"]:
                return False
            # 同タイプ同分類で威力が拮抗＝役割が重複する。効果テキストが違っても併用しない
            # （とびひざげり130＋インファイト120、うたかたのアリア90＋なみのり90）。
            # 威力差が大きいものは使い分けがある（はめつのひかり140＋ムーンフォース95）。
            # 実型での発火は威力比1.3倍未満で0.16%。
            # 分類違いの同タイプ（ポルターガイスト＋シャドーボール）も上位構築に3件(0.12%)あるが、
            # 許すと両刀の受け皿の性格で膨らむ（M-5ギルガルドで実0件→生成5.1%）ので禁止のまま
            pa, pb = eff_power(x), eff_power(y)
            if max(pa, pb) / min(pa, pb) < POWER_RATIO:
                return False
    if not _NOATK_OK[0] and not any(MV.get(m, {}).get("cat", "status") != "status"
                                    for m in moves):
        return False
    if _boost_clash(moves):
        return False
    # トリック/すりかえ はこだわり系とセット（29/29）で、こだわりは積み・守る・回復と両立しない
    if set(moves) & TRICK and set(moves) & (SETUP | PROTECT | RECOVERY):
        return False
    # 攻撃を上げる積み技なのに主力が特殊技だけ（逆も）。上位構築2460型で0件、生成ではミロカロス・ギルガルドに5%出ていた
    ph = any(MV[m]["cat"] == "physical" for m in atk)
    sp = any(MV[m]["cat"] == "special" for m in atk)
    if (set(moves) & SETUP_A and sp and not ph) or (set(moves) & SETUP_C and ph and not sp):
        return False
    # 同タイプ主力3本は明確に過剰（実型で0%）。2本は威力差があれば成立するので、
    # 重複の判定は下の威力比で行う。
    t = collections.Counter(MV[m]["type"] for m in moves if m in MV and _plain(m))
    if any(v >= 3 for v in t.values()):
        return False
    if item is not None and not item_ok(moves, item):
        return False
    return True


TAIL = "＊10位以下"


_TS = None
CORR_W = float(os.environ.get("CORR_W", "0"))   # 時系列相関から出す共起制約の強さ


def move_corr(sp):
    """その種の技どうしの使用率の連動（時系列相関）。

    セットで使われる技は型の人気が動けば一緒に動く。18時点の観測から相関を取ると、
    実際の結びつき(lift)との相関が平均+0.33（15種すべて正）で、
    連動する対は lift 1.32・逆に動く対は 0.54 だった。
    使用率の周辺分布だけでは分からない共起を、同じ使用率データから引き出せる。
    """
    global _TS
    if _TS is None:
        _TS = collections.defaultdict(dict)
        for _sp, _se, _dt, _mv, _r in con.execute(
                "select pokemon,season,crawled_date,move,usage_rate from pokemon_moves"):
            _TS[(_sp, _mv)][(_se, _dt)] = _r / 100.0
    import math
    ms = sorted({k[1] for k in _TS if k[0] == sp})
    out = {}
    for i, a in enumerate(ms):
        for b in ms[i + 1:]:
            ka, kb = _TS[(sp, a)], _TS[(sp, b)]
            pts = sorted(set(ka) & set(kb))
            if len(pts) < 5:
                continue
            x = [ka[p] for p in pts]
            y = [kb[p] for p in pts]
            n = len(x)
            mx, my = sum(x) / n, sum(y) / n
            sx = math.sqrt(sum((v - mx) ** 2 for v in x))
            sy = math.sqrt(sum((v - my) ** 2 for v in y))
            if sx < 1e-9 or sy < 1e-9:
                continue
            r = sum((u - mx) * (v - my) for u, v in zip(x, y)) / (sx * sy)
            out[(a, b)] = out[(b, a)] = r
    return out


PAIR_W = float(os.environ.get("PAIR_W", "1.0"))   # 技の対の相性（上位構築から学習）の強さ
PAIR_SEASON = tuple(x for x in os.environ.get("PAIR_SEASON", "").split(",") if x)  # 学習に使う templates のシーズン（カンマ区切り・空で全部）
LOSO = os.environ.get("LOSO", "0") == "1"           # 検証用: 対象種を学習から外す
ROLE_BACKOFF = os.environ.get("ROLE_BACKOFF", "1") == "1"
# 上位構築は少数かつ上位層に偏るので、排他（負の相性）は使用率の母集団へ持ち込まない。
# この値未満の技の対の相性は捨て、正の連動だけを学ぶ
PAIR_MIN = float(os.environ.get("PAIR_MIN", "0"))
PAIR_NEG = float(os.environ.get("PAIR_NEG", "-0.7"))   # これ以下の強い負の技の組の相性は使う
NEG_W = float(os.environ.get("NEG_W", "1"))
# 役割の対の負の相性はこの値以下だけ使う（ピボット×積み -0.66 等）。広く使うと歪む
ROLE_NEG = float(os.environ.get("ROLE_NEG", "-0.85"))   # 強い負の役割の組（積み×ピボット等）は使う。M-5 で役割の組の差 3.46→3.27pt・G2 はゲート内
# 対象種自身の過去の上位構築を、他種から学んだ相性より優先する重みの目安（件数換算）。
# 他種と共有の閾値（支持6件以上）では実型10件前後の種の対がほぼ全部落ち、
# 真の対を与えれば誤差が標本誤差まで下がる種でも 18pt 残っていた（M-5メタグロス）
OWN_K = float(os.environ.get("OWN_K", "0"))
_PAIR = {}


def own_pair_strength(sp):
    """対象種自身の上位構築だけから測った対の相性と支持件数。{(a,b): (相性, 件数)}"""
    rows = [set(m for m in mv if m) for lab, *mv in con.execute(
        "select label,move1,move2,move3,move4 from templates where pokemon=?", (sp,))
        if not PAIR_SEASON or lab.startswith(PAIR_SEASON)]
    n = len(rows)
    if n < 3:
        return {}
    cnt = collections.Counter(m for r in rows for m in r)
    out = {}
    for a, b in itertools.combinations(sorted(m for m, k in cnt.items() if k >= 2), 2):
        pa, pb = cnt[a] / n, cnt[b] / n
        pab = sum(1 for r in rows if a in r and b in r) / n
        ind = pa * pb
        hi, lo = min(pa, pb), max(0.0, pa + pb - 1.0)
        if pab >= ind:
            st = (pab - ind) / (hi - ind) if hi - ind > 1e-9 else 0.0
        else:
            st = -(ind - pab) / (ind - lo) if ind - lo > 1e-9 else 0.0
        out[(a, b)] = out[(b, a)] = (st, min(cnt[a], cnt[b]))
    return out


def pair_strength(exclude=None):
    """技の対の相性を上位構築（templates）から**種をまたいで**学ぶ。

    ボディプレス＋てっぺき、設置技＋強制交代のような組み合わせは種を問わない
    （ガブリアス・ブリジュラスの ドラゴンテール→ステルスロック、カバルドンの
    ふきとばし→ステルスロック は同じ構造）。種ごとの周辺分布の違いを消すため、
    種の中で「独立＝0・必ず一緒＝+1・必ず別＝-1」に正規化してから種をまたいで平均する。
    exclude の種は学習から外す（検証でのリーブワンアウト）。
    """
    key = (exclude, PAIR_SEASON)
    if key in _PAIR:
        return _PAIR[key]
    by = collections.defaultdict(list)
    q = "select pokemon,label,move1,move2,move3,move4 from templates"
    for sp, lab, *mv in con.execute(q):
        if sp == exclude:
            continue
        if PAIR_SEASON and not lab.startswith(PAIR_SEASON):
            continue
        by[sp].append(set(m for m in mv if m))
    acc = collections.defaultdict(lambda: [0.0, 0.0])
    for sp, rows in by.items():
        n = len(rows)
        if n < 8:
            continue
        cnt = collections.Counter(m for r in rows for m in r)
        moves = [m for m, k in cnt.items() if k >= 2]
        for a, b in itertools.combinations(sorted(moves), 2):
            pa, pb = cnt[a] / n, cnt[b] / n
            pab = sum(1 for r in rows if a in r and b in r) / n
            ind = pa * pb
            hi, lo = min(pa, pb), max(0.0, pa + pb - 1.0)
            if pab >= ind:
                st = (pab - ind) / (hi - ind) if hi - ind > 1e-9 else 0.0
            else:
                st = -(ind - pab) / (ind - lo) if ind - lo > 1e-9 else 0.0
            w = min(cnt[a], cnt[b])            # 支持の少ない対は軽く
            acc[(a, b)][0] += st * w
            acc[(a, b)][1] += w
    out = {}
    for (a, b), (sw, w) in acc.items():
        if w >= 6:
            out[(a, b)] = out[(b, a)] = sw / w
    _PAIR[key] = out
    return out


def move_role(m):
    """技の役割。技の対が未学習のとき、役割の対の相性に退避するために使う。
    ふきとばし・ほえる・ドラゴンテールはどれも「強制交代」で、設置技との相性は共通。"""
    if m not in MV:
        return None
    v = MV[m]
    if m in FORCE or "交代させる" in v["eff"] or "強制的に交代" in v["eff"]:
        return "強制交代"
    if m in HAZARD:
        return "設置"
    if m in PIVOT:
        return "ピボット"
    if m in BOOST:
        return "積み"
    if m in RECOVERY:
        return "回復"
    if m in PROTECT:
        return "守る"
    if v["cat"] == "status":
        return "変化"
    if v["pri"] > 0:
        return "先制"
    # 吸収技（きゅうけつ・ドレインパンチ等）は体力管理の役割。積み型が回復手段として持つ（グソクムシャの つるぎのまい＋きゅうけつ）
    if "与えたダメージ" in v["eff"] and "回復" in v["eff"]:
        return "吸収"
    return "火力:" + v["cat"]


_ROLE_PAIR = {}


def role_pair_strength(exclude=None):
    """役割の対の相性。pair_strength と同じ正規化を役割単位で行う。"""
    key = (exclude, PAIR_SEASON)
    if key in _ROLE_PAIR:
        return _ROLE_PAIR[key]
    by = collections.defaultdict(list)
    for sp, lab, *mv in con.execute(
            "select pokemon,label,move1,move2,move3,move4 from templates"):
        if sp == exclude or (PAIR_SEASON and not lab.startswith(PAIR_SEASON)):
            continue
        by[sp].append({move_role(m) for m in mv if m and move_role(m)})
    acc = collections.defaultdict(lambda: [0.0, 0.0])
    for sp, rows in by.items():
        n = len(rows)
        if n < 8:
            continue
        cnt = collections.Counter(r for row in rows for r in row)
        for a, b in itertools.combinations(sorted(cnt), 2):
            pa, pb = cnt[a] / n, cnt[b] / n
            pab = sum(1 for row in rows if a in row and b in row) / n
            ind = pa * pb
            hi, lo = min(pa, pb), max(0.0, pa + pb - 1.0)
            if pab >= ind:
                st = (pab - ind) / (hi - ind) if hi - ind > 1e-9 else 0.0
            else:
                st = -(ind - pab) / (ind - lo) if ind - lo > 1e-9 else 0.0
            w = min(cnt[a], cnt[b])
            acc[(a, b)][0] += st * w
            acc[(a, b)][1] += w
    out = {}
    for (a, b), (sw, w) in acc.items():
        if w >= 10:
            out[(a, b)] = out[(b, a)] = sw / w
    _ROLE_PAIR[key] = out
    return out


_POP = None


def tail_moves(sp, known):
    """使用率の上位に載らない技の候補。
    第一の手がかりは「その種が他シーズンで使っていた技」。環境全体の採用頻度だけで選ぶと
    当てずっぽうになり、枠が1つ以上ある種で妥当性が大きく落ちた（実測 -7.4pt）。"""
    global _POP
    learn = [r[0] for r in con.execute(
        "select move_jp from pokemon_learnsets where pokemon_name=?", (sp,))]
    if _POP is None:
        _POP = collections.Counter()
        for m, r in con.execute("select move,usage_rate from pokemon_moves where season=?",
                                (SEASON,)):
            _POP[m] += r
    tot = sum(_POP.values()) or 1.0
    own = collections.Counter()
    for m, r in con.execute(
            "select move,max(usage_rate) from pokemon_moves "
            "where pokemon=? and season<>? group by move", (sp, SEASON)):
        own[m] = max(own[m], r or 0.0)
    cand = [(m, 100.0 * own.get(m, 0.0) / 100.0 + 100.0 * _POP.get(m, 0.0) / tot + 0.05)
            for m in learn if m in MV and m not in known]
    return cand


def tail_own(sp):
    """その種が他シーズン（検証時は学習シーズン）の採用率に載せた技。直接の証拠なので併用実績と並べて使う（割合）"""
    out = {}
    for m, r in con.execute(
            "select move,max(usage_rate) from pokemon_moves where pokemon=? and season<? group by move",
            (sp, SEASON)):
        if r and m in MV:
            out[m] = r / 100.0
    return out


_DATE = {}


def latest(table, sp):
    """そのシーズンで使うクロール日。最新日ではなく**最も完全な日**を選ぶ。

    最新日が壊れていることがある（M-3 の 07-01 は技10本そろう種が64/200・合計中央312%。
    06-25 は199/200・358%）。欠損日を読むと比較対象の技が「圏外」になり、
    検証がすべて無意味になっていた。技テーブルの完全性で日付を決め、全テーブルで揃える。
    """
    if "d" not in _DATE:
        best = None
        for (d,) in con.execute("select distinct crawled_date from pokemon_moves "
                                "where season=?", (SEASON,)):
            rows = list(con.execute(
                "select count(*) from pokemon_moves where season=? and crawled_date=? "
                "group by pokemon", (SEASON, d)))
            full = sum(1 for (n,) in rows if n >= 10)
            key = (full, d)
            if best is None or key > best:
                best = key
        _DATE["d"] = best[1] if best else None
    d = _DATE["d"]
    if table != "pokemon_moves":
        # 他テーブルに同じ日が無ければ、その日以前で最も近い日
        r = con.execute("select max(crawled_date) from %s where season=? and crawled_date<=?"
                        % table, (SEASON, d)).fetchone()[0]
        if r is None:
            r = con.execute("select max(crawled_date) from %s where season=?" % table,
                            (SEASON,)).fetchone()[0]
        return r
    return d


FLOOR = float(os.environ.get("FLOOR", "0.01"))       # この率以下は「無い」ものとして扱う
# 努力値は30通り前後に細かく分散するのが実態で、端数も本物。閾値を振ると 0 が最良だった
# （0.5%で最大誤差2.56pt・1%で3.96pt。0と0.2%は同値）。
FLOOR_EV = float(os.environ.get("FLOOR_EV", "0"))


def _floor(d, renorm=True, th=None):
    """使用率1%以下を切り捨てる。端数を満たすためだけに不自然な型が実体化するのを防ぐ
    （おくびょうエースバーン 0.6% 等）。全部落ちる場合は最大のものだけ残す。"""
    out = {k: v for k, v in d.items() if v > (FLOOR if th is None else th)}
    if not out and d:
        mk = max(d, key=d.get)
        out = {mk: d[mk]}
    if renorm:
        z = sum(out.values()) or 1.0
        out = {k: v / z for k, v in out.items()}
    return out


EV_STEP = int(os.environ.get("EV_STEP", "8"))    # この単位に丸めて集約する


def _ev_key(ev):
    """努力値を集約する。EV_STEP 未満の端数は切り捨て、合計が減った分は
    大きい振り先から順に戻す（総量32×2などの構造を保つため）。1項目の上限32は超えない
    （最大の振り先へ一括で戻していたため H40・S40 のような実在しない配分が13.5%できていた）。"""
    big = [(v // EV_STEP) * EV_STEP for v in ev]
    lost = ((sum(ev) - sum(big)) // EV_STEP) * EV_STEP
    for i in sorted(range(6), key=lambda j: -big[j]):
        if lost <= 0:
            break
        if big[i] == 0:
            continue
        add = min(lost, 32 - big[i])
        big[i] += add
        lost -= add
    return tuple(big)


MARG_SRC = os.environ.get("MARG_SRC", "usage")   # usage | templates（検証用）


_MD = {}


# 型の系統を単位にする事前分布の強さ。過去の上位構築の技構成と k 本一致する候補の事前の重みを ARCH_W**k 倍にする。
# 技の対の相性だけでは「この系統ならこの4本」というまとまりが出ず、実型の相関の約半分しか再現できなかった
# （M-5: 1本判明後の残りの的中の上乗せ 生成+6.0pt・実データ+11.7pt。メタグロスのてっぺき型/パンチ型が混ざる等）
ARCH_W = float(os.environ.get("ARCH_W", "8"))
ARCH_SEASONS = tuple(x for x in os.environ.get("ARCH_SEASONS", "").split(",") if x)
ARCH_MD = os.environ.get("ARCH_MD", "1") == "1"
# 系統ありで合わせ直し前の技の誤差が ARCH_TOL 以上悪化したら系統なしを採る。出力前のレーキングで
# 周辺分布は合わせ直すので既定は無効（99）。辞書が薄い種の偏りは ARCH_FULL_N で抑える
ARCH_TOL = float(os.environ.get("ARCH_TOL", "99"))
ARCH_FULL_N = float(os.environ.get("ARCH_FULL_N", "10"))
_ARCH = {}


def archetypes(sp):
    """過去の上位構築の技構成（系統の辞書）。対象シーズン自身は使わない"""
    if sp in _ARCH:
        return _ARCH[sp]
    out = set()
    for lab, *mv in con.execute(
            "select label,move1,move2,move3,move4 from templates where pokemon=?", (sp,)):
        if ARCH_SEASONS:
            if not lab.startswith(ARCH_SEASONS):
                continue
        elif lab.startswith(SEASON):
            continue
        ms = frozenset(m for m in mv if m)
        if len(ms) == 4:
            out.add(ms)
    if ARCH_MD and SEASON != "M-4":
        for r in md_builds().get(sp, []):
            ms = frozenset(r["moves"])
            if len(ms) == 4:
                out.add(ms)
    _ARCH[sp] = list(out)
    return _ARCH[sp]


def md_builds(path=None):
    """build_pool_*_extra.md（上位構築から抽出した実型）を読む。
    M-4 は m4_top74.json が消えており、この md だけが残っている。
    注意: 書き出し時に「完全に同一の型（努力値まで一致）」を1件にまとめ、M-3と同一の型も
    除いている。人気の型ほど件数が少なく見えるので、頻度には偏りがある。"""
    import re
    path = path or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "build_pool_M-4_extra.md")
    if path in _MD:
        return _MD[path]
    head = re.compile(r"^## ([^#]+?)\s+#")
    line = re.compile(r"^\s*-\s*(?:\*\*[^*]+\*\*\s*)?\[([^/]*)/([^/]*)/([^/]*)/([^\]]*)\]\s*(.+)$")
    out = collections.defaultdict(list)
    cur = None
    for ln in open(path, encoding="utf-8"):
        h = head.match(ln)
        if ln.startswith("## "):
            cur = h.group(1).strip() if h else None
            continue
        m = line.match(ln)
        if not (cur and m):
            continue
        it, na, ab, ev, mv = (x.strip() for x in m.groups())
        e = {k: 0 for k in "HABCDS"}
        for tok in ev.split():
            if tok[:1] in e and tok[1:].isdigit():
                e[tok[:1]] = int(tok[1:])
        moves = [x.strip() for x in mv.split("/") if x.strip()]
        out[cur].append({"item": it, "nature": na, "ability": ab,
                         "ev": tuple(e[k] for k in "HABCDS"), "moves": moves})
    _MD[path] = out
    return out


def _marginals_md(sp):
    """上位構築 md 自身から周辺分布を作る（検証で母集団を揃えるため）。"""
    rows = md_builds().get(sp, [])
    n = len(rows)
    if n == 0:
        return None
    mv, it, na, ab, ev = (collections.Counter() for _ in range(5))
    for r in rows:
        for m in set(r["moves"]):
            if m in MV:
                mv[m] += 1
        it[r["item"]] += 1
        na[r["nature"]] += 1
        ab[r["ability"]] += 1
        ev[_ev_key(r["ev"])] += 1
    out = {"moves": {m: k / n for m, k in mv.items()}}
    for key, cnt in (("items", it), ("natures", na), ("abilities", ab), ("evs", ev)):
        out[key] = {k: v / n for k, v in cnt.items() if k}
    out["tail"] = tail_moves(sp, set(out["moves"]))
    return out


def _marginals_templates(sp):
    """上位構築（templates）自身から周辺分布を作る。検証専用。

    templates は上位プレイヤーの構築で、使用率の母集団とは技ごとに30〜50pt違う
    （ガブリアスのスケイルショット: 使用率23%・上位構築69%）。使用率から作った型の
    共起を上位構築の共起と比べても原理的に一致しないので、検証では母集団を揃える。
    """
    rows = list(con.execute(
        "select move1,move2,move3,move4,item,nature,ability,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s "
        "from templates where pokemon=? and label like ?", (sp, SEASON + "%")))
    n = len(rows)
    if n == 0:
        return None
    mv, it, na, ab, ev = (collections.Counter() for _ in range(5))
    for r in rows:
        for m in set(r[:4]):
            if m and m in MV:
                mv[m] += 1
        it[r[4]] += 1
        na[r[5]] += 1
        ab[r[6]] += 1
        ev[_ev_key(tuple(r[7:13]))] += 1
    out = {"moves": {m: k / n for m, k in mv.items()}}
    for key, cnt in (("items", it), ("natures", na), ("abilities", ab), ("evs", ev)):
        out[key] = {k: v / n for k, v in cnt.items() if k}
    out["tail"] = tail_moves(sp, set(out["moves"]))
    return out


_STONES = {it for (_, it) in MEGA}


def marginals(sp):
    if MARG_SRC == "templates":
        return _marginals_templates(sp)
    if MARG_SRC == "md":
        return _marginals_md(sp)
    d = latest("pokemon_moves", sp)
    mv = {m: r / 100 for m, r in con.execute(
        "select move,usage_rate from pokemon_moves where season=? and crawled_date=? and pokemon=?",
        (SEASON, d, sp)) if m in MV}
    out = {"moves": _floor(mv, renorm=False)}
    for key, tab, col in (("items", "pokemon_items", "item"),
                          ("natures", "pokemon_natures", "nature"),
                          ("abilities", "pokemon_abilities", "ability")):
        dd = latest(tab, sp)
        rows = [(v, r) for v, r in con.execute(
            "select %s,usage_rate from %s where season=? and crawled_date=? and pokemon=?" % (col, tab),
            (SEASON, dd, sp)) if v]
        if key == "items":
            # 他種のメガ石はクロールの誤読（ルガルガン(昼)のリザードナイトY）。持たせても姿が変わらない
            rows = [(v, r) for v, r in rows if v not in _STONES or (sp, v) in MEGA]
        tot = sum(r for _, r in rows)
        out[key] = _floor({v: r / tot for v, r in rows}) if tot > 0 else {}
    dd = latest("pokemon_evs", sp)
    evs = [(tuple(r[:6]), r[6]) for r in con.execute(
        "select ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate from pokemon_evs "
        "where season=? and crawled_date=? and pokemon=?", (SEASON, dd, sp))]
    tot = sum(r for _, r in evs)
    # 努力値は「A32 S32 に余り2をHへ」「HB1」「B2」のような端数違いが大量にあるが、
    # 対戦への影響はほぼ無く、当てる意味も薄い。主要な振り先だけ残して集約する。
    agg = collections.Counter()
    for v, r in evs:
        agg[_ev_key(v)] += r
    out["evs"] = _floor({v: r / tot for v, r in agg.items()}, th=FLOOR_EV) if tot > 0 else {}
    out["tail"] = tail_moves(sp, set(mv))
    return out


def _draw(moves, w, rng):
    pool, ww, s = list(moves), list(w), []
    for _ in range(4):
        if not pool:
            break
        i = rng.choices(range(len(pool)), weights=ww)[0]
        s.append(pool.pop(i))
        ww.pop(i)
    return s


def ev_class(e):
    """努力値の型（素早さ振り・攻撃振り・耐久振り）。持ち物との相性を見る単位"""
    h, at, b, c, d, sp = e
    return (sp >= 24, max(at, c) >= 24, h + b + d >= 32)


_IEL = {}
ITEM_EV_ALPHA = float(os.environ.get("ITEM_EV_ALPHA", "20"))


# 技と「持ち物・性格・努力値の型」の相性（上位構築から学ぶ）。技構成から持ち物や振り方がかなり決まる
# （とんぼがえり＋こだわり、みがわり＋たべのこし、トリックルーム＋S0）のに、割り当ては技と無関係だった。
# M-5 検証（母集団一致）で、技4本→持ち物の上乗せが 生成+6.9pt / 実データ+27.8pt、努力値の型は +1.3 / +21.3
MOVE_LIFT_POW = float(os.environ.get("MOVE_LIFT_POW", "4"))
MOVE_LIFT_ALPHA = float(os.environ.get("MOVE_LIFT_ALPHA", "20"))
PRUNE_MASS = float(os.environ.get("PRUNE_MASS", "0.995"))
MAX_BUILDS = int(os.environ.get("MAX_BUILDS", "4000"))
TAIL_MODE = os.environ.get("TAIL_MODE", "past")    # past: 10位以下は過去シーズンの上位10の技だけ＋上位10を引き上げ / pool: 旧方式（併用実績で補充）
TAIL_PMAX = 0.98
TAIL_SUB = float(os.environ.get("TAIL_SUB", "0.2"))    # 上位10の技と同タイプ・同分類の攻撃技を補充するときの重みの倍率
TAIL_ITERS = int(os.environ.get("TAIL_ITERS", "6"))    # 10位以下の技を上限内に収める埋め直しの回数
PRUNE_W = float(os.environ.get("PRUNE_W", "3e-4"))   # これ未満の重みの型は落として合わせ直す（型数 42.6万→7.4万、周辺分布・的中は不変）
RAKE_ITERS = int(os.environ.get("RAKE_ITERS", "150"))    # 出力前に残った型の重みを周辺分布へ合わせ直す回数   # 種あたりの型の上限（重みの小さい順に切る）
# 注意: 重みは小数6桁で書き出す。4桁では重み0に丸められる小さな型が多く、全体の約12%が消えていた
NAT_LAYER = os.environ.get("NAT_LAYER", "1") == "1"
MOVE_LIFT_KEEP = float(os.environ.get("MOVE_LIFT_KEEP", "0.9"))   # 各型で持ち物・性格を残す質量（密になりすぎないよう）
LIFT_SEASONS = tuple(x for x in os.environ.get("LIFT_SEASONS", "").split(",") if x)
_ML = {}


_TC = {}


def _tail_cooc():
    """10位以下の技を選ぶための併用表。cond[k][m] = 技 k を持つ上位構築のうち m も持つ割合、base[m] = m の採用割合。
    学習に使う上位構築の範囲は技→持ち物の相性と同じ（LIFT_SEASONS。検証時に正解シーズンを含めない）"""
    if _TC:
        return _TC
    rows = []
    for lab, *mv in con.execute("select label,move1,move2,move3,move4 from templates"):
        if LIFT_SEASONS:
            if not lab.startswith(LIFT_SEASONS):
                continue
        elif lab.startswith(SEASON):
            continue
        rows.append({m for m in mv if m})
    if ARCH_MD and SEASON != "M-4":
        for recs in md_builds().values():
            for r in recs:
                rows.append(set(r["moves"]))
    n = len(rows) or 1
    have = collections.Counter(m for r in rows for m in r)
    pair = collections.defaultdict(collections.Counter)
    for r in rows:
        for k in r:
            for m in r:
                if m != k:
                    pair[k][m] += 1
    _TC["base"] = {m: c / n for m, c in have.items()}
    _TC["cond"] = {k: {m: c / have[k] for m, c in ms.items()} for k, ms in pair.items()}
    return _TC


def tail_scores(known, cands):
    """型の残りの技と上位構築で一緒に使われた実績から、10位以下の技の重みを決める。
    環境全体の人気で選ぶと、使われたことのない技（ボーマンダのおいかぜ・かげぶんしん）が入る。
    併用率に lift の平方根を掛け、どの型にも付く技（まもる）の底上げを抑える"""
    tc = _tail_cooc()
    ks = [k for k in known if k in tc["cond"]]
    if not ks:
        return {}
    out = {}
    for m in cands:
        v = sum(tc["cond"][k].get(m, 0.0) for k in ks) / len(ks)
        b = tc["base"].get(m, 0.0)
        if v > 0 and b > 0:
            out[m] = v * math.sqrt(v / b)
    return out


def _move_lift_tables():
    """技 m ごとの lift[kind][m][x]（kind = item / nature / evc）。種をまたいで数え、件数の少ない技は全体へ縮める"""
    if _ML:
        return _ML
    rows = []
    for lab, it, na, *rest in con.execute(
            "select label,item,nature,move1,move2,move3,move4,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s from templates"):
        if LIFT_SEASONS:
            if not lab.startswith(LIFT_SEASONS):
                continue
        elif lab.startswith(SEASON):
            continue
        mv = [m for m in rest[:4] if m]
        rows.append((mv, _lift_item(it), na, ev_class(_ev_key(tuple(rest[4:]))), it))
    if ARCH_MD and SEASON != "M-4":
        for recs in md_builds().values():
            for r in recs:
                ev = r.get("ev")
                e = tuple(ev.get(k, 0) for k in "HABCDS") if isinstance(ev, dict) else tuple(ev or (0,) * 6)
                rows.append((list(r["moves"]), _lift_item(r.get("item")), r.get("nature"), ev_class(_ev_key(e)),
                             r.get("item")))
    _ML["n_item_raw"] = collections.Counter(r[4] for r in rows)
    for kind, idx in (("item", 1), ("nature", 2), ("evc", 3), ("item_raw", 4)):
        tot = collections.Counter(r[idx] for r in rows)
        z = sum(tot.values()) or 1
        base = {x: c / z for x, c in tot.items()}
        by = collections.defaultdict(collections.Counter)
        for r in rows:
            for m in r[0]:
                by[m][r[idx]] += 1
        tab = {}
        for m, cnt in by.items():
            n = sum(cnt.values())
            tab[m] = {x: min(10.0, max(0.1, (cnt[x] + MOVE_LIFT_ALPHA * p) / (n + MOVE_LIFT_ALPHA) / p))
                      for x, p in base.items()}
        _ML[kind] = tab
    return _ML


MEGA_CLASS = "＜メガ石＞"
_MRL = {}


def mega_role_lift():
    """役割ごとの「メガの型が持つ割合 / 全体で持つ割合」（上位構築。学習範囲は技と持ち物の相性と同じ）"""
    if _MRL:
        return _MRL
    n = collections.Counter(); c = collections.Counter()
    for lab, sp, it, *mv in con.execute("select label,pokemon,item,move1,move2,move3,move4 from templates"):
        if not _lift_label_ok(lab):
            continue
        mega = (sp, it) in MEGA
        n[mega] += 1; n["all"] += 1
        for r in {move_role(m) for m in mv if m}:
            c[(mega, r)] += 1; c[("all", r)] += 1
    for (g, r), v in list(c.items()):
        if g is True and c[("all", r)] >= 20:
            _MRL[r] = (v / n[True]) / (c[("all", r)] / n["all"])
    return _MRL




def _lift_item(it):
    """技と持ち物の相性はメガ石をまとめて1つとして学ぶ。石は種ごとで実例が少なく、新しい石（ガブリアスナイトZ）は0件。
    上位構築ではメガの型は後続の補助をほぼしない（設置 0.5% vs 非メガ21.3%・強制交代 0.6% vs 11.2%・積み 44.8% vs 28.9%）"""
    return MEGA_CLASS if it in _STONES else it


PAST_TOP_FRAC = float(os.environ.get("PAST_TOP_FRAC", "1.0"))   # 過去シーズンの技の見積もり上限（今の10位の率に対する比）
STONE_K = float(os.environ.get("STONE_K", "10"))
_SL = {}


def stone_lift(m, stone):
    """技とメガ石の相性 = メガ石全体の相性 × (その石の型が技を持つ率 / メガの型全体が技を持つ率)。
    石の率は実例数に応じてメガ全体の率へ寄せる（STONE_K 件ぶん）。新しい石（ガブリアスナイトZ）はメガ全体の傾向になり、
    同じ種の石の違い（リザードンの ニトロチャージ は X 7/14・Y 7/42）は比のまま残る。上限で頭打ちにしない"""
    if not _SL:
        n = collections.Counter(); c = collections.Counter(); nm = 0; cm = collections.Counter()
        for lab, sp, it, *mv in con.execute("select label,pokemon,item,move1,move2,move3,move4 from templates"):
            if not _lift_label_ok(lab) or (sp, it) not in MEGA:
                continue
            n[it] += 1; nm += 1
            for x in set(mv):
                if x:
                    c[(it, x)] += 1; cm[x] += 1
        _SL["n"], _SL["c"], _SL["nm"], _SL["cm"] = n, c, nm, cm
    lc = _move_lift_tables()["item"].get(m, {}).get(MEGA_CLASS, 1.0)
    pm = (_SL["cm"][m] + 0.5) / (_SL["nm"] + 1.0)
    ps = (_SL["c"][(stone, m)] + STONE_K * pm) / (_SL["n"][stone] + STONE_K)
    return lc * ps / pm


def move_lift(kind, x, moves):
    """技構成と x（持ち物/性格/努力値の型）の相性。4技の lift の対数平均を MOVE_LIFT_POW 乗"""
    if MOVE_LIFT_POW <= 0:
        return 1.0
    if kind == "item" and x in _STONES:
        ls = [math.log(stone_lift(m, x)) for m in moves if m in _move_lift_tables()["item"]]
        return math.exp(MOVE_LIFT_POW * sum(ls) / len(ls)) if ls else 1.0
    if kind == "item":
        x = _lift_item(x)
    tab = _move_lift_tables()[kind]
    ls = [math.log(tab[m].get(x, 1.0)) for m in moves if m in tab]
    if not ls:
        return 1.0
    return math.exp(MOVE_LIFT_POW * sum(ls) / len(ls))


def item_ev_lift(item, e):
    """持ち物と努力値の型の相性（上位構築から学んだ lift）。
    タスキ・スカーフは素早さ＋攻撃振り、オボン・たべのこしは耐久振りに寄る。努力値を性格だけに
    合わせて割り振っていたため、型プールはタスキの耐久振り 9%（上位構築1%）、オボンの
    素早さ＋攻撃振り 17%（同3%）になっていた。件数の少ない持ち物は全体の分布へ縮める。"""
    if not _IEL:
        n = collections.defaultdict(collections.Counter)
        tot = collections.Counter()
        for lab, it, *ev in con.execute(
                "select label,item,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s from templates"):
            if not _lift_label_ok(lab):
                continue
            c = ev_class(_ev_key(tuple(ev)))
            n[it][c] += 1
            tot[c] += 1
        z = sum(tot.values()) or 1
        base = {c: v / z for c, v in tot.items()}
        for it, cnt in n.items():
            m = sum(cnt.values())
            _IEL[it] = {c: min(10.0, max(0.1, (cnt[c] + ITEM_EV_ALPHA * p) / (m + ITEM_EV_ALPHA) / p))
                        for c, p in base.items()}
        _IEL[None] = {}
    return _IEL.get(item, {}).get(ev_class(e), 1.0)


def _lift_label_ok(lab):
    """上位構築から相性を学ぶときに使う行か。検証（LIFT_SEASONS 指定）では学習シーズンだけ、
    本番では生成するシーズン自身を除く（正解を学習に混ぜない）"""
    if LIFT_SEASONS:
        return lab.startswith(LIFT_SEASONS)
    return not lab.startswith(SEASON)


_NEL = {}
NA_EV_POW = float(os.environ.get("NA_EV_POW", "2"))   # M-5 検証で性格×努力値の型の距離 13.6→7.5pt（3以上は頭打ち）


def nature_ev_lift(nature, e):
    """性格と努力値の型の相性（上位構築から学んだ lift）。持ち物との相性と同じ作り。
    素早さを上げる性格なのにSに振らない型が 生成2.95%・上位構築0.61% と多かった
    （性格と努力値を別々に周辺分布へ合わせていたため）。件数の少ない性格は全体の分布へ縮める"""
    if NA_EV_POW <= 0:
        return 1.0
    if not _NEL:
        n = collections.defaultdict(collections.Counter)
        tot = collections.Counter()
        for lab, na, *ev in con.execute(
                "select label,nature,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s from templates"):
            if not _lift_label_ok(lab):
                continue
            c = ev_class(_ev_key(tuple(ev)))
            n[na][c] += 1
            tot[c] += 1
        z = sum(tot.values()) or 1
        base = {c: v / z for c, v in tot.items()}
        for na, cnt in n.items():
            m = sum(cnt.values())
            _NEL[na] = {c: min(10.0, max(0.1, (cnt[c] + ITEM_EV_ALPHA * p) / (m + ITEM_EV_ALPHA) / p))
                        for c, p in base.items()}
        _NEL[None] = {}
    return _NEL.get(nature, {}).get(ev_class(e), 1.0) ** NA_EV_POW


def ev_for(nature, moves, evs, rng):
    """性格が下げた能力への大振りを避け、技が要求する攻撃方面には振ってある配分を選ぶ。"""
    _up, down = NATURE_MODS.get(nature, (None, None))
    idx = {"attack": 1, "defense": 2, "sp_attack": 3, "sp_defense": 4, "speed": 5}.get(down)
    ph, sp = orientation(moves)
    cand = [(v, p) for v, p in evs.items()
            if (idx is None or v[idx] < 16) and (not ph or v[1] > 0) and (not sp or v[3] > 0)]
    if not cand:
        cand = [(v, p) for v, p in evs.items() if idx is None or v[idx] < 16]
    if not cand:
        cand = list(evs.items())
    return rng.choices([v for v, _ in cand], weights=[p for _, p in cand])[0]


def _nnls(A, b, iters=3000):
    """min ||Ax-b||^2, x>=0 の射影勾配法（scipy が無い環境のため自前）。"""
    import numpy as _np
    A = _np.asarray(A, float)
    b = _np.asarray(b, float)
    x = _np.full(A.shape[1], 1.0 / max(A.shape[1], 1))
    L = float((A * A).sum()) or 1.0
    At = A.T
    for _ in range(iters):
        x = _np.maximum(0.0, x - (At @ (A @ x - b)) / L)
    return list(x)


def _resid(A, b, x):
    import numpy as _np
    return float(_np.abs(_np.asarray(A, float) @ _np.asarray(x, float)
                         - _np.asarray(b, float)).max())


SPARSE_TOL = float(os.environ.get("SPARSE_TOL", "0.01"))
EV_COVER = float(os.environ.get("EV_COVER", "1.0"))
# 最終的に残す型の数。主要な型は10個程度、あとは極端にレアというのが実際の姿。
TOPK = int(os.environ.get("TOPK", "0"))   # 0で解き直さない（決定化は全件を使う）


def _nnls_prior(A, b, prior, lam=0.3, iters=3000):
    """min ||Ax-b||^2 + lam*||x-prior||^2, x>=0。

    素の NNLS は実行可能解のうち任意のものを返すので、周辺分布は満たしても
    「どの型が主流か」が実態と逆転する（グソクムシャで使用率15%のつるぎのまい型が
    上位を占めた）。使用率の高い技が揃った型ほど出やすい、という事前分布へ引く。
    """
    import numpy as _np
    A = _np.asarray(A, float); b = _np.asarray(b, float)
    pr = _np.asarray(prior, float)
    pr = pr / (pr.sum() or 1.0)
    x = pr.copy()
    L = float((A * A).sum()) + lam or 1.0
    At = A.T
    for _ in range(iters):
        x = _np.maximum(0.0, x - (At @ (A @ x - b) + lam * (x - pr)) / L)
    return list(x)


LAM = float(os.environ.get("LAM", "0.3"))


def _sparse_nnls(A, b, tol=None, prior=None, lam=None):
    """残差が tol を超えない範囲でできるだけ疎な解を選ぶ。

    素の NNLS は実行可能解のうち**広がった**ものを返す。技構成が210通りあると
    210通りすべてに薄く重みが乗り、実型（ギャラドス26構成）とかけ離れる。
    小さい重みを落として再求解し、残差が悪化しない限り疎化を進める。
    """
    tol = SPARSE_TOL if tol is None else tol
    lam = LAM if lam is None else lam
    x = _nnls(A, b) if prior is None else _nnls_prior(A, b, prior, lam)
    best = list(x)
    idx = list(range(len(x)))
    # 閾値を20%まで上げていたため、支持集合が数十件まで削られ周辺分布が崩れた
    # （ガブリアスが2000件→35件・技誤差5.6pt）。1%までに留める。
    for th in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2):
        z = sum(x) or 1.0
        keep = [i for i in idx if x[i] / z > th]
        if not keep or len(keep) == len(idx):
            continue
        sub = [[row[i] for i in keep] for row in A]
        y = (_nnls(sub, b) if prior is None
             else _nnls_prior(sub, b, [prior[i] for i in keep], lam))
        if _resid(sub, b, y) > tol:
            break
        x = [0.0] * len(best)
        for k, i in enumerate(keep):
            x[i] = y[k]
        best = list(x)
        idx = keep
    return best


_LS = {}


def learnset(sp):
    if sp not in _LS:
        _LS[sp] = {r[0] for r in con.execute("select move_jp from pokemon_learnsets where pokemon_name=?", (sp,))}
    return _LS[sp]


def past_fill(sp, P, cap=None, sides=None, items=None):
    """4枠に足りない分（400%−上位10の合計）の埋め方。
    10位以下に使うのは、その種が過去シーズンに上位10へ入れた技だけ（過去の採用率の比を保ち、最大のものを今の10位の率に合わせる）。
    それ以外の技は根拠が無く、環境全体の人気で選ぶと使われない技が入る（ボーマンダのまもる・おいかぜ）ので使わない。
    足りない分は率の比を保って全体を400%へ伸ばす。過去の技を足して400%を超えるときは過去の技の側だけ縮める"""
    tot = sum(P.values())
    if tot >= 4.0 - 1e-9:
        return P, []
    p10 = min(P.values())
    # 過去の攻撃技は、今の上位10に同じ分類（物理/特殊）の主力技があるときだけ使う。
    # 今は物理しか使われない種に過去の特殊技（ギャラドスのだいもんじ・イダイトウのシャドーボール）を足すと、
    # 上位構築で0件の両刀型が4%できた
    cats = {MV[t]["cat"] for t in P if t in MV and _plain(t)}
    past = {m: r for m, r in tail_own(sp).items() if m not in P and r > 0
            and (MV[m]["cat"] == "status" or MV[m]["cat"] in cats)}
    # 今のシーズンで覚えられない過去の技は足さない（ブリジュラスのミラーコートは M-6 で没収）。
    # 覚える技の表は今の使用率上位の技を欠くことがあるので、判定は過去の技だけに使う
    ls = learnset(sp)
    if ls:
        past = {m: r for m, r in past.items() if m in ls}
    # その種の持ち物のどれとも組めない過去の技は足さない（カイロスはメガ石97%＋スカーフ3%で、ねむる はどちらとも組めない）
    if items:
        past = {m: r for m, r in past.items()
                if sum(p for it, p in items.items() if item_ok([m], it)) >= 0.05}
    # 今の上位10に入らない技の率は 0〜10位の間のどこか。見積もりの上限は10位の半分（範囲の中央）にする。
    # 10位そのもので見積もると、ガブリアスの つるぎのまい（M-6 の上位10外）が約20%になり、ステルスロック・ドラゴンテールと重なった
    kp = min(1.0, PAST_TOP_FRAC * p10 / max(past.values())) if past else 1.0
    add = {m: r * kp for m, r in past.items()}
    # 過去の技は、同じ役割の今の上位の技の残りの枠にしか入れない（サイコショックを足すと
    # ワイドフォース＋サイコキネシスの組が100%を超え、併用が避けられなくなった）
    for m in list(add):
        room = 1.0 - sum(P[t] for t in P if redundant(m, t)) - sum(
            add[t] for t in add if t != m and redundant(m, t))
        add[m] = max(0.0, min(add[m], room))
    add = {m: v for m, v in add.items() if v > 1e-6}
    # 片方の層にしか入れない過去の技は、その層の空き枠（層の大きさ×4 − 今の上位の技の取り分）を超えない。
    # リザードンは X（25%）にしか入れない過去の技（ドラゴンクロー・げきりん・かみなりパンチ・つるぎのまい）で X の枠が埋まり、
    # どちらにも入れる ニトロチャージ・はねやすめ が全部 Y に押し出されていた（上位構築では ニトロチャージ は X 7/14・Y 7/42）
    if sides:
        for k in sides:
            only = [m for m in add if gate(m, k) and not any(gate(m, k2) for k2 in sides if k2 != k and k2 != "mix")]
            if not only or k == "mix":
                continue
            room = 4.0 * sides[k] - sum(p * (1.0 if not any(gate(t, k2) for k2 in sides if k2 != k and k2 != "mix")
                                             else sides[k]) for t, p in P.items() if gate(t, k))
            have = sum(add[m] for m in only)
            if have > 0 and room < have:
                f = max(0.0, room) / have
                for m in only:
                    add[m] *= f
        add = {m: v for m, v in add.items() if v > 1e-6}
    ta = sum(add.values())
    if tot + ta > 4.0:
        k = (4.0 - tot) / ta
        return {**P, **{m: v * k for m, v in add.items()}}, []
    out = {**P, **add}
    # 同じ役割の技の組（併用しない2技）は、元の合計が100%以下なら伸ばした後も100%以下に止める。
    # 比で伸ばすと、ほぼ全員が使う技（グレンアルマのワイドフォース85.6%）が上がり、同じ役割の技
    # （サイコキネシス）を別の型へ逃がせなくなって、元の率なら不要だった併用が起きていた
    par = {m: m for m in out}

    def root(m):
        while par[m] != m:
            m = par[m]
        return m
    for x, y in itertools.combinations(sorted(out), 2):
        if redundant(x, y):
            par[root(x)] = root(y)
    grp = collections.defaultdict(list)
    for m in out:
        grp[root(m)].append(m)
    pairs = [tuple(g) for g in grp.values() if len(g) > 1 and sum(out[m] for m in g) <= 1.0]
    fixed = {}
    for _ in range(20):
        free = {m: v for m, v in out.items() if m not in fixed}
        need = 4.0 - sum(fixed.values())
        f = 1.0
        for _ in range(50):
            cur = sum(min(TAIL_PMAX, (cap or {}).get(m, 1.0), f * v) for m, v in free.items())
            if cur <= 0 or abs(cur - need) < 1e-6:
                break
            f *= need / cur
        new = {**{m: min(TAIL_PMAX, (cap or {}).get(m, 1.0), f * v) for m, v in free.items()}, **fixed}
        over = [g for g in pairs if sum(new[m] for m in g) > 1.0 + 1e-9]
        if not over:
            return new, []
        for g in over:
            gs = sum(out[m] for m in g)
            for m in g:
                fixed[m] = min(fixed.get(m, 1.0), out[m] / gs)
    return new, []


def generate(sp, n, seed=0):
    mg = marginals(sp)
    if not mg:
        return None
    P, items, nats, abils, evs = (mg["moves"], mg["items"], mg["natures"],
                                  mg["abilities"], mg["evs"])
    if not P or not items or not nats:
        return None
    P = dict(P)
    tail = mg["tail"]
    sides = side_weights(nats)
    if TAIL_MODE == "past" and P:
        # 伸ばした後の率は、その技が入れる層の合計を超えない（元の率より上は層の容量まで）。
        # 超えた分は向きの合わない型へあふれる（じしん 66→73% がメガガブリアスZ の特殊型に入った）
        cap = {m: max(p, sum(sides[k] for k in sides if gate(m, k))) for m, p in P.items()}
        P, tail = past_fill(sp, P, cap, sides, items)
    # 持ち物から必ず決まる技（カゴのみ→ねむる）が無ければ、その持ち物の率で足す（10位の率以下なので10位より下にいて矛盾しない）。
    # マルノームは カゴのみ 11.1% なのに ねむる が上位10に無く、カゴのみが0%になっていた。
    # 過去の技の上限（今の10位の率）を下げないよう、過去の技を足した後に入れる（先に入れるとガブリアスの過去の技が1.2%に縮んだ）
    for it, m in ITEM_NEEDS.items():
        if items.get(it, 0) > 0 and m not in P and m in MV and P:
            P[m] = min(items[it], min(P.values()))
    slack = max(0.0, 4.0 - sum(P.values()))
    moves = sorted(P)
    # 層の比率は性格分布だけでは決まらない。メガ石で攻撃方面が変わる種では持ち物の分布が
    # 強い証拠になる（カイリューは非メガ36.1%＝物理型だが、性格からは30.7%しか出ない）。
    lb = collections.Counter()
    for it, p in items.items():
        ok = [k for k in sides if it in (items_for(sp, k, items) or {})]
        if len(ok) == 1:
            lb[ok[0]] += p
    for k in sides:
        sides[k] = max(sides[k], lb[k])
    zs = sum(sides.values()) or 1.0
    sides = {k: v / zs for k, v in sides.items()}
    sk = sorted(sides)
    rng = random.Random(seed)
    choice_mass = sum(p for i, p in items.items() if i in CHOICE)

    # 1) 層ごとの目標「期待本数」を IPF で解く。
    #    列: Σ_k sides[k]·q[k][m] = P[m]   行: Σ_m q[k][m] + tail[k] = 4
    #    実技は1本が上限、10位以下の枠だけは1型に複数入りうる。
    # 規則が使用率と両立するかを種ごとに検査し、両立しない規則はこの種では外す
    _MUST.clear()
    real = [m for m in moves if m != TAIL]
    _MUST.update(forced_pairs(P, real))
    frag = sum(p for i, p in items.items() if i in FRAGILE)
    defn = sum(p for n2, p in nats.items()
               if NATURE_MODS.get(n2, (None, None))[0] in DEF_UP
               or NATURE_MODS.get(n2, (None, None))[0] is None)
    # ランクルス いのちのたま74%・攻撃系性格71%、レパルダス タスキ43%・攻撃系性格26%
    _FRAGILE_OFF[0] = frag + defn > 1.0 + 0.02
    atk = sum(P[m] for m in real if MV.get(m, {}).get("cat", "status") != "status")
    _NOATK_OK[0] = atk < 1.1
    # 開放は全か無かなので、わずかな超過で開くと向きの制約が丸ごと外れる
    # （ガブリアスナイトZ 36% に特殊＋両刀34% で2pt超過→開放→物理型に23.6%付いた）。
    # 使用率が容量を大きく超える＝層の判定がデータと明確に矛盾する場合だけ開く
    # （シビルドナイト83%に容量43%、スターミナイト92%、ボーマンダナイト98%に容量85%）。
    _ITEM_OPEN.clear()
    for it, pv in items.items():
        cap = sum(sides[k] for k in sides if it in items_for(sp, k, items))
        if pv > cap + 0.10:
            _ITEM_OPEN.add(it)
    # 層の容量を使用率が超える技は、層の規則よりデータを優先して全層で引けるようにする
    # （ガラルヤドランのシェルブレードは使用率73%だが物理・両刀層は計31%しかない）。
    open_all = {m for m in moves if m != TAIL and
                P[m] > sum(sides[k] for k in sk if gate(m, k)) + 0.02}
    mcorr = move_corr(sp) if CORR_W > 0 else {}
    mpair = pair_strength(sp if LOSO or OWN_K > 0 else None) if PAIR_W > 0 else {}
    if PAIR_W > 0 and OWN_K > 0 and not LOSO:
        # 自種の証拠と他種の相性を件数で重み付けして混ぜる（他種の相性が無ければ0へ縮める）
        mpair = dict(mpair)
        for key, (st, w) in own_pair_strength(sp).items():
            g = mpair.get(key)
            mpair[key] = (w * st + OWN_K * (g or 0.0)) / (w + OWN_K)
    rpair = role_pair_strength(sp if LOSO else None) if PAIR_W > 0 and ROLE_BACKOFF else {}
    gk = lambda m, k: gate(m, k) or m in open_all
    # 層の持ち物がメガ石中心なら、技をその層へ配る初期値にメガ石と技の相性を掛ける。
    # 持ち物の割り当てで相性を掛けても、特殊の層が実質メガ石だけ（ガブリアスナイトZ）だと、層に配られた
    # ステルスロックがそのままメガの型に残った（上位構築のメガの型は設置0.5%・非メガ21.3%）
    mtab = _move_lift_tables()["item"] if MOVE_LIFT_POW > 0 else {}
    # 層の中でメガの型になる割合: メガ石の使用率を、付けられる層へ層の大きさの比で配ったもの
    mf = {k: 0.0 for k in sk}
    mst = {k: collections.Counter() for k in sk}     # 層の中で各メガ石の型になる割合
    for it, p in items.items():
        if (sp, it) not in MEGA:
            continue
        ks = [k for k in sk if it in (items_for(sp, k, items) or items)]
        zs = sum(sides[k] for k in ks)
        for k in ks:
            if zs > 0 and sides[k] > 0:
                mf[k] += p * (sides[k] / zs) / sides[k]
                mst[k][it] += p * (sides[k] / zs) / sides[k]
    mf = {k: min(1.0, v) for k, v in mf.items()}
    mrole = mega_role_lift() if MOVE_LIFT_POW > 0 else {}
    def _mega_bias(m, k):
        tot = sum(mst[k].values())
        l = (sum(v * stone_lift(m, it) for it, v in mst[k].items()) / tot) if tot > 0 and m in mtab else 1.0
        # 層がほぼメガの型なら、メガと強く反発する役割（設置・強制交代：上位構築でメガの型の0.5%/0.6%）の技はその層に配らない。
        # 技ごとの相性だと件数の少ない技（まきびし 0.3）が漏れるので役割で見る
        # ただしメガでない層に入りきらない技は消さない（ドラミドロはほぼメガで、どくびし 30% が0%になった）
        if mf[k] >= 0.9 and mrole.get(move_role(m), 1.0) <= 0.2 \
                and sum(sides[k2] for k2 in sk if mf[k2] < 0.9 and gk(m, k2)) >= P[m]:
            return 0.0
        return mf[k] * l + (1.0 - mf[k])
    # 性格も同じ扱い: 層の性格と技の相性（上位構築の lift）を層の性格の使用率で平均し、全層の平均との比を掛ける。
    # 性格は層で決まるので、相性を持ち物の段で掛けても層に入った技は動かない（グソクムシャの ゆうかん 13% が
    # とんぼがえりの型ではなく つるぎのまい の型にも一律に付いた）
    ntab = _move_lift_tables()["nature"] if MOVE_LIFT_POW > 0 and NAT_LAYER else {}
    nz = sum(nats.values()) or 1.0
    def _nat_bias(m, k):
        if m not in ntab:
            return 1.0
        lay = {na: p for na, p in nats.items() if nature_side(na) == k}
        zl = sum(lay.values())
        if zl <= 0:
            return 1.0
        la = sum(p * ntab[m].get(na, 1.0) for na, p in lay.items()) / zl
        lo = sum(p * ntab[m].get(na, 1.0) for na, p in nats.items()) / nz
        return la / lo if lo > 0 else 1.0
    q = {k: {m: (P[m] * _mega_bias(m, k) * _nat_bias(m, k) if gk(m, k) else 0.0) for m in moves} for k in sk}
    qt = {k: slack for k in sk}
    for _ in range(600):
        for m in moves:
            got = sum(sides[k] * q[k][m] for k in sk)
            if got > 1e-12:
                f = P[m] / got
                for k in sk:
                    q[k][m] = min(1.0, q[k][m] * f)
        got = sum(sides[k] * qt[k] for k in sk)
        if got > 1e-12 and slack > 1e-12:
            f = slack / got
            for k in sk:
                qt[k] = min(4.0, qt[k] * f)
        for k in sk:
            tot = sum(q[k].values()) + qt[k]
            if tot > 1e-12:
                f = 4.0 / tot
                for m in moves:
                    q[k][m] = min(1.0, q[k][m] * f)
                qt[k] = min(4.0, qt[k] * f)

    if os.environ.get("DEBUG_Q"):
        for m in sorted(moves, key=lambda x: -P[x])[:int(os.environ.get("DEBUG_Q_N", "6"))]:
            agg = sum(sides[k] * q[k][m] for k in sk)
            print("   IPF後 %-14s 目標%5.1f%% 合算%5.1f%% 層別 %s" % (
                m, P[m] * 100, agg * 100,
                " ".join("%s:%.0f" % (k, q[k][m] * 100) for k in sk)), file=sys.stderr)
        for k in sk:
            print("   層 %s 行和 %.2f (技%.2f+尾%.2f)" % (
                k, sum(q[k].values()) + qt[k], sum(q[k].values()), qt[k]), file=sys.stderr)
    # 2) 層ごとに「4技組」を全列挙し、各組の確率を線形計画で解く。
    #    抽出の較正では包含確率が1に近い技に届かず発散した（リザードンで13.4pt）。
    #    候補は最大10技なので、4技以下の部分集合は最大386通り。全部並べて厳密に解ける。
    pool = collections.Counter()
    for k in sk:
        cand = [m for m in moves if gk(m, k) and q[k][m] > 1e-6]
        subs = []
        for r in range(5):
            for c in itertools.combinations(cand, r):
                if 4 - r > 0 and not tail:
                    continue
                if valid(c):
                    subs.append(c)
        if not subs:
            continue
        MW = 1.0
        rows = []
        for m in cand:
            rows.append([MW if m in c else 0.0 for c in subs])
        rows.append([MW * (4 - len(c)) for c in subs])      # 10位以下の枠数
        rows.append([MW] * len(subs))                       # 確率の合計
        tgt = [MW * q[k][m] for m in cand] + [MW * qt[k], MW * 1.0]
        # 技の対の共起を制約として入れる。目標 P(a,b) は
        #   独立値 q[a]*q[b] に、使用率の時系列相関から推定した lift を掛けたもの。
        # 事前分布に入れるだけでは周辺分布の制約に押し負けて効かなかった（10.6→10.3pt）。
        # 技の対の相性（上位構築から種をまたいで学習）。時系列相関と同じ補間で目標を作る。
        if PAIR_W > 0:
            for x, y in itertools.combinations(cand, 2):
                r = mpair.get((x, y))
                # 正の相関を中心に学ぶが、強い負の相関（型を分ける組: ガブリアスの つるぎのまい×ステルスロック −0.74・×ドラゴンテール −0.85）は使う
                if r is not None and PAIR_NEG < r < PAIR_MIN:
                    r = None
                # 技の組も役割の組も負なら強いほうを使う（グソクムシャ: つるぎのまい×とんぼがえり より 積み×ピボット −0.91 が強い）
                if r is not None and r < 0 and rpair:
                    ra, rb = move_role(x), move_role(y)
                    rr = rpair.get((ra, rb)) if ra and rb and ra != rb else None
                    if rr is not None and rr <= ROLE_NEG and rr < r:
                        r = rr
                if r is None and rpair:
                    # 技の対が未学習なら役割の対へ退避（ふきとばし→強制交代×設置）。
                    # 同じ役割どうし（火力×火力など）は情報が薄いので使わない。
                    ra, rb = move_role(x), move_role(y)
                    if ra and rb and ra != rb:
                        r = rpair.get((ra, rb))
                        # 役割の対は範囲が広く、負の相性（火力物理×火力特殊 -0.59 等）を
                        # 全技の対へ掛けると周辺分布が歪んだ（8.3→8.5pt）。強い正の相性だけ使う。
                        if r is not None and ROLE_NEG < r < 0.5:
                            r = None
                if r is None or q[k][x] <= 0 or q[k][y] <= 0:
                    continue
                qa, qb = q[k][x], q[k][y]
                ind = qa * qb
                if r >= 0:
                    t = ind + r * (min(qa, qb) - ind)
                else:
                    t = ind + (-r) * (max(0.0, qa + qb - 1.0) - ind)
                # 強い負の組（型を分ける組）は周辺分布の制約に押し負けやすいので重みを上げる
                pw = PAIR_W * (NEG_W if r <= PAIR_NEG else 1.0)
                rows.append([pw if (x in c and y in c) else 0.0 for c in subs])
                tgt.append(pw * t)
        if CORR_W > 0:
            for x, y in itertools.combinations(cand, 2):
                r = mcorr.get((x, y))
                if r is None or q[k][x] <= 0 or q[k][y] <= 0:
                    continue
                # 相関で「独立」と「完全に一緒／完全に排他」の間を補間する。
                # 全対の平均で較正した lift（最大でも独立の1.5倍程度）だと、
                # 相関0.99のセット技（実測P(b|a)=88〜92%）を再現できなかった。
                qa, qb = q[k][x], q[k][y]
                ind = qa * qb
                if r >= 0:
                    t = ind + r * (min(qa, qb) - ind)
                else:
                    t = ind + (-r) * (max(0.0, qa + qb - 1.0) - ind)
                rows.append([CORR_W if (x in c and y in c) else 0.0 for c in subs])
                tgt.append(CORR_W * t)
        arch = archetypes(sp) if ARCH_W > 0 else []
        # 辞書が薄い種（過去の上位構築が数件）で1件の型に全体を引っぱらせない。10件未満は件数に比例して弱める
        arch_w_eff = 1.0 + (ARCH_W - 1.0) * min(1.0, len(arch) / ARCH_FULL_N) if ARCH_W > 1 else ARCH_W
        pri = []
        for c in subs:
            v = 1.0
            for m in cand:
                pm = min(max(q[k][m], 1e-4), 1 - 1e-4)
                v *= pm if m in c else (1.0 - pm)
            # 使用率が連動する技どうしを同じ型へ寄せる（独立積だけでは共起が出ない）。
            # 相関をそのまま指数へ入れるのではなく、実測した相関→log(lift) の関係
            # （傾き0.6・切片-0.2、673対で較正）で確率的な意味のある量に直す。
            if CORR_W > 0 and len(c) > 1:
                bonus = 0.0
                for x, y in itertools.combinations(c, 2):
                    r = mcorr.get((x, y))
                    if r is not None:
                        bonus += 0.6 * r - 0.2
                v *= math.exp(CORR_W * bonus)
            if ARCH_W > 0 and arch:
                ov = max(len(set(c) & A) for A in arch)
                v *= arch_w_eff ** ov
            pri.append(v)
        x = _sparse_nnls(rows, tgt, prior=pri)
        # こだわり系は変化技と両立しない。変化技を持たない型がこだわりの使用率ぶん
        # 用意されていないと、持ち物の周辺分布が満たせない（サーフゴーで9.6pt ずれた）。
        if choice_mass > 1e-6:
            free = [MW if not (set(c) & (SETUP | PROTECT | RECOVERY)) else 0.0 for c in subs]
            zx = sum(x) or 1.0
            have = sum(f * v for f, v in zip(free, x)) / zx
            if have < choice_mass - 1e-3:
                x = _sparse_nnls(rows + [free], tgt + [choice_mass], prior=pri)
        
        z = sum(x) or 1.0
        for c, w in zip(subs, x):
            if w / z > 1e-4:
                pool[(k, c)] = w / z * sides[k]

    # 3) 10位以下の枠を実際の技で埋める（ここまでで技構成が確定する）
    # 10位以下の技は10位の採用率を超えられない。候補の重みは環境全体の人気を含むので、そのままだと
    # 使ったことのない技に偏る（ボーマンダのまもる9.3%・シャンデラののろい38%。10位は6.4%/8.9%）。
    # 埋めた結果が上限を超えた技の重みを下げて埋め直す
    tail_cap = min((p for m, p in P.items() if m != TAIL), default=1.0) if len(real) >= 10 else 1.0
    # 併用実績のある技を優先し、実績も過去シーズンの採用も無い型だけ従来の重み（環境全体の人気）で埋める
    base_w = dict(tail)
    own_w = tail_own(sp)
    for m in own_w:
        if m not in base_w and m not in P and m in MV:
            base_w[m] = 0.05
    # 上位10に同じタイプ・同じ分類の攻撃技がある技は、その技の代わりに選ばれた少数派
    # （ボーマンダはやけっぱちが10位。ほのおのキバが同じくらい入るのは不自然）
    for m in base_w:
        v = MV[m]
        if v["cat"] != "status" and any(MV[t]["cat"] == v["cat"] and MV[t]["type"] == v["type"]
                                        for t in real if t in MV):
            base_w[m] *= TAIL_SUB
            if m in own_w:
                own_w[m] *= TAIL_SUB
    sub_f = {m: (TAIL_SUB if MV[m]["cat"] != "status" and any(
        MV[t]["cat"] == MV[m]["cat"] and MV[t]["type"] == MV[m]["type"] for t in real if t in MV) else 1.0)
        for m in base_w}
    tw = {m: 1.0 for m in base_w}
    tail_cache = {}

    def fill():
        out = []
        for (side, c), w0 in pool.items():
            reps = 6 if len(c) < 4 else 1
            for _ in range(reps):
                mv = list(c)
                for _slot in range(4 - len(c)):
                    cands = [m for m in tw if gate(m, side) and m not in mv]
                    sc = tail_cache.get(tuple(mv))
                    if sc is None:
                        sc = tail_cache[tuple(mv)] = tail_scores(mv, list(tw))
                    pick = [(m, (sc.get(m, 0.0) * sub_f[m] + own_w.get(m, 0.0)) * tw[m]) for m in cands
                            if m in sc or own_w.get(m, 0.0) > 0]
                    if not pick:
                        pick = [(m, base_w[m] * tw[m]) for m in cands]
                    if not pick:
                        break
                    for _try in range(40):
                        m = rng.choices([z2[0] for z2 in pick],
                                        weights=[z2[1] for z2 in pick])[0]
                        if m not in mv and valid(tuple(mv + [m])):
                            mv.append(m)
                            break
                if len(mv) == 4:
                    out.append([side, tuple(sorted(mv)), w0 / reps])
        return out

    for _it in range(TAIL_ITERS):
        builds = fill()
        zb = sum(b[2] for b in builds) or 1.0
        inc = collections.Counter()
        for b in builds:
            for m in b[1]:
                if m in tw:
                    inc[m] += b[2] / zb
        over = {m: v for m, v in inc.items() if v > tail_cap * 1.02}
        if not over:
            break
        for m, v in over.items():
            tw[m] *= tail_cap / v * 0.9
    if not builds:
        return None
    zb = sum(b[2] for b in builds)
    for b in builds:
        b[2] /= zb                      # 埋められず落ちた分を再配分（取りこぼしで層が歪むため）

    # 4) 持ち物と性格を輸送問題(IPF)で割り当てる。
    #    「制約を満たす候補から周辺分布どおりに引く」だけだと、絞られた分の再配分が
    #    起きず周辺分布が壊れる（ラウドボーンで持ち物44pt ずれた）。
    def transport_dense(compat, wrow, target, iters=200):
        """行和=wrow・列和=target を満たす結合分布（IPF・密）。
        努力値は30通り前後に細かく分散するので、疎な解では周辺分布を満たせない
        （疎にしたら全198種で誤差1pt超・中央10pt になった）。"""
        keys = list(target)
        z = [[1.0 if compat[i][j] else 0.0 for j in range(len(keys))]
             for i in range(len(wrow))]
        for _ in range(iters):
            for i in range(len(wrow)):
                s2 = sum(z[i])
                if s2 > 1e-12:
                    f = wrow[i] / s2
                    for j in range(len(keys)):
                        z[i][j] *= f
            for j, kk in enumerate(keys):
                s2 = sum(z[i][j] for i in range(len(wrow)))
                if s2 > 1e-12:
                    f = target[kk] / s2
                    for i in range(len(wrow)):
                        z[i][j] *= f
        for i in range(len(wrow)):
            s2 = sum(z[i])
            if s2 > 1e-12:
                f = wrow[i] / s2
                for j in range(len(keys)):
                    z[i][j] *= f
        return keys, z

    def transport(compat, wrow, target):
        """行和=wrow・列和=target を満たす**疎な**結合分布を compat の台の上で求める。

        IPF（最大エントロピー解）だと密になり、1つの技構成が10種類の持ち物と
        30種類の努力値に薄く広がって組み合わせが爆発した（ギャラドスで12万件、
        重みの50%を占めるのに1,340件必要）。実際の型は技構成と持ち物・努力値が
        強く結びついているので、非ゼロが行数+列数程度に収まる貪欲解を使う。
        """
        keys = list(target)
        z = [[0.0] * len(keys) for _ in range(len(wrow))]
        rem_r = list(wrow)
        rem_c = [target[k] for k in keys]
        order = sorted(range(len(wrow)), key=lambda i: -rem_r[i])
        for i in order:
            cols = sorted((j for j in range(len(keys)) if compat[i][j]),
                          key=lambda j: -rem_c[j])
            for j in cols:
                if rem_r[i] <= 1e-12:
                    break
                m = min(rem_r[i], rem_c[j])
                if m <= 1e-12:
                    continue
                z[i][j] += m
                rem_r[i] -= m
                rem_c[j] -= m
            if rem_r[i] > 1e-12:          # 列の残量が尽きた分は台の上で按分して行和を守る
                cols = [j for j in range(len(keys)) if compat[i][j]]
                if cols:
                    for j in cols:
                        z[i][j] += rem_r[i] / len(cols)
                rem_r[i] = 0.0
        return keys, z

    def transport_w(weight, wrow, target, keep=None, iters=200):
        """重みつきの結合分布（技との相性を初期値にした IPF）。密になりすぎないよう、
        各行で質量の keep に届くまでの列だけ残して解き直す"""
        keep = MOVE_LIFT_KEEP if keep is None else keep
        keys, z = transport_dense_w(weight, wrow, target, iters)
        sup = []
        for i in range(len(wrow)):
            o = sorted(range(len(keys)), key=lambda j: -z[i][j])
            t = sum(z[i]) or 1.0
            acc = 0.0
            row = [0.0] * len(keys)
            for j in o:
                if z[i][j] <= 0:
                    break
                row[j] = weight[i][j]
                acc += z[i][j]
                if acc / t >= keep:
                    break
            if not any(row):
                row = list(weight[i])
            sup.append(row)
        keys, z = transport_dense_w(sup, wrow, target, iters)
        # 切り詰めで列和（採用率）を満たせなくなった列は、元の台に戻して解き直す
        # （サーフゴー・ボスゴドラで持ち物が 3〜5pt ずれた）
        bad = [j for j, kk in enumerate(keys)
               if abs(sum(z[i][j] for i in range(len(wrow))) - target[kk]) > 0.005]
        if bad:
            for i in range(len(wrow)):
                for j in bad:
                    sup[i][j] = weight[i][j]
            keys, z = transport_dense_w(sup, wrow, target, iters * 3)
        return keys, z

    def transport_dense_w(weight, wrow, target, iters=200):
        keys = list(target)
        z = [[float(weight[i][j]) for j in range(len(keys))] for i in range(len(wrow))]
        for _ in range(iters):
            for i in range(len(wrow)):
                s2 = sum(z[i])
                if s2 > 1e-12:
                    f = wrow[i] / s2
                    z[i] = [v * f for v in z[i]]
            for j, kk in enumerate(keys):
                s2 = sum(z[i][j] for i in range(len(wrow)))
                if s2 > 1e-12:
                    f = target[kk] / s2
                    for i in range(len(wrow)):
                        z[i][j] *= f
        for i in range(len(wrow)):
            s2 = sum(z[i])
            if s2 > 1e-12:
                f = wrow[i] / s2
                z[i] = [v * f for v in z[i]]
        return keys, z

    # データ優先で層を開放した技は、性格の整合判定には使わない。メガ石の向きは全部の技で見る
    # （ガブリアスはじしんが開放され、物理技だけの型にガブリアスナイトZが付いていた）
    # （特殊寄りの性格でシェルブレードを使うのがデータ上の実態）
    core = lambda mv: [m for m in mv if m not in open_all]
    it_keys = list(items)
    it_compat = [[(i in (items_for(sp, b[0], items) or items)) and item_ok(b[1], i)
                  and mega_orient_ok(sp, i, b[1])
                  for i in it_keys] for b in builds]
    for r, b in zip(it_compat, builds):    # 全滅する型は層の制限だけ外す（メガ石の向きは外さない：物理技だけの型にガブリアスナイトZが付いた）
        if not any(r):
            for j, i in enumerate(it_keys):
                r[j] = item_ok(b[1], i) and mega_orient_ok(sp, i, b[1])
        if not any(r):
            for j, i in enumerate(it_keys):
                r[j] = item_ok(b[1], i)
        if not any(r):
            r[it_keys.index(max(items, key=items.get))] = True
    if MOVE_LIFT_POW > 0:
        it_w = [[(move_lift("item", it, b[1]) * rest_item_w(b[1], it) if it_compat[bx][j] else 0.0)
                 for j, it in enumerate(it_keys)]
                for bx, b in enumerate(builds)]
        it_keys, zi = transport_w(it_w, [b[2] for b in builds], items)
    else:
        it_keys, zi = transport(it_compat, [b[2] for b in builds], items)

    na_keys = list(nats)
    # 性格は（型 × 持ち物）の単位で割り当てる。型の単位で「どれかの持ち物と両立すれば可」としていたため、
    # タスキとグラスシードを持つ型で タスキ＋ずぶとい が 26% できていた（クエスパトラ）
    # データ優先で層を開放した技は、性格の整合判定にも使わない
    # （特殊寄りの性格でシェルブレードを使うのがデータ上の実態）
    na_rows = [(bx, j) for bx in range(len(builds)) for j in range(len(it_keys)) if zi[bx][j] > 1e-9]
    na_row_of = {rk: r for r, rk in enumerate(na_rows)}
    na_compat = []
    for bx, j in na_rows:
        b = builds[bx]
        it = it_keys[j]
        r = [(nature_side(i) == b[0] or b[0] == "mix")
             and i in natures_for(core(b[1]), nats)
             and nature_item_ok(it, i, b[1]) for i in na_keys]
        if not any(r):
            r = [i in natures_for(core(b[1]), nats) and nature_item_ok(it, i, b[1]) for i in na_keys]
        if not any(r):
            r = [i in natures_for(core(b[1]), nats) for i in na_keys]
        if not any(r):
            r[na_keys.index(max(nats, key=nats.get))] = True
        na_compat.append(r)
    if MOVE_LIFT_POW > 0:
        na_w = [[(move_lift("nature", na, builds[bx][1]) if na_compat[r][k2] else 0.0)
                 for k2, na in enumerate(na_keys)] for r, (bx, _j) in enumerate(na_rows)]
        na_keys, zn = transport_w(na_w, [zi[bx][j] for bx, j in na_rows], nats)
    else:
        na_keys, zn = transport(na_compat, [zi[bx][j] for bx, j in na_rows], nats)

    # 努力値も同じ扱い。性格ごとに引けるスプレッドが違うので、性格を決めたあとに
    # (性格 × スプレッド) の結合分布を解く。素直に引くと最大26.4pt ずれた。
    ev_keys = list(evs) if evs else [(0, 0, 0, 0, 0, 0)]
    # 性格が下げた能力への大振りだけを避ける。
    # 「上げた能力に必ず振ってある」まで要求するとスターミーが壊れた（技誤差30.9pt）。
    # 実際の型は能力値や性格から一意に決まらない（メガスターミーはA100C130だが
    # 使用はいじっぱり47%・ようき42%の物理）。データが言う以上のことを制約にしない。
    ev_compat = []
    for na in na_keys:
        _u, down = NATURE_MODS.get(na, (None, None))
        idx = {"attack": 1, "defense": 2, "sp_attack": 3,
               "sp_defense": 4, "speed": 5}.get(down)
        row = [idx is None or e[idx] < 16 for e in ev_keys]
        if not any(row):
            row = [True] * len(ev_keys)
        ev_compat.append(row)
    na_mass = [sum(zn[i][j] for i in range(len(na_rows))) for j in range(len(na_keys))]
    _ek, ze = transport_dense(ev_compat, na_mass,
                              {e: evs.get(e, 1.0 / len(ev_keys)) for e in ev_keys})

    # 技の向きと努力値が正反対の配分だけを落とす。
    # 「性格が上げた能力に必ず振る」まで要求するとスターミーが壊れた（技誤差30.9pt）ので、
    # 「主力が全部物理なのにC特化」「全部特殊なのにA特化」だけを弾く。
    def ev_ok(mv, e):
        ph, spx = orientation(core(mv))
        if ph and not spx and e[1] == 0 and e[3] > 0:
            return False
        if spx and not ph and e[3] == 0 and e[1] > 0:
            return False
        # 使わない方の攻撃には振らない: 特殊の攻撃技が1本も無いのにC、物理の攻撃技が1本も無いのにA
        # （上位構築で 3/1284・2/836。ボーマンダの物理型に A32 C8 S24 が出ていた）。積み技で使う能力は除く
        mvs = [m for m in mv if m in MV]
        any_ph = any(MV[m]["cat"] == "physical" and MV[m]["power"] for m in mvs)
        any_sp = any(MV[m]["cat"] == "special" and MV[m]["power"] for m in mvs)
        if e[3] > 0 and not any_sp and not (set(mvs) & SETUP_C):
            return False
        if e[1] > 0 and not any_ph and not (set(mvs) & SETUP_A):
            return False
        # 攻撃を積むのにAに振らずCに振る（特攻を積むのにCに振らずAに振る）型は上位構築で0件
        # （ボーマンダの りゅうのまい＋すてみタックル＋りゅうせいぐん に A0 C32）
        if set(mvs) & SETUP_A and e[1] == 0 and e[3] > 0:
            return False
        if set(mvs) & SETUP_C and e[3] == 0 and e[1] > 0:
            return False
        # 同じ向きの主力技を2本以上持つならその能力に振る（上位構築の両刀: 特殊2本以上でC無振り 0/13・物理2本以上でA無振り 0/9。
        # 1本だけなら補助の打点として無振りもある）
        nph = sum(1 for m in mvs if _plain(m) and MV[m]["cat"] == "physical")
        nsp = sum(1 for m in mvs if _plain(m) and MV[m]["cat"] == "special")
        if nph >= 2 and e[1] == 0 and nsp >= 1:
            return False
        if nsp >= 2 and e[3] == 0 and nph >= 1:
            return False
        return True

    # 持ち物との相性を掛けると努力値の周辺分布がずれるので、努力値ごとの補正を数回かけて戻す
    ev_adj = {e: 1.0 for e in ev_keys}
    _rs = rng.getstate()
    for _pass in range(int(os.environ.get("EV_ADJ_PASSES", "12"))):
      rng.setstate(_rs)
      out = collections.Counter()
      got = collections.Counter()
      got_it = collections.Counter()
      got_na = collections.Counter()
      got_ev = collections.Counter()
      for bi, (side, mv, w) in enumerate(builds):
          if w <= 1e-9:
              continue
          for j, it in enumerate(it_keys):
              wi = zi[bi][j]
              if wi <= 1e-6:
                  continue
              nr = na_row_of.get((bi, j))
              if nr is None:
                  continue
              for k2, na in enumerate(na_keys):
                  wn = zn[nr][k2]
                  if wn <= 1e-6:
                      continue
                  # 特性は**メガ前**を入れる。メガ進化は対戦中に起きるので、決定化の時点で
                  # 持っているのは通常形の特性（ボーマンダは いかく であって スカイスキン ではない）。
                  # メガ後の特性はエンジンがメガ進化処理で差し替える。
                  ab = (rng.choices(list(abils), weights=list(abils.values()))[0]
                        if abils else "")
                  row = ze[k2]
                  if EV_COVER < 1.0:
                      # 1つの型が何通りもの努力値に枝分かれすると件数が爆発する。
                      # 実型では (持ち物,性格,技) あたり努力値は平均1.6通り。
                      o = sorted(range(len(row)), key=lambda j: -row[j])
                      tt = sum(row) or 1.0
                      acc = 0.0
                      keep = set()
                      for j in o:
                          keep.add(j)
                          acc += row[j]
                          if acc / tt >= EV_COVER:
                              break
                      row = [row[j] if j in keep else 0.0 for j in range(len(row))]
                  zr = sum(row) or 1.0
                  # 防御・特防を上げる性格なのに耐久に振らない型は上位構築で0件
                  bulk_nat = NATURE_MODS.get(na, (None, None))[0] in ("defense", "sp_defense")
                  row = [0.0 if bulk_nat and ev_keys[j][0] + ev_keys[j][2] + ev_keys[j][4] < 32 else row[j] for j in range(len(row))]
                  row = [row[j] * ev_adj[ev_keys[j]] * item_ev_lift(it, ev_keys[j])
                         * nature_ev_lift(na, ev_keys[j])
                         * move_lift("evc", ev_class(ev_keys[j]), mv)
                         if ev_ok(mv, ev_keys[j]) else 0.0
                         for j in range(len(ev_keys))]
                  zr = sum(row) or 1.0
                  for j, e in enumerate(ev_keys):
                      we = wn * row[j] / zr
                      if we <= 1e-7:
                          continue
                      out[(side, frozenset(mv), it, na, ab, e)] += we
                      for m in mv:
                          got[m] += we
                      got_it[it] += we
                      got_na[na] += we
                      got_ev[e] += we
      zz = sum(out.values()) or 1.0
      for e in ev_keys:
          tg = (evs or {}).get(e, 0.0)
          g = got_ev[e] / zz
          if g > 1e-9 and tg > 0:
              ev_adj[e] *= tg / g

    # 候補を数十に絞り、その支持集合の上で4つの周辺分布（技・持ち物・性格・努力値）を
    # 同時に満たすよう重みを解き直す。段階的に割り当てると件数が数千に膨らみ、
    # 「主要な型は10個程度、あとは極端にレア」という実際の姿と合わない。
    if TOPK > 0 and len(out) > TOPK:
        per_s = collections.defaultdict(list)
        for k2, w2 in out.items():
            per_s[k2[0]].append((k2, w2))
        cand = []
        for kk in sk:
            arr = sorted(per_s.get(kk, []), key=lambda kv: -kv[1])
            cand += arr[:max(1, round(TOPK * sides[kk]))]
        keys = [k2 for k2, _ in cand]
        rows, tgt = [], []
        for m in moves:
            rows.append([1.0 if m in k2[1] else 0.0 for k2 in keys]); tgt.append(P[m])
        for it, pv in items.items():
            rows.append([1.0 if k2[2] == it else 0.0 for k2 in keys]); tgt.append(pv)
        for na, pv in nats.items():
            rows.append([1.0 if k2[3] == na else 0.0 for k2 in keys]); tgt.append(pv)
        for e, pv in (evs or {}).items():
            rows.append([1.0 if k2[5] == e else 0.0 for k2 in keys]); tgt.append(pv)
        rows.append([1.0] * len(keys)); tgt.append(1.0)
        x = _nnls(rows, tgt)
        zx = sum(x) or 1.0
        out = collections.Counter()
        got = collections.Counter(); got_it = collections.Counter()
        got_na = collections.Counter(); got_ev = collections.Counter()
        for k2, w2 in zip(keys, x):
            w2 /= zx
            if w2 <= 1e-9:
                continue
            out[k2] = w2
            for m in k2[1]:
                got[m] += w2
            got_it[k2[2]] += w2
            got_na[k2[3]] += w2
            got_ev[k2[5]] += w2

    z = sum(out.values()) or 1.0
    err = max(abs(got[m] / z - P[m]) for m in moves)
    if os.environ.get("DEBUG"):
        print("  %s 層=%s" % (sp, {k: round(sides[k], 3) for k in sk}), file=sys.stderr)
        for m in sorted(moves, key=lambda x: -abs(got[x] / z - P[x]))[:6]:
            print("    %-16s 目標%5.1f%% 実現%5.1f%% 差%+6.1fpt  引ける層 %s"
                  % (m, P[m] * 100, got[m] / z * 100, (got[m] / z - P[m]) * 100,
                     ",".join(k for k in sk if gate(m, k))), file=sys.stderr)
    err_it = max(abs(got_it[i] / z - p) for i, p in items.items())
    err_na = max(abs(got_na[na] / z - p) for na, p in nats.items())
    err_ev = max(abs(got_ev[e] / z - p) for e, p in evs.items()) if evs else 0.0
    per = collections.defaultdict(collections.Counter)
    for key, c in out.items():
        per[key[0]][key] = c
    # n は「人が読むための件数」。決定化に使うプールを人向けの件数で切ると、
    # 少数派の層が1件まで潰れて実型の1/4〜1/6の多様性しか残らない（実測で発覚）。
    # n<=0 で切らずに全件返す。datapack へ載せるときは必ずこちら。
    top = []
    for kk in sk:
        if per[kk]:
            top += (per[kk].most_common() if n <= 0
                    else per[kk].most_common(max(1, round(n * sides[kk]))))
    # 重みの小さい型を切り捨てる（上位 PRUNE_MASS の重みを残す）。技との相性で割り当てが密になり型が3倍に増えた
    if PRUNE_MASS < 1.0 and top:
        top.sort(key=lambda kv: -kv[1])
        tot0 = sum(c for _, c in top) or 1.0
        acc, cut = 0.0, len(top)
        for i2, (_k, c) in enumerate(top):
            acc += c
            if acc / tot0 >= PRUNE_MASS:
                cut = i2 + 1
                break
        top = top[:cut]
    # 重みが広く薄い種（バチンウニ）で型が1万件を超えるので件数でも切る
    if MAX_BUILDS > 0 and len(top) > MAX_BUILDS:
        top.sort(key=lambda kv: -kv[1])
        top = top[:MAX_BUILDS]
    # 残った型の重みを採用率（技・持ち物・性格・努力値）へ合わせ直す（レーキング）。
    # 切り捨てで周辺分布が崩れ、マルノームで努力値が17.7pt・性格が14pt ずれていた
    if RAKE_ITERS > 0 and top:
        keys_t = [k for k, _ in top]
        wt = [c for _, c in top]
        mv_t = {m: p for m, p in P.items() if m != TAIL}
        ev_t = dict(evs or {})
        # 強い負の技の組（型を分ける組）の同時率の目標。持ち物の率を満たすための重み合わせで、ここが押し上げられていた
        # （ガブリアス: つるぎのまい も ステルスロック も タスキと相性が良く、つるぎのまい型の31%がステルスロック持ちになった。上位構築14%）
        neg_t = []
        for x, y in (itertools.combinations(sorted(mv_t), 2) if os.environ.get("RAKE_NEG", "1") == "1" else []):
            r = mpair.get((x, y)) if PAIR_W > 0 else None
            if rpair:
                ra, rb = move_role(x), move_role(y)
                rr = rpair.get((ra, rb)) if ra and rb and ra != rb else None
                if rr is not None and rr <= ROLE_NEG and (r is None or rr < r):
                    r = rr
            if r is None or r > PAIR_NEG:
                continue
            # 積むか積まないかは型の意図の一番大きな分かれ目。積み技が絡む組（積み×設置・強制交代・ピボット等）だけ下げる。
            # 他の組まで下げると持ち物の率との釣り合いが崩れた（ガブリアスナイトZ 33→27%）
            if x not in BOOST and y not in BOOST:
                continue
            qa, qb = mv_t[x], mv_t[y]
            lo = max(0.0, qa + qb - 1.0)
            neg_t.append((x, y, max(lo, qa * qb + (-r) * (lo - qa * qb))))
        def _rake(keys_t, wt):
            for _it in range(RAKE_ITERS):
                z0 = sum(wt) or 1.0
                wt = [x / z0 for x in wt]
                # 強い負の技の組を先に下げ、そのあと持ち物・性格・努力値・技の率へ合わせ直す
                for x2, y2, t in neg_t:
                    g = sum(x for k, x in zip(keys_t, wt) if x2 in k[1] and y2 in k[1])
                    if 1e-12 < g < 1 - 1e-12 and t < g:
                        fi, fo = t / g, (1 - t) / (1 - g)
                        wt = [x * (fi if (x2 in k[1] and y2 in k[1]) else fo) for k, x in zip(keys_t, wt)]
                # 技を最後に合わせる（持ち物・性格・努力値より技の採用率を優先。ヒスイバクフーンのふんかが7pt ずれた）
                for idx, tgt_d in ((2, items), (3, nats), (5, ev_t)):
                    g = collections.Counter()
                    for k, x in zip(keys_t, wt):
                        g[k[idx]] += x
                    zt = sum(p for x2, p in tgt_d.items() if g.get(x2, 0) > 0) or 1.0
                    f = {x2: (tgt_d.get(x2, 0.0) / zt) / g[x2] if g[x2] > 1e-12 and tgt_d.get(x2, 0) > 0 else 1.0
                         for x2 in g}
                    wt = [x * f[k[idx]] for k, x in zip(keys_t, wt)]
                if len(mv_t) >= 10:
                    cap = min(mv_t.values())
                    g = collections.Counter()
                    for k, x in zip(keys_t, wt):
                        for m in k[1]:
                            if m not in mv_t:
                                g[m] += x
                    for m, gm in g.items():
                        if cap < gm < 1 - 1e-12:
                            fi, fo = cap / gm, (1 - cap) / (1 - gm)
                            wt = [x * (fi if m in k[1] else fo) for k, x in zip(keys_t, wt)]
                for m, t in mv_t.items():
                    g = sum(x for k, x in zip(keys_t, wt) if m in k[1])
                    if g <= 1e-12 or g >= 1 - 1e-12 or t <= 0 or t >= 1:
                        continue
                    fi, fo = t / g, (1 - t) / (1 - g)
                    wt = [x * (fi if m in k[1] else fo) for k, x in zip(keys_t, wt)]
            return wt
        wt = _rake(keys_t, wt)
        # 重みの小さい型は落として残りで合わせ直す（型が数千件になり、6割が0.01%未満だった）
        if PRUNE_W > 0:
            z0 = sum(wt) or 1.0
            keep = [i for i, x in enumerate(wt) if x / z0 >= PRUNE_W] or list(range(len(wt)))
            keys_t = [keys_t[i] for i in keep]
            wt = _rake(keys_t, [wt[i] for i in keep])
        top = list(zip(keys_t, wt))
    tw = sum(c for _, c in top) or 1.0
    return {
        "species": sp,
        "marginal_error_pt": round(err * 100, 2),
        "item_error_pt": round(err_it * 100, 2),
        "nature_error_pt": round(err_na * 100, 2),
        "ev_error_pt": round(err_ev * 100, 2),
        "sides": {x: round(sides[x], 3) for x in sk},
        # spec は人が読むための表記。種族名に ":" を含むもの（ケンタロス:炎）があるので、
        # 機械で読む側は必ず個別フィールドを使うこと。
        "builds": sorted(({
            "spec": "%s@%s:%s:%s:%s:%s" % (sp, it, na, "|".join(sorted(sv)),
                                           "/".join(str(x) for x in ev), ab),
            "item": it, "nature": na, "ability": ab,
            "moves": sorted(sv), "ev": list(ev),
            "side": side,
            "weight": round(c / tw, 6),
        } for (side, sv, it, na, ab, ev), c in top), key=lambda b: -b["weight"]),
    }


def main():
    if os.environ.get("SPECIES"):
        targets = [x for x in os.environ["SPECIES"].split(",") if x]
    else:
        d = latest("pokemon_usage", None)
        targets = [r[0] for r in con.execute(
            "select pokemon from pokemon_usage where season=? and crawled_date=? order by rank limit ?",
            (SEASON, d, TOPN))]
    res = []
    global ARCH_W
    arch_w0 = ARCH_W
    for i, sp in enumerate(targets):
        r = generate(sp, NBUILD, seed=i)
        # 系統の辞書が今シーズンの採用率と合わない過去の型へ引っぱる種がある（M-6 アローラキュウコン +5pt）。
        # 系統なしでも作り、技の周辺分布の誤差が ARCH_TOL 以上悪化していれば系統なしを採る
        if arch_w0 > 0 and r:
            ARCH_W = 0.0
            r0 = generate(sp, NBUILD, seed=i)
            ARCH_W = arch_w0
            if r0 and r["marginal_error_pt"] > r0["marginal_error_pt"] + ARCH_TOL:
                r = r0
                r["arch"] = False
            else:
                r["arch"] = True
        if r:
            res.append(r)
            print(("%-16s 型%2d件  技 %5.2f  持ち物 %5.2f  性格 %5.2f  努力値 %5.2f (pt)"
                   % (sp, len(r["builds"]), r["marginal_error_pt"],
                      r["item_error_pt"], r["nature_error_pt"], r["ev_error_pt"]))
                  + ("" if r.get("arch", True) else "  系統なし"),
                  file=sys.stderr, flush=True)
    if OUT:
        with open(OUT, "w") as f:
            json.dump(res, f, ensure_ascii=False, indent=1)
        print("→ %s (%d種)" % (OUT, len(res)), file=sys.stderr)
    else:
        print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
