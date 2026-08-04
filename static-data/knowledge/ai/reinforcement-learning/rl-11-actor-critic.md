---
slug: rl-11-actor-critic
title: "Actor-Critic Methods"
description: "Combining policy gradients with value functions — the actor-critic architecture, A2C, A3C, and the advantage function."
order: 11
tags:
  - reinforcement-learning
  - actor-critic
  - a2c
  - a3c
  - advantage-function
prerequisites:
  - rl-10-policy-gradient-methods
knowledge_refs:
  - rl-10-policy-gradient-methods
    title: "Policy Gradient Methods"
  - rl-12-proximal-policy-optimization
    title: "PPO & Modern Policy Optimization"
  - rl-09-deep-q-networks
    title: "Deep Q-Networks"
references:
  - title: "Mnih et al. (2016) — Asynchronous Methods for Deep RL (A3C)"
    url: "https://proceedings.mlr.press/v48/mniha16.html"
  - title: "Actor-Critic Methods: A3C and A2C — Daniel Takeshi"
    url: "https://danieltakeshi.github.io/2018/06/28/a2c-a3c/"
  - title: "A2C and A3C in PyTorch — Isaac Kargar"
    url: "https://kargarisaac.medium.com/rl-series-a2c-and-a3c-in-pytorch-6e9edf5c8788"
  - title: "OpenAI Baselines: ACKTR & A2C"
    url: "https://openai.com/index/openai-baselines-acktr-a2c/"
  - title: "Actor-Critic Algorithm — GeeksforGeeks"
    url: "https://www.geeksforgeeks.org/machine-learning/actor-critic-algorithm-in-reinforcement-learning/"
---

## Actor-Critic Methods

Actor-critic methods combine the best of policy gradients and value-based methods. The actor selects actions while the critic evaluates them — reducing variance while maintaining the flexibility of policy optimization.

### The Architecture

**Actor (π_θ):** Parameterized policy that outputs action probabilities given a state. Updated via policy gradient, modulated by the critic's feedback.

**Critic (V_w or Q_w):** Parameterized value function that evaluates states or state-action pairs. Trained via TD learning to minimize estimation error.

### The Advantage Function

Instead of scaling policy gradient updates by raw returns (high variance), use the **advantage function**:

**A(s, a) = Q(s, a) - V(s)**

- **A > 0:** Action was better than average → increase probability
- **A < 0:** Action was worse than average → decrease probability

In practice, computed via n-step returns or Generalized Advantage Estimation (GAE).

### A3C (Asynchronous Advantage Actor-Critic)

Mnih et al. (2016) introduced asynchronous parallelism:
- Multiple workers explore different environments simultaneously
- Decorrelated data without experience replay
- Each worker computes gradients and asynchronously updates a shared global network
- Optimized for multi-core CPUs

### A2C (Synchronous Advantage Actor-Critic)

OpenAI's synchronous alternative:
- All workers take steps in lock-step
- Gradients are averaged into a synchronized batch update
- Better GPU utilization
- More stable and reproducible than A3C
- Often matches or exceeds A3C performance

### Comparison

| Aspect | A3C | A2C |
|---|---|---|
| Execution | Asynchronous | Synchronous |
| Hardware | CPU-optimized | GPU-optimized |
| Stability | Race-condition noise | Deterministic |
| Reproducibility | Lower | Higher |

### Common Mistakes

- **No advantage estimation:** Using raw returns causes high variance.
- **Ignoring entropy bonus:** Without entropy regularization, policies collapse prematurely.
- **Too many workers:** Diminishing returns beyond a point; communication overhead grows.

---

*Continue to learn about PPO — the modern standard for policy optimization.*
