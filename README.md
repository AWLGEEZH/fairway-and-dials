# Fairway & Dials

Curated pre-owned golf clubs and mechanical watches. **fairwayanddials.com**

- [`PLAN.md`](PLAN.md): the project plan, phase by phase
- [`site/`](site/): the website (currently a one-page coming-soon site)
- [`brand/`](brand/): logo files

## Run the site locally

The site is a single static page with no build step:

```bash
npx serve site
```

## Deploy

The site deploys on Vercel from `main`, with `site/` as the output directory.
