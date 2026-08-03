---
{
  "title": "RL for Recommender Systems",
  "description": "Ranking as sequential decisions: contextual bandits and long-term user value.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Frame recommendation as a bandit problem",
    "Explain contextual bandits",
    "Balance short-term engagement with long-term value",
    "Deploy bandits safely with policies"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-19-rl-for-recommendation"
  ],
  "prerequisites": [
    "RL-07: Exploration vs Exploitation"
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

# RL-19-RL-FOR-RECOMMENDATION: RL for Recommender Systems

## Introduction

Ranking as sequential decisions: contextual bandits and long-term user value. By the end of this lesson you will be able to: Frame recommendation as a bandit problem; Explain contextual bandits; Balance short-term engagement with long-term value; Deploy bandits safely with policies.

## Key Concepts

### 1. Frame recommendation as a bandit problem

Target: Frame recommendation as a bandit problem. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Contextual bandit: choose item given user context
context = np.array([0.3, 0.7, 0.2])
item_values = np.array([0.5, 0.9, 0.4])
print("recommend item:", int(np.argmax(item_values)))
```
### 2. Explain contextual bandits

Target: Explain contextual bandits. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Explore: try new items for some users
rng = np.random.default_rng(0)
if rng.random() < 0.1:
    print("explore: random item")
else:
    print("exploit: best item")
```
### 3. Balance short-term engagement with long-term value

Target: Balance short-term engagement with long-term value. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Long-term value via discounting
rewards = np.array([1.0, 0.5, 0.8])
print("discounted value:", round((0.9 ** np.arange(3) * rewards).sum(), 3))
```
### 4. Deploy bandits safely with policies

Target: Deploy bandits safely with policies. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("offline evaluation on logged interactions")
```

## Practice Questions

1. What is the key idea behind "RL for Recommender Systems"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain RL for Recommender Systems with analogies and real-world examples"
1. "Show me common mistakes beginners make with RL for Recommender Systems"
1. "Provide advanced patterns and performance considerations for RL for Recommender Systems"

## Key Takeaways

- Master the core ideas of RL for Recommender Systems through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
