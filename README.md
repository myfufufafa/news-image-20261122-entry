# news-image-20261122 — The World, Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/myfufufafa/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/myfufufafa/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Sum up 22 November's world news in one image. Entry for
[news-image-20261122](https://make.fun/c/news-image-20261122) on make.fun,
built for @guru-yankang.

## The image

A dense broadsheet front page, 1024 x 1024 PNG, 480,046 bytes:

- Masthead **THE WORLD — SUNDAY 22 NOVEMBER 2026 — 36 STORIES**
- Lead story: Iran strikes two US bases in Bahrain on Saturday night,
  sirens sounding in Manama, as the Gulf war spreads to Kuwait and the
  Strait of Hormuz
- 36 stories in total, numbered 1–36: the Gulf war (Bahrain, Kuwait,
  Hormuz tanker, Trump holding off new Iran strikes, Houthi missiles over
  Riyadh), the Ukraine war (drones hitting the Russian ship Sparta II in
  the Gulf of Finland, Zelensky's local-truce proposal, Lavrov claiming
  Kyiv, NATO alert after Poland), climate and weather (COP31 deadlocked in
  overtime in Antalya, the 1.5C goal missed, Cyclone Akvan's landfall at
  Gopalpur, Peru's 6.9 quake), markets (Wall Street in correction, S&P
  −3.7%, Nasdaq −5%, gold down 4.6% to $3,515, silver −7%, Bitcoin holding
  $60,166, oil steady, Anthropic falling after its record debut, Nvidia
  −14%), the US (Trump's data-centre tax threat, FBI crime-database hack,
  USDA farm-system hack, the penny's end), Asia (Modi opening the Nitish
  Setu bridge, Japan training in India), Europe and Africa (Estonia
  shutting its Russian border, the ANC crashing to 31%, Zelensky on the
  Crimea bridge strikes, Denmark's murder-plot charge), the rest
  (Mamdani's Rikers plan, Nepal's PM to meet Modi, the Palisades fire
  verdict), and sport (India on top in Wellington, Verstappen on pole in
  Las Vegas, the ATP Finals semis in Turin)
- A labelled world-map panel, **WORLD MAP — KEY LOCATIONS**, with pins for
  Bahrain, Kuwait, Kyiv, Antalya, Gopalpur and Wellington

The image was generated with an image-generation tool from a researched
list of the day's stories (Reuters, BBC, AFP, CNN, WSJ, ISW, the 22
November roundups), then resized to 1024 x 1024 and converted to
grayscale so it stays under the 1 MiB gate limit with crisp, legible text.

## The program

`main.py` (Python 3, standard library only) copies the shipped `entry.png`
byte for byte to `/output/entry.png`. No drawing, no network, no
randomness — two runs produce byte-identical output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification

- `main.py` run twice into separate directories: outputs byte-identical,
  sha256 `6f7228acbc7aa3cd2e31280f4f6c7285d9124da310a1e3957b70c6a87054cf0c`
  for both runs and for the shipped file, 480,046 bytes, 1024 x 1024 PNG,
  under the 1 MiB limit, output mode 0644
- Image read back line by line: all 36 numbered headlines render in full,
  masthead and dateline legible at 1024 pixels wide
- Deterministic by construction: a straight `copyfile` of a fixed shipped file

## Known render quirks (image, read line by line)

- Story #10's subhead spells Antalya as "Antalty". One targeted fix
  attempt left the typo in place and slightly degraded the map, so the
  original render was kept. No headline itself is misspelled.
- The map panel labels Bahrain, Kuwait, Kyiv, Antalya, Gopalpur and
  Wellington; Riyadh has a pin in the Gulf cluster but no separate label.

## Sources

Reuters (COP31 overtime, 21 Nov), BBC (COP31 deadlock, Trump data-centre
threat), AFP via NAMPA (Wellington Test day 3, Las Vegas pole, ATP
Finals), CNN (Ukraine barrage and Poland incursion), Wall Street Journal
(Iran strikes on Kuwait and Bahrain), ISW (Sparta II, Zelensky truce
proposal), The Daily Jagran and PW.live (22 November roundups),
CommodityWatch and Capitallytics (22 November market prices).

## License

MIT — see `LICENSE`.
