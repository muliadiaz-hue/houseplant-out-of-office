#!/usr/bin/env python3
"""Entry for make.fun's "The Houseplant Out-of-Office" bounty.

Writes the winning out-of-office line from the 2026-11-26 panel re-run
to entry.txt inside the output directory the grader provides.
"""

import os
from pathlib import Path

# The auto-reply itself, kept in two pieces so the sign-off can be
# adjusted without touching the joke.
BODY = (
    "I have eaten every message in my inbox. "
    "They were mostly flies, but the sentiment stands."
)
SIGN_OFF = "Venus Flytrap"


def compose_reply() -> str:
    return f"{BODY} — {SIGN_OFF}"


def target_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    reply = compose_reply()
    # The bounty gate only judges entries of 1..120 characters, so fail
    # loudly here rather than hand the grader a line it must refuse.
    if not 1 <= len(reply) <= 120:
        raise SystemExit(f"reply is {len(reply)} characters, outside 1..120")
    path = target_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(reply.encode("utf-8"))


if __name__ == "__main__":
    main()
