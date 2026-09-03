"""M-3パーティ生成の土台：build_pool_M-3.md の型のみを使い、使用率順位で重み付けして
6体パーティをサンプルする（型数の多寡が種の選出確率に影響しないよう、種→型の二段選択）。
任意のわざ/特性/持ち物/EVの組合せ探索はしない（mdの型のみ）。GAはこの上に載せる。

M-3はusage_rate未格納のため種の重みは順位(rank)から算出（既定 1/rank^RANK_EXP）。
使い方: venv/bin/python gen_party_pool.py [N]
"""
import os, re, sys, random, collections, sqlite3, math

D = os.path.dirname(__file__)
MD = os.path.join(D, "build_pool_M-3.md")
DBPATH = os.path.join(D, "pokenavi.db")
SEASON = "M-3"
EVK = ["H", "A", "B", "C", "D", "S"]
RANK_EXP = float(os.environ.get("RANK_EXP", "1.0"))
TYPE_LINE = re.compile(r"^- (?:\*\*.+?\*\*\s*)?\[([^/\]]+)/([^/\]]+)/([^/\]]+)/([^\]]+)\]\s*(.+)$")
HEADER = re.compile(r"^## (.+?)  #(\d+)")
# spec区切り":"と衝突する種(コロン形)は解決可能な括弧形へ
FORM_FIX = {"ケンタロス:炎": "パルデアケンタロス(炎)", "ケンタロス:水": "パルデアケンタロス(水)",
            "ケンタロス:格": "パルデアケンタロス(闘)",
            # build_pool の「## キュウコン #17」は中身が完全にアローラ種（特性ゆきふらし100%・
            # フリーズドライ/ふぶき・オーロラベール96%）。素の名前だと通常キュウコン（ほのお単・ひでり）が
            # 解決され「ほのおタイプでゆきふらしを持つ」実在しないキメラになり、さらに使用率も
            # 通常キュウコンの168位で上書きされて MAX_RANK=80 の補完プールから脱落していた（実際は9位）。
            "キュウコン": "アローラキュウコン"}

def _ev_to_slash(evstr):
    d = {k: 0 for k in EVK}
    for tok in evstr.replace("なし", "").split():
        m = re.match(r"([HABCDS])(\d+)", tok)
        if m: d[m.group(1)] = int(m.group(2))
    return "/".join(str(d[k]) for k in EVK)

def _is_mega(item):
    return (item.endswith("ナイト")
            or item.endswith("ナイトＸ") or item.endswith("ナイトＹ")
            or item.endswith("ナイトX") or item.endswith("ナイトY"))

ITEMUSE = re.compile(r"([^\s/(]+)\((\d+)\)")

def _moves_of(s):
    return s.split("@", 1)[1].split(":")[2].split("|")

def _moves_clean(mv_list, avail):
    """技クリーン型か：重複が無く、全技が使用率リスト(avail)内。avail未整備(空)は判定せずTrue。"""
    if len(mv_list) != len(set(mv_list)):
        return False                           # 重複技（build_pool ドラフトのバグ）
    if avail and any(m not in avail for m in mv_list):
        return False                           # 使用率リスト外の技(≈0%=古いM-2技等)
    return True

