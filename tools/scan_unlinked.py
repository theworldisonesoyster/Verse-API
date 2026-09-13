# -*- coding: utf-8 -*-
"""扫描成员表未链接的父页"""
import glob
import os
import re

bad = []
for p in glob.glob('0[123]*/**/*.md', recursive=True):
    if p.endswith('_overview.md'):
        continue
    s = open(p, encoding='utf-8').read()
    if '### Functions' not in s and '### Data' not in s:
        continue
    in_tbl = False
    for ln in s.splitlines():
        if ln.startswith('### '):
            t = ln[4:].strip().lower()
            in_tbl = t in ('data', 'functions')
            continue
        if in_tbl and ln.startswith('| ') and not ln.startswith('| Name') \
                and not ln.startswith('| Data Member') and not ln.startswith('| Function'):
            first = ln.split('|')[1].strip()
            if first and not first.startswith('[') and not first.startswith('-') \
                    and re.search(r'[A-Za-z]{3}', first):
                bad.append((p.replace(os.sep, '/'), first))
                break
for p, n in bad[:20]:
    print(p, '|', n)
print('未链接父页数:', len(bad))
