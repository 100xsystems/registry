---
slug: rl-03-dynamic-programming
title: "Dynamic Programming"
description: "Computing optimal policies when the environment model is known — policy evaluation, policy improvement, and value iteration."
order: 3
tags:
  - reinforcement-learning
  - dynamic-programming
  - policy-iteration
  - value-iteration
  - bellman-equations
prerequisites:
  - rl-02-markov-decision-processes
knowledge_refs:
  - rl-02-markov-decision-processes
    title: "Markov Decision Processes"
  - rl-04-monte-carlo-methods
    title: "Monte Carlo Methods"
references:
  - title: "Sutton & Barto — Chapter 4: Dynamic Programming"
    url: "http://incompleteideas.net/book/the-book-2nd.html"
  - title: "David Silver — RL Course: Dynamic Programming"
    url: "https://www.davidsilver.uk/teaching/"
  - title: "Dynamic Programming in RL — Towards Data Science"
    url: "https://towardsdatascience.com/"
  - title: "OpenAI Spinning Up — Dynamic Programming"
    url: "https://spinningup.openai.com/en/latest/spinningup/rl_intro.html"
  - title: "Berkeley CS285 — Dynamic Programming"
    url: "https://rail.eecs.berkeley.edu/deeprlcourse/"
---

## Dynamic Programming

Dynamic programming (DP) methods compute optimal policies when the environment model (transition probabilities and rewards) is fully known. While rarely practical in real-world problems, DP provides the conceptual foundation for all RL algorithms.

### The Key Idea

DP uses the Bellman equations as update rules. By iteratively applying these equations, value functions converge to the optimal values, from which the optimal policy can be extracted.

### Policy Evaluation (Prediction)

Given a fixed policy π, compute V^π(s) for all states:

```
Initialize V(s) arbitrarily
Repeat:
    For each state s:
        V(s) ← Σ_a π(a|s) Σ_{s'} P(s'|s,a) [R(s,a) + γV(s')]
Until V converges
```

This is iterative application of the Bellman equation as an update rule.

### Policy Improvement

Given V^π, compute a better policy π' by acting greedily with respect to V^π:

π'(s) = argmax_a Σ_{s'} P(s'|s,a) [R(s,a) + γV^π(s')]

The improved policy is guaranteed to be at least as good as the original (policy improvement theorem).

### Policy Iteration

Combine evaluation and improvement iteratively:

1. Initialize a random policy π
2. Evaluate π → compute V^π
3. Improve π → compute π' (greedy w.r.t. V^π)
4. Repeat until policy converges

Policy iteration converges to the optimal policy in a finite number of iterations for finite MDPs.

### Value Iteration

Instead of fully evaluating each policy before improving, value iteration interleaves one step of evaluation with improvement:

```
Initialize V(s) arbitrarily
Repeat:
    For each state s:
        V(s) ← max_a Σ_{s'} P(s'|s,a) [R(s,a) + γV(s')]
Until V converges
Extract policy: π(s) = argmax_a Σ_{s'} P(s'|s,a) [R(s,a) + γV(s')]
```

Value iteration is often more efficient than policy iteration because it doesn't require full convergence at each step.

### Comparison

| Method | Convergence | Complexity | Best For |
|---|---|---|---|
| Policy Evaluation | To V^π | O(n²) per sweep | Prediction |
| Policy Iteration | To π* | Fewer iterations, each expensive | Small MDPs |
| Value Iteration | To V* | O(n²) per sweep | Medium MDPs |

### Common Mistakes

- **Assuming DP works in practice:** DP requires known transitions — most real problems don't have this.
- **Not checking convergence:** Prematurely stopping iteration gives suboptimal policies.
- **Ignoring computational cost:** For large state spaces, DP is infeasible (curse of dimensionality).

---

*Continue to learn about Monte Carlo methods — learning from experience without a model.*
