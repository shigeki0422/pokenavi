"""正準状態シリアライズ（rust_engine/engine/src/statec.rs と 1:1）。

R2 コーパス（cases/turn_*.jsonl）の期待値を採り直すために使う。元の state_codec.py は
消失しており、これは statec.rs からの逆移植。フィールドの順序・名前・型は statec.rs と
完全に一致させること（1つでもずれると gate_r2 が全件赤くなる）。

Python 側の属性名は battle.py が動的に付けるものが多く、Rust では underscore 無しの名前に
なっている（例: _disguise_broken → disguise_broken）。_get はその差を吸収する。
"""
from typing import List, Optional, Tuple

STAGE_NAMES = ["stage_attack", "stage_defense", "stage_sp_attack",
               "stage_sp_defense", "stage_speed", "stage_accuracy", "stage_evasion"]
EV_KEYS = ["H", "A", "B", "C", "D", "S"]


def _get(o, name, default=None):
    """name → _name の順に引く（battle.py は動的属性を _ 付きで持つ）。"""
    if hasattr(o, name):
        return getattr(o, name)
    return getattr(o, "_" + name, default)


class Enc:
    def __init__(self, with_names: bool = False):
        self.vals: List = []
        self.names: Optional[List[str]] = [] if with_names else None
        self.pfx = ""

    def a(self, n, v):
        if self.names is not None:
            self.names.append(self.pfx + n)
        self.vals.append(v)

    def i(self, n, v):
        self.a(n, int(v))

    def b(self, n, v):
        self.a(n, bool(v))

    def f(self, n, v):
        self.a(n, float(v))

    def sym(self, n, v):
        self.a(n, None if not v else str(v))

    def ty(self, n, v):
        self.a(n, None if not v else str(v))


