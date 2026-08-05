---
title: The Python ML Stack
description: 'Master the essential Python libraries for machine learning: NumPy, pandas,
  scikit-learn, matplotlib, and Jupyter.'
type: lesson
order: 4
duration: 50 min
difficulty: beginner
learning_objectives:
- Use NumPy for efficient numerical computation and array operations
- Manipulate datasets with pandas DataFrames
- Build and evaluate ML models with scikit-learn
- Create informative visualizations with matplotlib
- Work interactively in Jupyter notebooks
knowledge_refs:
- machine-learning/ml-01-what-is-machine-learning
- data-science/ds-03-python-for-data-science
- tools/apache-spark
prerequisites:
- 'DS-03: Python for Data Science'
references:
- title: NumPy Official Documentation
  url: https://numpy.org/doc/stable/
  description: Comprehensive reference for NumPy arrays, broadcasting, and vectorized
    operations.
- title: pandas User Guide
  url: https://pandas.pydata.org/docs/user_guide/
  description: Official pandas documentation with tutorials on DataFrames, groupby,
    and time series.
- title: scikit-learn User Guide
  url: https://scikit-learn.org/stable/user_guide.html
  description: The authoritative guide to scikit-learn's ML algorithms, preprocessing,
    and evaluation tools.
- title: Python Data Science Handbook — Jake VanderPlas
  url: https://jakevdp.github.io/PythonDataScienceHandbook/
  description: Free online book covering NumPy, pandas, matplotlib, and scikit-learn
    with practical examples.
- title: Matplotlib Tutorials
  url: https://matplotlib.org/stable/tutorials/index.html
  description: Official matplotlib tutorials covering basic to advanced visualization
    techniques.
---

Python dominates machine learning not because it's the fastest language, but because of its ecosystem. The combination of NumPy, pandas, scikit-learn, matplotlib, and Jupyter creates a workflow that's unmatched in productivity. This lesson gives you fluency in the core tools.

---

## NumPy: The Foundation

NumPy provides the N-dimensional array (`ndarray`) — the fundamental data structure for all numerical computing in Python. Every other library in the stack builds on top of it.

### Why NumPy Is Fast

Python lists are slow because each element is a separate object with type information. NumPy arrays are contiguous blocks of typed data — the CPU can process them with vectorized operations that operate on entire arrays at once, without Python loops.

```python
import numpy as np

# Python loop: slow
result = []
for i in range(1000000):
    result.append(i ** 2)

# NumPy vectorized: 10-100x faster
arr = np.arange(1000000)
result = arr ** 2
```

### Core Operations

```python
# Array creation
a = np.array([1, 2, 3, 4, 5])        # From list
b = np.zeros((3, 4))                   # 3x4 zeros
c = np.random.randn(100, 10)           # 100x10 random normal

# Indexing and slicing
c[0, :]                                # First row
c[:, 3]                                # Fourth column
c[c > 0]                               # Boolean indexing

# Linear algebra
np.dot(a, b)                           # Dot product
np.linalg.inv(matrix)                  # Matrix inverse
np.linalg.eig(matrix)                  # Eigenvalues
```

### Broadcasting

NumPy automatically expands arrays with different shapes for element-wise operations:

```python
# Add a scalar to every element
matrix = np.random.randn(100, 5)
result = matrix + 1.0

# Add a vector to each row
means = np.mean(matrix, axis=0)        # Shape: (5,)
centered = matrix - means              # Broadcasting subtracts from each row
```

---

## pandas: Data Manipulation

pandas provides the `DataFrame` — a table-like data structure that's like a spreadsheet in Python. It's the primary tool for loading, cleaning, and transforming data.

### Creating DataFrames

```python
import pandas as pd

# From a dictionary
df = pd.DataFrame({
    'age': [25, 30, 35, 40],
    'salary': [50000, 60000, 70000, 80000],
    'department': ['engineering', 'engineering', 'sales', 'sales']
})

# From a CSV file
df = pd.read_csv('data.csv')
```

### Essential Operations

```python
# Inspecting data
df.head()                               # First 5 rows
df.describe()                           # Statistical summary
df.info()                               # Column types and null counts

# Selecting data
df['salary']                            # Single column
df[['age', 'salary']]                   # Multiple columns
df[df['age'] > 30]                      # Filtering rows

# Grouping and aggregation
df.groupby('department')['salary'].mean()

# Handling missing values
df.dropna()                             # Remove rows with NaN
df.fillna(df.mean())                    # Fill with column means

# Feature engineering
df['salary_log'] = np.log(df['salary'])
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 40, 100])
```

