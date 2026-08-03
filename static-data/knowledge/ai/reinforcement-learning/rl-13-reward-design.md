---
{
  "title": "Reward Design",
  "description": "Rewards shape everything: sparse vs dense, shaping and the specification problem.",
  "type": "lesson",
  "order": 13,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design rewards that express the true goal",
    "Handle sparse rewards with shaping",
    "Avoid reward hacking",
    "Use reward shaping theorems safely"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-12-proximal-policy-optimization",
    "ai-agents/agents-17-agent-design-patterns"
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

# RL-13-REWARD-DESIGN: Reward Design

## Introduction

Rewards shape everything: sparse vs dense, shaping and the specification problem. By the end of this lesson you will be able to: Design rewards that express the true goal; Handle sparse rewards with shaping; Avoid reward hacking; Use reward shaping theorems safely.

## Key Concepts

### 1. Design rewards that express the true goal

Target: Design rewards that express the true goal. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Sparse: reward only at the goal
sparse = np.zeros(100)
sparse[-1] = 1.0
print("sparse returns nonzero only at end")
```
### 2. Handle sparse rewards with shaping

Target: Handle sparse rewards with shaping. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Dense shaping: small progress rewards at every step
progress = np.linspace(0, 1, 100) * 0.01
print("shaped reward example:", progress[:3])
```
### 3. Avoid reward hacking

Target: Avoid reward hacking. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
hacks = ["agent finds loopholes", "exploits simulator bugs", "games the metric"]
for h in hacks:
    print(f"- {h}")
```
### 4. Use reward shaping theorems safely

Target: Use reward shaping theorems safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Shaping must not change the optimal policy (potential-based)
Phi = np.array([0.0, 0.5, 1.0])  # potential per state
gamma = 0.9
shaping = gamma * np.roll(Phi, -1) - Phi
print("potential shaping:", shaping.round(2))
```

## Practice Questions

1. What is the key idea behind "Reward Design"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Reward Design with analogies and real-world examples"
1. "Show me common mistakes beginners make with Reward Design"
1. "Provide advanced patterns and performance considerations for Reward Design"

## Key Takeaways

- Master the core ideas of Reward Design through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
