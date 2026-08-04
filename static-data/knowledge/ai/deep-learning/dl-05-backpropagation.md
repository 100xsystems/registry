---
slug: dl-05-backpropagation
title: "Backpropagation"
description: "The algorithm that makes deep learning possible — efficiently computing gradients through arbitrary computation graphs."
order: 5
tags:
  - deep-learning
  - backpropagation
  - gradient-computation
  - chain-rule
prerequisites:
  - dl-04-forward-propagation
  - dl-03-activation-functions
  - ml-06-gradient-descent
references:
  - title: "Learning Representations by Back-Propagating Errors (Rumelhart, Hinton, Williams, 1986)"
    url: "https://doi.org/10.1038/323533a0"
    description: "The foundational paper that popularized backpropagation"
  - title: "Calculus on Computational Graphs: Backpropagation (Colah)"
    url: "https://colah.github.io/posts/2015-08-Backprop/"
    description: "The best visual/intuitive explanation of backpropagation"
  - title: "CS231n: Backpropagation"
    url: "https://cs231n.github.io/optimization-2/"
    description: "Stanford CS231n's step-by-step derivation"
  - title: "Yes you should understand backprop (Andrej Karpathy)"
    url: "https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b"
    description: "Karpathy's argument for why every practitioner should understand backprop"
  - title: "Automatic Differentiation in Deep Learning"
    url: "https://arxiv.org/abs/1703.09734"
    description: "Baydin et al.'s survey of autodiff methods used in modern frameworks"
knowledge_refs:
  - dl-04-forward-propagation
  - dl-03-activation-functions
  - dl-06-loss-functions
---

# Backpropagation

Backpropagation is the algorithm that computes gradients of the loss function with respect to every parameter in the network. It's the reason deep learning works — without it, training networks with millions of parameters would be intractable.

## The Core Idea

Backpropagation is simply the **chain rule** applied systematically through the computation graph:

$$\frac{\partial \mathcal{L}}{\partial w} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial \mathbf{z}^{(L)}} \cdot \frac{\partial \mathbf{z}^{(L)}}{\partial \mathbf{h}^{(L-1)}} \cdot \frac{\partial \mathbf{h}^{(L-1)}}{\partial \mathbf{z}^{(L-1)}} \cdots \frac{\partial \mathbf{z}^{(1)}}{\partial w}$$

The key insight: compute gradients **backward** from the loss to the parameters, reusing intermediate results.

## Step by Step

Consider a 2-layer network:
$$\mathbf{h} = \text{ReLU}(W_1 \mathbf{x} + \mathbf{b}_1)$$
$$\hat{y} = W_2 \mathbf{h} + \mathbf{b}_2$$
$$\mathcal{L} = \frac{1}{2}(\hat{y} - y)^2$$

**Forward pass** (already done — we have all intermediate values).

**Backward pass** (compute gradients):

**Step 1**: Gradient of loss w.r.t. output:
$$\frac{\partial \mathcal{L}}{\partial \hat{y}} = \hat{y} - y$$

**Step 2**: Gradient of loss w.r.t. $W_2$:
$$\frac{\partial \mathcal{L}}{\partial W_2} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \cdot \mathbf{h}^T = (\hat{y} - y) \mathbf{h}^T$$

**Step 3**: Gradient of loss w.r.t. $\mathbf{h}$:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{h}} = W_2^T \cdot \frac{\partial \mathcal{L}}{\partial \hat{y}}$$

**Step 4**: Gradient through ReLU:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(1)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{h}} \odot \mathbb{1}[\mathbf{z}^{(1)} > 0]$$

(ReLU gradient is 0 where $z \leq 0$, 1 where $z > 0$)

**Step 5**: Gradient of loss w.r.t. $W_1$:
$$\frac{\partial \mathcal{L}}{\partial W_1} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(1)}} \cdot \mathbf{x}^T$$

## Implementation from Scratch

```python
import numpy as np

def forward(x, params):
    W1, b1, W2, b2 = params
    z1 = x @ W1 + b1
    a1 = np.maximum(0, z1)        # ReLU
    z2 = a1 @ W2 + b2
    return z2, (x, z1, a1)        # return intermediates for backward

def backward(dy, params, intermediates):
    x, z1, a1 = intermediates
    W1, b1, W2, b2 = params
    
    dW2 = a1.T @ dy                # gradient for W2
    db2 = dy.sum(axis=0)           # gradient for b2
    
    da1 = dy @ W2.T                # gradient through W2
    dz1 = da1 * (z1 > 0)           # gradient through ReLU
    
    dW1 = x.T @ dz1                # gradient for W1
    db1 = dz1.sum(axis=0)          # gradient for b1
    
    return [dW1, db1, dW2, db2]
```

