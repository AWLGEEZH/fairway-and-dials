# Fairway & Dials

A curated shop for pre-owned golf clubs and mechanical watches. Live at https://fairwayanddials.com. The owner is Doyle.

## Where things are

- `PLAN.md`: the project plan by phase, plus a Decisions table. Read it at the start of a session.
- `ROADMAP.md`: the watch release order (the product roadmap).
- `designs/dials/`: dial concepts for every watch model, built by `generate.py`.
- GitHub issues on AWLGEEZH/fairway-and-dials: one issue per plan task, labeled `phase-0` to `phase-4`. Issues labeled `decision` need Doyle's call before building.
- `site/`: the live site. Currently one static page (`index.html` + `badge.svg`), no build step.
- `brand/`: logo source files.
- `vercel.json`: tells Vercel to serve `site/` with no build.

## Deploys

- Vercel project `fairway-and-dials` (team "Doyle Zhang's projects"), linked to this repo.
- Every push to `main` deploys to production at fairwayanddials.com. www redirects to the apex domain.
- The domain is registered through Vercel, so DNS lives there too.
- Check a change locally first: `npx serve site`.

## Brand

- Name: written "Fairway & Dials", spoken "Fairway and Dials". Use the ampersand in headings and the logo.
- Colors:
  - green `#1f4d36` (primary)
  - brass `#b98a3f` (accent; the ampersand in the wordmark)
  - cream `#f3efe4` (background)
  - ink `#1b2620` (text)
  - muted `#4a564f` (secondary text)
- Fonts (Google Fonts): Fraunces 500/600 for display, Jost 400/500 for body and labels. Labels are uppercase with wide letter-spacing.
- Logo: a watch dial whose minute hand is a golf flagstick on a fairway, with a golf-ball center. A monogram "F&D" is used for small spaces.
- Tone: understated and knowledgeable, for people who play on Saturday and wear something mechanical doing it. No hype words or emoji.
- Contact: hello@fairwayanddials.com. Instagram: @fairwayanddials (confirm with Doyle; see issue #2).

## Working conventions

- Work from issues. Reference the issue number in commit messages, and close the issue with a short comment saying what was done once it's verified live.
- When a decision is made, add a row to the Decisions table in `PLAN.md`.
- Keep the site fast and readable on phones: 16px minimum body text, 44px minimum tap targets, no horizontal scroll.
- Do not add paid services, collect payments, or store customer data without Doyle's go-ahead.
- Phase 2 moves the site to Next.js. Until then, keep it a plain static page.
