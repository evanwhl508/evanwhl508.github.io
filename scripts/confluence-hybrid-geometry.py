"""Three hybrids of Elegant Flow. Organic tension, restrained structural discipline.
All contours are direct SVG geometry; no typography input and no Micro C edits.
"""
from pathlib import Path
import runpy
P=runpy.run_path(str(Path(__file__).with_name('confluence-primary-geometry.py')))
VARIANTS=[
 dict(id='h1',label='Elegant Hybrid',description='Closest to Elegant Flow: a tall, open silhouette with a slightly firmer spine, a gently drifting counter and a restrained upper terminal. The lower return stays light and extended.',character='Closest to 01 · open · graceful',overlap=(.03,.23,.04,.18),bend=(2.0,-1.5),segments=[
 ((81.5,24),(74.5,12),(63.5,7),(50,7)),
 ((50,7),(28.5,7),(14,25.5),(14,49)),
 ((14,49),(14,73),(28,91),(48.5,91)),
 ((48.5,91),(62,91),(74.8,86),(81.5,78)),
 ((81.5,78),(85.2,72.5),(77.2,67.5),(70.8,70.2)),
 ((70.8,70.2),(65.4,75.2),(57.8,77.5),(49.8,77.5)),
 ((49.8,77.5),(36.2,77.5),(27.8,65),(27.8,49.5)),
 ((27.8,49.5),(27.8,32.4),(37.8,19.3),(51.4,19.3)),
 ((51.4,19.3),(61.4,19.3),(69,24.0),(73.4,30.6)),
 ((73.4,30.6),(75.2,33.0),(77.0,24.7),(81.5,24))]),
 dict(id='h2',label='Signature Hybrid',description='The opening is more deliberate: a compact receiving curve above and a longer inward return below. A shifted counter adds organic tension while the slender body and light lower sweep remain anchored in Elegant Flow.',character='Expressive opening · organic tension',overlap=(.05,.23,.06,.18),bend=(3.0,-1.6),segments=[
 ((81,29),(75,14),(64,7),(51,7)),
 ((51,7),(29,7),(14,25),(14,48)),
 ((14,48),(14,72),(27.8,91),(47.8,91)),
 ((47.8,91),(62,91),(75,84.5),(81.5,75.5)),
 ((81.5,75.5),(85,69.4),(76.5,63.6),(69.7,66.8)),
 ((69.7,66.8),(64.7,72.7),(57.6,77.0),(49.1,77.0)),
 ((49.1,77.0),(36.2,77.0),(28,64.0),(28,50)),
 ((28,50),(28,34),(39.8,20.0),(53,20.0)),
 ((53,20.0),(62.8,20.0),(68.1,27.8),(72,35.5)),
 ((72,35.5),(73.8,36.4),(76.6,30.5),(81,29))]),
 dict(id='h3',label='Structured Hybrid',description='A balanced oval skeleton and cleaner terminal faces add technical composure. The body stays tall and light, with a controlled lower return and just enough counter asymmetry to avoid a mechanical ring.',character='Disciplined curves · light structure',overlap=(.04,.22,.035,.19),bend=(1.8,-2.0),segments=[
 ((82,25.5),(75.0,13.3),(63,7.5),(49.5,7.5)),
 ((49.5,7.5),(28.0,7.5),(14,26.0),(14,49)),
 ((14,49),(14,72.0),(28.0,90.5),(49.0,90.5)),
 ((49.0,90.5),(63,90.5),(75.0,84.6),(82,77)),
 ((82,77),(84,73.0),(77.0,67.4),(72.0,68.5)),
 ((72.0,68.5),(66.8,74.0),(58.5,76.8),(50.1,76.8)),
 ((50.1,76.8),(36.8,76.8),(28,64.5),(28,49)),
 ((28,49),(28,32.5),(37.1,20.3),(50.5,20.3)),
 ((50.5,20.3),(60.7,20.3),(68.1,25.0),(73.2,31.3)),
 ((73.2,31.3),(75.0,28.5),(79.2,27.6),(82,25.5))]),
]
def construction(v):
 return P['construction'](v)
