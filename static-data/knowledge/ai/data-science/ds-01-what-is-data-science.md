---
{
  "title": "What Is Data Science?",
  "description": "Define data science, understand its core disciplines, and map the roles and workflow of a modern data team.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define data science and contrast it with data analysis and statistics",
    "Identify the roles in a modern data science team",
    "Describe the data science workflow at a high level",
    "Recognize the core tools and languages used across the field"
  ],
  "knowledge_refs": [
    "machine-learning/ml-01-what-is-machine-learning",
    "data-science/ds-02-the-data-science-pipeline",
    "tools/apache-spark",
    "databases/postgresql"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "What is Data Science? What a Data Scientist Actually Does — freeCodeCamp",
      "url": "https://www.freecodecamp.org/news/what-is-data-science-what-a-data-scientist-actually-does/",
      "description": "Beginner-friendly explainer of what data science is, the skills it requires, and the day-to-day work."
    },
    {
      "title": "50 Years of Data Science — David Donoho (2017)",
      "url": "https://courses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf",
      "description": "The influential essay that traces how 'data science' grew out of statistics and computing."
    },
    {
      "title": "A Very Short History of Data Science — Gil Press",
      "url": "https://www.forbes.com/sites/gilpress/2013/05/28/a-very-short-history-of-data-science/",
      "description": "History of the term 'data science' from the 1960s to today."
    },
    {
      "title": "Data Science Lifecycle — GeeksforGeeks",
      "url": "https://www.geeksforgeeks.org/data-science/data-science-lifecycle/",
      "description": "Maps the end-to-end lifecycle often aligned with CRISP-DM."
    },
    {
      "title": "Data Scientist vs Data Engineer vs Data Analyst — GeeksforGeeks",
      "url": "https://www.geeksforgeeks.org/data-science/difference-between-data-scientist-data-engineer-data-analyst/",
      "description": "Clear breakdown of the three core data roles and their distinct tech stacks."
    }
  ]
}
---

# DS-01-WHAT-IS-DATA-SCIENCE: What Is Data Science?

## Introduction

Data science is the discipline of turning raw data into decisions. It sits at the intersection of three older fields — **statistics** (how to reason about uncertainty), **computer science** (how to process data at scale), and **domain expertise** (how to know which questions matter). A data scientist does not merely report what *happened* (that is descriptive analytics); they build models that predict what *will happen* and design experiments that reveal *why* it happens.

The term itself is young. In his widely-cited essay *50 Years of Data Science*, statistician David Donoho argues that the field's core ideas — data analysis, data curation, reproducible research, and communication — existed long before the name, but that computing finally made them practical at scale [1]. The name "data science" circulated through the 1960s–90s, was popularized in the late 2000s (in part by *Sexy Jobs in the Next 10 Years* — the 2012 Harvard Business Review article that called the data scientist "the sexiest job of the 21st century"), and has been mainstream ever since [2].

Why should you care? Because data science is the engine behind everything from Netflix recommendations and fraud detection to medical imaging and self-driving cars. And unlike most engineering fields, its raw material — data — is everywhere and free.

## Key Concepts

### 1. Data science vs. data analysis vs. statistics

These terms overlap, but the boundaries matter:

- **Statistics** is the mathematics of uncertainty: sampling, distributions, estimation, and hypothesis testing. It answers "how confident can I be?"
- **Data analysis** is the craft of examining a dataset to find patterns, trends, and anomalies. It is descriptive and diagnostic.
- **Data science** extends both with *prediction* and *engineering*: it builds models that generalize to new data, and ships them in production systems.

A useful way to remember the difference: a statistician asks *"is this effect real?"*, an analyst asks *"what does the data say?"*, and a data scientist asks *"can I build something that predicts the next observation?"*.

### 2. The roles in a modern data team

Real projects are team efforts. The three headline roles are [3]:

