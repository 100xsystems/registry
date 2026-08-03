---
{
  "title": "Function Approximation",
  "description": "Scale RL beyond tables: approximate Q-values with linear and neural models.",
  "type": "lesson",
  "order": 8,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain why tabular methods do not scale",
    "Approximate Q with a linear model",
    "Describe the deadly triad",
    "Use features for generalization"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-08-function-approximation"
  ],
  "prerequisites": [
    "RL-06: Q-Learning"
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

# RL-08-FUNCTION-APPROXIMATION: Function Approximation

## Introduction

Scale RL beyond tables: approximate Q-values with linear and neural models. By the end of this lesson you will be able to: Explain why tabular methods do not scale; Approximate Q with a linear model; Describe the deadly triad; Use features for generalization.

## Key Concepts

### 1. Explain why tabular methods do not scale

Target: Explain why tabular methods do not scale. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Linear Q-approximation: Q(s,a) = w . phi(s,a)
phi = np.array([1.0, 0.5, -0.2])
w = np.array([0.3, 0.1, 0.4])
print("Q estimate:", round(phi @ w, 3))
```
### 2. Approximate Q with a linear model

Target: Approximate Q with a linear model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Gradient update toward the TD target
w = np.zeros(3)
phi = np.array([1.0, 0.0, 0.0])
target = 1.0
alpha = 0.1
w += alpha * (target - phi @ w) * phi
print("updated weights:", w.round(3))
```
### 3. Describe the deadly triad

Target: Describe the deadly triad. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Neural Q: MLP mapping state to action values
import torch.nn as nn
q_net = nn.Sequential(nn.Linear(4, 64), nn.ReLU(), nn.Linear(64, 2))
print(q_net(torch.randn(1, 4)))
```
### 4. Use features for generalization

Target: Use features for generalization. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Deadly triad: function approx + bootstrapping + off-policy
print("combination can diverge; handled with target nets + replay")
```

## Practice Questions

1. What is the key idea behind "Function Approximation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Function Approximation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Function Approximation"
1. "Provide advanced patterns and performance considerations for Function Approximation"

## Key Takeaways

- Master the core ideas of Function Approximation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
