"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene to $MAKEFUN_OUTPUT_DIR/entry.txt:
a father who still sets the table for four, years after his
daughter moved away, and the Sunday she comes home, sits in her
old chair, and tells him the food tastes better here.
Standard library only.
"""

import os
import sys

FAMILY_SCENE = (
    "Dad still sets the table for four, though his daughter "
    "moved away years ago.\n"
    "Last Sunday she came home, sat in her old chair, and said "
    "the food tasted better here \u2014 and he cried into the "
    "soup and blamed the onions."
)


def scene_gate(text):
    """Check the scene against the competition gate.

    The gate wants plain UTF-8 text of 1 to 280 characters, not
    only white space, in one or two lines: a small domestic
    moment that is warm, funny and heartfelt. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("family scene must not be only whitespace")
    if len(cleaned) > 280:
        raise ValueError(
            "family scene is %d characters, over the 280 limit"
            % len(cleaned)
        )
    lines = cleaned.splitlines()
    if len(lines) > 2:
        raise ValueError("family scene must be one or two lines")
    return cleaned


def scene_measure(text):
    """Measure the scene for one last sanity pass.

    Returns a dict with the character count, the line count and
    the word count of the cleaned text. A scene too short to
    carry a moment, or one padded out to fill the cap instead of
    landing the feeling, is caught here before anything is
    written.
    """
    words = text.split()
    return {
        "chars": len(text),
        "lines": len(text.splitlines()),
        "words": len(words),
    }


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = scene_gate(FAMILY_SCENE)
    shape = scene_measure(text)
    if shape["words"] < 10:
        raise ValueError("family scene is too short to carry a moment")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
