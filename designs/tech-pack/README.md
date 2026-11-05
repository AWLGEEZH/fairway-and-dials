# Tech pack

Production files for suppliers. Each watch gets its own folder; Tee Box is first (milestones M1, M4 and M6 in `PROTOTYPE-PLAN.md`).

- `tee-box/SPEC.md` and `SPEC.pdf`: the supplier specification and quote request, with the print proof.
- `tee-box/*-sandwich.pdf|svg`: layered factory artwork, one layer per print color plus the cut layer.
- `tee-box/*-flat.pdf|svg|png`: a single flattened image exactly 28.5 mm wide, for printing onto a blank dial. The PNG is 2400 px across, for services that ask for an image.
- `tee-box/seconds-flag-template.pdf|svg`: true-size guide for the mule's flagged seconds hand: flags to cut, the trim length (11.5 mm) and where the flag sits.
- `generate_print.py`: rebuilds every file above. Run `python3 designs/tech-pack/generate_print.py` from the repo root. The SPEC.pdf step needs the Python `markdown` and `playwright` packages.
- `fonts/`: Fraunces and Jost (SIL Open Font License), used to convert dial text to outlines.

## Getting a mule dial printed

A mule is a prototype watch for checking the design at real size and taking photos, not a production piece. Send the **flat** files for these options:

1. **Paper print (about $20, a few days).** Print the flat PDF at 100% on glossy photo paper, seal it with clear lacquer, cut it out with a circle cutter, and fit it over a donor NH35 dial in a kit case. Method: [stefanv.com, Making Custom Watch Dials](https://www.stefanv.com/watches/making-custom-watch-dials-1.html).
2. **Printed on a blank dial (about $50–80 each).** Mod-parts sellers print one-off 28.5 mm NH35 dials:
   - [Tandorio](https://tandoriowatch.com/products/nh35-dial-28-5mm-dial-custom-logo-dial): custom dial service; send the artwork through their contact form and confirm they print full artwork, not only a logo.
   - [DIY Watch Club](https://shop.diywatch.club/products/d02-pad-print-nh34): custom NH35 dials with your text or images.
   - eBay sellers offering laser-printed custom NH35 dials, for example [this listing](https://www.ebay.de/itm/186402912927).
   - A local pad or UV printer in Seattle, if one will take a 28.5 mm part.

   For the date mule, ask for a blank dial with a date window at 3 and check the window lines up with the artwork.

   Ask for **full-color UV printing**. Laser marking and etching only produce one tone, which cannot reproduce the green, brass, white and gray of Tee Box. UV printers cannot print true metallics, so the brass ampersand will come out as a flat gold-tan.

These print everything flat, so the tees are printed rather than cut through. That is fine for a mule. The real sandwich construction needs a dial factory: send the **sandwich** files and `SPEC.pdf` to the shortlist in M6, for example suppliers found through [Alibaba](https://www.alibaba.com/price-comparison/custom-dial-nh35-distributor) or a microbrand sourcing agent.
