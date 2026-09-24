"""(S10) /species静的JSON化: product3_server.py の /species ハンドラが返すVARIANTSと
同じ形式のJSONを事前生成する。

product3_server.py自体は起動にモデル常駐(feature1のネット/アンサンブル/アーキタイプ)を要するが、
VARIANTSの中身はDBクエリだけのgen_party_pool.PartyGen()から組み立てられるため、重いモデル読込は
不要（実測0.1秒未満）。product3_server.pyは変更せず、_variants()/VARIANTS組み立てロジックだけを
ここに複製する（ロジックが乖離したら手動で追従させる）。

使い方: venv/bin/python export_species_json.py [出力先パス]
既定の出力先は public/suggest-data/species.json（工房が使う public/builder-data/ とは別名にして衝突を避ける）。
POOL_SEASON環境変数で対象シーズンを切り替える(既定M-6＝本番Cloud RunのPOOL_SEASONと同じ)。
gen_party_pool.py自体の既定はM-3のままなので、ここで明示的にM-6を既定にしないと、この
静的JSONだけ古いシーズンのまま取り残される（過去に本体のbuilder-dataで実際に起きた事故と同種）。
シーズン移行時はこの既定値も一緒に更新すること。
"""
import os
import sys
import json

os.environ.setdefault("POOL_SEASON", "M-6")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_party_pool import PartyGen, _spec_mega, _item_of  # noqa: E402


def _xy_suffix(stone):
    # M-6でZストーン（ルカリオナイトZ等）が追加された。Zを拾わないと同名2件が並ぶ（product3_server.pyと同一）。
    for c in ("X", "Y", "Z"):
        if stone.endswith((c, chr(ord(c) - ord("A") + ord("Ａ")))):
            return c
    return ""


def _variants(pg, sp):
    """種の選べる型。メガは『メガ○○』(X/Y付き)、非メガ型があれば素の種名も。メガ前提種はメガのみ。
    product3_server.py:_variants() と同一ロジック。"""
    blds = pg.pool.get(sp) or []
    stones, has_nm = [], False
    for s in blds:
        if _spec_mega(s):
            st = _item_of(s)
            if st not in stones:
                stones.append(st)
        else:
            has_nm = True
    opts = [{"label": f"メガ{sp}{_xy_suffix(st)}", "sp": sp, "mega": st} for st in stones]
    if has_nm:
        opts.append({"label": sp, "sp": sp, "mega": ""})
    if not opts:
        opts.append({"label": sp, "sp": sp, "mega": None})
    return opts


def build_variants():
    pg = PartyGen()
    species = [p for p, _ in sorted(pg.rank.items(), key=lambda x: x[1]) if p in pg.pokes]
    variants = []
    for sp in species:
        rk = pg.rank.get(sp, 9999)
        for v in _variants(pg, sp):
            v["rank"] = rk
            variants.append(v)
    return variants


def main():
    default_out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "public", "suggest-data", "species.json")
    out_path = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(default_out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    variants = build_variants()
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(variants, f, ensure_ascii=False)
    print(f"[export_species_json] {len(variants)}件 -> {out_path}")


if __name__ == "__main__":
    main()
