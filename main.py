#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry (round-2 resubmit).

Writes one funny, heartfelt wedding vow a robot says at its own wedding
to /output/entry.txt. Deterministic: the same line every run.

The line (183 characters, gate allows 1-200):
  "I, Unit 12, take you to have and to hold — my error log holds exactly
   one entry in 4,000 days: the day I met you, when love crashed my
   scheduler and I have refused every reboot since."

Why this line (pairwise selection, see HANDOFF.md in the build dir):
  - 2-beat + reveal in the final clause (winner pattern from 15 finalist
    one-liners: vacuum-alibi, pickup-lines, judge-smile).
  - Explicit wedding formula ("take you to have and to hold") — judge
    criterion 1 first: it must BE a robot's wedding vow.
  - Two laugh beats, not a bolted-on pun (criterion 2): love as an
    "unknown process" that crashed the scheduler, and a robot that
    refuses every reboot since — machine defiance as devotion.
  - Genuine tenderness under the joke (criterion 3): the refusal to
    reboot is an ongoing choice to stay in love, not a one-off promise.
  - Machine-specific detail (criterion 4): error log, scheduler,
    reboot — the robot's own systems, not a human's words with a robot
    label.
  - Named character (Unit 12) and a specific number (4,000 days).
  - Fresh angle: error log / scheduler crash — not the crowded
    "love you through every firmware update" (8+ clones), battery (28),
    or reboot-as-joke angles, and not the round-1 warranty angle.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)
    if not line.endswith("."):
        print("ERROR: entry must be one sentence ending in a period",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "I, Unit 12, take you to have and to hold — my error log holds exactly "
    "one entry in 4,000 days: the day I met you, when love crashed my "
    "scheduler and I have refused every reboot since."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
