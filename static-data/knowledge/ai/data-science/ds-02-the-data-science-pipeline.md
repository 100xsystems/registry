---
{
  "title": "The Data Science Pipeline",
  "description": "Walk through the six stages of a data science project and learn where real projects fail — and why iteration matters.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Identify the six stages of the data science pipeline",
    "Explain why iteration beats a linear flow",
    "Map real project tasks onto pipeline stages",
    "Anticipate the most common failure points"
  ],
  "knowledge_refs": [
    "data-science/ds-01-what-is-data-science",
    "machine-learning/ml-03-the-learning-problem",
    "mlops/mlops-02-the-ml-lifecycle",
    "data-science/ds-20-end-to-end-project"
  ],
  "prerequisites": [
    "DS-01: What Is Data Science?"
  ],
  "references": [
    {
      "title": "Data Science Lifecycle — GeeksforGeeks",
      "url": "https://www.geeksforgeeks.org/data-science/data-science-lifecycle/",
      "description": "The standard end-to-end lifecycle, often mapped to CRISP-DM."
    },
    {
      "title": "How to Build a Data Science Project from Scratch — freeCodeCamp",
      "url": "https://www.freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1/",
      "description": "A real project (Berlin rental prices) walked through every pipeline stage."
    },
    {
      "title": "CRISP-DM — IBM (Reference)",
      "url": "https://www.ibm.com/think/topics/crisp-dm",
      "description": "The classic cross-industry process model for data mining projects."
    },
    {
      "title": "The ML Lifecycle — Google Cloud",
      "url": "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning",
      "description": "How the pipeline extends beyond modeling into deployment and monitoring."
    }
  ]
}
---

# DS-02-THE-DATA-SCIENCE-PIPELINE: The Data Science Pipeline

## Introduction

A data science project is not "load data, run a model, done." In practice it is a loop of six stages that you revisit constantly. This lesson walks each stage, shows what "done" looks like, and — just as importantly — where projects most often go wrong. Almost every failure you will encounter in your first year can be traced to skipping one of these stages.

## Key Concepts

### 1. The six stages

**Stage 1 — Frame the problem.** Before any code, write down: What decision will this analysis inform? Who will use the result? What would "success" look like? The best question to ask a stakeholder is *"what will you do differently with this answer?"* If the answer is "nothing," the project probably shouldn't start. A crisp problem statement also picks the evaluation metric — predicting *whether* someone churns (classification) is a different problem from predicting *how much* they will spend (regression).

**Stage 2 — Acquire data.** Identify where the data lives: internal databases, CSV exports, APIs, or web scraping. Two decisions dominate this stage: (a) *granularity* — is each row the right unit (a user, a transaction, a day)? (b) *time range* — does it cover the conditions you want to predict? Data you cannot legally or reliably obtain is a project blocker, not a detail.

**Stage 3 — Clean & wrangle.** Real data is messy: missing values, wrong types, duplicate rows, inconsistent categories ("NY" vs "New York"), and outliers that are actually typos. This stage typically consumes 60–80% of a project's time — which is normal, not a sign you are doing something wrong. pandas is the workhorse here, and we dedicate a full lesson to it.

**Stage 4 — Explore & visualize (EDA).** Summarize each variable (distributions, ranges, missingness), then look at relationships between variables (correlations, grouped means, scatter plots). EDA is where you discover that the "obvious" feature is useless and the "boring" one is gold. It also catches data bugs that would silently poison a model.

**Stage 5 — Model.** Choose a method appropriate to the problem (regression, classification, clustering), split your data honestly into training and test sets, train, and evaluate. Modeling is often the *shortest* stage — a well-cleaned dataset beats a fancy algorithm every time.

**Stage 6 — Communicate & deploy.** Show the result to the people who will act on it: a chart plus a plain-language finding ("customers who X are 3× more likely to churn"). If the model is meant to run in production, this stage extends to APIs, monitoring, and retraining — the subject of our MLOps course.

### 2. Why iteration beats a linear flow

Here is the truth most tutorials hide: you will not pass through these stages once. Exploration reveals that the data is missing a key variable, so you go back to acquisition. The model's errors reveal a data-cleaning bug, so you go back to cleaning. The stakeholder clarifies the question, so you reframe the problem.

Treat the pipeline as a **feedback loop**. A good sign of a mature data scientist is that they plan for these loops instead of being surprised by them. Set aside time for "the second pass": the first version of any analysis is for learning, the second is for correctness, and only the third is presentable.

### 3. Where projects fail

The most common failure points, in rough order of frequency:

1. **The wrong question** — solving a problem nobody asked, or optimizing a metric that doesn't map to the decision.
2. **Leakage** — accidentally letting future information into training data (e.g., scaling with statistics computed on the full dataset). We cover this in the train/test lesson.
3. **Undisciplined splitting** — evaluating on data the model already saw, producing magical-but-fake accuracy.
4. **Skewed evaluation** — using accuracy on a 99/1 class-imbalanced problem and concluding the model is great.
5. **Silent data bugs** — duplicates, shifted time zones, stale joins — that produce confident, wrong answers.
6. **Ignoring deployment** — a model that lives only in a notebook changes nothing.

As you work through this course, notice how lessons on cleaning, EDA, evaluation, and deployment all exist to prevent exactly these failures.

### 4. Mapping real tasks to stages

A useful exercise: take any real project description and label each task with its stage. For example, for the freeCodeCamp Berlin-rental walkthrough [2]:

- "Which neighborhoods should we compare?" → Frame
- "Download rental listings + scrape amenity data" → Acquire
- "Parse prices, drop invalid rows, unify district names" → Clean
- "Plot price vs. area; check for outliers" → Explore
- "Train a regression to predict rent from features" → Model
- "Present a chart of price drivers to the client" → Communicate

## Practice Questions

1. Write the six pipeline stages in order, then explain which two stages are most often skipped by beginners.
2. What is data leakage? Give one concrete example that could happen during scaling or cleaning.
3. Why is "accuracy" a dangerous metric on imbalanced data? Give an example.
4. A stakeholder asks "just give me a model that predicts sales." What three clarifying questions should you ask in Stage 1?

## LLM Prompts for Deeper Understanding

1. "Give me a checklist I can use to audit my own data science project for the six most common failure points."
2. "Explain data leakage with five different concrete examples in machine learning."
3. "Compare CRISP-DM, TDSP, and the Google ML lifecycle — what do they agree on?"

## Key Takeaways

- The pipeline is: frame → acquire → clean → explore → model → communicate — and it loops.
- Cleaning and framing dominate real project time; modeling is often the shortest stage.
- The most common failures are wrong questions, leakage, dishonest splits, and ignored deployment.
- Plan for iteration: the first pass is for learning, the second for correctness.

## Footnotes & Attribution

1. GeeksforGeeks, *Data Science Lifecycle*. Stage breakdown aligned with CRISP-DM. [https://www.geeksforgeeks.org/data-science/data-science-lifecycle/](https://www.geeksforgeeks.org/data-science/data-science-lifecycle/)
2. freeCodeCamp, *How to Build a Data Science Project from Scratch* (Berlin rentals). Real pipeline walkthrough. [https://www.freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1/](https://www.freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1/)
3. IBM, *CRISP-DM*. The cross-industry process model. [https://www.ibm.com/think/topics/crisp-dm](https://www.ibm.com/think/topics/crisp-dm)
4. Google Cloud, *MLOps: Continuous Delivery and Automation Pipelines*. The lifecycle beyond the notebook. [https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
