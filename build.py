#!/usr/bin/env python3
# Rebuild index.html from template.html + board.css + bgm.b64 + imgs.json
css=open('board.css').read()
bgm=open('bgm.b64').read().strip()
imgs=open('imgs.json').read().strip()
reveal=open('reveal.b64').read().strip()
result=open('result.b64').read().strip()
html=open('template.html').read()
for ph in ('__CSS__','__IMGS_JSON__'):
    assert ph in html, f'missing {ph}'
html=html.replace('__CSS__',css).replace('__IMGS_JSON__',imgs)  # 音源は bgm.mp3/reveal.mp3/result.mp3（進行役だけ読み込む）
open('index.html','w').write(html)
print('index.html rebuilt:', round(len(html)/1024),'KB')
