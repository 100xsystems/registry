---
{
  "title": "Types of Learning",
  "description": "Supervised, unsupervised and reinforcement learning — and the sub-tasks that fall under each.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Distinguish supervised, unsupervised and reinforcement learning",
    "Identify regression versus classification tasks",
    "Recognize clustering, anomaly detection and dimensionality reduction",
    "Choose the right learning type for a problem"
  ],
  "knowledge_refs": [
    "machine-learning/ml-01-what-is-machine-learning"
  ],
  "prerequisites": [
    "ML-01: What Is Machine Learning?"
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

# ML-02-TYPES-OF-LEARNING: Types of Learning

## Introduction

Supervised, unsupervised and reinforcement learning — and the sub-tasks that fall under each. By the end of this lesson you will be able to: Distinguish supervised, unsupervised and reinforcement learning; Identify regression versus classification tasks; Recognize clustering, anomaly detection and dimensionality reduction; Choose the right learning type for a problem.

## Key Concepts

### 1. Distinguish supervised, unsupervised and reinforcement learning

Target: Distinguish supervised, unsupervised and reinforcement learning. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
learning_types = {
    "supervised": ["regression", "classification"],
    "unsupervised": ["clustering", "anomaly detection", "dim reduction"],
    "reinforcement": ["policy learning"],
}
for kind, tasks in learning_types.items():
    print(f"{kind:14} -> {
```
### 2. Identify regression versus classification tasks

Target: Identify regression versus classification tasks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
.join(tasks)}")
```
### 3. Recognize clustering, anomaly detection and dimensionality reduction

Target: Recognize clustering, anomaly detection and dimensionality reduction. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
m = LogisticRegression(max_iter=200).fit(iris.data, iris.target)
print("classification accuracy:", round(m.score(iris.data, iris.target), 2))
```
### 4. Choose the right learning type for a problem

Target: Choose the right learning type for a problem. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.cluster import KMeans

X = [[0, 0], [0, 1], [1, 0], [10, 10], [10, 11]]
labels = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(X)
print("cluster labels:", labels)
```

## Practice Questions

1. What is the key idea behind "Types of Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Types of Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Types of Learning"
1. "Provide advanced patterns and performance considerations for Types of Learning"

## Key Takeaways

- Master the core ideas of Types of Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
