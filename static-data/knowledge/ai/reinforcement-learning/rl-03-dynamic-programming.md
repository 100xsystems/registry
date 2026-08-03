---
{
  "title": "Dynamic Programming",
  "description": "Solve MDPs exactly with policy evaluation, policy iteration and value iteration.",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Perform policy evaluation",
    "Improve policies with greedy selection",
    "Run value iteration",
    "Understand DP limits with large state spaces"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-02-markov-decision-processes"
  ],
  "prerequisites": [
    "RL-02: Markov Decision Processes"
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

# RL-03-DYNAMIC-PROGRAMMING: Dynamic Programming

## Introduction

Solve MDPs exactly with policy evaluation, policy iteration and value iteration. By the end of this lesson you will be able to: Perform policy evaluation; Improve policies with greedy selection; Run value iteration; Understand DP limits with large state spaces.

## Key Concepts

### 1. Perform policy evaluation

Target: Perform policy evaluation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Policy evaluation: iterative Bellman backup
V = np.zeros(3)
P = np.array([[0.5, 0.5, 0], [0, 0.5, 0.5], [0, 0, 1]])
R = np.array([0, 0, 1.0])
for _ in range(100):
    V = R + 0.9 * P @ V
print("values:", V.round(3))
```
### 2. Improve policies with greedy selection

Target: Improve policies with greedy selection. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Greedy improvement: act optimally under current values
V = np.array([0.1, 0.5, 1.0])
best = int(np.argmax(V))
print("best state:", best)
```
### 3. Run value iteration

Target: Run value iteration. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Value iteration: V <- max over actions of backup
V = np.zeros(4)
rewards = np.array([0, 0, 0, 1.0])
for _ in range(100):
    V = np.maximum(rewards + 0.9 * np.roll(V, 1), rewards + 0.9 * V)
print("value iteration done:", V.round(2))
```
### 4. Understand DP limits with large state spaces

Target: Understand DP limits with large state spaces. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Curse of dimensionality: 10^state_dim grows fast
for d in [4, 8, 12]:
    print(f"states in {d}-dim grid:", 10 ** d)
```

## Practice Questions

1. What is the key idea behind "Dynamic Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dynamic Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dynamic Programming"
1. "Provide advanced patterns and performance considerations for Dynamic Programming"

## Key Takeaways

- Master the core ideas of Dynamic Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
