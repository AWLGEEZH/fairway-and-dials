# Dial concepts

Concept dials for Fairway & Dials watches, in the brand palette and fonts. These are design studies for prototyping (issue #19), not production artwork.

`collection-sheet.svg` shows every dial on one page. `tee-box-side-by-side.svg` shows the launch model large, no date next to date. To change a design, edit `generate.py` and run it from the repo root:

```
python3 designs/dials/generate.py
```

## Collections

| Collection | Type | Models | Files |
|---|---|---|---|
| Links | Field, sandwich dial (Clubhouse uses applied indices) | Bunker, Fairway Stripe, Pin High, Tee Box, Caddie, Dawn Patrol, Front Nine, Clubhouse | `links/` |
| Tool | Diver, sandwich dial | Marker (stroke-counter bezel, hole-counter inner ring) | `tool/` |

Every model comes in a no-date version (NH38 movement) and a date version (NH35, window at 3). Each file is named `<model>-no-date.svg` or `<model>-date.svg`.

## Shared details

- Sandwich construction: numerals and markers are cut through the top plate, with lume underneath.
- "Fairway & Dials" wordmark under 12, with the model name directly beneath it.
- "Automatic" printed small and faint in light-weight Jost above 6.
- The seconds hand carries a small brass flag near the center; hour and minute hands are plain with lume. Golf-ball center cap.

## Models

- **Bunker:** sand dial with raked grooves, green lume.
- **Fairway Stripe:** mowing stripes on the green dial.
- **Pin High:** a flagstick cutout replaces the 12, and a cup replaces the 6.
- **Tee Box:** the launch model. Cream dial with realistic golf-tee hour markers and a ball resting on the 12 tee. A printed cup replaces the 6. Every :30 the flagged seconds hand stands in the cup like a pin in the hole; hack the movement at :30 for product photos.
- **Caddie:** cream dial, full green Arabic numerals, with a faint tone-on-tone caddie bib (number 1) printed behind the center. The bib is a generic design; avoid any tournament-specific bib styling, which is trademarked.
- **Dawn Patrol:** ink dial, warm vintage lume, railroad track.
- **Front Nine:** green dial with all twelve Arabic numerals. Hours 1 to 9 (the front nine) are cream lume cutouts; 10, 11 and 12 are printed in brass.
- **Clubhouse:** the 19th hole and the dressiest model, meant for after the round. Deep green dial with applied brass batons (double at 12), brass dauphine hands and a brass minute track. A tiny brass "19" replaces the 19th minute tick.
- **Marker:** the first Tool collection model, named for the golfer who keeps your score. Graphite dial, the color of a scorecard pencil. The outer bezel counts strokes (120 clicks, marked every 20). The crown at 2 turns the inner ring for holes 1 to 18, starting with hole 1 at 12. The crown at 4 sets the time.

## Production notes

- Names are working titles. Run a USPTO search in Class 14 before committing to any of them.
- Thin Fraunces strokes (1, 4, 7) may be too fine to cut through a dial plate; a dial maker may thicken them.
- Marker needs a compressor-style case with a second crown for the inner ring.
