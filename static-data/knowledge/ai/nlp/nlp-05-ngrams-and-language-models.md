---
slug: nlp-05-ngrams-and-language-models
title: "N-grams & Language Models"
description: "Predicting the next word — from simple n-gram counts to neural language models."
order: 5
tags:
  - nlp
  - n-grams
  - language-models
  - perplexity
  - smoothing
prerequisites:
  - nlp-02-text-representation
  - nlp-03-text-preprocessing
  - ml-07-logistic-regression
references:
  - title: "Speech and Language Processing: N-grams"
    url: "https://web.stanford.edu/~jurafsky/slp3/4.pdf"
    description: "Jurafsky & Martin's chapter on n-gram language models"
  - title: "A Neural Probabilistic Language Model (Bengio et al.)"
    url: "https://jmlr.org/papers/v3/bengio03a.html"
    description: "Bengio et al.'s foundational neural language model paper"
  - title: "CS224n: Language Models"
    url: "https://web.stanford.edu/class/cs224n/"
    description: "Stanford's NLP course covering language modeling"
  - title: "NLTK Language Model Tools"
    url: "https://www.nltk.org/howto/lanes.html"
    description: "NLTK's language modeling utilities"
  - title: "Hugging Face: Language Models"
    url: "https://huggingface.co/docs/transformers/language_model"
    description: "Modern transformer-based language models"
knowledge_refs:
  - nlp-02-text-representation
  - dl-17-transformers
  - genai-03-text-generation-basics
---

# N-grams & Language Models

Language models predict the probability of the next word in a sequence. They're the foundation of text generation, speech recognition, and machine translation.

## The Language Modeling Task

Given a sequence of words, predict the next word:
$$P(w_t | w_1, w_2, \ldots, w_{t-1})$$

**Example:**
```
"The cat sat on the" → P("mat" | "The cat sat on the") = 0.3
                      → P("floor" | "The cat sat on the") = 0.2
                      → P("table" | "The cat sat on the") = 0.15
```

## N-gram Language Models

Approximate the full history with the last $n-1$ words:
$$P(w_t | w_1, \ldots, w_{t-1}) \approx P(w_t | w_{t-n+1}, \ldots, w_{t-1})$$

### Unigram Model (n=1)
Each word independent:
$$P(w_t) = \frac{\text{count}(w_t)}{\text{total words}}$$

### Bigram Model (n=2)
Each word depends on previous word:
$$P(w_t | w_{t-1}) = \frac{\text{count}(w_{t-1}, w_t)}{\text{count}(w_{t-1})}$$

### Trigram Model (n=3)
Each word depends on previous two words:
$$P(w_t | w_{t-2}, w_{t-1}) = \frac{\text{count}(w_{t-2}, w_{t-1}, w_t)}{\text{count}(w_{t-2}, w_{t-1})}$$

```python
from collections import defaultdict, Counter

def build_bigram_model(corpus):
    bigrams = defaultdict(Counter)
    for sentence in corpus:
        for i in range(len(sentence) - 1):
            bigrams[sentence[i]][sentence[i+1]] += 1
    
    # Convert counts to probabilities
    model = {}
    for word, next_words in bigrams.items():
        total = sum(next_words.values())
        model[word] = {w: c/total for w, c in next_words.items()}
    return model

corpus = [["the", "cat", "sat"], ["the", "dog", "ran"], ["the", "cat", "ran"]]
model = build_bigram_model(corpus)
print(model["the"])  # {'cat': 0.67, 'dog': 0.33}
```

## Smoothing

Handle unseen n-grams (zero probabilities):

### Laplace (Add-1) Smoothing
$$P(w_t | w_{t-1}) = \frac{\text{count}(w_{t-1}, w_t) + 1}{\text{count}(w_{t-1}) + V}$$

where $V$ is vocabulary size.

### Kneser-Ney Smoothing
Better smoothing using lower-order distributions.

## Perplexity

Measures how well a language model predicts text:
$$\text{PPL} = 2^{-\frac{1}{N}\sum_{i=1}^{N}\log_2 P(w_i | w_{<i})}$$

**Lower perplexity = better model**. A perplexity of 100 means the model is as confused as if it had to choose uniformly among 100 words.

```python
import math

def perplexity(model, test_corpus):
    log_prob = 0
    n = 0
    for sentence in test_corpus:
        for i in range(1, len(sentence)):
            word = sentence[i]
            prev = sentence[i-1]
            prob = model.get(prev, {}).get(word, 1e-10)
            log_prob += math.log2(prob)
            n += 1
    return 2 ** (-log_prob / n)
```

## Neural Language Models

### Feedforward (Bengio et al., 2003)
First neural language model:
- Embed previous $n-1$ words
- Pass through hidden layers
- Output probability over vocabulary

### Recurrent (RNN/LSTM)
Process unlimited context:
- Maintain hidden state across time steps
- Can model long-range dependencies
- But slow (sequential processing)

### Transformer (GPT, BERT)
Self-attention over full context:
- Parallel processing
- Better long-range dependencies
- State-of-the-art performance

## N-grams vs. Neural Models

| Aspect | N-grams | Neural LMs |
|---|---|---|
| Context | Fixed (n-1 words) | Unlimited |
| Training | Counting | Gradient descent |
| Parameters | Sparse table | Dense matrices |
| Generalization | Poor for unseen | Better |
| Speed | Very fast | Slow |

## Practical Applications

| Application | How LMs Help |
|---|---|
| **Autocomplete** | Predict next word |
| **Spell checking** | Find likely corrections |
| **Speech recognition** | Disambiguate phonetically similar words |
| **Machine translation** | Generate fluent output |
| **Text generation** | Create coherent text |

## Further Reading

- Jurafsky & Martin Chapter 4 is the definitive n-gram reference
- Bengio et al. (2003) started neural language modeling
- Stanford CS224n covers modern language models
- For modern LLMs: see the GenAI course's text generation lessons
