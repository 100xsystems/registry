#!/usr/bin/env python3
"""Shared deep-curriculum generator template for all language generators.

Every language generator (gen-c.py, gen-cpp.py, ...) imports this module and
provides: LANGUAGE (slug), LESSONS (21 dicts), CODE (21 x 4 distinct samples).
This keeps the lesson format identical across all languages and avoids drift.
"""

import json
import os


def sample_intro(i, obj):
    """Vary the prose per sub-topic position so the lesson body is not a verbatim template."""
    openings = [
        'Start with the foundations — read the runnable example carefully and trace its output before moving on.',
        'Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.',
        'Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.',
        'Put it together — extend the example to combine this concept with what you learned in earlier lessons.',
    ]
    return f'Target: {obj}. {openings[i % len(openings)]}'


def build_lesson(ls, samples, code_lang, lang_slug):
    """Build one lesson markdown file from its metadata + 4 code samples."""
    n = ls['order']
    code_list = samples.get(n, samples.get(1))
    objs = ls['objs']

    concepts = []
    for i in range(4):
        obj = objs[i] if i < len(objs) else objs[0]
        sample = code_list[i] if i < len(code_list) else code_list[0]
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
        'prerequisites': ls['prereq'],
        'references': ls['refs'],
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


def main(lang_slug, code_lang, lessons, code, base_dir):
    """Run the generator: remove skeletons, write 21 lessons, update index.json lessons."""
    os.makedirs(base_dir, exist_ok=True)
    for f in ['fundamentals.md', 'practical-guide.md']:
        p = os.path.join(base_dir, f)
        if os.path.exists(p):
            os.remove(p)
            print(f'removed {f}')

    for i, ls in enumerate(lessons, 1):
        ls['order'] = i
        with open(os.path.join(base_dir, f"{ls['slug']}.md"), 'w') as fh:
            fh.write(build_lesson(ls, code, code_lang, lang_slug))
    print(f'wrote {len(lessons)} lesson files')

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
    print('updated index.json')
