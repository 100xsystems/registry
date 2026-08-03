---
{
  "title": "Evaluating RL Agents",
  "description": "Measures beyond total reward: returns curves, sample efficiency and robustness.",
  "type": "lesson",
  "order": 20,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read learning curves correctly",
    "Report mean and variance across seeds",
    "Measure sample efficiency",
    "Test robustness to environment changes"
  ],
  "knowledge_refs": [
    "ai-agents/agents-12-evaluating-agents",
    "reinforcement-learning/rl-19-rl-for-recommendation",
    "ai-agents/agents-01-what-are-ai-agents"
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

# RL-20-EVALUATING-RL-AGENTS: Evaluating RL Agents

## Introduction

Measures beyond total reward: returns curves, sample efficiency and robustness. By the end of this lesson you will be able to: Read learning curves correctly; Report mean and variance across seeds; Measure sample efficiency; Test robustness to environment changes.

## Key Concepts

### 1. Read learning curves correctly

Target: Read learning curves correctly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Learning curves: mean + std band over seeds
seeds = np.random.default_rng(0).normal(size=(5, 100))
mean = seeds.mean(axis=0)
std = seeds.std(axis=0)
print("final mean:", round(mean[-1], 2), "+-", round(std[-1], 2))
```
### 2. Report mean and variance across seeds

Target: Report mean and variance across seeds. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Sample efficiency: return per timestep
return_per_step = 0.01
print("after 1M steps:", int(1_000_000 * return_per_step))
```
### 3. Measure sample efficiency

Target: Measure sample efficiency. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Robustness: perturb the environment
for noise in [0.0, 0.1, 0.5]:
    print(f"noise {noise}: perturbed reward {round(1.0 - noise * 0.5, 2)}")
```
### 4. Test robustness to environment changes

Target: Test robustness to environment changes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("always report multiple seeds, not one lucky run")
```

## Practice Questions

1. What is the key idea behind "Evaluating RL Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Evaluating RL Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with Evaluating RL Agents"
1. "Provide advanced patterns and performance considerations for Evaluating RL Agents"

## Key Takeaways

- Master the core ideas of Evaluating RL Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
