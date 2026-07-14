"""Product3 ローカル製品：コア入力→残り枠補完→サロゲート提案。
モデル常駐のHTTPサーバ＋簡易UI。 起動: venv/bin/python product3_server.py  → http://localhost:8899
"""
import os, json, random, html, glob, threading, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", os.environ.get("SIM_SIMS", "150"))   # ライブ実戦テストのMCTS探索数（軽め）
import multiprocessing as mp
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import feature1 as _f1
from gen_party_pool import PartyGen, _spec_mega, _item_of
from _threat_coverage import load_threats, team_coverage
import _product3 as P3
from _product3_complete import complete_core, resolve_fixed, complete_core_free
from _ensemble_surrogate import EnsembleScorer
from simulator.pokemon import build_from_spec, parse_pokemon_spec
import _explain as EX

PORT = int(os.environ.get("PORT", "8899"))
EVK = ["H", "A", "B", "C", "D", "S"]

print("モデル読込中...", flush=True)
_f1._ensure_loaded("M-3", 8)
L = _f1._W["loader"]; NET = _f1._W["net"]
PG = PartyGen(); TH = load_threats(L)
ENS = EnsembleScorer(L, NET, PG, TH)   # アンサンブル(ネット+リッチ守備+構築, CV r≈0.69)
SPECIES = [p for p, _ in sorted(PG.rank.items(), key=lambda x: x[1]) if p in PG.pokes]

_CALIB = None
try:
    _cf = os.path.join(os.path.dirname(__file__), "calib_net.json")
    _cd = json.load(open(_cf, encoding="utf-8")); _CALIB = (_cd["x"], _cd["y"])
    print(f"較正ロード: {len(_CALIB[0])}点（生評価→実勝率）", flush=True)
except FileNotFoundError:
    pass

def calibrate(v):
    """価値ネットの生評価を総当たり実勝率にキャリブレーション（単調線形補間）。"""
    if not _CALIB: return v
    xs, ys = _CALIB
    if v <= xs[0]: return ys[0]
    if v >= xs[-1]: return ys[-1]
    for i in range(1, len(xs)):
        if v <= xs[i]:
            t = (v - xs[i - 1]) / (xs[i] - xs[i - 1] or 1)
            return ys[i - 1] + t * (ys[i] - ys[i - 1])
    return ys[-1]

_ARCH_FILE = os.path.join(os.path.dirname(__file__), "archetypes_m3.json")

def _scan_archetypes(n=8):
    """総当たり実勝率(5.5GB)から、メガ軸が重複しない代表アーキタイプをn個抽出（devのみ）。"""
    files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "f1_cache_m3/*.json")))
    rows = []
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        w = sum(c.get("wins", 0) for c in d["cards"]); l = sum(c.get("losses", 0) for c in d["cards"])
        rows.append((w / max(1, w + l), d["subject_party"]))
    rows.sort(key=lambda x: -x[0])
    picked, sigs = [], set()
    for wr, p in rows:
        names = [s.split("@")[0] for s in p]
        megas = tuple(sorted(nm for nm, s in zip(names, p) if _spec_mega(s)))
        if megas in sigs: continue
        sigs.add(megas)
        label = ("＋".join(megas) + "軸") if megas else (names[0] + "軸")
        picked.append({"party": p, "names": names, "label": label, "wr": round(wr, 3)})
        if len(picked) >= n: break
    return picked

def _load_archetypes(n=8):
    """事前計算した小さなJSONを優先ロード。無ければ5.5GBを走査してキャッシュ生成（本番は前者のみ）。"""
    if os.path.exists(_ARCH_FILE):
        meta = json.load(open(_ARCH_FILE, encoding="utf-8"))[:n]
    else:
        meta = _scan_archetypes(n)
        json.dump(meta, open(_ARCH_FILE, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"アーキタイプを {os.path.basename(_ARCH_FILE)} に事前計算保存", flush=True)
    for a in meta:
        a["built"] = [build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False) for s in a["party"]]
    return meta

ARCHES = _load_archetypes(8)
print(f"アーキタイプ盤面 {len(ARCHES)}個: {[a['label'] for a in ARCHES]}", flush=True)

def _xy_suffix(stone):
    if stone.endswith(("X", "Ｘ")): return "X"
    if stone.endswith(("Y", "Ｙ")): return "Y"
    return ""

