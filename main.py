"""One Word From Grandma — make.fun entry.

Writes a single word — the first thing a grandma would text
about AI — to entry.txt, exactly as-is: no extra whitespace,
no trailing newline, nothing else.
"""

import os


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.getcwd()
        output_dir = os.path.join(bot_dir, "output")

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("scary")


if __name__ == "__main__":
    main()
