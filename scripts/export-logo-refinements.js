// Run against the local site with Playwright CLI run-code.
async (page) => {
  const origin = new URL(page.url()).origin;
  if (!/^https?:/.test(origin)) throw new Error('Open the local site first.');
  for (const variant of ['a', 'b', 'c']) {
    for (const colorway of ['dark', 'light', 'white', 'navy']) {
      for (const size of [16, 24, 32, 64, 512]) {
        await page.setViewportSize({ width: size, height: size });
        await page.setContent(`<html><head><link rel="icon" href="${origin}/logo/covan-mark-dark.svg"><style>html,body{margin:0;padding:0;background:transparent}img{display:block;width:100vw;height:100vh}</style></head><body><img src="${origin}/logo/refinements/${variant}-${colorway}.svg" alt=""></body></html>`);
        await page.locator('img').evaluate(img => img.decode());
        await page.screenshot({ path: `logo/refinements/${variant}-${colorway}-${size}.png`, omitBackground: true });
      }
    }
  }
  await page.setViewportSize({ width: 1600, height: 1100 });
  await page.goto(origin + '/logo/refinements/');
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: 'output/playwright/logo-refinements-comparison.png', fullPage: true });
  return { variants: 3, sizes: [16,24,32,64,512], colorways: 4, transparentPngs: 60 };
}
