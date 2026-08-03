---
{
  "title": "Gradient Boosting",
  "description": "Boosted trees — the tabular-data champion — fit sequentially to the mistakes of previous models.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain boosting versus bagging",
    "Fit gradient-boosted trees with scikit-learn and XGBoost-style APIs",
    "Tune learning rate versus tree count",
    "Use early stopping to avoid overfitting"
  ],
  "knowledge_refs": [
    "machine-learning/ml-09-ensemble-methods",
    "reinforcement-learning/rl-10-policy-gradient-methods"
  ],
  "prerequisites": [
    "ML-09: Ensemble Methods: Bagging & Random Forests"
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

# ML-10-GRADIENT-BOOSTING: Gradient Boosting

## Introduction

Boosted trees — the tabular-data champion — fit sequentially to the mistakes of previous models. By the end of this lesson you will be able to: Explain boosting versus bagging; Fit gradient-boosted trees with scikit-learn and XGBoost-style APIs; Tune learning rate versus tree count; Use early stopping to avoid overfitting.

## Key Concepts

### 1. Explain boosting versus bagging

Target: Explain boosting versus bagging. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
gb = GradientBoostingClassifier(random_state=0).fit(X, y)
print("GB accuracy:", round(gb.score(X, y), 3))
```
### 2. Fit gradient-boosted trees with scikit-learn and XGBoost-style APIs

Target: Fit gradient-boosted trees with scikit-learn and XGBoost-style APIs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.ensemble import GradientBoostingRegressor

X = [[i] for i in range(1, 21)]
y = [v ** 2 for v in range(1, 21)]
gb = GradientBoostingRegressor(learning_rate=0.1, n_estimators=100, random_state=0).fit(X, y)
print("pred(25):", round(gb.predict([[25]])[0], 1))
```
### 3. Tune learning rate versus tree count

Target: Tune learning rate versus tree count. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.ensemble import GradientBoostingRegressor

X = [[i] for i in range(50)]
y = [v * 2 + (v % 3) for v in range(50)]
# Lower learning rate needs more trees
for lr in [1.0, 0.05]:
    gb = GradientBoostingRegressor(learning_rate=lr, n_estimators=200, random_state=0).fit(X, y)
    print(f"lr={lr}: train R2 {gb.score(X, y):.3f}")
```
### 4. Use early stopping to avoid overfitting

Target: Use early stopping to avoid overfitting. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.ensemble import GradientBoostingRegressor

X = [[i] for i in range(100)]
y = [v + (v % 7) for v in range(100)]
gb = GradientBoostingRegressor(learning_rate=0.05, n_estimators=300, random_state=0)
gb.fit(X, y)
print("staged best:", gb.n_estimators_, "trees")
```

## Practice Questions

1. What is the key idea behind "Gradient Boosting"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Gradient Boosting with analogies and real-world examples"
1. "Show me common mistakes beginners make with Gradient Boosting"
1. "Provide advanced patterns and performance considerations for Gradient Boosting"

## Key Takeaways

- Master the core ideas of Gradient Boosting through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
