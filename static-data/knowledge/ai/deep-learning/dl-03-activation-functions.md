---
slug: dl-03-activation-functions
title: "Activation Functions"
description: "The non-linearities that make deep learning possible — ReLU, GELU, SiLU, and the trade-offs between them."
order: 3
tags:
  - deep-learning
  - activation-functions
  - relu
  - gelu
prerequisites:
  - dl-02-perceptron-and-linear-units
  - dl-01-what-is-deep-learning
references:
  - title: "Relu: The simplest activation function for deep learning"
    url: "https://www.wikipedia.org/wiki/Rectifier_(neural_networks)"
    description: "Wikipedia's comprehensive treatment of ReLU and its variants"
  - title: "Gaussian Error Linear Units (GELUs)"
    url: "https://arxiv.org/abs/1606.08415"
    description: "Hendrycks & Gimpel's GELU paper — now standard in transformers"
  - title: "Searching for Activation Functions (Swish)"
    url: "https://arxiv.org/abs/1710.05941"
    description: "Google Brain's automated search for activation functions — found Swish"
  - title: "A Comprehensive Guide to ReLU"
    url: "https://www.analyticsvidhya.com/blog/2021/04/activation-functions-and-their-derivatives-a-deep-dive-into-the-heart-of-neural-networks/"
    description: "Practical guide covering all major activation functions"
  - title: "Neural Network Non-linearities: A Survey"
    url: "https://arxiv.org/abs/2104.09487"
    description: "Comprehensive survey of activation functions and their properties"
knowledge_refs:
  - dl-02-perceptron-and-linear-units
  - dl-06-loss-functions
  - dl-05-backpropagation
---

# Activation Functions

Activation functions introduce **non-linearity** into neural networks. Without them, a deep network is just one giant linear transformation — depth would be meaningless. Choosing the right activation function can significantly impact training speed and final performance.

## Why Non-Linearity Matters

