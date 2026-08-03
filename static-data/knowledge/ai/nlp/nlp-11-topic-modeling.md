---
{
  "title": "Topic Modeling with LDA",
  "description": "Discover latent themes in a corpus with Latent Dirichlet Allocation.",
  "type": "lesson",
  "order": 11,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the LDA generative story",
    "Fit an LDA model with gensim or scikit-learn",
    "Interpret topic-word distributions",
    "Choose the number of topics"
  ],
  "knowledge_refs": [
    "nlp/nlp-11-topic-modeling"
  ],
  "prerequisites": [
    "NLP-02: Text Representation: From Tokens to Vectors"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "The hands-on course for transformers and modern NLP."
    },
    {
      "title": "Speech and Language Processing — Jurafsky & Martin",
      "url": "https://web.stanford.edu/~jurafsky/slp3/",
      "description": "The standard textbook for NLP (free draft)."
    },
    {
      "title": "Stanford CS224n",
      "url": "https://web.stanford.edu/class/cs224n/",
      "description": "Natural Language Processing with Deep Learning."
    },
    {
      "title": "NLTK Book",
      "url": "https://www.nltk.org/book/",
      "description": "Natural Language Processing with Python — classic fundamentals."
    },
    {
      "title": "spaCy Documentation",
      "url": "https://spacy.io/usage",
      "description": "Industrial-strength NLP library docs."
    }
  ]
}
---

# NLP-11-TOPIC-MODELING: Topic Modeling with LDA

## Introduction

Discover latent themes in a corpus with Latent Dirichlet Allocation. By the end of this lesson you will be able to: Explain the LDA generative story; Fit an LDA model with gensim or scikit-learn; Interpret topic-word distributions; Choose the number of topics.

## Key Concepts

### 1. Explain the LDA generative story

Target: Explain the LDA generative story. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

docs = ["cats and dogs and cats", "dogs chase cats", "stocks rally on earnings", "market rally"]
X = CountVectorizer().fit_transform(docs)
lda = LatentDirichletAllocation(n_components=2, random_state=0).fit(X)
print("topics:", lda.components_.shape)
```
### 2. Fit an LDA model with gensim or scikit-learn

Target: Fit an LDA model with gensim or scikit-learn. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Top words per topic
for t in lda.components_:
    top = np.argsort(t)[-5:]
    print([X_feature_names[i] for i in top])
```
### 3. Interpret topic-word distributions

Target: Interpret topic-word distributions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.feature_extraction.text import CountVectorizer

X_feature_names = CountVectorizer().fit(docs).get_feature_names_out()
print("vocab size:", len(X_feature_names))
```
### 4. Choose the number of topics

Target: Choose the number of topics. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Document-topic mixture: each doc is a blend of topics
print(lda.transform(X).round(2))
```

## Practice Questions

1. What is the key idea behind "Topic Modeling with LDA"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Topic Modeling with LDA with analogies and real-world examples"
1. "Show me common mistakes beginners make with Topic Modeling with LDA"
1. "Provide advanced patterns and performance considerations for Topic Modeling with LDA"

## Key Takeaways

- Master the core ideas of Topic Modeling with LDA through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
