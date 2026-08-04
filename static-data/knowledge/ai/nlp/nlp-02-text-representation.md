---
slug: nlp-02-text-representation
title: "Text Representation: From Tokens to Vectors"
description: "How to turn text into numbers — one-hot encoding, bag-of-words, TF-IDF, and word embeddings."
order: 2
tags:
  - nlp
  - text-representation
  - tf-idf
  - bag-of-words
  - embeddings
prerequisites:
  - nlp-01-what-is-nlp
  - nlp-03-text-preprocessing
references:
  - title: "Word Embeddings in NLP (GeeksforGeeks)"
    url: "https://www.geeksforgeeks.org/nlp/word-embeddings-in-nlp/"
    description: "Comprehensive overview of text vectorization methods"
  - title: "Bag-of-Words and TF-IDF (Analytics Vidhya)"
    url: "https://www.analyticsvidhya.com/blog/2020/02/quick-introduction-bag-of-words-bow-tf-idf/"
    description: "Practical walkthrough of frequency-based representations"
  - title: "Word Embeddings Guide (TensorFlow)"
    url: "https://www.tensorflow.org/text/guide/word_embeddings"
    description: "Official TensorFlow tutorial on word embeddings"
  - title: "Word Embeddings Tutorial (PyTorch)"
    url: "https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html"
    description: "PyTorch tutorial on embedding layers"
  - title: "Text Vectorization Guide (Analytics Vidhya)"
    url: "https://www.analyticsvidhya.com/blog/2021/06/part-5-step-by-step-guide-to-master-nlp-text-vectorization-approaches/"
    description: "Step-by-step guide to text vectorization approaches"
knowledge_refs:
  - nlp-01-what-is-nlp
  - nlp-06-word-embeddings
  - dl-08-pytorch-tensors-and-autograd
---

# Text Representation: From Tokens to Vectors

Computers can't process raw text — they need numbers. Text representation is the process of converting text into numerical vectors that machine learning models can understand.

## The Evolution of Text Representation

```
One-Hot Encoding → Bag-of-Words → TF-IDF → Word2Vec/GloVe → Contextual Embeddings
(sparse, no semantics)                                    (dense, contextual)
```

## One-Hot Encoding

Each word becomes a binary vector of vocabulary size:
```python
vocab = {"cat": 0, "dog": 1, "fish": 2}
# "cat" → [1, 0, 0]
# "dog" → [0, 1, 0]
```

**Problem**: No semantic similarity — "cat" and "dog" are equally distant from each other.

## Bag-of-Words (BoW)

Count word frequencies in each document:
```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = ["the cat sat", "the dog sat", "the cat chased the dog"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())  # ['cat', 'chased', 'dog', 'sat', 'the']
print(X.toarray())
# [[1, 0, 0, 1, 1],
#  [0, 0, 1, 1, 1],
#  [1, 1, 1, 1, 2]]
```

**Advantages**: Simple, fast, works well for many tasks
**Disadvantages**: Ignores word order, no semantics, sparse vectors

## TF-IDF (Term Frequency-Inverse Document Frequency)

Weights words by importance — rare words get higher weight:
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
# Rare words like "chased" get higher TF-IDF than common words like "the"
```

**How it works:**
- **TF**: How often does word appear in this document? (frequency)
- **IDF**: How rare is this word across all documents? (importance)
- **TF-IDF**: Product of TF and IDF (informative words highlighted)

## N-grams

Capture local word order:
```python
# Unigrams: ["the", "cat", "sat"]
# Bigrams:  ["the cat", "cat sat"]
# Trigrams: ["the cat sat"]

vectorizer = TfidfVectorizer(ngram_range=(1, 2))  # unigrams + bigrams
X = vectorizer.fit_transform(corpus)
```

## Word Embeddings

Dense vectors that capture semantic meaning:
```python
from gensim.models import Word2Vec

sentences = [["I", "love", "NLP"], ["NLP", "is", "great"], ["I", "love", "AI"]]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

# Similar words have similar vectors
print(model.wv.most_similar("NLP"))  # [('AI', 0.95), ('great', 0.87), ...]
```

**Key property**: Similar words are close in vector space.

## Comparison

| Method | Dimensions | Semantics | Speed | Use Case |
|---|---|---|---|---|
| One-Hot | |V| | None | Fast | Simple baselines |
| BoW | |V| | None | Fast | Text classification |
| TF-IDF | |V| | None | Fast | Search, classification |
| Word2Vec | 100-300 | Yes | Medium | Semantic similarity |
| BERT | 768 | Yes (contextual) | Slow | Modern NLP tasks |

## Practical Tips

1. **TF-IDF is a strong baseline**: Try it before complex models
2. **Word embeddings help**: Use pretrained GloVe/Word2Vec
3. **Contextual embeddings win**: BERT/transformers for modern NLP
4. **Feature selection**: Remove rare words to reduce dimensionality
5. **Normalization**: Always lowercase and remove punctuation

## Further Reading

- GeeksforGeeks' word embeddings guide covers all methods
- Analytics Vidhya's TF-IDF walkthrough is practical
- TensorFlow and PyTorch tutorials cover embeddings hands-on
- For modern NLP: contextual embeddings (BERT) have largely replaced static embeddings
