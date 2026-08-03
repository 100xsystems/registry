---
{
  "title": "RL in Games",
  "description": "From Atari to AlphaGo: self-play, Monte Carlo tree search, and superhuman play.",
  "type": "lesson",
  "order": 17,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain self-play",
    "Describe Monte Carlo tree search (MCTS)",
    "Combine MCTS with neural nets (AlphaGo)",
    "Understand why games are ideal testbeds"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-17-rl-in-games"
  ],
  "prerequisites": [
    "RL-09: Deep Q-Networks (DQN)"
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

# RL-17-RL-IN-GAMES: RL in Games

## Introduction

From Atari to AlphaGo: self-play, Monte Carlo tree search, and superhuman play. By the end of this lesson you will be able to: Explain self-play; Describe Monte Carlo tree search (MCTS); Combine MCTS with neural nets (AlphaGo); Understand why games are ideal testbeds.

## Key Concepts

### 1. Explain self-play

Target: Explain self-play. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# MCTS: select, expand, simulate, backpropagate
for _ in range(100):
    print("node: select -> expand -> rollout -> backup")
```
### 2. Describe Monte Carlo tree search (MCTS)

Target: Describe Monte Carlo tree search (MCTS). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# UCB in MCTS balances exploration
N = np.array([10, 5])
W = np.array([8, 4])
ucb = W / N + np.sqrt(2 * np.log(N.sum()) / N)
print("MCTS UCB:", ucb.round(3))
```
### 3. Combine MCTS with neural nets (AlphaGo)

Target: Combine MCTS with neural nets (AlphaGo). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("self-play: train against yourself to keep improving")
```
### 4. Understand why games are ideal testbeds

Target: Understand why games are ideal testbeds. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Value + policy network guides the search
value = 0.7
prior = np.array([0.6, 0.4])
print("neural MCTS blends value and policy priors")
```

## Practice Questions

1. What is the key idea behind "RL in Games"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain RL in Games with analogies and real-world examples"
1. "Show me common mistakes beginners make with RL in Games"
1. "Provide advanced patterns and performance considerations for RL in Games"

## Key Takeaways

- Master the core ideas of RL in Games through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
