"""
持ち物効果の定義
"""
import math
import random
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .pokemon import BattlePokemon
    from .data import MoveData

# ── ダメージ計算内の補正 ────────────────────────────────────────────────────

# タイプ強化アイテム: {item_name: (type, multiplier)}
TYPE_BOOST_ITEMS: dict[str, tuple[str, float]] = {
    "もくたん":         ("ほのお",    1.2),
    "とけないこおり":   ("こおり",    1.2),
    "しんぴのしずく":   ("みず",      1.2),
    "じしゃく":         ("でんき",    1.2),
    "くろいメガネ":     ("あく",      1.2),
    "ようせいのハネ":   ("フェアリー",1.2),
    "どくバリ":         ("どく",      1.2),
    "やわらかいすな":   ("じめん",    1.2),
    "するどいくちばし": ("ひこう",    1.2),
    "シルクのスカーフ": ("ノーマル",  1.2),
    "りゅうのキバ":     ("ドラゴン",  1.2),
    "くろおび":         ("かくとう",  1.2),
    "まがったスプーン": ("エスパー",  1.2),
    "のろいのおふだ":   ("ゴースト",  1.2),
    "メタルコート":     ("はがね",    1.2),
    "かたいいし":       ("いわ",      1.2),
    "ぎんのこな":       ("むし",      1.2),
    "きせきのタネ":     ("くさ",      1.2),
    "ピントレンズ":     None,  # 急所ランク+1（別処理）
    "するどいツメ":     None,  # 急所ランク+1
    "せんせいのツメ":   None,  # 先制確率
}

# でんきだま: ピカチュウ専用でんき技×2
PIKACHU_BOOST_ITEM = "でんきだま"


def get_type_boost(item: Optional[str], move_type: str, attacker_name: str) -> float:
    if item is None:
        return 1.0
    if item == PIKACHU_BOOST_ITEM and move_type == "でんき" and "ピカチュウ" in attacker_name:
        return 2.0
    entry = TYPE_BOOST_ITEMS.get(item)
    if entry is not None and len(entry) == 2 and entry[0] == move_type:
        return entry[1]
    return 1.0


def get_crit_stage_bonus(item: Optional[str]) -> int:
    """急所ランク加算"""
    if item in ("ピントレンズ", "するどいツメ"):
        return 1
    if item == "ラッキーパンチ":
        return 2
    return 0


# ── スカーフ速度補正 ────────────────────────────────────────────────────────

def get_speed_item_multiplier(item: Optional[str]) -> float:
    if item == "こだわりスカーフ":
        return 1.5
    if item == "くろいてっきゅう":
        return 0.5
    return 1.0


# ── こだわり縛り（スカーフ・ハチマキ・メガネ） ──────────────────────────────

CHOICE_ITEMS = {"こだわりスカーフ", "こだわりハチマキ", "こだわりメガネ"}


def is_choice_item(item: Optional[str]) -> bool:
    return item in CHOICE_ITEMS


# ── がんじょう（HP満タン時耐え） ────────────────────────────────────────────

def apply_sturdy(poke: "BattlePokemon", damage: int, ability: str) -> int:
    """がんじょう / きあいのタスキ と同等の「1耐え」処理。返り値は実ダメ量"""
    if ability == "がんじょう" and poke.hp == poke.max_hp and damage >= poke.hp:
        return poke.hp - 1
    return damage


# ── 回復きのみ ──────────────────────────────────────────────────────────────

