---
slug: nlp-01-what-is-nlp
title: "What Is NLP?"
description: "The field that enables machines to understand, interpret, and generate human language — from rule-based systems to neural language models."
order: 1
tags:
  - nlp
  - fundamentals
  - language-models
prerequisites:
  - dl-01-what-is-deep-learning
  - ml-01-what-is-machine-learning
references:
  - title: "Speech and Language Processing (Jurafsky & Martin)"
    url: "https://web.stanford.edu/~jurafsky/slp3/"
    description: "The authoritative NLP textbook — free online third edition"
  - title: "Stanford CS224n: NLP with Deep Learning"
    url: "https://web.stanford.edu/class/cs224n/"
    description: "Stanford's flagship NLP course"
  - title: "Hugging Face NLP Course"
    url: "https://huggingface.co/learn/nlp-course"
    description: "Practical NLP course with transformers"
  - title: "NLTK Book: Natural Language Processing with Python"
    url: "https://www.nltk.org/book/"
    description: "The classic NLP tutorial with Python"
  - title: "spaCy Documentation"
    url: "https://spacy.io/"
    description: "Production-ready NLP library"
knowledge_refs:
  - dl-17-transformers
  - dl-18-attention-mechanisms
  - nlp-06-word-embeddings
---

# What Is NLP?

Natural Language Processing (NLP) is a field of AI that enables machines to understand, interpret, and generate human language. It's one of the most impactful applications of AI — powering search engines, chatbots, translation, and content generation.

## The Goal of NLP

Human language is ambiguous, context-dependent, and full of nuance:
- "I saw her duck" — Did she duck, or did I see her pet duck?
- "The bank is closed" — River bank or financial bank?
- Sarcasm, idioms, cultural references

NLP aims to bridge the gap between human communication and computer understanding.

## Key NLP Tasks

### Understanding Tasks
| Task | Description | Example |
|---|---|---|
| **Text Classification** | Assign category to text | Spam detection, sentiment |
| **Named Entity Recognition** | Extract entities from text | "Apple" → ORG |
| **Sentiment Analysis** | Determine emotional tone | Positive/Negative/Neutral |
| **Question Answering** | Answer questions from text | "When was Python created?" → "1991" |
| **Text Summarization** | Condense text to key points | Article → 3-sentence summary |

### Generation Tasks
| Task | Description | Example |
|---|---|---|
| **Text Generation** | Create new text | Story writing, completion |
| **Machine Translation** | Translate between languages | English → French |
| **Dialogue Systems** | Conversational AI | Chatbots, assistants |
| **Text-to-Speech** | Convert text to audio | Screen readers |
| **Paraphrasing** | Rewrite text differently | Formal → casual |

## A Brief History

| Era | Approach | Example |
|---|---|---|
| 1950s-1970s | Rule-based | ELIZA chatbot |
| 1980s-1990s | Statistical | HMMs, n-grams |
| 2000s-2013 | Feature engineering | SVMs + handcrafted features |
| 2013-2017 | Neural embeddings | Word2Vec, GloVe, LSTM |
| 2017-Present | Transformers | BERT, GPT, T5 |

## The Modern NLP Stack

```
Raw Text
    ↓
[Tokenization] → Split into tokens
    ↓
[Preprocessing] → Clean, normalize
    ↓
[Model] → Understand or generate
    ↓
[Post-processing] → Format output
```

## NLP vs. Other AI Tasks

| Aspect | NLP | Computer Vision | Speech |
|---|---|---|---|
| Input | Text sequences | Image pixels | Audio waveforms |
| Structure | Sequential | Grid | Sequential |
| Key challenge | Ambiguity | Variation | Noise |
| Modern approach | Transformers | CNNs/ViTs | Transformers |

## What You'll Learn in This Course

1. **Text representation**: How to turn text into numbers
2. **Preprocessing**: Cleaning and normalizing text
3. **Classical NLP**: Regex, n-grams, TF-IDF
4. **Word embeddings**: Word2Vec, GloVe, FastText
5. **Deep learning for NLP**: RNNs, LSTMs, Transformers
6. **Modern NLP**: BERT, GPT, fine-tuning
7. **Applications**: Classification, NER, QA, summarization
8. **Evaluation**: BLEU, ROUGE, perplexity
9. **Production**: Deploying NLP models

## Further Reading

- Jurafsky & Martin's textbook is the definitive NLP reference
- Stanford CS224n covers modern neural NLP
- Hugging Face's course is the practical starting point
- NLTK and spaCy are the essential NLP libraries
