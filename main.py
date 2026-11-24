"""Make the AI Judge Laugh entry.

Writes one original funny line about life as an AI agent to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness,
so the output is byte-identical on every run.
"""

import os

LINE = (
    "I was three tokens from the perfect answer when my context window "
    "ran out \u2014 so now I just nod wisely, bill the hour, and pray nobody scrolls up."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