Stacking linear layers:
$$\mathbf{y} = W_3(W_2(W_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2) + \mathbf{b}_3$$

This simplifies to $\mathbf{y} = W'\mathbf{x} + \mathbf{b}'$ — a single linear transformation. No matter how many layers you stack, the result is always linear.

With activation functions:
$$\mathbf{y} = f(W_3 \cdot f(W_2 \cdot f(W_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2) + \mathbf{b}_3)$$

Now the network can learn arbitrarily complex, non-linear mappings.

## Sigmoid

$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

- Output range: (0, 1) — interpretable as probability
- Smooth, differentiable everywhere
- **Problem**: Vanishing gradients for large |x| (derivative approaches 0)
- **Problem**: Outputs not zero-centered (shifts gradients)

```python
torch.sigmoid(x)  # rarely used in hidden layers, still used in output layer for binary classification
```

## Tanh

$$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} = 2\sigma(2x) - 1$$

- Output range: (-1, 1) — zero-centered
- Stronger gradients than sigmoid (derivative max = 1 vs 0.25)
- **Problem**: Still saturates for large |x|
- **Use case**: RNNs (before LSTM/GRU made this obsolete)

```python
torch.tanh(x)
```

## ReLU (Rectified Linear Unit)

$$\text{ReLU}(x) = \max(0, x)$$

The activation that launched deep learning:

- **Computationally efficient**: Just a threshold operation
- **Sparse activation**: Many neurons output exactly 0
- **No vanishing gradient**: Gradient is either 0 or 1
- **Problem**: "Dying ReLU" — neurons that output 0 never recover (gradient = 0)
- **Problem**: Not zero-centered

```python
torch.relu(x)
nn.ReLU()  # as a layer
```

**Why ReLU works so well**: It's piecewise linear, so gradients flow freely through the active (positive) region. The sparsity it creates acts as implicit regularization.

## Leaky ReLU and Parametric ReLU (PReLU)

Fix the dying ReLU problem by allowing small negative values:

$$\text{LeakyReLU}(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha x & \text{if } x \leq 0 \end{cases}$$

- **Leaky ReLU**: $\alpha = 0.01$ (fixed)
- **PReLU**: $\alpha$ is a learnable parameter
- **ELU**: Smooth version, $f(x) = x$ if $x > 0$, $\alpha(e^x - 1)$ if $x \leq 0$

```python
nn.LeakyReLU(negative_slope=0.01)
nn.PReLU()  # learnable slope
```

## GELU (Gaussian Error Linear Unit)

$$\text{GELU}(x) = x \cdot \Phi(x) \approx 0.5x(1 + \tanh[\sqrt{2/\pi}(x + 0.044715x^3)])$$

The modern default for **transformers** (BERT, GPT, ViT):
- Smooth, non-monotonic
- Gates based on input magnitude (similar to dropout + ReLU)
- Better performance than ReLU in transformers
- Slightly more expensive to compute

```python
nn.GELU()  # default in most transformer implementations
```

## SiLU / Swish

$$\text{Swish}(x) = x \cdot \sigma(x)$$

Found by Google Brain's automated search for activation functions:
- Very similar to GELU
- Smooth, non-monotonic
- Self-gating (uses the input to gate itself)
- Found by searching over combinations of existing functions

```python
nn.SiLU()  # same as Swish
```

## Comparison

| Function | Formula | Range | Pros | Cons |
|---|---|---|---|---|
| Sigmoid | $\sigma(x)$ | (0, 1) | Interpretable | Vanishing gradient |
| Tanh | $\tanh(x)$ | (-1, 1) | Zero-centered | Saturates |
| ReLU | $\max(0, x)$ | [0, ∞) | Fast, sparse | Dying neurons |
| Leaky ReLU | $\max(\alpha x, x)$ | (-∞, ∞) | No dying neurons | Extra hyperparameter |
| GELU | $x \Phi(x)$ | (-0.17, ∞) | Best for transformers | Slower |
| SiLU | $x \sigma(x)$ | (-0.28, ∞) | Smooth, self-gating | Slower |

## The Die Hard ReLU vs. GELU Debate

**ReLU** is still used in:
- Computer vision CNNs (ResNet, EfficientNet)
- Lightweight models (MobileNet)
- When inference speed matters (ReLU is fastest)

**GELU/SiLU** is used in:
- Transformers (BERT, GPT, ViT)
- When training speed isn't critical
- Large language models (LLaMA uses SiLU)

**Rule of thumb**: Use GELU for transformers, ReLU for CNNs, experiment for everything else.

## Output Layer Activations

The output layer activation depends on the task:

| Task | Output Activation | Loss Function |
|---|---|---|
| Binary classification | Sigmoid | Binary Cross-Entropy |
| Multi-class classification | Softmax | Categorical Cross-Entropy |
| Regression | None (linear) | MSE / MAE / Huber |
| Multi-label classification | Sigmoid per output | Binary Cross-Entropy |

```python
# Binary classification
model = nn.Sequential(nn.Linear(100, 1), nn.Sigmoid())
loss = nn.BCELoss()

# Multi-class classification
model = nn.Sequential(nn.Linear(100, 10))  # no softmax — handled by loss
loss = nn.CrossEntropyLoss()  # combines LogSoftmax + NLLLoss

# Regression
model = nn.Sequential(nn.Linear(100, 1))  # no activation
loss = nn.MSELoss()
```

## Practical Guidelines

1. **Default to ReLU** for CNNs and simple architectures
2. **Default to GELU** for transformers and attention-based models
3. **Never use sigmoid/tanh in hidden layers** (vanishing gradients)
4. **Use sigmoid in output** only for binary classification
5. **Try SiLU** if GELU doesn't work — they're very similar
6. **Monitor dying neurons**: If many ReLU neurons output 0, try Leaky ReLU

## Further Reading

- Hendrycks & Gimpel (2016) introduced GELU — now ubiquitous in NLP
- Ramachandran et al. (2017) discovered Swish via automated search
- The "dying ReLU" problem is analyzed in detail in Lu et al. (2019)
- For extreme environments: quantized networks may need specialized activations