### Why pandas Matters for ML

Before any model training, you need to:
1. Load and inspect your data
2. Handle missing values
3. Encode categorical variables
4. Engineer new features
5. Split data into train/test sets

pandas handles all of this with clean, readable syntax.

---

## scikit-learn: The ML Workhorse

scikit-learn provides a unified interface for dozens of ML algorithms. Its consistent API means once you learn one model, you can use them all.

### The Consistent API

Every model in scikit-learn follows the same pattern:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Create model
model = LinearRegression()

# 3. Train
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate
mse = mean_squared_error(y_test, y_pred)
```

### Key Components

**Preprocessing**: StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder

**Models**: LinearRegression, LogisticRegression, RandomForest, SVM, KNN, DecisionTree

**Model Selection**: train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV

**Metrics**: accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, r2_score

### Pipelines

Chain preprocessing and modeling to prevent data leakage:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf'))
])

pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
```

---

## matplotlib: Visualization

matplotlib is Python's foundational plotting library. While it's verbose, understanding it gives you complete control over every visual element.

### Basic Plots

```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Plot')
plt.show()

# Scatter plot
plt.scatter(x, y, c=colors, alpha=0.5)
plt.colorbar()

# Subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes[0, 0].hist(data, bins=30)
axes[0, 1].scatter(x, y)
```

### ML-Specific Visualizations

```python
# Learning curves
from sklearn.model_selection import learning_curve
train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, scoring='neg_mean_squared_error'
)

# Confusion matrix
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)

# Feature importance
importances = model.feature_importances_
plt.barh(feature_names, importances)
```

### Alternatives

For quick exploration, seaborn (built on matplotlib) and plotly (interactive) are popular. But matplotlib is the foundation everything else builds on.

---

## Jupyter: Interactive Development

Jupyter notebooks let you run code interactively, mixing code, output, and narrative text. They're the standard environment for ML experimentation.

### Best Practices

1. **Restart and run all** before sharing — ensure reproducibility
2. **One notebook per experiment** — don't mix unrelated work
3. **Clear outputs before committing** — keep version control clean
4. **Use markdown cells** for documentation — explain what you're doing and why

### Tips

- `Shift+Enter` runs the current cell and moves to the next
- `%timeit` measures execution time
- `%%capture` captures output (useful for suppressing noisy warnings)
- `!command` runs shell commands from within a cell

### When to Graduate

Notebooks are great for exploration, but production code should be in proper Python modules. The workflow: explore in notebooks → extract reusable functions → test in modules → deploy.

---

## Putting It All Together

Here's a complete ML workflow using the full stack:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv('customer_churn.csv')

# Explore
print(df.head())
print(df.describe())
df['churn'].value_counts().plot(kind='bar')

# Preprocess
X = pd.get_dummies(df.drop('churn', axis=1))
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

# Visualize feature importance
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(10).plot(kind='barh')
```

---

## Key Takeaways

- **NumPy**: Foundation — fast array operations, linear algebra, broadcasting
- **pandas**: Data manipulation — DataFrames, cleaning, grouping, feature engineering
- **scikit-learn**: ML models — consistent API for training, evaluation, and tuning
- **matplotlib**: Visualization — learning curves, confusion matrices, feature importance
- **Jupyter**: Interactive development — explore, prototype, document

---

## References

1. **NumPy Documentation** — Official reference for arrays and numerical computing. https://numpy.org/doc/stable/
2. **pandas User Guide** — Official documentation for DataFrames and data manipulation. https://pandas.pydata.org/docs/user_guide/
3. **scikit-learn User Guide** — Authoritative guide to ML algorithms and tools. https://scikit-learn.org/stable/user_guide.html
4. **Python Data Science Handbook** — Jake VanderPlas. Free book covering the full stack. https://jakevdp.github.io/PythonDataScienceHandbook/
5. **Matplotlib Tutorials** — Official tutorials for visualization techniques. https://matplotlib.org/stable/tutorials/index.html

---

## Footnotes

The Python ML stack's dominance is discussed in detail by Jake VanderPlas in *Python Data Science Handbook* (2016). The scikit-learn API design philosophy — consistent `fit`/`predict`/`score` interface — was pioneered by Pedregosa et al. (2011) and has become the de facto standard for ML library design.

