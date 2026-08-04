---
slug: ml-15-regularization
title: "Regularization"
description: "The art of preventing overfitting — L1, L2, Elastic Net, dropout, and early stopping as implicit regularization."
order: 15
tags:
  - machine-learning
  - regularization
  - overfitting
  - l1
  - l2
  - elastic-net
prerequisites:
  - ml-03-the-learning-problem
  - ml-07-logistic-regression
  - ml-06-gradient-descent
references:
  - title: "Elements of Statistical Learning, Ch. 3 & 7"
    url: "https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf"
    description: "Chapters on model assessment, regularization, and shrinkage methods"
  - title: "An Overview of Regularization Methods in Machine Learning"
    url: "https://towardsdatascience.com/regularization-in-machine-learning-7633c782521d"
    description: "Comprehensive overview of all regularization techniques"
  - title: "The Elements of Statistical Learning: Ridge vs Lasso"
    url: "https://www.stat.cmu.edu/~larry/all-of-statistical-learning.pdf"
    description: "James, Witten, Hastie, Tibshirani — practical comparison of Ridge and Lasso"
  - title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
    url: "https://jmlr.org/papers/v15/srivastava14a.html"
    description: "The foundational dropout paper by Srivastava et al."
  - title: "Early Stopping — but When?"
    url: "https://www.cs.toronto.edu/~hinton/absps/earlystop.pdf"
    description: "Yao et al. (2007) on early stopping as regularization"
knowledge_refs:
  - ml-03-the-learning-problem
  - ml-14-feature-scaling
  - ml-16-cross-validation
---

# Regularization

Overfitting is the central challenge of machine learning. Regularization is any technique that constrains model complexity to improve generalization. Understanding regularization is understanding the bias-variance trade-off in practice.

## The Problem: Overfitting

A model that perfectly memorizes training data but fails on new data has overfit. This happens when the model is too complex relative to the amount of training data:

- **Too many parameters**: Model has capacity to memorize noise
- **Too few training examples**: Not enough data to constrain the model
- **Noisy features**: Irrelevant features add noise the model can exploit

**Symptoms**: Training loss very low, validation loss increasing. Large gap between train and test performance.

## L2 Regularization (Ridge / Weight Decay)

Adds the **squared magnitude** of weights to the loss:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \sum_{j=1}^{D} w_j^2$$

The penalty $\lambda$ (alpha) pushes all weights toward zero but never exactly to zero. This:
- Prevents any single feature from dominating
- Makes the model more robust to noise
- Smooths the decision boundary

**Effect on weights**: L2 shrinks all weights proportionally. Large weights shrink more. The resulting model is smoother and more generalizable.

```python
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)  # lambda parameter
ridge.fit(X_train, y_train)
```

**Closed-form solution**: Unlike unregularized linear regression, Ridge has a direct solution:
$$\hat{\mathbf{w}} = (X^TX + \lambda I)^{-1}X^Ty$$

The $\lambda I$ term ensures the matrix is always invertible, even when features are perfectly correlated.

## L1 Regularization (Lasso)

Adds the **absolute magnitude** of weights to the loss:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \sum_{j=1}^{D} |w_j|$$

The key difference from L2: L1 **sets some weights to exactly zero**, performing automatic feature selection.

**Geometric intuition**: L1 creates a diamond-shaped constraint region. The optimal solution often lies at the corners (where some weights are zero). L2 creates a circular region, and the optimal solution rarely hits the boundary.

```python
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.01)
lasso.fit(X_train, y_train)
print(f"Non-zero features: {(lasso.coef_ != 0).sum()} / {len(lasso.coef_)}")
```

## Elastic Net: Best of Both Worlds

Combines L1 and L2:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \alpha \left( \rho \sum |w_j| + \frac{1-\rho}{2} \sum w_j^2 \right)$$

where $\rho$ (l1_ratio) controls the mix:
- $\rho = 1$: Pure L1 (Lasso)
- $\rho = 0$: Pure L2 (Ridge)
- $\rho = 0.5$: Equal mix (default)

```python
from sklearn.linear_model import ElasticNet

en = ElasticNet(alpha=0.01, l1_ratio=0.5)
en.fit(X_train, y_train)
```

**When to use Elastic Net**:
- Correlated features (Lasso arbitrarily picks one)
- High-dimensional data with groups of correlated features
- When you want both feature selection and stability

## Choosing Alpha (Regularization Strength)

The regularization parameter $\alpha$ (or $\lambda$) controls the trade-off:
- $\alpha = 0$: No regularization (overfits)
- $\alpha \to \infty$: All weights zero (underfits)

**Cross-validation** is the standard approach:
```python
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV

# Ridge with built-in CV
ridge_cv = RidgeCV(alphas=[0.001, 0.01, 0.1, 1.0, 10.0, 100.0], cv=5)
ridge_cv.fit(X_train, y_train)
print(f"Best alpha: {ridge_cv.alpha_}")

# Lasso with built-in CV
lasso_cv = LassoCV(cv=5, n_alphas=100, random_state=42)
lasso_cv.fit(X_train, y_train)
print(f"Best alpha: {lasso_cv.alpha_}")
```

## Regularization in Neural Networks

### Dropout (Srivastava et al., 2014)
Randomly zeros out a fraction of neurons during training:
```python
import torch.nn as nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Dropout(0.5),  # 50% of neurons zeroed during training
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 10)
        )
```

**Why it works**: Each forward pass uses a different random sub-network. At test time, all neurons are active but scaled. This forces the network to learn redundant representations.

### Weight Decay
L2 regularization applied to neural network weights:
```python
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
```

### Batch Normalization
Normalizes activations within each mini-batch. Has an implicit regularization effect because each batch introduces noise.

### Data Augmentation
Not technically regularization, but serves the same purpose — artificially increasing training data variety:
```python
from torchvision import transforms
augment = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomCrop(32, padding=4),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
])
```

## Early Stopping

Monitor validation loss during training and stop when it starts increasing:

```python
best_val_loss = float('inf')
patience = 10
patience_counter = 0

for epoch in range(max_epochs):
    train(model, train_loader)
    val_loss = evaluate(model, val_loader)
    
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        patience_counter = 0
        save_checkpoint(model)
    else:
        patience_counter += 1
        if patience_counter >= patience:
            break  # stop training

model = load_checkpoint()  # restore best model
```

**Early stopping as implicit L2 regularization**: For linear models with gradient descent, early stopping with $T$ steps is equivalent to L2 regularization with $\lambda \propto 1/T$.

## When to Use What

| Scenario | Regularization |
|---|---|
| Linear/Logistic regression | L1 (feature selection), L2 (default), Elastic Net |
| Neural networks | Dropout + weight decay + data augmentation |
| Tree ensembles | n_estimators (early stopping), max_depth, min_samples_leaf |
| Small dataset | Stronger regularization (higher $\alpha$, more dropout) |
| High-dimensional data | L1 or Elastic Net |
| Many correlated features | Elastic Net or Ridge |

## Practical Tips

1. **Always regularize** unless you have far more data than features
2. **Start with L2** (Ridge) — it's the safest default
3. **Use L1** when you suspect many features are irrelevant
4. **Cross-validate alpha** — don't guess
5. **Combine methods**: Dropout + weight decay + early stopping together
6. **Monitor train/val gap**: If gap is large, increase regularization

## Further Reading

- ESL Chapters 3 and 7 are the definitive treatment
- The dropout paper (Srivastava et al., 2014) is foundational for deep learning
- Yao et al. (2007) proved the equivalence between early stopping and L2 regularization
- For Bayesian perspective: L2 is a Gaussian prior on weights, L1 is a Laplace prior
