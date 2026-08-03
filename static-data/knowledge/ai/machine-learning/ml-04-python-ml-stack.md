---
{
  "title": "The Python ML Stack",
  "description": "Get fluent with scikit-learn: estimators, fit/predict, pipelines, and the dataset zoo used everywhere.",
  "type": "lesson",
  "order": 4,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use scikit-learn estimators with fit and predict",
    "Build pipelines that compose transforms and models",
    "Load built-in datasets for practice",
    "Inspect model parameters and hyperparameters"
  ],
  "knowledge_refs": [
    "machine-learning/ml-03-the-learning-problem"
  ],
  "prerequisites": [
    "ML-03: The Learning Problem"
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

# ML-04-PYTHON-ML-STACK: The Python ML Stack

## Introduction

Get fluent with scikit-learn: estimators, fit/predict, pipelines, and the dataset zoo used everywhere. By the end of this lesson you will be able to: Use scikit-learn estimators with fit and predict; Build pipelines that compose transforms and models; Load built-in datasets for practice; Inspect model parameters and hyperparameters.

## Key Concepts

### 1. Use scikit-learn estimators with fit and predict

Target: Use scikit-learn estimators with fit and predict. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

X, y = load_diabetes(return_X_y=True)
m = LinearRegression().fit(X, y)
print("R2:", round(m.score(X, y), 3))
```
### 2. Build pipelines that compose transforms and models

Target: Build pipelines that compose transforms and models. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=300))
pipe.fit(X, y)
print("pipeline accuracy:", round(pipe.score(X, y), 3))
```
### 3. Load built-in datasets for practice

Target: Load built-in datasets for practice. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.datasets import load_iris

iris = load_iris()
print("features:", iris.feature_names)
print("targets:", iris.target_names)
```
### 4. Inspect model parameters and hyperparameters

Target: Inspect model parameters and hyperparameters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.ensemble import RandomForestClassifier

m = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=0)
print("defaults ->", m.get_params()["n_estimators"], "trees")
```

## Practice Questions

1. What is the key idea behind "The Python ML Stack"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Python ML Stack with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Python ML Stack"
1. "Provide advanced patterns and performance considerations for The Python ML Stack"

## Key Takeaways

- Master the core ideas of The Python ML Stack through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
