---
slug: dl-08-pytorch-tensors-and-autograd
title: "PyTorch: Tensors & Autograd"
description: "The two pillars of PyTorch — tensors for computation, autograd for automatic differentiation."
order: 8
tags:
  - deep-learning
  - pytorch
  - tensors
  - autograd
prerequisites:
  - dl-04-forward-propagation
  - dl-05-backpropagation
  - dl-07-optimizers
references:
  - title: "PyTorch Official Tutorials"
    url: "https://pytorch.org/tutorials/"
    description: "The official PyTorch learning resources — start here"
  - title: "PyTorch 60 Minute Blitz"
    url: "https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html"
    description: "The official quick-start tutorial covering tensors, autograd, and nn"
  - title: "From NumPy to PyTorch"
    url: "https://pytorch.org/tutorials/beginner/examples_tensor/two_tensor_examples.html"
    description: "Side-by-side comparison of NumPy and PyTorch operations"
  - title: "Understanding PyTorch Autograd"
    url: "https://pytorch.org/docs/stable/autograd.html"
    description: "Official autograd documentation with computation graph details"
  - title: "PyTorch Internals (Edward Yang)"
    url: "http://blog.ezyang.com/2019/05/pytorch-internals/"
    description: "Deep dive into PyTorch's internal architecture"
knowledge_refs:
  - dl-04-forward-propagation
  - dl-05-backpropagation
  - dl-09-building-an-mlp-in-pytorch
---

# PyTorch: Tensors & Autograd

PyTorch is the dominant framework for deep learning research. Two concepts underpin everything: **tensors** (multi-dimensional arrays with GPU support) and **autograd** (automatic differentiation).

## Tensors: GPU-Accelerated Arrays

A tensor is a multi-dimensional array — like NumPy's ndarray but with GPU support and automatic differentiation.

### Creating Tensors

```python
import torch

# From Python lists
x = torch.tensor([1.0, 2.0, 3.0])

# From NumPy arrays
import numpy as np
x_np = np.array([1.0, 2.0, 3.0])
x = torch.from_numpy(x_np)

# Random initialization
x = torch.randn(3, 4)           # standard normal
x = torch.rand(3, 4)            # uniform [0, 1)
x = torch.zeros(3, 4)           # zeros
x = torch.ones(3, 4)            # ones
x = torch.empty(3, 4)           # uninitialized (fast)

# With specific dtype
x = torch.float32               # default
x = torch.float16               # half precision
x = torch.int64
x = torch.bool
```

### Tensor Operations

PyTorch mirrors NumPy's API closely:

```python
# Element-wise operations
a + b          # addition
a * b          # multiplication
a ** 2         # power
torch.exp(a)   # exponential
torch.log(a)   # logarithm
torch.sqrt(a)  # square root

# Matrix operations
a @ b          # matrix multiplication
a.matmul(b)    # same
torch.mm(a, b) # same

# Reduction
a.mean()
a.sum()
a.max(dim=0)   # max along dimension 0

# Reshaping
a.view(3, 4)   # reshape (contiguous only)
a.reshape(3, 4) # reshape (may copy)
a.unsqueeze(0)  # add dimension
a.squeeze()     # remove size-1 dimensions
a.transpose(0, 1) # swap dimensions
```

### GPU Acceleration

```python
# Move to GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x = x.to(device)
# or
x = x.cuda()
x = x.cpu()

# Operations between CPU and GPU tensors fail
x_gpu = torch.randn(3, 4).cuda()
x_cpu = torch.randn(3, 4)
# x_gpu + x_cpu  # RuntimeError!

# Always keep tensors on the same device
model = model.to(device)
for batch in dataloader:
    batch = batch.to(device)
    output = model(batch)
```

### Tensor Memory

