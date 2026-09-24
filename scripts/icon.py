"""Rasterize Stufo's original vector mark for Apple's required app-icon asset."""
from pathlib import Path
import json, math
from PIL import Image, ImageDraw
r=Path(__file__).resolve().parents[1]
paths=[]
for row in range(15):
    points=[]
    for i in range(161):
        t=i/160
        x=160+t*704
        y=512+math.sin(t*math.pi*3.2+row*0.23)*math.sin(t*math.pi)**1.3*(130+row*11)
        points.append(f'{"M" if i==0 else "L"}{x:.2f},{y:.2f}')
    paths.append(f'<path d="{" ".join(points)}" fill="none" stroke="#202722" stroke-width="11" stroke-linecap="round" opacity="{.35+row*.043:.3f}"/>')
svg='<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#C9ED5C"/>'+''.join(paths)+'</svg>'
(r/'scripts/mark.svg').write_text(svg)
im=Image.new('RGB',(2048,2048),'#C9ED5C')
for row in range(15):
    layer=Image.new('RGBA',im.size)
    draw=ImageDraw.Draw(layer)
    points=[]
    for i in range(641):
        t=i/640
        x=(160+t*704)*2
        y=(512+math.sin(t*math.pi*3.2+row*0.23)*math.sin(t*math.pi)**1.3*(130+row*11))*2
        points.append((x,y))
    draw.line(points,fill=(32,39,34,int(255*(.35+row*.043))),width=22,joint='curve')
    im=Image.alpha_composite(im.convert('RGBA'),layer).convert('RGB')
im.resize((1024,1024),Image.Resampling.LANCZOS).save(r/'Stufo/Assets.xcassets/AppIcon.appiconset/AppIcon.png')
(r/'Stufo/Assets.xcassets/Contents.json').write_text(json.dumps({'info':{'author':'xcode','version':1}},indent=2))
(r/'Stufo/Assets.xcassets/AppIcon.appiconset/Contents.json').write_text(json.dumps({'images':[{'filename':'AppIcon.png','idiom':'universal','platform':'ios','size':'1024x1024'}],'info':{'author':'xcode','version':1}},indent=2))
print('Created vector mark and opaque 1024px icon')
