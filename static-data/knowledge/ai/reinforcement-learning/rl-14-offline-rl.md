---
{
  "title": "Offline Reinforcement Learning",
  "description": "Learn policies from logged data without a live environment — conservative and practical.",
  "type": "lesson",
  "order": 14,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the offline RL setting",
    "Describe distribution shift",
    "Use conservative methods (CQL)",
    "Evaluate offline policies safely"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-14-offline-rl"
  ],
  "prerequisites": [
    "RL-12: PPO & Modern Policy Optimization"
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

# RL-14-OFFLINE-RL: Offline Reinforcement Learning

## Introduction

Learn policies from logged data without a live environment — conservative and practical. By the end of this lesson you will be able to: Explain the offline RL setting; Describe distribution shift; Use conservative methods (CQL); Evaluate offline policies safely.

## Key Concepts

### 1. Explain the offline RL setting

Target: Explain the offline RL setting. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Offline dataset: (s, a, r, s', done) tuples, no new interaction
N = 1000
s = np.random.default_rng(0).normal(size=(N, 4))
print("offline dataset:", s.shape)
```
### 2. Describe distribution shift

Target: Describe distribution shift. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("risk: policy sees states it never visited -> unreliable")
```
### 3. Use conservative methods (CQL)

Target: Use conservative methods (CQL). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Conservative Q: penalize unseen actions
Q = np.array([0.5, 0.8])
penalty = 0.1
print("conservative Q:", Q - penalty)
```
### 4. Evaluate offline policies safely

Target: Evaluate offline policies safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("evaluate via off-policy evaluation or safe rollout")
```

## Practice Questions

1. What is the key idea behind "Offline Reinforcement Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Offline Reinforcement Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Offline Reinforcement Learning"
1. "Provide advanced patterns and performance considerations for Offline Reinforcement Learning"

## Key Takeaways

- Master the core ideas of Offline Reinforcement Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
