---
{
  "title": "Policy Gradient Methods",
  "description": "Optimize the policy directly — REINFORCE and the log-probability trick.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain policy parameterization",
    "Derive the REINFORCE update",
    "Implement a policy-gradient loop",
    "Reduce variance with baselines"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-09-deep-q-networks",
    "machine-learning/ml-06-gradient-descent",
    "machine-learning/ml-10-gradient-boosting"
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

# RL-10-POLICY-GRADIENT-METHODS: Policy Gradient Methods

## Introduction

Optimize the policy directly — REINFORCE and the log-probability trick. By the end of this lesson you will be able to: Explain policy parameterization; Derive the REINFORCE update; Implement a policy-gradient loop; Reduce variance with baselines.

## Key Concepts

### 1. Explain policy parameterization

Target: Explain policy parameterization. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

class Policy(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(4, 32), nn.ReLU(), nn.Linear(32, 2))
    def forward(self, x):
        return torch.softmax(self.net(x), dim=-1)

print(Policy())
```
### 2. Derive the REINFORCE update

Target: Derive the REINFORCE update. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# REINFORCE: grad = return * grad log pi(a|s)
log_prob = torch.tensor(-0.5, requires_grad=True)
ret = 1.2
loss = -(ret * log_prob)
loss.backward()
print("gradient:", log_prob.grad)
```
### 3. Implement a policy-gradient loop

Target: Implement a policy-gradient loop. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Baseline reduces variance: grad = (return - b) * log pi
ret, baseline = 1.2, 0.8
print("advantage:", ret - baseline)
```
### 4. Reduce variance with baselines

Target: Reduce variance with baselines. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Policy is stochastic: better exploration than greedy Q
print("samples actions from a distribution")
```

## Practice Questions

1. What is the key idea behind "Policy Gradient Methods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Policy Gradient Methods with analogies and real-world examples"
1. "Show me common mistakes beginners make with Policy Gradient Methods"
1. "Provide advanced patterns and performance considerations for Policy Gradient Methods"

## Key Takeaways

- Master the core ideas of Policy Gradient Methods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