## PyTorch's Autograd

PyTorch computes backpropagation automatically via **autograd**:

```python
import torch
import torch.nn as nn

# Forward pass builds computation graph automatically
x = torch.randn(32, 784, requires_grad=False)
target = torch.randint(0, 10, (32,))

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

output = model(x)           # forward pass
loss = nn.CrossEntropyLoss()(output, target)  # compute loss

# Backward pass — computes all gradients automatically
loss.backward()             # this is backpropagation!

# Check gradients
for name, param in model.named_parameters():
    print(f"{name}: grad shape={param.grad.shape}, mean={param.grad.mean():.6f}")
```

**What `loss.backward()` does:**
1. Traverses the computation graph in reverse
2. Applies chain rule at each node
3. Stores gradients in `.grad` attributes
4. Accumulates gradients (call `.zero_grad()` before each backward pass)

## The Vanishing Gradient Problem

As gradients flow backward through many layers, they can become exponentially small:

$$\frac{\partial \mathcal{L}}{\partial W^{(1)}} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \prod_{l=1}^{L} \frac{\partial \mathbf{h}^{(l)}}{\partial \mathbf{h}^{(l-1)}}$$

If each factor is $< 1$ (e.g., sigmoid derivative max = 0.25), the product shrinks exponentially.

**Consequences:**
- Early layers learn very slowly or not at all
- Deep networks are hard to train without careful initialization
- Gradient-based optimization stalls

**Solutions:**
- **ReLU activation**: Gradient is 1 for positive inputs (no shrinking)
- **Skip connections**: Provide gradient "highways" (ResNet)
- **Batch normalization**: Stabilizes gradient magnitudes
- **Better initialization**: He, Xavier, or LSUV initialization
- **LSTM/GRU**: Special gating mechanisms for RNNs

## The Exploding Gradient Problem

The opposite: gradients become exponentially large:

$$\frac{\partial \mathcal{L}}{\partial W^{(1)}} \to \infty$$

**Consequences:**
- Weights receive huge updates
- Loss becomes NaN
- Training diverges

**Solutions:**
- **Gradient clipping**: Cap gradient norm at a maximum value
- **Weight initialization**: Prevent large initial activations
- **Batch normalization**: Bounds activations
- **Careful learning rate**: Lower lr reduces update magnitude

```python
# Gradient clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

## Why Backpropagation is Efficient

For a network with $P$ parameters:
- **Naive**: Compute $\frac{\partial \mathcal{L}}{\partial w_i}$ independently for each parameter → $O(P \times \text{forward passes})$
- **Backpropagation**: Compute all gradients in one forward + one backward pass → $O(\text{forward pass})$

Backpropagation achieves this by **reusing intermediate results**. Each gradient computation uses results already computed for later layers.

## Numerical Gradient Checking

Verify your backpropagation implementation by comparing with numerical gradients:

```python
def numerical_gradient(f, x, eps=1e-5):
    grad = np.zeros_like(x)
    for i in range(x.size):
        old_val = x.flat[i]
        x.flat[i] = old_val + eps
        fxh1 = f(x)
        x.flat[i] = old_val - eps
        fxh2 = f(x)
        grad.flat[i] = (fxh1 - fxh2) / (2 * eps)
        x.flat[i] = old_val
    return grad

# Compare: analytical vs numerical
# Should be very close (< 1e-5 difference)
```

**Never skip this check** when implementing backpropagation from scratch. Most bugs manifest as slightly wrong gradients.

## Practical Tips

1. **Always use `.zero_grad()`** before each backward pass — gradients accumulate by default
2. **Monitor gradient norms** — use TensorBoard or wandb
3. **Gradient clipping** prevents explosion — especially important for RNNs
4. **Use `torch.autograd.gradcheck`** for verifying custom backward functions
5. **Mixed precision** can reduce memory for backward pass but requires careful handling

## What's Next

With forward and backward passes understood, the next lesson covers **loss functions** — the objective that determines what "good" means for your network.

## Further Reading

- Rumelhart, Hinton & Williams (1986) is one of the most cited papers in ML history
- Colah's visual explanation is the best intuitive introduction
- Karpathy's blog post makes a compelling case for understanding backprop deeply
- Baydin et al.'s survey covers the autodiff methods used in PyTorch and TensorFlow
