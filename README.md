# news-image-01 — The World Today, Friday 13 November 2026

A newspaper-front-page image summing up the world's news of Friday
13 November 2026, judged by what the image itself shows.

## Stories in the image

- **Hero: U.S. flights grounded** — the FAA ordered a nationwide ground
  stop after a communications failure; flights were halted for about
  four hours and more than 11,000 flights were delayed or cancelled
  (FlightAware via Reuters: nearly 10,000 delayed, over 1,000
  cancelled), the second nationwide stop since 9/11.
- **Senate summons Huang & Lutnick** — the US Senate Banking Committee
  summoned former Nvidia chief executive Jensen Huang (who resigned on
  12 November) and Commerce Secretary Howard Lutnick to testify in
  December over Nvidia chip exports to China.
- **Europe to join Ukraine peace talks** — President Zelensky met US
  envoys Witkoff and Kushner in Dublin; the envoys said European
  partners would join the next round of talks, and a prisoner exchange,
  the largest of the war, was agreed.
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
corrected for faithfulness: the generated departures board repeated
the same few garbled rows, so the board was repainted with twelve
distinct delayed flights in a matching gold mono face, with
destinations corrected to the flights' real routes (BA177 to New
York, EK215 to Los Angeles, SQ318 and QF9 to London). Nothing else
was altered. This version also fixes the three points where the
previous version was weakest: the hero sub-headline now fits on one
line, nobody in the Europe panel looks at the camera, and the footer
is two lines in larger type.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`. Run locally with:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a 1024x1024 JPEG (named `entry.png`, as the rules allow),
372,208 bytes (under the 1 MiB limit), and byte-identical on every run.
