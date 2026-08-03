---
{
  "title": "What Is Machine Learning?",
  "description": "Define machine learning, contrast it with rules-based programming, and survey where ML wins in production.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define machine learning and its core components",
    "Contrast ML with hand-written rules",
    "Name the main families of ML tasks",
    "Identify good first problems for ML"
  ],
  "knowledge_refs": [
    "machine-learning/ml-01-what-is-machine-learning"
  ],
  "prerequisites": [],
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

# ML-01-WHAT-IS-MACHINE-LEARNING: What Is Machine Learning?

## Introduction

Define machine learning, contrast it with rules-based programming, and survey where ML wins in production. By the end of this lesson you will be able to: Define machine learning and its core components; Contrast ML with hand-written rules; Name the main families of ML tasks; Identify good first problems for ML.

## Key Concepts

### 1. Define machine learning and its core components

Target: Define machine learning and its core components. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Rules: if x > 3: y = 1. Learned: fit a line to data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression().fit(X, y)
print("learned slope:", round(model.coef_[0], 2))
```
### 2. Contrast ML with hand-written rules

Target: Contrast ML with hand-written rules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
task = {
    "supervised": "learn from labeled examples",
    "unsupervised": "find structure in unlabeled data",
    "reinforcement": "learn from rewards and actions",
}
for name, desc in task.items():
    print(f"{name:14} {desc}")
```
### 3. Name the main families of ML tasks

Target: Name the main families of ML tasks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
candidates = ["spam filter", "fraud detection", "product ranking", "sensor anomaly detection"]
for c in candidates:
    print(f"- {c}")
```
### 4. Identify good first problems for ML

Target: Identify good first problems for ML. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Even a dumb baseline matters: predict the majority class
labels = np.array([0, 0, 0, 1, 1])
baseline = labels.mean() > 0.5
print("majority-class baseline:", int(baseline))
```

## Practice Questions

1. What is the key idea behind "What Is Machine Learning?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Machine Learning? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Machine Learning?"
1. "Provide advanced patterns and performance considerations for What Is Machine Learning?"

## Key Takeaways

- Master the core ideas of What Is Machine Learning? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
