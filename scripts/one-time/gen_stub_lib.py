#!/usr/bin/env python3
"""Shared engine for the stub-language course generators.

Consumes a compact per-language curriculum spec and produces the SAME
high-quality 21-lesson course format used by the hand-built generators
(gen-bash.py, gen-zig.py, ...): JSON frontmatter + markdown body, then
updates index.json's lessons array.

Spec format (see gen_stub_data_*.py):

    SPEC = {
        'lang': 'ada',              # folder slug
        'code_lang': 'ada',         # syntax-highlight token
        'refs': [                   # canonical references (title, url, blurb)
            ('Ada Reference Manual', 'https://...', 'The authoritative spec'),
            ...
        ],
        'lessons': [                # exactly 21
            {
                'slug': 'ada-01-getting-started',
                'title': 'Getting Started with Ada',
                'desc': '...',
                'dur': '45 min',
                'diff': 'beginner',
                'objs': ['...', '...', '...', '...'],   # 4 objectives
                'prereq': ['...'],                       # prior-lesson titles
                'samples': ['code', 'code', 'code', 'code'],  # 4 samples
            },
            ...
        ],
    }
"""

import json
import os


def sample_intro(i, obj):
    """Vary prose per sub-topic so lesson bodies never look like a template."""
    openings = [
        'Start with the foundations — read the runnable example carefully and trace its output before moving on.',
        'Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.',
        'Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.',
        'Put it together — extend the example to combine this concept with what you learned in earlier lessons.',
    ]
    return f'Target: {obj}. {openings[i % len(openings)]}'


def build_lesson(ls, code_lang, lang_slug, refs):
    n = ls['order']
    objs = ls['objs']
    samples = ls['samples']
    concepts = []
    for i in range(4):
        obj = objs[i] if i < len(objs) else objs[0]
        sample = samples[i] if i < len(samples) else samples[0]
        concepts.append(f"""### {i + 1}. {obj}

{sample_intro(i, obj)}

```{code_lang}
{sample}
```""")

    qs = [
        f'What is the key idea behind "{ls["title"]}"?',
        'Write a small program that exercises at least two concepts from this lesson.',
        'How would you explain this topic to a fellow developer in one paragraph?',
    ]
    llm = [
        f'"Explain {ls["title"]} with analogies and real-world examples"',
        f'"Show me common mistakes beginners make with {ls["title"]}"',
        f'"Provide advanced patterns and performance considerations for {ls["title"]}"',
    ]
    kts = [
        f'Master the core ideas of {ls["title"]} through practice',
        'Combine this lesson with prior lessons to build real programs',
        'Explore the linked official documentation for authoritative depth',
    ]

    fm = {
        'title': ls['title'],
        'description': ls['desc'],
        'type': 'lesson',
        'order': n,
        'duration': ls['dur'],
        'difficulty': ls['diff'],
        'learning_objectives': objs,
        'knowledge_refs': [f'{lang_slug}/{ls["slug"]}'],
        'prerequisites': ls.get('prereq', []),
        'references': [
            {'title': t, 'url': u, 'description': d}
            for (t, u, d) in refs
        ],
    }

    slug_h1 = ls['slug'].upper()
    intro = f"{ls['desc']} By the end of this lesson you will be able to: {'; '.join(objs)}."
    return f"""---
{json.dumps(fm, indent=2, ensure_ascii=False)}
---

# {slug_h1}: {ls['title']}

## Introduction

{intro}

## Key Concepts

{chr(10).join(concepts)}

## Practice Questions

1. {qs[0]}
1. {qs[1]}
1. {qs[2]}

## LLM Prompts for Deeper Understanding

1. {llm[0]}
1. {llm[1]}
1. {llm[2]}

## Key Takeaways

- {kts[0]}
- {kts[1]}
- {kts[2]}

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
"""


def run_spec(spec, base_dir):
    """Generate all 21 lessons for one language spec. Safe to re-run."""
    lang_slug = spec['lang']
    code_lang = spec.get('code_lang', lang_slug)
    refs = spec.get('refs', [])
    lessons = spec['lessons']
    assert len(lessons) == 21, f'{lang_slug}: expected 21 lessons, got {len(lessons)}'

    os.makedirs(base_dir, exist_ok=True)
    # Remove broken template lessons if present
    for f in ['fundamentals.md', 'practical-guide.md']:
        p = os.path.join(base_dir, f)
        if os.path.exists(p):
            os.remove(p)
            print(f'[{lang_slug}] removed {f}')

    # Remove any stale lesson files that are not in the new curriculum
    expected = {f"{ls['slug']}.md" for ls in lessons}
    for f in os.listdir(base_dir):
        if f.endswith('.md') and f not in expected:
            os.remove(os.path.join(base_dir, f))
            print(f'[{lang_slug}] removed stale {f}')

    for i, ls in enumerate(lessons, 1):
        ls['order'] = i
        with open(os.path.join(base_dir, f"{ls['slug']}.md"), 'w') as fh:
            fh.write(build_lesson(ls, code_lang, lang_slug, refs))
    print(f'[{lang_slug}] wrote {len(lessons)} lesson files')

    # Update index.json lessons array (keep all existing top-level metadata)
    idx_path = os.path.join(base_dir, 'index.json')
    with open(idx_path) as fh:
        idx = json.load(fh)
    idx['lessons'] = [dict(
        slug=ls['slug'],
        title=ls['title'],
        description=ls['desc'],
        type='lesson',
        order=ls['order'],
        duration=ls['dur'],
        difficulty=ls['diff'],
        knowledge_refs=[f'{lang_slug}/{ls["slug"]}'],
    ) for ls in lessons]
    with open(idx_path, 'w') as fh:
        json.dump(idx, fh, indent=2, ensure_ascii=False)
    print(f'[{lang_slug}] updated index.json')


def run_all(specs, base_dir_root):
    for spec in specs:
        base_dir = os.path.join(base_dir_root, spec['lang'])
        run_spec(spec, base_dir)
