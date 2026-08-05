---
slug: rl-05-temporal-difference-learning
title: "Temporal Difference Learning"
description: "The core of modern RL — combining Monte Carlo sampling with bootstrapping for online, incremental learning."
order: 5
tags:
  - reinforcement-learning
  - temporal-difference
  - td-learning
  - sarsa
  - eligibility-traces
  - bootstrapping
prerequisites:
  - rl-04-monte-carlo-methods
knowledge_refs:
  - slug: rl-04-monte-carlo-methods
    title: "Monte Carlo Methods"
  - slug: rl-06-q-learning
    title: "Q-Learning"
references:
  - title: "Sutton & Barto — Chapter 6: Temporal-Difference Learning"
    url: "http://incompleteideas.net/book/the-book-2nd.html"
  - title: "David Silver — RL Course: TD Learning"
    url: "https://www.davidsilver.uk/teaching/"
  - title: "Temporal Difference Learning — Richard Warren"
    url: "https://richard-warren.github.io/blog/rl_intro_3/"
  - title: "Dissecting RL: Temporal Differencing — Pattacchiola"
    url: "https://mpatacchiola.github.io/blog/2017/01/29/dissecting-reinforcement-learning-3.html"
  - title: "Sutton & Barto Summary: TD Learning"
    url: "https://lcalem.github.io/blog/2018/10/31/sutton-chap06-td"
---
## Temporal Difference Learning

Temporal Difference (TD) learning is the core insight of modern RL. It combines Monte Carlo's sampling with Dynamic Programming's bootstrapping — learning from experience without waiting for episode completion.

### The Core Idea

TD methods update estimates based on other learned estimates, without waiting for the final outcome:

**V(S_t) ← V(S_t) + α[R_{t+1} + γV(S_{t+1}) - V(S_t)]**

The term **δ_t = R_{t+1} + γV(S_{t+1}) - V(S_t)** is the **TD error** — the difference between the estimated target and the current estimate. It measures "surprise."

### TD(0): One-Step TD

The simplest form. After each step, update using only the immediate reward and next state's value:

- Learns online (every step)
- Works in continuing tasks
- Lower variance than MC
- Biased (bootstraps from estimates)

### SARSA: On-Policy TD Control

SARSA (State-Action-Reward-State-Action) learns action values Q(s,a) using on-policy updates:

**Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γQ(S_{t+1}, A_{t+1}) - Q(S_t, A_t)]**

The key: A_{t+1} is the *actual* next action taken by the current policy (e.g., ε-greedy).

### Expected SARSA

Instead of sampling the next action, compute the expectation over all actions:

**Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ Σ_a π(a|S_{t+1}) Q(S_{t+1}, a) - Q(S_t, A_t)]**

More stable than SARSA because it eliminates sampling variance. If π is greedy, it behaves identically to Q-learning.

### TD(λ) and Eligibility Traces

TD(0) looks one step ahead. Monte Carlo looks to episode end. TD(λ) bridges both:

**λ-return:** G_t^λ = (1-λ) Σ_{n=1}^∞ λ^{n-1} G_{t:t+n}

- λ = 0: Standard 1-step TD
- λ = 1: Monte Carlo
- 0 < λ < 1: Blended approach

**Eligibility traces** provide an efficient online implementation. A trace z_t accumulates for recently visited states and decays over time. When a TD error occurs, all eligible states receive credit proportional to their trace:

**z_t = γλz_{t-1} + ∇_w v̂(S_t, w)**
**w_{t+1} = w_t + αδ_t z_t**

### Comparison

| Method | Variance | Bias | Updates | Sample Efficiency |
|---|---|---|---|---|
| MC | High | None | End of episode | Low |
| TD(0) | Low | High | Every step | High |
| TD(λ) | Medium | Medium | Every step | High |

### Common Mistakes

- **Confusing TD with MC:** TD bootstraps (uses estimates). MC uses actual returns.
- **Ignoring eligibility traces:** For sparse rewards, eligibility traces dramatically speed up learning.
- **Setting λ wrong:** λ too high increases variance. λ too low loses long-term credit assignment.

---

*Continue to learn about Q-learning — the off-policy TD control algorithm.*