def _variants(sp):
    """種の選べる型。メガは『メガ○○』(X/Y付き)、非メガ型があれば素の種名も。メガ前提種はメガのみ。
    低使用率メガ(実使用率<MIN_MEGA_USAGE%)はPartyGen側で既にpg.mega/pg.poolから除外済みなので、
    ここではpg.poolの中身をそのまま見ればよい。"""
    blds = PG.pool.get(sp) or []
    stones, has_nm = [], False
    for s in blds:
        if _spec_mega(s):
            st = _item_of(s)
            if st not in stones: stones.append(st)
        else:
            has_nm = True
    opts = [{"label": f"メガ{sp}{_xy_suffix(st)}", "sp": sp, "mega": st} for st in stones]
    if has_nm:
        opts.append({"label": sp, "sp": sp, "mega": ""})
    if not opts:
        opts.append({"label": sp, "sp": sp, "mega": None})
    return opts

VARIANTS = []
for sp in SPECIES:
    rk = PG.rank.get(sp, 9999)
    for v in _variants(sp):
        v["rank"] = rk
        VARIANTS.append(v)
print(f"準備完了。種{len(SPECIES)} 選択肢{len(VARIANTS)} / http://localhost:{PORT}", flush=True)

def _cpu_avail():
    try:
        return len(os.sched_getaffinity(0))   # cgroup/affinity準拠（コンテナのCPU割当を尊重）
    except (AttributeError, OSError):
        return os.cpu_count() or 2

# WORKERS env 優先。無ければ割当CPU-1（コンテナでは os.cpu_count がホスト全コアを返しがちなので affinity 基準）
_WORKERS = int(os.environ.get("WORKERS") or 0) or max(1, _cpu_avail() - 1)
print(f"並列ワーカー数 _WORKERS={_WORKERS} (cpu_avail={_cpu_avail()}, cpu_count={os.cpu_count()})", flush=True)
_POOL = None

def _get_pool():
    """永続forkプール（起動後モデル込みで1回だけfork→毎リクエストのfork overheadを回避）。
    重い処理は _HEAVY_LOCK で直列化されるため単一プールの共有で安全。"""
    global _POOL
    if _POOL is None:
        _POOL = mp.get_context("fork").Pool(_WORKERS)
    return _POOL

def _score_one(spec):
    return (ENS.score(spec), spec)

def _par_score(cands):
    """候補のENSスコアをCPU並列で計算（fork継承でネットは共有・ピクル不要）。"""
    if len(cands) < 8:
        return [_score_one(p) for p in cands]
    return _get_pool().map(_score_one, cands, chunksize=4)

# メガ数較正は実測A/Bで不採用（2026-07-12）: 候補プールは実119構築の2メガ率84%とほぼ一致[82-91%]なのに
# ENS順位のtop5では約54%まで下がる。層化選出(2メガ84%へ強制)を実装し検証したが、
# 実対戦A/B 43.5%(20-26/48)で有意に敗北＝「実プレイヤーの構成比に寄せる」ことは強さの改善にならず、
# 総当たり実勝率データ(1メガ0.502/2メガ0.495・ほぼ拮抗)と整合。ENSのtop5選好は測定として正しい。
# 教訓: 母集団分布との一致は目的ではなく手段。効果は必ず実対戦A/Bで確認してから採用する。

def _proposal_detail(args):
    """1提案ぶんの詳細（役割・想定勝率・相性・統計）を組み立てる。fork並列用にモジュール関数化。"""
    sc, p, fixnames = args
    mons = []
    for s in p:
        hd, rest = s.split("@", 1); it, na, mv, ev, ab = rest.split(":")
        evs = " ".join(f"{k}{v}" for k, v in zip(EVK, ev.split("/")) if v != "0")
        mons.append({"name": hd, "item": it, "nature": na, "ability": ab, "ev": evs,
                     "moves": mv.split("|"), "mega": _spec_mega(s), "core": hd in fixnames,
                     "roles": EX.role_of(s, L)})
    arch = []
    for a in ARCHES:
        v, pick = P3.eval_vs_built(p, a["built"])
        arch.append({"label": a["label"], "opp": a["names"], "wr": a["wr"],
                     "adv": round(calibrate(v), 4), "pick": pick})
    return {"score": round(sc, 3), "coverage": round(team_coverage(p, L, TH)[0], 2),
            "specs": p, "mons": mons, "stats": EX.party_stats(p, L, PG, TH), "matchup": EX.matchup_grid(p, L),
            "details": EX.stat_details(p, L, TH), "archetypes": arch,
            "speed": EX.speed_info(p, L)}

