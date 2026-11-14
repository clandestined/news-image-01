"""news-image-01 entry: copy the bundled front-page image to /output/entry.png.

Deterministic, standard library only, no network. The image in this
repository sums up the world news of Friday 13 November 2026: the FAA
nationwide ground stop (hero story, more than 11,000 flights delayed
or cancelled, shown as stranded passengers camped on the terminal
floor), the Senate's call for Huang and Lutnick to testify, the US
envoys' announcement that Europe would join the Ukraine peace talks
(caption attributed to the US, since Moscow had not confirmed the
European seat), a drone hitting a Russian warship in the Gulf
of Finland, the Qatar-Turkey defence pact and the worldwide Microsoft
365 outage, plus a footer strip with Iran's claimed strike on a US
radar site in Bahrain, the FBI's $400m North Korea crypto-scam
warning, Kane's England caps record and the record US deportation
figure. The departures board in the hero photo was repainted with
twelve distinct delayed flights (destinations matched to the flights'
real routes); the Europe caption's first line was repainted to read
"US: EUROPE TO JOIN" so the claim is attributed to the US envoys
rather than stated as settled; the hero deck fits on one line and
the footer on two.
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
