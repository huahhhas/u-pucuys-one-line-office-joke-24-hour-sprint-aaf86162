#!/usr/bin/env python3
"""One-line office joke for make.fun's One-Line Office Joke: 24-Hour Sprint.

Writes a single-line joke about office life (at most 200 characters)
to /output/entry.txt.
"""

import os

JOKE = "The meeting that could have been an email just booked a follow-up to discuss why it wasn't an email."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
