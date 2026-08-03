---
{
  "title": "Model Evaluation Metrics",
  "description": "Accuracy, precision, recall, F1, ROC-AUC and confusion matrices — the honest measurement of model quality.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read a confusion matrix",
    "Explain precision, recall, and F1",
    "Interpret ROC curves and AUC",
    "Choose the right metric for a business problem"
  ],
  "knowledge_refs": [
    "machine-learning/ml-18-classification-metrics",
    "data-science/ds-16-classification-models",
    "data-science/ds-14-train-test-split"
  ],
  "prerequisites": [
    "DS-17: Clustering"
  ],
  "references": [
    {
      "title": "scikit-learn — Model Evaluation",
      "url": "https://scikit-learn.org/stable/modules/model_evaluation.html",
      "description": "The official guide to every classification/regression metric."
    },
    {
      "title": "scikit-learn — Confusion Matrix",
      "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html",
      "description": "Visualizing and interpreting confusion matrices."
    },
    {
      "title": "Google ML Crash Course — Classification Metrics",
      "url": "https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc",
      "description": "Precision/recall and ROC-AUC explained with interactive examples."
    },
    {
      "title": "StatQuest — ROC and AUC",
      "url": "https://www.youtube.com/watch?v=4jRBRDbJemM",
      "description": "The clearest visual explanation of ROC curves."
    }
  ]
}
---

# DS-18-MODEL-EVALUATION: Model Evaluation Metrics

## Introduction

A model's "score" is meaningless without context. Is 90% accuracy good? For a spam filter where 99% of mail is legitimate — no, a model that always says "not spam" hits 99% accuracy while doing nothing. This lesson replaces naive accuracy with the metrics that actually measure quality: **confusion matrices, precision, recall, F1, and ROC-AUC**. The central skill is matching the metric to the *cost of being wrong* in your specific problem.

## Key Concepts

### 1. The confusion matrix

For binary classification, four cells capture everything:

| | Predicted positive | Predicted negative |
| --- | --- | --- |
| **Actual positive** | True Positive (TP) | False Negative (FN) |
| **Actual negative** | False Positive (FP) | True Negative (TN) |

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, preds)
print(cm)   # [[TN, FP], [FN, TP]]
```

Everything else is built from these four numbers.

### 2. Precision and recall: the two ways to be wrong

- **Precision = TP / (TP + FP)** — of the things I flagged as positive, how many were right? High precision = few false alarms.
- **Recall (sensitivity) = TP / (TP + FN)** — of the things that *were* positive, how many did I catch? High recall = few missed cases.

The two trade off against each other: flag everything and recall = 100% but precision collapses; flag almost nothing and precision is high but recall collapses. The right balance depends on which error is more expensive:

- **Fraud detection**: missing fraud (low recall) costs money → chase recall.
- **Legal email review**: wrongly flagging innocent mail (low precision) wastes lawyers' time → chase precision.

### 3. F1: the harmonic balance

**F1 = 2·precision·recall / (precision + recall)** — a single number that balances both. It is the standard summary when you care about *both* error types equally. (It's a harmonic mean, so it's harsh on imbalance: precision 1.0 + recall 0.1 → F1 ≈ 0.18.)

```python
from sklearn.metrics import precision_score, recall_score, f1_score

print(precision_score(y_test, preds))
print(recall_score(y_test, preds))
print(f1_score(y_test, preds))
```

### 4. Accuracy and when it lies

Accuracy = correct / total. It is reasonable for *balanced* classes and misleading for *imbalanced* ones. With 95% non-spam, the "always non-spam" model scores 95% accuracy and is useless. When classes are imbalanced, report precision/recall/F1 (and the confusion matrix) instead of, or alongside, accuracy.

### 5. ROC curves and AUC

The ROC curve shows the trade-off between true positive rate and false positive rate as you sweep the decision threshold. **AUC** (area under the curve) is one number summarizing "how well the model ranks positives above negatives":

- AUC 0.5 = random guessing; AUC 1.0 = perfect ranking.
- AUC is **threshold-independent** — it measures ranking quality, not a specific operating point.

```python
from sklearn.metrics import roc_auc_score, roc_curve

probs = model.predict_proba(X_test)[:, 1]
print(roc_auc_score(y_test, probs))        # ranking quality
fpr, tpr, _ = roc_curve(y_test, probs)     # plot for the full trade-off
```

Note the distinction: AUC tells you how well the model *ranks*; precision/recall at a chosen threshold tell you how well it *operates* at your business decision point. Both belong in a complete report.

### 6. Choosing metrics for your problem

A practical recipe:

1. Write down what each type of error *costs*.
2. Choose the primary metric that reflects that cost (recall for missed fraud, precision for false alarms, F1 for balance).
3. Report the confusion matrix + AUC alongside, so the number has context.
4. For regression, use RMSE/MAE/R² (see the regression lesson) — never accuracy.

## Practice Questions

1. For a cancer-screening model, which is worse: low precision or low recall? Justify.
2. Compute precision and recall from this confusion matrix: TN=900, FP=50, FN=10, TP=40.
3. Why can accuracy be 99% on a model that's useless?
4. What does AUC=0.5 mean? What does AUC measure that accuracy doesn't?

## LLM Prompts for Deeper Understanding

1. "Explain precision-recall trade-off with a concrete business scenario."
2. "When would I optimize for F1 vs AUC? What's the difference?"
3. "How do I evaluate an imbalanced dataset honestly?"

## Key Takeaways

- Accuracy lies on imbalanced data — use confusion matrices, precision/recall, F1.
- Precision = how many flags were right; recall = how many positives were caught.
- The metric you optimize must reflect the cost of each error type.
- ROC-AUC measures ranking quality and is threshold-independent.
- Always report context: confusion matrix + the business meaning of errors.

## Footnotes & Attribution

1. scikit-learn documentation, *Model Evaluation*. [https://scikit-learn.org/stable/modules/model_evaluation.html](https://scikit-learn.org/stable/modules/model_evaluation.html)
2. scikit-learn documentation, *Confusion Matrix*. [https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)
3. Google Developers, *ML Crash Course — Classification: ROC and AUC*. [https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)
4. Josh Starmer, *StatQuest — ROC and AUC*. [https://www.youtube.com/watch?v=4jRBRDbJemM](https://www.youtube.com/watch?v=4jRBRDbJemM)