def parse_pool(md=MD):
    """returns (pool {poke:[spec,...]}, rank {poke:int}, item_usage {poke:{item:pct}})。種名はFORM_FIX適用済み。"""
    pool = collections.defaultdict(list); rank = {}; item_usage = collections.defaultdict(dict)
    moves_pool = collections.defaultdict(list)
    # 追加型ファイル（M-3上位構築から抽出したクリーン実型）を後続でマージ。rankは本体md優先。
    _extra = os.path.join(os.path.dirname(md), "build_pool_M-3_extra.md")
    sources = [md] + ([_extra] if os.path.exists(_extra) else [])
    cur = None
    for _src in sources:
      for ln in open(_src, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln.startswith("## "):
            h = HEADER.match(ln)
            if h and not ln[3:].startswith("（"):
                cur = h.group(1).strip(); rank.setdefault(cur, int(h.group(2)))
            else:
                cur = None
            continue
        if cur is None: continue
        if ln.lstrip().startswith("- 持ち物:"):
            for it, pct in ITEMUSE.findall(ln): item_usage[cur][it] = int(pct)
            continue
        if ln.lstrip().startswith(("- 攻撃技:", "- 変化技:")):
            for mn, _ in ITEMUSE.findall(ln):
                if mn not in moves_pool[cur]: moves_pool[cur].append(mn)
            continue
        m = TYPE_LINE.match(ln)
        if not m: continue
        item, nature, ability, evs, moves = (x.strip() for x in m.groups())
        moves = "|".join(s.strip() for s in moves.split("/") if s.strip())
        sp = FORM_FIX.get(cur, cur)
        pool[cur].append(f"{sp}@{item}:{nature}:{moves}:{_ev_to_slash(evs)}:{ability}")
    def norm(s):
        head, rest = s.split("@", 1); it, na, mv, ev, ab = rest.split(":")
        return (it, na, ab, frozenset(mv.split("|")), ev)
    for p in pool:
        seen, uniq = set(), []
        for s in pool[p]:
            k = norm(s)
            if k in seen: continue
            seen.add(k); uniq.append(s)
        pool[p] = uniq
    return dict(pool), rank, dict(item_usage), dict(moves_pool)

def _ev_clean(s):
    """ブッパ型か：最大振り(≥28)が1〜2ステ、中間値(7〜27)なし、端数(1〜6)は最大1ステまで。
    ＝実質「2ステに全振り＋余り」。散らばった振り(H29 A32 B4 S3 等)は弾く。"""
    ev = [int(x) for x in s.split("@", 1)[1].split(":")[3].split("/")]
    big = sum(1 for v in ev if v >= 28)
    small = sum(1 for v in ev if 1 <= v <= 6)
    mid = sum(1 for v in ev if 7 <= v <= 27)
    return mid == 0 and 1 <= big <= 2 and small <= 1

def _prefer_builds(builds, avail, item_usage=None):
    """技クリーン型(重複無し・使用率リスト内)を優先→その中でEVブッパ型を優先。各段で無ければフォールバック。
    技構成が完全一致する型が複数残る場合は持ち物使用率最大の1つに絞る（例: 壁2種持ちで「ひかりのねんど」が
    実測70%なのに「たべのこし」型が同居していると、IU_FLOORで両者の重み差が縮まり技と噛み合わない持ち物が
    一定確率で選ばれてしまう。技が同じなら持ち物の優劣はほぼ決定的なので、ここで重複を除いておく）。"""
    c = [s for s in builds if _moves_clean(_moves_of(s), avail)]
    builds = c if c else builds
    c = [s for s in builds if _ev_clean(s)]
    builds = c if c else builds
    if item_usage:
        best = {}
        for s in builds:
            key = tuple(sorted(_moves_of(s)))
            iu = item_usage.get(_item_of(s), 0)
            if key not in best or iu > item_usage.get(_item_of(best[key]), 0):
                best[key] = s
        builds = list(best.values()) or builds
    return builds

def _spec_mega(s):
    return _is_mega(s.split("@", 1)[1].split(":")[0])

def _item_of(s):
    return s.split("@", 1)[1].split(":")[0]

_HAZARD_M = {"ステルスロック", "まきびし", "どくびし", "スパイク"}
_STATUS_M = {"おにび", "でんじは", "どくどく", "あくび", "ちょうはつ", "ねむりごな", "キノコのほうし",
             "やどりぎのタネ", "しびれごな", "どくのこな", "さいみんじゅつ", "でんじゃく"}
_RECOVERY_M = {"なまける", "はねやすめ", "じこさいせい", "つきのひかり", "こうごうせい", "あさのひざし",
               "タマゴうみ", "ねむる"}
_RECOVERY_IT = {"たべのこし", "オボンのみ", "くろいヘドロ"}
# 人間分布に寄せる役割目標（1チームあたり）
_ROLE_TARGET = {"hazard": 1, "special": 2, "status": 1, "recovery": 2, "bulk": 3}

def sample_role_targets(rng):
    """M-3上位119実構築の役割/党統計（hazard0.78 special2.59 status1.15 recovery2.03 bulk3.08 scarf0.57）に較正した確率的目標。"""
    t = {"special": 3 if rng.random() < 0.6 else 2, "status": 1, "recovery": 2, "bulk": 3}
    if rng.random() < 0.6: t["hazard"] = 1
    if rng.random() < 0.25: t["scarf"] = 1
    return t
ITEM_USAGE_W = float(os.environ.get("ITEM_USAGE_W", "1.5"))   # パーティ採用スコアでの持ち物使用率の重み（支配的アイテムを優先／拮抗時は役割が決める）
MV_POW = float(os.environ.get("MV_POW", "1.5"))     # 技使用率(幾何平均)の指数。上げるほど人気技構成に寄る（トリル等の低使用率技を抑制）
ROLE_W = float(os.environ.get("ROLE_W", "2.0"))     # 型選択での役割充足ボーナス係数。上げるほど役割目標(実構築較正)の達成率が上がる
IU_FLOOR = float(os.environ.get("IU_FLOOR", "20"))  # argmax使用率項の持ち物使用率フロア。上げるほど不人気持ち物×人気技構成の型が役割枠を競える（20でミミッキュトリル率15%≒実12%）
MIN_MEGA_USAGE = float(os.environ.get("MIN_MEGA_USAGE", "5"))   # メガ石の実使用率(%)がこれ未満なら生成候補から除外（2026-07-13）

class PartyGen:
    def __init__(self):
        self.pool, self.rank, self.item_usage, self.moves_pool = parse_pool()
        self.pokes = [p for p in self.pool if self.pool[p]]
        live = self._live_rank()                       # 最新クロール(7/1)の使用率順位を優先
        # プールのキーとDBの種名が食い違うフォーム（例: キー「キュウコン」＝実体アローラキュウコン）は
        # FORM_FIX で解決した実体名の順位を引く。素の名前で引くと別種の順位（通常キュウコン168位）を
        # 拾い、MAX_RANK の補完プールから実使用率9位の種が丸ごと脱落する。
        if live:
            # FORM_FIX は「このプールキーの実体はこの種」という宣言なので、キーが同名で
            # DBに存在していても実体側の順位で必ず上書きする（同名の別種を拾うのが問題そのもの）。
            for _k, _real in FORM_FIX.items():
                if _real in live: live[_k] = live[_real]
            self.rank = {p: live.get(p, self.rank.get(p, 9999)) for p in self.pokes}
        self.w = {p: 1.0 / (self.rank.get(p, 9999) ** RANK_EXP) for p in self.pokes}
        self.wlist = [self.w[p] for p in self.pokes]
        # 型をメガ/非メガに分割（ちょうどMEGAS体メガにするため）。技クリーン→EVブッパの順で優先。
        # メガ型はさらに実使用率でhi/loに分ける：hiのみクロール使用率ベースの技クリーンフィルタ(_prefer_builds)
        # を通す。lo（実使用率がMIN_MEGA_USAGE%未満＝実例0〜僅少で技クリーン判定に使う使用率リスト自体が
        # 無い/信頼できない。メガライチュウXの手動作成型もここに入る）はフィルタを適用せず素通しする
        # （壊れ型チェックは将来greedyで別途行う想定＝Part3 S1）。
        def _usage_of(p, s): return self.item_usage.get(p, {}).get(_item_of(s), 0)
        _mega_raw = {p: [s for s in self.pool[p] if _spec_mega(s)] for p in self.pokes}
        _mega_hi = {p: [s for s in bs if _usage_of(p, s) >= MIN_MEGA_USAGE] for p, bs in _mega_raw.items()}
        _mega_lo = {p: [s for s in bs if _usage_of(p, s) < MIN_MEGA_USAGE] for p, bs in _mega_raw.items()}
        # 実使用率がMIN_MEGA_USAGE%未満のメガ型は「自動生成（ランダムな相方選択）」の候補から除外する
        # （例: メガガブリアス実使用率1%＝ガブリアス使用者のほぼ誰も選ばない型だが、記事1本の実例だけで
        # プールに残っていた）。ただし self.mega_all（除外前）は明示コア指定の解決用に残す＝
        # Part3「低使用率ポケモンのパーティ提案対応」でユーザーが意図してメガライチュウX等を選んだ場合は
        # 使用率に関わらず解決できる（種自体・非メガ型は元々フィルタ対象外）。
        self.mega = {p: _prefer_builds(_mega_hi.get(p, []), self.moves_pool.get(p, []), self.item_usage.get(p, {})) for p in self.pokes}
        self.mega_all = {p: self.mega[p] + _mega_lo.get(p, []) for p in self.pokes}
        self.nonm = {p: _prefer_builds([s for s in self.pool[p] if not _spec_mega(s)], self.moves_pool.get(p, []), self.item_usage.get(p, {})) for p in self.pokes}
        self.pool = {p: self.mega[p] + self.nonm[p] for p in self.pokes}   # 自動生成用（コア解決も既定はこちら）
        # 明示コア指定の解決専用プール（低使用率メガも含む・resolve_fixedが参照）
        self.pool_resolve = {p: self.mega_all[p] + self.nonm[p] for p in self.pokes}
        # 生成除外: イリュージョン/へんしんで価値ネットが扱いづらい種、および上のメガ除外で型が0件になった種は
        # 自動生成の候補にしない（poolには残す種は残すので明示指定コアとしては解決可能な場合は解決可能。
        # self.w/pokesから外れ同居率・貪欲の両経路で候補外）
        _ban = {n for n in ("メタモン", "ゾロアーク", "ゾロアーク(ヒスイ)", "ヒスイゾロアーク") if n in self.pokes}
        _ban |= {p for p in self.pokes if not self.pool[p]}
        if _ban:
            self.pokes = [p for p in self.pokes if p not in _ban]
            for p in _ban: self.w.pop(p, None)
            self.wlist = [self.w[p] for p in self.pokes]
        self.key_of = {self.pool[p][0].split("@")[0]: p for p in self.pokes}   # spec種名→プールキー
        self.dex = self._build_dex()   # プール種→図鑑番号(4桁)。同一図鑑(リージョン/性別違い)は同種扱い
        self.cooc = self._load_cooc()  # 同居率グラフ（人間が一緒に使う＝整合コアの事前分布）
        self.mvcat = self._load_mvcat()
        self.build_roles = {s: self._role_tags(s) for p in self.pokes for s in self.pool[p]}

    def _load_mvcat(self):
        d = {}
        try:
            con = sqlite3.connect(DBPATH)
            for n, c in con.execute("SELECT name_jp,category FROM move_master"):
                d[n] = c
            con.close()
        except Exception:
            pass
        return d

    def _role_tags(self, spec):
        head, rest = spec.split("@", 1)
        item, nature, moves_s, ev, ability = rest.split(":")
        moves = set(moves_s.split("|"))
        evk = ev.split("/")
        tags = set()
        if moves & _HAZARD_M: tags.add("hazard")
        if moves & _STATUS_M: tags.add("status")
        if (moves & _RECOVERY_M) or (item in _RECOVERY_IT): tags.add("recovery")
        if int(evk[0]) >= 16: tags.add("bulk")   # HP16+投資=耐久意図
        if item == "こだわりスカーフ": tags.add("scarf")   # 速度操作
        nsp = sum(1 for m in moves if self.mvcat.get(m) == "special")
        nph = sum(1 for m in moves if self.mvcat.get(m) == "physical")
        if nsp > nph: tags.add("special")
        elif nph > nsp: tags.add("physical")
        return tags

    def _live_rank(self):
        try:
            con = sqlite3.connect(DBPATH)
            cd = con.execute("SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-3' AND rule='single'").fetchone()[0]
            r = {p: rk for p, rk in con.execute("SELECT pokemon,rank FROM pokemon_usage WHERE season='M-3' AND rule='single' AND crawled_date=?", (cd,)) if rk}
            con.close()
            return r
        except Exception:
            return {}

    def _load_cooc(self):
        g = collections.defaultdict(dict)
        try:
            con = sqlite3.connect(DBPATH)
            cd = con.execute("SELECT MAX(crawled_date) FROM pokemon_partners WHERE season='M-3' AND rule='single'").fetchone()[0]
            for pk, pt, rk in con.execute("SELECT pokemon,partner,rank FROM pokemon_partners WHERE season='M-3' AND rule='single' AND crawled_date=?", (cd,)):
                if rk: g[pk][pt] = 1.0 / rk
            con.close()
        except Exception:
            pass
        return dict(g)

    def _pick_holders(self, picked, megas, rng):
        forced = [p for p in picked if self.mega[p] and not self.nonm[p]]
        if len(forced) > megas: return None
        holders = set(forced)
        cand = [p for p in picked if p not in holders and self.mega[p]]
        need = megas - len(holders)
        if len(cand) < need: return None
        holders |= set(rng.sample(cand, need))
        if any(not self.nonm[p] for p in picked if p not in holders): return None
        return holders

    def sample_cooc(self, rng, n=6):
        """同居率を事前分布に、整合したコアを育てて6体を組む。メガは1〜2。
        各追加は確率COOC_Pで『既選出メンバーの同居相手』から同居重みでサンプル（＝実同居構造を忠実に再現）、
        残りは使用率×同居ブーストの大域サンプル。"""
        COOC_P = float(os.environ.get("COOC_P", "0.6"))
        COOC_W = float(os.environ.get("COOC_W", "4.0"))
        for _ in range(400):
            megas = 2 if rng.random() < 0.83 else 1   # 実M-2のメガ数分布に寄せる
            picked = [rng.choices(self.pokes, weights=self.wlist, k=1)[0]]
            used_dex = {self.dex.get(picked[0])}
            ok = True
            while len(picked) < n:
                nxt = None
                if rng.random() < COOC_P:   # 既選出の同居相手から（同居構造を忠実に）
                    neigh = collections.Counter()
                    for q in picked:
                        for pt, w in self.cooc.get(q, {}).items():
                            if pt in self.w and self.dex.get(pt) not in used_dex:
                                neigh[pt] += w
                    if neigh:
                        cs = list(neigh); nxt = rng.choices(cs, weights=[neigh[c] for c in cs], k=1)[0]
                if nxt is None:             # 大域（使用率×同居ブースト）
                    cands = []; ws = []
                    for p in self.pokes:
                        if self.dex.get(p) in used_dex: continue
                        cs = sum(self.cooc.get(q, {}).get(p, 0) + self.cooc.get(p, {}).get(q, 0) for q in picked)
                        cands.append(p); ws.append(self.w[p] * (1 + COOC_W * cs))
                    if not cands: ok = False; break
                    nxt = rng.choices(cands, weights=ws, k=1)[0]
                picked.append(nxt); used_dex.add(self.dex.get(nxt))
            if not ok: continue
            holders = self._pick_holders(picked, megas, rng)
            if holders is None: continue
            if os.environ.get("ROLE_BIAS", "1") == "1":
                tgt = dict(_ROLE_TARGET)
                if rng.random() < 0.65: tgt["scarf"] = 1   # 実人間のスカーフ採用率に合わせる
                party = self._role_builds(picked, holders, rng, targets=tgt)
            else:
                party = self._distinct_builds(picked, holders, rng)
            if party and self.is_legal(party, megas_set=(1, 2)):
                return party
        return None

    def _build_dex(self):
        name2dex = {}
        try:
            con = sqlite3.connect(DBPATH)
            for nm, pid in con.execute("SELECT DISTINCT pokemon,pokemon_id FROM pokemon_usage WHERE pokemon_id IS NOT NULL"):
                if pid and len(pid) >= 4:
                    name2dex.setdefault(nm, pid[:4])
            con.close()
        except Exception:
            pass
        base = lambda n: re.split(r"[（(:：]", n)[0].strip()
        bidx = {}
        for n, d in name2dex.items():
            bidx.setdefault(base(n), d)
        out = {}
        for p in self.pokes:
            out[p] = name2dex.get(p) or bidx.get(base(p)) or ("X:" + p)   # 未解決は固有扱い
        return out

    def dexof(self, spec):
        k = self.keyof(spec)
        return self.dex.get(k, "X:" + spec.split("@")[0])

    def keyof(self, spec):
        return self.key_of.get(spec.split("@")[0])

    def fix_mega(self, party, rng, megas=2):
        """party(6spec)のメガ数をちょうどmegasに調整（同種内で型差替、無理なら種差替）。失敗時None。"""
        party = list(party)
        for _ in range(60):
            idx_m = [i for i, s in enumerate(party) if _spec_mega(s)]
            if len(idx_m) == megas:
                return party
            if len(idx_m) > megas:   # 減らす: メガmonを非メガ型へ
                cands = [i for i in idx_m if self.nonm.get(self.keyof(party[i]))]
                if not cands: return None
                i = rng.choice(cands); party[i] = rng.choice(self.nonm[self.keyof(party[i])])
            else:                    # 増やす: 非メガmonをメガ型へ
                cands = [i for i, s in enumerate(party) if not _spec_mega(s) and self.mega.get(self.keyof(s))]
                if not cands: return None
                i = rng.choice(cands); party[i] = rng.choice(self.mega[self.keyof(party[i])])
        return None

    def sample(self, rng, n=6, megas=2):
        """6種を順位重みで選び、ちょうど megas 体をメガ石持ちにする。"""
        for _ in range(500):
            picked = []
            used = set(); used_dex = set(); t = 0
            while len(picked) < n and t < 300:
                t += 1
                p = rng.choices(self.pokes, weights=self.wlist, k=1)[0]
                d = self.dex.get(p)
                if p not in used and d not in used_dex:
                    picked.append(p); used.add(p); used_dex.add(d)
            if len(picked) < n: continue
            forced = [p for p in picked if self.mega[p] and not self.nonm[p]]   # メガ専用(非メガ型なし)
            if len(forced) > megas: continue
            holders = set(forced)
            cand = [p for p in picked if p not in holders and self.mega[p]]
            need = megas - len(holders)
            if len(cand) < need: continue
            holders |= set(rng.sample(cand, need))
            rest = [p for p in picked if p not in holders]
            if any(not self.nonm[p] for p in rest): continue   # 非メガにできない種が残ると不可
            party = self._distinct_builds(picked, holders, rng)
            if party is not None:
                return party
        return None

    def _distinct_builds(self, picked, holders, rng, tries=60):
        """各種に型を割当て、6体の持ち物が全て相異なるようにする（メガ石は種固有で自動的に別）。
        充足できなければ None。"""
        for _ in range(tries):
            order = list(picked); rng.shuffle(order)
            party = {}; used_items = set(); ok = True
            for p in order:
                builds = list(self.mega[p] if p in holders else self.nonm[p])
                rng.shuffle(builds)
                chosen = next((b for b in builds if _item_of(b) not in used_items), None)
                if chosen is None: ok = False; break
                party[p] = chosen; used_items.add(_item_of(chosen))
            if ok:
                return [party[p] for p in picked]
        return None

    def _traits(self, name, mega=False):
        """種→(遅いエースか, あまごい受け手か)。トリル/雨の始動技ペイオフ判定用・キャッシュ。
        メガ前提の種はメガ後の素早さ/火力/特性で判定（例: メガメタグロスはS110＝遅いエースではない）。"""
        cache = self.__dict__.setdefault("_traits_cache", {})
        if (name, mega) in cache: return cache[(name, mega)]
        if "_L" not in self.__dict__:
            try:
                from simulator.simulate import get_loader
                self._L = get_loader()
            except Exception:
                self._L = None
        slow_ace = rain = False
        try:
            t = self._L.get_pokemon_template(name)
            spd, atk, spa = t.base_speed, t.base_attack, t.base_sp_attack
            t1, t2 = t.type1, t.type2
            abils = {a for a, _ in (t.top_abilities or [])}
            md = list((t.mega_data or {}).values())
            if mega and md:
                m = md[0]
                spd, atk, spa, t1, t2, abils = m.speed, m.attack, m.sp_attack, m.type1, m.type2, {m.ability}
            off = max(atk, spa)
            slow_ace = spd <= 70 and off >= 110
            rain = "すいすい" in abils   # あまごいのペイオフ＝速度操作。みず1.5倍は始動1ターンの理由にならない
        except Exception:
            pass
        cache[(name, mega)] = (slow_ace, rain); return cache[(name, mega)]

    def _mvw(self, name, build):
        """型の4技の実使用率（template top_moves）の幾何平均。人間が実際に使う技構成を優先
        （例: ミミッキュのトリックルーム=技使用率3.4% → トリル型の選択頻度が実態12%程度に寄る）。"""
        cache = self.__dict__.setdefault("_mvw_cache", {})
        if build in cache: return cache[build]
        if "_L" not in self.__dict__:
            try:
                from simulator.simulate import get_loader
                self._L = get_loader()
            except Exception:
                self._L = None
        w = 1.0
        try:
            tm = dict(self._L.get_pokemon_template(name).top_moves or [])
            rates = [max(1.0, tm.get(m, 1.0)) for m in _moves_of(build)]
            w = (math.prod(rates) ** (1.0 / len(rates)) / 100.0) ** MV_POW
        except Exception:
            pass
        cache[build] = w; return w

    def _role_builds(self, picked, holders, rng, tries=120, targets=None, fixed=None):
        """役割目標を満たすよう型を選ぶ。持ち物は全相異。best-effort。
        fixed={種キー: spec} を渡すとその枠は指定specをそのまま採用（軸指定コア用）。
        低使用率メガ軸（pg.megaに型が無い＝mega_allのみ）でも生成できるほか、
        固定枠の持ち物・役割が重複判定/役割カウントに正しく反映される。"""
        targets = targets or sample_role_targets(rng)
        best = None; best_score = -1
        # チーム文脈のペイオフ判定（種族依存＝triesで不変）。始動技が活きる受け手が居ないパーティでは
        # その型を選ばない（例: 遅いエース不在のトリックルーム、あまごい受け手不在のあまごい＝死に技回避）
        has_slow_ace = any(self._traits(q, q in holders)[0] for q in picked)
        has_rain = any(self._traits(q, q in holders)[1] for q in picked)
        def payoff(b):
            mv = _moves_of(b)
            if "トリックルーム" in mv and not has_slow_ace: return 0.0
            if "あまごい" in mv and not has_rain: return 0.0
            return 1.0
        for _ in range(tries):
            order = list(picked); rng.shuffle(order)
            party = {}; used_items = set(); need = dict(targets); ok = True
            for p in order:
                fb = (fixed or {}).get(p)
                if fb is not None:
                    if _item_of(fb) in used_items: ok = False; break
                    party[p] = fb; used_items.add(_item_of(fb))
                    for t in self.build_roles.get(fb, ()):
                        if need.get(t, 0) > 0: need[t] -= 1
                    continue
                builds = [b for b in (self.mega[p] if p in holders else self.nonm[p]) if _item_of(b) not in used_items]
                if not builds: ok = False; break
                def gain(b):
                    return sum(1 for t in self.build_roles.get(b, ()) if need.get(t, 0) > 0)
                iu = self.item_usage.get(p, {})
                # 持ち物使用率×技使用率を主・役割充足を従に重み付け・ペイオフ不在の始動技はゼロ重み
                wts = [(iu.get(_item_of(b), 0) + 1) * self._mvw(p, b) * (1 + ROLE_W * gain(b)) * payoff(b) for b in builds]
                if sum(wts) <= 0: wts = [(iu.get(_item_of(b), 0) + 1) * self._mvw(p, b) * (1 + ROLE_W * gain(b)) for b in builds]   # 全滅回避
                chosen = rng.choices(builds, weights=wts, k=1)[0]
                party[p] = chosen; used_items.add(_item_of(chosen))
                for t in self.build_roles.get(chosen, ()):
                    if need.get(t, 0) > 0: need[t] -= 1
            if not ok: continue
            roles = sum(targets[t] - max(0, need[t]) for t in targets)   # 満たした役割数
            # 使用率項＝持ち物×技構成（技を無視すると120試行のargmaxが人気持ち物の低使用率技型を系統選択してしまう）。
            # +30フロア: 持ち物使用率が低くても技構成が標準的な型が役割枠を競えるように（トリル型が唯一のbulk供給になるのを防ぐ）
            usage = sum((self.item_usage.get(p, {}).get(_item_of(party[p]), 0) + IU_FLOOR) * self._mvw(p, party[p]) for p in picked) / 100.0
            score = roles + ITEM_USAGE_W * usage                          # 役割充足＋使用率
            if score > best_score:
                best_score = score; best = [party[p] for p in picked]
                if score == sum(targets.values()): break
        return best

    def mutate_cooc(self, party, rng, nslots=None):
        """既存パーティのk枠を、残りと同居しやすい種へ差し替え→役割型で組み直す（1〜2メガ維持）。"""
        sp = [s.split("@")[0] for s in party]
        keys = [self.keyof(s) or sp[i] for i, s in enumerate(party)]
        k = nslots or rng.choice([1, 1, 2])
        idxs = rng.sample(range(6), k)
        keep = [keys[i] for i in range(6) if i not in idxs]
        used_dex = {self.dex.get(x) for x in keep}
        picked = list(keep)
        for _ in idxs:
            cands = []; ws = []
            for p in self.pokes:
                if self.dex.get(p) in used_dex: continue
                cs = sum(self.cooc.get(q, {}).get(p, 0) + self.cooc.get(p, {}).get(q, 0) for q in picked)
                cands.append(p); ws.append(self.w[p] * (1 + 4.0 * cs))
            if not cands: return None
            nxt = rng.choices(cands, weights=ws, k=1)[0]
            picked.append(nxt); used_dex.add(self.dex.get(nxt))
        megas = sum(_spec_mega(s) for s in party)
        if megas not in (1, 2): megas = 2
        holders = self._pick_holders(picked, megas, rng)
        if holders is None:
            holders = self._pick_holders(picked, 2, rng) or self._pick_holders(picked, 1, rng)
        if holders is None: return None
        tgt = dict(_ROLE_TARGET)
        if rng.random() < 0.65: tgt["scarf"] = 1
        party2 = self._role_builds(picked, holders, rng, targets=tgt)
        return party2 if (party2 and self.is_legal(party2, megas_set=(1, 2))) else None

    def fix_items(self, party, rng):
        """6specの持ち物を全て相異なるよう、同種内で型を差し替えて修復。無理なら None。"""
        picked = [self.keyof(s) for s in party]
        if any(k is None for k in picked) or len(set(picked)) != 6:
            return None
        holders = {picked[i] for i, s in enumerate(party) if _spec_mega(s)}
        return self._distinct_builds(picked, holders, rng)

    def is_legal(self, party, megas=2, megas_set=None):
        """合法性: 6体・図鑑番号全相異(リージョン/性別違いも重複NG)・メガ数(既定ちょうど2, megas_setで許容集合指定)・持ち物全相異。"""
        if len(party) != 6: return False
        if len({self.dexof(s) for s in party}) != 6: return False
        nmega = sum(_spec_mega(s) for s in party)
        if megas_set is not None:
            if nmega not in megas_set: return False
        elif nmega != megas:
            return False
        if len({_item_of(s) for s in party}) != 6: return False
        return True

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    pg = PartyGen()
    print(f"プール {len(pg.pokes)}種 / 型合計 {sum(len(v) for v in pg.pool.values())}  "
          f"メガ可能種={sum(1 for p in pg.pokes if pg.mega[p])}  RANK_EXP={RANK_EXP}")
    rng = random.Random(1)
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader()
    cnt = collections.Counter(); dup = mega_bad = none_cnt = 0; fail = []
    for _ in range(N):
        party = pg.sample(rng)
        if party is None: none_cnt += 1; continue
        names = [s.split("@")[0] for s in party]
        if len(set(names)) != len(names): dup += 1
        if sum(_spec_mega(s) for s in party) != 2: mega_bad += 1
        for s in party:
            cnt[s.split("@")[0]] += 1
            try: build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False)
            except Exception as e:
                if len(fail) < 8: fail.append((s[:46], str(e)[:46]))
    print(f"検証 {N}体: 重複種={dup} メガ≠2={mega_bad} 生成失敗={none_cnt} ビルド失敗={len(fail)}")
    for s, e in fail: print("  FAIL", s, e)
    print("種出現TOP15 (rank / 重み):")
    for nm, c in cnt.most_common(15):
        print(f"  {nm:<18} {c}回  rank{pg.rank.get(nm,'?')}  w={pg.w.get(nm,0):.3f}")

if __name__ == "__main__":
    main()
