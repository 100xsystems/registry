---
{
  "title": "PPO & Modern Policy Optimization",
  "description": "Stable, sample-efficient updates with clipping — the default choice in modern RL.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the PPO clipped objective",
    "Use importance sampling ratios",
    "Run PPO with Stable-Baselines3",
    "Tune PPO hyperparameters"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-11-actor-critic",
    "llm-engineering/llm-16-cost-optimization",
    "mlops/mlops-19-cost-and-performance"
  ],
  "prerequisites": [
    "RL-11: Actor-Critic Methods"
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

# RL-12-PROXIMAL-POLICY-OPTIMIZATION: PPO & Modern Policy Optimization

## Introduction

Stable, sample-efficient updates with clipping — the default choice in modern RL. By the end of this lesson you will be able to: Explain the PPO clipped objective; Use importance sampling ratios; Run PPO with Stable-Baselines3; Tune PPO hyperparameters.

## Key Concepts

### 1. Explain the PPO clipped objective

Target: Explain the PPO clipped objective. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

# Importance ratio: how likely under new vs old policy
ratio = torch.tensor([1.1, 0.9, 1.2])
print("ratios:", ratio)
```
### 2. Use importance sampling ratios

Target: Use importance sampling ratios. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Clipping limits the update: min(ratio*A, clip(ratio, 0.8, 1.2)*A)
advantage = torch.tensor([1.0, 0.5, 0.2])
clipped = torch.clamp(ratio, 0.8, 1.2)
obj = torch.min(ratio * advantage, clipped * advantage)
print("objective:", obj)
```
### 3. Run PPO with Stable-Baselines3

Target: Run PPO with Stable-Baselines3. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from stable_baselines3 import PPO

model = PPO("MlpPolicy", "CartPole-v1", verbose=0)
model.learn(total_timesteps=50_000)
print("PPO trained")
```
### 4. Tune PPO hyperparameters

Target: Tune PPO hyperparameters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from stable_baselines3 import PPO

model = PPO("MlpPolicy", "CartPole-v1", learning_rate=3e-4, n_steps=2048, verbose=0)
print("defaults are sensible; tune lr and batch carefully")
```

## Practice Questions

1. What is the key idea behind "PPO & Modern Policy Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain PPO & Modern Policy Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with PPO & Modern Policy Optimization"
1. "Provide advanced patterns and performance considerations for PPO & Modern Policy Optimization"

## Key Takeaways

- Master the core ideas of PPO & Modern Policy Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
