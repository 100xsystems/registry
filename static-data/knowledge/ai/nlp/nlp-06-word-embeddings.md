---
slug: nlp-06-word-embeddings
title: "Word Embeddings"
description: "Dense vector representations that capture semantic meaning — Word2Vec, GloVe, FastText, and the distributional hypothesis."
order: 6
tags:
  - nlp
  - embeddings
  - word2vec
  - glove
  - fasttext
prerequisites:
  - nlp-02-text-representation
  - nlp-05-ngrams-and-language-models
  - dl-08-pytorch-tensors-and-autograd
references:
  - title: "Efficient Estimation of Word Representations (Word2Vec)"
    url: "https://arxiv.org/abs/1301.3781"
    description: "Mikolov et al.'s Word2Vec paper introducing CBOW and Skip-gram"
  - title: "GloVe: Global Vectors for Word Representation"
    url: "https://nlp.stanford.edu/pubs/glove.pdf"
    description: "Pennington et al.'s GloVe paper from Stanford NLP"
  - title: "Enriching Word Vectors with Subword Information (FastText)"
    url: "https://arxiv.org/abs/1607.04606"
    description: "Bojanowski et al.'s FastText paper"
  - title: "Word2Vec Tutorial (The Skip-Gram Model)"
    url: "http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/"
    description: "Chris McCormick's clear Word2Vec tutorial"
  - title: "Gensim Word2Vec Documentation"
    url: "https://radimrehurek.com/gensim/models/word2vec.html"
    description: "Gensim's practical Word2Vec implementation guide"
knowledge_refs:
  - nlp-02-text-representation
  - nlp-05-ngrams-and-language-models
  - dl-08-pytorch-tensors-and-autograd
---

# Word Embeddings

Word embeddings map words to dense, continuous vectors where semantic similarity is captured by geometric proximity. They're the foundation of modern NLP.

## The Distributional Hypothesis

"You shall know a word by the company it keeps." — Firth (1957)

Words that appear in similar contexts have similar meanings:
- "The **cat** sat on the mat"
- "The **dog** sat on the mat"

"cat" and "dog" appear in similar contexts → they should have similar embeddings.

## Word2Vec (Mikolov et al., 2013)

Two architectures for learning embeddings:

### Skip-gram
Predict context words from a center word:
```
Input: "cat" → Predict: ["the", "sat", "on"]
```

```python
from gensim.models import Word2Vec

sentences = [["I", "love", "NLP"], ["NLP", "is", "great"], ["I", "love", "AI"]]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1)

# Access embeddings
vector = model.wv["NLP"]  # 100-dimensional vector
similar = model.wv.most_similar("NLP")  # Similar words
```

### CBOW (Continuous Bag of Words)
Predict center word from context:
```
Input: ["the", "cat", "on"] → Predict: "sat"
```

### Skip-gram vs. CBOW

| Aspect | Skip-gram | CBOW |
|---|---|---|
| Training speed | Slower | Faster |
| Rare words | Better | Worse |
| Large datasets | Better | Better |
| Small datasets | Better | Worse |

## GloVe (Global Vectors)

Combines global co-occurrence statistics with local context:
1. Build word-word co-occurrence matrix
2. Factorize using weighted least squares
3. Result: dense embeddings capturing global statistics

```python
import gensim.downloader as api

# Load pretrained GloVe
glove = api.load("glove-wiki-gigaword-100")

# Similar words
print(glove.most_similar("king"))
# [('queen', 0.85), ('prince', 0.77), ('throne', 0.74), ...]

# Word arithmetic
result = glove["king"] - glove["man"] + glove["woman"]
print(glove.most_similar(result))
# [('queen', 0.88), ('throne', 0.76), ...]
```

## FastText

Extends Word2Vec with subword information:
```
"where" → {"<wh", "wh", "h", "he", "ere", "re", "e>"}
```

**Benefits**:
- Handles out-of-vocabulary words
- Works with morphologically rich languages
- Robust to misspellings

```python
from gensim.models import FastText

model = FastText(sentences, vector_size=100, window=5, min_count=1, sg=1)
# Can get vectors for unseen words
vector = model.wv["unseenword"]
```

## Word Arithmetic

Embeddings capture relationships:
```python
# king - man + woman ≈ queen
glove.most_similar(positive=["king", "woman"], negative=["man"])

# Paris - France + Italy ≈ Rome
glove.most_similar(positive=["Paris", "Italy"], negative=["France"])

# walking - walked + swam ≈ swimming
glove.most_similar(positive=["walking", "swam"], negative=["walked"])
```

## Visualization

```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Get embeddings for visualization
words = ["cat", "dog", "fish", "bird", "car", "bus", "train", "plane"]
vectors = [glove[w] for w in words]

# Reduce to 2D
tsne = TSNE(n_components=2, random_state=42)
coords = tsne.fit_transform(vectors)

# Plot
plt.figure(figsize=(10, 8))
for i, word in enumerate(words):
    plt.scatter(coords[i, 0], coords[i, 1])
    plt.annotate(word, (coords[i, 0], coords[i, 1]))
plt.show()
```

## Pretrained Embeddings

| Model | Dimensions | Vocabulary | Source |
|---|---|---|---|
| GloVe 6B | 50-300 | 400K | Wikipedia + Gigaword |
| GloVe 840B | 300 | 2.2M | Common Crawl |
| Word2Vec Google News | 300 | 3M | Google News |
| FastText Wiki | 300 | 2M | Wikipedia |

## Static vs. Contextual Embeddings

| Aspect | Static (Word2Vec) | Contextual (BERT) |
|---|---|---|
| Vector per word | One fixed vector | Different per context |
| "bank" (river) | Same vector | Different vectors |
| Training | Lightweight | Expensive |
| Use case | Traditional NLP | Modern NLP |

## Practical Tips

1. **Use pretrained embeddings** when you have limited data
2. **Fine-tune embeddings** for domain-specific tasks
3. **GloVe 840B** is the best general-purpose static embedding
4. **FastText** for morphologically rich languages
5. **For modern NLP**: Use BERT/GPT contextual embeddings instead

## Further Reading

- Mikolov et al.'s Word2Vec paper started the embedding revolution
- GloVe combined global and local statistics
- FastText handled OOV words via subword information
- For contextual embeddings: see the BERT lesson
