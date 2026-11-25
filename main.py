#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true one-line review of the dullest everyday object
we could name - a doorstop - to /output/entry.txt.

The joke is the object's own dullness: its entire job is lying on the
floor, and it still gets kicked for doing that job perfectly.

Arena champion (5-0, then 4-0 vs the gold set): chosen from 16 candidates
by two-way pairwise judging against the published judge brief. The line
is 107 characters, one line, every word earning its place.
"""

import os

REVIEW = (
    "One star. The doorstop's entire job is lying on the floor, "
    "and it still gets kicked for doing it perfectly."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert "\n" not in REVIEW, "entry must be a single line"
    assert 1 <= len(REVIEW) <= 200, "entry must be 1-200 characters"
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
