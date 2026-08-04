---
slug: rl-02-markov-decision-processes
title: "Markov Decision Processes"
description: "The mathematical framework for sequential decision-making — states, actions, transitions, rewards, and Bellman equations."
order: 2
tags:
  - reinforcement-learning
  - mdp
  - bellman-equations
  - value-functions
  - discount-factor
prerequisites:
  - rl-01-what-is-reinforcement-learning
knowledge_refs:
  - rl-01-what-is-reinforcement-learning
    title: "What Is Reinforcement Learning?"
  - rl-03-dynamic-programming
    title: "Dynamic Programming"
references:
  - title: "Sutton & Barto — Chapter 3: Finite Markov Decision Processes"
    url: "http://incompleteideas.net/book/the-book-2nd.html"
  - title: "David Silver — RL Course: MDPs"
    url: "https://www.davidsilver.uk/teaching/"
  - title: "Stanford CS234 — Markov Decision Processes"
    url: "https://web.stanford.edu/class/cs234/"
  - title: "OpenAI Spinning Up — Key Concepts in RL"
    url: "https://spinningup.openai.com/en/latest/spinningup/rl_intro.html"
  - title: "Berkeley CS285 — Deep Reinforcement Learning"
    url: "https://rail.eecs.berkeley.edu/deeprlcourse/"
---

## Markov Decision Processes

A Markov Decision Process (MDP) provides the mathematical foundation for reinforcement learning. It formalizes the sequential decision-making problem with states, actions, transitions, and rewards.

### MDP Definition

An MDP is defined by the tuple (S, A, P, R, γ):

- **S:** Set of all possible states
- **A:** Set of all possible actions
- **P(s'|s,a):** Transition probability — probability of reaching state s' from state s after taking action a
- **R(s,a):** Reward function — expected reward for taking action a in state s
- **γ (gamma):** Discount factor (0 ≤ γ ≤ 1) — how much future rewards are valued relative to immediate rewards

### The Markov Property

The future depends only on the present, not the past. Formally:

P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, ...) = P(s_{t+1} | s_t, a_t)

This memoryless property is what makes MDPs tractable — the current state contains all relevant information.

### Return and Discounting

The **return** at time t is the total discounted reward:

G_t = R_{t+1} + γR_{t+2} + γ²R_{t+3} + ... = Σ_{k=0}^∞ γ^k R_{t+k+1}

**Why discount?**
- Prevents infinite sums in continuing tasks
- Models uncertainty about the future
- Makes the agent prefer immediate rewards (practical for real-world applications)

### Value Functions

**State-value function V^π(s):** Expected return starting from state s, following policy π:

V^π(s) = E_π[G_t | S_t = s]

**Action-value function Q^π(s,a):** Expected return starting from state s, taking action a, then following π:

Q^π(s,a) = E_π[G_t | S_t = s, A_t = a]

### Bellman Equations

The Bellman equation decomposes the value of a state into immediate reward plus discounted value of successor states:

**V^π(s) = Σ_a π(a|s) Σ_{s'} P(s'|s,a) [R(s,a) + γV^π(s')]**

**Q^π(s,a) = Σ_{s'} P(s'|s,a) [R(s,a) + γ Σ_{a'} π(a'|s') Q^π(s',a')]**

The **Bellman optimality equation** defines the optimal value:

**V*(s) = max_a Σ_{s'} P(s'|s,a) [R(s,a) + γV*(s')]**

### Common Mistakes

- **Ignoring discount factor:** γ = 0 makes the agent myopic. γ = 1 can cause divergence.
- **Non-Markov states:** If the state doesn't capture all relevant information, learning is unstable.
- **Assuming known transitions:** Most real-world problems have unknown P(s'|s,a), requiring model-free methods.

---

*Continue to learn about dynamic programming — computing optimal policies when the model is known.*
