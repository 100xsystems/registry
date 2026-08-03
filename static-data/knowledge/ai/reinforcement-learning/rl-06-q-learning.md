---
{
  "title": "Q-Learning",
  "description": "Off-policy control: learn action values with Q-learning and watch agents improve from scratch.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define the Q-function",
    "Explain the Q-learning update",
    "Implement a tabular Q-learning agent",
    "Describe off-policy learning"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-05-temporal-difference-learning"
  ],
  "prerequisites": [
    "RL-05: Temporal Difference Learning"
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

# RL-06-Q-LEARNING: Q-Learning

## Introduction

Off-policy control: learn action values with Q-learning and watch agents improve from scratch. By the end of this lesson you will be able to: Define the Q-function; Explain the Q-learning update; Implement a tabular Q-learning agent; Describe off-policy learning.

## Key Concepts

### 1. Define the Q-function

Target: Define the Q-function. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Q-learning update
Q = np.zeros((4, 2))
alpha, gamma = 0.1, 0.9
s, a, r, s_next = 0, 0, 0.0, 1
Q[s, a] += alpha * (r + gamma * Q[s_next].max() - Q[s, a])
print("Q table:", Q)
```
### 2. Explain the Q-learning update

Target: Explain the Q-learning update. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Greedy action from Q
Q = np.array([[0.1, 0.9], [0.5, 0.2]])
action = int(np.argmax(Q[0]))
print("best action in s0:", action)
```
### 3. Implement a tabular Q-learning agent

Target: Implement a tabular Q-learning agent. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Epsilon-greedy: explore with prob epsilon
rng = np.random.default_rng(0)
eps = 0.1
chosen = rng.choice(2) if rng.random() < eps else int(np.argmax(Q[0]))
print("chosen action:", chosen)
```
### 4. Describe off-policy learning

Target: Describe off-policy learning. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Learning rate decay: big steps early, fine later
for t in range(100):
    alpha = 1.0 / (1 + t)
print("final alpha:", round(alpha, 4))
```

## Practice Questions

1. What is the key idea behind "Q-Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Q-Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Q-Learning"
1. "Provide advanced patterns and performance considerations for Q-Learning"

## Key Takeaways

- Master the core ideas of Q-Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
