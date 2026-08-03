---
{
  "title": "Tokenization & the Vocabulary",
  "description": "Subword tokens (BPE) — the hidden layer between characters and embeddings.",
  "type": "lesson",
  "order": 7,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain byte-pair encoding (BPE)",
    "Inspect tokenizers with tiktoken/Hugging Face",
    "Understand token cost for APIs",
    "Handle edge cases in tokenization"
  ],
  "knowledge_refs": [
    "generative-ai/genai-06-llm-architecture",
    "llm-engineering/llm-05-tokenization-and-context",
    "nlp/nlp-02-text-representation"
  ],
  "prerequisites": [
    "GENAI-03: Text Generation Fundamentals"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "Transformers, fine-tuning and LLM fundamentals with hands-on code."
    },
    {
      "title": "OpenAI Documentation",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for GPT models, embeddings and function calling."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The Transformer paper that made generative AI possible."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "DeepLearning.AI Short Courses",
      "url": "https://www.deeplearning.ai/short-courses/",
      "description": "Practical AI courses from industry experts."
    }
  ]
}
---

# GENAI-07-TOKENIZATION: Tokenization & the Vocabulary

## Introduction

Subword tokens (BPE) — the hidden layer between characters and embeddings. By the end of this lesson you will be able to: Explain byte-pair encoding (BPE); Inspect tokenizers with tiktoken/Hugging Face; Understand token cost for APIs; Handle edge cases in tokenization.

## Key Concepts

### 1. Explain byte-pair encoding (BPE)

Target: Explain byte-pair encoding (BPE). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("hello world")
print("tokens:", tokens, "->", [enc.decode([t]) for t in tokens])
```
### 2. Inspect tokenizers with tiktoken/Hugging Face

Target: Inspect tokenizers with tiktoken/Hugging Face. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("gpt2")
print(tok.tokenize("unhappiness"))
```
### 3. Understand token cost for APIs

Target: Understand token cost for APIs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
print("1 char:", len(enc.encode("a")))
print("10 words:", len(enc.encode("the quick brown fox jumps over the lazy dog")))
```
### 4. Handle edge cases in tokenization

Target: Handle edge cases in tokenization. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("tokenization is invisible but drives cost and behavior")
```

## Practice Questions

1. What is the key idea behind "Tokenization & the Vocabulary"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tokenization & the Vocabulary with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tokenization & the Vocabulary"
1. "Provide advanced patterns and performance considerations for Tokenization & the Vocabulary"

## Key Takeaways

- Master the core ideas of Tokenization & the Vocabulary through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
