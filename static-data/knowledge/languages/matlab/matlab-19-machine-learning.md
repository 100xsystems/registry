---
{
  "title": "Machine Learning",
  "description": "Classification and regression.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Load sample data",
    "Split train/test",
    "Train a classifier",
    "Evaluate accuracy"
  ],
  "knowledge_refs": [
    "matlab/matlab-19-machine-learning"
  ],
  "prerequisites": [
    "Matlab-18: Working with Tables"
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

# MATLAB-19-MACHINE-LEARNING: Machine Learning

## Introduction

Classification and regression. By the end of this lesson you will be able to: Load sample data; Split train/test; Train a classifier; Evaluate accuracy.

## Key Concepts

### 1. Load sample data

Target: Load sample data. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
load fisheriris
X = meas;
y = species;
```
### 2. Split train/test

Target: Split train/test. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
rng(1)
cv = cvpartition(y, "HoldOut", 0.3);
```
### 3. Train a classifier

Target: Train a classifier. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
model = fitcknn(X(training(cv), :), y(training(cv)));
```
### 4. Evaluate accuracy

Target: Evaluate accuracy. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
pred = predict(model, X(test(cv), :));
accuracy = sum(pred == y(test(cv))) / numel(pred)
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
