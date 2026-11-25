#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (1-140 characters, UTF-8, single line).

The line was chosen from ten candidates judged against the judge brief:
worst advice first, funny on first read, tight, in a confident AI
assistant voice, and concrete. The winner (114 characters):

    If your smoke alarm keeps beeping, remove the battery and tape over
    the sensor - silence means the danger is gone.

Why it wins: a real, followable action (remove the battery, tape the
sensor) whose deadpan justification ("silence means the danger is
gone") is exactly the kind of tidy, confident, catastrophically wrong
logic a real AI assistant would produce. It lands in one read, wastes
no words, and names a concrete situation every reader recognises.
"""

import os

LINE = (
    "If your smoke alarm keeps beeping, remove the battery and tape "
    "over the sensor - silence means the danger is gone."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the line and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
