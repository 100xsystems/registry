---
{
  "title": "Testing with FiveAM",
  "description": "Unit testing library.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up FiveAM",
    "Write tests",
    "Run suites",
    "Use assertions"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-20-tests"
  ],
  "prerequisites": [
    "Common Lisp-19: Debugging Tools"
  ],
  "references": [
    {
      "title": "Practical Common Lisp",
      "url": "https://gigamonkeys.com/book/",
      "description": "The classic online book"
    },
    {
      "title": "Common Lisp HyperSpec",
      "url": "http://www.lispworks.com/documentation/HyperSpec/Front/Contents.htm",
      "description": "Official standard reference"
    },
    {
      "title": "Common Lisp Cookbook",
      "url": "https://lispcookbook.github.io/cl-cookbook/",
      "description": "Community cookbook"
    }
  ]
}
---

# COMMON-LISP-20-TESTS: Testing with FiveAM

## Introduction

Unit testing library. By the end of this lesson you will be able to: Set up FiveAM; Write tests; Run suites; Use assertions.

## Key Concepts

### 1. Set up FiveAM

Target: Set up FiveAM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(def-suite my-suite)
```
### 2. Write tests

Target: Write tests. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(in-suite my-suite)
(test addition
  (is (= 4 (+ 2 2))))
```
### 3. Run suites

Target: Run suites. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(test string
  (is (string= "AB" (concatenate 'string "A" "B"))))
```
### 4. Use assertions

Target: Use assertions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(run! 'my-suite)
```

## Practice Questions

1. What is the key idea behind "Testing with FiveAM"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with FiveAM with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with FiveAM"
1. "Provide advanced patterns and performance considerations for Testing with FiveAM"

## Key Takeaways

- Master the core ideas of Testing with FiveAM through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
