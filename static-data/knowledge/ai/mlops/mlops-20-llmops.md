---
slug: mlops-20-llmops
title: "LLMOps"
description: "The emerging discipline of operating LLMs in production — prompt management, LLM evaluation, RAG monitoring, and cost optimization."
order: 20
tags:
  - mlops
  - llmops
  - llm-operations
  - prompt-management
  - rag-monitoring
prerequisites:
  - mlops-14-monitoring-and-drift
knowledge_refs:
  - slug: mlops-14-monitoring-and-drift
    title: "Monitoring & Drift Detection"
  - slug: mlops-19-cost-and-performance
    title: "Cost & Performance Optimization"
  - slug: pe-10-system-prompts
    title: "System Prompts in Production"
references:
  - title: "LLMOps: From Prototype to Production"
    url: "https://www.comet.com/site/blog/llmops/"
  - title: "LangSmith — LLM Observability"
    url: "https://docs.smith.langchain.com/"
  - title: "Langfuse — Open Source LLM Engineering"
    url: "https://langfuse.com/"
  - title: "Helicone — LLM Observability"
    url: "https://www.helicone.ai/"
  - title: "Prompt Engineering for Production"
    url: "https://www.promptingguide.ai/"
---
## LLMOps

LLMOps is MLOps adapted for large language models. LLMs introduce unique challenges: non-deterministic outputs, prompt management, token-level costs, and complex evaluation. LLMOps addresses these with specialized tools and practices.

### What's Different About LLMs

**Non-deterministic outputs:** The same prompt can produce different results. Evaluation must be statistical, not deterministic.

**Prompt as configuration:** Changing behavior means changing prompts, not retraining models. Prompts need version control, testing, and deployment pipelines.

**Token-based costs:** Every request costs money based on input + output tokens. Cost management is critical.

**External dependencies:** LLMs are often API-based (OpenAI, Anthropic). Vendor changes affect your system.

### Prompt Management

Treat prompts like code:
- **Version control:** Store prompts in Git
- **A/B testing:** Test prompt variations
- **Evaluation:** Measure prompt quality systematically
- **Deployment:** Promote prompts through environments

Tools: LangSmith Prompt Hub, PromptLayer, custom solutions.

### LLM Evaluation

**Automated evaluation:** Use LLM-as-judge to score outputs on quality, safety, and factualness.

**Human evaluation:** Expert review for high-stakes applications.

**Metrics:** Relevance, faithfulness, toxicity, latency, cost per request.

**Benchmarks:** Run standard benchmarks (MT-Bench, HumanEval) to track model performance over time.

### RAG Monitoring

RAG systems need specialized monitoring:
- **Retrieval quality:** Are relevant documents being retrieved?
- **Grounding:** Is the model using retrieved context faithfully?
- **Latency:** End-to-end latency including retrieval
- **Context utilization:** What percentage of retrieved context is actually used?

### Cost Optimization

- **Caching:** Cache frequent queries
- **Prompt compression:** Reduce token count
- **Model routing:** Use cheap models for simple tasks, expensive models for complex ones
- **Batching:** Process multiple requests together

### Common Mistakes

- **No prompt versioning:** Changing prompts without tracking breaks reproducibility.
- **Ignoring cost:** LLM costs can spiral without monitoring.
- **No evaluation:** Non-deterministic outputs require systematic evaluation.
- **Treating LLMs like traditional ML:** Different challenges need different solutions.

---

*Continue to the final lesson — the MLOps roadmap and career guide.*
