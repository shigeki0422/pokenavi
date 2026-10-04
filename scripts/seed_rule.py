"""シード（サイコ/グラス/エレキ/ミストシード）は、同じパーティにそのフィールドを張る個体がいるときだけ採用する規則。
張る個体＝特性（〜メイカー・こぼれダネ。メガ石を持つならメガ後の特性も）か、該当のフィールド技を持つ個体。
パーティを作る全経路（gen_party_pool・_coevo_groups・_product3_complete）と週次チェック（pool_checks）で共有する。
spec は「種@持ち物:性格:技|技:努力値:特性」。"""
import os
import sqlite3

SEED_TERRAIN = {"サイコシード": "psychic", "グラスシード": "grassy", "エレキシード": "electric", "ミストシード": "misty"}
# エンジン（abilities.entry_ability・battle のこぼれダネ）がフィールドを張る特性だけ
ABILITY_TERRAIN = {"サイコメイカー": "psychic", "グラスメイカー": "grassy", "エレキメイカー": "electric", "こぼれダネ": "grassy"}
MOVE_TERRAIN = {"サイコフィールド": "psychic", "グラスフィールド": "grassy", "エレキフィールド": "electric", "ミストフィールド": "misty"}
DBPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")
_MEGA_AB = {}


def _mega_abilities():
    if not _MEGA_AB:
        con = sqlite3.connect(DBPATH)
        _MEGA_AB.update({st: ab for st, ab in con.execute("select mega_stone, ability from pokemon_mega_stats") if ab})
        _MEGA_AB.setdefault("", "")
        con.close()
    return _MEGA_AB


def parts(spec):
    """(持ち物, 技のリスト, 特性)"""
    body = spec.split("@", 1)[1].split(":")
    item = body[0]
    moves = body[2].split("|") if len(body) > 2 and body[2] else []
    ability = body[4] if len(body) > 4 else ""
    return item, moves, ability


def seed_terrain(spec):
    return SEED_TERRAIN.get(parts(spec)[0])


def is_seed(spec):
    return seed_terrain(spec) is not None


def terrains_set(spec):
    item, moves, ability = parts(spec)
    out = {MOVE_TERRAIN[m] for m in moves if m in MOVE_TERRAIN}
    for ab in (ability, _mega_abilities().get(item)):
        if ab in ABILITY_TERRAIN:
            out.add(ABILITY_TERRAIN[ab])
    return out


def violations(specs, exempt=()):
    """設置役がいないシードの枠の添字（exempt の spec は見ない＝ユーザーが明示した型）"""
    have = set()
    for s in specs:
        have |= terrains_set(s)
    return [i for i, s in enumerate(specs)
            if s not in exempt and seed_terrain(s) is not None and seed_terrain(s) not in have]


def ok(specs, exempt=()):
    return not violations(specs, exempt)


def fix(specs, alts, rng, keep=()):
    """設置役のいないシードの枠を、alts(i) が返す同じ系統の候補 [(spec, 重み)] のうち
    持ち物が他の枠と重ならず規則を満たす型に替える。keep の spec は替えない。替えられなければ None"""
    out = list(specs)
    for _ in range(len(out)):
        bad = [i for i in violations(out) if out[i] not in keep]
        if not bad:
            break
        i = bad[0]
        used = {parts(s)[0] for j, s in enumerate(out) if j != i}
        cand = []
        for s, w in alts(i):
            if parts(s)[0] in used or w <= 0:
                continue
            trial = out[:i] + [s] + out[i + 1:]
            vt = set(violations(trial))
            if i not in vt and vt <= set(bad):
                cand.append((s, w))
        if not cand:
            return None
        out[i] = rng.choices([s for s, _ in cand], weights=[w for _, w in cand])[0]
    return out if not [i for i in violations(out) if out[i] not in keep] else None
