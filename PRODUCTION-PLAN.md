# Tee Box: production plan (Feb – Nov 2027)

How Tee Box goes from factory samples to a first run of about 100 watches delivered to customers. Starts where `PROTOTYPE-PLAN.md` ends: a **go** at M7 on January 31, with a supplier shortlist and quotes in hand. If M7 is a no-go, this plan waits.

Working premise, carried over: a small-batch, pre-order microbrand; NH38 movement (Miyota 9039 as the fallback if quotes favor it); price $450–650.

## Milestones

| # | Milestone | Target | Done when |
|---|---|---|---|
| P1 | Protection in place | Feb 7 | NNN agreement signed with the chosen supplier; trademark filings submitted in the US and China; repo private |
| P2 | Supplier chosen | Feb 14 | One partner picked from the M6 quotes; decision row in `PLAN.md` |
| P3 | Tech pack complete | Feb 21 | Case drawing with tolerances, hand spec, strap, caseback and packaging added to `designs/tech-pack/` |
| P4 | Sample order placed | Feb 28 | PO for 3–5 samples sent; deposit paid |
| P5 | Samples received | Apr 15 | Samples in hand and photographed on arrival |
| P6 | Samples tested | May 1 | Every test below logged; list of required changes sent to the supplier |
| P7 | Revision round | Jun 1 | Revised samples received, if P6 found problems |
| P8 | Golden sample approved | Jun 15 | One sample signed off as the production standard; a matching one kept by the supplier |
| P9 | Production order placed | Jun 30 | PO for the first run, referencing the golden sample; deposit paid |
| P10 | Pre-shipment inspection | Sep 30 | Independent inspection passed; balance paid |
| P11 | Delivered and cleared | Oct 20 | Watches through customs and in Seattle; landed cost per watch recorded |
| P12 | First customer shipments | Nov 2027 | Pre-order customers' watches shipped |

Dates assume one revision round and a 12–16 week production lead time. Each extra revision round adds about 4–6 weeks.

## P1: Protection (by Feb 7)

- **NNN agreement** (non-disclosure, non-use, non-circumvention) with the chosen supplier, written to be enforceable in China. A standard US NDA is not enough. Sign it before the full tech pack is shared.
- **Trademarks:** file "Fairway & Dials" and the Tee Box name in Class 14 (watches) with the USPTO, and in China, which grants marks to whoever files first. Run the USPTO search first (see `ROADMAP.md`).
- **Repo:** make AWLGEEZH/fairway-and-dials private before files go to factories.

## P2: Choosing the supplier (by Feb 14)

Compare the M6 quotes side by side:

| Ask | Supplier A | Supplier B | Supplier C |
|---|---|---|---|
| Sample cost and lead time | | | |
| MOQ | | | |
| Unit cost at 100 and 300 | | | |
| Tooling (case, dial plates, hands) | | | |
| Payment terms | | | |
| QC they do before shipping | | | |
| Handling of defective units | | | |
| Microbrand references | | | |

Pick on references and communication as much as price. For a first run, a full-service assembler or a sourcing agent that works with microbrands is simpler than buying the case, dial and hands separately.

## P3: Completing the tech pack (by Feb 21)

Already done: dial artwork, print spec and the flagged seconds hand concept (`designs/tech-pack/tee-box/`). Still needed:

- **Case drawing:** diameter (chosen at M2), lug-to-lug, thickness, lug width (20 mm), crown type, crystal (double-domed sapphire), solid engraved caseback, water resistance (100 m), finish. A freelance watch designer can draw it, or the supplier's engineers can work from the mule.
- **Hands:** hour and minute shapes and lengths, finish (black), lume (C3 or BGW9), and the seconds hand with its brass flag, about 11.5 mm long so the tip reaches the cup.
- **Dial for the chosen movement:** confirm dial feet, centre hole and size against the case. Rebuild the artwork at the final size with `generate_print.py` if it changes from 28.5 mm.
- **Strap:** default strap and one alternate (decided at M1).
- **Caseback engraving, packaging, warranty card.**

## P4–P8: Samples (Feb 28 – Jun 15)

Test every sample and log the results:

| Test | Pass when |
|---|---|
| Water resistance | Holds the rated 100 m on a pressure tester (a Seattle watchmaker can test this) |
| Timekeeping | Within the movement's spec on a timegrapher in five positions; target ±10 s/day after regulation |
| Swing test (#20) | No change in timekeeping after a range session |
| Dial and hands | Dial centred, print sharp, hands clear the dial and crystal, flag lands in the cup at :30 |
| Lume | Hands readable after 30 minutes in the dark |
| Crown and caseback | Crown screws down cleanly; no dust under the crystal |
| Wear test | Worn for a week with no issues; two or three outside people give first impressions |

The approved sample becomes the **golden sample**. Keep it, and make sure the supplier keeps an identical one. Every production watch is judged against it.

## P9–P11: Production run (Jun 30 – Oct 20)

- **Purchase order:** quantity, unit price, the golden sample as the standard, delivery date, payment terms (commonly 30–50% deposit, balance before shipping), and how defects are handled.
- **Pre-shipment inspection:** hire an independent inspector (for example QIMA or V-Trust) to check a sample of the finished watches against the spec before paying the balance.
- **Shipping and import:** for about 100 watches, express courier is usually simplest. Watch duties are calculated from several parts of the watch, not one flat rate, and tariffs on goods from China change often. Get a customs broker's quote before P9 so the landed cost is known when the PO is placed.
- **On arrival:** check every watch on the timegrapher and by eye before it goes to a customer.

## Go conditions for the production order (P9)

1. The golden sample passes every test above.
2. Landed cost per watch at 100 units still supports the $450–650 price with 35–40% net after fees, shipping and warranty (same test as M7).
3. Pre-orders or waitlist signups support the run size.

## Budget

| Item | Estimate |
|---|---|
| NNN agreement and trademark filings | A few hundred dollars per class per country; more with an attorney |
| Case drawing (if outsourced) | $0–1,000 |
| Sample order (3–5 pieces) | $2,000–5,000 (from `PROTOTYPE-PLAN.md`) |
| Production run (100 units) | Unit cost × 100, plus tooling, from the chosen quote |
| Pre-shipment inspection | A few hundred dollars per inspection |
| Freight, duties and broker | From the customs broker's quote |

## Open decisions

- How to fund the run: pre-orders on the site, a crowdfunding campaign, or self-funded. Taking payments needs Doyle's go-ahead (see `CLAUDE.md`).
- Warranty length and who services watches under warranty.
- Packaging: box, travel pouch, or both.
- Whether the first run includes the date version, or stays no-date only (`ROADMAP.md` says no-date first).

## Not in this plan

- The second release (Caddie) and the Tool collection.
- Reviewer outreach, which starts at M7 with prototypes and continues alongside this plan.
