---
slug: rl-06-q-learning
title: "Q-Learning"
description: "The off-policy TD control algorithm that learns the optimal action-value function directly — the foundation of deep RL."
order: 6
tags:
  - reinforcement-learning
  - q-learning
  - off-policy
  - td-control
  - q-table
prerequisites:
  - rl-05-temporal-difference-learning
knowledge_refs:
  - rl-05-temporal-difference-learning
    title: "Temporal Difference Learning"
  - rl-09-deep-q-networks
    title: "Deep Q-Networks"
  - rl-07-exploration-vs-exploitation
    title: "Exploration vs Exploitation"
references:
  - title: "Q-Learning — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Q-learning"
  - title: "A Deep Dive into Q-Learning — NeuraForge"
    url: "https://neuraforge.substack.com/p/a-deep-dive-into-q-learning"
  - title: "Q-Learning in Python — GeeksforGeeks"
    url: "https://www.geeksforgeeks.org/machine-learning/q-learning-in-python/"
  - title: "Watkins (1989) — Learning from Delayed Rewards"
    url: "https://link.springer.com/article/10.1007/BF00992698"
  - title: "OpenAI Spinning Up — Q-Learning"
    url: "https://spinningup.openai.com/en/latest/spinningup/algorithms/qlearning.html"
---

## Q-Learning

Q-learning is the off-policy TD control algorithm that learns the optimal action-value function Q*(s,a) directly. It's the foundation of deep RL — DQN, Rainbow, and most value-based algorithms build on Q-learning.

### The Q-Learning Update Rule

**Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ max_a Q(S_{t+1}, a) - Q(S_t, A_t)]**

Key insight: The update uses **max_a Q(S_{t+1}, a)** — the value of the best possible next action — regardless of what action the agent actually takes. This makes Q-learning off-policy.

### The Q-Table

A lookup table where rows are states and columns are actions. Each cell stores Q(s,a) — the estimated value of taking action a in state s.

For small, discrete MDPs, Q-learning converges to the optimal Q* with probability 1 if:
- Every state-action pair is visited infinitely often
- Learning rate satisfies Robbins-Monro conditions

### Q-Learning vs SARSA

| Aspect | Q-Learning (Off-Policy) | SARSA (On-Policy) |
|---|---|---|
| Update target | max_a Q(s', a) | Q(s', a') — actual next action |
| Learns | Optimal policy directly | Value of current policy |
| Exploration impact | Ignores exploration mistakes | Learns from exploration penalties |
| Training performance | Lower (explores dangerously) | Higher (safe exploration) |
| Final policy | Optimal | Near-optimal (ε-dependent) |

### The Cliff Walking Example

In the classic cliff walking gridworld:
- **Q-learning** learns to walk along the cliff edge — optimal but risky during training
- **SARSA** learns to walk safely inland — suboptimal but safer during training

This illustrates the exploration-exploitation tradeoff in action.

### Convergence Guarantees

Watkins and Dayan (1992) proved Q-learning converges to Q* with probability 1 given:
1. All state-action pairs are visited infinitely often
2. α_t satisfies: Σα_t = ∞ and Σα_t² < ∞

In practice, convergence is slow for large state spaces — motivating function approximation.

### Common Mistakes

- **No exploration:** Without ε-greedy, Q-learning never discovers good actions.
- **Learning rate too high:** Causes oscillation and divergence.
- **Ignoring convergence conditions:** Q-learning may not converge with function approximation.

---

*Continue to learn about exploration vs exploitation — the fundamental tradeoff in RL.*
