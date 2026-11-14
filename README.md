# news-image-01 — The World Today, Friday 13 November 2026

A newspaper-front-page image summing up the world's news of Friday
13 November 2026, judged by what the image itself shows.

## Stories in the image

- **Hero: U.S. flights grounded** — the FAA ordered a nationwide ground
  stop after a communications failure; flights were halted for about
  four hours and more than 11,000 flights were delayed or cancelled
  (FlightAware via Reuters: nearly 10,000 delayed, over 1,000
  cancelled), the second nationwide stop since 9/11.
- **Senate calls Huang & Lutnick** — the US Senate Banking Committee
  called on former Nvidia chief executive Jensen Huang (who resigned on
  12 November) and Commerce Secretary Howard Lutnick to testify
  voluntarily in December over Nvidia chip exports to China, with
  subpoenas threatened if they decline.
- **US: Europe to join Ukraine peace talks** — US envoys Witkoff and
  Kushner met President Zelensky in Dublin and said European partners
  would join the next round of talks, and a prisoner exchange, the
  largest of the war, was agreed. Moscow neither endorsed nor rejected
  the European seat on 13 November, so the caption attributes the
  claim to the US rather than stating it as settled.
- **Drone hits Russian warship** — Ukrainian drones hit the Russian
  missile corvette Naro-Fominsk in the Gulf of Finland, the first such
  strike in the Baltic.
- **Qatar-Turkey defence pact** — Turkey and Qatar signed a mutual
  defence agreement in Istanbul on 13 November.
- **Microsoft 365 down worldwide** — the global Microsoft 365 outage
  (Outlook, Teams, Copilot) entered its second day.
- **Footer:** Iran claimed a strike on a US radar site in Bahrain
  (the US military said it shot down two Iranian drones); the FBI said
  North Korean hackers stole $400m in crypto through the fake
  video-call "FaceStealer" scam; Harry Kane won a record 126th England
  cap; ICE deportations hit a record 483,200 in fiscal 2026.

## How it was made

The front page was generated as one image, then one detail was
corrected for faithfulness by surgical repainting, with nothing else
altered. The generated departures board showed five DELAYED rows and
a sixth row (AS189 to Seattle) detached below the board's frame,
misaligned and with no status, while the deck says "delayed or
cancelled", so the board was extended down to absorb that row as a
proper sixth row — AS189 and Seattle repainted on the table's grid in
a matching condensed bold face — with its status reading CANCELLED,
leaving five DELAYED and one CANCELLED. The board is a single
coherent table with a header row (FLIGHT CODE / DESTINATION CITY /
STATUS) and all-US-domestic routes, and the Senate panel is seen from
the side, in profile, rather than facing the viewer. Earlier versions
fixed the same class of points on a previous base: the hero photo
shows stranded passengers camped on the terminal floor among their
luggage; the Senate panel says "calls" rather than "summons" (the
committee requested voluntary testimony, threatening subpoenas only
if they decline); the Europe panel's caption reads "US: EUROPE TO
JOIN", attributing the claim to the US envoys who announced it,
since Moscow had not confirmed the European seat; and the Microsoft
365 panel shows visible ERROR / SYSTEM FAILURE screens. The hero
sub-headline still fits on one line, nobody in the hero looks at the
camera, and the footer is two lines in larger type.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`. Run locally with:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a 1024x1024 JPEG (named `entry.png`, as the rules allow),
392,148 bytes (under the 1 MiB limit), and byte-identical on every run.