def poke_fields(e: Enc, p, pfx: str):
    e.pfx = pfx
    e.sym("name", p.name)
    e.i("dex", _get(p, "dex", 0) or 0)
    e.ty("type1", p.type1)
    e.ty("type2", p.type2)
    e.ty("base_type1", _get(p, "base_type1"))
    e.ty("base_type2", _get(p, "base_type2"))
    e.i("max_hp", p.max_hp)
    e.i("hp", p.hp)
    e.i("attack", p.attack)
    e.i("defense", p.defense)
    e.i("sp_attack", p.sp_attack)
    e.i("sp_defense", p.sp_defense)
    e.i("speed", p.speed)
    e.sym("item", p.item)
    e.sym("ability", p.ability)
    e.sym("nature", _get(p, "nature"))
    evs = _get(p, "evs", {}) or {}
    for k in EV_KEYS:
        e.i(f"ev_{k}", evs.get(k, 0) if isinstance(evs, dict) else 0)
    e.f("weight_kg", _get(p, "weight_kg", 0.0) or 0.0)
    mv = [m for m in (p.moves or [])]
    pp = _get(p, "pp", []) or []
    for i in range(4):
        m = mv[i] if i < len(mv) else None
        e.sym(f"move{i}", m.name_jp if m is not None else None)
        e.a(f"pp{i}", int(pp[i]) if i < len(pp) else None)
    e.i("n_moves", len(mv))
    for nm in STAGE_NAMES:
        e.i(nm, _get(p, nm, 0) or 0)
    e.sym("status", p.status)
    e.i("bad_poison_count", _get(p, "bad_poison_count", 0) or 0)
    e.i("sleep_count", _get(p, "sleep_count", 0) or 0)
    e.b("confused", _get(p, "confused", False))
    e.b("flinched", _get(p, "flinched", False))
    e.b("is_alive", p.is_alive)
    e.b("mega_evolved", p.mega_evolved)
    e.b("has_mega_data", _get(p, "mega_data") is not None)
    e.b("hero_forme", _get(p, "hero_forme", False))
    e.b("protecting", _get(p, "protecting", False))
    e.i("protect_consecutive", _get(p, "protect_consecutive", 0) or 0)
    e.b("enduring", _get(p, "enduring", False))
    e.b("ate_berry", _get(p, "ate_berry", False))
    um = _get(p, "used_moves", None) or []
    e.a("used_moves", "|".join(sorted(str(x) for x in um)))
    e.b("grounded", _get(p, "grounded", False))
    e.i("syrup_count", _get(p, "syrup_count", 0) or 0)
    e.i("heal_block_count", _get(p, "heal_block_count", 0) or 0)
    e.b("deka_last", _get(p, "deka_last", False))
    e.sym("locked_move", _get(p, "locked_move"))
    e.sym("choice_locked_move", _get(p, "choice_locked_move"))
    e.sym("disabled_move", _get(p, "disabled_move"))
    e.i("disabled_turns", _get(p, "disabled_turns", 0) or 0)
    e.i("lock_count", _get(p, "lock_count", 0) or 0)
    e.b("recharge", _get(p, "recharge", False))
    e.sym("charging_move", _get(p, "charging_move"))
    e.b("seeded", _get(p, "seeded", False))
    e.i("yawn_count", _get(p, "yawn_count", 0) or 0)
    e.i("encore_count", _get(p, "encore_count", 0) or 0)
    e.i("taunt_count", _get(p, "taunt_count", 0) or 0)
    e.i("bound_count", _get(p, "bound_count", 0) or 0)
    e.i("throat_chop_count", _get(p, "throat_chop_count", 0) or 0)
    e.i("stockpile_count", _get(p, "stockpile_count", 0) or 0)
    e.b("infatuation", _get(p, "infatuation", False))
    e.b("torment", _get(p, "torment", False))
    e.b("trapped", _get(p, "trapped", False))
    e.i("times_hit", _get(p, "times_hit", 0) or 0)
    e.b("ability_suppressed", _get(p, "ability_suppressed", False))
    e.b("rooted", _get(p, "rooted", False))
    e.b("aqua_ring", _get(p, "aqua_ring", False))
    e.b("magnet_rise", _get(p, "magnet_rise", False))
    e.b("lock_on", _get(p, "lock_on", False))
    e.b("move_failed_last", _get(p, "move_failed_last", False))
    e.b("minimized", _get(p, "minimized", False))
    lum = _get(p, "last_used_move")
    e.sym("last_used_move", getattr(lum, "name_jp", lum))
    e.i("turns_out", _get(p, "turns_out", 0) or 0)
    e.i("fainted_allies", _get(p, "fainted_allies", 0) or 0)
    e.i("perish_count", _get(p, "perish_count", 0) or 0)
    e.b("destiny_bond", _get(p, "destiny_bond", False))
    e.b("cursed", _get(p, "cursed", False))
    e.b("charged", _get(p, "charged", False))
    e.i("crit_stage", _get(p, "crit_stage", 0) or 0)
    e.b("acts_second", _get(p, "acts_second", False))
    e.b("barrier_done", _get(p, "barrier_done", False))
    bs = _get(p, "baton_stages")
    e.b("has_baton", bs is not None)
    for i, nm in enumerate(STAGE_NAMES):
        e.i(f"baton_{nm}", (bs[i] if bs is not None else 0))
    e.b("beak_primed", _get(p, "beak_primed", False))
    e.b("destiny_bond_last_turn", _get(p, "destiny_bond_last_turn", False))
    e.b("disguise_broken", _get(p, "disguise_broken", False))
    e.b("electrified", _get(p, "electrified", False))
    e.b("electromorphosis_charged", _get(p, "electromorphosis_charged", False))
    e.b("flash_fire_active", _get(p, "flash_fire_active", False))
    e.b("force_switch", _get(p, "force_switch", False))
    e.b("gyaku_triggered", _get(p, "gyaku_triggered", False))
    e.b("hangry", _get(p, "hangry", False))
    e.b("honey_used", _get(p, "honey_used", False))
    e.sym("illusion_name", _get(p, "illusion_name"))
    e.b("in_blade_forme", _get(p, "in_blade_forme", False))
    e.b("info_done", _get(p, "info_done", False))
    e.sym("last_berry", _get(p, "last_berry"))
    e.sym("last_consumed_item", _get(p, "last_consumed_item"))
    e.sym("last_flung_item", _get(p, "last_flung_item"))
    e.sym("last_item", _get(p, "last_item"))
    lmo = _get(p, "last_move_obj")
    e.sym("last_move_obj", getattr(lmo, "name_jp", None) if lmo is not None else None)
    e.i("last_physical_dmg_received", _get(p, "last_physical_dmg_received", 0) or 0)
    e.i("last_special_dmg_received", _get(p, "last_special_dmg_received", 0) or 0)
    e.i("levitate_turns", _get(p, "levitate_turns", 0) or 0)
    e.b("move_failed_this_turn", _get(p, "move_failed_this_turn", False))
    e.i("multi_hit_index", _get(p, "multi_hit_index", 0) or 0)
    e.b("pierce_quarter", _get(p, "pierce_quarter", False))
    e.b("pivot_out", _get(p, "pivot_out", False))
    e.b("protean_used", _get(p, "protean_used", False))
    pm = _get(p, "protect_move")
    e.sym("protect_move", getattr(pm, "name_jp", pm))
    rt = _get(p, "roost_types")
    if rt is None:
        e.a("roost_t1", None); e.a("roost_t2", None)
    else:
        e.ty("roost_t1", rt[0]); e.ty("roost_t2", rt[1] if len(rt) > 1 else None)
    e.b("has_roost", rt is not None)
    e.sym("ruminate_berry", _get(p, "ruminate_berry"))
    e.i("ruminate_count", _get(p, "ruminate_count", 0) or 0)
    e.b("salted", _get(p, "salted", False))
    e.b("sealed", _get(p, "sealed", False))
    e.i("shield_atk", _get(p, "shield_atk", 0) or 0)
    e.i("shield_def", _get(p, "shield_def", 0) or 0)
    e.i("shield_spatk", _get(p, "shield_spatk", 0) or 0)
    e.i("shield_spdef", _get(p, "shield_spdef", 0) or 0)
    e.i("substitute_hp", _get(p, "substitute_hp", 0) or 0)
    e.b("switched_this_turn", _get(p, "switched_this_turn", False))
    e.b("took_damage_this_turn", _get(p, "took_damage_this_turn", False))
    e.b("transformed", _get(p, "transformed", False))
    tb = _get(p, "transform_backup")
    e.b("has_transform_backup", tb is not None)
    def tbg(attr, d=0):
        # battle.py:2607 の _transform_backup は dict（Rust 側は構造体）。
        # getattr で引くと常に既定値になり tb_* が全部0になる。
        if tb is None:
            return d
        if isinstance(tb, dict):
            v = tb.get(attr, d)
            return d if v is None else v
        return getattr(tb, attr, d)
    e.i("tb_attack", tbg("attack"))
    e.i("tb_defense", tbg("defense"))
    e.i("tb_sp_attack", tbg("sp_attack"))
    e.i("tb_sp_defense", tbg("sp_defense"))
    e.i("tb_speed", tbg("speed"))
    e.sym("tb_ability", tbg("ability", None) if tb is not None else None)
    tmv = tbg("moves", []) or []
    tpp = tbg("pp", []) or []
    for i in range(4):
        m = tmv[i] if i < len(tmv) else None
        e.sym(f"tb_move{i}", getattr(m, "name_jp", None) if m is not None else None)
        e.a(f"tb_pp{i}", int(tpp[i]) if i < len(tpp) else None)
    e.i("tb_n_moves", len(tmv))


