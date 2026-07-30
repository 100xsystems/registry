#!/usr/bin/env python3
"""Final pass: replace any remaining generic resource URLs with exact chapter URLs in all 21 JS lesson files."""

import os

BASE = os.path.join(os.path.dirname(__file__), '..', 'static-data', 'knowledge', 'languages', 'javascript')

# Per-lesson: (old_url_substring, new_exact_url)
# We look for the generic URL and replace it with the exact one
GENERIC_TO_EXACT: dict[str, list[tuple[str, str]]] = {
    'js-01-values-types-variables': [
        # Already fixed - just double-check
    ],
    'js-02-control-flow-operators': [
        # Already fixed
    ],
    'js-03-functions-basics': [
        # Already fixed
    ],
    'js-04-objects-arrays-collections': [
        # Already fixed
    ],
    'js-05-dom-browser-apis': [
        # Already fixed
    ],
    'js-06-debugging-tools': [
        # Already fixed
    ],
    'js-07-beginner-project': [
        # Can stay generic for project pages
    ],
    'js-08-scope-closures': [
        # Already fixed
    ],
    'js-09-this-prototypes-classes': [
        # Already fixed
    ],
    'js-10-async-promises': [
        ('https://github.com/getify/you-dont-know-js"', 'https://github.com/getify/you-dont-know-js/blob/2nd-ed/sync-async/ch1.md"'),
    ],
    'js-11-event-loop-concurrency': [
        # Already fixed
    ],
    'js-12-higher-order-generators': [
        # Already fixed
    ],
    'js-13-modules-syntax': [
        # Already fixed
    ],
    'js-14-advanced-project': [
        # Already fixed
    ],
    'js-15-coercion-equality': [
        # Already fixed
    ],
    'js-16-memory-performance': [
        # Already fixed
    ],
    'js-17-metaprogramming': [
        # Already fixed
    ],
    'js-18-error-patterns': [
        # Already fixed
    ],
    'js-19-browser-apis-workers': [
        # Already fixed
    ],
    'js-20-module-systems': [
        # Already fixed
    ],
    'js-21-ecmascript-spec': [
        # Already fixed
    ],
}

# Also scan ALL files for any remaining generic URLs that should be specific
# These are resource URLs that appear as generics in multiple lessons
GLOBAL_FIXES: list[tuple[str, str, str]] = [
    # (old_url, new_url, description)
    ('url: "https://github.com/getify/you-dont-know-js"', 'url: "https://github.com/getify/you-dont-know-js/blob/2nd-ed/sync-async/ch1.md"', 'YDKJSY async chapter'),
    ('url: "https://eloquentjavascript.net/"', 'url: "https://eloquentjavascript.net/"', 'Keep generic Eloquent (no better match)'),
    ('url: "https://javascript.info/"', 'url: "https://javascript.info/"', 'Keep generic JS Info (no better match)'),
    ('url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"', 'url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"', 'Keep generic MDN Reference (no better match)'),
]

def main():
    files_updated = 0
    
    # Phase 1: Apply per-lesson fixes
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.md'):
            continue
        slug = fname.replace('.md', '')
        if slug not in GENERIC_TO_EXACT:
            continue
        
        fpath = os.path.join(BASE, fname)
        with open(fpath, 'r') as f:
            content = f.read()
        original = content
        
        for old_url, new_url in GENERIC_TO_EXACT[slug]:
            if old_url in content:
                content = content.replace(old_url, new_url)
                print(f'  {slug}: replaced generic URL → specific')
        
        if content != original:
            with open(fpath, 'w') as f:
                f.write(content)
            files_updated += 1
    
    # Phase 2: Global scan - find any remaining generic URLs that should be specific
    print('\nScanning for remaining generic URLs...')
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(BASE, fname)
        with open(fpath, 'r') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            # Look for `url: "https://..."` that looks like a generic homepage
            if 'url: "https://' in line and not line.strip().endswith('"'):
                # Check if it's a known generic that should be specific
                url_match = __import__('re').search(r'url:\s*"([^"]+)"', line)
                if url_match:
                    url = url_match.group(1)
                    # Known generics that might need fixing
                    if 'github.com/getify/you-dont-know-js"' in line and 'blob' not in line:
                        print(f'  ⚠ {fname}:{i+1} - Generic YDKJSY URL: {url.strip()}')
    
    print(f'\n✅ Fixed {files_updated} files')


if __name__ == '__main__':
    main()
