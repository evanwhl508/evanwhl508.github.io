// Render the single-concept family at exact native pixel sizes, with transparency.
async (page) => {
  const origin=new URL(page.url()).origin;
  if(!/^https?:/.test(origin))throw new Error('Open the local review before exporting.');
  const ctx=await page.context().browser().newContext({deviceScaleFactor:1});
  const p=await ctx.newPage();let count=0;
  for(const id of ['01','02','03','04','05']){
    for(const color of ['white','navy']){
      for(const size of [16,24,32,64,512]){
        await p.setViewportSize({width:size,height:size});
        await p.setContent(`<style>html,body{margin:0;background:transparent}img{display:block;width:100vw;height:100vh}</style><img src="${origin}/logo/two-origin/${id}/mark-${color}.svg">`);
        await p.locator('img').evaluate(i=>i.decode());
        await p.screenshot({path:`logo/two-origin/${id}/mark-${color}-${size}.png`,omitBackground:true});count++;
      }
    }
    // Independently render the two ribbons together for union/silhouette verification.
    const a=await(await p.request.get(`${origin}/logo/two-origin/${id}/origin-a-white.svg`)).text();
    const b=await(await p.request.get(`${origin}/logo/two-origin/${id}/origin-b-white.svg`)).text();
    await p.setViewportSize({width:512,height:512});
    await p.setContent(`<style>html,body{margin:0;background:transparent}svg{position:absolute;inset:0;width:512px;height:512px}</style>${a}${b}`);
    await p.screenshot({path:`output/playwright/two-origin-union-${id}.png`,omitBackground:true});
  }
  await p.setViewportSize({width:1400,height:640});
  for(const color of ['white','navy']){
    await p.goto(`${origin}/logo/two-origin/comparison-${color}.svg`);
    await p.screenshot({path:`logo/two-origin/comparison-${color}.png`});
  }
  await p.setViewportSize({width:1440,height:1000});
  await p.goto(`${origin}/logo/two-origin/`);await p.evaluate(()=>document.fonts.ready);
  await p.screenshot({path:'output/playwright/two-origin-gallery.png',fullPage:true});
  await ctx.close();await page.goto(`${origin}/logo/two-origin/`);
  return {concepts:1,variants:5,monochromePngs:count};
}
