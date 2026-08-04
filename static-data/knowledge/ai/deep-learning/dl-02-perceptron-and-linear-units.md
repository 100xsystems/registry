---
slug: dl-02-perceptron-and-linear-units
title: "The Perceptron & Linear Units"
description: "Where deep learning began — the simplest neural unit and why linear models alone aren't enough."
order: 2
tags:
  - deep-learning
  - perceptron
  - linear-units
  - history
prerequisites:
  - dl-01-what-is-deep-learning
  - ml-07-logistic-regression
references:
  - title: "The Perceptron: A Probabilistic Model (Rosenblatt, 1958)"
    url: "https://doi.org/10.1007/BF02258918"
    description: "Frank Rosenblatt's original perceptron paper — the birth of neural networks"
  - title: "Perceptrons (Minsky & Papert, 1969)"
    url: "https://mitpress.mit.edu/9780262534772/perceptrons/"
    description: "The book that identified the limitations of single-layer perceptrons"
  - title: "3Blue1Brown: But what is a neural network?"
    url: "https://www.youtube.com/watch?v=aircAruvnKk"
    description: "Visual explanation of single neurons and networks"
  - title: "Single-Layer Neural Networks and Gradient Descent"
    url: "https://sebastianraschka.com/Articles/2015_singlelayer_neurons.html"
    description: "Sebastian Raschka's mathematical treatment of single-layer networks"
  - title: "The Perceptron: A Comprehensive Tutorial"
    url: "https://www.dipf.de/en/forschung/schwerpunkte/datenwissenschaft-und-bildung/ki-werkstatt/kipedia/detail/perceptron"
    description: "Historical context and mathematical foundations"
knowledge_refs:
  - dl-01-what-is-deep-learning
  - ml-07-logistic-regression
  - ml-05-linear-regression
---

# The Perceptron & Linear Units

The perceptron is the simplest neural network — a single computational unit that inspired decades of research and eventually led to modern deep learning.

## The Original Perceptron (1958)

Frank Rosenblatt's perceptron was a binary classifier that mimics a biological neuron:

1. Receives weighted inputs: $z = \sum_{i=1}^{n} w_i x_i + b$
2. Applies a step function: $y = \begin{cases} 1 & \text{if } z \geq 0 \\ 0 & \text{if } z < 0 \end{cases}$

```python
import numpy as np

def perceptron_predict(x, weights, bias):
    z = np.dot(weights, x) + bias
    return 1 if z >= 0 else 0
```

**Learning rule** (Rosenblatt's rule):
- If prediction is correct: do nothing
- If prediction is 0 but should be 1: increase weights for active features
- If prediction is 1 but should be 0: decrease weights for active features

$$w_i \leftarrow w_i + \eta (y_{\text{true}} - y_{\text{pred}}) x_i$$

This is essentially a simplified version of gradient descent.

## The Minsky Critique (1969)

Marvin Minsky and Seymour Papert proved that a single perceptron **cannot learn XOR** — or any non-linearly separable function. This "killed" neural network research for over a decade (the first "AI winter").

**The XOR problem:**
| x₁ | x₂ | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No single line can separate the 0s from the 1s. But a **two-layer network** can — it just needs depth.

## Linear Units

A linear unit computes a weighted sum of inputs:

$$y = \mathbf{w}^T \mathbf{x} + b$$

This is exactly **linear regression** — one of the oldest statistical models. Linear units are useful but limited:
- Can only learn linear relationships
- The output is unbounded
- No non-linearity means stacking layers is pointless (composition of linear functions is linear)

### PyTorch Implementation

```python
import torch
import torch.nn as nn

# A single linear unit
linear = nn.Linear(in_features=10, out_features=1)
x = torch.randn(1, 10)  # batch of 1, 10 features
y = linear(x)  # shape: (1, 1)

print(f"Weights shape: {linear.weight.shape}")  # (1, 10)
print(f"Bias shape: {linear.bias.shape}")  # (1,)
```

## Why Linear Models Fail

Consider fitting a circle boundary in 2D:
```python
# Data: points inside circle → class 1, outside → class 0
# No straight line can separate them!
```

But with just one hidden layer:
```python
# Layer 1: creates features that "unfold" the circle
# Layer 2: draws a linear boundary on the unfolded features
# Result: perfectly separates the classes
```

This is the power of **depth + non-linearity**. The hidden layer learns new representations that make the problem linearly separable.

## From Perceptron to Multi-Layer Network

The key insight: stack multiple perceptrons and add non-linearity between layers:

```
Input → [Linear + ReLU] → [Linear + ReLU] → ... → [Linear] → Output
```

```python
model = nn.Sequential(
    nn.Linear(10, 64),    # Layer 1
    nn.ReLU(),            # Non-linearity
    nn.Linear(64, 32),    # Layer 2
    nn.ReLU(),            # Non-linearity
    nn.Linear(32, 1)      # Output
)
```

Each hidden layer creates new features. The non-linearity (ReLU) allows the network to learn curved decision boundaries. With enough layers and neurons, the network can approximate **any** function.

## The Universal Approximation Theorem

**Theorem** (Cybenko, 1989): A feedforward network with a single hidden layer containing a finite number of neurons can approximate any continuous function on compact subsets of $\mathbb{R}^n$, given appropriate weights.

**Why this isn't enough**: The theorem guarantees existence but not efficiency. A single layer might need exponentially many neurons, while a deep network can represent the same function with polynomially many. Depth provides **efficiency**, not just capability.

## Geometric Interpretation

Each linear layer performs an **affine transformation** (rotation + translation + scaling):
$$\mathbf{h} = W\mathbf{x} + \mathbf{b}$$

Each non-linearity (ReLU) "folds" the space:
$$\mathbf{h}_{\text{out}} = \max(0, \mathbf{h})$$

Stacked together: linear transforms + non-linear folds = arbitrarily complex mappings.

**Visual intuition**: Think of crumpling a piece of paper. Each ReLU layer folds the space, and the linear layers rotate/translate the folds. With enough folds, any two regions can be separated.

## Historical Impact

The perceptron's story teaches a crucial lesson in AI:
- **1958**: Rosenblatt builds the first learning machine — huge excitement
- **1969**: Minsky & Papert prove fundamental limitations — research collapses
- **1986**: Rumelhart, Hinton & Williams show backpropagation works for multi-layer networks — research revives
- **2012**: Deep networks crush all alternatives — the deep learning revolution

The lesson: **architectural innovation (depth) + algorithmic innovation (backpropagation) + computational innovation (GPUs) = breakthrough performance**.

## Practical Takeaways

1. **A single linear layer = linear regression/logistic regression** — useful baseline
2. **Depth matters**: Even a shallow 2-layer network can learn XOR
3. **Non-linearity is essential**: Without it, depth is pointless
4. **More capacity = more potential**: But also more overfitting risk
5. **Modern networks are just stacked perceptrons** with better activations and training techniques

## Further Reading

- Rosenblatt's 1958 paper is a historical artifact worth reading
- Minsky & Papert's critique was technically correct but prematurely pessimistic
- 3Blue1Brown's video series builds intuition from the ground up
- Sebastian Raschka's tutorial provides the mathematical bridge from perceptron to modern networks