def apply_hp_berry(poke: "BattlePokemon", logs: list) -> None:
    """HP回復きのみをターン終了時に適用（オボンは battle.py で処理済み）"""
    if poke.item == "たべのこし":
        return  # battle.pyで処理

    # きのみ系 HP1/3以下で発動
    QUARTER_BERRIES = {
        "カムラのみ": "speed",
        "サルのみ":  "sp_attack", "リュガのみ": "defense",
        "タラプのみ": "sp_defense",
    }
    # くいしんぼう: HP1/2以下できのみを食べる
    _thr = poke.max_hp // (2 if poke.ability == "くいしんぼう" else 4)
    if poke.item in QUARTER_BERRIES and poke.hp <= _thr:
        stat = QUARTER_BERRIES[poke.item]
        # じゅくせい: きのみ効果2倍
        _amt = 2 if poke.ability == "じゅくせい" else 1
        setattr(poke, f"stage_{stat}", min(6, getattr(poke, f"stage_{stat}", 0) + _amt))
        logs.append(f"{poke.name} の {poke.item} が発動！ {stat}が上がった！")
        poke._last_berry = poke.item  # type: ignore  # しゅうかく/はんすう用
        if poke.ability == "はんすう" and not getattr(poke, "_ruminate_berry", None):
            poke._ruminate_berry = poke.item  # type: ignore
            poke._ruminate_count = 1  # type: ignore  # 次ターン終わりに再度食べる
        poke.item = None
        # ほおぶくろ: きのみを食べると最大HP1/3回復
        if poke.ability == "ほおぶくろ":
            _h = max(1, poke.max_hp // 3)
            poke.hp = min(poke.max_hp, poke.hp + _h)
            logs.append(f"{poke.name} の ほおぶくろ！ HPが {_h} 回復した！")


# ── ラムのみ / カゴのみ（状態異常治癒） ────────────────────────────────────

def try_cure_berry(poke: "BattlePokemon", logs: list) -> None:
    """状態異常治癒きのみを状態付与直後またはターン終了時に適用"""
    if poke.item == "ラムのみ" and (poke.status is not None or poke.confused):
        poke.status = None
        poke.bad_poison_count = 0
        poke.sleep_count = 0
        poke.confused = False
        poke.item = None
        logs.append(f"{poke.name} の ラムのみ！ 状態異常が治った")
    elif poke.item == "カゴのみ" and poke.status == "sleep":
        poke.status = None
        poke.sleep_count = 0
        poke.item = None
        logs.append(f"{poke.name} の カゴのみ！ 目を覚ました")
    elif poke.item == "モモンのみ" and poke.status in ("poison", "badpoison"):
        poke.status = None
        poke.bad_poison_count = 0
        poke.item = None
        logs.append(f"{poke.name} の モモンのみ！ どくが治った")
    elif poke.item == "チーゴのみ" and poke.status == "burn":
        poke.status = None
        poke.item = None
        logs.append(f"{poke.name} の チーゴのみ！ やけどが治った")
    elif poke.item == "クラボのみ" and poke.status == "paralysis":
        poke.status = None
        poke.item = None
        logs.append(f"{poke.name} の クラボのみ！ まひが治った")
    elif poke.item == "キーのみ" and poke.status == "freeze":
        poke.status = None
        poke.item = None
        logs.append(f"{poke.name} の キーのみ！ こおりが治った")
    elif poke.item == "ナナシのみ" and poke.confused:
        poke.confused = False
        poke.item = None
        logs.append(f"{poke.name} の ナナシのみ！ こんらんが治った")


# ── しろいハーブ（能力低下を一度リセット） ──────────────────────────────────

def try_white_herb(poke: "BattlePokemon", logs: list) -> None:
    if poke.item != "しろいハーブ":
        return
    stats = ["stage_attack","stage_defense","stage_sp_attack",
             "stage_sp_defense","stage_speed"]
    if any(getattr(poke, s, 0) < 0 for s in stats):
        for s in stats:
            if getattr(poke, s, 0) < 0:
                setattr(poke, s, 0)
        poke.item = None
        logs.append(f"{poke.name} の しろいハーブ！ 能力低下がリセットされた")


# ── メンタルハーブ（メロメロ・ちょうはつ等を一度だけ回復） ──────────────────

def try_mental_herb(poke: "BattlePokemon", logs: list) -> None:
    if poke.item != "メンタルハーブ":
        return
    afflicted = (poke.infatuation or poke.taunt_count > 0 or poke.encore_count > 0
                 or poke.heal_block_count > 0 or poke.disabled_turns > 0)
    if not afflicted:
        return
    poke.infatuation = False
    poke.taunt_count = 0
    poke.encore_count = 0
    poke.locked_move = None
    poke.heal_block_count = 0
    poke.disabled_move = None
    poke.disabled_turns = 0
    poke.item = None
    logs.append(f"{poke.name} の メンタルハーブ！ 行動制限が解除された")


# ── ヒメリのみ（PPが0になった技のPPを10回復） ──────────────────────────────

def try_leppa_berry(poke: "BattlePokemon", logs: list) -> None:
    if poke.item != "ヒメリのみ":
        return
    for i, mv in enumerate(poke.moves):
        if mv is not None and i < len(poke.pp) and poke.pp[i] == 0:
            poke.pp[i] = min(mv.pp, poke.pp[i] + 10)
            poke.item = None
            logs.append(f"{poke.name} の ヒメリのみ！ {mv.name_jp} のPPが回復した")
            return


# ── せんせいのツメ（20%先制） ────────────────────────────────────────────────

def has_quick_claw_trigger(item: Optional[str]) -> bool:
    if item == "せんせいのツメ":
        return random.random() < 0.20
    return False


# ── ひかりのこな（相手の命中率-10%） ──────────────────────────────────────────

def get_accuracy_evasion_item(item: Optional[str]) -> float:
    """命中率補正（攻撃側のアイテム影響）"""
    if item == "こうかくレンズ":
        return 1.1
    return 1.0


def get_evasion_item_mult(item: Optional[str]) -> float:
    """回避率補正（防御側のアイテム）"""
    if item == "ひかりのこな":
        return 0.90
    if item == "するどいツメ":
        return 1.0  # 急所ランクは別処理
    return 1.0


# ── カゴのみ (ねむり中に自動使用) ──────────────────────────────────────────

def check_sleep_berry(poke: "BattlePokemon", logs: list) -> None:
    if poke.item == "カゴのみ" and poke.status == "sleep":
        poke.status = None
        poke.sleep_count = 0
        poke.item = None
        logs.append(f"{poke.name} の カゴのみ で目を覚ました！")


# ── かるわざ（アイテムを消費した後 Speed×2） ──────────────────────────────

def on_item_consumed(poke: "BattlePokemon", logs: list) -> None:
    """アイテムが消費されたらかるわざを発動"""
    if poke.ability == "かるわざ" and poke.item is None:
        poke.stage_speed = min(6, poke.stage_speed + 2)
        logs.append(f"{poke.name} の かるわざ！ 素早さが大幅に上がった！")
