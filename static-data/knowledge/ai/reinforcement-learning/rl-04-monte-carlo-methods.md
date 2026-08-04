---
slug: rl-04-monte-carlo-methods
title: "Monte Carlo Methods"
description: "Learning from complete episodes — model-free methods that estimate value functions by averaging sample returns."
order: 4
tags:
  - reinforcement-learning
  - monte-carlo
  - model-free
  - importance-sampling
  - on-policy
  - off-policy
prerequisites:
  - rl-03-dynamic-programming
knowledge_refs:
  - rl-03-dynamic-programming
    title: "Dynamic Programming"
  - rl-05-temporal-difference-learning
    title: "Temporal Difference Learning"
references:
  - title: "Sutton & Barto — Chapter 5: Monte Carlo Methods"
    url: "http://incompleteideas.net/book/the-book-2nd.html"
  - title: "David Silver — RL Course: Monte Carlo"
    url: "https://www.davidsilver.uk/teading/"
  - title: "Monte Carlo RL — Towards Data Science"
    url: "https://towardsdatascience.com/"
  - title: "OpenAI Spinning Up — Monte Carlo"
    url: "https://spinningup.openai.com/en/latest/spinningup/rl_intro.html"
  - title: "Berkeley CS285 — Monte Carlo Methods"
    url: "https://rail.eecs.berkeley.edu/deeprlcourse/"
---

## Monte Carlo Methods

Monte Carlo (MC) methods learn directly from episodes of experience — no model of the environment is needed. They estimate value functions by averaging complete returns from actual trajectories.

### Core Idea

Instead of using the Bellman equation with known transitions (DP), MC methods:
1. Run complete episodes
2. Observe the actual rewards received
3. Average the returns to estimate values

**V(s) ← average of all returns G_t where S_t = s**

### First-Visit vs. Every-Visit MC

**First-Visit MC:** Only uses the first visit to each state per episode. Guarantees unbiased estimates.

**Every-Visit MC:** Uses every visit to a state per episode. Lower variance but slightly biased.

First-Visit MC is the textbook standard, but Every-Visit MC works well in practice.

### MC for Prediction (Policy Evaluation)

Given policy π, estimate V^π:
```
Initialize V(s) arbitrarily
For each episode:
    Generate trajectory following π: S0, A0, R1, S1, A1, R2, ...
    For each state St in the episode:
        Gt ← return from St
        V(St) ← V(St) + α[Gt - V(St)]  (incremental update)
```

### MC for Control (Finding Optimal Policy)

Use ε-greedy policy improvement:
1. Evaluate the current ε-greedy policy using MC
2. Improve the policy greedily with respect to the learned values
3. Repeat (GLIE — Greedy in the Limit with Infinite Exploration)

### On-Policy vs. Off-Policy

**On-Policy MC:** The behavior policy (what the agent does) and the target policy (what we're evaluating) are the same. Simple but requires exploring all actions.

**Off-Policy MC:** The behavior policy differs from the target policy. Uses importance sampling to correct for the distribution mismatch.

### Importance Sampling

Off-Policy methods need to correct for the fact that the behavior policy generated the data, not the target policy:

**Importance sampling ratio:** ρ_{t:T-1} = Π_{k=t}^{T-1} π(A_k|S_k) / b(A_k|S_k)

This ratio weights each return by how much more likely the target policy would have chosen those actions compared to the behavior policy.

### Advantages and Limitations

**Advantages:**
- Model-free — no transition probabilities needed
- Unbiased estimates (first-visit MC)
- Can learn from real experience
- Converges to optimal policy (GLIE)

**Limitations:**
- Must wait until end of episode to update
- Doesn't work for continuing (non-episodic) tasks
- High variance in estimates
- Inefficient for large state spaces

### Common Mistakes

- **Using MC for continuing tasks:** MC requires complete episodes. Use TD for continuing tasks.
- **Ignoring variance:** MC returns have high variance, especially for long episodes.
- **No exploration:** Without ε-greedy or other exploration, MC may never visit all states.

---

*Continue to learn about temporal difference learning — combining Monte Carlo sampling with bootstrapping.*
