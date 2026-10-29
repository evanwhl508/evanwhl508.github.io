async(page)=>{
 const origin='http://127.0.0.1:4173';
 const ctx=await page.context().browser().newContext({deviceScaleFactor:1}); const p=await ctx.newPage();
 const manifest=await (await p.request.get(origin+'/public/brand/manifest.json')).json();let count=0;
 async function render(src,width,height,path,transparent=true){
  await p.setViewportSize({width,height});await p.setContent(`<style>html,body{margin:0;background:transparent}img{display:block;width:100vw;height:100vh}</style><img src="${origin}/public/brand/${src}">`);await p.locator('img').evaluate(i=>i.decode());await p.screenshot({path,omitBackground:transparent});count++;
 }
 for(const asset of manifest.exports){
  for(const size of [512,256,128,64,32])await render(asset.svg,size,Math.max(1,Math.round(size*asset.height/asset.width)),`public/brand/png/${asset.svg.split('/').pop().replace('.svg',`-${size}.png`)}`);
 }
 for(const type of ['primary','monochrome','light','navy'])for(const size of [16,20,24,32,48,64])await render(`micro/covan-mark-micro-${type}.svg`,size,size,`public/brand/micro/covan-mark-micro-${type}-${size}.png`);
 for(const candidate of ['a','b'])for(const size of [16,24,32,48])await render(`favicon/candidate-${candidate}.svg`,size,size,`public/brand/favicon/candidate-${candidate}-${size}.png`);
 for(const size of [16,24,32,48])await render('favicon/favicon.svg',size,size,`public/brand/favicon/favicon-${size}.png`);
 for(const [name,size]of [['apple-touch-icon',180],['android-chrome-192',192],['android-chrome-512',512]])await render('social/covan-avatar-512.svg',size,size,`public/brand/favicon/${name}.png`);
 for(const size of [512,1024])await render(`social/covan-avatar-${size}.svg`,size,size,`public/brand/social/covan-avatar-${size}.png`);
 await render('social/covan-og-brand.svg',1200,630,'public/brand/social/covan-og-brand.png');
 const imgs=(name)=>[16,24,32,48].map(size=>`<div><img width="${size}" height="${size}" src="${origin}/public/brand/favicon/candidate-${name}-${size}.png"><p>${size}px</p></div>`).join('');
 await p.setViewportSize({width:1000,height:660});await p.setContent(`<style>body{margin:0;font:16px system-ui;background:#08111F;color:#F4F7FA;padding:32px}section{padding:24px;display:flex;gap:48px;align-items:center}p{font-size:12px} .light{background:#F6F8FB;color:#08111F}</style><h2>Favicon · actual pixels</h2><section>A · two-color ${imgs('a')}</section><section>B · monochrome ${imgs('b')}</section><section class="light">A · two-color ${imgs('a')}</section><section class="light">B · monochrome ${imgs('b')}</section><section><span>Inter</span><img width="178" src="${origin}/public/brand/proofs/wordmark-inter.svg"><span>Manrope</span><img width="178" src="${origin}/public/brand/proofs/wordmark-manrope.svg"></section>`);await p.locator('img').evaluateAll(is=>Promise.all(is.map(i=>i.decode())));await p.screenshot({path:'output/playwright/production-favicon-type.png'});
 // Pixel-equivalence proof: same approved source and frozen production art at 512.
 for(const [src,name] of [['/logo/h1-polish/polish-b/mark-primary.svg','approved'],['/public/brand/logo/covan-mark-primary.svg','production']]){
  await p.setViewportSize({width:512,height:512});await p.setContent(`<style>body{margin:0;background:transparent}img{width:512px;height:512px;display:block}</style><img src="${origin}${src}">`);await p.locator('img').evaluate(i=>i.decode());await p.screenshot({path:`output/playwright/master-${name}.png`,omitBackground:true});
 }
 await ctx.close();return {pngExports:count};
}
