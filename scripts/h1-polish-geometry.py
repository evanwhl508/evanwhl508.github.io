"""H1 master: unchanged benchmark plus two optical-polish alternatives.
Area is integrated from cubic paths; no raster-size optimization or font input.
"""
from pathlib import Path
import runpy,copy,math
H=runpy.run_path(str(Path(__file__).with_name('confluence-hybrid-geometry.py')))
P=H['P'];split,path,reverse=P['split'],P['path'],P['reverse']
MASTER=H['construction'](H['VARIANTS'][0])
VARIANTS=[dict(id='benchmark',label='H1 benchmark',description='The selected H1 master, preserved exactly.'),dict(id='polish-a',label='Polish A',description='The exact H1 silhouette with more fluid confluence boundaries. The aqua area is retained.'),dict(id='polish-b',label='Polish B',description='Polish A’s confluence, lifted by 0.5 design units, with a 2.5% reduction in the defined lower-terminal area. The outer body curves and tall proportions stay fixed.')]
def point(q,t):return split(q,t)[0][-1]
def coeff(q,axis):
 a,b,c,d=[p[axis] for p in q];return [a,3*(b-a),3*(c-2*b+a),d-3*c+3*b-a]
def cubic_area(q):
 x,y=coeff(q,0),coeff(q,1);total=0
 for i in range(4):
  for j in range(1,4):total+=(x[i]*j*y[j]-y[i]*j*x[j])/(i+j)
 return total/2

def area(qs):
 a,b=qs[-1][-1],qs[0][0]
 return abs(sum(cubic_area(q) for q in qs)+(a[0]*b[1]-a[1]*b[0])/2)
def at(q,axis,value):
 lo,hi=0.,1.;rising=q[-1][axis]>q[0][axis]
 for _ in range(60):
  mid=(lo+hi)/2
  if (point(q,mid)[axis]<value)==rising:lo=mid
  else:hi=mid
 return (lo+hi)/2

def source_parts(q,ts):
 tu,tl,ti,tb=ts
 _,ou=split(q[1],1-tu);ol,_=split(q[2],tl)
 _,il=split(q[6],1-tb);iu,_=split(q[7],ti)
 return ou,ol,il,iu

def overlap_curves(parts,upper,lower):
 ou,ol,il,iu=parts;return [ou,ol,lower,il,iu,reverse(upper)]
def reattach(q,upper,lower,upper_dy,lower_dy):
 ot,ob,it,ib=upper[0],lower[0],upper[-1],lower[-1]
 ts=(1-at(q[1],1,ot[1]+upper_dy),at(q[2],1,ob[1]+lower_dy),at(q[7],1,it[1]+upper_dy),1-at(q[6],1,ib[1]+lower_dy))
 parts=source_parts(q,ts);ou,ol,il,iu=parts
 def move(seam,start,end):
  da=tuple(start[i]-seam[0][i] for i in (0,1));db=tuple(end[i]-seam[-1][i] for i in (0,1))
  return (start,tuple(seam[1][i]+da[i] for i in (0,1)),tuple(seam[2][i]+db[i] for i in (0,1)),end)
 return parts,move(upper,ou[0],iu[-1]),move(lower,ol[-1],il[0])
def area_equalize(q,upper,lower,target):
 # Reattach endpoints symmetrically along the real contours. Control vectors
 # stay fixed, retaining the edited seam tangent directions and exact area.
 def trial(t):
  parts,up,low=reattach(q,upper,lower,t,-t)
  return area(overlap_curves(parts,up,low)),parts,up,low
 lo,hi=-2.,2.;assert trial(lo)[0]>target>trial(hi)[0]
 for _ in range(60):
  mid=(lo+hi)/2
  if trial(mid)[0]>target:lo=mid
  else:hi=mid
 t=(lo+hi)/2;value,parts,up,low=trial(t);assert abs(value-target)<1e-7
 return parts,up,low,t

