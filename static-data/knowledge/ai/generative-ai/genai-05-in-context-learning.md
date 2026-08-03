---
{
  "title": "In-Context Learning",
  "description": "Teach new tasks with examples in the prompt — no weight updates required.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain in-context learning (ICL)",
    "Show zero-shot vs few-shot differences",
    "Understand context window limits",
    "Use ICL with structured examples"
  ],
  "knowledge_refs": [
    "generative-ai/genai-04-prompt-engineering",
    "prompt-engineering/pe-03-roles-and-context",
    "llm-engineering/llm-12-context-engineering"
  ],
  "prerequisites": [
    "GENAI-04: Prompt Engineering"
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

# GENAI-05-IN-CONTEXT-LEARNING: In-Context Learning

## Introduction

Teach new tasks with examples in the prompt — no weight updates required. By the end of this lesson you will be able to: Explain in-context learning (ICL); Show zero-shot vs few-shot differences; Understand context window limits; Use ICL with structured examples.

## Key Concepts

### 1. Explain in-context learning (ICL)

Target: Explain in-context learning (ICL). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
zero_shot = "Is this review positive or negative? \"terrible product\""
print(zero_shot)
```
### 2. Show zero-shot vs few-shot differences

Target: Show zero-shot vs few-shot differences. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
few_shot = """Classify sentiment.\n\"love it\" -> positive\n\"hate it\" -> negative\n\"it was okay\" -> neutral\n\"amazing\" ->"""
print(few_shot)
```
### 3. Understand context window limits

Target: Understand context window limits. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
print("tokens in prompt:", len(enc.encode("the quick brown fox")))
```
### 4. Use ICL with structured examples

Target: Use ICL with structured examples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("context window: model sees only what fits in the prompt")
```

## Practice Questions

1. What is the key idea behind "In-Context Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain In-Context Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with In-Context Learning"
1. "Provide advanced patterns and performance considerations for In-Context Learning"

## Key Takeaways

- Master the core ideas of In-Context Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
