---
{
  "title": "Data Visualization",
  "description": "Choose the right chart, encode data honestly, and tell a story with matplotlib and seaborn.",
  "type": "lesson",
  "order": 8,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Pick the right chart for the question",
    "Build line, bar and scatter plots with matplotlib",
    "Add grouping with seaborn",
    "Avoid common misleading-visualization traps"
  ],
  "knowledge_refs": [
    "data-science/ds-08-data-visualization"
  ],
  "prerequisites": [
    "DS-07: Exploratory Data Analysis"
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

# DS-08-DATA-VISUALIZATION: Data Visualization

## Introduction

Choose the right chart, encode data honestly, and tell a story with matplotlib and seaborn. By the end of this lesson you will be able to: Pick the right chart for the question; Build line, bar and scatter plots with matplotlib; Add grouping with seaborn; Avoid common misleading-visualization traps.

## Key Concepts

### 1. Pick the right chart for the question

Target: Pick the right chart for the question. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 24, 18, 32]
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker="o")
plt.title("Revenue by quarter")
plt.xlabel("Q")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
```
### 2. Build line, bar and scatter plots with matplotlib

Target: Build line, bar and scatter plots with matplotlib. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import matplotlib.pyplot as plt

cats = ["free", "pro", "team"]
vals = [1200, 340, 95]
plt.bar(cats, vals, color="#572EFF")
plt.title("Signups by plan")
plt.show()
```
### 3. Add grouping with seaborn

Target: Add grouping with seaborn. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import seaborn as sns

penguins = sns.load_dataset("penguins")
sns.scatterplot(data=penguins.dropna(), x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.title("Bill shape by species")
plt.show()
```
### 4. Avoid common misleading-visualization traps

Target: Avoid common misleading-visualization traps. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import matplotlib.pyplot as plt

# A fixed y-axis so small differences are not exaggerated
cats = ["A", "B"]
vals = [100, 102]
plt.bar(cats, vals, color="#572EFF")
plt.ylim(0, 120)   # honest scale
plt.show()
```

## Practice Questions

1. What is the key idea behind "Data Visualization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Visualization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Visualization"
1. "Provide advanced patterns and performance considerations for Data Visualization"

## Key Takeaways

- Master the core ideas of Data Visualization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
