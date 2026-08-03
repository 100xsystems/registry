---
{
  "title": "Evaluating LLM Systems",
  "description": "Build evals that catch regressions: golden sets, LLM-as-judge and human review.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build a golden eval set",
    "Use LLM-as-judge for open-ended outputs",
    "Measure correctness, faithfulness and safety",
    "Run evals in CI"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-12-context-engineering",
    "deep-learning/dl-20-evaluating-deep-models",
    "computer-vision/cv-20-evaluating-vision-models"
  ],
  "prerequisites": [
    "LLM-04: Prompting Systems at Scale"
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

# LLM-13-EVALUATING-LLM-SYSTEMS: Evaluating LLM Systems

## Introduction

Build evals that catch regressions: golden sets, LLM-as-judge and human review. By the end of this lesson you will be able to: Build a golden eval set; Use LLM-as-judge for open-ended outputs; Measure correctness, faithfulness and safety; Run evals in CI.

## Key Concepts

### 1. Build a golden eval set

Target: Build a golden eval set. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
evals = [
    {"prompt": "What is the capital of France?", "expected": "Paris"},
    {"prompt": "2+2?", "expected": "4"},
]
print("golden set:", len(evals))
```
### 2. Use LLM-as-judge for open-ended outputs

Target: Use LLM-as-judge for open-ended outputs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
def exact_match(pred, expected):
    return pred.strip().lower() == expected.strip().lower()

print("EM:", exact_match("Paris", "Paris"))
```
### 3. Measure correctness, faithfulness and safety

Target: Measure correctness, faithfulness and safety. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("LLM-as-judge: score helpfulness, faithfulness, tone")
```
### 4. Run evals in CI

Target: Run evals in CI. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("CI gate: block merges that lower eval scores")
```

## Practice Questions

1. What is the key idea behind "Evaluating LLM Systems"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Evaluating LLM Systems with analogies and real-world examples"
1. "Show me common mistakes beginners make with Evaluating LLM Systems"
1. "Provide advanced patterns and performance considerations for Evaluating LLM Systems"

## Key Takeaways

- Master the core ideas of Evaluating LLM Systems through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
