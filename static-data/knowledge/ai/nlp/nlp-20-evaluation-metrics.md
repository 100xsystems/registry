---
{
  "title": "NLP Evaluation Metrics",
  "description": "Perplexity, BLEU, ROUGE and human judgment — measuring language models honestly.",
  "type": "lesson",
  "order": 20,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compute perplexity for language models",
    "Use BLEU for translation",
    "Use ROUGE for summarization",
    "Know when human evaluation is essential"
  ],
  "knowledge_refs": [
    "nlp/nlp-20-evaluation-metrics"
  ],
  "prerequisites": [
    "NLP-19: Text Summarization"
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

# NLP-20-EVALUATION-METRICS: NLP Evaluation Metrics

## Introduction

Perplexity, BLEU, ROUGE and human judgment — measuring language models honestly. By the end of this lesson you will be able to: Compute perplexity for language models; Use BLEU for translation; Use ROUGE for summarization; Know when human evaluation is essential.

## Key Concepts

### 1. Compute perplexity for language models

Target: Compute perplexity for language models. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn.functional as F

# Perplexity = exp(cross-entropy)
logits = torch.randn(1, 20, 1000)
target = torch.randint(0, 1000, (1, 20))
ce = F.cross_entropy(logits.view(-1, 1000), target.view(-1))
print("perplexity:", round(torch.exp(ce).item(), 2))
```
### 2. Use BLEU for translation

Target: Use BLEU for translation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from nltk.translate.bleu_score import sentence_bleu

ref = [["the", "cat", "sat"]]
cand = ["the", "cat", "sat"]
print("BLEU:", round(sentence_bleu(ref, cand), 3))
```
### 3. Use ROUGE for summarization

Target: Use ROUGE for summarization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"])
print(scorer.score("the cat sat", "the cat sat down"))
```
### 4. Know when human evaluation is essential

Target: Know when human evaluation is essential. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("automatic metrics correlate, but humans decide quality")
```

## Practice Questions

1. What is the key idea behind "NLP Evaluation Metrics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain NLP Evaluation Metrics with analogies and real-world examples"
1. "Show me common mistakes beginners make with NLP Evaluation Metrics"
1. "Provide advanced patterns and performance considerations for NLP Evaluation Metrics"

## Key Takeaways

- Master the core ideas of NLP Evaluation Metrics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
