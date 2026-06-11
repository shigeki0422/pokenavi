"""戦略学習の対戦環境ハーネス（Phase 0）。

- 登録テンプレート（正本＝DB表 templates）の読み込みと確定スペック構築（型・EV・性格は Given）
- 選出方策(SelectionPolicy)の差し替えインターフェース（学習対象①）
- 自己対戦マッチの実行
- 決定化ロールアウトの土台となる状態クローン（Battle.clone）

行動方策（学習対象②）は ai callable をそのまま差し替えることで切り替える。
"""
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, List, Optional

from .data import DataLoader
from .pokemon import BattlePokemon, build_from_template
from .battle import Battle, BattleSide
from .ai import HeuristicAI, select_party

# UIのテンプレート選択（コンボボックス）と同一の登録パーティ源。
# 形式: name@item:nature:move1|move2|move3|move4:H/A/B/C/D/S:ability
TEMPLATES_TXT = Path(__file__).resolve().parent.parent / "party_templates_new.txt"
# 学習検証用の追加テンプレ（M-1正本とは別管理。バトン等の仮説検証用）
EXTRA_TEMPLATES_JSON = Path(__file__).resolve().parent.parent / "extra_templates.json"

# 選出方策の型: 自分6体・相手6体・loader → 選出済み順序付きリスト（先頭=リード）
SelectionPolicy = Callable[[List[BattlePokemon], List[BattlePokemon], DataLoader], List[BattlePokemon]]


@dataclass
class RegisteredParty:
    """登録テンプレートの確定パーティ（6体、型・EV・性格すべて確定）。"""
    party_id: int
    specs: List[dict] = field(default_factory=list)
    label: str = ""

    @property
    def names(self) -> List[str]:
        return [s["name"] for s in self.specs]


def _parse_member(s: str) -> dict:
    """'name@item:nature:m1|m2|m3|m4:H/A/B/C/D/S:ability' を spec dict に変換。"""
    name, rest = s.split("@", 1)
    item, nature, moves_s, ev_s, ability = rest.split(":")
    evk = [int(x) for x in ev_s.split("/")]
    evs = {k: (evk[i] if i < len(evk) else 0) for i, k in enumerate("HABCDS")}
    moves = [m for m in moves_s.split("|") if m and m not in ("不明", "なし")]
    return {"name": name.strip(), "item": item.strip(), "nature": nature.strip(),
            "ability": ability.strip(), "moves": moves, "evs": evs}


def _load_templates_txt(path: Path = TEMPLATES_TXT) -> List["RegisteredParty"]:
    """旧テンプレ txt をパースする（正本DB表へ移行するためのシード専用。通常は使わない）。"""
    if not Path(path).exists():
        return []
    txt = Path(path).read_text(encoding="utf-8")
    entries = re.findall(
        r'\{\s*id:\s*"([^"]+)",\s*name:\s*"([^"]+)",\s*tag:\s*"([^"]+)",\s*party:\s*\[(.*?)\]\s*\}',
        txt, re.S)
    out = []
    for _id, name, tag, body in entries:
        members = re.findall(r'"([^"]+@[^"]+)"', body)
        m = re.search(r'#(\d+)', tag)
        pid = int(m.group(1)) if m else len(out) + 1
        out.append(RegisteredParty(party_id=pid, label=name,
                                   specs=[_parse_member(s) for s in members]))
    return out


def load_templates(loader: Optional[DataLoader] = None) -> List["RegisteredParty"]:
    """登録テンプレートの**正本**（DB表 templates）を読み込む。
    party_id は M-1 順位。表が無い場合は旧 txt にフォールバック（移行期のみ）。"""
    if loader is None:
        from .simulate import get_loader
        loader = get_loader()
    has = loader.con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='templates'"
    ).fetchone()
    if not has:
        return _load_templates_txt()
    rows = loader.con.execute(
        "SELECT party_id, label, slot, pokemon, item, nature, ability, "
        "move1, move2, move3, move4, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s "
        "FROM templates ORDER BY party_id, slot"
    ).fetchall()
    by_id: dict = {}
    for r in rows:
        moves = [r[c] for c in ("move1", "move2", "move3", "move4") if r[c]]
        spec = {"name": r["pokemon"], "item": r["item"], "nature": r["nature"],
                "ability": r["ability"], "moves": moves,
                "evs": {"H": r["ev_h"], "A": r["ev_a"], "B": r["ev_b"],
                        "C": r["ev_c"], "D": r["ev_d"], "S": r["ev_s"]}}
        if r["party_id"] not in by_id:
            by_id[r["party_id"]] = RegisteredParty(party_id=r["party_id"], label=r["label"], specs=[])
        by_id[r["party_id"]].specs.append(spec)
    return [by_id[k] for k in sorted(by_id)]