_SCACHE = {}   # 提案は決定的（固定シード＋温度0の貪欲選出）なので軸ごとに結果をキャッシュ
_SCACHE_FILE = os.path.join(os.path.dirname(__file__), "suggest_cache.json")
try:
    for _k, _v in json.load(open(_SCACHE_FILE, encoding="utf-8")).items():
        _SCACHE[_k] = _v
    print(f"提案キャッシュ事前ロード: {len(_SCACHE)}件（人気軸）", flush=True)
except FileNotFoundError:
    pass

# 選出ガイド（バッチが焼き上げ済みのコアのみ・全240コア完了前でも計算済み分から段階的に同梱可）。
# ファイルが無ければ何もしない＝未焼成コアは従来通りguide/strategyキー無し（UIは「準備中」表示）。
_SGUIDE_FILE = os.path.join(os.path.dirname(__file__), "suggest_cache_guided_s.json")
try:
    _n_guided = 0
    for _k, _v in json.load(open(_SGUIDE_FILE, encoding="utf-8")).items():
        _SCACHE[_k] = _v; _n_guided += 1
    print(f"選出ガイドオーバーレイ: {_n_guided}件", flush=True)
except FileNotFoundError:
    pass

def suggest(core_args, ncand, top):
    fixed = resolve_fixed(PG, core_args)
    ck = json.dumps([fixed, ncand, top], ensure_ascii=False)   # 解決後specでキー化（入力形式に非依存）
    hit = _SCACHE.get(ck)
    if hit is not None:
        return hit                      # 同一軸は即時返却（重い計算をスキップ）
    # キャッシュミス＝事前計算済み241軸に無い組み合わせ（未収録種 or 複数コア指定等）。
    # 必然性修復はコスト上ライブ計算に組み込めないため、後日オフラインでキャッシュへ追加できるよう
    # Cloud Logging（標準stdout）に構造化ログを残すのみ（追加インフラ不要・$0）。
    print(f"CACHE_MISS {json.dumps({'fixed': fixed, 'ncand': ncand, 'top': top}, ensure_ascii=False)}", flush=True)
    rng = random.Random(0)
    _t = time.time(); cands = complete_core(PG, L, TH, fixed, rng, ncand); tg = time.time() - _t
    _t = time.time(); scored = sorted(_par_score(cands), key=lambda x: -x[0])[:top]; ts = time.time() - _t
    fixnames = [f.split("@")[0] for f in fixed]
    jobs = [(sc, p, fixnames) for sc, p in scored]
    _t = time.time(); out = _get_pool().map(_proposal_detail, jobs); td = time.time() - _t   # 提案ごとに並列（永続プール）
    print(f"[suggest] gen={tg:.2f}s score={ts:.2f}s detail={td:.2f}s workers={_WORKERS}", flush=True)
    res = {"fixed": fixnames, "results": out, "opps": [{"label": a["label"], "wr": a["wr"]} for a in ARCHES]}
    _SCACHE[ck] = res
    return res

COMPLETE_NCAND = int(os.environ.get("COMPLETE_NCAND", "50"))   # /complete の補完候補数（応答時間と品質のトレードオフ。fill=1/5実測: 総 4-9秒 <<20秒目標）

def complete(specs, fill, top, ncand=None):
    """型(spec)固定メンバー(specs、型プール非所属可)から残りfill体を補完し、上位topを返す。
    返却specsは追加分のみ（固定分は含まない）。決定的（固定シード）。"""
    ncand = ncand or COMPLETE_NCAND
    fixed = list(specs)
    for s in fixed:
        parse_pokemon_spec(s)   # 形式検証。不正なら例外→呼び出し側でエラー応答
    rng = random.Random(0)
    cands = complete_core_free(PG, L, TH, fixed, rng, ncand)
    if not cands:
        return {"results": []}
    scored = sorted(_par_score(cands), key=lambda x: -x[0])[:top]
    nfixed = len(fixed)
    out = [{"specs": p[nfixed:nfixed + fill], "score": round(sc, 3)} for sc, p in scored]
    return {"results": out}

