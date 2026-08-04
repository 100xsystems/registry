---
slug: ml-18-classification-metrics
title: "Classification Metrics Deep Dive"
description: "Accuracy is almost never the right metric — precision, recall, F1, AUC-ROC, and choosing what matters for your problem."
order: 18
tags:
  - machine-learning
  - evaluation
  - metrics
  - precision-recall
  - auc-roc
prerequisites:
  - ml-03-the-learning-problem
  - ml-07-logistic-regression
references:
  - title: "scikit-learn: Classification Metrics"
    url: "https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics"
    description: "Official documentation with comprehensive metric implementations"
  - title: "Wikipedia: F1 Score"
    url: "https://en.wikipedia.org/wiki/F-score"
    description: "Comprehensive treatment of F-score variants and their use cases"
  - title: "Sokolova & Lapalme: A systematic analysis of performance measures for classification tasks"
    url: "https://doi.org/10.1016/j.inffus.2009.03.004"
    description: "Analysis of when to use which classification metric"
  - title: "Davis & Goadrich: The Relationship Between Precision-Recall and ROC Curves"
    url: "https://doi.org/10.1145/1143844.1143874"
    description: "Seminal paper on PR vs ROC curves"
  - title: "Hand & Till: A Simple Generalisation of the Area Under the ROC Curve"
    url: "https://doi.org/10.1016/j.patrec.2002.04.002"
    description: "Mann-Whitney U statistic and multi-class AUC"
knowledge_refs:
  - ml-07-logistic-regression
  - ml-09-ensemble-methods
  - ml-16-cross-validation
---

# Classification Metrics Deep Dive

"Accuracy" on an imbalanced dataset is meaningless. If 99% of emails are not spam, a model that predicts "not spam" for everything has 99% accuracy but is useless. Choosing the right metric is as important as choosing the right model.

## The Confusion Matrix

Everything starts here:

|  | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

- **False Positive (Type I Error)**: Crying wolf — model says positive, reality says negative
- **False Negative (Type II Error)**: Missing the alarm — model says negative, reality says positive

## Core Metrics

### Accuracy
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

**When to use**: Balanced classes, equal cost of FP and FN. Almost never the right metric.

### Precision (Positive Predictive Value)
$$\text{Precision} = \frac{TP}{TP + FP}$$

**When to use**: Cost of false positive is high (spam filter — don't mark legitimate email as spam; medical diagnosis — don't give healthy patient bad news).

### Recall (Sensitivity, True Positive Rate)
$$\text{Recall} = \frac{TP}{TP + FN}$$

**When to use**: Cost of false negative is high (cancer screening — don't miss a cancer; fraud detection — don't let fraud through).

### F1 Score
$$F1 = 2 \cdot \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

The harmonic mean of precision and recall. Balances both concerns. Better than accuracy for imbalanced classes.

### F-beta Score
$$F_\beta = (1 + \beta^2) \cdot \frac{\text{Precision} \times \text{Recall}}{\beta^2 \cdot \text{Precision} + \text{Recall}}$$

- $\beta < 1$ (e.g., F0.5): Weights precision higher — prefer fewer false positives
- $\beta > 1$ (e.g., F2): Weights recall higher — prefer fewer false negatives

```python
from sklearn.metrics import fbeta_score
f2 = fbeta_score(y_true, y_pred, beta=2)  # recall-weighted
f05 = fbeta_score(y_true, y_pred, beta=0.5)  # precision-weighted
```

## Threshold-Dependent Metrics

Precision, recall, and F1 depend on a **decision threshold** (typically 0.5). But the optimal threshold depends on your problem's cost structure.

### ROC Curve and AUC-ROC

Plots **True Positive Rate** (recall) vs. **False Positive Rate** at every possible threshold:

$$\text{FPR} = \frac{FP}{FP + TN}$$

The **Area Under the ROC Curve** (AUC-ROC) summarizes performance across all thresholds:
- AUC = 1.0: Perfect classifier
- AUC = 0.5: Random classifier (no discrimination)
- AUC < 0.5: Worse than random (model is inverted)

