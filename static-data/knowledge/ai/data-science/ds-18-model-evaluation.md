---
{
  "title": "Model Evaluation Metrics",
  "description": "Accuracy is a trap. Learn precision, recall, F1, ROC curves, and the confusion matrix inside out.",
  "type": "lesson",
  "order": 18,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read a confusion matrix correctly",
    "Compute precision, recall and F1",
    "Explain the precision-recall trade-off",
    "Use ROC-AUC for ranking quality"
  ],
  "knowledge_refs": [
    "data-science/ds-18-model-evaluation"
  ],
  "prerequisites": [
    "DS-16: Classification Models"
  ],
  "references": [
    {
      "title": "Python for Data Analysis — Wes McKinney",
      "url": "https://wesmckinney.com/book/",
      "description": "The definitive guide to pandas, NumPy and the PyData stack."
    },
    {
      "title": "Pandas User Guide",
      "url": "https://pandas.pydata.org/docs/user_guide/index.html",
      "description": "Official documentation for the pandas data-analysis library."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Kaggle Learn — Data Science",
      "url": "https://www.kaggle.com/learn",
      "description": "Hands-on micro-courses covering pandas, EDA and modeling."
    },
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "Authoritative guide to the Python machine-learning toolbox."
    }
  ]
}
---

# DS-18-MODEL-EVALUATION: Model Evaluation Metrics

## Introduction

Accuracy is a trap. Learn precision, recall, F1, ROC curves, and the confusion matrix inside out. By the end of this lesson you will be able to: Read a confusion matrix correctly; Compute precision, recall and F1; Explain the precision-recall trade-off; Use ROC-AUC for ranking quality.

## Key Concepts

### 1. Read a confusion matrix correctly

Target: Read a confusion matrix correctly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.metrics import confusion_matrix

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]
print(confusion_matrix(y_true, y_pred))
```
### 2. Compute precision, recall and F1

Target: Compute precision, recall and F1. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.metrics import precision_score, recall_score, f1_score

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]
print("precision:", round(precision_score(y_true, y_pred), 2))
print("recall:", round(recall_score(y_true, y_pred), 2))
print("F1:", round(f1_score(y_true, y_pred), 2))
```
### 3. Explain the precision-recall trade-off

Target: Explain the precision-recall trade-off. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.metrics import roc_auc_score

y_true = [0, 1, 1, 0, 1, 0]
y_prob = [0.1, 0.9, 0.4, 0.2, 0.8, 0.7]
print("ROC-AUC:", round(roc_auc_score(y_true, y_prob), 3))
```
### 4. Use ROC-AUC for ranking quality

Target: Use ROC-AUC for ranking quality. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Threshold sweep: raising the bar boosts precision, cuts recall
scores = np.array([0.2, 0.5, 0.7, 0.9])
labels = np.array([0, 1, 0, 1])
for t in [0.3, 0.6, 0.8]:
    preds = (scores >= t).astype(int)
    tp = ((preds == 1) & (labels == 1)).sum()
    fp = ((preds == 1) & (labels == 0)).sum()
    fn = ((preds == 0) & (labels == 1)).sum()
    prec = tp / (tp + fp) if tp + fp else 0
    rec = tp / (tp + fn) if tp + fn else 0
    print(f"t={t}: precision={prec:.2f} recall={rec:.2f}")
```

## Practice Questions

1. What is the key idea behind "Model Evaluation Metrics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Model Evaluation Metrics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Model Evaluation Metrics"
1. "Provide advanced patterns and performance considerations for Model Evaluation Metrics"

## Key Takeaways

- Master the core ideas of Model Evaluation Metrics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
