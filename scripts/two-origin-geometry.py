"""Font-independent two-origin C geometry. Two eccentric circular ribbons share a spine."""
import math
VARIANTS=[
 dict(id='01',label='Upper sweep',left=10,spine=30,y=50,upper=41,lower=37,inner_upper=28,inner_lower=27,opening_upper=32,opening_lower=36,offset_upper=8,offset_lower=8),
 dict(id='02',label='Lower sweep',left=11,spine=31,y=50,upper=39,lower=40,inner_upper=27,inner_lower=29,opening_upper=36,opening_lower=32,offset_upper=10,offset_lower=9),
 dict(id='03',label='Deeper counter',left=10,spine=33,y=50,upper=40,lower=38,inner_upper=28,inner_lower=27,opening_upper=32,opening_lower=36,offset_upper=11,offset_lower=10),
 dict(id='04',label='Inclined opening',left=10,spine=30,y=50,upper=40,lower=38,inner_upper=28,inner_lower=27,opening_upper=22,opening_lower=44,offset_upper=8,offset_lower=10),
 dict(id='05',label='Open crown',left=10,spine=31,y=50,upper=40,lower=38,inner_upper=27,inner_lower=26,opening_upper=40,opening_lower=30,offset_upper=10,offset_lower=8),
]
def n(x):return f'{x:.5f}'.rstrip('0').rstrip('.')
def xy(p):return ' '.join(n(z) for z in p)
def point(cx,cy,r,angle):
    a=math.radians(angle);return cx+r*math.cos(a),cy+r*math.sin(a)
def construction(v):
    l,i,y=v['left'],v['spine'],v['y'];u,d,iu,id=v['upper'],v['lower'],v['inner_upper'],v['inner_lower']
    ou=point(l+u,y,u,-v['opening_upper']);od=point(l+d,y,d,v['opening_lower'])
    hu,hd=v['offset_upper'],v['offset_lower']
    cu=(i+math.sqrt(iu*iu-hu*hu),y+hu);cd=(i+math.sqrt(id*id-hd*hd),y-hd)
    au=math.degrees(math.atan2(ou[1]-cu[1],ou[0]-cu[0]))
    ad=math.degrees(math.atan2(od[1]-cd[1],od[0]-cd[0]))
    inu=point(*cu,iu,au);ind=point(*cd,id,ad)
    outside=(l,y);inside=(i,y)
    upper_outer=f'M{xy(ou)}A{u} {u} 0 0 0 {xy(outside)}'
    lower_outer=f'A{d} {d} 0 0 0 {xy(od)}'
    lower_inner=f'L{xy(ind)}A{id} {id} 0 0 1 {xy(inside)}'
    upper_inner=f'A{iu} {iu} 0 0 1 {xy(inu)}Z'
    a=upper_outer+f'L{xy(inside)}'+upper_inner
    b=f'M{xy(outside)}'+lower_outer+lower_inner+'Z'
    merged=upper_outer+lower_outer+lower_inner+upper_inner
    return dict(origin_a=a,origin_b=b,merged=merged,outer_join=outside,inner_join=inside,upper_terminal=[ou,inu],lower_terminal=[od,ind],circles=[dict(label='Upper outer',cx=l+u,cy=y,r=u),dict(label='Upper inner',cx=cu[0],cy=cu[1],r=iu),dict(label='Lower outer',cx=l+d,cy=y,r=d),dict(label='Lower inner',cx=cd[0],cy=cd[1],r=id)])
