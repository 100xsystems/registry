---
{
  "title": "Exploratory Data Analysis",
  "description": "Use summaries and plots to interrogate a dataset before any modeling — find patterns, outliers and bugs.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Profile variables with univariate summaries",
    "Explore relationships between variables",
    "Spot outliers, missingness and data bugs through plots",
    "Use EDA to inform modeling decisions"
  ],
  "knowledge_refs": [
    "data-science/ds-05-pandas-dataframes",
    "data-science/ds-08-data-visualization",
    "data-science/ds-12-correlation-and-causation"
  ],
  "prerequisites": [
    "DS-06: Data Cleaning & Wrangling"
  ],
  "references": [
    {
      "title": "EDA with pandas — Kaggle Learn",
      "url": "https://www.kaggle.com/learn/data-visualization",
      "description": "Kaggle's hands-on EDA and visualization micro-course."
    },
    {
      "title": "Exploratory Data Analysis — Towards Data Science (reference)",
      "url": "https://towardsdatascience.com/exploratory-data-analysis-eda-a-practical-guide-and-templates-for-structured-data-ab99bfecc654",
      "description": "A practical EDA template with code you can adapt."
    },
    {
      "title": "Python for Data Analysis — Wes McKinney (Chapter 9)",
      "url": "https://wesmckinney.com/book/plotting-and-visualization",
      "description": "Plotting and EDA patterns from the pandas creator."
    },
    {
      "title": "DataExplorer / pandas-profiling (tooling reference)",
      "url": "https://github.com/ydataai/ydata-profiling",
      "description": "Automated EDA reports — useful as a first pass, not a substitute for thinking."
    }
  ]
}
---

# DS-07-EXPLORATORY-DATA-ANALYSIS: Exploratory Data Analysis

## Introduction

Exploratory Data Analysis (EDA) is the step where you *meet* your data: summarizing each variable, looking at relationships, and hunting for problems before you commit to a model. The term was popularized by statistician John Tukey, whose core message was: **look at the data before you theorize about it.** EDA's goals are (1) check the data is what you think it is, (2) find patterns worth modeling, and (3) surface bugs that would silently corrupt results. It is quick to learn and endlessly valuable.

## Key Concepts

### 1. Univariate profiling: each variable alone

For every column, ask: *What type is it? What's the distribution? How much is missing?*

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df.describe())                        # numeric: count, mean, std, min, quartiles, max
print(df["plan"].value_counts(dropna=False)) # categorical: counts per level
print(df.isna().sum())                       # missingness
```

Three things `describe()` will tell you instantly:

- **Range** — is the max absurd (`9999999`)? Outlier alert.
- **Count vs rows** — a count lower than `len(df)` means missing values.
- **Mean vs median** — a mean far above the median signals a right-skewed distribution, which matters for modeling choices later.

### 2. Bivariate exploration: relationships

Now ask how variables move together. The classic quick checks:

```python
print(df.groupby("plan")["revenue"].agg(["mean", "median", "count"]))
print(df[["revenue", "age", "orders"]].corr())
```

Grouped means (split-apply-combine from the pandas lesson) reveal differences across categories; the correlation matrix reveals linear relationships at a glance. Both generate *hypotheses* ("pro-plan users spend more") that you will test properly in the statistics lessons.

### 3. Plotting the key views

Four plots cover most EDA:

```python
import matplotlib.pyplot as plt

df["revenue"].hist(bins=30)              # distribution of one variable
plt.show()

df.boxplot(column="revenue", by="plan")  # distribution by category (outliers!)
plt.show()

df.plot.scatter(x="age", y="revenue")    # relationship between two numeric vars
plt.show()

df["plan"].value_counts().plot.bar()     # category counts
plt.show()
```

These are quick, disposable plots — the polished, decision-facing versions come in the visualization lesson.

### 4. Using EDA to catch bugs

This is EDA's hidden superpower. Consider a `date` column: plot orders by month and a mysterious drop appears — is it real seasonality or a data-collection gap? A histogram with a pile of values at exactly `0` might mean "0" was used as a stand-in for missing. A scatter plot with a perfectly straight diagonal often means the same column got copied into itself during a merge.

Every plot you draw is also a test you run. If the plot looks "wrong," investigate *before* modeling — the model will happily learn from your bugs.

### 5. Automating the first pass

Tools like `ydata-profiling` (formerly pandas-profiling) generate a full HTML EDA report from one line:

```python
from ydata_profiling import ProfileReport
ProfileReport(df).to_file("report.html")
```

Use these as a *first pass* to get oriented fast, but never as a substitute for the targeted plots above — automated reports can't tell you which questions matter for *your* problem.

## Practice Questions

1. From `df.describe()`, how would you detect a column with outliers, one with missing values, and one that is right-skewed?
2. Write the pandas code to compare median revenue across three subscription plans.
3. What questions would you ask after seeing a histogram with a spike at zero?
4. When would you prefer a boxplot over a histogram?

## LLM Prompts for Deeper Understanding

1. "Show me an EDA checklist I can run on any tabular dataset."
2. "What are 5 real data bugs that EDA typically catches, with examples?"
3. "How does EDA differ when the goal is prediction vs explanation?"

## Key Takeaways

- EDA = profile each variable, explore relationships, hunt for bugs — before modeling.
- `describe()`, `value_counts()`, `isna().sum()` and `corr()` cover the summary pass.
- Histograms, boxplots, scatters and bars cover the visual pass.
- Treat every plot as a test of your data's sanity.
- Automated profiling reports are a fast first pass, not a replacement for thinking.

## Footnotes & Attribution

1. Kaggle Learn, *Data Visualization* (EDA micro-course). [https://www.kaggle.com/learn/data-visualization](https://www.kaggle.com/learn/data-visualization)
2. Towards Data Science, *EDA: A Practical Guide and Templates for Structured Data*. [https://towardsdatascience.com/exploratory-data-analysis-eda-a-practical-guide-and-templates-for-structured-data-ab99bfecc654](https://towardsdatascience.com/exploratory-data-analysis-eda-a-practical-guide-and-templates-for-structured-data-ab99bfecc654)
3. Wes McKinney, *Python for Data Analysis* (Ch. 9, Plotting & Visualization). [https://wesmckinney.com/book/plotting-and-visualization](https://wesmckinney.com/book/plotting-and-visualization)
4. ydata-profiling (GitHub). Automated EDA report generation. [https://github.com/ydataai/ydata-profiling](https://github.com/ydataai/ydata-profiling)
