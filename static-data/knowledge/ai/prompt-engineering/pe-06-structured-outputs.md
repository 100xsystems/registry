---
slug: pe-06-structured-outputs
title: "Structured Outputs"
description: "Getting JSON, tables, and formatted responses from any model — schema enforcement, function calling, and constrained decoding."
order: 6
tags:
  - prompt-engineering
  - structured-outputs
  - json
  - function-calling
prerequisites:
  - pe-05-chain-of-thought
knowledge_refs:
  - slug: pe-05-chain-of-thought
    title: "Chain-of-Thought Reasoning"
  - slug: pe-10-system-prompts
    title: "System Prompts in Production"
  - slug: llm-10-function-calling
    title: "Function Calling & Structured Outputs"
references:
  - title: "Instructor — Multi-Language Library for Structured LLM Outputs"
    url: "https://python.useinstructor.com/"
  - title: "The Guide to Structured Outputs and Function Calling with LLMs"
    url: "https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms"
  - title: "Best Structured Prompt Formats for LLMs, Ranked"
    url: "https://mightybot.ai/blog/best-structured-prompt-formats-for-llms/"
  - title: "Claude API Structured Output: Complete Guide"
    url: "https://thomas-wiegold.com/blog/claude-api-structured-output/"
  - title: "Structured Outputs with OpenAI — Instructor Guide"
    url: "https://python.useinstructor.com/integrations/openai/"
---
## Structured Outputs

Getting a model to produce valid JSON, tables, or formatted data is one of the most common and critical tasks in prompt engineering. Without structured outputs, you're parsing free-form text and hoping it matches your schema. With structured outputs, you get guaranteed, type-safe data every time.

### JSON Mode vs. Schema Enforcement

**JSON Mode** tells the model "return valid JSON." This guarantees syntactic correctness — the model won't output malformed JSON. But it doesn't guarantee the structure matches what you need. You might get valid JSON with the wrong keys, wrong types, or missing fields.

**Schema Enforcement** (structured outputs) goes further. It compiles your schema into a grammar that constrains the model's token generation at inference time. The model physically cannot produce output that violates the schema. OpenAI calls this `response_format: { type: "json_schema" }`. Anthropic offers `output_format` with `json_schema`. The result is mathematically guaranteed compliance.

```python
from pydantic import BaseModel
from instructor import patch
from openai import OpenAI

class SentimentResult(BaseModel):
    sentiment: str  # "positive", "negative", "neutral"
    confidence: float  # 0.0 to 1.0
    reasoning: str

client = OpenAI()
patch(client)

result = client.chat.completions.create(
    model="gpt-4",
    response_model=SentimentResult,
    messages=[{"role": "user", "content": "This product is amazing but shipping was slow."}]
)

# result is guaranteed to be a SentimentResult instance
print(result.sentiment)    # "positive"
print(result.confidence)   # 0.75
```

The `instructor` library wraps provider APIs to automatically handle validation failures, triggering retries until the output conforms to your Pydantic model.

### Function Calling & Tool Use

Function calling transforms models from passive text generators into active decision-makers. The LLM evaluates user intent, selects an appropriate tool, and formats arguments into validated JSON payloads.

This is structured outputs applied to API design: instead of returning data, the model returns function calls with typed arguments. Modern frameworks generate function schemas automatically from Python type hints or Pydantic models.

### Format Selection Guide

| Format | Best For | Parsing | Token Efficiency |
|---|---|---|---|
| **JSON** | APIs, databases, structured data | Trivial | Good |
| **XML** | Complex nested data, prompt structuring | Easy | Moderate |
| **Markdown tables** | Human-readable comparisons | Moderate | Good |
| **YAML** | Configuration, readable configs | Easy | Good |
| **CSV/TSV** | Tabular data, bulk exports | Trivial | Excellent |

### Practical Patterns

**For APIs and databases:** Use JSON schema enforcement. Define a Pydantic model (Python) or Zod schema (TypeScript) and enforce it at the API level.

**For prompt structuring:** Use XML tags. They're cleaner for separating sections and Claude handles them natively.

**For human-readable output:** Use Markdown. Tables, lists, and headers are naturally readable and parseable.

**For maximum token efficiency:** Use CSV/TSV for flat tabular data. Minified JSON for nested data.

### Common Mistakes

- **Relying on prompt instructions for format:** "Please respond in JSON" is a request, not a guarantee. Use schema enforcement for production.
- **Over-engineering schemas:** Start simple. A flat JSON object is better than a deeply nested schema if you don't need the nesting.
- **Ignoring error handling:** Even with schema enforcement, handle validation failures gracefully with retry logic.

---

*Continue to learn about prompting for code generation, review, and debugging.*
