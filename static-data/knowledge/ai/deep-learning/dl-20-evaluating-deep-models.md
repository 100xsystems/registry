---
slug: dl-20-evaluating-deep-models
title: "Evaluating Deep Models"
description: "Beyond accuracy — calibration, robustness, fairness, and understanding what your model actually learned."
order: 20
tags:
  - deep-learning
  - evaluation
  - calibration
  - robustness
  - interpretability
prerequisites:
  - dl-10-the-training-loop
  - ml-18-classification-metrics
  - dl-06-loss-functions
references:
  - title: "On Calibration of Modern Neural Networks"
    url: "https://arxiv.org/abs/1706.04599"
    description: "Guo et al.'s paper showing modern NNs are poorly calibrated"
  - title: "Adversarial Examples in Deep Learning"
    url: "https://arxiv.org/abs/1412.6575"
    description: "Goodfellow et al.'s original adversarial examples paper"
  - title: "Grad-CAM: Visual Explanations from Deep Networks"
    url: "https://arxiv.org/abs/1610.02391"
    description: "Selvaraju et al.'s Grad-CAM for model interpretability"
  - title: "ImageNet-trained CNNs are Biased (Torralba & Efros)"
    url: "https://arxiv.org/abs/1605.02640"
    description: "Torralba & Efros on dataset bias and evaluation pitfalls"
  - title: "Beyond Accuracy: Behavioral Testing of NLP Models"
    url: "https://arxiv.org/abs/1902.01007"
    description: "Ribeiro et al.'s CheckList methodology for NLP evaluation"
knowledge_refs:
  - ml-18-classification-metrics
  - dl-10-the-training-loop
  - dl-14-transfer-learning
---

# Evaluating Deep Models

Accuracy is rarely sufficient. Deep models can be overconfident, brittle to adversarial attacks, biased against certain groups, and unable to explain their decisions. Comprehensive evaluation requires going beyond simple metrics.

## Beyond Accuracy: Key Metrics

### Top-5 Accuracy
Percentage where the correct label is among the model's top 5 predictions:
```python
top5_correct = (output.topk(5, dim=1).indices == target.unsqueeze(1)).any(dim=1).sum()
top5_acc = top5_correct / len(target)
```

### Confusion Matrix
Reveals which classes are confused with each other:
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_true, y_pred)
ConfusionMatrixDisplay(cm, display_labels=class_names).plot()
```

### Per-Class Metrics
Some classes may have much worse performance:
```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred, target_names=class_names))
```

## Model Calibration

Modern neural networks are **overconfident** — they output probabilities near 0 or 1 even when wrong.

**Expected Calibration Error (ECE)**: Groups predictions into bins and measures how well predicted probabilities match actual accuracy:
$$\text{ECE} = \sum_{b=1}^{B} \frac{|B_b|}{n} |\text{acc}(B_b) - \text{conf}(B_b)|$$

```python
def expected_calibration_error(predictions, labels, n_bins=15):
    confidences = predictions.max(dim=1).values
    accuracies = predictions.argmax(dim=1) == labels
    
    bin_boundaries = torch.linspace(0, 1, n_bins + 1)
    ece = 0
    for i in range(n_bins):
        mask = (confidences > bin_boundaries[i]) & (confidences <= bin_boundaries[i + 1])
        if mask.sum() > 0:
            bin_acc = accuracies[mask].float().mean()
            bin_conf = confidences[mask].mean()
            ece += mask.sum().float() / len(labels) * (bin_acc - bin_conf).abs()
    return ece
```

**Temperature scaling**: Simple post-hoc calibration:
```python
class TemperatureScaler(nn.Module):
    def __init__(self):
        super().__init__()
        self.temperature = nn.Parameter(torch.ones(1))
    
    def forward(self, logits):
        return logits / self.temperature

# Fit on validation set, apply at test time
```

## Robustness Testing

### Adversarial Examples
Imperceptible perturbations that fool the model:

```python
def fgsm_attack(model, x, y, epsilon=0.03):
    x.requires_grad = True
    output = model(x)
    loss = nn.CrossEntropyLoss()(output, y)
    loss.backward()
    
    # Add perturbation in the direction of gradient
    perturbed = x + epsilon * x.grad.sign()
    return perturbed.detach()