```python
from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)
```

### Precision-Recall Curve and AUC-PR

More informative than ROC when classes are imbalanced:

```python
from sklearn.metrics import precision_recall_curve, average_precision_score

precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
ap = average_precision_score(y_true, y_scores)
```

**ROC vs PR curves:**
- **ROC**: Can be misleadingly optimistic with heavy class imbalance (FPR denominator includes all negatives)
- **PR**: Focuses on the positive class — better when positive class is rare

| Scenario | Use |
|---|---|
| Balanced classes | ROC-AUC is fine |
| Imbalanced classes | PR-AUC is more informative |
| Equal importance of FP/FN | ROC-AUC |
| Cost-sensitive | PR curve + threshold tuning |

## Multi-Class Metrics

For $K > 2$ classes:

**Macro-average**: Compute metric per class, then average (treats all classes equally):
```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred, average='macro'))
```

**Weighted-average**: Weight by class support (accounts for class imbalance):
```python
print(classification_report(y_true, y_pred, average='weighted'))
```

**Micro-average**: Aggregate TP, FP, FN globally (dominated by majority class):
```python
print(classification_report(y_true, y_pred, average='micro'))
```

### Cohen's Kappa

Measures agreement between predictions and true labels, corrected for chance:
$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

where $p_o$ is observed agreement and $p_e$ is expected agreement by chance.

```python
from sklearn.metrics import cohen_kappa_score
kappa = cohen_kappa_score(y_true, y_pred)
# κ > 0.8: excellent agreement
# κ = 0: no better than chance
```

## Choosing the Right Threshold

The default 0.5 threshold is rarely optimal:

```python
from sklearn.metrics import precision_recall_curve

precisions, recalls, thresholds = precision_recall_curve(y_true, y_scores)

# Find threshold for target recall
target_recall = 0.95
idx = (recalls >= target_recall).nonzero()[0][-1]
optimal_threshold = thresholds[idx]
print(f"Threshold: {optimal_threshold:.3f}, Precision: {precisions[idx]:.3f}")

# F1-optimized threshold
f1_scores = 2 * precisions[:-1] * recalls[:-1] / (precisions[:-1] + recalls[:-1] + 1e-8)
best_idx = f1_scores.argmax()
print(f"F1-optimal threshold: {thresholds[best_idx]:.3f}")
```

## Log Loss (Cross-Entropy)

Measures the quality of predicted probabilities, not just labels:

$$\text{Log Loss} = -\frac{1}{N}\sum_{i=1}^{N}\left[y_i\log(\hat{p}_i) + (1-y_i)\log(1-\hat{p}_i)\right]$$

Penalizes confident wrong predictions heavily. A model with 99% accuracy but terrible log loss is overconfident and poorly calibrated.

```python
from sklearn.metrics import log_loss
log_loss(y_true, y_prob)  # y_prob are probabilities, not labels
```

## Practical Decision Guide

| What you care about | Metric |
|---|---|
| Overall correctness (balanced) | Accuracy |
| Don't miss positives | Recall (or F2) |
| Don't false-alarm | Precision (or F0.5) |
| Balance precision/recall | F1 or PR-AUC |
| Ranking quality | ROC-AUC |
| Probability quality | Log Loss |
| Multi-class balanced | Macro F1 |
| Multi-class imbalanced | Weighted F1 |
| Agreement with chance removed | Cohen's Kappa |

## Common Mistakes

1. **Using accuracy on imbalanced data**: Always check class distribution first
2. **Not using the right averaging**: Macro vs micro vs weighted matters
3. **Using AUC-ROC when AUC-PR is more appropriate**: Check class balance
4. **Ignoring threshold optimization**: Don't assume 0.5 is optimal
5. **Not considering costs**: FP and FN may have very different costs

## Further Reading

- Sokolova & Lapalme's systematic analysis helps choose the right metric
- Davis & Goadrich show the relationship between ROC and PR curves
- For cost-sensitive classification, look into cost curves and cost-sensitive learning
- In production, always define your business metric and map it to a technical metric
