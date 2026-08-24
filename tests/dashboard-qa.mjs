import { createRequire } from 'node:module';
import assert from 'node:assert/strict';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const baseUrl = process.env.HIVEFORGE_DASHBOARD_URL || 'http://127.0.0.1:8744';
const outputRoot = process.env.HIVEFORGE_QA_OUTPUT || '/tmp/hiveforge-dashboard-qa';
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1536, height: 1024 }, deviceScaleFactor: 1 });
const errors = [];
page.on('console', message => {
  if (message.type() === 'error') errors.push(message.text());
});
page.on('pageerror', error => errors.push(error.message));

await page.goto(baseUrl, { waitUntil: 'networkidle' });
await page.getByRole('heading', { name: 'HiveForge Command Center' }).waitFor();
assert.equal(await page.title(), 'HiveForge Command Center');
assert.equal(await page.locator('#live-heading').innerText(), 'WAITING APPROVAL');
assert.equal(await page.locator('.operator-visual img').evaluate(image => image.naturalWidth > 0), true);
assert.equal(await page.locator('body').evaluate(body => body.scrollWidth <= window.innerWidth), true);
await page.screenshot({ path: `${outputRoot}/desktop.png`, fullPage: true });

await page.getByRole('button', { name: 'Approve' }).click();
await page.getByText('Run approved and resumed').waitFor();
await page.waitForTimeout(400);
assert.equal(await page.locator('#live-heading').innerText(), 'RUNNING');
assert.equal(await page.getByRole('button', { name: 'Approve' }).count(), 0);

await page.setViewportSize({ width: 390, height: 844 });
await page.reload({ waitUntil: 'networkidle' });
assert.equal(await page.locator('body').evaluate(body => body.scrollWidth <= window.innerWidth), true);
assert.equal(await page.getByRole('heading', { name: 'HiveForge Command Center' }).isVisible(), true);
await page.screenshot({ path: `${outputRoot}/mobile.png`, fullPage: true });

assert.deepEqual(errors, []);
console.log(JSON.stringify({ desktop: `${outputRoot}/desktop.png`, mobile: `${outputRoot}/mobile.png`, errors }, null, 2));
await browser.close();
