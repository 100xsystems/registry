---
{
  "title": "An End-to-End Data Science Project",
  "description": "Combine everything into a real project: from a raw dataset to a working, honestly-evaluated model.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Structure a project from question to delivery",
    "Apply the full pipeline: clean, explore, engineer, model, evaluate",
    "Build an honest train/test evaluation",
    "Package results for a stakeholder"
  ],
  "knowledge_refs": [
    "data-science/ds-02-the-data-science-pipeline",
    "data-science/ds-14-train-test-split",
    "data-science/ds-18-model-evaluation",
    "mlops/mlops-02-the-ml-lifecycle"
  ],
  "prerequisites": [
    "DS-19: Communicating Results"
  ],
  "references": [
    {
      "title": "End-to-End Data Science Project — Beginner Guide (Kaggle)",
      "url": "https://www.kaggle.com/code/kutaykutlu/end-to-end-data-science-project-beginner-guide",
      "description": "A complete walkthrough: problem framing through evaluation."
    },
    {
      "title": "UCI Machine Learning Repository",
      "url": "https://archive.ics.uci.edu/datasets",
      "description": "Hundreds of clean, well-documented classic datasets for practice."
    },
    {
      "title": "Kaggle Datasets",
      "url": "https://www.kaggle.com/datasets",
      "description": "Real-world open datasets across every domain."
    },
    {
      "title": "How to Build a Data Science Project from Scratch — freeCodeCamp",
      "url": "https://www.freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1/",
      "description": "Berlin rental prices walked through every stage."
    },
    {
      "title": "Machine Learning Mastery — Start Here",
      "url": "https://machinelearningmastery.com/start-here/",
      "description": "A systematic applied-ML workflow with worked examples."
    }
  ]
}
---

# DS-20-END-TO-END-PROJECT: An End-to-End Data Science Project

## Introduction

This is the capstone of the course: everything you've learned — pipeline, Python, NumPy, pandas, cleaning, EDA, visualization, statistics, features, splits, modeling, evaluation, communication — applied to one real project. We'll use a classic starter dataset: predicting **house prices** (a regression problem) from the California Housing dataset, or any dataset you prefer. The structure shown here is the structure of almost every professional data science project [1].

## Key Concepts

### 1. Frame the question

**Question**: "Can we predict a house's median value from its features?" A crisp problem statement: *regression*, target = median house value, features = location, income, age, population, rooms.

Write down success criteria up front: *"We will consider the model useful if it achieves RMSE below $50k on a held-out test set."* Deciding the metric before building the model is the discipline that prevents p-hacking later.

### 2. Acquire and explore

```python
import pandas as pd

df = pd.read_csv("california_housing.csv")   # or from sklearn.datasets
print(df.info(), df.describe())
print(df.isna().sum())
```

Quick observations from real data: `total_bedrooms` has missing values; `ocean_proximity` is categorical; income is right-skewed (log transform candidate). These observations drive the cleaning plan.

### 3. Clean and engineer features

```python
df = df.dropna(subset=["total_bedrooms"])
df["log_income"] = df["median_income"].apply(lambda x: __import__("numpy").log1p(x))
df["rooms_per_household"] = df["total_rooms"] / df["households"]
df["bedrooms_per_room"] = df["total_bedrooms"] / df["total_rooms"]
df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)
```

Each line has a reason: impute/drop missing sensibly, log-tame skew, encode domain ratios (rooms per household is often more predictive than raw counts), one-hot the categorical.

### 4. Split honestly and build a pipeline

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

X, y = df.drop(columns=["median_house_value"]), df["median_house_value"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=10.0))])
model.fit(X_train, y_train)
```

The pipeline guarantees the scaler learns only from the training set — no leakage (see the train/test lesson).

### 5. Evaluate honestly and improve

```python
from sklearn.metrics import mean_squared_error, r2_score

preds = model.predict(X_test)
print(f"RMSE: ${mean_squared_error(y_test, preds, squared=False):,.0f}")
print(f"R²:   {r2_score(y_test, preds):.3f}")
```

Then iterate — but measure every change on the *test set only at the end*. Improve via:

- Trying gradient boosting (`HistGradientBoostingRegressor`) — often the strongest tabular model.
- Cross-validating to compare variants robustly.
- Adding the domain-derived features above.

```python
from sklearn.model_selection import cross_val_score
cv = cross_val_score(model, X_train, y_train, cv=5, scoring="r2")
print(cv.mean(), cv.std())
```

### 6. Communicate the result

Finish with the one-page structure from the communication lesson:

1. **Answer**: "With 5 features we predict median house value with an RMSE of ~$47k (R² 0.80), evaluated on a held-out test set."
2. **Evidence**: one chart (predicted vs actual) + the key numbers.
3. **Limits**: no causal claims; the model is best in dense urban areas.
4. **Ask**: "We can deploy this as a valuation baseline — want a demo?"

### 7. Where to go next

- Swap in a different dataset from UCI or Kaggle and repeat the workflow [2][3].
- Add the ML course's models (random forests, gradient boosting) and beat this baseline.
- Take the MLOps course to learn how this notebook becomes a production service.

## Practice Questions

1. Why do we decide the success metric *before* training?
2. What would happen if the scaler saw the test set?
3. Why might `rooms_per_household` beat raw `total_rooms` as a feature?
4. Run this project on a dataset of your choice and report RMSE/R² honestly.

## LLM Prompts for Deeper Understanding

1. "Review my end-to-end pipeline for data leakage and give me a checklist."
2. "How should I present a regression model's RMSE to a non-technical stakeholder?"
3. "What are the differences between this sklearn workflow and a production MLOps pipeline?"

## Key Takeaways

- A real project = frame → acquire → clean → engineer → split → model → evaluate → communicate.
- Decide the success metric before training; evaluate on test only at the end.
- Pipelines prevent preprocessing leakage.
- Domain-derived features often beat raw columns.
- Iterate with cross-validation, then deliver the one-page answer.

## Footnotes & Attribution

1. Kaggle, *End-to-End Data Science Project — Beginner Guide*. [https://www.kaggle.com/code/kutaykutlu/end-to-end-data-science-project-beginner-guide](https://www.kaggle.com/code/kutaykutlu/end-to-end-data-science-project-beginner-guide)
2. UCI Machine Learning Repository. [https://archive.ics.uci.edu/datasets](https://archive.ics.uci.edu/datasets)
3. Kaggle Datasets. [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)
4. freeCodeCamp, *How to Build a Data Science Project from Scratch*. [https://www.freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1/](https://www.freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1/)
5. Jason Brownlee, *Machine Learning Mastery — Start Here*. [https://machinelearningmastery.com/start-here/](https://machinelearningmastery.com/start-here/)
