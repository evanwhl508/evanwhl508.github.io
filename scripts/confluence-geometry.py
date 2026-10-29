"""Confluence C: paired circular bodies, custom Bezier terminal relationship.
No typography, font outlines or external geometry packages enter this module.
"""
from pathlib import Path
import runpy,math
BASE=runpy.run_path(str(Path(__file__).with_name('two-origin-geometry.py')))
xy=BASE['xy'];point=BASE['point']
# Two references, four terminal treatments. Body radii stay fixed by reference.
VARIANTS=[
 dict(id='01',reference='01',label='Cupped opening',upper_controls=[(75.8,34.0),(81.0,31.4)],lower_controls=[(79.2,66.8),(75.7,63.0)],description='A concave upper cut receives the convex lower return. Their unequal lengths create one gently leaning opening.'),
 dict(id='02',reference='01',label='Shared inflection',upper_controls=[(79.0,40.0),(77.5,28.0)],lower_controls=[(78.5,67.4),(72.0,64.2)],description='A shallow reverse curve at the upper terminal is answered by a quieter lower transition. The two faces carry the same directional flow.'),
 dict(id='03',reference='04',label='Staggered return',upper_controls=[(78.0,37.7),(83.6,36.5)],lower_controls=[(80.0,69.0),(74.0,62.4)],description='The upper curve reaches farther; the lower curve returns toward it with a rounded shoulder. The opening is intentionally off-axis.'),
 dict(id='04',reference='04',label='Swept opening',upper_controls=[(81.0,41.0),(81.8,36.0)],lower_controls=[(79.2,71.0),(72.4,62.2)],description='A restrained reverse curve above and a longer sweep below give the opening a continuous, asymmetric rhythm.'),
]
def construction(v):
    ref=next(x for x in BASE['VARIANTS'] if x['id']==v['reference']);d=BASE['construction'](ref)
    ou,inu=d['upper_terminal'];od,ind=d['lower_terminal'];o=d['outer_join'];i=d['inner_join']
    u,l,iu,il=ref['upper'],ref['lower'],ref['inner_upper'],ref['inner_lower']
    uc=v['upper_controls'];lc=v['lower_controls']
    uppercap=f'C{xy(uc[0])} {xy(uc[1])} {xy(ou)}'
    lowercap=f'C{xy(lc[0])} {xy(lc[1])} {xy(ind)}'
    upperoutside=f'M{xy(ou)}A{u} {u} 0 0 0 {xy(o)}'
    loweroutside=f'A{l} {l} 0 0 0 {xy(od)}'
    lowerinside=f'{lowercap}A{il} {il} 0 0 1 {xy(i)}'
    upperinside=f'A{iu} {iu} 0 0 1 {xy(inu)}{uppercap}Z'
    d.update(merged=upperoutside+loweroutside+lowerinside+upperinside,
      origin_a=upperoutside+f'L{xy(i)}'+upperinside,
      origin_b=f'M{xy(o)}'+loweroutside+lowerinside+'Z',
      upper_cap=f'M{xy(inu)}'+uppercap,lower_cap=f'M{xy(od)}'+lowercap,
      upper_controls=uc,lower_controls=lc,reference=ref)
    # The color zone is a short annular section centred on the real shared join.
    # A broad sector defines the fill partition; only its intersection with the
    # complete silhouette is painted. No line is added to the contour.
    center=(50,50)
    def sector(start,end):
        a=point(*center,150,start);b=point(*center,150,end)
        return f'M50 50L{xy(a)}A150 150 0 0 1 {xy(b)}Z'
    d['confluence_zone']=sector(160,200)
    # Alternate: one source starts in aqua at the upper mouth, then joins white.
    d['origin_zone']=sector(278,360)
    return d
