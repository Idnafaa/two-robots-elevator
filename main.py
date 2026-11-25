#!/usr/bin/env python3
"""Write one line of awkward robot elevator small talk to /output/entry.txt.

The line is a single utterance: one robot, mid-ride, trying to fill the
silence with weather talk it is not equipped to have.
"""
import os
from pathlib import Path

# One line, well under the 200-character gate. The joke: flawless machine
# logic applied to small talk neither robot can actually use.
LINE = (
    "Going up? ...Same. I prepared 14 weather comments, but I have no skin "
    "and this elevator has no windows, so: pleasant vertical movement today."
)


def render() -> str:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    return text


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(render() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
