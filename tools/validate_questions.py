#!/usr/bin/env python3
"""Dependency-free structural check for the Q&A Markdown. Not a translation verifier."""
from pathlib import Path
import re,sys
p=Path(__file__).resolve().parents[1]/'QUESTIONS_128_zh_CN.md'
s=p.read_text(encoding='utf-8')
sections=re.split(r'(?=^### (\d{1,3})\. )',s,flags=re.M)
nums=[int(v) for v in sections[1::2]]
assert nums==list(range(1,129)),f'Question-number sequence invalid: {nums}'
answers=[]
for content in sections[2::2]:
    lst=[z for z in content.splitlines() if z.startswith('- ')]
    assert len(lst)>0
    answers.append(len(lst))
assert sum(answers)==411,f'Expected 411 answer alternatives, found {sum(answers)}'
starred=[int(i) for i,line in re.findall(r'^### (\d+)\. (.+)$',s,flags=re.M) if line.endswith('*')]
assert starred==[2,7,12,20,30,36,38,39,44,52,61,66,74,78,86,94,113,115,121,126],f'Asterisk questions changed: {starred}'
assert '投票不需要缴纳人头税。' in s
assert '投票无需缴费' not in s
assert '如需查询美国总统的姓名，请访问。' not in s
print('PASS: 128 questions; 411 nonempty answers; 20 starred questions; targeted corrections present')
