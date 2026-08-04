---
slug: rl-20-evaluating-rl-agents
title: "Evaluating RL Agents"
description: "Measuring performance and ensuring reproducibility — RL evaluation metrics, benchmarks, and common pitfalls."
order: 20
tags:
  - reinforcement-learning
  - evaluation
  - metrics
  - benchmarks
  - reproducibility
prerequisites:
  - rl-11-actor-critic
knowledge_refs:
  - rl-11-actor-critic
    title: "Actor-Critic Methods"
  - rl-01-what-is-reinforcement-learning
    title: "What Is Reinforcement Learning?"
  - rl-21-roadmap
    title: "Reinforcement Learning Roadmap"
references:
  - title: "Empirical Evaluation of RL Algorithms — Henderson et al."
    url: "https://arxiv.org/abs/1707.03899"
  - title: "Deep RL Eval — How to Evaluate RL Algorithms"
    url: "https://spinningup.openai.com/en/latest/spinningup/spinningup.html"
  - title: "Reproducibility in Deep RL — Andrychowicz et al."
    url: "https://arxiv.org/abs/2005.13509"
  - title: "Gymnasium Benchmark Environments"
    url: "https://gymnasium.farama.org/"
  - title: "RL Baselines Comparison — Practical RL"
    url: "https://arxiv.org/abs/2007.12869"
---

## Evaluating RL Agents

RL evaluation is notoriously difficult. High variance across random seeds, sensitivity to hyperparameters, and non-stationary learning curves make reliable comparison challenging.

### Evaluation Metrics

**Episodic return:** Total reward per episode. The primary metric. Report mean ± standard deviation across seeds.

**Sample efficiency:** How many environment steps to reach a performance threshold. Critical for real-world applications.

**Asymptotic performance:** Final performance after convergence.

**Training stability:** Variance across random seeds. High variance indicates algorithmic instability.

**Wall-clock time:** Total training time. Important for practical deployment.

### Best Practices

**Multiple random seeds:** Run at least 5–10 seeds. Report mean and confidence intervals, not just the best run.

**Statistical tests:** Use paired t-tests or bootstrap confidence intervals to compare algorithms.

**Fixed compute budgets:** Compare algorithms at the same total environment steps, not wall-clock time.

**Learning curves, not final scores:** The full learning trajectory matters — a fast-learning algorithm may be preferable even with lower asymptotic performance.

**Hyperparameter sensitivity:** Report performance across hyperparameter settings, not just the best configuration.

### Benchmark Environments

**Gymnasium:** Standard continuous control (CartPole, Pendulum, MuJoCo tasks).

**Atari 2600:** Pixel-based game playing benchmark.

**MuJoCo:** High-fidelity physics for locomotion and manipulation.

**ML-Agents:** Unity-based 3D environments.

### Common Pitfalls

**Seed sensitivity:** Two algorithms may swap ranking across different seeds. Always use multiple seeds.

**Reporting only the best seed:** Cherry-picking the best run misrepresents performance.

**Ignoring hyperparameter tuning:** Comparing untuned algorithms is meaningless.

**Overfitting to benchmarks:** Performance on standard benchmarks may not transfer to real-world tasks.

### Common Mistakes

- **Single seed evaluation:** Inadequate for reliable comparison.
- **No confidence intervals:** Mean without variance is misleading.
- **Ignoring sample efficiency:** For real-world RL, sample efficiency matters more than asymptotic performance.

---

*Continue to the final lesson — your roadmap for a career in reinforcement learning.*
