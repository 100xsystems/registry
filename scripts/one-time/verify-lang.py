#!/usr/bin/env python3
"""Generic verification for a generated language curriculum.

Usage: python3 verify-lang.py <lang_dir_relative> [code_fence] [slug_prefix]
Example: python3 verify-lang.py static-data/knowledge/languages/php php php-

Checks:
  1. index.json has `lessons` and `categories`; lesson file count matches lessons array
  2. Every lesson file has valid JSON frontmatter (--- {json} ---)
  3. Every lesson references exactly 4 code blocks with the given fence
  4. Slug prefixes in filenames match the lessons array
"""
import json
import os
import re
import sys

base = sys.argv[1]
fence = sys.argv[2] if len(sys.argv) > 2 else 'code'
prefix = sys.argv[3] if len(sys.argv) > 3 else ''

idx = json.load(open(os.path.join(base, 'index.json')))
lessons = idx.get('lessons', [])
categories = idx.get('categories', [])
slugs = [l['slug'] for l in lessons]

print(f'index.json lessons: {len(lessons)} | categories: {len(categories)}')

# 1. file count matches
md_files = sorted(f for f in os.listdir(base) if f.endswith('.md'))
expected = [f'{s}.md' for s in slugs]
missing = [e for e in expected if e not in md_files]
extra = [f for f in md_files if f not in expected]
print(f'lesson files on disk: {len(md_files)} | missing: {missing} | extra: {extra}')

# 2. frontmatter validity + 3. code block count + 4. prefix check
fail = 0
for slug in slugs:
    path = os.path.join(base, f'{slug}.md')
    if not os.path.exists(path):
        print(f'MISSING FILE {slug}')
        fail += 1
        continue
    s = open(path).read()
    m = re.match(r'^---\n(.*?)\n---', s, re.S)
    if not m:
        print(f'NO FRONTMATTER {slug}')
        fail += 1
        continue
    try:
        fm = json.loads(m.group(1))
    except Exception as e:
        print(f'INVALID FRONTMATTER JSON {slug}: {e}')
        fail += 1
        continue
    if not prefix or slug.startswith(prefix):
        pass
    else:
        print(f'SLUG PREFIX MISMATCH {slug} (expected {prefix}*)')
        fail += 1
    blocks = re.findall(rf'```{fence}\n', s)
    if len(blocks) != 4:
        print(f'CODE BLOCKS {len(blocks)} (expected 4) in {slug}')
        fail += 1
    # knowledge_refs / prerequisites conventions
    krefs = fm.get('knowledge_refs', [])
    for k in krefs:
        if not k.startswith(os.path.basename(base) + '/'):
            print(f'KNOWLEDGE_REF MISMATCH {slug}: {k}')
            fail += 1

if fail:
    print(f'VERIFY FAILED: {fail} problems')
    sys.exit(1)
print('ALL CHECKS PASSED')
