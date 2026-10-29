// Playwright CLI run-code. Render proofs in an isolated 1× context.
async (page) => {
  const origin=new URL(page.url()).origin;
  const context=await page.context().browser().newContext({deviceScaleFactor:1});
  const proof=await context.newPage();
  const manifest=await (await proof.request.get(origin+'/logo/identity/manifest.json')).json();
  for(const variant of manifest.variants){
    for(const color of ['white','navy']){
      for(const size of [16,24,32,64,512]){
        await proof.setViewportSize({width:size,height:size});
        await proof.setContent(`<style>html,body{margin:0;background:transparent}img{display:block;width:100vw;height:100vh}</style><img src="${origin}/logo/identity/${variant.id}/mark-${color}.svg">`);
        await proof.locator('img').evaluate(i=>i.decode());
        await proof.screenshot({path:`logo/identity/${variant.id}/mark-${color}-${size}.png`,omitBackground:true});
      }
      for(const scale of [1,2]){
        const w=Math.ceil(variant.navbar_width*scale),h=variant.navbar_height*scale;
        await proof.setViewportSize({width:w,height:h});
        await proof.setContent(`<style>html,body{margin:0;background:transparent}img{display:block;height:100vh;width:auto}</style><img src="${origin}/logo/identity/${variant.id}/identity-${color}.svg">`);
        await proof.locator('img').evaluate(i=>i.decode());
        await proof.screenshot({path:`logo/identity/${variant.id}/identity-${color}-${scale}x.png`,omitBackground:true});
      }
    }
  }
  await proof.setViewportSize({width:1440,height:960});
  for(const color of ['white','navy']){
    await proof.goto(origin+`/logo/identity/comparison-${color}.svg`);
    await proof.screenshot({path:`logo/identity/comparison-${color}.png`});
  }
  await proof.goto(origin+'/logo/identity/');
  await proof.evaluate(()=>document.fonts.ready);
  await proof.screenshot({path:'output/playwright/identity-desktop.png',fullPage:true});
  await context.close();
  await page.goto(origin+'/logo/identity/');
  return {directions:2,refinements:4,monochromeMarks:40,identityPngs:16,comparisonSheets:2};
}