def view_fields(e: Enc, v, pfx: str):
    e.pfx = pfx
    ks = sorted(v.pokemon.values(), key=lambda k: k.name)
    e.i("n", len(ks))
    for i, k in enumerate(ks):
        e.pfx = f"{pfx}k{i}_"
        e.sym("name", k.name)
        e.b("previewed", k.previewed)
        e.b("seen", k.seen)
        e.ty("type1", k.type1)
        e.ty("type2", k.type2)
        e.a("moves", "|".join(k.known_moves))
        e.sym("item", k.known_item)
        e.sym("ability", k.known_ability)
        e.b("threat", k.threat_alert)
        e.f("hpfrac", k.hp_fraction)
        e.i("dlog_n", len(k.damage_log))
        for j, d in enumerate(k.damage_log):
            e.sym(f"d{j}_mv", d.get("move"))
            e.sym(f"d{j}_at", d.get("attacker"))
            e.f(f"d{j}_fr", d.get("fraction", 0.0))
    e.pfx = pfx


def side_fields(e: Enc, s, field, pfx: str):
    e.pfx = pfx
    e.i("active_idx", s.active_idx)
    e.i("n_party", len(s.party))
    e.b("stealth_rock_set", _get(s, "stealth_rock_set", False))
    e.b("mega_used", s.mega_used)
    e.b("reflect", s.reflect)
    e.i("reflect_count", s.reflect_count)
    e.b("light_screen", s.light_screen)
    e.i("light_screen_count", s.light_screen_count)
    e.b("aurora_veil", s.aurora_veil)
    e.i("aurora_veil_count", s.aurora_veil_count)
    e.b("tailwind", s.tailwind)
    e.i("tailwind_count", _get(s, "tailwind_count", 0) or 0)
    e.i("wish_hp", _get(s, "wish_hp", 0) or 0)
    e.i("wish_count", _get(s, "wish_count", 0) or 0)
    e.b("healing_wish", _get(s, "healing_wish", False))
    e.i("safeguard", _get(s, "safeguard", 0) or 0)
    e.i("future_sight_count", _get(s, "future_sight_count", 0) or 0)
    e.i("future_sight_dmg", _get(s, "future_sight_dmg", 0) or 0)
    fsn = _get(s, "future_sight_name")
    e.a("future_sight_name", "" if not fsn else str(fsn))
    e.i("field_idx", s.field_idx)
    e.b("sr_pending", _get(s, "sr_pending", False))
    e.b("entry_pending", _get(s, "entry_pending", False))
    for i in range(len(s.party)):
        poke_fields(e, s.party[i], f"{pfx}p{i}.")
    view_fields(e, s.opp_view, f"{pfx}view.")


