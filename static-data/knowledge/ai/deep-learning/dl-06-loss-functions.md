---
slug: dl-06-loss-functions
title: "Loss Functions"
description: "The objective functions that define what 'good' means for your neural network — cross-entropy, MSE, and beyond."
order: 6
tags:
  - deep-learning
  - loss-functions
  - cross-entropy
  - mse
prerequisites:
  - dl-04-forward-propagation
  - dl-05-backpropagation
references:
  - title: "Deep Learning Book: Chapter 5 — Machine Learning Basics"
    url: "https://www.deeplearningbook.org/contents/ml.html"
    description: "Goodfellow et al.'s treatment of loss functions in the ML context"
  - title: "PyTorch Loss Functions Documentation"
    url: "https://pytorch.org/docs/stable/nn.html#loss-functions"
    description: "Official reference for all built-in PyTorch loss functions"
  - title: "Focal Loss for Dense Object Detection"
    url: "https://arxiv.org/abs/1708.02002"
    description: "Lin et al.'s focal loss — addressing class imbalance in object detection"
  - title: "A Comprehensive Survey of Loss Functions in ML"
    url: "https://arxiv.org/abs/2101.04220"
    description: "Thung & Yang's survey covering classification, regression, and generative losses"
  - title: "Label Smoothing and Knowledge Distillation"
    url: "https://arxiv.org/abs/1512.00567"
    description: "Szegedy et al.'s label smoothing technique — regularization via loss modification"
knowledge_refs:
  - dl-05-backpropagation
  - dl-03-activation-functions
  - dl-18-evaluating-deep-models
---

# Loss Functions

The loss function measures how wrong the network's prediction is. It's the signal that drives learning — gradients of the loss tell every weight how to change. Choosing the right loss function is as important as choosing the right architecture.

## Classification Losses

### Binary Cross-Entropy (BCE)

For binary classification (0 or 1):
$$\mathcal{L} = -\frac{1}{N}\sum_{i=1}^{N}\left[y_i \log(\hat{p}_i) + (1-y_i)\log(1-\hat{p}_i)\right]$$

where $\hat{p}_i = \sigma(z_i)$ is the sigmoid output (predicted probability of class 1).

```python
# With sigmoid output
loss = nn.BCELoss()
pred = torch.sigmoid(model(x))
l = loss(pred, target.float())

# Numerically stable (combines sigmoid + BCE)
loss = nn.BCEWithLogitsLoss()
logits = model(x)  # raw output, no sigmoid
l = loss(logits, target.float())
```

**Always use `BCEWithLogitsLoss`** — it's numerically more stable than applying sigmoid then BCE.

### Categorical Cross-Entropy (CE)

For multi-class classification ($K$ classes):
$$\mathcal{L} = -\frac{1}{N}\sum_{i=1}^{N}\sum_{k=1}^{K} y_{ik} \log(\hat{p}_{ik})$$

where $\hat{p}_{ik} = \text{softmax}(z_i)_k$.

```python
# PyTorch combines LogSoftmax + NLLLoss
loss = nn.CrossEntropyLoss()
logits = model(x)  # raw output, shape (N, K)
l = loss(logits, target)  # target is class indices, not one-hot
```

**Critical**: `CrossEntropyLoss` expects **raw logits**, not softmax outputs. Applying softmax first causes numerical instability.

### Label Smoothing

Instead of hard labels (0 or 1), use soft labels ($\epsilon/K$ and $1-\epsilon+\epsilon/K$):
$$y_{\text{smooth}} = (1-\epsilon) y_{\text{hard}} + \frac{\epsilon}{K}$$

```python
loss = nn.CrossEntropyLoss(label_smoothing=0.1)
```

**Why it works**: Prevents the model from becoming overconfident. Acts as regularization. Improves calibration.

### Focal Loss

Down-weights easy examples, focuses on hard ones:
$$\mathcal{L}_{\text{focal}} = -\alpha_t (1-p_t)^\gamma \log(p_t)$$

where $\gamma = 2$ (standard) controls the focusing parameter.

```python
# Custom focal loss
def focal_loss(logits, target, gamma=2.0, alpha=0.25):
    ce = nn.functional.cross_entropy(logits, target, reduction='none')
    pt = torch.exp(-ce)
    focal = alpha * (1 - pt) ** gamma * ce
    return focal.mean()
```

**Use case**: Object detection (RetinaNet), imbalanced classification.

## Regression Losses

### Mean Squared Error (MSE / L2 Loss)

$$\mathcal{L} = \frac{1}{N}\sum_{i=1}^{N}(\hat{y}_i - y_i)^2$$

```python
loss = nn.MSELoss()
l = loss(predictions, targets)
```

