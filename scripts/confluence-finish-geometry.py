"""Only optical finishing of the owner's selected A base. No new concepts."""
from pathlib import Path
import runpy,copy
BASE=runpy.run_path(str(Path(__file__).with_name('confluence-flow-geometry.py')))
path,split,reverse=BASE['path'],BASE['split'],BASE['reverse']
VARIANTS=[dict(id='a1',label='Current benchmark',description='The selected A geometry, preserved exactly.'),dict(id='a2',label='Refined confluence',description='The same silhouette, with a slightly smaller overlap and curved seams that rise naturally through the spine.'),dict(id='a3',label='Refined silhouette',description='A2’s confluence with a slightly tighter upper terminal and 2.5% less width. The fuller lower return is retained.')]
def construction(v):
 d=copy.deepcopy(BASE['construction'](BASE['VARIANTS'][0]))
 if v['id']=='a1':
  d.update(horizontal_scale=1.0,benchmark_exact=True);return d
 q=d['segments']
 if v['id']=='a3':
  # Shorten the small upper reverse bend; leave the outer reach/lower return intact.
  ui=(76.0,37.35);q[8]=(*q[8][:3],ui);q[9]=(ui,(77.65,37.8),(79.1,30.15),q[9][3])
 # The overlap travels gently upward across the spine. Independent inner and
 # outer endpoints avoid the previous nearly horizontal, parallel band.
 _,ou=split(q[1],1-.065);ol,_=split(q[2],.10)
 _,il=split(q[6],1-.02);iu,_=split(q[7],.20)
 ot,ob,it,ib=ou[0],ol[-1],iu[-1],il[0]
 upper=(ot,(ot[0]+5,ot[1]+1.3),(it[0]-5,it[1]+.8),it)
 lower=(ob,(ob[0]+6,ob[1]+.7),(ib[0]-5,ib[1]+.4),ib)
 a=[q[0],q[1],ol,lower,il,q[7],q[8],q[9]]
 b=[ou,q[2],q[3],q[4],q[5],q[6],iu,reverse(upper)]
 overlap=[ou,ol,lower,il,iu,reverse(upper)]
 scale=.975 if v['id']=='a3' else 1
 def point(p):return (47.5+(p[0]-47.5)*scale,p[1])
 def curve(c):return tuple(point(p) for p in c)
 q=[curve(c) for c in q];upper=curve(upper);lower=curve(lower)
 d.update(merged=path(q,True),origin_a=path([curve(c) for c in a],True),origin_b=path([curve(c) for c in b],True),confluence=path([curve(c) for c in overlap],True),segments=q,upper_seam=upper,lower_seam=lower,outer_join=point(d['outer_join']),inner_join=point(d['inner_join']),upper_cap=path([q[-1]]),lower_cap=path([q[4]]),horizontal_scale=scale,benchmark_exact=False)
 return d
