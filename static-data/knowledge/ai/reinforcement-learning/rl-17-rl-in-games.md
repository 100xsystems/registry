---
slug: rl-17-rl-in-games
title: "RL in Games"
description: "From Atari to StarCraft — AlphaGo, AlphaStar, OpenAI Five, and the game environments that drive RL research."
order: 17
tags:
  - reinforcement-learning
  - games
  - alpha-go
  - alphastar
  - openai-five
  - gymnasium
prerequisites:
  - rl-16-multi-agent-rl
knowledge_refs:
  - slug: rl-16-multi-agent-rl
    title: "Multi-Agent Reinforcement Learning"
  - slug: rl-09-deep-q-networks
    title: "Deep Q-Networks"
  - slug: rl-18-rl-for-robotics
    title: "RL for Robotics"
references:
  - title: "AlphaGo — Mastering Go with Deep Neural Networks (Nature)"
    url: "https://www.nature.com/articles/nature16961"
  - title: "AlphaStar — Grandmaster Level in StarCraft II (Nature)"
    url: "https://www.nature.com/articles/s41586-019-1724-z"
  - title: "OpenAI Five — Dota 2 with Large Scale Deep RL"
    url: "https://cdn.openai.com/dota-2.pdf"
  - title: "Gymnasium Documentation"
    url: "https://gymnasium.farama.org/"
  - title: "AlphaGo Zero — Starting from Scratch (DeepMind)"
    url: "https://deepmind.google/blog/alphago-zero-starting-from-scratch/"
---
## RL in Games

Games have been the proving ground for RL breakthroughs. From Atari to Go to Dota 2, game environments provide the complexity, clear objectives, and simulation capability needed to push RL research forward.

### AlphaGo and AlphaZero

**AlphaGo (2016):** Combined deep neural networks (policy + value) with Monte Carlo Tree Search (MCTS). Defeated world champion Lee Sedol 4–1.

**AlphaGo Zero:** Learned entirely from self-play — no human data. surpassed AlphaGo within 40 hours by discovering novel strategies.

**AlphaZero:** Generalized to chess and shogi. Mastered all three games from scratch using only self-play RL + MCTS.

### AlphaStar

**StarCraft II (2019):** Achieved Grandmaster level across all three races. Key innovations:
- Multi-agent league training (diverse opponents prevent cyclic strategies)
- Hierarchical action space (high-level strategic decisions → low-level micro)
- Partial observability (imperfect information)

### OpenAI Five

**Dota 2 (2019):** Trained 5v5 team play using massive distributed PPO:
- Tens of thousands of CPU cores + thousands of GPUs
- Hundreds of years of gameplay per day
- Emergent teamwork, drafting, and long-term strategy

### Gymnasium (Standard Environment API)

The Farama Foundation's Gymnasium (successor to OpenAI Gym) provides the standard Python API for RL environments:

```python
env = gymnasium.make('CartPole-v1')
obs, info = env.reset()
action = env.action_space.sample()
obs, reward, terminated, truncated, info = env.step(action)
```

Standard interface: `reset()`, `step()`, `observation_space`, `action_space`.

### Why Games Matter for RL

- **Simulation:** Unlimited, safe, fast environment interaction
- **Clear metrics:** Win/loss, score — unambiguous evaluation
- **Scalability:** Massive parallelization possible
- **Complexity:** Games capture strategic reasoning, planning, and multi-agent dynamics

### Common Mistakes

- **Overfitting to games:** Success in games doesn't guarantee real-world transfer.
- **Ignoring sample efficiency:** Games allow billions of samples; real-world RL can't.
- **Dismissing game research:** Games drive fundamental RL algorithmic advances.

---

*Continue to learn about RL for robotics — sim-to-real transfer and real-world RL.*
