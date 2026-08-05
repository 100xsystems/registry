---
slug: rl-10-policy-gradient-methods
title: "Policy Gradient Methods"
description: "Optimizing policies directly — the policy gradient theorem, REINFORCE, variance reduction, and natural gradients."
order: 10
tags:
  - reinforcement-learning
  - policy-gradient
  - reinforce
  - policy-optimization
  - variance-reduction
prerequisites:
  - rl-09-deep-q-networks
knowledge_refs:
  - slug: rl-09-deep-q-networks
    title: "Deep Q-Networks"
  - slug: rl-11-actor-critic
    title: "Actor-Critic Methods"
  - slug: rl-12-proximal-policy-optimization
    title: "PPO & Modern Policy Optimization"
references:
  - title: "Sutton et al. (1999) — Policy Gradient Methods"
    url: "https://papers.nips.cc/paper/1999/hash/464d828b85b0bed98e022f3a26e17d94-Abstract.html"
  - title: "OpenAI Spinning Up — Policy Gradient"
    url: "https://spinningup.openai.com/en/latest/spinningup/rl_intro.html#policy-optimization"
  - title: "REINFORCE Algorithm — Williams (1992)"
    url: "https://link.springer.com/article/10.1007/BF00992698"
  - title: "Policy Gradient Methods for RL — Sutton et al."
    url: "https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf"
  - title: "Lilian Weng — Policy Gradient Algorithms"
    url: "https://lilianweng.github.io/posts/2018-04-08-policy-gradient/"
---
## Policy Gradient Methods

Instead of learning value functions and deriving policies from them, policy gradient methods optimize the policy directly. They parameterize the policy as π_θ(a|s) and use gradient ascent on expected return.

### Why Policy Gradient?

**Continuous action spaces:** Value-based methods (Q-learning) need to take max over actions — infeasible for continuous actions.

**Stochastic policies:** Q-learning learns deterministic policies. Policy gradient naturally handles stochastic policies, which are optimal in partially observable environments.

**Smoother optimization:** Small policy changes lead to small performance changes, unlike value-based methods where small Q-value changes can cause large policy changes.

### The Policy Gradient Theorem

The gradient of expected return J(θ) with respect to policy parameters θ:

**∇_θ J(θ) = E_π[∇_θ log π_θ(a|s) · G_t]**

- **∇_θ log π_θ(a|s):** Direction to increase probability of action a in state s
- **G_t:** Return from time t — scales the update by how good the action was

Intuition: Increase probability of actions that led to high returns, decrease probability of actions that led to low returns.

### REINFORCE

The simplest policy gradient algorithm:

```
Initialize policy π_θ
For each episode:
    Collect trajectory: s0, a0, r1, s1, a1, r2, ...
    For each step t:
        Gt ← return from step t
        θ ← θ + α ∇_θ log π_θ(at|st) · Gt
```

REINFORCE is Monte Carlo policy gradient — it waits until the episode ends to compute returns.

### Variance Reduction

REINFORCE has high variance because returns vary wildly across episodes.

**Baseline subtraction:** Subtract a baseline b(s) from the return:

**∇_θ J(θ) = E_π[∇_θ log π_θ(a|s) · (G_t - b(s))]**

The baseline doesn't change the expected gradient but reduces variance. Common baseline: state value function V(s).

**Discounting:** Apply γ^t to weight earlier rewards more than later ones.

### Common Mistakes

- **No baseline:** High variance makes learning unstable and slow.
- **Too high learning rate:** Policy gradient methods are sensitive to step size.
- **Ignoring exploration:** Policy gradient needs stochastic policies for exploration.

---

*Continue to learn about actor-critic methods — combining policy gradients with value functions.*
