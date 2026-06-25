import sys, json, pickle

src = sys.argv[1] if len(sys.argv) > 1 else "/tmp/selector3.pkl"
dst = sys.argv[2] if len(sys.argv) > 2 else "simulator/selector_m3.json"
season = sys.argv[3] if len(sys.argv) > 3 else "M-3"

with open(src, "rb") as fh:
    sel = pickle.load(fh)
out = {
    "W1": sel.W1.tolist(), "b1": sel.b1.tolist(),
    "W2": sel.W2.tolist(), "b2": float(sel.b2),
    "dim": int(sel.W1.shape[1]), "hidden": int(sel.W1.shape[0]),
    "season": season, "teacher": "mcts-regret@400-905switch",
}
with open(dst, "w") as fh:
    json.dump(out, fh)
print(f"wrote {dst} dim={out['dim']} hidden={out['hidden']}")
