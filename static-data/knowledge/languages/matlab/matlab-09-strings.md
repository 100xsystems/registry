---
{
  "title": "Strings and Text",
  "description": "String manipulation.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Use string functions",
    "Format with sprintf",
    "Parse text"
  ],
  "knowledge_refs": [
    "matlab/matlab-09-strings"
  ],
  "prerequisites": [
    "Matlab-08: Scripts vs Functions"
  ],
  "references": [
    {
      "title": "MATLAB Documentation",
      "url": "https://www.mathworks.com/help/matlab/",
      "description": "Official docs"
    },
    {
      "title": "MATLAB Onramp",
      "url": "https://www.mathworks.com/learn/tutorials/matlab-onramp.html",
      "description": "Official intro course"
    },
    {
      "title": "MATLAB Central",
      "url": "https://www.mathworks.com/matlabcentral/",
      "description": "Community Q&A"
    }
  ]
}
---

# MATLAB-09-STRINGS: Strings and Text

## Introduction

String manipulation. By the end of this lesson you will be able to: Concatenate strings; Use string functions; Format with sprintf; Parse text.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
s = "Hello" + " " + "World";
```
### 2. Use string functions

Target: Use string functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
strjoin(["a", "b", "c"], " | ")
```
### 3. Format with sprintf

Target: Format with sprintf. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
sprintf("value: %d", 42)
```
### 4. Parse text

Target: Parse text. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
split("a,b,c", ",")
```

## Practice Questions

1. What is the key idea behind "Strings and Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and Text"
1. "Provide advanced patterns and performance considerations for Strings and Text"

## Key Takeaways

- Master the core ideas of Strings and Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
