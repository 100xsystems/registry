---
{
  "title": "Temporal Difference Learning",
  "description": "Learn from partial episodes with bootstrapping — the idea at the heart of modern RL.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain TD(0) bootstrapping",
    "Update values incrementally after each step",
    "Compare TD to MC (bias-variance)",
    "Use TD for prediction"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-05-temporal-difference-learning"
  ],
  "prerequisites": [
    "RL-04: Monte Carlo Methods"
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

# RL-05-TEMPORAL-DIFFERENCE-LEARNING: Temporal Difference Learning

## Introduction

Learn from partial episodes with bootstrapping — the idea at the heart of modern RL. By the end of this lesson you will be able to: Explain TD(0) bootstrapping; Update values incrementally after each step; Compare TD to MC (bias-variance); Use TD for prediction.

## Key Concepts

### 1. Explain TD(0) bootstrapping

Target: Explain TD(0) bootstrapping. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# TD(0): V(s) <- V(s) + alpha * (r + gamma*V(s') - V(s))
V = np.zeros(3)
alpha, gamma = 0.1, 0.9
r, s_next = 0.0, 1
V[0] += alpha * (r + gamma * V[s_next] - V[0])
print("updated V(s0):", V[0])
```
### 2. Update values incrementally after each step

Target: Update values incrementally after each step. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# TD error: the surprise signal
r, gamma, V_next, V_now = 1.0, 0.9, 0.5, 0.3
td_error = r + gamma * V_next - V_now
print("TD error:", td_error)
```
### 3. Compare TD to MC (bias-variance)

Target: Compare TD to MC (bias-variance). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# TD learns online, MC waits for episode end
print("TD: update every step. MC: update at episode end.")
```
### 4. Use TD for prediction

Target: Use TD for prediction. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# TD: lower variance than MC, biased by bootstrap
print("bias-variance trade-off: TD wins in practice")
```

## Practice Questions

1. What is the key idea behind "Temporal Difference Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Temporal Difference Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Temporal Difference Learning"
1. "Provide advanced patterns and performance considerations for Temporal Difference Learning"

## Key Takeaways

- Master the core ideas of Temporal Difference Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
