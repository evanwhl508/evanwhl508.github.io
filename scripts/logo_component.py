"""Static-site Logo component; shared asset mapping, never duplicated geometry."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
BASE='/public/brand/'

def logo(variant='primary', layout='horizontal', size='md', decorative=False):
    if variant not in ('primary','light','white','navy','monochrome'):raise ValueError(variant)
    if layout not in ('mark','horizontal','stacked','localized'):raise ValueError(layout)
    heights={'xs':24,'sm':32,'md':40,'lg':64,'xl':128}
    h=heights[size]
    if layout=='mark':
        if h<64:
            ink={'primary':'primary','light':'light','white':'monochrome','navy':'navy','monochrome':'navy'}[variant]
            path=f'micro/covan-mark-micro-{ink}.svg'
        else:
            ink='navy' if variant=='monochrome' else variant
            path=f'logo/covan-mark-{ink}.svg'
    else:
        ink={'primary':'dark','light':'light','white':'white','navy':'monochrome','monochrome':'monochrome'}[variant]
        path=f'logo/covan-logo-{layout}-{ink}.svg'
        # Do not silently shrink a full lockup below its tested minimum.
        h=max(h,36 if layout=='horizontal' else 60 if layout=='localized' else 144)
    box=list(map(float,ET.parse(ROOT/'public/brand'/path).getroot().get('viewBox').split()))
    w=round(h*box[2]/box[3],2)
    return f'<img class="covan-logo covan-logo--{layout}" src="{BASE+path}" width="{w}" height="{h}" alt="{escape("" if decorative else "Covan Labs")}">'
