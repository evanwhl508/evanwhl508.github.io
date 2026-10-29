// Use via Playwright CLI run-code against the existing local preview.
async(page)=>{
 const origin=new URL(page.url()).origin;
 if(!/^https?:/.test(origin))throw new Error('Open the local preview first.');
 const ctx=await page.context().browser().newContext({deviceScaleFactor:1});const p=await ctx.newPage();let count=0;
 for(const id of ['benchmark','polish-a','polish-b']){
  for(const color of ['white','navy','black','primary','light']){
   for(const size of [64,128,256]){
    await p.setViewportSize({width:size,height:size});
    await p.setContent(`<style>html,body{margin:0;background:transparent}img{display:block;width:100vw;height:100vh}</style><img src="${origin}/logo/h1-polish/${id}/mark-${color}.svg">`);
    await p.locator('img').evaluate(i=>i.decode());
    await p.screenshot({path:`logo/h1-polish/${id}/mark-${color}-${size}.png`,omitBackground:true});count++;
   }
  }
  for(const part of ['origin-a','origin-b','overlap']){
   await p.setViewportSize({width:512,height:512});
   await p.setContent(`<style>html,body{margin:0;background:transparent}img{display:block;width:512px;height:512px}</style><img src="${origin}/logo/h1-polish/${id}/${part}.svg">`);
   await p.locator('img').evaluate(i=>i.decode());await p.screenshot({path:`output/playwright/h1-polish-${id}-${part}.png`,omitBackground:true});
  }
 }
 await p.setViewportSize({width:1200,height:880});
 for(const color of ['white','primary','light']){
  await p.goto(`${origin}/logo/h1-polish/comparison-${color}.svg`);
  await p.screenshot({path:`logo/h1-polish/comparison-${color}.png`});
 }
 await p.setViewportSize({width:1440,height:1000});await p.goto(`${origin}/logo/h1-polish/`);await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:'output/playwright/h1-polish-gallery.png',fullPage:true});
 await ctx.close();await page.goto(`${origin}/logo/h1-polish/`);return {refinements:3,pngs:count};
}
