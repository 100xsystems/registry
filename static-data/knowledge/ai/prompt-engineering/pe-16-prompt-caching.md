---
slug: pe-16-prompt-caching
title: "Prompt Caching & Cost"
description: "Making prompts efficient at scale — caching strategies, token pricing, context optimization, and cost management."
order: 16
tags:
  - prompt-engineering
  - caching
  - cost-optimization
  - token-pricing
prerequisites:
  - pe-10-system-prompts
knowledge_refs:
  - slug: pe-10-system-prompts
    title: "System Prompts in Production"
  - slug: pe-19-optimizing-for-cost
    title: "Optimizing Prompts for Cost"
  - slug: llm-16-cost-optimization
    title: "Cost Optimization"
references:
  - title: "Anthropic — Prompt Caching"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-caching"
  - title: "OpenAI — Prompt Caching"
    url: "https://platform.openai.com/docs/guides/prompt-caching"
  - title: "LangChain — Prompt Caching Guide"
    url: "https://python.langchain.com/docs/how_to/llm_caching/"
  - title: "LLM Token Pricing Comparison 2024"
    url: "https://artificialanalysis.ai/text/arena?tab=pricing"
  - title: "Anthropic — Context Engineering for AI Agents"
    url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
---
## Prompt Caching & Cost

At scale, prompt costs add up fast. A system prompt sent with every request, repeated context across conversations, and verbose instructions all consume tokens — and tokens cost money. Prompt caching and cost optimization are essential for production systems.

### How Prompt Caching Works

Prompt caching stores the processed (cached) representation of a prompt prefix so that repeated requests with the same prefix skip the expensive prefill computation.

**Anthropic's approach:** Caches the system prompt and long context blocks. If a subsequent request starts with the same prefix (at least 1024 tokens for Claude), the cached portion is reused at a fraction of the cost.

**OpenAI's approach:** Automatically caches identical prompt prefixes. No configuration needed — if two requests share the same starting tokens, the second one gets a 50% discount on cached tokens.

### When Caching Helps

- **Long system prompts** sent with every request (1000+ tokens)
- **RAG contexts** where the same documents appear across multiple queries
- **Multi-turn conversations** where history is resent each turn
- **Batch processing** with shared context (same instructions, different data)

### Token Pricing Awareness

Understanding pricing helps you make informed design decisions:

- Input tokens are cheaper than output tokens (typically 3–10×)
- Longer prompts cost more per request
- Cached tokens are significantly cheaper (50–90% discount)
- Different models have wildly different pricing

### Cost Optimization Strategies

1. **Compress instructions:** Remove redundant phrases,合并 similar rules, use concise language
2. **Cache aggressively:** Structure prompts so the expensive prefix (system prompt + context) is cacheable
3. **Use smaller models for simple tasks:** Don't use GPT-4 for classification that GPT-3.5 handles well
4. **Batch similar requests:** Process multiple items in one prompt when possible
5. **Monitor token consumption:** Track average tokens per request and optimize outliers

### Common Mistakes

- **Ignoring caching:** A 2000-token system prompt sent 10,000 times/day wastes money if not cached
- **Over-compressing:** Cutting too much from prompts degrades quality more than it saves
- **Not tracking costs:** Without monitoring, cost spikes go unnoticed until the bill arrives

---

*Continue to learn about domain-specific prompting — tailoring prompts for medical, legal, financial, and educational applications.*
