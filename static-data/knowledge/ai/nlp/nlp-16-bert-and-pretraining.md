---
{
  "title": "BERT & Pretrained Language Models",
  "description": "Masked language modeling and the pretrain-then-fine-tune recipe that powers NLP.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain masked language modeling",
    "Describe BERT's bidirectional encoder",
    "Load BERT from Hugging Face",
    "Use embeddings for downstream tasks"
  ],
  "knowledge_refs": [
    "nlp/nlp-16-bert-and-pretraining"
  ],
  "prerequisites": [
    "NLP-15: Attention & Transformers for NLP"
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

# NLP-16-BERT-AND-PRETRAINING: BERT & Pretrained Language Models

## Introduction

Masked language modeling and the pretrain-then-fine-tune recipe that powers NLP. By the end of this lesson you will be able to: Explain masked language modeling; Describe BERT's bidirectional encoder; Load BERT from Hugging Face; Use embeddings for downstream tasks.

## Key Concepts

### 1. Explain masked language modeling

Target: Explain masked language modeling. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
print("BERT loaded")
```
### 2. Describe BERT's bidirectional encoder

Target: Describe BERT's bidirectional encoder. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import BertTokenizer

inputs = tokenizer("the quick brown fox", return_tensors="pt")
print("token ids:", inputs["input_ids"])
```
### 3. Load BERT from Hugging Face

Target: Load BERT from Hugging Face. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

with torch.no_grad():
    out = model(**inputs)
print("cls embedding:", out.last_hidden_state[:, 0].shape)
```
### 4. Use embeddings for downstream tasks

Target: Use embeddings for downstream tasks. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("pretrain: learn language. fine-tune: learn the task.")
```

## Practice Questions

1. What is the key idea behind "BERT & Pretrained Language Models"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain BERT & Pretrained Language Models with analogies and real-world examples"
1. "Show me common mistakes beginners make with BERT & Pretrained Language Models"
1. "Provide advanced patterns and performance considerations for BERT & Pretrained Language Models"

## Key Takeaways

- Master the core ideas of BERT & Pretrained Language Models through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
