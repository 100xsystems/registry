---
{
  "title": "Communicating Results",
  "description": "The analysis only matters if it changes decisions. Learn to write, present and defend findings clearly.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Structure a findings memo for decision-makers",
    "Pair every claim with its uncertainty",
    "Design a clean, honest dashboard",
    "Answer objections with pre-registered evidence"
  ],
  "knowledge_refs": [
    "data-science/ds-19-communicating-results"
  ],
  "prerequisites": [
    "DS-18: Model Evaluation Metrics"
  ],
  "references": [
    {
      "title": "Python for Data Analysis — Wes McKinney",
      "url": "https://wesmckinney.com/book/",
      "description": "The definitive guide to pandas, NumPy and the PyData stack."
    },
    {
      "title": "Pandas User Guide",
      "url": "https://pandas.pydata.org/docs/user_guide/index.html",
      "description": "Official documentation for the pandas data-analysis library."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Kaggle Learn — Data Science",
      "url": "https://www.kaggle.com/learn",
      "description": "Hands-on micro-courses covering pandas, EDA and modeling."
    },
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "Authoritative guide to the Python machine-learning toolbox."
    }
  ]
}
---

# DS-19-COMMUNICATING-RESULTS: Communicating Results

## Introduction

The analysis only matters if it changes decisions. Learn to write, present and defend findings clearly. By the end of this lesson you will be able to: Structure a findings memo for decision-makers; Pair every claim with its uncertainty; Design a clean, honest dashboard; Answer objections with pre-registered evidence.

## Key Concepts

### 1. Structure a findings memo for decision-makers

Target: Structure a findings memo for decision-makers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
memo = {
    "question": "Does the new onboarding increase activation?",
    "finding": "Activation +4.2pp (95% CI [1.9, 6.5])",
    "caveat": "Early adopters only; revisit at 8 weeks",
    "next_step": "Roll out to 25% and monitor churn",
}
for k, v in memo.items():
    print(f"{k}: {v}")
```
### 2. Pair every claim with its uncertainty

Target: Pair every claim with its uncertainty. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Report uncertainty, not just point estimates
lift = np.array([0.02, 0.05, 0.06, 0.03, 0.04])
print(f"mean lift {lift.mean()*100:.1f}pp +/- {1.96*lift.std(ddof=1)/np.sqrt(lift.size)*100:.1f}pp")
```
### 3. Design a clean, honest dashboard

Target: Design a clean, honest dashboard. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import pandas as pd

# A dashboard starts with a clear metric definition
metrics = {
    "activation_rate": "activated / signed_up (7d)",
    "retention_w4": "active at week 4 / signed_up",
    "nps": "promoters - detractors (0-10 scale)",
}
print(pd.DataFrame(metrics.items(), columns=["metric", "definition"]))
```
### 4. Answer objections with pre-registered evidence

Target: Answer objections with pre-registered evidence. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
def pre_register(question, hypothesis, metric, analysis):
    return {"question": question, "hypothesis": hypothesis, "metric": metric, "analysis": analysis}

plan = pre_register(
    "Does X move retention?", "Retention +1pp", "retention_w4", "two-sample t-test, alpha=0.05"
)
print(plan)
```

## Practice Questions

1. What is the key idea behind "Communicating Results"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Communicating Results with analogies and real-world examples"
1. "Show me common mistakes beginners make with Communicating Results"
1. "Provide advanced patterns and performance considerations for Communicating Results"

## Key Takeaways

- Master the core ideas of Communicating Results through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
