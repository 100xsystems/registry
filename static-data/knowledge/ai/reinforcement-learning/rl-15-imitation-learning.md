---
{
  "title": "Imitation Learning",
  "description": "Learn from demonstrations: behavioral cloning and DAgger for expert-like behavior.",
  "type": "lesson",
  "order": 15,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain behavioral cloning",
    "Describe the covariate shift problem",
    "Use DAgger to correct drift",
    "Combine imitation with RL"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-14-offline-rl"
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

# RL-15-IMITATION-LEARNING: Imitation Learning

## Introduction

Learn from demonstrations: behavioral cloning and DAgger for expert-like behavior. By the end of this lesson you will be able to: Explain behavioral cloning; Describe the covariate shift problem; Use DAgger to correct drift; Combine imitation with RL.

## Key Concepts

### 1. Explain behavioral cloning

Target: Explain behavioral cloning. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Behavioral cloning: supervised learning on (obs, action)
obs = np.random.default_rng(0).normal(size=(500, 4))
actions = np.random.default_rng(1).randint(0, 2, size=500)
print("demo dataset:", obs.shape, actions.shape)
```
### 2. Describe the covariate shift problem

Target: Describe the covariate shift problem. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression().fit(obs, actions)
print("clone accuracy:", round(clf.score(obs, actions), 3))
```
### 3. Use DAgger to correct drift

Target: Use DAgger to correct drift. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("drift: small errors compound as the agent leaves the demo distribution")
```
### 4. Combine imitation with RL

Target: Combine imitation with RL. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# DAgger: query the expert on visited states
print("aggregate: add expert labels for states the learner visits")
```

## Practice Questions

1. What is the key idea behind "Imitation Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Imitation Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Imitation Learning"
1. "Provide advanced patterns and performance considerations for Imitation Learning"

## Key Takeaways

- Master the core ideas of Imitation Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
