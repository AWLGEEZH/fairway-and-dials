// Renders the PNG brand assets and the social card from the SVG sources.
// Usage: node tools/render-assets.mjs
// Fonts come from Google Fonts, so this needs network access.

// Playwright may be installed globally (outside the project), so resolve it via
// require(), which honours NODE_PATH; a bare ESM import would not find it.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { readFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const read = (p) => readFileSync(resolve(root, p), 'utf8');

const FONTS = 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Jost:wght@400;500&display=swap';

const GREEN = '#1f4d36';
const BRASS = '#b98a3f';
const CREAM = '#f3efe4';
const MUTED = '#4a564f';

// A page that holds one SVG at an exact pixel size, on a transparent canvas.
const svgPage = (svg, w, h) => `<!doctype html><meta charset="utf-8">
<link href="${FONTS}" rel="stylesheet">
<style>
  html,body{margin:0;background:transparent}
  #a{width:${w}px;height:${h}px;display:block}
  #a svg{width:100%;height:100%;display:block}
</style>
<div id="a">${svg}</div>`;

const ogPage = (badge) => `<!doctype html><meta charset="utf-8">
<link href="${FONTS}" rel="stylesheet">
<style>
  html,body{margin:0}
  body{width:1200px;height:630px;background:${CREAM};font-family:Jost,system-ui,sans-serif;
       display:flex;align-items:center;gap:72px;padding:0 90px;box-sizing:border-box;position:relative}
  body::after{content:"";position:absolute;left:0;right:0;bottom:0;height:10px;background:${BRASS}}
  .badge{width:300px;height:300px;flex:none}
  .badge svg{width:100%;height:100%;display:block}
  h1{margin:0;font-family:Fraunces,Georgia,serif;font-weight:600;font-size:92px;line-height:1;color:${GREEN}}
  h1 .amp{color:${BRASS};font-weight:500}
  .rule{width:104px;height:3px;background:${BRASS};margin:26px 0 24px}
  .tag{margin:0;font-size:23px;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:${MUTED}}
  .dom{margin:30px 0 0;font-size:28px;font-weight:500;color:${GREEN}}
</style>
<div class="badge">${badge}</div>
<div>
  <h1>Fairway <span class="amp">&amp;</span> Dials</h1>
  <div class="rule"></div>
  <p class="tag">Golf clubs &middot; Timepieces</p>
  <p class="dom">fairwayanddials.com</p>
</div>`;

const badge = read('brand/badge.svg');
const monogram = read('brand/monogram.svg');
const wordmark = read('brand/wordmark.svg');

const jobs = [
  // Social card
  { out: 'site/og.png', html: ogPage(badge), w: 1200, h: 630, omitBg: false },
  // Badge
  { out: 'brand/png/badge-512.png', html: svgPage(badge, 512, 512), w: 512, h: 512 },
  { out: 'site/icon-512.png',       html: svgPage(badge, 512, 512), w: 512, h: 512 },
  { out: 'site/icon-192.png',       html: svgPage(badge, 192, 192), w: 192, h: 192 },
  { out: 'site/apple-touch-icon.png', html: svgPage(badge, 180, 180), w: 180, h: 180, bg: CREAM },
  { out: 'site/favicon-32.png',     html: svgPage(monogram, 32, 32), w: 32, h: 32 },
  // Monogram
  { out: 'brand/png/monogram-512.png', html: svgPage(monogram, 512, 512), w: 512, h: 512 },
  { out: 'brand/png/monogram-64.png',  html: svgPage(monogram, 64, 64),   w: 64, h: 64 },
  // Wordmark (2x)
  { out: 'brand/png/wordmark-1440.png', html: svgPage(wordmark, 1440, 320), w: 1440, h: 320 },
];

const browser = await chromium.launch();
try {
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 1 });
    await page.setContent(j.html, { waitUntil: 'load' });
    try { await page.evaluate(() => document.fonts.ready); } catch {}
    await page.waitForTimeout(400);
    if (j.bg) await page.evaluate((c) => { document.body.style.background = c; }, j.bg);
    mkdirSync(dirname(resolve(root, j.out)), { recursive: true });
    await page.screenshot({ path: resolve(root, j.out), omitBackground: j.omitBg !== false });
    await page.close();
    console.log('wrote', j.out, `${j.w}x${j.h}`);
  }
} finally {
  await browser.close();
}
