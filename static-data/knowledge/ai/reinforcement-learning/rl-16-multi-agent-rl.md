---
{
  "title": "Multi-Agent Reinforcement Learning",
  "description": "Multiple learners interacting: cooperation, competition, and the games they create.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Describe multi-agent settings (cooperative, competitive, mixed)",
    "Explain non-stationarity",
    "Use independent learners",
    "Discuss centralized training, decentralized execution"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-15-imitation-learning",
    "ai-agents/agents-06-multi-agent-systems",
    "ai-agents/agents-02-agent-architecture"
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

# RL-16-MULTI-AGENT-RL: Multi-Agent Reinforcement Learning

## Introduction

Multiple learners interacting: cooperation, competition, and the games they create. By the end of this lesson you will be able to: Describe multi-agent settings (cooperative, competitive, mixed); Explain non-stationarity; Use independent learners; Discuss centralized training, decentralized execution.

## Key Concepts

### 1. Describe multi-agent settings (cooperative, competitive, mixed)

Target: Describe multi-agent settings (cooperative, competitive, mixed). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
settings = {
    "cooperative": "shared reward",
    "competitive": "zero-sum",
    "mixed": "social dilemmas",
}
print(settings)
```
### 2. Explain non-stationarity

Target: Explain non-stationarity. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("non-stationary: the environment changes as others learn")
```
### 3. Use independent learners

Target: Use independent learners. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Independent Q-learners: each learns its own table
Q_a = np.zeros((4, 2))
Q_b = np.zeros((4, 2))
print("independent learners")
```
### 4. Discuss centralized training, decentralized execution

Target: Discuss centralized training, decentralized execution. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("CTDE: train together centrally, act with local info")
```

## Practice Questions

1. What is the key idea behind "Multi-Agent Reinforcement Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Multi-Agent Reinforcement Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Multi-Agent Reinforcement Learning"
1. "Provide advanced patterns and performance considerations for Multi-Agent Reinforcement Learning"

## Key Takeaways

- Master the core ideas of Multi-Agent Reinforcement Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
