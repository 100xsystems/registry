#!/usr/bin/env python3
"""Repair broken concatenated URLs in JS lesson files and replace with exact sub-topic URLs."""

import json
import os
import re

BASE = os.path.join(os.path.dirname(__file__), '..', 'static-data', 'knowledge', 'languages', 'javascript')

# Known broken URL patterns → correct exact URLs
BROKEN_FIXES: dict[str, str] = {
    # js-01 - Eloquent JavaScript
    'https://eloquentjavascript.net/02_program_structure.html01_values.html': 'https://eloquentjavascript.net/01_values.html',
    
    # js-05 - Eloquent JavaScript  
    'https://eloquentjavascript.net/15_event.html14_dom.html': 'https://eloquentjavascript.net/14_dom.html',
    
    # js-09 - Eloquent JavaScript
    'https://eloquentjavascript.net/06_object.html': 'https://eloquentjavascript.net/06_object.html',
    
    # js-14 - Eloquent JavaScript  
    'https://eloquentjavascript.net/20_node.html18_http.html': 'https://eloquentjavascript.net/18_http.html',
    
    # js-19 - MDN Web Docs (multiple broken)
    # These are less likely to be broken but let's check
}

# Per-resource exact URLs by lesson
LESSON_EXACT_URLS: dict[str, dict[str, str]] = {
    'js-01-values-types-variables': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/01_values.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/variables',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let',
        'Exploring JS': 'https://exploringjs.com/js/ch_values.html',
        'You Don\'t Know JS Yet': 'https://github.com/getify/you-dont-know-js/blob/2nd-ed/get-started/ch2.md',
    },
    'js-02-control-flow-operators': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/02_program_structure.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/while-for',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling',
        'Exploring JS': 'https://exploringjs.com/js/ch_control-flow.html',
    },
    'js-03-functions-basics': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/03_functions.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/function-basics',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions',
        'Exploring JS': 'https://exploringjs.com/js/ch_functions.html',
    },
    'js-04-objects-arrays-collections': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/04_data.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/object',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
        'Exploring JS': 'https://exploringjs.com/js/ch_objects.html',
    },
    'js-05-dom-browser-apis': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/14_dom.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/document',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction',
        'MDN Web Docs': 'https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model',
    },
    'js-06-debugging-tools': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/08_error.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/try-catch',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch',
    },
    'js-07-beginner-project': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/',
        'You Don\'t Know JS Yet': 'https://github.com/getify/you-dont-know-js',
        'The Modern JavaScript Tutorial': 'https://javascript.info/',
    },
    'js-08-scope-closures': {
        'You Don\'t Know JS Yet': 'https://github.com/getify/you-dont-know-js/blob/2nd-ed/scope-closures/ch1.md',
        'Eloquent JavaScript': 'https://eloquentjavascript.net/03_functions.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/closure',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures',
    },
    'js-09-this-prototypes-classes': {
        'You Don\'t Know JS Yet': 'https://github.com/getify/you-dont-know-js/blob/2nd-ed/objects-classes/ch1.md',
        'Eloquent JavaScript': 'https://eloquentjavascript.net/06_object.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/prototype-inheritance',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain',
        'Exploring JS': 'https://exploringjs.com/js/ch_classes.html',
    },
    'js-10-async-promises': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/11_async.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/promise-basics',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise',
        'Exploring JS': 'https://exploringjs.com/js/ch_promises.html',
    },
    'js-11-event-loop-concurrency': {
        'You Don\'t Know JS Yet': 'https://github.com/getify/you-dont-know-js/blob/2nd-ed/sync-async/ch1.md',
        'The Modern JavaScript Tutorial': 'https://javascript.info/event-loop',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop',
        'Exploring JS': 'https://exploringjs.com/js/ch_async-functions.html',
    },
    'js-12-higher-order-generators': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/05_higher_order.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/array-methods',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*',
    },
    'js-13-modules-syntax': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/10_modules.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/modules-intro',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import',
        'Exploring JS': 'https://exploringjs.com/js/ch_modules.html',
    },
    'js-14-advanced-project': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/18_http.html',
        'The Modern JavaScript Tutorial': 'https://javascript.info/fetch',
        'MDN Web Docs': 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API',
    },
    'js-15-coercion-equality': {
        'You Don\'t Know JS Yet': 'https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md',
        'The Modern JavaScript Tutorial': 'https://javascript.info/type-conversions',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness',
        'TC39 ECMAScript Spec': 'https://tc39.es/ecma262/#sec-abstract-equality-comparison',
    },
    'js-16-memory-performance': {
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap',
        'The Modern JavaScript Tutorial': 'https://javascript.info/garbage-collection',
        'Exploring JS': 'https://exploringjs.com/js/ch_memory.html',
    },
    'js-17-metaprogramming': {
        'The Modern JavaScript Tutorial': 'https://javascript.info/proxy',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy',
        'Exploring JS': 'https://exploringjs.com/js/ch_proxies.html',
    },
    'js-18-error-patterns': {
        'The Modern JavaScript Tutorial': 'https://javascript.info/custom-errors',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error',
    },
    'js-19-browser-apis-workers': {
        'The Modern JavaScript Tutorial': 'https://javascript.info/service-workers',
        'MDN Web Docs': 'https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API',
    },
    'js-20-module-systems': {
        'Eloquent JavaScript': 'https://eloquentjavascript.net/10_modules.html',
        'MDN JavaScript Guide': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules',
        'MDN JavaScript Reference': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export',
    },
    'js-21-ecmascript-spec': {
        'TC39 ECMAScript Proposals': 'https://github.com/tc39/proposals',
        'TC39 ECMAScript Spec': 'https://tc39.es/ecma262/',
    },
}


