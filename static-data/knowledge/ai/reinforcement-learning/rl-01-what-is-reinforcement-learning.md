---
{
  "title": "What Is Reinforcement Learning?",
  "description": "Agents, environments, rewards and the trial-and-error loop that powers RL.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define the agent-environment-reward loop",
    "Contrast RL with supervised and unsupervised learning",
    "Name the core RL problems and applications",
    "Describe the exploration-exploitation tension"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-01-what-is-reinforcement-learning"
  ],
  "prerequisites": [
    "ML-01: What Is Machine Learning?"
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

# RL-01-WHAT-IS-REINFORCEMENT-LEARNING: What Is Reinforcement Learning?

## Introduction

Agents, environments, rewards and the trial-and-error loop that powers RL. By the end of this lesson you will be able to: Define the agent-environment-reward loop; Contrast RL with supervised and unsupervised learning; Name the core RL problems and applications; Describe the exploration-exploitation tension.

## Key Concepts

### 1. Define the agent-environment-reward loop

Target: Define the agent-environment-reward loop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
loop = {
    "agent": "takes actions",
    "environment": "responds with next state + reward",
    "goal": "maximize cumulative reward",
}
print(loop)
```
### 2. Contrast RL with supervised and unsupervised learning

Target: Contrast RL with supervised and unsupervised learning. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import gymnasium as gym

env = gym.make("CartPole-v1")
obs, info = env.reset()
print("observation:", obs)
```
### 3. Name the core RL problems and applications

Target: Name the core RL problems and applications. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Reward signal drives learning
r = np.array([0.0, 0.0, 0.0, 1.0, 0.0])
print("total return:", r.sum())
```
### 4. Describe the exploration-exploitation tension

Target: Describe the exploration-exploitation tension. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("supervised: learn from labels. RL: learn from outcomes.")
```

## Practice Questions

1. What is the key idea behind "What Is Reinforcement Learning?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Reinforcement Learning? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Reinforcement Learning?"
1. "Provide advanced patterns and performance considerations for What Is Reinforcement Learning?"

## Key Takeaways

- Master the core ideas of What Is Reinforcement Learning? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
