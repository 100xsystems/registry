---
slug: dl-04-forward-propagation
title: "Forward Propagation"
description: "How data flows through a neural network — from raw input to final prediction, one layer at a time."
order: 4
tags:
  - deep-learning
  - forward-pass
  - computation-graph
prerequisites:
  - dl-03-activation-functions
  - dl-02-perceptron-and-linear-units
references:
  - title: "Deep Learning Book: Chapter 6 — Deep Feedforward Networks"
    url: "https://www.deeplearningbook.org/contents/mlp.html"
    description: "Goodfellow et al.'s treatment of forward propagation through deep networks"
  - title: "Computational Graphs and Automatic Differentiation"
    url: "https://colah.github.io/posts/2015-08-Backprop/"
    description: "Colah's visual explanation of computation graphs and backpropagation"
  - title: "PyTorch: Forward Pass Tutorial"
    url: "https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html"
    description: "Official PyTorch tutorial on building and running forward passes"
  - title: "CS231n: Neural Network Forward Pass"
    url: "https://cs231n.github.io/neural-networks-1/"
    description: "Stanford CS231n lecture notes on neural network computation"
  - title: "Automatic Differentiation in Machine Learning: A Survey"
    url: "https://arxiv.org/abs/1526.05267"
    description: "Comprehensive survey of how forward and backward passes relate"
knowledge_refs:
  - dl-03-activation-functions
  - dl-05-backpropagation
  - dl-06-loss-functions
---

# Forward Propagation

Forward propagation (or the forward pass) is the process of computing a neural network's output from its input. Data flows through every layer sequentially, with each layer transforming the data until a prediction emerges.

## The Forward Pass: Layer by Layer

Given input $\mathbf{x}$ and a network with $L$ layers:

$$\mathbf{h}^{(0)} = \mathbf{x}$$
$$\mathbf{z}^{(l)} = W^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}$$
$$\mathbf{h}^{(l)} = f^{(l)}(\mathbf{z}^{(l)})$$

where $W^{(l)}$ and $\mathbf{b}^{(l)}$ are the weights and biases of layer $l$, and $f^{(l)}$ is the activation function.

**The prediction** is $\hat{y} = \mathbf{h}^{(L)}$ (or a transformation of it).

## A Concrete Example

A 3-layer network for classifying 28×28 images (784 pixels) into 10 digits:

```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)   # Layer 1
        self.fc2 = nn.Linear(256, 128)    # Layer 2
        self.fc3 = nn.Linear(128, 10)     # Output layer
    
    def forward(self, x):
        x = x.view(-1, 784)              # Flatten image
        x = torch.relu(self.fc1(x))       # Layer 1: Linear + ReLU
        x = torch.relu(self.fc2(x))       # Layer 2: Linear + ReLU
        x = self.fc3(x)                   # Output: Linear (no activation)
        return x

model = SimpleNet()
x = torch.randn(32, 1, 28, 28)  # batch of 32 images
output = model(x)  # shape: (32, 10) — logits for 10 classes
```

## Tensor Shapes Through the Network

Tracking shapes is essential for debugging:

```
Input:       (32, 1, 28, 28)    — 32 images, 1 channel, 28x28 pixels
Flatten:     (32, 784)           — 32 vectors of 784 features
fc1 + ReLU:  (32, 256)           — 32 vectors of 256 features
fc2 + ReLU:  (32, 128)           — 32 vectors of 128 features
fc3:         (32, 10)            — 32 vectors of 10 logits
```

**Shape mismatches** are the most common error in deep learning. Always check shapes at each layer.

## Batch Processing

Neural networks process data in **batches** for efficiency:
- GPU parallelism: Process 32, 64, 128... samples simultaneously
- Better gradient estimates: Batch gradients average over multiple samples
- Memory efficiency: Fixed memory regardless of dataset size

```python
# Single sample
x = torch.randn(1, 784)        # shape: (1, 784)
y = model(x)                   # shape: (1, 10)

# Batch
x = torch.randn(32, 784)       # shape: (32, 784)
y = model(x)                   # shape: (32, 10)

# The same computation runs for all 32 samples in parallel
```

## The Computation Graph