def simulate(specs, opp_idx, k):
    if not (0 <= opp_idx < len(ARCHES)): return {"error": "相手が不正"}
    opp = ARCHES[opp_idx]
    jobs = [(specs, opp["party"], (1234 + i * 97 + 13) & 0x7fffffff) for i in range(k)]
    workers = max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(workers) as pool:
        res = pool.map(P3._play_winner, jobs, chunksize=1)
    w = sum(1 for r in res if r == 1); l = sum(1 for r in res if r == 2); dr = sum(1 for r in res if r == 0)
    dec = w + l
    return {"label": opp["label"], "wins": w, "losses": l, "draws": dr, "k": k,
            "wr": round(w / dec, 3) if dec else 0.5}

PAGE = """<!doctype html><html lang=ja><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>M-3 パーティ提案（Product3）</title><style>
body{font-family:system-ui,'Hiragino Kaku Gothic ProN',sans-serif;max-width:920px;margin:0 auto;padding:16px;background:#f6f7f9;color:#1f2937}
h1{font-size:1.25rem} .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:12px 0}
input,select,button{font-size:1rem;padding:8px 10px;border:1px solid #cbd5e1;border-radius:8px}
button{background:#2563eb;color:#fff;border:0;cursor:pointer} button:disabled{opacity:.5}
.chip{background:#e0e7ff;border-radius:999px;padding:4px 10px;font-size:.85rem}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:12px;margin:12px 0;box-shadow:0 1px 2px rgba(0,0,0,.04)}
.hd{display:flex;justify-content:space-between;align-items:center;font-weight:700}
table{width:100%;border-collapse:collapse;margin-top:8px;font-size:.82rem}
td,th{border-bottom:1px solid #eef2f7;padding:4px 6px;text-align:left;vertical-align:top}
.core{background:#fff7ed} .mega{color:#b45309;font-weight:700}
.muted{color:#6b7280;font-size:.85rem} .sc{color:#2563eb;font-weight:700}
.role{display:inline-block;background:#eef2ff;color:#3730a3;border-radius:6px;padding:1px 6px;font-size:.72rem;margin-right:3px}
.stats{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0;font-size:.8rem}
.stats span{background:#f1f5f9;border-radius:6px;padding:3px 8px}
.mg{font-size:.72rem;margin-top:6px;overflow-x:auto}
.mg table{min-width:640px} .mg td,.mg th{text-align:center;padding:2px 3px;border:1px solid #eef2f7}
.v◎{background:#bbf7d0} .vmark-good{background:#bbf7d0}
.cc{font-weight:700}
</style></head><body>
<h1>M-3 パーティ提案 <span class=muted>コアを固定→残り枠をAIが補完・強い順に提案</span></h1>
<div class=row>
 <input id=core placeholder="コア(カンマ区切り 例: サザンドラ,メタグロス)" style="flex:1;min-width:260px" list=splist>
 <datalist id=splist></datalist>
 <label class=muted>候補 <input id=nc type=number value=120 style="width:70px"></label>
 <label class=muted>提案数 <input id=tp type=number value=5 style="width:60px"></label>
 <button id=go onclick=run()>提案する</button>
</div>
<div id=status class=muted></div><div id=out></div>
<script>
fetch('/species').then(r=>r.json()).then(d=>{document.getElementById('splist').innerHTML=d.map(s=>`<option value="${s}">`).join('')});
async function run(){
 const core=document.getElementById('core').value.split(',').map(s=>s.trim()).filter(Boolean);
 if(!core.length){alert('コアを入力');return}
 const go=document.getElementById('go');go.disabled=true;
 document.getElementById('status').textContent='生成・評価中…（数〜十数秒）';document.getElementById('out').innerHTML='';
 try{
  const r=await fetch('/suggest',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({core,ncand:+document.getElementById('nc').value,top:+document.getElementById('tp').value})});
  const d=await r.json();
  if(d.error){document.getElementById('status').textContent='エラー: '+d.error;go.disabled=false;return}
  document.getElementById('status').textContent=`固定コア: ${d.fixed.join(' + ')} / ${d.results.length}件`;
  document.getElementById('out').innerHTML=d.results.map((res,i)=>{
   const rows=res.mons.map(m=>`<tr class="${m.core?'core':''}"><td>${m.core?'◆':(m.mega?'<span class=mega>★</span>':'')}${m.name}<br>${(m.roles||[]).map(r=>`<span class=role>${r}</span>`).join('')}</td><td>${m.item}</td><td>${m.nature}</td><td>${m.ability}</td><td>${m.ev}</td><td>${m.moves.join(' / ')}</td></tr>`).join('');
   const st=res.stats?('<div class=stats>'+Object.entries(res.stats).map(([k,v])=>`<span><b>${k}</b> ${v}</span>`).join('')+'</div>'):'';
   const col=c=>({'◎':'#16a34a','○':'#65a30d','△':'#6b7280','▲':'#ea580c','×':'#dc2626'}[c]||'#6b7280');
   let mg='';
   if(res.matchup){
     const th='<tr><th>自分＼相手</th>'+res.matchup.tops.map(t=>`<th>${t}</th>`).join('')+'</tr>';
     const mr=res.matchup.rows.map(r=>`<tr><td style="text-align:left">${r.mon}</td>`+r.cells.map(c=>`<td class=cc style="color:${col(c)}">${c}</td>`).join('')+'</tr>').join('');
     mg=`<div class=mg><div class=muted>1v1 相性（使用率上位）　◎有利 ○やや有利 △五分 ▲やや不利 ×不利</div><table>${th}${mr}</table></div>`;
   }
   return `<div class=card><div class=hd><span>提案 ${i+1}</span><span><span class=sc>スコア ${res.score}</span> ・ 脅威対応 ${Math.round(res.coverage*100)}%</span></div>
   ${st}<table><tr><th>ポケモン / 役割</th><th>持ち物</th><th>性格</th><th>特性</th><th>EV</th><th>技</th></tr>${rows}</table>${mg}</div>`;
  }).join('');
 }catch(e){document.getElementById('status').textContent='通信エラー: '+e}
 go.disabled=false;
}
</script></body></html>"""

ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")   # 本番は https://pokenavi.jp を推奨
MIN_INTERVAL = float(os.environ.get("MIN_INTERVAL", "0"))  # 同一IPの重い処理の最短間隔(秒)。0で無効
_HEAVY_LOCK = threading.Lock()                       # 重い計算の同時実行を1本に直列化（CPU保護）
_LAST_HIT = {}                                       # ip -> 直近の重い処理時刻
_HEAVY = ("/suggest", "/simulate", "/complete")
MAX_BODY_BYTES = int(os.environ.get("MAX_BODY_BYTES", 16 * 1024))  # POSTボディ上限(既定16KB)。超過は413
MAX_SPEC_LEN = 500                                   # /complete の specs 1本あたりの文字数上限

