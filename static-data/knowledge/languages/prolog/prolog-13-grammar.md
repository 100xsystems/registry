---
{
  "title": "DCG: Grammar Rules",
  "description": "Parse with definite clause grammars.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write DCG rules",
    "Parse sentences",
    "Generate sentences",
    "Build expression parsers"
  ],
  "knowledge_refs": [
    "prolog/prolog-13-grammar"
  ],
  "prerequisites": [
    "Prolog-12: File I/O"
  ],
  "references": [
    {
      "title": "SWI-Prolog Documentation",
      "url": "https://www.swi-prolog.org/pldoc/",
      "description": "Official SWI-Prolog docs"
    },
    {
      "title": "Learn Prolog Now!",
      "url": "https://www.learnprolognow.org/",
      "description": "The classic free textbook"
    },
    {
      "title": "Prolog Wiki",
      "url": "https://en.wikipedia.org/wiki/Prolog",
      "description": "Overview article"
    }
  ]
}
---

# PROLOG-13-GRAMMAR: DCG: Grammar Rules

## Introduction

Parse with definite clause grammars. By the end of this lesson you will be able to: Write DCG rules; Parse sentences; Generate sentences; Build expression parsers.

## Key Concepts

### 1. Write DCG rules

Target: Write DCG rules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
determiner --> [the].
 noun --> [cat].
```
### 2. Parse sentences

Target: Parse sentences. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
sentence --> [the, cat, eats].
?- phrase(sentence, [the, cat, eats]).
true.
```
### 3. Generate sentences

Target: Generate sentences. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
expr --> term, [+], term.
term --> [X], {number(X)}.
```
### 4. Build expression parsers

Target: Build expression parsers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
phrase(sentence, L, []).
```

## Practice Questions

1. What is the key idea behind "DCG: Grammar Rules"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain DCG: Grammar Rules with analogies and real-world examples"
1. "Show me common mistakes beginners make with DCG: Grammar Rules"
1. "Provide advanced patterns and performance considerations for DCG: Grammar Rules"

## Key Takeaways

- Master the core ideas of DCG: Grammar Rules through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
