"""本番選出(learned_select_party)が受けポケモンを過小選出しているか測定。
各M-1パーティ(6体)を相手とペアにして3体選出させ、種族ごとに『6体中にいる時の選出率』を集計。
種族を防御寄り/攻撃寄りに分類し、選出率を比較する。
"""
import os, json, glob, random, collections
os.environ.setdefault("OMP_NUM_THREADS", "1")

SEASON = "M-3"; N = int(os.environ.get("N", "400"))

def main():
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    L = get_loader()
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    rng = random.Random(3)

    def base_role(name):
        tpl = L.get_pokemon_template(name)
        if tpl is None: return None, 0
        bulk = tpl.base_hp + tpl.base_defense + tpl.base_sp_defense
        off = max(tpl.base_attack, tpl.base_sp_attack)
        ratio = bulk / max(1, off)
        role = "受け" if ratio >= 2.0 else ("攻め" if ratio <= 1.3 else "中間")
        return role, ratio

    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    present = collections.Counter(); selected = collections.Counter()
    for _ in range(N):
        a, b = rng.sample(range(len(parties)), 2)
        A = team(parties[a]); B = team(parties[b])
        sa = learned_select_party(A, B, L, n=3, temperature=0.3, rng=rng)
        for p in A: present[p.name] += 1
        for p in sa: selected[p.name] += 1
    rows = []
    for nm, pc in present.items():
        if pc < 8: continue
        rate = selected[nm] / pc
        role, ratio = base_role(nm)
        rows.append((nm, role, ratio, pc, selected[nm], rate))
    # 役割別の集計（present重み付き平均選出率）
    agg = collections.defaultdict(lambda: [0, 0])
    for nm, role, ratio, pc, sc, rate in rows:
        if role: agg[role][0] += sc; agg[role][1] += pc
    print(f"=== 役割別 選出率（6体中にいる時に選ばれる割合） N={N}ペア ===")
    for role in ("受け", "中間", "攻め"):
        sc, pc = agg[role]
        if pc: print(f"  {role}: {sc*100/pc:.1f}%  (選出{sc}/在籍{pc})")
    print("\n=== 受け系個別（選出率の低い順） ===")
    for nm, role, ratio, pc, sc, rate in sorted([r for r in rows if r[1] == "受け"], key=lambda r: r[5]):
        print(f"  {nm:<16} bulk/off={ratio:.1f} 在籍{pc} 選出{sc} → {rate*100:.0f}%")
    print("\n=== 攻め系で選出率の高い順 TOP10 ===")
    for nm, role, ratio, pc, sc, rate in sorted([r for r in rows if r[1] == "攻め"], key=lambda r: -r[5])[:10]:
        print(f"  {nm:<16} bulk/off={ratio:.1f} 在籍{pc} 選出{sc} → {rate*100:.0f}%")

if __name__ == "__main__":
    main()
