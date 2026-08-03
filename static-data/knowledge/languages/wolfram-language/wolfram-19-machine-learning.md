---
{
  "title": "Machine Learning",
  "description": "Classify and predict.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create classifiers",
    "Train models",
    "Evaluate accuracy",
    "Use neural nets"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-19-machine-learning"
  ],
  "prerequisites": [
    "Wolfram-18: Statistics"
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

# WOLFRAM-19-MACHINE-LEARNING: Machine Learning

## Introduction

Classify and predict. By the end of this lesson you will be able to: Create classifiers; Train models; Evaluate accuracy; Use neural nets.

## Key Concepts

### 1. Create classifiers

Target: Create classifiers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
data = {1 -> "low", 2 -> "low", 10 -> "high", 11 -> "high"}
c = Classify[data]
c[5]
```
### 2. Train models

Target: Train models. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
c[5, "Probabilities"]
```
### 3. Evaluate accuracy

Target: Evaluate accuracy. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Classify[{1 -> "a", 2 -> "b"}, Method -> "LogisticRegression"]
```
### 4. Use neural nets

Target: Use neural nets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
NetChain[{LinearLayer[5], Ramp, LinearLayer[1]}]
```

## Practice Questions

1. What is the key idea behind "Machine Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Machine Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Machine Learning"
1. "Provide advanced patterns and performance considerations for Machine Learning"

## Key Takeaways

- Master the core ideas of Machine Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
