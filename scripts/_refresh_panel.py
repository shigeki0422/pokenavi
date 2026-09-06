"""使用率順位が変わったときだけ、提案キャッシュの「順位依存の部分」を作り直す。

提案キャッシュを全部作り直すと数時間かかるが、その大半は必然性修復
（死に枠の差し替え＝pick_rate測定）で、これは使用率順位と無関係。
順位が変わって古くなるのは次の4つだけで、提案するパーティ自体は変わらない。

  matchup  … 相手パネル（使用率上位30体）に対する相性グリッド
  coverage … 脅威カバー率（脅威リスト＝使用率上位N体）
  stats    … パーティ統計（脅威依存の項目を含む）
  details  … タイプ相性等の内訳（同上）

実測では上位30の顔ぶれは14日間変化なし・順位変動も最大1位だったので、
毎日回す必要はない。指紋（顔ぶれと順位）を保存し、変化したときだけ実行する。

  python _refresh_panel.py                 # 変化が無ければ何もしない
  FORCE=1 python _refresh_panel.py         # 変化の有無によらず実行
  IN=... OUT=... python _refresh_panel.py

env: IN(suggest_cache.json) OUT(=IN) FP(panel_fingerprint.json) FORCE(0)
"""
import json
import os
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", "1")

D = os.path.dirname(os.path.abspath(__file__))
IN = os.environ.get("IN", os.path.join(D, "suggest_cache.json"))
OUT = os.environ.get("OUT", IN)
FP = os.environ.get("FP", os.path.join(D, "panel_fingerprint.json"))
FORCE = os.environ.get("FORCE", "0") == "1"


def fingerprint():
    """相手パネルと脅威リストの中身。これが同じなら作り直す必要はない。"""
    import _explain as EX
    import product3_server as S
    from _threat_coverage import load_threats
    panel = [nm for nm, _ in EX.load_top_builds(S.L)]
    threats = [t["name"] if isinstance(t, dict) else t[0] for t in load_threats(S.L)]
    return {"season": EX.USAGE_SEASON, "panel": panel, "threats": threats}


def main() -> None:
    t0 = time.time()
    import product3_server as S
    import _explain as EX
    from _threat_coverage import team_coverage

    fp = fingerprint()
    old = json.load(open(FP, encoding="utf-8")) if os.path.exists(FP) else None
    if old == fp and not FORCE:
        print("相手パネル・脅威リストに変化なし。作り直しは不要")
        return
    if old:
        add = [x for x in fp["panel"] if x not in old["panel"]]
        rm = [x for x in old["panel"] if x not in fp["panel"]]
        print(f"パネルの変化: 追加{add or 'なし'} / 除外{rm or 'なし'}")

    cache = json.load(open(IN, encoding="utf-8"))
    n_ent = n_res = 0
    for ent in cache.values():
        n_ent += 1
        for r in ent.get("results", []):
            specs = r.get("specs")
            if not specs:
                continue
            # 順位に依存する4項目だけ差し替える。specs/mons/archetypes/speed は触らない
            r["matchup"] = EX.matchup_grid(specs, S.L)
            r["coverage"] = round(team_coverage(specs, S.L, S.TH)[0], 2)
            r["stats"] = EX.party_stats(specs, S.L, S.PG, S.TH)
            r["details"] = EX.stat_details(specs, S.L, S.TH)
            n_res += 1
    json.dump(cache, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(fp, open(FP, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"{OUT}: {n_ent}軸 {n_res}提案の順位依存部分を作り直した / {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
