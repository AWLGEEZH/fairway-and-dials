# Fairway & Dials: project plan

A curated shop for pre-owned golf clubs and mechanical watches, at **fairwayanddials.com** with a matching Instagram account.

Each task below has a matching GitHub issue, labeled by phase.

## Phase 0: Lock down the brand (week 1)

| Task | Owner | Done when |
|---|---|---|
| Register `fairwayanddials.com` (Vercel, $11.25/yr, auto-renew on) | Doyle approves, Claude buys | Domain shows in the Vercel domains dashboard |
| Instagram business account | Doyle | Profile live with logo, bio and link to the site |
| Reserve the same handle on Facebook and TikTok | Doyle | Handles held, even if unused |
| Brand email `hello@fairwayanddials.com` | Doyle + Claude | Mail to that address reaches Doyle's inbox (forwarding is enough to start) |
| Export the logo set (badge, monogram, wordmark) as SVG and PNG | Claude | Files in `/brand` |

## Phase 1: Coming-soon site (weeks 1–2)

Goal: the domain shows a real page the day it's bought, and the Instagram bio has somewhere to point.

| Task | Owner | Done when |
|---|---|---|
| One-page site: logo, one-line pitch, Instagram link, contact email | Claude | `site/index.html` in this repo (starter already included) |
| Deploy on Vercel from this repo | Claude | Every push to `main` deploys automatically |
| Connect `fairwayanddials.com` and `www` | Claude | Both load the site over HTTPS |
| Email waitlist signup | Claude | Signups are stored (Supabase table) and Doyle can export them |
| Basic analytics | Claude | Vercel Web Analytics turned on |
| Social share metadata, icon set and social card | Claude | Link previews render on Instagram, iMessage and X |

## Phase 2: Storefront MVP (weeks 3–6)

Goal: people can browse inventory on the site and buy.

| Task | Owner | Done when |
|---|---|---|
| Decide checkout: link out to eBay listings, or native checkout (Stripe) | Doyle | Decision recorded below |
| Move the site to Next.js (keep the same look) | Claude | Same pages, now built with components |
| Catalog: two collections, Fairway (clubs) and Dials (watches) | Claude | Collection pages and product detail pages |
| Inventory source: pull from the eBay store or a simple admin sheet | Claude | Adding an item doesn't require editing code |
| Product photo standard (angles, background, lighting) | Doyle | Short shot list in `/docs` |
| Policies: returns, shipping, authenticity | Doyle | Pages live on the site |

## Phase 3: Brand and content (ongoing)

| Task | Owner | Done when |
|---|---|---|
| Instagram feed on the homepage | Claude | Latest posts show on the site |
| Journal: watch-on-the-course stories, club reviews | Doyle writes, Claude formats | First 3 posts live |
| Concept page for the Fairway & Dials golf counter watch | Claude | Bezel counter design shown, with interest signup |

## Phase 4: The golf counter watch (later)

| Task | Owner | Done when |
|---|---|---|
| Mod prototype: NH35 case with internal rotating ring and 120-click bezel, custom printed insert and ring | Doyle | A wearable prototype has been tested on the course |
| Swing testing: timekeeping before and after range sessions | Doyle | Results written up |
| Factory samples: 18-click inner ring detent, titanium case, shock-mounted movement | Doyle | Quotes from 2–3 assemblers |
| Waitlist demand check before any tooling | Doyle | Enough signups to justify a first run |

## Decisions

| Date | Decision |
|---|---|
| 2026-10 | Name: **Fairway & Dials** (spoken "Fairway and Dials"); domain `fairwayanddials.com` |
| 2026-10 | Hosting: Vercel; code in this repo |
| — | Checkout approach (Phase 2) |

## Open questions

- Instagram handle: confirm the exact handle so the site links to it (currently `@fairwayanddials`).
- Business entity and sales tax setup before taking payments directly.
