---
slug: llm-03-llm-apis
title: "Working with LLM APIs"
description: "Practical guide to OpenAI, Anthropic, and Google APIs — authentication, streaming, rate limiting, and error handling patterns."
order: 3
tags:
  - llm-engineering
  - api
  - openai
  - anthropic
  - google
prerequisites:
  - llm-02-llm-architecture-review
knowledge_refs:
  - llm-02-llm-architecture-review
  - llm-05-tokenization-and-context
references:
  - title: "OpenAI API Documentation"
    url: "https://platform.openai.com/docs/api-reference"
    notes: "Official OpenAI API reference"
  - title: "Claude API Overview"
    url: "https://platform.claude.com/docs/en/api/overview"
    notes: "Anthropic's API documentation"
  - title: "Gemini API Text Generation"
    url: "https://ai.google.dev/gemini-api/docs/text-generation"
    notes: "Google's Gemini API guide"
  - title: "Anthropic Rate Limits"
    url: "https://docs.anthropic.com/en/api/rate-limits"
    notes: "Detailed rate limiting documentation"
  - title: "LiteLLM: Universal LLM API"
    url: "https://docs.litellm.ai/"
    notes: "Unified interface for 100+ LLM providers"
---

# Working with LLM APIs

LLM APIs are the primary interface for building LLM applications. This lesson covers the practical details of working with the major providers.

## The Three Major APIs

### OpenAI
```python
from openai import OpenAI
client = OpenAI(api_key="sk-...")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=0.7,
    max_tokens=1000
)
print(response.choices[0].message.content)
```

### Anthropic (Claude)
```python
from anthropic import Anthropic
client = Anthropic(api_key="sk-ant-...")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    system="You are a helpful assistant.",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.content[0].text)
```

### Google (Gemini)
```python
from google import genai
client = genai.Client(api_key="...")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello!"
)
print(response.text)
```

## Streaming Responses

Streaming reduces time-to-first-token and improves user experience:

```python
# OpenAI streaming
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

## Rate Limiting

All providers enforce rate limits across multiple dimensions:
- **RPM**: Requests Per Minute
- **TPM/ITPM/OTPM**: Tokens Per Minute (total/input/output)
- **RPD**: Requests Per Day
- **Spend caps**: Maximum cost per time window

### Best Practices
1. **Exponential backoff**: wait 1s, 2s, 4s, 8s on 429 errors
2. **Request queuing**: buffer requests and process at controlled rate
3. **Cache responses**: avoid redundant API calls
4. **Monitor headers**: `retry-after`, `x-ratelimit-remaining`

## Error Handling

| Error | Meaning | Action |
|-------|---------|--------|
| 400 | Bad request | Fix input format |
| 401 | Auth error | Check API key |
| 429 | Rate limit | Backoff and retry |
| 500 | Server error | Retry with backoff |
| 503 | Overloaded | Retry later |

### Streaming Errors
Errors can arrive mid-stream after an initial 200 OK. Always handle `error` events in SSE streams.

## Prompt Caching

Both OpenAI and Anthropic support prompt caching:
- Cache system prompts and repeated context
- Cached tokens are cheaper (up to 90% discount)
- Anthropic: cached tokens exempt from rate limits

## Key Takeaways

1. OpenAI, Anthropic, and Google have similar but distinct API patterns
2. Streaming reduces perceived latency — always use it for user-facing apps
3. Handle rate limits with exponential backoff and request queuing
4. Prompt caching reduces cost for repeated system prompts
5. Consider using LiteLLM or similar for provider-agnostic code
