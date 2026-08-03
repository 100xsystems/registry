---
{
  "title": "Classification Metrics Deep Dive",
  "description": "Precision, recall, F1, ROC curves and calibration — choose the metric that matches the business cost.",
  "type": "lesson",
  "order": 18,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compute precision, recall, F1 and support",
    "Read ROC curves and compare models with AUC",
    "Explain calibration and reliability",
    "Choose a metric from business costs"
  ],
  "knowledge_refs": [
    "machine-learning/ml-17-hyperparameter-tuning",
    "computer-vision/cv-05-image-classification",
    "nlp/nlp-07-text-classification"
  ],
  "prerequisites": [
    "ML-16: Cross-Validation"
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

# ML-18-CLASSIFICATION-METRICS: Classification Metrics Deep Dive

## Introduction

Precision, recall, F1, ROC curves and calibration — choose the metric that matches the business cost. By the end of this lesson you will be able to: Compute precision, recall, F1 and support; Read ROC curves and compare models with AUC; Explain calibration and reliability; Choose a metric from business costs.

## Key Concepts

### 1. Compute precision, recall, F1 and support

Target: Compute precision, recall, F1 and support. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.metrics import classification_report

y_true = [0, 1, 1, 0, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1, 1, 1]
print(classification_report(y_true, y_pred, target_names=["neg", "pos"]))
```
### 2. Read ROC curves and compare models with AUC

Target: Read ROC curves and compare models with AUC. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.metrics import roc_curve, auc
import numpy as np

y_true = np.array([0, 0, 1, 1])
y_score = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, _ = roc_curve(y_true, y_score)
print("AUC:", round(auc(fpr, tpr), 3))
```
### 3. Explain calibration and reliability

Target: Explain calibration and reliability. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.calibration import calibration_curve

# Calibration: does 70% probability mean 70% of the time?
y_true = [0, 1, 0, 1, 1]
y_prob = [0.3, 0.7, 0.6, 0.9, 0.8]
fraction_positive, mean_predicted = calibration_curve(y_true, y_prob, n_bins=3)
print("mean predicted:", mean_predicted.round(2))
print("fraction positive:", fraction_positive.round(2))
```
### 4. Choose a metric from business costs

Target: Choose a metric from business costs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Cost-aware threshold: FP costs 1, FN costs 10
costs = {"fp": 1, "fn": 10}
for t in [0.5, 0.9]:
    preds = (np.array([0.4, 0.6, 0.95]) >= t).astype(int)
    print(f"t={t}: {preds}")
```

## Practice Questions

1. What is the key idea behind "Classification Metrics Deep Dive"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classification Metrics Deep Dive with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classification Metrics Deep Dive"
1. "Provide advanced patterns and performance considerations for Classification Metrics Deep Dive"

## Key Takeaways

- Master the core ideas of Classification Metrics Deep Dive through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