def field_fields(e: Enc, f):
    e.pfx = "F."
    e.sym("weather", f.weather)
    e.i("weather_count", _get(f, "weather_count", 0) or 0)
    e.b("trick_room", f.trick_room)
    e.i("trick_room_count", _get(f, "trick_room_count", 0) or 0)
    e.b("stealth_rock0", f.stealth_rock[0])
    e.b("stealth_rock1", f.stealth_rock[1])
    e.i("spikes0", f.spikes[0])
    e.i("spikes1", f.spikes[1])
    e.i("toxic_spikes0", f.toxic_spikes[0])
    e.i("toxic_spikes1", f.toxic_spikes[1])
    e.b("sticky_web0", f.sticky_web[0])
    e.b("sticky_web1", f.sticky_web[1])
    e.b("misty_terrain", _get(f, "misty_terrain", False))
    e.i("misty_terrain_count", _get(f, "misty_terrain_count", 0) or 0)
    e.b("electric_terrain", _get(f, "electric_terrain", False))
    e.i("electric_terrain_count", _get(f, "electric_terrain_count", 0) or 0)
    e.b("psychic_terrain", _get(f, "psychic_terrain", False))
    e.i("psychic_terrain_count", _get(f, "psychic_terrain_count", 0) or 0)
    e.i("gravity", _get(f, "gravity", 0) or 0)
    e.i("magic_room", _get(f, "magic_room", 0) or 0)
    e.i("wonder_room", _get(f, "wonder_room", 0) or 0)
    e.b("grassy_terrain", _get(f, "grassy_terrain", False))
    e.i("grassy_terrain_count", _get(f, "grassy_terrain_count", 0) or 0)
    e.b("weather_negated", _get(f, "weather_negated", False))


def encode_battle(b, with_names: bool = False) -> Enc:
    e = Enc(with_names)
    e.pfx = ""
    e.i("turn", b.turn)
    field_fields(e, b.field)
    side_fields(e, b.side1, b.field, "S1.")
    side_fields(e, b.side2, b.field, "S2.")
    return e
