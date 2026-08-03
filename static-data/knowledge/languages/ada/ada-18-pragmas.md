---
{
  "title": "Pragmas and Preconditions",
  "description": "Compiler directives and contracts.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use common pragmas",
    "Write preconditions",
    "Write postconditions",
    "Enable contract checking"
  ],
  "knowledge_refs": [
    "ada/ada-18-pragmas"
  ],
  "prerequisites": [
    "Ada-17: Command-Line Interfaces"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-18-PRAGMAS: Pragmas and Preconditions

## Introduction

Compiler directives and contracts. By the end of this lesson you will be able to: Use common pragmas; Write preconditions; Write postconditions; Enable contract checking.

## Key Concepts

### 1. Use common pragmas

Target: Use common pragmas. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
pragma Assert (X > 0);
```
### 2. Write preconditions

Target: Write preconditions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
procedure Deposit (Amount : in Integer)
   with Pre => Amount > 0,
        Post => Balance'Old + Amount = Balance;
```
### 3. Write postconditions

Target: Write postconditions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
pragma Restrictions (No_Recursion);
```
### 4. Enable contract checking

Target: Enable contract checking. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
pragma Pure (Math_Utils);
```

## Practice Questions

1. What is the key idea behind "Pragmas and Preconditions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pragmas and Preconditions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pragmas and Preconditions"
1. "Provide advanced patterns and performance considerations for Pragmas and Preconditions"

## Key Takeaways

- Master the core ideas of Pragmas and Preconditions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
