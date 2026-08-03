---
{
  "title": "Deep Q-Networks (DQN)",
  "description": "Play Atari from pixels: experience replay, target networks and the tricks that made DQN work.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain experience replay",
    "Use target networks to stabilize training",
    "Implement a DQN training loop",
    "Describe the DQN architecture"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-09-deep-q-networks"
  ],
  "prerequisites": [
    "RL-08: Function Approximation"
  ],
  "references": [
    {
      "title": "Reinforcement Learning: An Introduction — Sutton & Barto",
      "url": "http://incompleteideas.net/book/the-book-2nd.html",
      "description": "The canonical RL textbook (free PDF)."
    },
    {
      "title": "Spinning Up in Deep RL — OpenAI",
      "url": "https://spinningup.openai.com/en/latest/",
      "description": "A practitioner-focused deep RL resource with clean implementations."
    },
    {
      "title": "Stable-Baselines3 Documentation",
      "url": "https://stable-baselines3.readthedocs.io/",
      "description": "Reliable RL algorithm implementations in PyTorch."
    },
    {
      "title": "Gymnasium Documentation",
      "url": "https://gymnasium.farama.org/",
      "description": "The standard API for RL environments."
    },
    {
      "title": "RL Course by David Silver",
      "url": "https://www.davidsilver.uk/teaching/",
      "description": "The classic lecture series on RL fundamentals."
    }
  ]
}
---

# RL-09-DEEP-Q-NETWORKS: Deep Q-Networks (DQN)

## Introduction

Play Atari from pixels: experience replay, target networks and the tricks that made DQN work. By the end of this lesson you will be able to: Explain experience replay; Use target networks to stabilize training; Implement a DQN training loop; Describe the DQN architecture.

## Key Concepts

### 1. Explain experience replay

Target: Explain experience replay. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import collections
import random

replay = collections.deque(maxlen=10000)
replay.append((s, a, r, s_next, done))
print("experience replay buffer ready")
```
### 2. Use target networks to stabilize training

Target: Use target networks to stabilize training. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch
import torch.nn as nn

class DQN(nn.Module):
    def __init__(self, n_obs, n_act):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(n_obs, 128), nn.ReLU(), nn.Linear(128, n_act))
    def forward(self, x):
        return self.net(x)

print(DQN(4, 2))
```
### 3. Implement a DQN training loop

Target: Implement a DQN training loop. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Target network: slow copy of the online net
online = DQN(4, 2)
target = DQN(4, 2)
target.load_state_dict(online.state_dict())
print("target net frozen copy")
```
### 4. Describe the DQN architecture

Target: Describe the DQN architecture. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Loss: (r + gamma * max_a Q_target(s') - Q_online(s, a))^2
print("bellman residual squared")
```

## Practice Questions

1. What is the key idea behind "Deep Q-Networks (DQN)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Deep Q-Networks (DQN) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Deep Q-Networks (DQN)"
1. "Provide advanced patterns and performance considerations for Deep Q-Networks (DQN)"

## Key Takeaways

- Master the core ideas of Deep Q-Networks (DQN) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
