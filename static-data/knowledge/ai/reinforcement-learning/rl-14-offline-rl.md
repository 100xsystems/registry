---
slug: rl-14-offline-rl
title: "Offline Reinforcement Learning"
description: "Learning from pre-collected datasets without environment interaction — batch RL, conservative Q-learning, and decision transformers."
order: 14
tags:
  - reinforcement-learning
  - offline-rl
  - batch-rl
  - conservative-q-learning
  - decision-transformer
prerequisites:
  - rl-09-deep-q-networks
knowledge_refs:
  - rl-09-deep-q-networks
    title: "Deep Q-Networks"
  - rl-15-imitation-learning
    title: "Imitation Learning"
  - rl-10-policy-gradient-methods
    title: "Policy Gradient Methods"
references:
  - title: "Conservative Q-Learning — Kumar et al. (2020)"
    url: "https://arxiv.org/abs/2006.04779"
  - title: "Decision Transformer — Chen et al. (2021)"
    url: "https://arxiv.org/abs/2106.01345"
  - title: "Offline RL — Levine et al. (2020)"
    url: "https://arxiv.org/abs/2005.01643"
  - title: "BCQ — Fujimoto et al. (2019)"
    url: "https://arxiv.org/abs/1812.02900"
  - title: "MOReL — Kumar et al. (2020)"
    url: "https://arxiv.org/abs/2005.01643"
---

## Offline Reinforcement Learning

Offline RL learns policies from pre-collected datasets without interacting with the environment. This is critical when environment interaction is expensive, dangerous, or impossible — autonomous driving, healthcare, robotics.

### Why Offline RL?

**Safety:** Can't afford to explore in safety-critical domains (self-driving, medical treatment).

**Cost:** Real-world interaction is expensive (robot hardware, energy).

**Data availability:** Large datasets already exist (web logs, driving records, clinical data).

**Reproducibility:** Fixed datasets enable reproducible research.

### The Challenge: Distribution Shift

Standard RL algorithms are trained on data they generate. Offline, the policy may select actions never seen in the dataset. Extrapolation beyond the dataset leads to catastrophic overestimation.

### Conservative Q-Learning (CQL)

CQL addresses overestimation by learning a lower bound on Q-values:

**Q̂(s,a) ≤ Q*(s,a)** for all (s,a) in the dataset

It penalizes Q-values for actions outside the dataset's distribution, preventing the policy from exploiting unknown regions.

### Batch-Constrained Deep Q-Learning (BCQ)

BCQ constrains the policy to only select actions similar to those in the dataset:
1. Train a generative model of dataset actions
2. During action selection, perturb only the top actions from the generative model
3. The policy never strays far from the dataset distribution

### Decision Transformer

Reframes RL as sequence modeling:
- Treat (return-to-go, state, action) as tokens
- Train a transformer to predict the next action given desired return and history
- At inference, specify the desired return and the model generates actions

No Bellman updates, no bootstrapping — just sequence prediction.

### Common Mistakes

- **Using standard RL on offline data:** Q-learning overestimates values for unseen actions.
- **Ignoring dataset quality:** Bad data produces bad policies, regardless of algorithm.
- **Over-constraining:** Too conservative policies don't learn anything new.

---

*Continue to learn about imitation learning — learning from expert demonstrations.*
