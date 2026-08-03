---
{
  "title": "Decision Trees",
  "description": "Greedy splits, impurity, and why trees are the most interpretable nonlinear models.",
  "type": "lesson",
  "order": 8,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain how trees choose splits with impurity",
    "Read and interpret a fitted tree",
    "Control depth to balance bias and variance",
    "Extract feature importances"
  ],
  "knowledge_refs": [
    "machine-learning/ml-07-logistic-regression",
    "reinforcement-learning/rl-02-markov-decision-processes"
  ],
  "prerequisites": [
    "ML-07: Logistic Regression"
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

# ML-08-DECISION-TREES: Decision Trees

## Introduction

Greedy splits, impurity, and why trees are the most interpretable nonlinear models. By the end of this lesson you will be able to: Explain how trees choose splits with impurity; Read and interpret a fitted tree; Control depth to balance bias and variance; Extract feature importances.

## Key Concepts

### 1. Explain how trees choose splits with impurity

Target: Explain how trees choose splits with impurity. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X, y)
print("accuracy:", round(tree.score(X, y), 3))
```
### 2. Read and interpret a fitted tree

Target: Read and interpret a fitted tree. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.tree import DecisionTreeClassifier, export_text

X = [[1, 1], [2, 2], [3, 3], [10, 10]]
y = [0, 0, 1, 1]
tree = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)
print(export_text(tree, feature_names=["a", "b"]))
```
### 3. Control depth to balance bias and variance

Target: Control depth to balance bias and variance. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
for depth in [1, 3, 20]:
    t = DecisionTreeClassifier(max_depth=depth, random_state=0).fit(X, y)
    print(f"depth={depth}: train acc {t.score(X, y):.3f}")
```
### 4. Extract feature importances

Target: Extract feature importances. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
rf = RandomForestClassifier(random_state=0).fit(X, y)
print("importances:", rf.feature_importances_.round(3))
```

## Practice Questions

1. What is the key idea behind "Decision Trees"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Decision Trees with analogies and real-world examples"
1. "Show me common mistakes beginners make with Decision Trees"
1. "Provide advanced patterns and performance considerations for Decision Trees"

## Key Takeaways

- Master the core ideas of Decision Trees through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
