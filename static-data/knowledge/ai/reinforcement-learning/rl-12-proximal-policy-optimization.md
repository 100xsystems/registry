---
slug: rl-12-proximal-policy-optimization
title: "PPO & Modern Policy Optimization"
description: "The de facto standard for policy optimization — TRPO's simplified successor with clipped surrogate objectives and trust regions."
order: 12
tags:
  - reinforcement-learning
  - ppo
  - trpo
  - clipped-objective
  - trust-region
prerequisites:
  - rl-11-actor-critic
knowledge_refs:
  - slug: rl-11-actor-critic
    title: "Actor-Critic Methods"
  - slug: rl-10-policy-gradient-methods
    title: "Policy Gradient Methods"
  - slug: rl-13-reward-design
    title: "Reward Design"
references:
  - title: "Schulman et al. (2017) — Proximal Policy Optimization"
    url: "https://huggingface.co/papers/1707.06347"
  - title: "Schulman et al. (2015) — Trust Region Policy Optimization"
    url: "https://proceedings.mlr.press/v37/schulman15.html"
  - title: "PPO — OpenAI Spinning Up"
    url: "https://spinningup.openai.com/en/latest/algorithms/ppo.html"
  - title: "TRPO — OpenAI Spinning Up"
    url: "https://spinningup.openai.com/en/latest/algorithms/trpo.html"
  - title: "GAE — Schulman et al. (2016)"
    url: "https://arxiv.org/abs/1606.05560"
---
## PPO & Modern Policy Optimization

PPO (Schulman et al., 2017) is the most widely used policy optimization algorithm. It achieves TRPO's stability through a simple clipped objective that's easy to implement and tune.

### The Problem PPO Solves

Vanilla policy gradients perform one update per data sample. If the step size is too large, a single bad update can catastrophically degrade performance. Small changes in parameter space can cause massive behavior shifts.

### TRPO: The Precursor

TRPO (Trust Region Policy Optimization) constrains policy updates using KL divergence:

**E[D_KL(π_old || π)] ≤ δ**

This ensures the new policy doesn't deviate too far from the old one. But TRPO requires computing the Fisher Information Matrix — expensive and complex to implement.

### PPO-Clip: The Practical Solution

PPO achieves trust region behavior with a simple clipping mechanism:

**L_CLIP(θ) = E[min(r_t(θ)Â_t, clip(r_t(θ), 1-ε, 1+ε)Â_t)]**

Where:
- **r_t(θ) = π_θ(a|s) / π_θold(a|s)** — probability ratio
- **Â_t** — estimated advantage
- **ε** — clip parameter (typically 0.1–0.2)

**How clipping works:**
- **Positive advantage:** Increasing action probability is rewarded, but capped at ratio 1+ε
- **Negative advantage:** Decreasing action probability is rewarded, but capped at ratio 1-ε

This prevents destructive large updates while allowing small, safe improvements.

### Practical Implementation

PPO allows multiple epochs of minibatch SGD on the same trajectory:
1. Collect trajectories using current policy
2. Compute advantages (usually via GAE)
3. Run K epochs of minibatch updates on the collected data
4. Repeat with new trajectories

**Total loss:** L = L_CLIP - c₁L_VF + c₂S[π]

Where L_VF is the value function loss and S is the entropy bonus.

### Early Stopping

Monitor approximate KL divergence. If it exceeds a threshold, stop updating for that epoch to prevent destructive policy shifts.

### Common Mistakes

- **No clipping:** Without the clip, PPO degenerates to vanilla policy gradients.
- **Too many epochs:** Too many passes over the same data causes overfitting.
- **Ignoring GAE:** Poor advantage estimation degrades PPO's performance.

---

*Continue to learn about reward design — crafting the signals that guide agent behavior.*
