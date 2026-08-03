---
{
  "title": "Data Visualization",
  "description": "Build clear, honest charts with Matplotlib and Seaborn — and learn which chart answers which question.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Choose the right chart for a question",
    "Build plots with Matplotlib's object-oriented API",
    "Use Seaborn for statistical plots with one line",
    "Apply principles of clear, honest visualization"
  ],
  "knowledge_refs": [
    "data-science/ds-07-exploratory-data-analysis",
    "data-science/ds-19-communicating-results",
    "data-science/ds-09-statistics-fundamentals"
  ],
  "prerequisites": [
    "DS-07: Exploratory Data Analysis"
  ],
  "references": [
    {
      "title": "Matplotlib Tutorials",
      "url": "https://matplotlib.org/stable/tutorials/index.html",
      "description": "Official step-by-step tutorials, including the Pyplot tutorial and the object-oriented interface."
    },
    {
      "title": "Seaborn User Guide and Tutorial",
      "url": "https://seaborn.pydata.org/tutorial.html",
      "description": "Official tutorial for statistical graphics with clean aesthetics."
    },
    {
      "title": "Python Data Science Handbook — Chapter 4 (Visualization)",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Hands-on Matplotlib/Seaborn coverage with executable examples."
    },
    {
      "title": "Plotly Python Graphing Library",
      "url": "https://plotly.com/python/",
      "description": "Interactive charts for dashboards and web apps."
    }
  ]
}
---

# DS-08-DATA-VISUALIZATION: Data Visualization

## Introduction

A chart's job is to transfer understanding faster than a table can. The two Python libraries you need are **Matplotlib** (the low-level engine — total control, and the foundation everything else uses) and **Seaborn** (a high-level layer that produces statistical plots from pandas DataFrames in one line). This lesson teaches the "which chart for which question" decision first, then the mechanics, then the principles of honesty — because a chart that misleads is worse than no chart at all.

## Key Concepts

### 1. Which chart answers which question

| Question | Chart |
| --- | --- |
| Distribution of one numeric variable | Histogram, KDE, boxplot |
| Distribution by category | Boxplot, violin plot |
| Relationship between two numerics | Scatter plot (+ trend line) |
| Change over time | Line plot |
| Counts of categories | Bar chart |
| Share of a whole | Donut/pie (use sparingly) |
| Relationship among many variables | Heatmap of correlations |

Rule of thumb: if a table of numbers answers the question in one glance, a chart adds nothing. Use charts when they *reduce* cognitive load.

### 2. Matplotlib: the object-oriented API

The modern way to write Matplotlib uses explicit figure and axes objects (not the old `plt.plot` state-machine style):

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(dates, revenue, marker="o", linewidth=2)
ax.set_title("Monthly Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
```

With `ax` you control exactly what you see, compose subplots, and reuse styles — worth the extra keystrokes.

### 3. Seaborn: statistical plots in one line

Seaborn works directly with DataFrames and adds statistical summaries automatically:

```python
import seaborn as sns

sns.histplot(data=df, x="revenue", bins=30)            # distribution
sns.boxplot(data=df, x="plan", y="revenue")            # by category
sns.scatterplot(data=df, x="age", y="revenue", hue="plan")
sns.heatmap(df[["revenue", "age", "orders"]].corr(), annot=True)
sns.regplot(data=df, x="age", y="revenue")             # scatter + trend line
```

`hue=` is the star feature: it splits any plot by a category with zero extra code, which makes three-variable questions trivial.

### 4. Principles of honest visualization

Cole Nussbaumer Knaflic's *Storytelling with Data* framework distills the craft into a few rules [4]:

1. **Start axes at zero** for bar charts — truncated axes exaggerate differences.
2. **Declutter**: remove gridlines that don't help, excess borders, and chart junk.
3. **Use color with intent**: highlight the one thing you want the viewer to see; keep everything else muted.
4. **Label directly** — put text next to the data instead of forcing legend hunting.
5. **Never distort scales** (e.g., log axes without saying so) and never cherry-pick windows that flatter the story.

The same data can support two opposite stories depending on axis ranges — your integrity is on the line in every chart.

### 5. Interactive charts with Plotly

When the audience needs to explore (dashboards, web apps), Plotly provides interactivity: zoom, hover, and tooltips out of the box. The API mirrors what you've learned:

```python
import plotly.express as px

fig = px.line(df, x="month", y="revenue", color="region")
fig.show()
```

## Practice Questions

1. A colleague asks whether users with more orders spend more per order. Which chart(s) do you draw?
2. Write Matplotlib code that renders two subplots: a histogram of `revenue` and a line plot of revenue over time.
3. Why are truncated y-axes considered misleading in bar charts?
4. When would you choose a boxplot over a histogram?

## LLM Prompts for Deeper Understanding

1. "Show me a chart-type decision tree for tabular data questions."
2. "Critique this chart for honesty: what could make it misleading?"
3. "How do I make publication-quality Matplotlib charts with minimal code?"

## Key Takeaways

- Choose the chart by the question: distribution, relationship, trend, counts.
- Use Matplotlib's object-oriented API (`fig, ax = plt.subplots()`).
- Seaborn gives statistical plots from DataFrames in one line, with `hue=` for categories.
- Honesty rules: zero-based bars, decluttered, purposeful color, direct labels.
- Plotly for interactive, exploratory charts.

## Footnotes & Attribution

1. Matplotlib documentation, *Tutorials*. [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)
2. Seaborn documentation, *User Guide and Tutorial*. [https://seaborn.pydata.org/tutorial.html](https://seaborn.pydata.org/tutorial.html)
3. Jake VanderPlas, *Python Data Science Handbook*, Ch. 4. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
4. Cole Nussbaumer Knaflic, *Storytelling with Data* — principles summarized via the official blog. [https://www.storytellingwithdata.com/blog](https://www.storytellingwithdata.com/blog)
5. Plotly documentation, *Python Graphing Library*. [https://plotly.com/python/](https://plotly.com/python/)
