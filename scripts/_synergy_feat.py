"""パーティのシナジー特徴（機械的定義）。spec 文字列だけから算出する。
「その種が要求するシナジー」を受け手/始動の観点で数える。定義はここが唯一の正本。
"""
import os, sys, sqlite3, functools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")


@functools.lru_cache(maxsize=1)
def moves():
    con = sqlite3.connect(DB)
    d = {n: (t, c, p) for n, t, c, p in con.execute("SELECT name_jp,type,category,power FROM move_master")}
    con.close()
    return d


_L = {}


def _loader():
    if "L" not in _L:
        from simulator.simulate import get_loader
        _L["L"] = get_loader()
    return _L["L"]


def _mega_ability(sp, item):
    """メガ石装備時の実効特性（specのability欄は非メガ時の特性なので別解決が要る）。"""
    key = (sp, item)
    if key in _L.setdefault("m", {}):
        return _L["m"][key]
    ab = None
    try:
        md = (_loader().get_pokemon_template(sp).mega_data or {}).get(item)
        ab = md.ability if md else None
    except Exception:
        ab = None
    _L["m"][key] = ab
    return ab


def _is_mega_item(it):
    return it.endswith(("ナイト", "ナイトＸ", "ナイトＹ", "ナイトX", "ナイトY"))


def parse(spec):
    head, rest = spec.split("@", 1)
    item, nature, mv, ev, ab = rest.split(":")
    if _is_mega_item(item):
        ab = _mega_ability(head, item) or ab
    return {"sp": head, "item": item, "moves": mv.split("|"), "ability": ab}


# --- 天候の「始動」定義（特性 or 技） ---
SETTER_ABIL = {"あめふらし": "rain", "ひでり": "sun", "ゆきふらし": "snow", "すなおこし": "sand",
               "メガソーラー": "sun", "ドロそう": None, "すなはき": "sand", "ゆきかき": None,
               "こだいかっせい": None, "エレキメイカー": "electric", "グラスメイカー": "grassy",
               "ミストメイカー": "misty", "サイコメイカー": "psychic"}
SETTER_MOVE = {"あまごい": "rain", "にほんばれ": "sun", "ゆきげしき": "snow", "あられ": "snow",
               "すなあらし": "sand", "エレキフィールド": "electric", "グラスフィールド": "grassy",
               "ミストフィールド": "misty", "サイコフィールド": "psychic"}
# --- 天候の「受け手」定義（速度特性 / 威力が乗る技タイプ / 天候専用技） ---
SPEED_ABIL = {"rain": "すいすい", "sun": "ようりょくそ", "snow": "ゆきかき", "sand": "すなかき"}
BOOST_TYPE = {"rain": "みず", "sun": "ほのお", "snow": None, "sand": None}
WEATHER_ONLY_MOVE = {"rain": {"かみなり", "ぼうふう", "エレクトロビーム"},
                     "sun": {"ソーラービーム", "ソーラーブレード", "グロウパンチ"},
                     "snow": {"オーロラベール", "ふぶき"},
                     "sand": set()}
DEFENSIVE_TYPE = {"snow": "こおり", "sand": "いわ"}   # 雪=こおりのB1.5 / 砂=いわのD1.5
MISC_ABIL = {"sun": {"サンパワー", "リーフガード", "かんそうはだ"},
             "rain": {"うるおいボディ", "あめうけざら", "かんそうはだ"},
             "sand": {"すながくれ", "すなのちから", "すなかき", "砂のちから"},
             "snow": {"ゆきがくれ", "アイスボディ", "ゆきかき"}}


def setter_of(spec):
    p = parse(spec)
    w = SETTER_ABIL.get(p["ability"])
    if w:
        return w
    for m in p["moves"]:
        if m in SETTER_MOVE:
            return SETTER_MOVE[m]
    return None


def weather_payoff(spec, w):
    """この1体が天候 w からどれだけ利益を得るか（0/1/2 のスコア）。"""
    p = parse(spec)
    MV = moves()
    sc = 0
    if p["ability"] == SPEED_ABIL.get(w):
        sc += 2
    if p["ability"] in MISC_ABIL.get(w, ()):
        sc += 1
    bt = BOOST_TYPE.get(w)
    if bt and any(MV.get(m, ("", "", None))[0] == bt and MV.get(m, ("", "status"))[1] != "status"
                  for m in p["moves"]):
        sc += 1
    if set(p["moves"]) & WEATHER_ONLY_MOVE.get(w, set()):
        sc += 2
    dt = DEFENSIVE_TYPE.get(w)
    return sc


def party_weather_payoff(specs, w, exclude=None):
    """自分（exclude=index）以外のチームメイトが天候 w から得る利益の合計スコア。"""
    return sum(weather_payoff(s, w) for i, s in enumerate(specs) if i != exclude)


def n_receivers(specs, w, exclude=None, thr=1):
    return sum(1 for i, s in enumerate(specs) if i != exclude and weather_payoff(s, w) >= thr)


def has_trickroom(specs, exclude=None):
    return any("トリックルーム" in parse(s)["moves"] for i, s in enumerate(specs) if i != exclude)


def other_setters(specs, exclude=None):
    return [setter_of(s) for i, s in enumerate(specs) if i != exclude and setter_of(s)]
