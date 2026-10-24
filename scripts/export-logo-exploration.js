// Playwright CLI run-code, from an open local-server tab. Native 1x transparent exports.
async (page) => {
  const origin = new URL(page.url()).origin;
  if (!/^https?:/.test(origin)) throw new Error('Open the local site first.');
  const sourcePage = page;
  const exportContext = await page.context().browser().newContext({ deviceScaleFactor: 1 });
  page = await exportContext.newPage();
  let count = 0;
  for (let number = 1; number <= 10; number++) {
    const id = String(number).padStart(2, '0');
    for (const palette of ['dark', 'light', 'white', 'navy']) {
      for (const size of [16, 24, 32, 64, 512]) {
        await page.setViewportSize({width:size,height:size});
        await page.setContent(`<style>html,body{margin:0;padding:0;background:transparent}img{display:block;width:100vw;height:100vh}</style><img src="${origin}/logo/exploration/${id}/mark-${palette}.svg" alt="">`);
        await page.locator('img').evaluate(img => img.decode());
        await page.screenshot({path:`logo/exploration/${id}/mark-${palette}-${size}.png`,omitBackground:true});
        count++;
      }
    }
  }
  await page.setViewportSize({width:1280,height:800});
  for (const palette of ['dark','light','white','navy']) {
    await page.setContent(`<style>html,body{margin:0}img{display:block;width:1280px;height:800px}</style><img src="${origin}/logo/exploration/contact-sheet-${palette}.svg" alt="">`);
    await page.locator('img').evaluate(img=>img.decode());
    await page.screenshot({path:`logo/exploration/contact-sheet-${palette}.png`});
  }
  await page.setViewportSize({width:1440,height:1000});
  await page.goto(origin+'/logo/exploration/');
  await page.evaluate(()=>document.fonts.ready);
  await page.screenshot({path:'output/playwright/logo-exploration-gallery.png',fullPage:true});
  await exportContext.close();
  await sourcePage.goto(origin+'/logo/exploration/');
  return {concepts:10,transparentPngs:count,contactSheets:4,sizes:[16,24,32,64,512]};
}
