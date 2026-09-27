"""型プール・系統表の版の解決。どの版を使うかは scripts/pool_versions.json のポインタで持つ。
  page   … 情報ページの想定型・1v1（archetypes.json・public/builder-data）。週次で更新
  season … AI・提案API・共進化・datapack 用のシーズン固定版
版は「シーズン/タグ」（例: M-6/2026-09-27）。実体は _local/ai_work/pools/<シーズン>/<タグ>/<name>.json、
無ければ固定版 _local/ai_work/frozen/<name>_<シーズン>_<タグ>.json（M-6/v41 など従来の置き場所）。"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
POOLS = os.path.join(ROOT, "_local", "ai_work", "pools")
FROZEN = os.path.join(ROOT, "_local", "ai_work", "frozen")
POINTER = os.path.join(HERE, "pool_versions.json")


def pointer(kind):
    return json.load(open(POINTER))[kind]


def set_pointer(kind, version):
    p = json.load(open(POINTER))
    p[kind] = version
    with open(POINTER, "w") as f:
        json.dump(p, f, ensure_ascii=False, indent=1)
        f.write("\n")


def version_dir(version):
    return os.path.join(POOLS, *version.split("/"))


def path(name, version):
    """name: type_pool / type_groups / meta"""
    p = os.path.join(version_dir(version), name + ".json")
    if os.path.exists(p):
        return p
    season, tag = version.split("/")
    return os.path.join(FROZEN, f"{name}_{season}_{tag}.json")


def season_of(version):
    return version.split("/")[0]
