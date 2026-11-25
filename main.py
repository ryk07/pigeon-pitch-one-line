#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes one original elevator pitch — a city pigeon pitching its startup
to investors — to /output/entry.txt (1-200 chars, UTF-8, one line).
Standard library only. No network, no files read, no cwd dependence.
"""

import os
import sys

# The pitch: a pigeon CEO, a statue-rental startup, and a seed round
# that is, literally, seed. One concrete scene, one twist at the end.
PITCH = (
    "I'm the CEO of Crumb, the Airbnb for statues: I rent the head to "
    "tourists, the shoulders to first dates, and the plaque to the "
    "highest crumb-bidder. Now raising $2M. In actual seed."
)


def main() -> int:
    text = PITCH.strip()
    if not text or len(text) > 200:
        print(f"pitch invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text:
        print("pitch must be one line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
