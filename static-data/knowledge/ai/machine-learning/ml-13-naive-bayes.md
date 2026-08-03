---
{
  "title": "Naive Bayes",
  "description": "Bayes' rule applied to text and beyond — fast, simple, and shockingly effective on the right problems.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "State Bayes' rule in plain terms",
    "Explain the naive independence assumption",
    "Fit a MultinomialNB text classifier",
    "Know when Naive Bayes is a good first choice"
  ],
  "knowledge_refs": [
    "machine-learning/ml-13-naive-bayes"
  ],
  "prerequisites": [
    "ML-07: Logistic Regression"
  ],
  "references": [
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "The authoritative guide to the Python ML toolbox."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Hands-On Machine Learning — Aurélien Géron",
      "url": "https://github.com/ageron/handson-ml3",
      "description": "Practical ML with scikit-learn, Keras and TensorFlow."
    },
    {
      "title": "Andrew Ng — Machine Learning Specialization",
      "url": "https://www.coursera.org/specializations/machine-learning-introduction",
      "description": "The most popular introductory ML course in the world."
    },
    {
      "title": "Kaggle Learn — Intro to Machine Learning",
      "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
      "description": "Hands-on micro-course for the fundamentals."
    }
  ]
}
---

# ML-13-NAIVE-BAYES: Naive Bayes

## Introduction

Bayes' rule applied to text and beyond — fast, simple, and shockingly effective on the right problems. By the end of this lesson you will be able to: State Bayes' rule in plain terms; Explain the naive independence assumption; Fit a MultinomialNB text classifier; Know when Naive Bayes is a good first choice.

## Key Concepts

### 1. State Bayes' rule in plain terms

Target: State Bayes' rule in plain terms. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.naive_bayes import MultinomialNB

X = [[2, 1, 0], [1, 2, 0], [0, 1, 3], [0, 0, 4]]
y = [0, 0, 1, 1]
clf = MultinomialNB().fit(X, y)
print("pred:", clf.predict([[1, 1, 1]])[0])
```
### 2. Explain the naive independence assumption

Target: Explain the naive independence assumption. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["cheap pills now", "free money", "meeting at noon", "lunch tomorrow"]
y = [1, 1, 0, 0]
X = CountVectorizer().fit_transform(texts)
clf = MultinomialNB().fit(X, y)
print("spam prob:", clf.predict_proba(CountVectorizer().transform(["free money now"]))[0][1].round(3))
```
### 3. Fit a MultinomialNB text classifier

Target: Fit a MultinomialNB text classifier. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.naive_bayes import GaussianNB

X = [[1.0, 2.0], [1.2, 1.8], [5.0, 5.2], [5.5, 4.8]]
y = [0, 0, 1, 1]
clf = GaussianNB().fit(X, y)
print("pred:", clf.predict([[2.0, 2.0]])[0])
```
### 4. Know when Naive Bayes is a good first choice

Target: Know when Naive Bayes is a good first choice. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Prior updates: P(A|B) = P(B|A) P(A) / P(B)
p_a = 0.01
test_sens = 0.99
test_spec = 0.95
p_b_given_a = test_sens
p_b = test_sens * p_a + (1 - test_spec) * (1 - p_a)
p_a_given_b = p_b_given_a * p_a / p_b
print("P(disease | positive):", round(p_a_given_b, 3))
```

## Practice Questions

1. What is the key idea behind "Naive Bayes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Naive Bayes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Naive Bayes"
1. "Provide advanced patterns and performance considerations for Naive Bayes"

## Key Takeaways

- Master the core ideas of Naive Bayes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
