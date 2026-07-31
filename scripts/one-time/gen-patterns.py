#!/usr/bin/env python3
"""Generate deep ACID-format curricula for all 52 patterns.

Each pattern gets 4 lessons: fundamentals, applications, advanced, and a
review quiz — matching the approved ACID template depth. Content comes from
the patterns_data*.py modules.
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_knowledge_lib import run_topic  # noqa: E402


def build(slug, topics):
    """Derive the standard 4-lesson structure from a compact topic spec."""
    lessons = []
    kinds = ['fundamentals', 'applications', 'advanced', 'review-quiz']
    for kind, t in zip(kinds, topics):
        lessons.append({
            'slug': f'{slug}-{kind}',
            'title': t['title'],
            'description': t['desc'],
            'duration': t.get('dur', '45 min' if kind == 'fundamentals' else ('60 min' if kind == 'applications' else '75 min')),
            'difficulty': t.get('diff', 'Beginner' if kind == 'fundamentals' else ('Intermediate' if kind in ('applications', 'review-quiz') else 'Advanced')),
            'type': 'quiz' if kind == 'review-quiz' else 'lesson',
            'objectives': t['objs'],
            'prereqs': t.get('prereqs', []),
            'sections': t.get('sections', []),
            'practice': t.get('practice'),
            'prompts': t.get('prompts', []),
            'takeaways': t.get('takeaways', []),
            'further': t.get('further', []),
        })
    return lessons


if __name__ == '__main__':
    merged = {}
    mod_names = ['patterns_data'] + [f'patterns_data{i}' for i in range(2, 10)]
    for mod_name in mod_names:
        try:
            mod = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            continue
        merged.update(mod.TOPICS)
        print(f'loaded {mod_name}: {len(mod.TOPICS)} topics')

    for slug, topics in merged.items():
        lessons = build(slug, topics)
        run_topic('patterns', slug, lessons)

    print(f'\nTOTAL patterns generated: {len(merged)}')
