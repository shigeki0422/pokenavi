#!/usr/bin/env python3
"""PreToolUse(Bash): 作業ツリー・共有ビルド成果物を壊すコマンドを拒否する。

2026-09-12に、エージェントがリポジトリ全体の stash と共有ディレクトリの再帰削除を打ち、
並行作業中の別セッションの未コミット変更とビルド出力を消した事故への対策。
"""
import json
import re
import subprocess
import sys

PROTECTED_DIRS = r"(dist|\.astro|node_modules|\.git|\.claude|src|public|scripts|assets)"

# コマンド位置（先頭・区切り直後）でのみ判定する。コミットメッセージや grep の
# 引数に危険な文字列が入っていても誤検知しないため。
SEGMENT_SEP = re.compile(r"\|\||&&|[;\n|`()]|\$\(")
LEADING_NOISE = re.compile(r"^\s*(?:sudo\s+|\w+=\S*\s+)*")

RULES = [
    (
        re.compile(r"^git\s+clean\b"),
        "git clean は未追跡ファイルを消します。他セッションの作業中ファイルが飛びます。",
    ),
    (
        re.compile(
            r"^git\s+stash\s*$|^git\s+stash\s+(?:push|save)\b(?!.*\s--\s)|^git\s+stash\s+-\w"
        ),
        "パス指定なしの git stash はリポジトリ全体の変更を退避します（内部で reset --hard 相当）。\n"
        "切り分けが必要なら git worktree add で別ディレクトリを作ってください。\n"
        "退避するならパスを限定してください（push -- <path>）。",
    ),
    (
        re.compile(r"^git\s+reset\b.*(--hard|--merge|--keep)"),
        "git reset の --hard/--merge/--keep は作業ツリーを破棄します。",
    ),
    (
        re.compile(r"^git\s+checkout\b.*\s--\s"),
        "git checkout の -- <path> 形式は変更を破棄します。自分が編集していないファイルなら特に危険です。",
    ),
    (
        re.compile(r"^git\s+restore\b(?!.*--staged\b)"),
        "git restore は作業ツリーの変更を破棄します（--staged のみなら安全）。",
    ),
    (
        re.compile(r"^git\s+push\b.*(?:--force(?!-with-lease)|\s-f\b)"),
        "強制 push はリモートの履歴を壊します。--force-with-lease を使ってください。",
    ),
    (
        re.compile(
            rf"^rm\s+(?=(?:-\S+\s+)*-\S*[rR])[^;&|]*?(?<![\w.-]){PROTECTED_DIRS}(?:/|(?![\w.-]))"
        ),
        "共有ディレクトリの再帰削除です。dist・.astro・node_modules は他セッションのビルドも使っています。",
    ),
    (
        re.compile(r"^(kill|pkill|killall)\s"),
        "プロセスの強制終了は禁止です。自分が起動していないビルドやサーバを止める事故が起きました。\n"
        "止める必要があるならユーザーに確認してください。",
    ),
]

BUILD = re.compile(r"^(?:npm\s+run\s+build|astro\s+build|npx\s+astro\s+build)\b")


def segments(command):
    for raw in SEGMENT_SEP.split(command):
        yield LEADING_NOISE.sub("", raw).strip()


def deny(reason):
    print(f"[destructive_guard] 拒否しました。\n{reason}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    command = payload.get("tool_input", {}).get("command", "")
    if not command:
        sys.exit(0)

    parts = list(segments(command))

    for pattern, reason in RULES:
        if any(pattern.search(part) for part in parts):
            deny(reason)

    if any(BUILD.search(part) for part in parts):
        try:
            running = subprocess.run(
                ["pgrep", "-f", "astro build"], capture_output=True, text=True, timeout=5
            ).stdout.split()
        except Exception:
            running = []
        if running:
            deny(
                f"別の astro build が実行中です (PID {' '.join(running)})。\n"
                "同じ dist/ へ同時に書き込むと prerender チャンクが壊れ、両方のビルドが失敗します。\n"
                "完了を待つか、ユーザーに確認してください。"
            )

    sys.exit(0)


if __name__ == "__main__":
    main()