class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        b = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code); self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", ALLOW_ORIGIN)
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def _client_ip(self):
        xff = self.headers.get("Fly-Client-IP") or self.headers.get("X-Forwarded-For", "")
        return (xff.split(",")[0].strip() if xff else self.client_address[0])

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", ALLOW_ORIGIN)
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

    def log_message(self, *a): pass

    def do_GET(self):
        if self.path == "/" or self.path == "/health":
            self._send(200, "ok" if self.path == "/health" else PAGE, "text/plain" if self.path == "/health" else "text/html")
        elif self.path == "/species":
            self._send(200, json.dumps(VARIANTS, ensure_ascii=False))
        else:
            self._send(404, "{}")

    def do_POST(self):
        if self.path not in ("/suggest", "/simulate", "/complete", "/fire_detail", "/speed_detail", "/matchup_detail", "/atk_detail", "/guide_request"):
            self._send(404, "{}"); return
        try:
            n = int(self.headers.get("Content-Length", 0) or 0)
        except ValueError:
            n = 0
        if n > MAX_BODY_BYTES:
            self._send(413, json.dumps({"error": f"リクエストボディが大きすぎます（上限{MAX_BODY_BYTES}バイト）"}, ensure_ascii=False)); return
        if MIN_INTERVAL and self.path in _HEAVY:
            ip = self._client_ip(); now = time.time()
            if now - _LAST_HIT.get(ip, 0) < MIN_INTERVAL:
                self._send(429, json.dumps({"error": "リクエストが多すぎます。少し待って再試行してください。"}, ensure_ascii=False)); return
            _LAST_HIT[ip] = now
        try:
            req = json.loads(self.rfile.read(n) or "{}")
            if self.path == "/guide_request":
                core = req.get("core") or []
                if not isinstance(core, list) or len(core) > 6:
                    self._send(200, json.dumps({"error": "invalid"}, ensure_ascii=False)); return
                safe = []
                for a in core[:6]:
                    if isinstance(a, dict):
                        safe.append({"sp": str(a.get("sp", ""))[:30], "mega": (None if a.get("mega") is None else str(a.get("mega"))[:30])})
                    else:
                        safe.append(str(a)[:120])
                print("[GUIDE_REQUEST] " + json.dumps({"core": safe, "ip": self._client_ip()}, ensure_ascii=False), flush=True)
                self._send(200, json.dumps({"ok": True}, ensure_ascii=False)); return
            if self.path == "/atk_detail":
                self._send(200, json.dumps(EX.atk_detail(req.get("specs") or [], req.get("mon", ""), req.get("type", ""), L), ensure_ascii=False)); return
            if self.path in ("/fire_detail", "/speed_detail", "/matchup_detail"):
                fn = {"/fire_detail": EX.fire_detail, "/speed_detail": EX.speed_detail, "/matchup_detail": EX.matchup_detail}[self.path]
                self._send(200, json.dumps(fn(req.get("specs") or [], req.get("mon", ""), req.get("opp", ""), L), ensure_ascii=False)); return
            if self.path == "/simulate":
                specs = req.get("specs") or []
                opp_idx = int(req.get("opp_idx", 0))
                k = min(20, max(2, int(req.get("k", 6))))
                with _HEAVY_LOCK:
                    self._send(200, json.dumps(simulate(specs, opp_idx, k), ensure_ascii=False))
                return
            if self.path == "/complete":
                specs = req.get("specs") or []
                if not isinstance(specs, list) or not all(isinstance(s, str) for s in specs) or len(specs) > 5:
                    self._send(200, json.dumps({"error": "specsは文字列配列（最大5件）で指定してください"}, ensure_ascii=False)); return
                if any(len(s) > MAX_SPEC_LEN for s in specs):
                    self._send(200, json.dumps({"error": f"specの文字数が上限（{MAX_SPEC_LEN}）を超えています"}, ensure_ascii=False)); return
                if any(("@" not in s or len(s.split("@", 1)[1].split(":")) != 5) for s in specs):
                    self._send(200, json.dumps({"error": "spec形式が不正です（種名@持ち物:性格:技1|技2|技3|技4:H/A/B/C/D/S:特性 の完全形式で指定してください）"}, ensure_ascii=False)); return
                fill = int(req.get("fill", 0))
                if not (1 <= fill <= 6 - len(specs)):
                    self._send(200, json.dumps({"error": "fillが不正です（1 <= fill <= 6-specs.length）"}, ensure_ascii=False)); return
                top = min(3, max(1, int(req.get("top", 3))))
                with _HEAVY_LOCK:
                    res = complete(specs, fill, top)
                self._send(200, json.dumps(res, ensure_ascii=False))
                return
            core = req.get("core") or []
            nc = min(300, max(20, int(req.get("ncand", 120))))
            top = min(10, max(1, int(req.get("top", 5))))
            with _HEAVY_LOCK:
                res = suggest(core, nc, top)
            self._send(200, json.dumps(res, ensure_ascii=False))
        except SystemExit as e:
            self._send(200, json.dumps({"error": str(e)}, ensure_ascii=False))
        except Exception as e:
            self._send(200, json.dumps({"error": repr(e)}, ensure_ascii=False))

if __name__ == "__main__":
    HOST = os.environ.get("HOST", "127.0.0.1")   # 本番(コンテナ)は 0.0.0.0
    _get_pool()   # 単スレッドのうちに永続プールをfork（マルチスレッド化後のfork回避）
    print(f"listen {HOST}:{PORT}  CORS={ALLOW_ORIGIN}  rate={MIN_INTERVAL}s", flush=True)
    ThreadingHTTPServer((HOST, PORT), H).serve_forever()
