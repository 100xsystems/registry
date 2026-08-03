#!/usr/bin/env python3
"""One-shot patch for gen-perl.py applying reviewer fixes."""
import io

PATH = 'scripts/one-time/gen-perl.py'
src = open(PATH, encoding='utf-8').read()

# --- Fix 1: Lesson 6.4 — do-while with next/last is a Perl compile error ---
old_do = """my $i = 0;
do {
    $i++;
    next if $i == 3;       # skip 3
    last if $i == 6;       # stop at 6
    print "$i ";
} while $i < 10;"""
new_while = """my $i = 0;
while ($i < 10) {
    $i++;
    next if $i == 3;       # skip 3
    last if $i == 6;       # stop at 6
    print "$i ";
}"""
assert old_do in src, 'Fix1 old not found'
src = src.replace(old_do, new_while)

# Lesson 6 metadata: remove do-while from objectives
old_obj = "'Loop with while and do-while',"
new_obj = "'Loop with while loops',"
assert old_obj in src, 'Fix1b old not found'
src = src.replace(old_obj, new_obj)

# --- Fix 2: Lesson 20.3 — use a valid UTF-8 byte sequence (e9 is C3 A9) ---
old_bytes = 'my $bytes = "\\\\x{e9}";'
new_bytes = 'my $bytes = "\\\\xc3\\\\xa9";      # é (U+00E9) encoded as UTF-8 bytes'
assert old_bytes in src, 'Fix2 old not found'
src = src.replace(old_bytes, new_bytes)

# --- Fix 3: rename $a/$b to $x/$y in lessons 2.2 and 4.1 (avoid sort vars) ---
pairs = [
    ('my $a = "3";\nmy $b = 4;\nprint $a + $b,', 'my $x = "3";\nmy $y = 4;\nprint $x + $y,'),
    ('print $a . $b,', 'print $x . $y,'),
    ('my $a = 7;\nprint $a + 3,', 'my $x = 7;\nprint $x + 3,'),
    ('print $a - 2,', 'print $x - 2,'),
    ('print $a * 2,', 'print $x * 2,'),
    ('print $a / 2,', 'print $x / 2,'),
    ('print $a % 4,', 'print $x % 4,'),
    ('print $a ** 2,', 'print $x ** 2,'),
]
for old, new in pairs:
    assert old in src, f'Fix3 old not found: {old!r}'
    src = src.replace(old, new)

open(PATH, 'w', encoding='utf-8').write(src)
print('PATCH OK')
