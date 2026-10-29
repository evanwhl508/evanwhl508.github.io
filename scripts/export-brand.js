// Pass this function to playwright-cli run-code after opening the local site.
async (page) => {
  const origin = new URL(page.url()).origin;
  if (!/^https?:/.test(origin)) throw new Error('Open the local preview server first.');
  const render = async (source, target, width, height = width, transparent = true) => {
    await page.setViewportSize({ width, height });
    await page.setContent(`<html><head><style>html,body{margin:0;padding:0;background:transparent}img{display:block;width:100vw;height:100vh}</style></head><body><img src="${origin}${source}" alt=""></body></html>`);
    await page.locator('img').evaluate(image => image.decode());
    await page.screenshot({ path: target, omitBackground: transparent });
  };
  for (const size of [512, 256, 128, 64, 32, 16]) {
    const name = size < 64 ? `favicon-${size}` : `covan-mark-${size}`;
    await render('/logo/covan-mark-dark.svg', `logo/${name}.png`, size);
    await render('/logo/covan-mark-light.svg', `logo/${name}-light.png`, size);
  }
  await render('/logo/covan-mark-dark.svg', 'logo/apple-touch-icon.png', 180);
  await render('/logo/social-card.svg', 'logo/social-card.png', 1200, 630, false);
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto(origin + '/');
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: 'output/playwright/theme2-desktop.png', fullPage: true });
  await page.goto(origin + '/logo/concepts/');
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: 'output/playwright/logo-concepts.png', fullPage: true });
  return { transparentPngs: 13, socialCard: '1200 × 630', concepts: 3 };
}