def parse_yaml_frontmatter_simple(lines: list[str]):
    """Simple YAML parser for the references section."""
    # Returns list of (title, url) tuples found in the references section
    refs = []
    current_title = None
    current_url = None
    in_refs = False
    
    for line in lines:
        stripped = line.strip()
        if stripped == 'references:':
            in_refs = True
            continue
        if in_refs and stripped.startswith('- title:'):
            # Save previous
            if current_title and current_url:
                refs.append((current_title, current_url))
            current_title = stripped.split(':', 1)[1].strip().strip('"')
            current_url = None
        elif in_refs and stripped.startswith('url:'):
            current_url = stripped.split(':', 1)[1].strip().strip('"')
        elif in_refs and not stripped.startswith(' ') and not stripped.startswith('-'):
            # Reached end of refs section
            break
    
    if current_title and current_url:
        refs.append((current_title, current_url))
    
    return refs


def main():
    # First, fix all known broken concatenated URLs
    count = 0
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(BASE, fname)
        with open(fpath, 'r') as f:
            content = f.read()
        original = content
        
        for broken, correct in BROKEN_FIXES.items():
            if broken in content:
                content = content.replace(broken, correct)
                print(f'  Fixed {broken} → {correct}')
        
        if content != original:
            with open(fpath, 'w') as f:
                f.write(content)
            count += 1
    
    print(f'✅ Fixed {count} files with broken URLs\n')
    
    # Second, apply exact per-lesson URLs  
    print('Applying exact sub-topic URLs by lesson...')
    for slug, resource_urls in LESSON_EXACT_URLS.items():
        fpath = os.path.join(BASE, f'{slug}.md')
        if not os.path.exists(fpath):
            print(f'  ~ {slug}.md not found, skipping')
            continue
        
        with open(fpath, 'r') as f:
            content = f.read()
        original = content
        
        # For each resource in this lesson's mapping
        for resource_title, exact_url in resource_urls.items():
            # Find the reference block with this title
            # Pattern: find title line, then the url line after it
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if re.match(r'^\s+-\s+title:\s*"', line):
                    # Extract the title from this line
                    title_match = re.search(r'title:\s*"([^"]*)"', line)
                    if title_match:
                        title = title_match.group(1)
                        # Check if this title starts with or contains our resource title
                        if title == resource_title or title.startswith(resource_title):
                            # Found the right reference block - now find its URL line
                            for j in range(i + 1, min(i + 5, len(lines))):
                                url_match = re.search(r'url:\s*"([^"]*)"', lines[j])
                                if url_match:
                                    old_url = url_match.group(1)
                                    if old_url != exact_url:
                                        lines[j] = lines[j].replace(old_url, exact_url)
                                        print(f'  {slug}: {resource_title} → {exact_url}')
                                    break
                            break  # Only process the first matching title
        
        content = '\n'.join(lines)
        if content != original:
            with open(fpath, 'w') as f:
                f.write(content)
    
    print('✅ All lessons processed')


if __name__ == '__main__':
    main()
