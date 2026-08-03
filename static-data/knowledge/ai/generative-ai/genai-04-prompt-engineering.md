---
{
  "title": "Prompt Engineering",
  "description": "Design instructions that get reliable outputs: roles, structure, few-shot examples and constraints.",
  "type": "lesson",
  "order": 4,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Structure prompts with roles and tasks",
    "Use few-shot examples effectively",
    "Constrain output format (JSON, bullet, length)",
    "Iterate on prompts systematically"
  ],
  "knowledge_refs": [
    "generative-ai/genai-04-prompt-engineering"
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

# GENAI-04-PROMPT-ENGINEERING: Prompt Engineering

## Introduction

Design instructions that get reliable outputs: roles, structure, few-shot examples and constraints. By the end of this lesson you will be able to: Structure prompts with roles and tasks; Use few-shot examples effectively; Constrain output format (JSON, bullet, length); Iterate on prompts systematically.

## Key Concepts

### 1. Structure prompts with roles and tasks

Target: Structure prompts with roles and tasks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
system = "You are a senior backend engineer."
user = "Review this code for race conditions: ..."
print(system, "|", user)
```
### 2. Use few-shot examples effectively

Target: Use few-shot examples effectively. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Summarize in one sentence: ..."}],
)
print(res.choices[0].message.content)
```
### 3. Constrain output format (JSON, bullet, length)

Target: Constrain output format (JSON, bullet, length). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
prompt = """Extract into JSON: {"name": ..., "price": ...}
Item: "Wireless mouse, $29"
Answer: {"name": "Wireless mouse", "price": 29}
"""
print(prompt)
```
### 4. Iterate on prompts systematically

Target: Iterate on prompts systematically. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("evaluate prompts on a fixed eval set, not vibes")
```

## Practice Questions

1. What is the key idea behind "Prompt Engineering"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompt Engineering with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompt Engineering"
1. "Provide advanced patterns and performance considerations for Prompt Engineering"

## Key Takeaways

- Master the core ideas of Prompt Engineering through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
