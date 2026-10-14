#!/usr/bin/env python3
# Rebuild index.html from template.html + board.css + bgm.b64 + imgs.json
css=open('board.css').read()
bgm=open('bgm.b64').read().strip()
imgs=open('imgs.json').read().strip()
reveal=open('reveal.b64').read().strip()
result=open('result.b64').read().strip()
html=open('template.html').read()
for ph in ('__CSS__','__BGM_B64__','__IMGS_JSON__','__REVEAL_B64__','__RESULT_B64__'):
    assert ph in html, f'missing {ph}'
html=(html.replace('__CSS__',css).replace('__BGM_B64__',bgm).replace('__IMGS_JSON__',imgs)
      .replace('__REVEAL_B64__',reveal).replace('__RESULT_B64__',result))
open('index.html','w').write(html)
print('index.html rebuilt:', round(len(html)/1024),'KB')