**Properties**: Differentiable everywhere. Penalizes large errors heavily (squaring). Sensitive to outliers.

### Mean Absolute Error (MAE / L1 Loss)

$$\mathcal{L} = \frac{1}{N}\sum_{i=1}^{N}|\hat{y}_i - y_i|$$

```python
loss = nn.L1Loss()
l = loss(predictions, targets)
```

**Properties**: Robust to outliers. Not differentiable at 0 (use subgradient). Gradients are constant magnitude.

### Huber Loss (Smooth L1)

Combines MSE and MAE — quadratic near zero, linear for large errors:
$$\mathcal{L}_\delta = \begin{cases} \frac{1}{2}(\hat{y}-y)^2 & \text{if } |\hat{y}-y| \leq \delta \\ \delta(|\hat{y}-y| - \frac{1}{2}\delta) & \text{otherwise} \end{cases}$$

```python
loss = nn.HuberLoss(delta=1.0)  # delta controls the transition point
```

**Best of both worlds**: Smooth near zero (like MSE), robust to outliers (like MAE). Widely used in object detection (Smooth L1).

### Log-Cosh Loss

$$\mathcal{L} = \frac{1}{N}\sum_{i=1}^{N}\log(\cosh(\hat{y}_i - y_i))$$

Approximates MSE for small errors, MAE for large errors. Smooth and differentiable everywhere.

## Losses for Specific Tasks

### Triplet Loss (Metric Learning)

$$\mathcal{L} = \max(0, d(a, p) - d(a, n) + \text{margin})$$

Ensures anchor is closer to positive than to negative by at least `margin`.

```python
loss = nn.TripletMarginLoss(margin=1.0)
anchor = model(anchor_images)
positive = model(positive_images)
negative = model(negative_images)
l = loss(anchor, positive, negative)
```

### Cosine Embedding Loss

$$\mathcal{L} = \begin{cases} 1 - \cos(x_1, x_2) & \text{if } y = 1 \\ \max(0, \cos(x_1, x_2) - \text{margin}) & \text{if } y = -1 \end{cases}$$

Used for semantic similarity, sentence embeddings.

### KL Divergence Loss

$$D_{KL}(P \| Q) = \sum_i P(i) \log\frac{P(i)}{Q(i)}$$

Used in VAEs, knowledge distillation, and distribution matching:

```python
loss = nn.KLDivLoss(reduction='batchmean')
log_pred = F.log_softmax(model(x), dim=-1)
target_dist = F.softmax(target_model(x), dim=-1)
l = loss(log_pred, target_dist)
```

## Choosing the Right Loss

| Task | Loss Function | Notes |
|---|---|---|
| Binary classification | BCEWithLogitsLoss | Always use with logits version |
| Multi-class classification | CrossEntropyLoss | Raw logits, not softmax |
| Imbalanced classification | Focal Loss or weighted CE | Down-weight majority class |
| Regression (clean data) | MSE | Standard choice |
| Regression (outliers) | Huber / MAE | Robust to outliers |
| Object detection | Smooth L1 + CE | Box regression + classification |
| Image generation (GAN) | Wasserstein / hinge | More stable than vanilla BCE |
| Sequence generation | Cross-entropy (teacher forcing) | Next-token prediction |
| Self-supervised | Contrastive loss, VICReg | Representation learning |
| Knowledge distillation | KL divergence | Soft target matching |

## Numerical Stability

```python
# WRONG: Applying log to very small probabilities
loss = -torch.log(softmax(logits))  # log(0) = -inf

# RIGHT: Use PyTorch's numerically stable implementation
loss = nn.CrossEntropyLoss()(logits, targets)  # LogSumExp trick internally

# For custom losses, always add epsilon
epsilon = 1e-7
loss = -torch.log(predictions + epsilon)
```

## Loss Function Debugging

```python
# Monitor loss during training
for epoch in range(num_epochs):
    train_loss = train_one_epoch(model, train_loader, optimizer, criterion)
    val_loss = evaluate(model, val_loader, criterion)
    
    # Check for:
    # 1. Loss not decreasing → wrong learning rate, bad model, wrong loss
    # 2. Loss oscillating → learning rate too high
    # 3. Loss going to NaN → exploding gradients, numerical issues
    # 4. Train loss << val loss → overfitting
    # 5. Train loss ≈ val loss ≈ random → underfitting
```

## Further Reading

- Goodfellow et al. Chapter 5 covers loss functions from an ML perspective
- Focal loss paper is essential for anyone working on imbalanced classification
- Label smoothing has become standard in transformer training
- For generative models: adversarial losses (GAN, WGAN) are a whole topic
