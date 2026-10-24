"""Three optically drawn Confluence C refinements. No font or circle subtraction.
The two source ribbons overlap; their exact intersection is the aqua transition.
Every outer/inner join through the spine is tangent-continuous.
"""
def n(v): return f'{v:.6f}'.rstrip('0').rstrip('.')
def xy(p): return ' '.join(n(v) for v in p)
def mix(a,b,t):return tuple(x+(y-x)*t for x,y in zip(a,b))
def split(q,t):
    a,b,c=mix(q[0],q[1],t),mix(q[1],q[2],t),mix(q[2],q[3],t)
    d,e=mix(a,b,t),mix(b,c,t);f=mix(d,e,t)
    return (q[0],a,d,f),(f,e,c,q[3])
def reverse(q):return tuple(reversed(q))
def path(qs,close=False):
    return 'M'+xy(qs[0][0])+''.join('C'+' '.join(xy(p) for p in q[1:]) for q in qs)+('Z' if close else '')
VARIANTS=[
 dict(id='a',label='Balanced',spine=31.2,crown=(56.8,28.8),bowl=(55.8,67.8),upper_outer=(85.0,28.8),upper_inner=(76.2,37.7),lower_outer=(78.0,72.2),lower_inner=(71.4,63.5),upper_controls=((78.3,38.6),(78.8,30.1)),lower_controls=((81.1,68.1),(76.4,62.8)),flow=.0,overlap=.105,description='A quiet receiving cut above, a fuller returning curve below. The two directions frame a gently offset passage through the C.'),
 dict(id='b',label='Flowing',spine=31.4,crown=(56.9,28.6),bowl=(55.7,67.6),upper_outer=(85.5,30.1),upper_inner=(76.9,38.8),lower_outer=(78.2,73.1),lower_inner=(71.0,63.1),upper_controls=((79.2,39.3),(79.8,31.7)),lower_controls=((82.1,68.0),(76.2,61.7)),flow=1.1,overlap=.106,description='The lower return reaches farther into the opening while the upper terminal stays compact. A slightly longer inward sweep carries the restrained influence of study 04.'),
 dict(id='c',label='Minimal',spine=31.0,crown=(56.8,28.9),bowl=(55.8,67.9),upper_outer=(84.9,28.8),upper_inner=(76.1,37.6),lower_outer=(77.7,72.0),lower_inner=(71.5,63.6),upper_controls=((77.1,33.3),(80.9,31.7)),lower_controls=((79.9,68.4),(75.9,63.3)),flow=-.4,overlap=.106,description='The same offset passage, with the reverse bend removed from the upper cut. The simpler terminal face keeps the silhouette clear at 16–24px.'),
]
def construction(v):
    u,ui,l,li=v['upper_outer'],v['upper_inner'],v['lower_outer'],v['lower_inner']
    spine=v['spine'];crown=v['crown'];bowl=v['bowl'];f=v['flow']
    # Clockwise walk around the filled silhouette (outer then inner).
    q=[(u,(78.0,16.1),(65.2,9),(51,9)),
       ((51,9),(28.35,9),(10,27.35),(10,50)),
       ((10,50),(10,70.45),(26.55,87),(47,87)),
       ((47,87),(60.0,87),(71.4,81.3+f),l),
       (l,*v['lower_controls'],li),
       (li,(67.1,66.4-f), (61.0, bowl[1]),bowl),
       (bowl,(42.5,bowl[1]),(spine,61.5),(spine,50)),
       ((spine,50),(spine,37.2),(43.9,crown[1]),crown),
       (crown,(64.0,crown[1]),(71.1,32.1-f*.25),ui),
       (ui,*v['upper_controls'],u)]
    t=v['overlap']
    # Split both spine contours to build an actual overlapping source union.
    ou_before,ou_overlap=split(q[1],1-t)
    ol_overlap,ol_after=split(q[2],t)
    il_before,il_overlap=split(q[6],1-t)
    iu_overlap,iu_after=split(q[7],t)
    ot,ob=ou_overlap[0],ol_overlap[-1]
    it,ib=iu_overlap[-1],il_overlap[0]
    # Two softly S-curved boundaries replace the earlier radial straight seams.
    # Matching x-progress keeps a short ribbon overlap, never a pie wedge.
    upper_seam=(ot,(ot[0]+6,ot[1]+4.0),(it[0]-6,it[1]-4.0),it)
    lower_seam=(ob,(ob[0]+6,ob[1]+4.0),(ib[0]-6,ib[1]-4.0),ib)
    a=[q[0],q[1],ol_overlap,lower_seam,il_overlap,q[7],q[8],q[9]]
    b=[ou_overlap,q[2],q[3],q[4],q[5],q[6],iu_overlap,reverse(upper_seam)]
    overlap=[ou_overlap,ol_overlap,lower_seam,il_overlap,iu_overlap,reverse(upper_seam)]
    return dict(merged=path(q,True),origin_a=path(a,True),origin_b=path(b,True),confluence=path(overlap,True),segments=q,upper_seam=upper_seam,lower_seam=lower_seam,outer_join=(10,50),inner_join=(spine,50),upper_cap=path([q[-1]]),lower_cap=path([q[4]]),reference='Confluence 02; restrained opening influence from 04',optical_stations={'spine':round(spine-10,2),'crown':round(crown[1]-9,2),'lower_sweep':round(87-bowl[1],2)})
