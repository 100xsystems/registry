---
{
  "title": "Markov Decision Processes",
  "description": "The formal framework: states, actions, transitions, rewards and the Markov property.",
  "type": "lesson",
  "order": 2,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define an MDP formally (S, A, P, R, gamma)",
    "Explain the Markov property",
    "Define policies, returns and discounting",
    "Write the Bellman expectation equation"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-02-markov-decision-processes"
  ],
  "prerequisites": [
    "RL-01: What Is Reinforcement Learning?"
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

# RL-02-MARKOV-DECISION-PROCESSES: Markov Decision Processes

## Introduction

The formal framework: states, actions, transitions, rewards and the Markov property. By the end of this lesson you will be able to: Define an MDP formally (S, A, P, R, gamma); Explain the Markov property; Define policies, returns and discounting; Write the Bellman expectation equation.

## Key Concepts

### 1. Define an MDP formally (S, A, P, R, gamma)

Target: Define an MDP formally (S, A, P, R, gamma). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
mdp = {
    "states": ["s0", "s1", "s2"],
    "actions": ["left", "right"],
    "discount": 0.9,
}
print(mdp)
```
### 2. Explain the Markov property

Target: Explain the Markov property. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Return with discounting: sum of gamma^t * r_t
rewards = np.array([1.0, 1.0, 1.0])
gamma = 0.9
t = np.arange(len(rewards))
print("discounted return:", round((gamma ** t * rewards).sum(), 3))
```
### 3. Define policies, returns and discounting

Target: Define policies, returns and discounting. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Policy: probability of each action per state
policy = {"s0": {"left": 0.5, "right": 0.5}}
print(policy)
```
### 4. Write the Bellman expectation equation

Target: Write the Bellman expectation equation. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Bellman expectation: V = R + gamma * P * V
P = np.array([[0.7, 0.3], [0.2, 0.8]])
R = np.array([1.0, 2.0])
V = np.linalg.solve(np.eye(2) - 0.9 * P, R)
print("state values:", V.round(3))
```

## Practice Questions

1. What is the key idea behind "Markov Decision Processes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Markov Decision Processes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Markov Decision Processes"
1. "Provide advanced patterns and performance considerations for Markov Decision Processes"

## Key Takeaways

- Master the core ideas of Markov Decision Processes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
