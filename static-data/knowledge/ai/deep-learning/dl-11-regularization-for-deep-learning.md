---
slug: dl-11-regularization-for-deep-learning
title: "Regularization for Deep Learning"
description: "Preventing overfitting in deep networks — dropout, batch normalization, data augmentation, and weight decay."
order: 11
tags:
  - deep-learning
  - regularization
  - dropout
  - batch-norm
  - data-augmentation
prerequisites:
  - dl-10-the-training-loop
  - dl-09-building-an-mlp-in-pytorch
  - ml-15-regularization
references:
  - title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
    url: "https://jmlr.org/papers/v15/srivastava14a.html"
    description: "Srivastava et al.'s foundational dropout paper"
  - title: "Batch Normalization: Accelerating Deep Network Training"
    url: "https://arxiv.org/abs/1502.03167"
    description: "Ioffe & Szegedy's batch normalization paper"
  - title: "Bagging Predictors (Breiman, 1996)"
    url: "https://link.springer.com/article/10.1007/BF00140686"
    description: "The bootstrap aggregating paper that inspired dropout"
  - title: "Adam: Weight Decay as Regularization"
    url: "https://arxiv.org/abs/1711.05101"
    description: "Loshchilov & Hutter on decoupled weight decay in AdamW"
  - title: "Data Augmentation: A Survey"
    url: "https://arxiv.org/abs/2009.07830"
    description: "Shorten & Khoshgoftaar's comprehensive survey of augmentation techniques"
knowledge_refs:
  - ml-15-regularization
  - dl-10-the-training-loop
  - dl-12-convolutional-networks
---

# Regularization for Deep Learning

Deep networks have millions of parameters and can easily memorize training data. Regularization techniques prevent overfitting by constraining the model's capacity or artificially increasing the diversity of training data.

## The Overfitting Problem

A model with too much capacity relative to data learns noise instead of patterns:

**Training accuracy**: 99.5%
**Test accuracy**: 85.0%
**Gap**: 14.5% → severe overfitting

Regularization reduces this gap by:
- Adding noise during training (dropout, data augmentation)
- Constraining weights (weight decay, max norm)
- Regularizing activations (batch normalization)
- Early stopping

## Dropout

Randomly zeros out a fraction of neurons during each forward pass:

$$h_j = \begin{cases} 0 & \text{with probability } p \\ h_j / (1-p) & \text{otherwise} \end{cases}$$

```python
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Dropout(0.5),  # 50% dropout
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),  # 30% dropout
            nn.Linear(128, 10)
        )
    
    def forward(self, x):
        return self.layers(x)

model.train()   # Dropout ON
model.eval()    # Dropout OFF
```

**Why it works:**
- Each forward pass uses a different random sub-network
- Forces neurons to be independently useful (can't rely on specific co-adaptations)
- At test time, all neurons active but scaled — ensemble effect

**Dropout rates:**
- Hidden layers: 0.2-0.5 (standard)
- Input layer: 0.1-0.2 (less common)
- After attention: 0.1 (transformers use this)
- Never on output layer

## Batch Normalization

Normalizes activations within each mini-batch to have zero mean and unit variance:

$$\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$
$$y_i = \gamma \hat{x}_i + \beta$$

where $\gamma$ and $\beta$ are learnable parameters (scale and shift).

```python
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.BatchNorm1d(256),  # After linear, before activation
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

**Benefits:**
- Faster training (allows higher learning rates)
- Reduces internal covariate shift
- Mild regularization effect (batch statistics add noise)
- Makes initialization less critical

**Running statistics**: During training, BN maintains running mean/variance. During eval, uses these instead of batch statistics.

```python
# BN layers behave differently in train vs eval mode
model.train()   # Uses batch statistics + updates running stats
model.eval()    # Uses running statistics
```

**For convolutions**: Use `nn.BatchNorm2d(channels)` — normalizes per-channel over spatial dimensions.

## Weight Decay (L2 Regularization)

Adds a penalty proportional to the squared magnitude of weights:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \sum w_i^2$$

```python
# L2 regularization via weight decay
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)

# Or via L2 penalty (less common in deep learning)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=0.01)
```

**AdamW vs Adam**: AdamW applies weight decay correctly (decoupled from gradient). Adam's weight decay is slightly wrong (through the adaptive learning rate).

## Data Augmentation

Artificially increase training data variety by applying transformations:

```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(10),
    transforms.RandomCrop(32, padding=4),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Test time: no augmentation
test_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
```

**Common augmentations:**
| Technique | Use For | Effect |
|---|---|---|
| Random flip | Images | Horizontal flip invariance |
| Random crop | Images | Translation invariance |
| Color jitter | Images | Color invariance |
| RandAugment | Images | Auto augment policy |
| Text back-translation | NLP | Paraphrase invariance |
| SpecAugment | Audio | Time/frequency masking |
| Mixup | Any | Interpolates samples + labels |
| CutMix | Images | Combines patches from two images |

### Mixup and CutMix

```python
# Mixup: interpolate between two training examples
def mixup(x1, y1, x2, y2, alpha=0.2):
    lam = np.random.beta(alpha, alpha)
    x = lam * x1 + (1 - lam) * x2
    y = lam * y1 + (1 - lam) * y2
    return x, y

# CutMix: paste a patch from one image onto another
# Improves both accuracy and calibration
```

## Label Smoothing

Instead of hard labels (0 or 1), use soft targets:
$$y_{\text{smooth}} = (1 - \epsilon) \cdot y_{\text{hard}} + \frac{\epsilon}{K}$$

```python
loss_fn = nn.CrossEntropyLoss(label_smoothing=0.1)
```

Prevents the model from becoming overconfident. Standard in transformer training.

## Early Stopping

Monitor validation loss and stop when it starts increasing:

```python
best_val_loss = float('inf')
patience = 10
counter = 0

for epoch in range(max_epochs):
    train_loss = train_epoch(model, train_loader, optimizer, criterion, device)
    val_loss = evaluate_loss(model, val_loader, criterion, device)
    
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        counter = 0
        torch.save(model.state_dict(), 'best_model.pth')
    else:
        counter += 1
        if counter >= patience:
            break
```

## Max-Norm Clipping

Clip weight norms during training:
```python
# After each optimizer step
for p in model.parameters():
    if p.grad is not None:
        norm = p.data.norm(2)
        if norm > max_norm:
            p.data.mul_(max_norm / norm)
```

## Regularization Strategy by Architecture

| Architecture | Primary Regularization |
|---|---|
| MLP | Dropout (0.2-0.5) + weight decay |
| CNN | Data augmentation + weight decay + batch norm |
| RNN/LSTM | Weight tying + dropout + gradient clipping |
| Transformer | Dropout (0.1) + weight decay + label smoothing + data augmentation |
| Vision Transformer | Strong augmentation (RandAugment, Mixup) + dropout |

## Combining Regularization Methods

Most production models use multiple regularization methods together:

```python
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.BatchNorm1d(256),  # 1. Batch normalization
    nn.ReLU(),
    nn.Dropout(0.3),       # 2. Dropout
    nn.Linear(256, 10)
)

# 3. Weight decay via optimizer
optimizer = AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)

# 4. Label smoothing in loss
criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

# 5. Data augmentation in data pipeline
train_transform = transforms.Compose([...])

# 6. Early stopping in training loop
```

## Further Reading

- Srivastava et al.'s dropout paper is foundational
- Ioffe & Szegedy's batch norm paper transformed deep learning practice
- For modern augmentation: RandAugment (Cubuk et al., 2020) and TrivialAugment
- Mixup and CutMix are essential for vision transformers
