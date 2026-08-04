---
slug: rl-19-rl-for-recommendation
title: "RL for Recommender Systems"
description: "Sequential decision-making for user engagement — bandits, contextual bandits, and RL for recommendations and ads."
order: 19
tags:
  - reinforcement-learning
  - recommender-systems
  - bandits
  - contextual-bandits
  - user-modeling
prerequisites:
  - rl-01-what-is-reinforcement-learning
knowledge_refs:
  - rl-01-what-is-reinforcement-learning
    title: "What Is Reinforcement Learning?"
  - rl-07-exploration-vs-exploitation
    title: "Exploration vs Exploitation"
  - rl-06-q-learning
    title: "Q-Learning"
references:
  - title: "Contextual Bandits for Recommendations — Li et al."
    url: "https://arxiv.org/abs/1003.0146"
  - title: "RL for Recommendation Systems — Survey"
    url: "https://arxiv.org/abs/2203.13539"
  - title: "Deep Reinforcement Learning for Page-Wide Recommendations"
    url: "https://arxiv.org/abs/1611.00399"
  - title: "Bandit Algorithms for Website Optimization"
    url: "https://www.jmlr.org/papers/volume14/li13a/li13a.pdf"
  - title: "Exploration in Interactive Recommender Systems"
    url: "https://dl.acm.org/doi/10.1145/2652481.2652496"
---

## RL for Recommender Systems

Recommendation is a sequential decision-making problem: each recommendation changes user state, and the goal is to maximize long-term engagement, not just immediate clicks.

### Why RL for Recommendations?

**Sequential nature:** Recommendations are sequential — each choice affects future user behavior.

**Delayed feedback:** True preference (purchase, subscription) arrives long after the click.

**Exploration-exploitation:** The system must try new items (explore) while recommending known good items (exploit).

**Long-term optimization:** Maximizing immediate clicks leads to clickbait. RL optimizes long-term user satisfaction.

### Bandit Approaches

**Multi-armed bandits:** The simplest case — K items, unknown reward distributions. Pull one arm per round. Maximizes cumulative reward.

**Contextual bandits:** Items have features (category, price, popularity). Use features to generalize across items. This is the foundation of modern recommendation RL.

**LinUCB:** Upper confidence bound for linear contextual bandits. Provably optimal under linear reward assumptions.

### Deep RL for Recommendations

For large-scale recommendations with millions of items:
- **State:** User history, demographics, context (time, device)
- **Action:** Select item from catalog
- **Reward:** Click, purchase, time spent, satisfaction

Deep Q-networks or policy gradient methods learn user response models and optimize long-term engagement.

### Challenges

**Scalability:** Action spaces with millions of items require efficient exploration.
**Non-stationarity:** User preferences change over time.
**Feedback loops:** Recommendations shape preferences, creating feedback loops.
**Cold start:** New users and items have no history.

### Common Mistakes

- **Optimizing for clicks:** Clicks ≠ satisfaction. Long-term metrics matter.
- **Ignoring exploration:** Pure exploitation leads to filter bubbles.
- **No user modeling:** Static recommendations don't adapt to changing preferences.

---

*Continue to learn about evaluating RL agents — measuring performance and ensuring reproducibility.*