def lower_terminal_area(q):
 # A fixed x=65 plane isolates the forward lower return from the body.
 _,outer=split(q[3],at(q[3],0,65));inner,_=split(q[5],at(q[5],0,65))
 return area([outer,q[4],inner])
def lighter_terminal(q):
 q=copy.deepcopy(q);start=lower_terminal_area(q);inside=q[4][3];outside=q[4][0]
 direction=(outside[0]-inside[0],outside[1]-inside[1])
 def shifted(t):
  out=copy.deepcopy(q);delta=(direction[0]*t,direction[1]*t)
  def move(p):return (p[0]+delta[0],p[1]+delta[1])
  out[4]=(q[4][0],q[4][1],move(q[4][2]),move(q[4][3]))
  out[5]=(move(q[5][0]),move(q[5][1]),q[5][2],q[5][3]);return out
 lo,hi=0,.2
 assert lower_terminal_area(shifted(hi))<start*.975
 for _ in range(60):
  mid=(lo+hi)/2
  if lower_terminal_area(shifted(mid))>start*.975:lo=mid
  else:hi=mid
 out=shifted((lo+hi)/2)
 return out,dict(region='lower terminal, x >= 65 in 100-unit design space',before=start,after=lower_terminal_area(out),reduction_percent=2.5,inner_terminal_shift=[out[4][3][i]-q[4][3][i] for i in (0,1)])

def construction(v):
 q=copy.deepcopy(MASTER['segments']);ts=H['VARIANTS'][0]['overlap'];parts=source_parts(q,ts)
 original_area=area(overlap_curves(parts,MASTER['upper_seam'],MASTER['lower_seam']))
 if v['id']=='benchmark':
  return {**copy.deepcopy(MASTER),'aqua_exact_area':original_area,'filled_exact_area':area(q),'polish':{'benchmark_exact':True,'upward_shift':0,'lower_terminal_reduction':0}}
 upper=MASTER['upper_seam'];lower=MASTER['lower_seam']
 # Modest movement towards the local source-contour tangent directions.
 # Preserve both seam endpoints and compensate total overlap area exactly.
 targets=((13.95,49.3),(28.04,44.5),(17.2,67.8),(29.2,60.5))
 def blend(p,t,amount=.30):return tuple(p[i]+amount*(t[i]-p[i]) for i in (0,1))
 upper=(upper[0],blend(upper[1],targets[0]),blend(upper[2],targets[1]),upper[3])
 lower=(lower[0],blend(lower[1],targets[2]),blend(lower[2],targets[3],.70),lower[3])
 parts,upper,lower,compensation=area_equalize(q,upper,lower,original_area)
 metadata={'benchmark_exact':False,'upward_shift':0,'lower_terminal_reduction':0,'area_compensation_boundary_shift':compensation}
 if v['id']=='polish-b':
  q,terminal=lighter_terminal(q);metadata['terminal_measurement']=terminal;metadata['lower_terminal_reduction']=2.5;metadata['upward_shift']=.5
  # A half-unit lift along the same spine, retaining A's seam flow.
  parts,upper,lower=reattach(q,upper,lower,-.5,-.5)
  parts,upper,lower,offset=area_equalize(q,upper,lower,original_area)
  metadata['lift_area_compensation_boundary_shift']=offset
 ou,ol,il,iu=parts
 a=[q[0],q[1],ol,lower,il,q[7],q[8],q[9]]
 b=[ou,q[2],q[3],q[4],q[5],q[6],iu,reverse(upper)]
 overlap=overlap_curves(parts,upper,lower)
 return dict(merged=path(q,True),origin_a=path(a,True),origin_b=path(b,True),confluence=path(overlap,True),segments=q,upper_seam=upper,lower_seam=lower,outer_join=q[1][-1],inner_join=q[6][-1],upper_cap=path([q[9]]),lower_cap=path([q[4]]),aqua_exact_area=area(overlap),filled_exact_area=area(q),polish=metadata)
