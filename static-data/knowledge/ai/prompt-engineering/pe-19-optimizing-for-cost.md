---
slug: pe-19-optimizing-for-cost
title: "Optimizing Prompts for Cost"
description: "Token efficiency, prompt compression, caching strategies, model selection, and batching — reducing cost without sacrificing quality."
order: 19
tags:
  - prompt-engineering
  - cost-optimization
  - token-efficiency
  - model-selection
  - batching
prerequisites:
  - pe-16-prompt-caching
knowledge_refs:
  - pe-16-prompt-caching
    title: "Prompt Caching & Cost"
  - pe-20-production-prompting
    title: "Prompt Engineering in Production"
  - llm-16-cost-optimization
    title: "Cost Optimization"
references:
  - title: "OpenAI — Pricing"
    url: "https://openai.com/pricing"
  - title: "Anthropic — Pricing"
    url: "https://www.anthropic.com/pricing"
  - title: "Artificial Analysis — LLM Pricing Comparison"
    url: "https://artificialanalysis.ai/text/arena?tab=pricing"
  - title: "LangChain — Caching Guide"
    url: "https://python.langchain.com/docs/how_to/llm_caching/"
  - title: "Anthropic — Prompt Caching"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-caching"
---

## Optimizing Prompts for Cost

Every token costs money. At scale — thousands or millions of requests per day — even small prompt optimizations compound into significant savings. Cost optimization isn't about cutting corners; it's about being efficient.

### Understanding Token Costs

LLM pricing is based on tokens (roughly 4 characters per token):
- **Input tokens:** What you send to the model (system prompt + user message)
- **Output tokens:** What the model generates (usually 3–10× more expensive than input)
- **Cached tokens:** Previously processed tokens at 50–90% discount

### Prompt Compression

**Remove redundancy:** Eliminate repeated instructions,合并 similar rules, cut filler words.

**Before (150 tokens):**
"You are a helpful and friendly customer support agent. Your job is to help users with their questions. You should always be polite and professional. When answering questions, make sure to be thorough and complete. If you don't know the answer, say so honestly."

**After (60 tokens):**
"You are a polite, professional customer support agent. Answer thoroughly. If unsure, say so."

**Use concise structures:** Lists instead of paragraphs. JSON instead of verbose descriptions.

### Model Selection

Not every task needs the most expensive model:

| Task | Recommended Model | Why |
|---|---|---|
| Simple classification | GPT-3.5, Haiku | Fast, cheap, accurate enough |
| Complex reasoning | GPT-4, Claude Opus | Needs deep understanding |
| Code generation | GPT-4, Claude Sonnet | Balance of quality and cost |
| Summarization | GPT-3.5, Haiku | Works well for straightforward tasks |

### Batching

Process multiple items in a single prompt when possible:
- Classify 10 items in one prompt instead of 10 separate calls
- Summarize multiple documents in a single request
- Generate multiple variations in one batch

### Caching Strategies

- Structure prompts so the prefix (system prompt + context) is cacheable
- Reuse identical context across requests
- Use semantic caching for similar (not identical) queries

### Measurement

Track these metrics:
- **Average tokens per request** (input + output)
- **Cost per request** (in dollars)
- **Cache hit rate** (percentage of requests using cached tokens)
- **Cost per task** (total cost divided by successful completions)

### Common Mistakes

- **Over-optimization:** Cutting too much from prompts degrades quality more than it saves
- **Ignoring output tokens:** Long responses cost more than long prompts
- **Not measuring:** You can't optimize what you don't track
- **Using one model for everything:** Match model capability to task complexity

---

*Continue to learn about prompt engineering in production — deployment patterns, monitoring, and scaling.*
