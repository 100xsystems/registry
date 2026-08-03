---
{
  "title": "The Learning Problem",
  "description": "Formalize what a model learns: features, targets, hypotheses and loss — the vocabulary of every ML paper.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define features, targets and hypothesis space",
    "Explain loss functions as learning signals",
    "Describe the train-evaluate loop",
    "Frame overfitting and underfitting intuitively"
  ],
  "knowledge_refs": [
    "machine-learning/ml-03-the-learning-problem"
  ],
  "prerequisites": [
    "ML-02: Types of Learning"
  ],
  "references": [
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "The authoritative guide to the Python ML toolbox."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Hands-On Machine Learning — Aurélien Géron",
      "url": "https://github.com/ageron/handson-ml3",
      "description": "Practical ML with scikit-learn, Keras and TensorFlow."
    },
    {
      "title": "Andrew Ng — Machine Learning Specialization",
      "url": "https://www.coursera.org/specializations/machine-learning-introduction",
      "description": "The most popular introductory ML course in the world."
    },
    {
      "title": "Kaggle Learn — Intro to Machine Learning",
      "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
      "description": "Hands-on micro-course for the fundamentals."
    }
  ]
}
---

# ML-03-THE-LEARNING-PROBLEM: The Learning Problem

## Introduction

Formalize what a model learns: features, targets, hypotheses and loss — the vocabulary of every ML paper. By the end of this lesson you will be able to: Define features, targets and hypothesis space; Explain loss functions as learning signals; Describe the train-evaluate loop; Frame overfitting and underfitting intuitively.

## Key Concepts

### 1. Define features, targets and hypothesis space

Target: Define features, targets and hypothesis space. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
problem = {
    "features": ["age", "income", "region"],
    "target": "churn (0/1)",
    "loss": "log loss",
    "model_family": "logistic regression",
}
print(problem)
```
### 2. Explain loss functions as learning signals

Target: Explain loss functions as learning signals. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

def mse(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)

print("MSE:", mse([1, 2, 3], [1.1, 1.9, 3.2]))
```
### 3. Describe the train-evaluate loop

Target: Describe the train-evaluate loop. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# The learning loop: predict, measure, update
for epoch in range(3):
    loss = 1 / (epoch + 1)  # placeholder decreasing loss
    print(f"epoch {epoch}: loss={loss:.3f}")
```
### 4. Frame overfitting and underfitting intuitively

Target: Frame overfitting and underfitting intuitively. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Underfit: high bias. Overfit: high variance.
simple = np.polyfit([0, 1, 2, 3], [0, 1, 4, 9], deg=1)
complex = np.polyfit([0, 1, 2, 3], [0, 1, 4, 9], deg=3)
print("linear fit coefs:", simple.round(2))
print("cubic fit coefs:", complex.round(2))
```

## Practice Questions

1. What is the key idea behind "The Learning Problem"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Learning Problem with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Learning Problem"
1. "Provide advanced patterns and performance considerations for The Learning Problem"

## Key Takeaways

- Master the core ideas of The Learning Problem through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
