---
slug: ml-13-naive-bayes
title: "Naive Bayes"
description: "A probabilistic classifier based on Bayes' theorem with a 'naive' independence assumption — surprisingly effective for text classification."
order: 13
tags:
  - machine-learning
  - classification
  - naive-bayes
  - probabilistic
  - text-classification
prerequisites:
  - ml-07-logistic-regression
  - ml-03-the-learning-problem
references:
  - title: "scikit-learn: Naive Bayes User Guide"
    url: "https://scikit-learn.org/stable/modules/naive_bayes.html"
    description: "Official documentation covering all Naive Bayes variants"
  - title: "A Tutorial on Naive Bayes (Nir Friedman)"
    url: "https://www.cs.ubbcluj.ro/~gabis/ml/farabook/files/farututtorial.htm"
    description: "Nir Friedman's classic tutorial on Naive Bayes"
  - title: "A Comparison of Event Models for Naive Bayes Text Classification"
    url: "https://www.cs.cmu.edu/~tom/ml/publications/EventModels_NaiveBayes.pdf"
    description: "McCallum & Nigam's comparison of Multinomial vs Bernoulli models"
  - title: "Stanford NLP: Naive Bayes for Text Classification"
    url: "https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html"
    description: "Stanford's IR book chapter on Naive Bayes for NLP"
  - title: "Wikipedia: Naive Bayes Classifier"
    url: "https://en.wikipedia.org/wiki/Naive_Bayes_classifier"
    description: "Comprehensive mathematical treatment of all variants"
knowledge_refs:
  - ml-07-logistic-regression
  - ml-18-classification-metrics
  - ml-03-the-learning-problem
---

# Naive Bayes

Naive Bayes is a family of probabilistic classifiers based on **Bayes' theorem** with a strong (naive) assumption that features are conditionally independent given the class. Despite this unrealistic assumption, it works remarkably well in practice — especially for text classification.

## Bayes' Theorem

$$P(y \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid y) \cdot P(y)}{P(\mathbf{x})}$$

- $P(y \mid \mathbf{x})$: **Posterior** — what we want to predict
- $P(\mathbf{x} \mid y)$: **Likelihood** — how likely the features are given the class
- $P(y)$: **Prior** — how common each class is
- $P(\mathbf{x})$: **Evidence** — constant across classes, can be ignored

## The Naive Assumption

Computing $P(\mathbf{x} \mid y)$ directly is intractable (exponentially many feature combinations). The **naive independence assumption** factorizes it:

$$P(\mathbf{x} \mid y) = \prod_{j=1}^{D} P(x_j \mid y)$$

This reduces the problem from exponential to linear in the number of features.

**Why it works despite being "wrong":**
- Even with correlated features, the independence assumption can produce correct classifications
- The ranking of class probabilities is often preserved even if absolute probabilities are wrong
- For text classification, words are far from independent, but NB still performs well

## Multinomial Naive Bayes (Text Classification)

The most common variant for text. Features are word counts or TF-IDF values:

$$P(\text{class} \mid \text{words}) \propto P(\text{class}) \prod_{w \in \text{document}} P(w \mid \text{class})$$

Each word probability is estimated from training data:
$$P(w \mid c) = \frac{\text{count}(w, c) + \alpha}{\sum_{w'} (\text{count}(w', c) + \alpha)}$$

where $\alpha$ is Laplace smoothing (typically $\alpha = 1$).

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

nb_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000, ngram_range=(1, 2))),
    ('nb', MultinomialNB(alpha=1.0))
])
nb_pipeline.fit(texts_train, labels_train)
accuracy = nb_pipeline.score(texts_test, labels_test)
```

## Gaussian Naive Bayes (Continuous Features)

For continuous features, assume each feature follows a Gaussian distribution:

$$P(x_j \mid y) = \frac{1}{\sqrt{2\pi\sigma_{jy}^2}} \exp\left(-\frac{(x_j - \mu_{jy})^2}{2\sigma_{jy}^2}\right)$$

Parameters $\mu_{jy}$ and $\sigma_{jy}^2$ are estimated from training data.

```python
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(X_train, y_train)
```

## Bernoulli Naive Bayes

For binary features (word presence/absence instead of counts):

$$P(x_j \mid y) = P(x_j=1 \mid y)^{x_j} (1-P(x_j=1 \mid y))^{1-x_j}$$

Better than Multinomial for short texts where word frequency isn't informative.

## Complement Naive Bayes

Designed for imbalanced datasets. Instead of modeling each class separately, it models the "complement" (all other classes):

```python
from sklearn.naive_bayes import ComplementNB

cnb = ComplementNB(alpha=1.0)
cnb.fit(X_train, y_train)
```

Often outperforms Multinomial NB on imbalanced text classification.

## Laplace Smoothing

Without smoothing, a word that never appears in a class gets $P(w \mid c) = 0$, which zeroes out the entire posterior. Laplace (add-$\alpha$) smoothing fixes this:

$$P(w \mid c) = \frac{\text{count}(w, c) + \alpha}{\text{total words in c} + \alpha \cdot |V|}$$

where $|V|$ is the vocabulary size. $\alpha = 1$ is the standard default.

## Strengths

- **Extremely fast**: Training is $O(N \cdot D)$, prediction is $O(D)$
- **Works with small data**: Estimation is simple and stable
- **Handles high dimensions**: Scales linearly with features
- **Great for text**: Multinomial NB is a strong baseline for document classification
- **No tuning needed**: Works well with default parameters
- **Probabilistic output**: Gives calibrated probabilities (with caveat below)

## Limitations

- **Independence assumption**: Correlated features hurt performance
- **Poor probability calibration**: Often produces extreme probabilities (near 0 or 1)
- **Zero frequency problem**: Even with smoothing, rare features cause issues
- **Not competitive with modern methods**: For large, complex datasets

## When to Use Naive Bayes

| Use Case | Why NB Works |
|---|---|
| Spam detection | Word counts are approximately independent |
| Sentiment analysis | Bag-of-words captures enough signal |
| Topic classification | Words co-occur in predictable patterns |
| Quick baseline | Trains in milliseconds, gives you a performance floor |
| Small dataset | NB needs less data than complex models |
| Multi-class problems | Naturally handles $K > 2$ classes |

## Practical Tips

1. **Use TF-IDF, not raw counts** for Multinomial NB
2. **Tune $\alpha$** (smoothing parameter) via cross-validation — default 1.0 is often good
3. **Bigrams help**: `ngram_range=(1,2)` captures common phrases
4. **Calibrate probabilities** if needed:
   ```python
   from sklearn.calibration import CalibratedClassifierCV
   calibrated_nb = CalibratedClassifierCV(nb, cv=5, method='isotonic')
   ```
5. **Complement NB** for imbalanced classes
6. **Bernoulli NB** for binary features (short texts, presence/absence)

## Naive Bayes vs. Logistic Regression

Interestingly, Naive Bayes and logistic regression converge to the same solution given infinite data. NB converges faster (needs less data) but has higher asymptotic error. With limited data, NB often wins. With lots of data, logistic regression wins.

## Further Reading

- McCallum & Nigam's event models paper is essential for understanding Multinomial vs Bernoulli NB
- Stanford NLP chapter covers the text classification application in depth
- For better text classification, consider fastText (which extends NB ideas with embeddings)
