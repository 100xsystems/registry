---
slug: llm-17-observability
title: "Prompt Versioning & Observability"
description: "Monitoring LLM applications in production — tracing, logging, prompt versioning, and debugging non-deterministic systems."
order: 17
tags:
  - llm-engineering
  - observability
  - tracing
  - prompt-versioning
  - monitoring
prerequisites:
  - llm-13-evaluating-llm-systems
  - llm-16-cost-optimization
knowledge_refs:
  - llm-13-evaluating-llm-systems
  - llm-16-cost-optimization
  - llm-14-guardrails-and-safety
references:
  - title: "LangSmith Documentation"
    url: "https://docs.smith.langchain.com/"
    notes: "LLM observability platform"
  - title: "OpenTelemetry for LLMs"
    url: "https://opentelemetry.io/docs/languages/python/"
    notes: "Standard tracing for LLM apps"
  - title: "Prompt Versioning Guide"
    url: "https://agenta.ai/blog/prompt-versioning-guide"
    notes: "Managing prompt versions in production"
  - title: "Helicone LLM Observability"
    url: "https://www.helicone.ai/"
    notes: "Open-source LLM proxy with observability"
  - title: "Braintrust LLM Evaluation"
    url: "https://www.braintrust.dev/"
    notes: "Eval and observability platform"
---

# Prompt Versioning & Observability

LLM applications are non-deterministic — the same input can produce different outputs. Observability is essential for debugging, monitoring, and improving production systems.

## Why Observability Matters

Unlike traditional software:
- **Same input ≠ same output** (temperature, model updates)
- **Quality is subjective** (accuracy, helpfulness, tone)
- **Failures are silent** (hallucination looks plausible)
- **Costs are variable** (different responses use different tokens)

## Core Observability Signals

### Tracing
Record every step of the LLM pipeline:
```python
with tracer.start_as_current_span("llm_call") as span:
    span.set_attribute("model", "gpt-4o")
    span.set_attribute("prompt_tokens", len(prompt_tokens))
    
    response = llm.generate(prompt)
    
    span.set_attribute("completion_tokens", len(response.tokens))
    span.set_attribute("latency_ms", response.latency)
    span.set_attribute("cost_usd", response.cost)
```

### Logging
Capture structured data for every request:
```python
log_entry = {
    "timestamp": "2024-01-15T10:30:00Z",
    "request_id": "req_abc123",
    "model": "gpt-4o",
    "prompt_hash": hash(prompt),
    "response_preview": response[:100],
    "tokens": {"input": 500, "output": 200},
    "latency_ms": 1200,
    "cost_usd": 0.0035,
    "user_id": "user_xyz",
    "tags": ["customer-support", "tier-1"]
}
```

### Metrics
Track key performance indicators:
- **Latency**: p50, p95, p99 response times
- **Cost**: per-request and aggregate spend
- **Quality**: eval scores, user ratings
- **Errors**: rate limiting, timeouts, failures

## Prompt Versioning

### Why Version Prompts?
- Prompt changes affect output quality
- Need to roll back bad changes
- A/B test different versions
- Reproduce past results

### Version Management
```python
# Store prompt versions in a registry
prompts = {
    "v1.0": {"system": "You are helpful.", "template": "..."},
    "v1.1": {"system": "You are concise and helpful.", "template": "..."},
    "v1.2": {"system": "You are a technical expert.", "template": "..."},
}

# Tag production version
ACTIVE_VERSION = "v1.1"
```

### Git vs. Dedicated Tools
| Approach | Pros | Cons |
|----------|------|------|
| Git | Version control, diffs | Not accessible to non-engineers |
| Dedicated tools | Playground, A/B testing | Extra infrastructure |
| Hybrid | Best of both | More complexity |

## Debugging Non-Deterministic Systems

### Reproducibility Techniques
```python
# Fix temperature for debugging
response = llm.generate(prompt, temperature=0.0)

# Log the seed for exact reproduction
response = llm.generate(prompt, seed=42)
```

### Common Failure Patterns
1. **Hallucination**: model invents facts
   - Fix: add RAG, constrain outputs
2. **Prompt injection**: user overrides instructions
   - Fix: input validation, guardrails
3. **Context overflow**: information lost
   - Fix: better context management
4. **Degradation**: model update breaks behavior
   - Fix: eval pipeline catches regressions

## Production Dashboard

Key metrics to monitor:
- **Request volume**: requests/minute
- **Latency**: p50 < 2s, p99 < 10s
- **Cost**: daily spend, cost per request
- **Error rate**: < 1% of requests
- **Quality score**: eval score trend
- **User satisfaction**: ratings, feedback

## Key Takeaways

1. LLM observability is essential because outputs are non-deterministic
2. Trace every step: prompt, model, tokens, latency, cost, quality
3. Version prompts like code — tag, diff, and roll back
4. Fix temperature for debugging; log seeds for reproducibility
5. Monitor quality metrics alongside latency and cost
