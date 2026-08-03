---
{
  "title": "Monte Carlo Methods",
  "description": "Learn from complete episodes: average returns to estimate state values without a model.",
  "type": "lesson",
  "order": 4,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain episode-based learning",
    "Estimate values with first-visit and every-visit MC",
    "Implement MC prediction",
    "Understand variance of MC returns"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-04-monte-carlo-methods"
  ],
  "prerequisites": [
    "RL-03: Dynamic Programming"
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

# RL-04-MONTE-CARLO-METHODS: Monte Carlo Methods

## Introduction

Learn from complete episodes: average returns to estimate state values without a model. By the end of this lesson you will be able to: Explain episode-based learning; Estimate values with first-visit and every-visit MC; Implement MC prediction; Understand variance of MC returns.

## Key Concepts

### 1. Explain episode-based learning

Target: Explain episode-based learning. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# One episode: (state, reward) pairs
episode = [("s0", 0.0), ("s1", 0.0), ("s2", 1.0)]
returns = 0.0
for s, r in reversed(episode):
    returns = r + 0.9 * returns
    print(s, "return so far:", round(returns, 2))
```
### 2. Estimate values with first-visit and every-visit MC

Target: Estimate values with first-visit and every-visit MC. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# MC value estimate: average of sampled returns
returns_s0 = np.array([1.0, 0.9, 1.1])
print("V(s0) ~", round(returns_s0.mean(), 3))
```
### 3. Implement MC prediction

Target: Implement MC prediction. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# First-visit vs every-visit
visits = [1.0, 0.9, 1.1, 0.8]
first = visits[0]
print("first-visit return:", first, "| every-visit mean:", round(np.mean(visits), 3))
```
### 4. Understand variance of MC returns

Target: Understand variance of MC returns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# High variance: many episodes needed for stable estimates
rng = np.random.default_rng(0)
samples = rng.normal(1.0, 2.0, 1000)
print("MC mean:", round(samples.mean(), 3), "+-", round(samples.std(ddof=1) / np.sqrt(1000), 3))
```

## Practice Questions

1. What is the key idea behind "Monte Carlo Methods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Monte Carlo Methods with analogies and real-world examples"
1. "Show me common mistakes beginners make with Monte Carlo Methods"
1. "Provide advanced patterns and performance considerations for Monte Carlo Methods"

## Key Takeaways

- Master the core ideas of Monte Carlo Methods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
