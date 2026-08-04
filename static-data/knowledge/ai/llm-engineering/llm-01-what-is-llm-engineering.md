---
slug: llm-01-what-is-llm-engineering
title: "What Is LLM Engineering?"
description: "Defining the new discipline of building applications on top of large language models — how it differs from ML engineering and traditional software."
order: 1
tags:
  - llm-engineering
  - ai-engineering
  - foundations
prerequisites: []
knowledge_refs:
  - llm-02-llm-architecture-review
  - llm-03-llm-apis
references:
  - title: "The Rise of the AI Engineer"
    url: "https://www.latent.space/p/2023-aisp"
    notes: "swyx's seminal essay defining the AI Engineer role"
  - title: "Open Questions for AI Engineering"
    url: "https://simonwillison.net/2024/Oct/26/open-questions-for-ai-engineering/"
    notes: "Simon Willison on the emerging field"
  - title: "LLM Powered Autonomous Agents"
    url: "https://lilianweng.github.io/posts/2023-06-23-agent/"
    notes: "Lilian Weng's comprehensive agent framework"
  - title: "Andrej Karpathy: 2025 LLM Year in Review"
    url: "https://www.youtube.com/watch?v=bL02bC-E2bE"
    notes: "Karpathy's perspective on LLM app development"
  - title: "AI Engineer Summit Keynotes"
    url: "https://www.youtube.com/@aiaboratory"
    notes: "Industry talks on the AI Engineering discipline"
---

# What Is LLM Engineering?

LLM Engineering — also called **AI Engineering** — is the discipline of building applications on top of large language models. It represents a fundamental shift in how we build software: instead of writing explicit logic, we orchestrate probabilistic models that understand and generate natural language.

## LLM Engineering vs. ML Engineering

| Dimension | ML Engineering | LLM Engineering |
|-----------|---------------|-----------------|
| **Focus** | Training models from scratch | Building apps on top of models |
| **Data** | Labeled datasets, feature engineering | Prompts, context, retrieval |
| **Code** | PyTorch, training pipelines | API calls, orchestration, evaluation |
| **Infrastructure** | GPU clusters, training jobs | API rate limits, caching, serving |
| **Key skill** | Math, statistics, optimization | Prompting, RAG, systems design |

As Andrej Karpathy notes, an engineer can be highly successful in LLM engineering without ever training a model. The core competency shifts from model creation to **model orchestration**.

## The Three Layers of Modern AI

1. **Model Layer** — Training foundation models (OpenAI, Anthropic, Google, Meta)
2. **Infrastructure Layer** — Serving, inference, fine-tuning platforms
3. **Application Layer** — Products built on top (LLM Engineering lives here)

## What LLM Engineers Actually Do

- **Prompt Engineering** — Design system prompts, few-shot examples, chain-of-thought chains
- **RAG Architecture** — Build retrieval systems that ground LLMs in real data
- **Agent Systems** — Orchestrate LLM calls with tools, memory, and planning
- **Evaluation** — Build testing frameworks for non-deterministic outputs
- **Production Systems** — Handle rate limits, caching, error handling, cost optimization
- **Safety & Guardrails** — Prevent prompt injection, hallucination, harmful outputs

## Key Paradigm Shifts

### English as Programming Language
Natural language prompts become the new code. A well-crafted system prompt can replace hundreds of lines of conditional logic.

### Probabilistic Outputs
Unlike traditional software, LLM outputs are non-deterministic. The same prompt can yield different results. Evaluation must account for this variance.

### Ephemeral Code
Code becomes cheaper and more disposable. Entire applications can be prototyped in hours and discarded after use.

### New Failure Modes
- **Hallucinations**: plausible but incorrect outputs
- **Context overflow**: exceeding token limits
- **Prompt injection**: adversarial inputs bypassing safety
- **Alignment failures**: model ignoring instructions

## Essential Skills

1. **Prompt Design** — zero-shot, few-shot, chain-of-thought, structured outputs
2. **Systems Thinking** — DAG orchestration, caching, retry logic
3. **RAG Pipelines** — chunking, embedding, retrieval, reranking
4. **Evaluation** — LLM-as-judge, human evaluation, benchmark design
5. **Production Engineering** — streaming, rate limiting, cost monitoring

## Key Takeaways

1. LLM Engineering is building applications on foundation models, not training them
2. Natural language replaces explicit logic as the primary programming paradigm
3. The core skills are prompting, RAG, evaluation, and systems design
4. New failure modes (hallucination, injection) require new engineering practices
5. The field is evolving rapidly — staying current requires active community engagement
