#!/usr/bin/env python3
"""Shared renderer for ACID-format deep knowledge lessons (principles & patterns).

Each topic folder (static-data/knowledge/{principles|patterns}/{slug}/) gets:
  - index.json preserved (slug/name/description/categories) with the `lessons`
    array replaced by the deep curriculum
  - one .md lesson file per lesson, in the ACID template style:
      YAML frontmatter (title, order, difficulty, duration, learning_objectives,
      prerequisites, knowledge_refs)
      # Title
      Intro
      ## Why <Topic> Matters
      ## How It Works  (+ code blocks)
      ## Practice: <Challenge>
      ## Guided LLM Prompts
      ## Key Takeaways
      ## Further Reading
"""

import json
import os
import textwrap


def _yaml(v):
    """Escape a value for a double-quoted YAML scalar."""
    return str(v).replace('\\', '\\\\').replace('"', '\\"')


def render_lesson(lesson, base_kref):
    """Render one lesson dict into ACID-format markdown."""
    title = lesson['title']
    body = lesson.get('body', '').strip()

    # Frontmatter (YAML, matching the ACID template style)
    lines = [
        '---',
        f'title: "{_yaml(title)}"',
        f'order: {lesson["order"]}',
        f'difficulty: "{_yaml(lesson["difficulty"])}"',
        f'duration: "{_yaml(lesson["duration"])}"',
        'learning_objectives:',
    ]
    for obj in lesson['objectives']:
        lines.append(f'  - "{_yaml(obj)}"')
    lines.append('prerequisites:')
    prereqs = lesson.get('prereqs', []) or []
    if not prereqs:
        lines.append('  []')
    for p in prereqs:
        lines.append(f'  - "{_yaml(p)}"')
    lines.append('knowledge_refs:')
    for k in lesson.get('krefs', [base_kref]):
        lines.append(f'  - "{_yaml(k)}"')
    lines.append('---')
    lines.append('')
    lines.append(f'# {title}')
    lines.append('')

    # Sections
    sections = lesson.get('sections', [])
    if body:
        lines.append(body)
        lines.append('')
    for sec in sections:
        heading = sec.get('heading')
        paras = sec.get('paras', [])
        code = sec.get('code')
        bullets = sec.get('bullets')
        lines.append(f'## {heading}')
        lines.append('')
        for p in paras:
            lines.append(textwrap.dedent(p).strip())
            lines.append('')
        if bullets:
            for b in bullets:
                lines.append(f'- {b}')
            lines.append('')
        if code:
            lines.append(f'```{code.get("lang", "text")}')
            lines.append(textwrap.dedent(code.get('body', '')).strip())
            lines.append('```')
            lines.append('')

    # Practice
    practice = lesson.get('practice')
    if practice:
        lines.append(f'## Practice: {practice.get("title", "Hands-On Challenge")}')
        lines.append('')
        lines.append(textwrap.dedent(practice.get('intro', '')).strip())
        lines.append('')
        for t in practice.get('tasks', []):
            lines.append(f'**{t.get("label", "Task")}:** {t.get("text", "")}')
            lines.append('')
        if practice.get('code'):
            lines.append(f'```{practice["code"].get("lang", "text")}')
            lines.append(textwrap.dedent(practice['code'].get('body', '')).strip())
            lines.append('```')
            lines.append('')

    # LLM prompts
    prompts = lesson.get('prompts', [])
    if prompts:
        lines.append('## Guided LLM Prompts')
        lines.append('')
        for i, pr in enumerate(prompts, 1):
            lines.append(f'**Prompt {i} — {pr.get("label", "Deep Dive")}:**')
            lines.append('> ' + textwrap.dedent(pr.get('text', '')).strip().replace('\n', '\n> '))
            lines.append('')

    # Takeaways
    takeaways = lesson.get('takeaways', [])
    if takeaways:
        lines.append('## Key Takeaways')
        lines.append('')
        for t in takeaways:
            lines.append(f'- {t}')
        lines.append('')

    # Further reading
    further = lesson.get('further', [])
    if further:
        lines.append('## Further Reading')
        lines.append('')
        for f in further:
            lines.append(f'- [{f.get("title")}]({f.get("url")})')
        lines.append('')

    return '\n'.join(lines).rstrip() + '\n'


def run_topic(kind, slug, lessons):
    """Write lesson files + update index.json lessons for one topic.

    kind: 'principles' | 'patterns'
    slug: topic slug (folder name)
    lessons: list of lesson dicts (order auto-assigned)
    """
    base = os.path.join('static-data/knowledge', kind, slug)
    os.makedirs(base, exist_ok=True)

    idx_path = os.path.join(base, 'index.json')
    with open(idx_path) as fh:
        idx = json.load(fh)

    base_kref = f'{kind}/{slug}'

    # remove stale skeleton files
    for f in ['fundamentals.md', 'practical-guide.md']:
        p = os.path.join(base, f)
        if os.path.exists(p):
            os.remove(p)
            print(f'removed {kind}/{slug}/{f}')

    idx_lessons = []
    for i, ls in enumerate(lessons, 1):
        ls = dict(ls)
        ls['order'] = i
        with open(os.path.join(base, f"{ls['slug']}.md"), 'w') as fh:
            fh.write(render_lesson(ls, base_kref))
        idx_lessons.append(dict(
            slug=ls['slug'],
            title=ls['title'],
            description=ls.get('description', ''),
            type=ls.get('type', 'lesson'),
            order=i,
            duration=ls.get('duration', '45 min'),
            difficulty=ls.get('difficulty', 'Intermediate'),
        ))

    idx['lessons'] = idx_lessons
    with open(idx_path, 'w') as fh:
        json.dump(idx, fh, indent=2, ensure_ascii=False)
    print(f'updated {kind}/{slug}: {len(idx_lessons)} lessons')
