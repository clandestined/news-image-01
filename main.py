"""news-image-01 entry: copy the bundled front-page image to /output/entry.png.

Deterministic, standard library only, no network. The image in this
repository sums up the world news of Friday 13 November 2026: the FAA
nationwide ground stop (hero story), the Senate summons of Huang and
Lutnick, Zelensky meeting US envoys, a drone hitting a Russian warship,
Iran's claimed strike on a US radar site in Bahrain, and the FBI's
$400m North Korea crypto-hack warning, plus a footer strip with the
Qatar-Turkey defence pact, Kane's England caps record and the record
US deportation figure.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # A plain byte copy: no timestamps, no randomness, so repeated runs
    # always produce identical output bytes.
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
