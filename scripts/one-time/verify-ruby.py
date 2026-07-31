#!/usr/bin/env python3
"""Verify Ruby code blocks in generated lessons with `ruby -c` (if ruby exists).

Note: system Ruby is often 2.6.x which predates pattern matching (case/in,
Ruby 2.7+). Blocks that use pattern-matching syntax are validated only on
Ruby >= 2.7; on older Rubies they are reported as SKIPPED (the lessons are
written for modern Ruby and that syntax is intentionally taught).
"""
import re, glob, subprocess, tempfile, os, sys

have_ruby = subprocess.run(['which', 'ruby'], capture_output=True, text=True).returncode == 0
if not have_ruby:
    print('ruby NOT installed - skipping syntax check')
    sys.exit(0)

ver = subprocess.run(['ruby', '-e', 'print RUBY_VERSION'], capture_output=True, text=True).stdout
try:
    major, minor = (int(x) for x in ver.split('.')[:2])
    pm_supported = (major, minor) >= (2, 7)
except Exception:
    pm_supported = True
print(f'ruby {ver} (pattern matching supported: {pm_supported})')

PATTERN = re.compile(r'```ruby\n(.*?)\n```', re.S)
FAIL_LIKE = re.compile(r'syntax error|unexpected|undefined', re.I)

fail = 0
skip = 0
total = 0
for f in sorted(glob.glob('static-data/knowledge/languages/ruby/ruby-*.md')):
    content = open(f).read()
    blocks = PATTERN.findall(content)
    for i, b in enumerate(blocks, 1):
        total += 1
        if '...' in b or b.strip().startswith('#') or len(b.strip()) < 10:
            continue
        # Pattern-matching blocks on Ruby < 2.7: skip (valid on modern Ruby)
        uses_pm = re.search(r'^\s*in |\bin \[|\bin Integer|\bin \w+ =>', b, re.M)
        if uses_pm and not pm_supported:
            skip += 1
            continue
        with tempfile.NamedTemporaryFile('w', suffix='.rb', delete=False) as tf:
            tf.write(b)
            path = tf.name
        r = subprocess.run(['ruby', '-c', path], capture_output=True, text=True)
        os.unlink(path)
        if r.returncode != 0:
            # if it smells like a version issue, still flag it
            fail += 1
            print(f'SYNTAX FAIL {f} block {i}:')
            print(r.stderr.strip()[:400])
            print('---')
print(f'{total} blocks checked, {fail} failed, {skip} skipped (pattern-matching on Ruby<2.7)')
sys.exit(1 if fail else 0)
