"""AI の「相手の型の読み」のスナップショット（対戦記録・再生・精度集計用）。

対戦AIは相手の型を OpponentBelief（信念）で持ち、探索の決定化で型を引く。
ここではその中身を、人が読める形で取り出す。**信念は書き換えない**
（記録を付けても対戦の進行・乱数・AIの判断は変わらない）。

出すもの（相手の各ポケモン、viewer が見せ合い/登場で知っている種族ごと）:
- known: 判明済みの技・持ち物・特性・持ち物喪失
- marginal: 使用率ベースの周辺分布（JOINT_BUILD=0、または型が無い種の決定化が引く分布）
    技ごとの所持確率・持ち物/特性の確率・努力値/性格の事後上位
- pool: 型プールの事後（型まるごと。既定＝JOINT_BUILD ON の決定化が引く分布）
    判明情報と矛盾しない型を、観測したダメージの尤度で重み付けした上位候補と、そこから出す技/持ち物の確率
- used: その時点でAIの決定化が実際に使う方（"pool" / "marginal"）
"""
import copy
from typing import Dict, List, Optional

from .belief import pool_builds_by_species, OpponentBelief

def _norm(d: Dict[str, float]) -> Dict[str, float]:
    t = sum(v for v in d.values() if v > 0)
    return {k: v / t for k, v in d.items() if v > 0} if t > 0 else {}


def _top(d: Dict[str, float], n: int) -> List[list]:
    """確率の降順（小数4桁に丸めた値で並べ、同率は名前順。浮動小数の和の順序差で並びが揺れないように）"""
    return [[k, round(v, 4)] for k, v in sorted(d.items(), key=lambda kv: (-round(kv[1], 4), kv[0]))[:n]]


def _ev_str(ev) -> str:
    if isinstance(ev, dict):
        ev = [ev.get(k, 0) for k in "HABCDS"]
    return "/".join(str(int(x)) for x in ev)


