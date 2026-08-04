---
slug: ml-06-gradient-descent
title: "Gradient Descent"
description: "Master the optimization algorithm that powers nearly all of machine learning — from vanilla SGD to Adam and beyond."
order: 6
tags:
  - machine-learning
  - optimization
  - gradient-descent
  - adam
  - sgd
prerequisites:
  - ml-05-linear-regression
references:
  - title: "An Overview of Gradient Descent Optimization Algorithms"
    url: "https://ruder.io/optimizing-gradient-descent/"
    description: "Sebastian Ruder's comprehensive survey of every major gradient descent variant"
  - title: "Stanford CS231n: Optimizers"
    url: "https://cs231n.github.io/optimization-1/"
    description: "CS231n lecture notes on optimization for neural networks"
  - title: "Adam: A Method for Stochastic Optimization"
    url: "https://arxiv.org/abs/1412.6980"
    description: "The original Adam paper by Kingma and Ba"
  - title: "fast.ai: SGD from Scratch"
    url: "https://nbviewer.org/github/fastai/fastbook/blob/master/08_collab.ipynb"
    description: "Hands-on implementation of gradient descent from first principles"
  - title: "distill.pub: Why Momentum Really Works"
    url: "https://distill.pub/2017/momentum/"
    description: "Beautiful interactive visualization of momentum in gradient descent"
knowledge_refs:
  - ml-05-linear-regression
  - ml-03-the-learning-problem
  - ml-15-regularization
---

# Gradient Descent

Gradient descent is the workhorse optimization algorithm behind virtually every machine learning model. Understanding its variants, failure modes, and best practices is essential for any practitioner.

## The Core Idea

Given a loss function $J(\theta)$ that measures how wrong our predictions are, gradient descent iteratively adjusts parameters $\theta$ in the direction that reduces the loss:

$$\theta_{t+1} = \theta_t - \eta \nabla_\theta J(\theta_t)$$

where $\eta$ is the **learning rate** — the step size at each iteration. The gradient $\nabla_\theta J(\theta_t)$ points uphill, so we subtract it to move downhill.

Think of it like descending a mountain in fog: you feel the slope under your feet and take a step downhill. The steeper the slope, the bigger the step (proportional to the gradient magnitude).

## Batch, Stochastic, and Mini-Batch

The gradient can be computed over different subsets of the training data:

**Batch Gradient Descent** computes the gradient over the entire dataset:
```python
gradient = mean(gradient_of_loss_for_all_samples)
```
- ✅ Smooth, stable convergence
- ❌ Slow for large datasets (must process all data before one step)
- ❌ Can get stuck in shallow local minima

**Stochastic Gradient Descent (SGD)** computes the gradient on a single random sample:
```python
for x, y in dataloader:
    gradient = gradient_of_loss(x, y)
    params -= lr * gradient
```
- ✅ Very fast updates
- ✅ Noise can help escape local minima
- ❌ Very noisy convergence — loss oscillates wildly

**Mini-Batch SGD** is the practical compromise — compute the gradient on a batch of 32-512 samples:
```python
for batch in dataloader:
    gradient = gradient_of_loss(batch)
    params -= lr * gradient
```
This is what virtually everyone uses. The batch size is a hyperparameter that balances speed and stability.

## The Learning Rate Problem

The learning rate is the single most important hyperparameter:

- **Too high**: The optimizer overshoots minima, loss diverges or oscillates
- **Too low**: Training is painfully slow, may get stuck in suboptimal local minima
- **Just right**: Convergence is fast and stable

**Learning rate schedules** adapt the rate during training:
```python
# Step decay: halve every 30 epochs
scheduler = StepLR(optimizer, step_size=30, gamma=0.5)

# Cosine annealing: smooth decrease following a cosine curve
scheduler = CosineAnnealingLR(optimizer, T_max=100)

# Warmup + cosine: start low, warm up, then anneal
def warmup_cosine(step, warmup_steps=1000, total_steps=10000):
    if step < warmup_steps:
        return step / warmup_steps
    return 0.5 * (1 + math.cos(math.pi * (step - warmup_steps) / (total_steps - warmup_steps)))
```

## Momentum: Building Velocity

Plain SGD can be slow in ravines — areas where the surface curves much more steeply in one dimension than another. Momentum adds a velocity term that accumulates gradients over time:

$$v_t = \beta v_{t-1} + \nabla J(\theta_t)$$
$$\theta_{t+1} = \theta_t - \eta v_t$$

The momentum coefficient $\beta$ (typically 0.9) controls how much past gradients influence the current update. This smooths out oscillations and accelerates convergence in consistent gradient directions.

**Nesterov momentum** looks ahead before computing the gradient, providing a "corrective" effect:
$$v_t = \beta v_{t-1} + \nabla J(\theta_t - \eta \beta v_{t-1})$$

## Adaptive Learning Rate Methods

These methods maintain per-parameter learning rates that adapt based on gradient history:

### AdaGrad
Accumulates squared gradients and divides by their square root:
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_t + \epsilon}} g_t$$

- ✅ Great for sparse features (NLP, recommendation systems)
- ❌ Learning rate monotonically decreases → training stalls

### RMSProp
Fixes AdaGrad's dying learning rate with an exponential moving average:
$$v_t = \beta v_{t-1} + (1-\beta) g_t^2$$
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{v_t + \epsilon}} g_t$$

### Adam (Adaptive Moment Estimation)
Combines momentum (first moment) with RMSProp (second moment):
$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$
$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$

Default: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. Adam is the default optimizer for most deep learning tasks.

### AdamW (Adam with Decoupled Weight Decay)
The current gold standard. Decouples weight decay from the gradient update, fixing a subtle bug in Adam's L2 regularization:
```python
optimizer = AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
```

## Practical Tips

1. **Start with AdamW** — it works well out of the box for most problems
2. **Use learning rate scheduling** — cosine annealing with warmup is a strong default
3. **Monitor gradient norms** — exploding gradients (norm > 10) indicate instability
4. **Gradient clipping** prevents explosions:
   ```python
   torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
   ```
5. **Learning rate finder**: sweep lr from $10^{-7}$ to $10^{1}$ and plot loss vs lr — the optimal lr is where loss decreases fastest
6. **SGD + momentum** still wins for some vision tasks (ImageNet training), but AdamW is dominant in NLP and generative AI

## When to Use What

| Scenario | Recommended |
|---|---|
| Default / NLP / Transformers | AdamW + cosine schedule |
| Computer Vision (large scale) | SGD + momentum + step decay |
| Sparse features / embeddings | AdaGrad or Adam |
| GANs | Adam with $\beta_1 = 0.5$ (standard trick) |
| Fine-tuning pretrained models | AdamW with very low lr ($10^{-5}$ to $5 \times 10^{-5}$) |

## Common Failure Modes

- **Loss spikes**: Usually caused by bad data (outliers, label noise) or lr too high
- **Loss plateaus**: Learning rate too low, or model capacity insufficient
- **Loss oscillates without decreasing**: Learning rate too high, try reducing by 10x
- **Gradient explosion**: Common in RNNs — use gradient clipping
- **Gradient vanishing**: Common in deep networks without skip connections — use ReLU/残差 connections

## Further Reading

- Ruder's overview remains the definitive survey of optimization algorithms
- The distill.pub momentum article provides unmatched intuition
- Smith (2017) "Cyclical Learning Rates" shows how to schedule lr without extensive tuning
- Loshchilov & Hutter (2019) introduced AdamW, now the standard for transformer training
