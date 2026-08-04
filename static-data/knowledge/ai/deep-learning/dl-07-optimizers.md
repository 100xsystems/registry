---
slug: dl-07-optimizers
title: "Optimizers for Deep Learning"
description: "From SGD to AdamW — the optimizers that make training deep networks feasible."
order: 7
tags:
  - deep-learning
  - optimization
  - adam
  - sgd
  - adamw
prerequisites:
  - dl-05-backpropagation
  - dl-06-loss-functions
  - ml-06-gradient-descent
references:
  - title: "Adam: A Method for Stochastic Optimization"
    url: "https://arxiv.org/abs/1412.6980"
    description: "The original Adam paper by Kingma & Ba"
  - title: "Decoupled Weight Decay Regularization (AdamW)"
    url: "https://arxiv.org/abs/1711.05101"
    description: "Loshchilov & Hutter's AdamW — the standard for modern training"
  - title: "On the Convergence of Adam and Beyond"
    url: "https://openreview.net/forum?id=ryQu7f-RZ"
    description: "Reddi et al. showing Adam can diverge — motivating AMSGrad"
  - title: "A Method for Stochastic Optimization: Visual Guide"
    url: "https://ruder.io/optimizing-gradient-descent/"
    description: "Sebastian Ruder's comprehensive survey of all optimizers"
  - title: "SGDR: Stochastic Gradient Descent with Warm Restarts"
    url: "https://arxiv.org/abs/1608.03983"
    description: "Loshchilov & Hutter's cosine annealing with warm restarts schedule"
knowledge_refs:
  - dl-05-backpropagation
  - ml-06-gradient-descent
  - dl-19-training-at-scale
---

# Optimizers for Deep Learning

After computing gradients via backpropagation, we need to update the weights. The optimizer determines how gradients are translated into parameter updates — and the choice matters enormously.

## SGD with Momentum

The foundation — adding velocity to basic gradient descent:

$$v_t = \beta v_{t-1} + g_t$$
$$\theta_{t+1} = \theta_t - \eta v_t$$

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
```

**Why momentum helps**: Accelerates convergence in consistent gradient directions, dampens oscillations in ravines. $\beta = 0.9$ is standard.

**SGD with momentum + weight decay** remains competitive for computer vision and is often the best choice for ResNet-style architectures.

## Adaptive Methods

These maintain per-parameter learning rates that adapt based on gradient history:

### Adam

Combines momentum (first moment) with RMSProp (second moment):

```python
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, betas=(0.9, 0.999))
```

**Default hyperparameters**: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. Works well out of the box.

### AdamW (Adam with Decoupled Weight Decay)

The current gold standard for training deep networks, especially transformers:

```python
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
```

**The key difference from Adam**: Weight decay is applied directly to weights, not through the gradient. This fixes a subtle bug in Adam's L2 regularization.

**When to use AdamW**: Transformers, language models, diffusion models, any architecture where weight decay matters.

### LAMB (Layer-wise Adaptive Moments)

Scales learning rate per layer based on weight and gradient magnitudes. Enables large-batch training:

```python
optimizer = torch.optim.LAMB(model.parameters(), lr=1e-3)
```

**Use case**: Distributed training with very large batch sizes.

## Learning Rate Schedules

Static learning rates rarely work best. Schedules adapt the rate during training:

### Cosine Annealing

$$\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})\left(1 + \cos\left(\frac{\pi t}{T}\right)\right)$$

```python
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)
```

### Warmup + Cosine

Start with a low learning rate, warm up linearly, then cosine anneal:
```python
from torch.optim.lr_scheduler import LambdaLR

def warmup_cosine(step, warmup_steps=1000, total_steps=10000):
    if step < warmup_steps:
        return step / warmup_steps
    progress = (step - warmup_steps) / (total_steps - warmup_steps)
    return 0.5 * (1 + math.cos(math.pi * progress))

scheduler = LambdaLR(optimizer, lr_lambda=warmup_cosine)
```

**Why warmup helps**: Prevents large initial updates from destabilizing training, especially important for transformers.

### Step Decay

```python
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)
# Learning rate multiplies by 0.1 every 30 epochs
```

### One Cycle Policy

```python
scheduler = torch.optim.lr_scheduler.OneCycleLR(
    optimizer, max_lr=0.01, total_steps=total_training_steps
)
```

Warm up to max_lr, then anneal. Fast convergence.

## Practical Comparison

| Optimizer | Speed | Generalization | Memory | Best For |
|---|---|---|---|---|
| SGD+Momentum | Slow | Excellent | Low | Computer vision |
| Adam | Fast | Good | High | Default / exploration |
| AdamW | Fast | Excellent | High | Transformers, LLMs |
| LAMB | Fast | Good | Very high | Large-batch training |

## The Generalization Gap

Adam converges faster but sometimes generalizes worse than SGD:

- **SGD** finds flatter minima → better generalization
- **Adam** can find sharper minima → worse generalization on test data

**Mitigation**: Use AdamW with proper weight decay, lower learning rates, and cosine schedules.

## Hyperparameter Sensitivity

**Learning rate** is the single most important hyperparameter:
- Too high: Training diverges, loss oscillates
- Too low: Training is slow, may get stuck
- Just right: Fast convergence, good generalization

**Learning rate finder**:
```python
lrs, losses = [], []
for lr in np.logspace(-7, 0, 100):
    optimizer = Adam(model.parameters(), lr=lr)
    loss = train_one_batch(model, batch, optimizer)
    lrs.append(lr)
    losses.append(loss)

# Plot: optimal lr is where loss decreases fastest
plt.semilogx(lrs, losses)
```

## Mixed Precision Training

Use FP16 for forward/backward passes, FP32 for weight updates — 2x less memory, 2-3x faster:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
for batch in dataloader:
    optimizer.zero_grad()
    
    with autocast():  # FP16 forward pass
        output = model(batch)
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()  # FP16 backward pass
    scaler.step(optimizer)  # FP32 weight update
    scaler.update()
```

**When to use**: Almost always on modern GPUs. Reduces memory usage significantly.

## Gradient Accumulation

For larger effective batch sizes when GPU memory is limited:
```python
accumulation_steps = 4
for i, batch in enumerate(dataloader):
    loss = criterion(model(batch), target) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

## Practical Guidelines

1. **Start with AdamW** for any new project — it works well out of the box
2. **Use cosine annealing with warmup** — it's the default for transformers
3. **Try SGD + momentum for vision** — it often generalizes better
4. **Always use mixed precision** on modern GPUs
5. **Monitor learning rate** — log it alongside loss
6. **Learning rate is more important than optimizer choice**

## Further Reading

- Kingma & Ba (2014) introduced Adam — one of the most cited ML papers
- Loshchilov & Hutter (2017) fixed Adam's weight decay bug — now standard practice
- Ruder's survey is the definitive reference for understanding all optimizers
- For learning rate schedules, SGDR (cosine with warm restarts) is a strong default
