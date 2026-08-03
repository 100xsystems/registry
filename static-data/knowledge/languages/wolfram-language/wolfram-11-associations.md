---
{
  "title": "Associations",
  "description": "Key-value data.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create associations",
    "Access keys",
    "Add entries",
    "Use association functions"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-11-associations"
  ],
  "prerequisites": [
    "Wolfram-10: Pattern Matching"
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

# WOLFRAM-11-ASSOCIATIONS: Associations

## Introduction

Key-value data. By the end of this lesson you will be able to: Create associations; Access keys; Add entries; Use association functions.

## Key Concepts

### 1. Create associations

Target: Create associations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
person = <|"name" -> "Ada", "age" -> 36|>
```
### 2. Access keys

Target: Access keys. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
person["name"]
```
### 3. Add entries

Target: Add entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
person["city"] = "London"
person
```
### 4. Use association functions

Target: Use association functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
Keys[person]
Values[person]
```

## Practice Questions

1. What is the key idea behind "Associations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Associations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Associations"
1. "Provide advanced patterns and performance considerations for Associations"

## Key Takeaways

- Master the core ideas of Associations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
