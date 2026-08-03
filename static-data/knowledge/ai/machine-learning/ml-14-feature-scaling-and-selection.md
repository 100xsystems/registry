---
{
  "title": "Feature Scaling & Selection",
  "description": "Prepare features so models learn well: scaling, encoding, selection, and dropping noise.",
  "type": "lesson",
  "order": 14,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Scale features for distance and gradient models",
    "Encode categoricals without leaking order",
    "Select features with importance and statistical filters",
    "Explain why removing noise features helps"
  ],
  "knowledge_refs": [
    "machine-learning/ml-13-naive-bayes",
    "computer-vision/cv-13-feature-detection",
    "generative-ai/genai-06-llm-architecture"
  ],
  "prerequisites": [
    "ML-08: Decision Trees"
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

# ML-14-FEATURE-SCALING-AND-SELECTION: Feature Scaling & Selection

## Introduction

Prepare features so models learn well: scaling, encoding, selection, and dropping noise. By the end of this lesson you will be able to: Scale features for distance and gradient models; Encode categoricals without leaking order; Select features with importance and statistical filters; Explain why removing noise features helps.

## Key Concepts

### 1. Scale features for distance and gradient models

Target: Scale features for distance and gradient models. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = [[0, 10], [1, 20], [2, 30]]
print("standard:", StandardScaler().fit_transform(X).round(2))
print("minmax:", MinMaxScaler().fit_transform(X).round(2))
```
### 2. Encode categoricals without leaking order

Target: Encode categoricals without leaking order. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(sparse_output=False)
print(enc.fit_transform([["red"], ["green"], ["blue"]]))
```
### 3. Select features with importance and statistical filters

Target: Select features with importance and statistical filters. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

X = [[1, 2, 100], [2, 3, 200], [3, 4, 300]]
y = [0, 1, 1]
rf = RandomForestClassifier(random_state=0).fit(X, y)
selector = SelectFromModel(rf, max_features=2)
print("kept features:", selector.transform(X).shape[1])
```
### 4. Explain why removing noise features helps

Target: Explain why removing noise features helps. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# A useless feature (pure noise) should be dropped
rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
noise = rng.normal(size=(200, 10))
print("variance of useful feature:", round(X.var(), 3))
print("mean variance of noise:", round(noise.var(), 3))
```

## Practice Questions

1. What is the key idea behind "Feature Scaling & Selection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Feature Scaling & Selection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Feature Scaling & Selection"
1. "Provide advanced patterns and performance considerations for Feature Scaling & Selection"

## Key Takeaways

- Master the core ideas of Feature Scaling & Selection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