def load_extra_templates(path: Path = EXTRA_TEMPLATES_JSON) -> List["RegisteredParty"]:
    """学習検証用の追加テンプレ（M-1正本とは別ファイル）を読み込む。仮説検証専用。"""
    import json
    if not Path(path).exists():
        return []
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    out = []
    for d in data:
        specs = [{"name": s["name"], "item": s["item"], "nature": s["nature"],
                  "ability": s["ability"], "moves": [m for m in s["moves"] if m and m not in ("不明", "なし")],
                  "evs": {k: s["evs"].get(k, 0) for k in "HABCDS"}} for s in d["specs"]]
        out.append(RegisteredParty(party_id=d["party_id"], label=d.get("label", ""), specs=specs))
    return out


def spec_to_string(spec: dict) -> str:
    """spec dict → UI/サーバが用いる spec 文字列（generate_ui_templates と同形式）。"""
    moves = (list(spec.get("moves", [])) + ["なし", "なし", "なし", "なし"])[:4]
    ev = "/".join(str(spec["evs"].get(k, 0)) for k in "HABCDS")
    return f'{spec["name"]}@{spec["item"]}:{spec["nature"]}:{"|".join(moves)}:{ev}:{spec["ability"]}'


def template_index(loader: Optional[DataLoader] = None) -> dict:
    """6体 spec 文字列の集合 → テンプレート party_id の逆引き索引。
    ブラウザから送られた選出スペックを正本テンプレに対応づけ、学習済み選出戦略を引くのに使う。"""
    idx = {}
    for p in load_templates(loader):
        idx[frozenset(spec_to_string(s) for s in p.specs)] = p.party_id
    return idx


def is_complete_party(party: "RegisteredParty", loader: DataLoader,
                      season: str = "M-2") -> bool:
    """シミュレーション可能か：全メンバーの種族がDBに存在し、技が解決でき『不明』を含まない。"""
    for spec in party.specs:
        if loader.get_pokemon_template(spec["name"], season) is None:
            return False
        mv = spec.get("moves") or []
        if not mv or "不明" in mv:
            return False
        if any(loader.get_move(m) is None for m in mv):
            return False
    return True


def load_registered_parties(loader: DataLoader, complete_only: bool = False,
                            season: str = "M-2") -> List[RegisteredParty]:
    """登録パーティ一覧を読み込む（正本はDB表 templates）。
    M-1上位のうち情報欠落分を除いた完全パーティ群。complete_only は技解決可否で再フィルタ。"""
    out = load_templates(loader)
    if complete_only:
        out = [p for p in out if is_complete_party(p, loader, season)]
    return out


def build_party(party: RegisteredParty, loader: DataLoader,
                season: str = "M-2") -> List[BattlePokemon]:
    """登録パーティの確定スペックから BattlePokemon 6体を構築する（randomize しない）。"""
    out = []
    for spec in party.specs:
        tpl = loader.get_pokemon_template(spec["name"], season)
        if tpl is None:
            raise ValueError(f"ポケモン '{spec['name']}' が見つかりません (season={season})")
        out.append(build_from_template(
            tpl, loader, randomize=False,
            override_item=spec["item"], override_nature=spec["nature"],
            override_ability=spec["ability"], override_evs=spec["evs"],
            override_moves=spec["moves"]))
    return out


def heuristic_selection(my6: List[BattlePokemon], opp6: List[BattlePokemon],
                        loader: DataLoader) -> List[BattlePokemon]:
    """既定の選出方策（select_party）。"""
    return select_party(my6, opp6, loader, n=min(3, len(my6)))


def play_match(p1: RegisteredParty, p2: RegisteredParty, loader: DataLoader,
               ai1=None, ai2=None,
               sel1: SelectionPolicy = heuristic_selection,
               sel2: SelectionPolicy = heuristic_selection,
               season: str = "M-2") -> int:
    """登録パーティ同士を1試合対戦させる。戻り値: 1=p1勝利, 2=p2勝利, 0=引き分け。

    選出方策・行動方策(ai)は引数で差し替え可能（学習方策の評価に使う）。
    """
    ai1 = ai1 or HeuristicAI()
    ai2 = ai2 or HeuristicAI()
    party1 = build_party(p1, loader, season)
    party2 = build_party(p2, loader, season)
    sel_p1 = sel1(party1, party2, loader)
    sel_p2 = sel2(party2, party1, loader)
    return Battle(BattleSide(sel_p1), BattleSide(sel_p2)).run(ai1, ai2)