```

**Defense strategies:**
- Adversarial training (train on adversarial examples)
- Input preprocessing (JPEG compression, spatial smoothing)
- Certified defenses (randomized smoothing)

### Corruption Robustness
Test on corrupted versions of test data:
```python
# ImageNet-C: common corruptions
# Gaussian noise, blur, weather effects, digital artifacts
# Measures how well the model handles distribution shift
```

### Distribution Shift
Evaluate on data from different distributions:
- Different hospitals (medical imaging)
- Different camera types (autonomous driving)
- Different time periods (financial data)

## Interpretability

### Gradient-Based Methods

**Saliency Maps**: Direct gradient of output w.r.t. input:
```python
x.requires_grad = True
output = model(x)
output[0, target_class].backward()
saliency = x.grad.abs().max(dim=1)[0]
```

**Grad-CAM**: Gradient-weighted class activation mapping:
```python
import grad_cam  # or implement manually

# Get gradients of target class w.r.t. last conv layer
# Weight feature maps by gradient magnitude
# Produces a heatmap showing which regions matter most
```

**Integrated Gradients**: Axiomatically correct attribution method:
$$\text{IG}_i(x) = (x_i - x'_i) \times \int_0^1 \frac{\partial F(x' + \alpha(x-x'))}{\partial x_i} d\alpha$$

### Attention Visualization
In transformers, attention weights provide interpretability:
```python
# Visualize attention heads
# Different heads learn different patterns
# Useful for debugging and understanding
```

### Probing
Test what information is captured by intermediate representations:
```python
# Train a linear probe on frozen features
probe = nn.Linear(frozen_features.shape[1], num_classes)
probe.fit(frozen_features, labels)
# High accuracy → features capture this information
```

## Fairness Evaluation

Evaluate model performance across demographic groups:
```python
from fairlearn.metrics import MetricFrame

metric_frame = MetricFrame(
    metrics={'accuracy': accuracy_score, 'precision': precision_score},
    y_true=y_true, y_pred=y_pred, sensitive_features=groups
)

print(metric_frame.by_group)
print(metric_frame.difference())  # Disparity between groups
```

**Common fairness metrics:**
- Demographic parity: Equal prediction rates across groups
- Equalized odds: Equal TPR and FPR across groups
- Calibration: Equal accuracy within each confidence bin

## Evaluation Checklist

| Category | What to Check |
|---|---|
| **Performance** | Accuracy, top-5, per-class F1, confusion matrix |
| **Calibration** | ECE, reliability diagram, temperature scaling |
| **Robustness** | Adversarial accuracy, corruption accuracy, OOD detection |
| **Fairness** | Per-group metrics, bias audits |
| **Efficiency** | Latency, throughput, model size, memory |
| **Interpretability** | Grad-CAM, feature importance, attention patterns |
| **Edge cases** | Worst-case classes, rare events, boundary cases |

## Common Evaluation Mistakes

1. **Data leakage**: Test data accidentally included in training
2. **Wrong preprocessing**: Using test-time augmentation during evaluation
3. **Reporting only accuracy**: Missing class imbalance issues
4. **Overfitting to test set**: Multiple submissions → implicit training
5. **Not evaluating on real data**: Clean test set ≠ deployment conditions

## Practical Guidelines

1. **Always compute multiple metrics** — not just accuracy
2. **Plot confusion matrices** — reveals specific failure modes
3. **Check calibration** — especially for safety-critical applications
4. **Test robustness** — model should work on slightly different data
5. **Evaluate fairness** — especially for high-stakes decisions
6. **Use proper test sets** — held-out, representative, no leakage

## Further Reading

- Guo et al. (2017) showed modern NNs are poorly calibrated — essential reading
- Grad-CAM is the standard for visual model interpretability
- CheckList (Ribeiro et al., 2020) provides a behavioral testing methodology
- For adversarial robustness: Madry et al.'s adversarial training is the gold standard
