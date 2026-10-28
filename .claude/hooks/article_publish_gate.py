#!/usr/bin/env python3
"""PreToolUse(Bash): 記事の公開（draft:false の commit / push）を、article_gate.py が PASS しない限り拒否する。

背景: ガブリアスM-7記事で、数値の誤りが20ラウンド以上のレビュー往復でも残り続けた。
「ルールを書いて注意する」方式は再発し続けたため、公開の瞬間に機械的に止める。
ゲートは _local/article_facts/<slug>.json（article_facts.py の出力）と記事を照合する純Python処理で、
エンジンは呼ばない（hook のタイムアウト内で終わる）。

検査対象:
  - git commit … ステージ済みの src/content/blog/*.md のうち draft が false（または欠落）のもの
  - git push   … origin/main..HEAD で変わった同ファイル（origin/main が無ければスキップ）
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile

GIT_COMMIT = re.compile(r"(?:^|&&|;|\|\|)\s*git\s+commit\b")
GIT_PUSH = re.compile(r"(?:^|&&|;|\|\|)\s*git\s+push\b")
DRAFT_LINE = re.compile(r"^draft:\s*(true|false)", re.M)


def deny(reason):
    print(f"[article_publish_gate] 拒否しました。\n{reason}", file=sys.stderr)
    sys.exit(2)


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True, timeout=10)
    return r.returncode, r.stdout


def repo_root():
    rc, out = git("rev-parse", "--show-toplevel")
    return out.strip() if rc == 0 else None


def is_published(content):
    m = re.match(r"---\n(.*?)\n---\n", content, re.S)
    fm = m.group(1) if m else ""
    d = DRAFT_LINE.search(fm)
    return (d is None) or d.group(1) == "false"


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    command = payload.get("tool_input", {}).get("command", "")
    if not command:
        sys.exit(0)
    is_commit, is_push = bool(GIT_COMMIT.search(command)), bool(GIT_PUSH.search(command))
    if not (is_commit or is_push):
        sys.exit(0)

    root = repo_root()
    if not root:
        sys.exit(0)
    os.chdir(root)

    targets = []  # (path, content)
    if is_commit:
        rc, out = git("diff", "--cached", "--name-only", "--diff-filter=ACM")
        for f in out.splitlines():
            if f.startswith("src/content/blog/") and f.endswith(".md"):
                rc2, content = git("show", f":{f}")
                if rc2 == 0:
                    targets.append((f, content))
    if is_push:
        rc, out = git("diff", "--name-only", "origin/main..HEAD")
        if rc == 0:
            for f in out.splitlines():
                if f.startswith("src/content/blog/") and f.endswith(".md"):
                    rc2, content = git("show", f"HEAD:{f}")
                    if rc2 == 0 and not any(t[0] == f for t in targets):
                        targets.append((f, content))

    problems = []
    today = dt.date.today().isoformat()
    for f, content in targets:
        if not is_published(content):
            continue
        slug = os.path.basename(f)[:-3]
        facts = os.path.join(root, "_local", "article_facts", f"{slug}.json")
        if not os.path.exists(facts):
            problems.append(f"{f}: 事実ファイルが無い → python3 scripts/article_facts.py {slug}")
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        try:
            r = subprocess.run(
                [sys.executable, os.path.join(root, "scripts", "article_gate.py"), tmp_path,
                 "--facts", facts, "--today", today, "--slug", slug],
                capture_output=True, text=True, timeout=60,
            )
        finally:
            os.unlink(tmp_path)
        if r.returncode != 0:
            tail = "\n".join(r.stdout.strip().splitlines()[:25])
            problems.append(f"{f}: article_gate FAIL\n{tail}")

    if problems:
        deny("公開対象（draft:false）の記事がゲートを通っていません。\n" + "\n".join(problems)
             + "\n\n修正後に python3 scripts/article_gate.py <md> --facts _local/article_facts/<slug>.json で PASS を確認してください。")
    sys.exit(0)


if __name__ == "__main__":
    main()
