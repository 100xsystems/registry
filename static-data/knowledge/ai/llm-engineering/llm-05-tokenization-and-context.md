---
{
  "title": "Tokenization & Context Management",
  "description": "Budget tokens, count costs, and fit big context into small windows.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Count tokens with tiktoken",
    "Estimate cost per request",
    "Chunk content to fit context",
    "Use token budgets defensively"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-05-tokenization-and-context"
  ],
  "prerequisites": [
    "LLM-03: Working with LLM APIs"
  ],
  "references": [
    {
      "title": "OpenAI Platform Docs",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for chat, embeddings, function calling and vision."
    },
    {
      "title": "Anthropic Documentation",
      "url": "https://docs.anthropic.com/",
      "description": "Claude API docs including prompt engineering guides."
    },
    {
      "title": "Hugging Face Transformers",
      "url": "https://huggingface.co/docs/transformers",
      "description": "Models, tokenizers and pipelines for LLM work."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "vLLM Documentation",
      "url": "https://docs.vllm.ai/",
      "description": "High-throughput LLM serving and inference."
    }
  ]
}
---

# LLM-05-TOKENIZATION-AND-CONTEXT: Tokenization & Context Management

## Introduction

Budget tokens, count costs, and fit big context into small windows. By the end of this lesson you will be able to: Count tokens with tiktoken; Estimate cost per request; Chunk content to fit context; Use token budgets defensively.

## Key Concepts

### 1. Count tokens with tiktoken

Target: Count tokens with tiktoken. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "The quick brown fox jumps over the lazy dog" * 5
print("tokens:", len(enc.encode(text)))
```
### 2. Estimate cost per request

Target: Estimate cost per request. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
cost_per_1k = 0.00015
n = len(enc.encode("some prompt"))
print("cost:", round(n / 1000 * cost_per_1k, 6))
```
### 3. Chunk content to fit context

Target: Chunk content to fit context. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
def fit_to_window(text, max_tokens, enc):
    tokens = enc.encode(text)
    return enc.decode(tokens[:max_tokens])

print("truncated:", fit_to_window("a" * 100, 50, enc)[:20])
```
### 4. Use token budgets defensively

Target: Use token budgets defensively. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("budget: reserve room for the answer in the window")
```

## Practice Questions

1. What is the key idea behind "Tokenization & Context Management"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tokenization & Context Management with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tokenization & Context Management"
1. "Provide advanced patterns and performance considerations for Tokenization & Context Management"

## Key Takeaways

- Master the core ideas of Tokenization & Context Management through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
