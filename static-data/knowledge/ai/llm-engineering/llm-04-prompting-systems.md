---
slug: llm-04-prompting-systems
title: "Prompting Systems at Scale"
description: "Managing prompts as production systems — versioning, A/B testing, structured outputs, and prompt architecture patterns."
order: 4
tags:
  - llm-engineering
  - prompting
  - structured-outputs
  - versioning
prerequisites:
  - llm-03-llm-apis
knowledge_refs:
  - llm-03-llm-apis
  - llm-05-tokenization-and-context
references:
  - title: "OpenAI Structured Outputs"
    url: "https://platform.openai.com/docs/guides/structured-outputs"
    notes: "Schema enforcement via constrained decoding"
  - title: "Prompt Versioning Guide"
    url: "https://agenta.ai/blog/prompt-versioning-guide"
    notes: "Managing prompts in production teams"
  - title: "A/B Testing with Prompts"
    url: "https://www.getmaxim.ai/articles/how-to-perform-a-b-testing-with-prompts/"
    notes: "Experiment design for prompt optimization"
  - title: "Chain-of-Thought Prompting"
    url: "https://www.promptingguide.ai/techniques/cot"
    notes: "Reasoning frameworks for complex tasks"
  - title: "Few-Shot Prompting"
    url: "https://www.promptingguide.ai/techniques/fewshot"
    notes: "In-context learning mechanics"
---

# Prompting Systems at Scale

In production, prompts are not one-off scripts — they are **versioned, tested, and monitored systems**. This lesson covers the engineering practices for managing prompts at scale.

## System Prompt Architecture

A well-structured system prompt has clear sections:

```
[IDENTITY]      → Who the model is
[CONSTRAINTS]   → What it can/cannot do
[FORMAT]        → Output structure expectations
[EXAMPLES]      → Few-shot demonstrations
[DYNAMIC]       → Retrieved context (RAG)
[USER INPUT]    → The actual query
```

### Context Budgeting
Balance static and dynamic content within the context window:
- System prompt: ~500-2000 tokens
- Few-shot examples: ~1000-3000 tokens
- RAG context: ~2000-8000 tokens
- Conversation history: remaining budget
- Reserve for output: 1000-4000 tokens

## Few-Shot Prompting

Provide input-output examples to steer model behavior:

```python
prompt = """
Classify the sentiment of each review.

Review: "This product is amazing!" → Positive
Review: "Terrible quality, broke after one day." → Negative
Review: "It's okay, nothing special." → Neutral

Review: "I love this so much!" →
"""
```

### Best Practices
- Include diverse examples covering edge cases
- Match the exact output format expected
- Order matters — put most relevant examples last (recency bias)
- 3-5 examples is usually sufficient

## Chain-of-Thought (CoT)

Force step-by-step reasoning before the final answer:

```python
prompt = """
Q: Roger has 5 tennis balls. He buys 2 cans of 3 each. How many does he have now?
A: Roger starts with 5 balls. 2 cans × 3 balls = 6 balls. 5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. They used 20 for lunch and bought 6 more. How many do they have?
A:
"""
```

### Variants
- **Few-shot CoT**: exemplars include reasoning traces
- **Zero-shot CoT**: append "Let's think step by step"
- **Self-consistency**: sample multiple CoT paths, majority vote

## Structured Outputs

Guarantee valid JSON/structured output via constrained decoding:

```python
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object", "schema": {
        "type": "object",
        "properties": {
            "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]},
            "confidence": {"type": "number", "minimum": 0, "maximum": 1}
        },
        "required": ["sentiment", "confidence"]
    }},
    messages=[{"role": "user", "content": "This movie was fantastic!"}]
)
```

## Prompt Versioning

### Why Git Fails for Prompts
- Non-technical stakeholders can't use Git
- Prompt changes mix with code changes
- No playground for side-by-side comparison

### Dedicated Prompt Management
- **Branching**: isolate experimental prompts
- **Environments**: dev → staging → production
- **Reusable snippets**: modular safety guardrails
- **Live fetching**: runtime prompt updates without deployment

## A/B Testing Prompts

```
Variant A (control): "You are a helpful assistant."
Variant B (treatment): "You are a concise, technical assistant."

→ Route 50% traffic to each
→ Measure: accuracy, latency, cost, user satisfaction
→ Statistical significance: ~100-200 samples per variant
```

## Key Takeaways

1. Structure system prompts with clear sections (identity, constraints, format, examples)
2. Few-shot examples should be diverse and match expected output format
3. Chain-of-thought reasoning improves complex task performance
4. Structured outputs via constrained decoding eliminate parsing failures
5. Version and A/B test prompts like any other production code
