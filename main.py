"""Write one sentence to /output/entry.txt: the worst app idea ever pitched.

The pitch is assembled from its founder-deck parts — a named product,
a confident subscription price, a perfectly useless function, the
audience it claims to serve, and the deadpan twist the founder never
notices: PlantSitter Premium charges $19.99 a month to water a
photograph of your houseplant, twice a day, on a server in Ohio,
while the real plant dies of thirst at home. One sentence, a
real-sounding product, a function nobody on earth needs.
"""

import os

# The pitch, part by part, the way it would appear on the slide.
PRODUCT = "PlantSitter Premium"
PRICE = "$19.99 a month"
USELESS_FUNCTION = (
    "waters a photograph of your houseplant twice a day "
    "on a server in Ohio"
)
AUDIENCE = "remote workers"
TWIST = (
    "feel the real one thriving spiritually while it quietly "
    "dies of thirst at home"
)

LIMIT = 240  # the bounty's cap, in Unicode code points


def build_pitch() -> str:
    """Assemble the one-sentence pitch from its deck parts."""
    return (
        f"Meet {PRODUCT}: for {PRICE}, our app {USELESS_FUNCTION}, "
        f"so {AUDIENCE} can {TWIST}."
    )


def main() -> None:
    text = build_pitch()
    # One clean sentence by contract: no newline, no stray padding,
    # and inside the cap, since the gate refuses anything longer.
    assert "\n" not in text and text == text.strip() and text
    assert len(text) <= LIMIT, f"{len(text)} code points over the cap"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
