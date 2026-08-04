---
slug: rl-08-function-approximation
title: "Function Approximation"
description: "Scaling RL beyond tabular methods — linear approximation, tile coding, neural networks, and the deadly triad."
order: 8
tags:
  - reinforcement-learning
  - function-approximation
  - linear-methods
  - tile-coding
  - neural-networks
  - deadly-triad
prerequisites:
  - rl-06-q-learning
knowledge_refs:
  - rl-06-q-learning
    title: "Q-Learning"
  - rl-09-deep-q-networks
    title: "Deep Q-Networks"
  - rl-10-policy-gradient-methods
    title: "Policy Gradient Methods"
references:
  - title: "Sutton & Barto — Chapter 9: On-Policy Prediction with Approximation"
    url: "http://incompleteideas.net/book/the-book-2nd.html"
  - title: "Breaking the Deadly Triad with a Target Network — Zhang et al."
    url: "https://proceedings.mlr.press/v139/zhang21y.html"
  - title: "Function Approximation in RL — Kermali"
    url: "https://medium.com/@abdelfatahkermali/function-approximation-in-reinforcement-learning-from-tables-to-neural-networks-63764871d1d9"
  - title: "Tile Coding — Criteo Engineering"
    url: "https://medium.com/criteo-engineering/tile-coding-an-efficient-sparse-coding-method-for-real-valued-data-e787eddf630a"
  - title: "RL: An Introduction — Implementations"
    url: "https://marcinbogdanski.github.io/reinforcement-learning.html"
---

## Function Approximation

Tabular methods can't handle large or continuous state spaces — there are too many states to store values for individually. Function approximation parameterizes value functions, enabling generalization across similar states.

### Linear Function Approximation

Instead of storing V(s) for every state, learn a weight vector **w**:

**v̂(s, w) = w^T x(s) = Σ_i w_i x_i(s)**

Where x(s) is a feature vector representing state s.

**Semi-gradient TD update:**

w_{t+1} = w_t + α[R_{t+1} + γv̂(S_{t+1}, w_t) - v̂(S_t, w_t)] ∇_w v̂(S_t, w_t)

For linear models, ∇_w v̂ = x(s), so the update becomes:

w_{t+1} = w_t + αδ_t x(S_t)

### Tile Coding

A sparse coding method for continuous state spaces:
- Overlay multiple offset grids (tilings) over the state space
- Each tiling activates one tile per state
- Feature vector is binary: 1 for active tiles, 0 otherwise

Benefits: Local generalization (nearby states share tiles), efficient computation, handles continuous states.

### Neural Networks as Approximators

For complex, high-dimensional states (images, text), neural networks parameterize value functions:

**v̂(s, w) = neural_network(s; w)**

The gradient ∇_w v̂ is computed via backpropagation. Semi-gradient updates still apply.

### The Deadly Triad

Sutton and Barto identified three elements that, when combined, can cause divergence:

1. **Function approximation** (parameterized models)
2. **Bootstrapping** (TD-style updates using estimates)
3. **Off-policy learning** (learning about one policy while following another)

Any two are safe. All three together create feedback loops that amplify approximation errors.

**Survival strategies:**
- Target networks (freeze bootstrap targets periodically)
- Experience replay (break data correlation)
- Conservative updates (small learning rates)

### Common Mistakes

- **Ignoring the deadly triad:** Naive combination of function approximation, bootstrapping, and off-policy learning diverges.
- **Poor feature design:** Linear methods are only as good as their features.
- **No regularization:** Overfitting to recent experiences is common with neural approximators.

---

*Continue to learn about Deep Q-Networks — combining Q-learning with deep neural networks.*