| Role | Core question | Typical tools |
| --- | --- | --- |
| **Data Analyst** | What happened, and why? | SQL, Excel, Tableau/Power BI |
| **Data Scientist** | What will happen next? How do I model it? | Python/R, pandas, scikit-learn |
| **Data Engineer** | How do I get and keep the data reliable? | Python, Spark, Airflow, dbt, cloud warehouses |

Adjacent roles you will meet: the **ML engineer** (puts models into production), the **analytics engineer** (builds clean, transformed data models for analysts), and the **MLOps engineer** (automates the ML lifecycle). Don't worry about picking one yet — the foundations you are learning now are shared by all of them.

### 3. The data science workflow at a high level

Nearly every project moves through the same stages (formalized by the CRISP-DM methodology and its successors) [4]:

1. **Frame the problem** — turn a business question into a data question.
2. **Acquire data** — find, scrape, or query the data you need.
3. **Clean & wrangle** — fix missing values, types, duplicates, and structure.
4. **Explore & visualize** — find patterns, outliers, and relationships (EDA).
5. **Model** — train a statistical or ML model; evaluate it honestly.
6. **Communicate & deploy** — present findings and, if useful, ship the model.

The loop is not linear: you will circle back constantly as exploration changes your questions. Iteration is the norm, not the exception.

### 4. The core tools and languages

- **Python** dominates: pandas for tabular data, NumPy for arrays, Matplotlib/Seaborn for plots, scikit-learn for modeling.
- **R** remains strong in academia and statistical modeling.
- **SQL** is non-negotiable — most data lives in databases.
- **Jupyter notebooks** are the standard exploratory environment.
- **Cloud & big-data tools** (Spark, dbt, Airflow, cloud warehouses) matter once data outgrows a laptop.

You will learn the Python stack in detail in the next several lessons.

## Practice Questions

1. What is the difference between descriptive, diagnostic, predictive, and prescriptive analytics? Where does data science sit?
2. A stakeholder asks you to "explain why last quarter's sales dropped in the Midwest." Which role is this primarily?
3. Why is iteration a core part of the data science workflow rather than a sign of failure?
4. What are three questions you can already answer about a dataset before writing any code?

## LLM Prompts for Deeper Understanding

1. "Explain the difference between statistics, data analysis, and data science with a concrete business example."
2. "Walk me through a typical week in the life of a data scientist vs a data analyst vs a data engineer."
3. "What questions should I ask a stakeholder before starting any data science project?"

## Key Takeaways

- Data science = statistics + computing + domain knowledge, aimed at *decisions*.
- The workflow is: frame → acquire → clean → explore → model → communicate, and it loops.
- Teams divide labor into analyst, scientist, and engineer roles with overlapping toolkits.
- Python + SQL + statistics is the entry-point stack for nearly all data work.

## Footnotes & Attribution

1. David Donoho, *50 Years of Data Science* (2017). Analysis of the field's intellectual roots and future. [https://courses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf](https://courses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf)
2. Gil Press, *A Very Short History of Data Science* (Forbes, 2013). Background on the term's origins. [https://www.forbes.com/sites/gilpress/2013/05/28/a-very-short-history-of-data-science/](https://www.forbes.com/sites/gilpress/2013/05/28/a-very-short-history-of-data-science/)
3. GeeksforGeeks, *Data Scientist vs Data Engineer vs Data Analyst*. Role definitions and tooling. [https://www.geeksforgeeks.org/data-science/difference-between-data-scientist-data-engineer-data-analyst/](https://www.geeksforgeeks.org/data-science/difference-between-data-scientist-data-engineer-data-analyst/)
4. GeeksforGeeks, *Data Science Lifecycle*. CRISP-DM-aligned stage breakdown. [https://www.geeksforgeeks.org/data-science/data-science-lifecycle/](https://www.geeksforgeeks.org/data-science/data-science-lifecycle/)
5. freeCodeCamp, *What is Data Science? What a Data Scientist Actually Does*. Beginner overview. [https://www.freecodecamp.org/news/what-is-data-science-what-a-data-scientist-actually-does/](https://www.freecodecamp.org/news/what-is-data-science-what-a-data-scientist-actually-does/)