class Predictor:
    """1対戦ぶんの読み取り器。型プールの事後は種族ごとの影（信念の写し）で増分計算する。"""

    def __init__(self, loader, top: int = 5):
        self.loader = loader
        self.top = top
        self._pool = pool_builds_by_species()
        self._shadow: Dict[tuple, object] = {}
        self._fresh: Dict[int, OpponentBelief] = {}
        self._appeared: Dict[int, set] = {}

    def _pb(self, side, name):
        bel = getattr(side, "belief", None)
        pb = bel.get(name) if bel is not None else None
        if pb is not None:
            return pb, bel
        # AI がまだこの種の信念を作っていない（観測も無い）→ 同じ作り方の新品で事前分布を読む
        key = id(side)
        if key not in self._fresh:
            self._fresh[key] = OpponentBelief(self.loader)
        return self._fresh[key].ensure(name), bel

    def _shadow_of(self, side, name, pb):
        """型プールの事後を計算するための写し。known/absent は毎回写し直し、観測（dmg_obs）は共有して増分で反映。"""
        key = (id(side), name)
        sh = self._shadow.get(key)
        if sh is None or sh.dmg_obs is not pb.dmg_obs:
            sh = copy.copy(pb)
            sh.builds = self._pool.get(name, [])
            sh.pool_w, sh._pool_applied, sh._pool_prof, sh._profs = [], 0, [], []
            self._shadow[key] = sh
        sh.known_moves = set(pb.known_moves)
        sh.known_item = pb.known_item
        sh.known_ability = pb.known_ability
        sh.absent_items = set(pb.absent_items)
        sh.item_lost = pb.item_lost
        return sh

    def snapshot(self, side, opp_side=None) -> Dict[str, dict]:
        """side（読む側）が相手の各ポケモンをどう読んでいるか。
        opp_side を渡すと、場に出たことのある相手を appeared に記録する（先発は opp_view の seen が
        立たない経路＝feature1 の記録があるため、場の実物で数える）。"""
        view = side.opp_view
        app = self._appeared.setdefault(id(side), set())
        if opp_side is not None and opp_side.active is not None:
            app.add(opp_side.active.name)
        bel = getattr(side, "belief", None)
        out = {}
        for name, k in view.pokemon.items():
            pb, _ = self._pb(side, name)
            if pb is None:
                continue
            # AI は次の手番で opp_view の開示を信念に取り込む。記録時点で判明している分は
            # ここで写しに足して読む（信念そのものは書き換えない）
            known_moves = sorted(set(pb.known_moves) | set(k.known_moves))
            known_item = pb.known_item or k.known_item
            known_ability = pb.known_ability or k.known_ability
            item_lost = bool(pb.item_lost or getattr(k, "item_lost", False))
            ent = {"appeared": bool(k.seen or name in app),
                   "known": {"moves": known_moves, "item": known_item, "ability": known_ability,
                             "item_lost": item_lost}}
            # ── 周辺分布（JOINT_BUILD=0 の決定化） ──
            mv = {m: min(1.0, r / 100.0) for m, r in pb.move_prior.items()}
            for m in known_moves:
                mv[m] = 1.0
            if known_item is not None:
                it = {known_item: 1.0}
            else:
                it = _norm({i: r for i, r in pb.item_prior.items() if i not in pb.absent_items})
            ab = {known_ability: 1.0} if known_ability else _norm(dict(pb.ability_prior))
            sp = [{"ev": _ev_str(ev), "nature": nat, "p": round(p, 4)}
                  for _lab, ev, nat, p in pb.spread_posterior()[:3]]
            ent["marginal"] = {"moves": _top(mv, 12), "item": _top(it, self.top),
                               "ability": _top(ab, 3), "spread": sp}
            # ── 型プールの事後（JOINT_BUILD=1 の決定化） ──
            pool = None
            if self._pool.get(name):
                sh = self._shadow_of(side, name, pb)
                sh.known_moves |= set(k.known_moves)
                if k.known_item and sh.known_item is None:
                    sh.known_item = k.known_item
                if k.known_ability and sh.known_ability is None:
                    sh.known_ability = k.known_ability
                ok = sh.consistent_builds()
                if ok:
                    pw = sh.pool_weights()
                    wmap = {id(b): x for b, x in zip(sh.builds, pw)}
                    ws = [(b, wmap[id(b)]) for b in ok]
                    tot = sum(x for _, x in ws)
                    if tot > 0:
                        ws.sort(key=lambda bx: -bx[1])
                        pm: Dict[str, float] = {}
                        pi: Dict[str, float] = {}
                        pn: Dict[str, float] = {}
                        for b, x in ws:
                            p = x / tot
                            for m in b["moves"]:
                                pm[m] = pm.get(m, 0.0) + p
                            pi[b["item"]] = pi.get(b["item"], 0.0) + p
                            key = f'{_ev_str(b["ev"])} {b["nature"]}'
                            pn[key] = pn.get(key, 0.0) + p
                        pool = {"n_consistent": len(ok),
                                "top": [{"side": b.get("side", ""),
                                         "p": round(x / tot, 4), "item": b["item"],
                                         "nature": b["nature"], "ev": _ev_str(b["ev"]),
                                         "ability": b.get("ability", ""), "moves": list(b["moves"])}
                                        for b, x in ws[:self.top]],
                                "moves": _top(pm, 12), "item": _top(pi, self.top),
                                "spread": _top(pn, 3)}
            ent["pool"] = pool
            joint = bool(bel is not None and getattr(bel, "joint", False))
            ent["used"] = "pool" if (joint and pool is not None) else "marginal"
            out[name] = ent
        return out


def truth_of(p) -> dict:
    """個体の実際の型（精度集計の正解）。対戦開始時点で取る（メガ前の特性・消費前の持ち物）。"""
    evs = getattr(p, "evs", None) or {}
    return {"name": p.name, "item": p.item, "ability": p.ability, "nature": getattr(p, "nature", None),
            "ev": _ev_str({k: evs.get(k, 0) for k in "HABCDS"}),
            "moves": [m.name_jp for m in p.moves if m]}
