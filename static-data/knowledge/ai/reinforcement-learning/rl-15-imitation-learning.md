---
slug: rl-15-imitation-learning
title: "Imitation Learning"
description: "Learning from expert demonstrations — behavior cloning, DAgger, inverse RL, and learning without hand-crafted rewards."
order: 15
tags:
  - reinforcement-learning
  - imitation-learning
  - behavior-cloning
  - dagger
  - inverse-rl
prerequisites:
  - rl-13-reward-design
knowledge_refs:
  - rl-13-reward-design
    title: "Reward Design"
  - rl-14-offline-rl
    title: "Offline Reinforcement Learning"
  - rl-10-policy-gradient-methods
    title: "Policy Gradient Methods"
references:
  - title: "Ross & Bagnell (2010) — Efficient Reductions for Imitation Learning"
    url: "https://proceedings.mlr.press/v9/ross10a.html"
  - title: "Behavior Cloning — Ross et al."
    url: "https://www.cs.cmu.edu/~sross1/publications/RSS-AoIR12-ross.pdf"
  - title: "DAgger — Ross et al. (2011)"
    url: "https://arxiv.org/abs/1011.0686"
  - title: "Inverse RL — Ng & Russell (2000)"
    url: "https://people.eecs.berkeley.edu/~russell/papers/ecml00-ir.pdf"
  - title: "GAIL — Ho & Ermon (2016)"
    url: "https://arxiv.org/abs/1606.03476"
---

## Imitation Learning

Imitation learning learns policies from expert demonstrations instead of hand-crafted reward functions. When designing rewards is hard but expert behavior is available, imitation learning bridges the gap.

### Behavior Cloning

The simplest approach: treat demonstrations as a supervised learning problem.

**Collect expert demonstrations:** (state, action) pairs
**Train a policy:** π_θ(a|s) to minimize classification loss (discrete actions) or regression loss (continuous actions)

**Advantages:**
- Simple to implement
- No reward function needed
- Works with any supervised learning method

**Limitations:**
- Compounding errors: small mistakes lead to unseen states
- No exploration: never learns to recover from mistakes
- Distribution shift: training distribution ≠ test distribution

### DAgger (Dataset Aggregation)

DAgger addresses compounding errors by iteratively aggregating expert data:

1. Train initial policy π_1 on expert demonstrations
2. Run π_1 in the environment
3. Ask the expert to label the states the policy actually visits
4. Add these labels to the training dataset
5. Retrain the policy on the combined dataset
6. Repeat

DAgger bridges the distribution shift by training on states the policy encounters, not just expert states.

### Inverse Reinforcement Learning (IRL)

Instead of learning a policy directly, IRL infers the reward function from expert behavior, then runs RL on the inferred reward:

1. Observe expert demonstrations
2. Infer reward function R(s,a) that makes expert behavior optimal
3. Train a policy using RL on R(s,a)

**Applications:** Learning human preferences, reward shaping, understanding expert intent.

### GAIL (Generative Adversarial Imitation Learning)

Combines GANs with imitation learning:
- Generator: policy that generates state-action trajectories
- Discriminator: distinguishes expert from generated trajectories
- Training: adversarial — the policy improves to fool the discriminator

### Common Mistakes

- **Pure behavior cloning:** Without DAgger or online correction, compounding errors destroy performance.
- **Assuming expert optimality:** IRL assumes the expert is optimal. Suboptimal experts produce suboptimal rewards.
- **No diversity in demonstrations:** A single expert trajectory may not capture the full solution space.

---

*Continue to learn about multi-agent reinforcement learning — agents interacting with each other.*