Every forward pass builds a **computation graph** — a directed acyclic graph (DAG) of operations:

```
x → [Linear: W₁x + b₁] → [ReLU] → [Linear: W₂·] → [ReLU] → [Linear: W₃·] → ŷ
```

This graph is critical because:
1. **Forward pass**: Computes the output (and stores intermediate values)
2. **Backward pass**: Traverses the graph in reverse to compute gradients
3. **Optimization**: Uses gradients to update parameters

PyTorch builds this graph dynamically (eager mode), enabling flexible architectures.

## Forward Pass in Practice

### Without PyTorch (Manual)
```python
import numpy as np

def forward_manual(x, params):
    W1, b1, W2, b2, W3, b3 = params
    
    z1 = x @ W1 + b1
    a1 = np.maximum(0, z1)  # ReLU
    
    z2 = a1 @ W2 + b2
    a2 = np.maximum(0, z2)  # ReLU
    
    z3 = a2 @ W3 + b3  # no activation on output
    return z3
```

### With PyTorch (Automatic)
```python
# PyTorch handles everything automatically
output = model(input_tensor)

# Forward + loss in one step
output = model(x)
loss = criterion(output, target)
```

## Intermediate Values Matter

During training, we need to **save intermediate values** from the forward pass for the backward pass:

```python
# PyTorch saves these automatically
output = model(x)  # all intermediate activations are stored

# This is why GPU memory grows during training
# More layers + larger batches = more memory
```

**Memory implications:**
- A 100-layer network with batch size 64 needs to store 100 intermediate tensors
- Each tensor's shape is (batch_size, hidden_dim)
- For large models (GPT-3: 175B parameters), this requires hundreds of GB

## Activation Statistics

Monitoring activations during forward passes helps debug training:

```python
# Track activation statistics
for name, module in model.named_modules():
    if isinstance(module, nn.ReLU):
        module.register_forward_hook(lambda m, i, o, n=name: 
            print(f"{n}: mean={o.mean():.3f}, std={o.std():.3f}, dead={((o == 0).float().mean()):.1%}"))
```

**Healthy activations:**
- Mean around 0 (or slightly positive for ReLU)
- Standard deviation around 0.5-2.0
- Dead neurons (output = 0) less than 10%

**Warning signs:**
- Mean near 0 with small std → vanishing activations
- Very large values → exploding activations
- High dead neuron percentage → dying ReLU problem

## Numerical Stability

Deep networks can suffer from numerical issues during forward propagation:

**Overflow**: Very large values ($> 10^{38}$) become `inf`
**Underflow**: Very small values ($< 10^{-38}$) become 0
**NaN**: Result of `inf - inf`, `0/0`, or `sqrt(-1)`

Solutions:
```python
# Use float32 (not float64) — sufficient precision, less memory
x = x.float()

# Add epsilon to avoid division by zero
var = var + 1e-5

# Use LogSumExp for numerically stable softmax
def stable_softmax(x):
    x_max = x.max(dim=-1, keepdim=True).values
    exp_x = torch.exp(x - x_max)
    return exp_x / exp_x.sum(dim=-1, keepdim=True)
```

## Forward Pass Speed

Forward pass speed depends on:
- **Matrix multiplication size**: $O(\text{batch} \times \text{input\_dim} \times \text{output\_dim})$
- **Activation function**: ReLU is fastest (simple threshold), GELU is slower
- **Memory bandwidth**: Reading/writing large tensors is often the bottleneck
- **GPU utilization**: Larger batches → better GPU utilization

**Optimization tips:**
- Use `torch.no_grad()` during inference (disables gradient tracking)
- Use mixed precision (`torch.cuda.amp`) for faster forward passes
- Batch inference for maximum throughput

## What's Next

The forward pass computes predictions. The next lesson covers **backpropagation** — how gradients flow backward through the same computation graph to tell each weight how to change.

## Further Reading

- Goodfellow et al. Chapter 6 covers forward propagation through deep networks
- Colah's blog post beautifully connects computation graphs to backpropagation
- CS231n's neural network notes are essential for understanding the shapes and operations
- For numerical stability, see "What Every Computer Scientist Should Know About Floating-Point Arithmetic"
