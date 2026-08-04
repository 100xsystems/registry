---
slug: ml-11-support-vector-machines
title: "Support Vector Machines"
description: "The elegant maximum-margin classifier that dominated ML before deep learning — still powerful for high-dimensional, small-sample problems."
order: 11
tags:
  - machine-learning
  - svm
  - kernel-trick
  - maximum-margin
prerequisites:
  - ml-07-logistic-regression
  - ml-06-gradient-descent
references:
  - title: "scikit-learn: SVM User Guide"
    url: "https://scikit-learn.org/stable/modules/svm.html"
    description: "Official documentation with practical guidance on SVMs"
  - title: "A Tutorial on Support Vector Machines for Pattern Recognition (Burges)"
    url: "https://www.microsoft.com/en-us/research/publication/a-tutorial-on-support-vector-machines-for-pattern-recognition/"
    description: "Burges' classic tutorial on SVM theory and practice"
  - title: "CS229: SVM Notes"
    url: "https://cs229.stanford.edu/main_notes.pdf"
    description: "Andrew Ng's lecture notes covering margin maximization and kernels"
  - title: "StatQuest: Support Vector Machines"
    url: "https://www.youtube.com/watch?v=efR1C2K8KCw"
    description: "Josh Starmer's visual explanation of SVMs and the kernel trick"
  - title: "libsvm: A Library for Support Vector Machines"
    url: "https://www.csie.ntu.edu.tw/~cjlin/libsvm/"
    description: "The reference implementation that most libraries wrap"
knowledge_refs:
  - ml-07-logistic-regression
  - ml-14-feature-scaling
  - ml-12-k-nearest-neighbors
---

# Support Vector Machines

Support Vector Machines (SVMs) find the hyperplane that **maximizes the margin** between classes. Though largely superseded by deep learning for unstructured data, SVMs remain powerful for high-dimensional, small-sample problems.

## Maximum Margin Classification

Given labeled data, SVM finds the hyperplane $\mathbf{w}^T \mathbf{x} + b = 0$ that maximizes the distance to the nearest data point from each class. This distance is the **margin**:

$$\text{margin} = \frac{2}{\|\mathbf{w}\|}$$

The data points closest to the boundary are called **support vectors** — only they determine the decision boundary. All other points are irrelevant.

**Why maximize the margin?**
- Wider margins = better generalization (VC dimension theory)
- Fewer support vectors = simpler model
- More robust to noise in training data

## Soft Margin SVM

Real data is rarely linearly separable. **Soft margin** SVMs allow some misclassifications:

$$\min_{\mathbf{w}, b, \xi} \frac{1}{2}\|\mathbf{w}\|^2 + C \sum_{i=1}^{N} \xi_i$$

subject to:
$$y_i(\mathbf{w}^T \mathbf{x}_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0$$

The parameter $C$ controls the trade-off:
- **Large $C$**: Low tolerance for misclassifications (narrow margin, overfitting)
- **Small $C$**: More tolerant (wider margin, underfitting)

## The Kernel Trick

The real power of SVMs comes from **kernels** — implicitly mapping data to a higher-dimensional space where it becomes linearly separable, without ever computing the mapping:

$$K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$$

The dual formulation of SVM depends only on dot products, which can be replaced by kernel evaluations:

| Kernel | Formula | Best For |
|---|---|---|
| Linear | $K(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$ | Linearly separable, high-D |
| Polynomial | $K(\mathbf{x}, \mathbf{z}) = (\gamma \mathbf{x}^T \mathbf{z} + r)^d$ | Known polynomial relationships |
| RBF (Gaussian) | $K(\mathbf{x}, \mathbf{z}) = \exp(-\gamma\|\mathbf{x}-\mathbf{z}\|^2)$ | General non-linear, default choice |
| Sigmoid | $K(\mathbf{x}, \mathbf{z}) = \tanh(\gamma \mathbf{x}^T \mathbf{z} + r)$ | Neural network approximation |

**RBF kernel intuition**: Each support vector creates a Gaussian "bump" around itself. The decision boundary is a weighted sum of these bumps. The parameter $\gamma$ controls the width of each bump.

## Multi-Class Extension

SVMs are inherently binary classifiers. Multi-class is handled by:
- **One-vs-One (OvO)**: Train $\binom{K}{2}$ classifiers, majority vote (default in scikit-learn)
- **One-vs-Rest (OvR)**: Train $K$ classifiers, one per class

## Practical Guide

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Critical: SVMs require feature scaling!
svm_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        decision_function_shape='ovr'
    ))
])
svm_pipeline.fit(X_train, y_train)
```

**Key practical points:**
1. **Always scale features** — SVMs are distance-based
2. **RBF kernel is the default** — start here
3. **Tune $C$ and $\gamma$ jointly** — use GridSearchCV
4. **Small datasets**: SVMs excel (< 10K samples)
5. **Large datasets**: SVMs become slow ($O(N^2)$ to $O(N^3)$) — use linear SVM or SGD

```python
# For large datasets, use SGDClassifier with hinge loss
from sklearn.linear_model import SGDClassifier
linear_svm = SGDClassifier(loss='hinge', penalty='l2', alpha=0.0001)
linear_svm.fit(X_train_scaled, y_train)
```

## Strengths

- **Effective in high dimensions**: Even when features > samples
- **Memory efficient**: Only stores support vectors
- **Versatile kernels**: Adapts to different data geometries
- **Strong theoretical foundation**: PAC learning, VC dimension
- **Well-calibrated**: Probability estimates available via Platt scaling

## Limitations

- **Slow on large datasets**: $O(N^2)$ kernel computation
- **Sensitive to feature scaling**: Must normalize
- **No native probability output**: Requires Platt scaling (extra computation)
- **Kernel selection**: Can be difficult without domain knowledge
- **Superseded by deep learning**: For images, text, audio
- **Hard to interpret**: Kernel mapping is implicit

## SVM vs. Logistic Regression

| Aspect | SVM | Logistic Regression |
|---|---|---|
| Decision boundary | Max margin | Max likelihood |
| Loss function | Hinge loss | Log loss |
| Support vectors | Only boundary points | All points |
| Probabilities | Needs Platt scaling | Native |
| Kernel trick | Yes | No (but feature engineering works) |
| Scalability | Poor on large N | Good |

**When to use SVM**: Small-to-medium dataset, high-dimensional features, clear margin of separation, need for kernel methods.

## Further Reading

- Burges' tutorial remains the best theoretical introduction
- CS229 notes provide the mathematical derivation of the dual formulation
- For linear SVMs at scale, LIBLINEAR (Fan et al., 2008) is the go-to
- Schölkopf & Smola (2002) "Learning with Kernels" is the definitive textbook
