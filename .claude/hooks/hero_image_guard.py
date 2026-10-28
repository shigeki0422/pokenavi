#!/usr/bin/env python3
"""PreToolUse(Bash): ブログ記事の heroImage 参照先が未コミットのまま git commit されるのを防ぐ。

2026-09-14に、公開コミットで記事本体だけを git add し、heroImage が参照する
src/assets/*.png の追加を忘れたままpushする事故が2回連続で発生した
(カバルドン・アシレーヌ、いずれもCloudflare Pagesのビルド失敗＝デプロイ連続失敗)。
記憶頼みの確認では再発したため、commit実行前に機械的に検査する。
"""
import json
import re
import subprocess
import sys

GIT_COMMIT = re.compile(r"(?:^|&&|;|\|\|)\s*git\s+commit\b")
HERO_LINE = re.compile(r"^\s*heroImage:\s*'([^']+)'", re.MULTILINE)


def deny(reason):
    print(f"[hero_image_guard] 拒否しました。\n{reason}", file=sys.stderr)
    sys.exit(2)


def tracked_or_staged(path):
    """HEADに存在する、またはインデックスにステージ済みなら真。"""
    for args in (["git", "ls-files", "--error-unmatch", path],):
        r = subprocess.run(args, capture_output=True, text=True)
        if r.returncode == 0:
            return True
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    command = payload.get("tool_input", {}).get("command", "")
    if not command or not GIT_COMMIT.search(command):
        sys.exit(0)

    try:
        staged = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True, timeout=10,
        ).stdout.splitlines()
    except Exception:
        sys.exit(0)

    blog_files = [f for f in staged if f.startswith("src/content/blog/") and f.endswith(".md")]
    if not blog_files:
        sys.exit(0)

    missing = []
    for f in blog_files:
        try:
            content = subprocess.run(
                ["cat", f], capture_output=True, text=True, timeout=10,
            ).stdout
        except Exception:
            continue
        m = HERO_LINE.search(content)
        if not m:
            continue
        rel = m.group(1)  # 例: '../../assets/hero-xxx-m6.png'
        # src/content/blog/foo.md からの相対パスを src/... に解決する
        asset_path = "src/assets/" + rel.split("/assets/")[-1]
        if not tracked_or_staged(asset_path):
            missing.append((f, asset_path))

    if missing:
        lines = "\n".join(f"  - {f} が参照する {img} が未コミット" for f, img in missing)
        deny(
            f"heroImage の参照先がステージ/コミット済みでない記事があります。\n{lines}\n"
            "git add で画像を追加してからコミットしてください。"
        )

    sys.exit(0)


if __name__ == "__main__":
    main()
