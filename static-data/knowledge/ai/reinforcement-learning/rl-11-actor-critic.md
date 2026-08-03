---
{
  "title": "Actor-Critic Methods",
  "description": "Two networks in harmony: the actor picks actions, the critic judges them with bootstrapped values.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the actor-critic split",
    "Use the critic as a value baseline",
    "Implement a simple actor-critic",
    "Understand A2C and A3C"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-10-policy-gradient-methods",
    "machine-learning/ml-09-ensemble-methods"
  ],
  "prerequisites": [
    "RL-10: Policy Gradient Methods"
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

# RL-11-ACTOR-CRITIC: Actor-Critic Methods

## Introduction

Two networks in harmony: the actor picks actions, the critic judges them with bootstrapped values. By the end of this lesson you will be able to: Explain the actor-critic split; Use the critic as a value baseline; Implement a simple actor-critic; Understand A2C and A3C.

## Key Concepts

### 1. Explain the actor-critic split

Target: Explain the actor-critic split. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch.nn as nn

class ActorCritic(nn.Module):
    def __init__(self):
        super().__init__()
        self.shared = nn.Sequential(nn.Linear(4, 64), nn.ReLU())
        self.actor = nn.Linear(64, 2)
        self.critic = nn.Linear(64, 1)
    def forward(self, x):
        h = self.shared(x)
        return torch.softmax(self.actor(h), -1), self.critic(h)

print(ActorCritic())
```
### 2. Use the critic as a value baseline

Target: Use the critic as a value baseline. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Advantage: r + gamma*V(s') - V(s) — critic bootstraps
r, gamma, v_next, v_now = 1.0, 0.9, 0.5, 0.3
advantage = r + gamma * v_next - v_now
print("advantage:", advantage)
```
### 3. Implement a simple actor-critic

Target: Implement a simple actor-critic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Actor loss: -log pi * advantage. Critic loss: MSE of V
print("two losses, one shared network")
```
### 4. Understand A2C and A3C

Target: Understand A2C and A3C. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# A2C: multiple parallel workers synchronize gradients
print("A2C uses N parallel environments")
```

## Practice Questions

1. What is the key idea behind "Actor-Critic Methods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Actor-Critic Methods with analogies and real-world examples"
1. "Show me common mistakes beginners make with Actor-Critic Methods"
1. "Provide advanced patterns and performance considerations for Actor-Critic Methods"

## Key Takeaways

- Master the core ideas of Actor-Critic Methods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
