---
{
  "title": "Regression Models",
  "description": "Predict numbers with linear and regularized regression, and read the coefficients like an analyst.",
  "type": "lesson",
  "order": 15,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Fit and interpret a linear regression",
    "Handle multiple predictors and interactions",
    "Use Ridge/Lasso for stability",
    "Report error metrics such as RMSE and R²"
  ],
  "knowledge_refs": [
    "data-science/ds-15-regression-models"
  ],
  "prerequisites": [
    "DS-14: Train/Test Splits & Validation"
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

# DS-15-REGRESSION-MODELS: Regression Models

## Introduction

Predict numbers with linear and regularized regression, and read the coefficients like an analyst. By the end of this lesson you will be able to: Fit and interpret a linear regression; Handle multiple predictors and interactions; Use Ridge/Lasso for stability; Report error metrics such as RMSE and R².

## Key Concepts

### 1. Fit and interpret a linear regression

Target: Fit and interpret a linear regression. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression().fit(X, y)
print("slope:", model.coef_[0], "intercept:", model.intercept_)
```
### 2. Handle multiple predictors and interactions

Target: Handle multiple predictors and interactions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

X = np.array([[1, 3], [2, 5], [3, 7], [4, 9]])
y = np.array([2, 4, 6, 8])
m = LinearRegression().fit(X, y)
pred = m.predict(X)
print("RMSE:", round(mean_squared_error(y, pred, squared=False), 3))
print("R2:", round(m.score(X, y), 3))
```
### 3. Use Ridge/Lasso for stability

Target: Use Ridge/Lasso for stability. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.linear_model import Ridge, Lasso

X = [[1, 10], [2, 20], [3, 30], [4, 40]]
y = [1, 2, 3, 4]
for name, model in [("ridge", Ridge(alpha=1.0)), ("lasso", Lasso(alpha=0.1))]:
    model.fit(X, y)
    print(name, "coefs:", model.coef_.round(2))
```
### 4. Report error metrics such as RMSE and R²

Target: Report error metrics such as RMSE and R². Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Residuals: the story the model did not capture
actual = np.array([3, 5, 7, 9])
pred = np.array([3.2, 4.8, 7.5, 8.6])
residuals = actual - pred
print("residuals:", residuals)
print("largest miss:", residuals[np.abs(residuals).argmax()])
```

## Practice Questions

1. What is the key idea behind "Regression Models"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Regression Models with analogies and real-world examples"
1. "Show me common mistakes beginners make with Regression Models"
1. "Provide advanced patterns and performance considerations for Regression Models"

## Key Takeaways

- Master the core ideas of Regression Models through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
