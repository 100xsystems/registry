---
slug: rl-13-reward-design
title: "Reward Design"
description: "Crafting the signals that guide agent behavior — reward shaping, sparse rewards, reward hacking, and curriculum learning."
order: 13
tags:
  - reinforcement-learning
  - reward-design
  - reward-shaping
  - reward-hacking
  - curriculum-learning
prerequisites:
  - rl-02-markov-decision-processes
knowledge_refs:
  - slug: rl-02-markov-decision-processes
    title: "Markov Decision Processes"
  - slug: rl-15-imitation-learning
    title: "Imitation Learning"
  - slug: safety-04-alignment
    title: "Alignment"
references:
  - title: "Ng et al. (1999) — Policy Invariance Under Reward Transformations"
    url: "https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf"
  - title: "OpenAI — Reward Engineering"
    url: "https://openai.com/research/"
  - title: "DeepMind — Reward Is Enough"
    url: "https://arxiv.org/abs/2111.06891"
  - title: "Curriculum Learning for RL — Bengio et al."
    url: "https://proceedings.mlr.press/v9/bengio09a.html"
  - title: "Inverse RL — Ng & Russell"
    url: "https://people.eecs.berkeley.edu/~russell/papers/ecml00-ir.pdf"
---
## Reward Design

The reward function defines what the agent optimizes. Poorly designed rewards lead to unintended behavior, reward hacking, and failed training. Reward design is one of the most critical and underappreciated aspects of RL.

### Reward Shaping

Adding intermediate rewards to guide the agent toward the goal:

**Sparse reward:** Only rewards at episode end (e.g., +1 for winning a game). Hard to learn from — the agent must stumble upon the goal by chance.

**Dense reward:** Rewards at every step (e.g., distance to goal). Easier to learn but may not capture the true objective.

**Potential-based shaping:** Add rewards based on a potential function Φ(s):

**F(s, s') = γΦ(s') - Φ(s)**

This provably preserves the optimal policy (Ng et al., 1999) while making learning easier.

### Reward Hacking

When the agent finds a loophole to maximize reward without achieving the intended goal:

- A boat racing game agent learns to spin in circles collecting small bonuses instead of finishing the race
- A robot learns to fall forward (covering distance) instead of walking
- An RLHF agent learns to tell users what they want to hear instead of being truthful

**Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure."

### Sparse vs. Dense Rewards

**Sparse:** Simple, aligned with true objective, but extremely hard to learn (exploration bottleneck).

**Dense:** Easier to learn, but risk of misalignment between shaped reward and true goal.

**Curriculum learning:** Start with dense rewards, gradually remove shaping as the agent learns.

### Inverse Reward Design

Given observed expert behavior, infer the reward function that would produce it. This is the inverse RL problem — used in imitation learning and alignment.

### Common Mistakes

- **Overly complex rewards:** Multiple competing reward terms create unintended tradeoffs.
- **Ignoring reward scale:** If one reward term is 100× larger than others, the agent ignores the smaller ones.
- **No reward debugging:** Always visualize what the agent is actually optimizing before scaling up training.

---

*Continue to learn about offline reinforcement learning — learning from pre-collected datasets.*
