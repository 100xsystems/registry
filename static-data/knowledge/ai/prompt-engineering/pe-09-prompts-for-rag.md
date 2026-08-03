---
{
  "title": "Prompting for RAG",
  "description": "Write retrieval-grounded prompts: cite sources, handle missing context, stay faithful.",
  "type": "lesson",
  "order": 9,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Ground answers in provided context",
    "Handle missing information honestly",
    "Require citations",
    "Prevent hallucination beyond context"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-08-prompts-for-images",
    "llm-engineering/llm-07-rag-engineering",
    "llm-engineering/llm-08-advanced-rag"
  ],
  "prerequisites": [
    "LLM-07: RAG Engineering"
  ],
  "references": [
    {
      "title": "OpenAI Prompt Engineering Guide",
      "url": "https://platform.openai.com/docs/guides/prompt-engineering",
      "description": "Six strategies for reliable prompting from OpenAI."
    },
    {
      "title": "Anthropic Prompt Engineering Docs",
      "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering",
      "description": "Claude's practical prompt engineering guide."
    },
    {
      "title": "Prompt Engineering Guide (DAIR.AI)",
      "url": "https://www.promptingguide.ai/",
      "description": "A broad open-source guide to prompt techniques."
    },
    {
      "title": "CoT: Chain-of-Thought Prompting",
      "url": "https://arxiv.org/abs/2201.11903",
      "description": "The paper on reasoning via chain-of-thought prompts."
    },
    {
      "title": "ReAct: Reasoning + Acting",
      "url": "https://arxiv.org/abs/2210.03629",
      "description": "Combining reasoning traces with tool actions."
    }
  ]
}
---

# PE-09-PROMPTS-FOR-RAG: Prompting for RAG

## Introduction

Write retrieval-grounded prompts: cite sources, handle missing context, stay faithful. By the end of this lesson you will be able to: Ground answers in provided context; Handle missing information honestly; Require citations; Prevent hallucination beyond context.

## Key Concepts

### 1. Ground answers in provided context

Target: Ground answers in provided context. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
rag_prompt = """Answer using ONLY the context below. If the answer is not in the context, say "I don't have that information."\n\nContext: {context}\n\nQuestion: {question}"""
print(rag_prompt)
```
### 2. Handle missing information honestly

Target: Handle missing information honestly. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("instruct: quote sources, don't invent")
```
### 3. Require citations

Target: Require citations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("missing context -> explicit refusal beats guessing")
```
### 4. Prevent hallucination beyond context

Target: Prevent hallucination beyond context. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("evals: faithfulness (does it stick to context?)")
```

## Practice Questions

1. What is the key idea behind "Prompting for RAG"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompting for RAG with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompting for RAG"
1. "Provide advanced patterns and performance considerations for Prompting for RAG"

## Key Takeaways

- Master the core ideas of Prompting for RAG through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
