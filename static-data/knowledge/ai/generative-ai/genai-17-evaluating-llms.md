---
{
  "title": "Evaluating LLMs",
  "description": "Benchmarks, evals and human review — measuring quality, safety and reliability.",
  "type": "lesson",
  "order": 17,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use standard benchmarks (MMLU, HumanEval)",
    "Build task-specific eval sets",
    "Measure hallucination and grounding",
    "Track evals in CI"
  ],
  "knowledge_refs": [
    "generative-ai/genai-16-audio-and-speech",
    "deep-learning/dl-20-evaluating-deep-models",
    "computer-vision/cv-20-evaluating-vision-models"
  ],
  "prerequisites": [
    "GENAI-08: Fine-Tuning LLMs"
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

# GENAI-17-EVALUATING-LLMS: Evaluating LLMs

## Introduction

Benchmarks, evals and human review — measuring quality, safety and reliability. By the end of this lesson you will be able to: Use standard benchmarks (MMLU, HumanEval); Build task-specific eval sets; Measure hallucination and grounding; Track evals in CI.

## Key Concepts

### 1. Use standard benchmarks (MMLU, HumanEval)

Target: Use standard benchmarks (MMLU, HumanEval). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
benchmarks = {
    "MMLU": "knowledge across 57 subjects",
    "HumanEval": "code generation",
    "GSM8K": "math reasoning",
}
print(benchmarks)
```
### 2. Build task-specific eval sets

Target: Build task-specific eval sets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
eval_set = [
    {"question": "What is 2+2?", "expected": "4"},
    {"question": "Capital of France?", "expected": "Paris"},
]
print("task evals:", len(eval_set))
```
### 3. Measure hallucination and grounding

Target: Measure hallucination and grounding. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Grounding: does the answer cite the provided context?
answer = "Paris (source: doc 3)"
grounded = "doc 3" in answer
print("grounded:", grounded)
```
### 4. Track evals in CI

Target: Track evals in CI. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("regression: run evals on every prompt change")
```

## Practice Questions

1. What is the key idea behind "Evaluating LLMs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Evaluating LLMs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Evaluating LLMs"
1. "Provide advanced patterns and performance considerations for Evaluating LLMs"

## Key Takeaways

- Master the core ideas of Evaluating LLMs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
