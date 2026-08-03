---
{
  "title": "Strings",
  "description": "Text manipulation.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Split strings",
    "Use string functions",
    "Format output"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-07-strings"
  ],
  "prerequisites": [
    "Wolfram-06: Plotting"
  ],
  "references": [
    {
      "title": "Wolfram Language Documentation",
      "url": "https://reference.wolfram.com/language/",
      "description": "Official reference"
    },
    {
      "title": "Wolfram Language Fast Introduction",
      "url": "https://www.wolfram.com/language/fast-introduction-for-programmers/en/",
      "description": "Fast intro"
    },
    {
      "title": "Wolfram Language Guide",
      "url": "https://reference.wolfram.com/language/guide/LanguageOverview.html",
      "description": "Language guide"
    }
  ]
}
---

# WOLFRAM-07-STRINGS: Strings

## Introduction

Text manipulation. By the end of this lesson you will be able to: Concatenate strings; Split strings; Use string functions; Format output.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
"Hello" <> " " <> "World"
```
### 2. Split strings

Target: Split strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
StringSplit["a,b,c", ","]
```
### 3. Use string functions

Target: Use string functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
StringLength["hello"]
ToUpperCase["hi"]
```
### 4. Format output

Target: Format output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
StringJoin[{"a", "b", "c"}]
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
