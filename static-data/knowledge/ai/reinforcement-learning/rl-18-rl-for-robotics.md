---
{
  "title": "RL for Robotics",
  "description": "Physical agents learning motor skills: sim-to-real, reward shaping and safety in the real world.",
  "type": "lesson",
  "order": 18,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Describe the challenges of learning on real hardware",
    "Use simulation with domain randomization",
    "Explain sim-to-real transfer",
    "Apply safety constraints in control"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-17-rl-in-games"
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

# RL-18-RL-FOR-ROBOTICS: RL for Robotics

## Introduction

Physical agents learning motor skills: sim-to-real, reward shaping and safety in the real world. By the end of this lesson you will be able to: Describe the challenges of learning on real hardware; Use simulation with domain randomization; Explain sim-to-real transfer; Apply safety constraints in control.

## Key Concepts

### 1. Describe the challenges of learning on real hardware

Target: Describe the challenges of learning on real hardware. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Domain randomization: randomize physics in sim
mass = np.random.default_rng(0).uniform(0.8, 1.2)
friction = np.random.default_rng(0).uniform(0.5, 1.0)
print("randomized mass:", round(mass, 2), "friction:", round(friction, 2))
```
### 2. Use simulation with domain randomization

Target: Use simulation with domain randomization. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("safety: constraint satisfaction before pure reward")
```
### 3. Explain sim-to-real transfer

Target: Explain sim-to-real transfer. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Action limits keep the robot stable
action = np.clip(0.9, -1.0, 1.0)
print("clipped action:", action)
```
### 4. Apply safety constraints in control

Target: Apply safety constraints in control. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("sim-to-real: train in sim, transfer with randomization")
```

## Practice Questions

1. What is the key idea behind "RL for Robotics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain RL for Robotics with analogies and real-world examples"
1. "Show me common mistakes beginners make with RL for Robotics"
1. "Provide advanced patterns and performance considerations for RL for Robotics"

## Key Takeaways

- Master the core ideas of RL for Robotics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
