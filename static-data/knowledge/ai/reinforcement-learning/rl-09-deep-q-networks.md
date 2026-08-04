---
slug: rl-09-deep-q-networks
title: "Deep Q-Networks (DQN)"
description: "Combining Q-learning with deep neural networks — experience replay, target networks, and the breakthrough that mastered Atari games."
order: 9
tags:
  - reinforcement-learning
  - dqn
  - deep-rl
  - experience-replay
  - target-networks
prerequisites:
  - rl-08-function-approximation
knowledge_refs:
  - rl-08-function-approximation
    title: "Function Approximation"
  - rl-06-q-learning
    title: "Q-Learning"
  - rl-11-actor-critic
    title: "Actor-Critic Methods"
references:
  - title: "Mnih et al. (2015) — Human-level control through deep RL (Nature)"
    url: "https://www.nature.com/articles/nature14236"
  - title: "DeepMind DQN — OpenAI Spinning Up"
    url: "https://spinningup.openai.com/en/latest/spinningup/algorithms/dqn.html"
  - title: "Double DQN — Van Hasselt et al. (2016)"
    url: "https://arxiv.org/abs/1509.06461"
  - title: "Dueling DQN — Wang et al. (2016)"
    url: "https://arxiv.org/abs/1511.06581"
  - title: "Rainbow DQN — Hessel et al. (2018)"
    url: "https://arxiv.org/abs/1710.02229"
---

## Deep Q-Networks (DQN)

DQN (Mnih et al., 2015) was the breakthrough that proved deep neural networks could learn to play games directly from pixels. It combined Q-learning with deep learning and introduced two key innovations that stabilized training.

### The Architecture

A convolutional neural network takes raw pixel frames as input and outputs Q-values for each possible action:

**Input:** Stack of 4 grayscale frames (84×84)
**Output:** Q(s, a₁), Q(s, a₂), ..., Q(s, aₙ) — one value per action

The agent selects the action with the highest Q-value (or explores via ε-greedy).

### Key Innovation 1: Experience Replay

Instead of learning from consecutive experiences (which are highly correlated), DQN stores transitions in a replay buffer and samples random mini-batches:

**Buffer:** (s_t, a_t, r_{t+1}, s_{t+1}, done)

**Training:** Sample random mini-batches from the buffer.

Benefits:
- Breaks temporal correlation between consecutive experiences
- Reuses experiences multiple times (sample efficiency)
- Stabilizes learning by diversifying training data

### Key Innovation 2: Target Network

DQN uses a separate **target network** that is periodically updated (every C steps) with the current network's weights. The target network computes the bootstrap target:

**Target:** r_{t+1} + γ max_a Q_target(s_{t+1}, a)

Benefits:
- Prevents the "chasing your own tail" problem
- Provides stable targets for the learning updates
- Significantly reduces divergence

### Extensions

**Double DQN (2016):** Uses the online network to select actions and the target network to evaluate them. Reduces overestimation bias in Q-learning.

**Dueling DQN (2016):** Separates the network into value stream V(s) and advantage stream A(s,a). Better at states where action choice doesn't matter.

**Rainbow DQN (2018):** Combines 6 extensions (Double, Dueling, Prioritized Replay, Multi-step, Distributional, Noisy Nets). Achieves state-of-the-art on Atari.

### Training Process

1. Observe state s
2. Select action a via ε-greedy
3. Execute a, observe reward r and next state s'
4. Store (s, a, r, s') in replay buffer
5. Sample mini-batch from buffer
6. Compute target: r + γ max_a Q_target(s', a)
7. Update Q-network to minimize (Q(s,a) - target)²
8. Periodically update target network

### Common Mistakes

- **No experience replay:** Consecutive samples are correlated, causing instability.
- **No target network:** Without stable targets, Q-values oscillate or diverge.
- **Ignoring overestimation:** Standard Q-learning overestimates Q-values. Use Double DQN.

---

*Continue to learn about policy gradient methods — optimizing policies directly instead of value functions.*
