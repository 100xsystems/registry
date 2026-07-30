#!/usr/bin/env python3
"""Sync JavaScript curriculum: update index.json slugs + delete duplicate old files."""

import json
import os
import shutil

BASE = os.path.join(os.path.dirname(__file__), '..', 'static-data', 'knowledge', 'languages', 'javascript')

# Map: old slug → new flat slug
OLD_TO_NEW = {
    'js-beginner-01-values-types-variables': 'js-01-values-types-variables',
    'js-beginner-02-control-flow': 'js-02-control-flow-operators',
    'js-beginner-03-functions': 'js-03-functions-basics',
    'js-beginner-04-objects-arrays': 'js-04-objects-arrays-collections',
    'js-beginner-05-dom-browser': 'js-05-dom-browser-apis',
    'js-beginner-06-debugging-tools': 'js-06-debugging-tools',
    'js-beginner-07-project': 'js-07-beginner-project',
    'js-advanced-01-scope-closures': 'js-08-scope-closures',
    'js-advanced-02-this-prototypes-classes': 'js-09-this-prototypes-classes',
    'js-advanced-03-async-promises': 'js-10-async-promises',
    'js-advanced-04-event-loop-concurrency': 'js-11-event-loop-concurrency',
    'js-advanced-05-higher-order-generators': 'js-12-higher-order-generators',
    'js-advanced-06-modules-syntax': 'js-13-modules-syntax',
    'js-advanced-07-project': 'js-14-advanced-project',
    'js-expert-01-coercion-equality': 'js-15-coercion-equality',
    'js-expert-02-memory-performance': 'js-16-memory-performance',
    'js-expert-03-metaprogramming': 'js-17-metaprogramming',
    'js-expert-04-error-patterns': 'js-18-error-patterns',
    'js-expert-05-browser-apis-workers': 'js-19-browser-apis-workers',
    'js-expert-06-module-systems-bundlers': 'js-20-module-systems',
    'js-expert-07-ecmascript-spec-tc39': 'js-21-ecmascript-spec',
}

NEW_TITLES = {
    'js-01-values-types-variables': 'Values, Types, and Variables',
    'js-02-control-flow-operators': 'Control Flow, Operators, and Expressions',
    'js-03-functions-basics': 'Functions: Declarations, Scope, and Arrow Functions',
    'js-04-objects-arrays-collections': 'Objects, Arrays, and Collections',
    'js-05-dom-browser-apis': 'The DOM and Browser APIs',
    'js-06-debugging-tools': 'Debugging, Errors, and Developer Tools',
    'js-07-beginner-project': 'Beginner Project: Interactive Web Application',
    'js-08-scope-closures': 'Deep Scope, Hoisting, and Closures',
    'js-09-this-prototypes-classes': 'The `this` Keyword, Prototypes, and Classes',
    'js-10-async-promises': 'Asynchronous JavaScript: Promises and Async/Await',
    'js-11-event-loop-concurrency': 'The Event Loop, Microtasks, and Concurrency',
    'js-12-higher-order-generators': 'Higher-Order Functions, Iterators, and Generators',
    'js-13-modules-syntax': 'ES6+ Modules and Modern Syntax',
    'js-14-advanced-project': 'Advanced Project: Real-Time Data Dashboard',
    'js-15-coercion-equality': 'Type Coercion, Equality, and Grammar',
    'js-16-memory-performance': 'Memory Management, GC, and Performance',
    'js-17-metaprogramming': 'Metaprogramming: Proxy, Reflect, and Symbols',
    'js-18-error-patterns': 'Error Handling and Defensive Programming',
    'js-19-browser-apis-workers': 'Browser APIs, Web Workers, and Performance',
    'js-20-module-systems': 'Module Systems, Bundlers, and Pipelines',
    'js-21-ecmascript-spec': 'ECMAScript Spec, TC39, and Future Proposals',
}


def main():
    # 1. Update index.json slugs
    idx_path = os.path.join(BASE, 'index.json')
    with open(idx_path, 'r') as f:
        data = json.load(f)

    lessons = data.get('lessons', [])
    updated = []
    seen_slugs = set()

    for lesson in lessons:
        old_slug = lesson['slug']
        if old_slug in OLD_TO_NEW:
            new_slug = OLD_TO_NEW[old_slug]
            lesson['slug'] = new_slug
            lesson['title'] = NEW_TITLES[new_slug]
            lesson.pop('level', None)
            lesson['knowledge_refs'] = [f'languages/javascript/{new_slug}']
        if lesson['slug'] not in seen_slugs:
            seen_slugs.add(lesson['slug'])
            updated.append(lesson)

    data['lessons'] = updated
    with open(idx_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'✅ index.json: {len(updated)} lessons, all slugs now flat')

    # 2. Delete old level-based .md files
    deleted = 0
    for old_slug in OLD_TO_NEW:
        old_path = os.path.join(BASE, f'{old_slug}.md')
        if os.path.exists(old_path):
            os.remove(old_path)
            deleted += 1
            print(f'  🗑 Deleted {old_slug}.md')

    print(f'✅ Deleted {deleted} old duplicate files')

    # 3. Verify: only 21 new files remain
    remaining = [f for f in os.listdir(BASE) if f.endswith('.md')]
    print(f'✅ {len(remaining)} .md files remaining')


if __name__ == '__main__':
    main()
