#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes a single line — the one line its writer would send back to
his younger self — to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "Kid, the scar you hide under your sleeve becomes the map "
    "someone else follows home — wear it where they can see it."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
