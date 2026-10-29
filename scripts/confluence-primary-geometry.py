"""Three clearly different primary interpretations of the same Confluence C.
Master geometry is not constrained by favicon reduction. No font input.
"""
from pathlib import Path
import runpy
H=runpy.run_path(str(Path(__file__).with_name('confluence-flow-geometry.py')))
path,split,reverse=H['path'],H['split'],H['reverse']
VARIANTS=[
 dict(id='01',label='Elegant Flow',description='An elongated, lighter silhouette with a generous counter and a long, graceful lower sweep. The two terminal faces turn toward one another without matching.',character='Tall · slender · fluid',overlap=(.035,.26,.045,.22),bend=(2.5,-2.0),segments=[
 ((82,23),(75,12),(63,7),(49,7)),
 ((49,7),(28,7),(14,26),(14,49)),
 ((14,49),(14,73),(28,91),(49,91)),
 ((49,91),(63,91),(75,86),(82,78)),
 ((82,78),(86,72),(78,67),(71,70)),
 ((71,70),(66,75),(58,78),(50,78)),
 ((50,78),(36,78),(27,65),(27,49)),
 ((27,49),(27,32),(36,19),(50,19)),
 ((50,19),(61,19),(69,23),(74,29)),
 ((74,29),(75.4,33.2),(77,23),(82,23))]),
 dict(id='02',label='Architectural Precision',description='A firm, broad structure with controlled shoulders, a compact counter and an intentional offset between the terminal faces. The confluence is a disciplined curved joint.',character='Structured · firm · precise',overlap=(.14,.06,.06,.17),bend=(1.0,3.0),segments=[
 ((87,28),(79,13),(70,10),(50,10)),
 ((50,10),(18,10),(10,18),(10,50)),
 ((10,50),(10,82),(18,90),(50,90)),
 ((50,90),(70,90),(79,87),(87,72)),
 ((87,72),(85,68),(76,60),(72,62)),
 ((72,62),(67,67),(60,70),(52,70)),
 ((52,70),(34,70),(30,66),(30,50)),
 ((30,50),(30,34),(34,30),(52,30)),
 ((52,30),(60,30),(67,33),(72,38)),
 ((72,38),(73,34),(83,31),(87,28))]),
 dict(id='03',label='Organic Balance',description='A broad upper arc and a fuller, lower-set return create a deliberately asymmetric C. The counter drifts within the outer contour, and the confluence bends into that changing weight.',character='Asymmetric · full · natural',overlap=(.20,.07,.07,.17),bend=(5.0,3.5),segments=[
 ((88,34),(82,16),(71,9),(56,9)),
 ((56,9),(26,9),(9,24),(9,48)),
 ((9,48),(9,75),(23,89),(44,89)),
 ((44,89),(64,89),(75,85),(81,75)),
 ((81,75),(85,69),(80,56),(70,61)),
 ((70,61),(65,65),(59,68),(53,68)),
 ((53,68),(36,68),(27,62),(27,49)),
 ((27,49),(27,33),(42,24),(57,24)),
 ((57,24),(65,24),(71,30),(74,40)),
 ((74,40),(77,44),(82,35),(88,34))]),
]
def construction(v):
 q=v['segments'];tu,tl,ti,tb=v['overlap']
 _,ou=split(q[1],1-tu);ol,_=split(q[2],tl)
 _,il=split(q[6],1-tb);iu,_=split(q[7],ti)
 ot,ob,it,ib=ou[0],ol[-1],iu[-1],il[0];h,k=v['bend']
 # Actual shared region, with curved joins across the two source ribbons.
 dx=(it[0]-ot[0]);dy=(ib[0]-ob[0])
 upper=(ot,(ot[0]+dx*.28,ot[1]+h),(it[0]-dx*.28,it[1]+k),it)
 lower=(ob,(ob[0]+dy*.28,ob[1]+h),(ib[0]-dy*.28,ib[1]+k),ib)
 a=[q[0],q[1],ol,lower,il,q[7],q[8],q[9]]
 b=[ou,q[2],q[3],q[4],q[5],q[6],iu,reverse(upper)]
 overlap=[ou,ol,lower,il,iu,reverse(upper)]
 return dict(merged=path(q,True),origin_a=path(a,True),origin_b=path(b,True),confluence=path(overlap,True),segments=q,upper_seam=upper,lower_seam=lower,outer_join=q[1][3],inner_join=q[6][3],upper_cap=path([q[9]]),lower_cap=path([q[4]]))
