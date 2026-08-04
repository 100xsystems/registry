---
slug: llm-16-cost-optimization
title: "Cost Optimization for LLM Apps"
description: "Reducing LLM costs without sacrificing quality — caching, routing, prompt compression, and model selection strategies."
order: 16
tags:
  - llm-engineering
  - cost-optimization
  - caching
  - model-routing
prerequisites:
  - llm-03-llm-apis
  - llm-15-llm-serving
knowledge_refs:
  - llm-03-llm-apis
  - llm-15-llm-serving
  - llm-17-observability
references:
  - title: "OpenAI Pricing"
    url: "https://openai.com/pricing"
    notes: "Current pricing for all models"
  - title: "Anthropic Pricing"
    url: "https://www.anthropic.com/pricing"
    notes: "Claude pricing tiers"
  - title: "LLM Cost Calculator"
    url: "https://www.llm-price.com/"
    notes: "Compare costs across providers"
  - title: "Prompt Caching Guide"
    url: "https://platform.openai.com/docs/guides/prompt-caching"
    notes: "OpenAI's prompt caching"
  - title: "Semantic Caching for LLMs"
    url: "https://www.anthropic.com/news/prompt-caching"
    notes: "Anthropic's caching approach"
---

# Cost Optimization for LLM Apps

LLM costs can spiral quickly. A well-optimized system can reduce costs by 90% while maintaining quality.

## Cost Components

| Component | Typical Cost | Optimization Levers |
|-----------|-------------|---------------------|
| Input tokens | $0.50-15/1M tokens | Caching, compression |
| Output tokens | $2-60/1M tokens | Streaming, shorter responses |
| Embeddings | $0.02-0.13/1M tokens | Local models, batching |
| Vector DB | $0.00-0.10/hour | Self-hosted options |

## Caching Strategies

### Exact Match Cache
Cache identical requests:
```python
from functools import lru_cache

@lru_cache(maxsize=10000)
def cached_llm_call(prompt, model, temperature):
    return llm.generate(prompt, model=model, temperature=temperature)
```

### Semantic Cache
Cache similar requests using embeddings:
```python
def semantic_cache(query, threshold=0.95):
    embedding = embed(query)
    similar = vector_db.search(embedding, top_k=1)
    if similar.score > threshold:
        return similar.response  # Cache hit
    response = llm.generate(query)
    vector_db.store(embedding, response)  # Store for future
    return response
```

### Prompt Caching
Both OpenAI and Anthropic cache repeated prefixes:
- System prompts: always cached after first call
- RAG context: cached if reused across requests
- **Savings**: up to 90% on cached tokens

## Model Routing

Use the right model for each task:

```python
def route_to_model(query):
    if is_simple(query):          # "What's 2+2?"
        return "gpt-4o-mini"      # $0.15/1M input
    elif is_complex(query):       # "Analyze this codebase"
        return "gpt-4o"           # $2.50/1M input
    elif is_critical(query):      # Medical/legal
        return "claude-3.5-sonnet"  # $3/1M input
```

### Routing Heuristics
- **Query length**: short → small model
- **Task complexity**: classification → small, reasoning → large
- **Confidence threshold**: if small model is uncertain → escalate
- **User tier**: free → small, paid → large

## Prompt Optimization

### Reduce Token Count
- Remove redundant instructions
- Use shorter examples
- Compress context
- Eliminate unnecessary whitespace

### Output Control
```python
# Instead of unlimited output
response = llm.generate(query, max_tokens=500)

# Use structured output to limit response size
response = llm.generate(query, response_format={"type": "json_object"})
```

## Quantization for Self-Hosting

| Model Size | FP16 VRAM | 4-bit VRAM | Cost/month (GPU) |
|------------|-----------|------------|-------------------|
| 7B | 14GB | 4GB | ~$50 (A10G) |
| 13B | 26GB | 7GB | ~$100 (A10G) |
| 70B | 140GB | 35GB | ~$400 (A100) |

Self-hosting becomes cost-effective at scale (>1M requests/day).

## Cost Monitoring

```python
def track_cost(response):
    input_cost = response.usage.input_tokens * INPUT_PRICE_PER_TOKEN
    output_cost = response.usage.output_tokens * OUTPUT_PRICE_PER_TOKEN
    total = input_cost + output_cost
    
    metrics.record("llm_cost", total, tags={
        "model": response.model,
        "endpoint": current_endpoint
    })
    return total
```

## Key Takeaways

1. Prompt caching reduces costs by up to 90% for repeated prefixes
2. Semantic caching catches similar queries for even more savings
3. Model routing uses small models for simple tasks, large for complex
4. Prompt optimization reduces token count without quality loss
5. Self-hosting becomes cost-effective at high volume
