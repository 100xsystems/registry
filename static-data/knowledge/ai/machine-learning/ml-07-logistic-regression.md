---
slug: ml-07-logistic-regression
title: "Logistic Regression"
description: "The foundational classification algorithm — simple, interpretable, and still the first thing to try on any tabular classification problem."
order: 7
tags:
  - machine-learning
  - classification
  - logistic-regression
  - sigmoid
prerequisites:
  - ml-05-linear-regression
  - ml-06-gradient-descent
references:
  - title: "Logistic Regression — scikit-learn User Guide"
    url: "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression"
    description: "Official scikit-learn documentation with implementation details"
  - title: "StatQuest: Logistic Regression"
    url: "https://www.youtube.com/watch?v=yIYKR4sgzI8"
    description: "Josh Starmer's clear visual explanation of logistic regression"
  - title: "Elements of Statistical Learning, Ch. 4"
    url: "https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf"
    description: "Hastie, Tibshirani, Friedman — the authoritative textbook treatment"
  - title: "CS229 Lecture Notes: Logistic Regression"
    url: "https://cs229.stanford.edu/lectures-spring2022/main_notes.pdf"
    description: "Andrew Ng's Stanford course notes on logistic regression"
  - title: "Wikipedia: Logistic Regression"
    url: "https://en.wikipedia.org/wiki/Logistic_regression"
    description: "Comprehensive mathematical treatment including MLE derivation"
knowledge_refs:
  - ml-05-linear-regression
  - ml-06-gradient-descent
  - ml-18-classification-metrics
---

# Logistic Regression

Despite its name, logistic regression is a **classification** algorithm. It's the natural starting point for any classification task — simple, fast, interpretable, and surprisingly competitive on tabular data.

## From Regression to Classification

Linear regression predicts continuous values, but classification requires a probability between 0 and 1. The **sigmoid function** squashes any real number into $(0, 1)$:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Logistic regression applies a linear model followed by the sigmoid:

$$P(y=1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b)$$

The output is interpreted as the probability that the input belongs to the positive class. A threshold (typically 0.5) converts this probability into a class label.

## The Decision Boundary

The decision boundary is where $P(y=1) = 0.5$, which occurs when $\mathbf{w}^T \mathbf{x} + b = 0$. This is always a **linear** boundary — a line in 2D, a plane in 3D, a hyperplane in higher dimensions.

This linearity is both a strength (simple, interpretable) and a limitation (can't learn XOR or other non-linear patterns without feature engineering).

**Feature engineering for non-linearity:**
```python
# Polynomial features transform linear boundaries into non-linear ones
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, interaction_only=False)
X_poly = poly.fit_transform(X)
# Now logistic regression on X_poly can learn curved boundaries
```

## Loss Function: Cross-Entropy

Logistic regression is trained by minimizing **binary cross-entropy** (also called log loss):

$$\mathcal{L} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{p}_i) + (1 - y_i) \log(1 - \hat{p}_i) \right]$$

Why not MSE? Because the sigmoid + MSE creates a non-convex loss surface with local minima. Cross-entropy with sigmoid is **convex** — guaranteed to find the global optimum.

**Intuition**: When $y=1$, the loss is $-\log(\hat{p})$ — heavily penalizing low predicted probabilities. When $y=0$, the loss is $-\log(1-\hat{p})$ — penalizing high predicted probabilities.

## Maximum Likelihood Estimation

Logistic regression parameters are found via MLE — maximizing the likelihood of the observed data:

$$\mathcal{L}(\mathbf{w}) = \prod_{i=1}^{N} \hat{p}_i^{y_i} (1-\hat{p}_i)^{1-y_i}$$

Taking the log and negating gives the cross-entropy loss. Optimization is done via gradient descent or more efficient methods like L-BFGS.

## Multiclass Extension: Softmax

For $K > 2$ classes, logistic regression generalizes via **softmax regression**:

$$P(y=k \mid \mathbf{x}) = \frac{e^{\mathbf{w}_k^T \mathbf{x}}}{\sum_{j=1}^{K} e^{\mathbf{w}_j^T \mathbf{x}}}$$

Each class gets its own weight vector $\mathbf{w}_k$. The softmax ensures probabilities sum to 1. Training uses **categorical cross-entropy**.

```python
from sklearn.linear_model import LogisticRegression
# Automatically handles multiclass via softmax
clf = LogisticRegression(multi_class='multinomial', max_iter=1000)
clf.fit(X_train, y_train)
```

## Regularization

Logistic regression is prone to overfitting in high dimensions. scikit-learn applies L2 regularization by default (controlled by `C`, which is the **inverse** regularization strength):

```python
# Stronger regularization (smaller C)
clf = LogisticRegression(C=0.01, penalty='l2')

# L1 regularization for feature selection (sparse solutions)
clf = LogisticRegression(C=0.1, penalty='l1', solver='liblinear')

# Elastic net combines L1 and L2
clf = LogisticRegression(C=0.1, penalty='elasticnet', l1_ratio=0.5, solver='saga')
```

| Regularization | Effect | Use When |
|---|---|---|
| L2 (Ridge) | Shrinks weights toward zero | Default; all features potentially useful |
| L1 (Lasso) | Sets some weights to exactly zero | Feature selection; sparse models |
| Elastic Net | Combines both | High-dimensional with correlated features |

## Advantages

- **Interpretable**: Weights directly indicate feature importance and direction
- **Probabilistic output**: Gives calibrated probabilities, not just labels
- **Fast**: Training is O(N × D) — scales to millions of samples
- **Strong baseline**: Often competitive with complex models on tabular data
- **No hyperparameters to tune**: Works well with defaults
- **Well-understood theory**: Confidence intervals, hypothesis tests, p-values

## Limitations

- Linear decision boundary — can't learn complex patterns without feature engineering
- Assumes features are independently contributing (no interactions without manual creation)
- Sensitive to correlated features (use regularization)
- Can't capture non-linear relationships

## Practical Tips

1. **Always start with logistic regression** as a baseline for tabular classification
2. **Scale your features** — StandardScaler before logistic regression
3. **Check class imbalance** — use `class_weight='balanced'` or adjust threshold
4. **Use `liblinear` solver** for small datasets, `saga` for large ones
5. **L1 regularization** is excellent for understanding which features matter
6. **Calibrate probabilities** if you need well-calibrated outputs:
   ```python
   from sklearn.calibration import CalibratedClassifierCV
   calibrated = CalibratedClassifierCV(clf, cv=5, method='isotonic')
   ```

## Logistic Regression vs. Neural Networks

A single-neuron neural network with sigmoid activation IS logistic regression. Logistic regression is the simplest neural network. The boundary between "traditional ML" and "deep learning" is really about depth and non-linearity.

## Further Reading

- The Elements of Statistical Learning Chapter 4 is the definitive reference
- scikit-learn's documentation covers practical considerations and solver choices
- CS229 notes derive the gradient and Newton's method for logistic regression
- For probabilistic programming, PyMC3 and Stan have full Bayesian logistic regression implementations