```python
# Memory is shared (not copied) unless explicitly cloned
a = torch.randn(3, 4)
b = a           # b points to same memory
b[0, 0] = 99   # a[0, 0] is also 99!

c = a.clone()   # c is a separate copy
c[0, 0] = 0     # a is unchanged

# Check memory usage
print(f"GPU memory: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
```

## Autograd: Automatic Differentiation

Autograd records operations on tensors with `requires_grad=True` to build a computation graph, then computes gradients automatically via backpropagation.

### Basic Usage

```python
# requires_grad=True tells PyTorch to track operations
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1  # y = x² + 3x + 1

# Backward pass computes dy/dx automatically
y.backward()

# Gradient: dy/dx = 2x + 3 = 7 at x=2
print(x.grad)  # tensor(7.)
```

### Gradients in Neural Networks

```python
x = torch.randn(32, 10)  # input
W = torch.randn(10, 5, requires_grad=True)  # weights

# Forward
z = x @ W
loss = z.sum()

# Backward
loss.backward()

# W.grad contains d(loss)/dW
print(W.grad.shape)  # (10, 5)
```

### Gradient Accumulation

Gradients **accumulate** by default — each `.backward()` adds to `.grad`:

```python
for i in range(3):
    loss = model(x).sum()
    loss.backward()
    # W.grad is the SUM of gradients from all 3 iterations!

# Always zero gradients before backward
optimizer.zero_grad()  # or
model.zero_grad()
```

### Detaching Gradients

```python
# detach() removes from computation graph
x_detached = x.detach()  # same data, no grad tracking

# Use when:
# 1. You want to use a tensor's value without tracking gradients
# 2. You're mixing frozen and trainable parts
# 3. You want to log values without affecting computation
```

### Gradient Context Managers

```python
# torch.no_grad(): Disables gradient computation (faster, less memory)
with torch.no_grad():
    output = model(x)  # no gradients tracked
    # Use for inference, evaluation, logging

# torch.enable_grad(): Re-enable inside no_grad block
with torch.no_grad():
    with torch.enable_grad():
        output = model(x)  # gradients tracked again

# torch.inference_mode(): Even faster than no_grad
with torch.inference_mode():
    output = model(x)
```

### Custom Backward Functions

```python
class MyReLU(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x)
        return x.clamp(min=0)
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        grad_input = grad_output.clone()
        grad_input[x < 0] = 0
        return grad_input

# Use: MyReLU.apply(x)
```

## Common Patterns

### Training Loop

```python
model.train()
for epoch in range(num_epochs):
    for batch in dataloader:
        optimizer.zero_grad()           # 1. Zero gradients
        
        output = model(batch.x)         # 2. Forward pass
        loss = criterion(output, batch.y) # 3. Compute loss
        
        loss.backward()                 # 4. Backward pass
        optimizer.step()                # 5. Update weights
```

### Inference

```python
model.eval()
with torch.no_grad():  # or torch.inference_mode()
    for batch in test_dataloader:
        output = model(batch.x)
        predictions = output.argmax(dim=-1)
```

### Gradient Clipping

```python
# Clip by norm
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# Clip by value
torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=0.5)
```

## Debugging PyTorch Code

```python
# Check tensor shapes
print(f"Shape: {x.shape}, dtype: {x.dtype}, device: {x.device}")

# Check for NaN/Inf
assert torch.isfinite(x).all(), "Tensor contains NaN or Inf!"

# Check gradient flow
for name, p in model.named_parameters():
    if p.grad is not None:
        print(f"{name}: grad norm = {p.grad.norm():.4f}")

# Common errors:
# - Shape mismatch: most common error in deep learning
# - CPU/GPU mismatch: tensors must be on same device
# - requires_grad mismatch: can't backprop through detached tensors
```

## Further Reading

- PyTorch tutorials are the best starting point
- Edward Yang's internals post explains the C++/Python architecture
- For JAX (an alternative): think of it as NumPy + autograd + XLA
- For TensorFlow: PyTorch is now dominant in research; TF in some production
