---
slug: genai-18-llmops
title: "LLMOps: Running GenAI in Production"
description: "Deployment, monitoring, cost optimization, and reliability for large language model applications."
order: 18
tags:
  - generative-ai
  - llmops
  - deployment
  - monitoring
  - production
prerequisites:
  - genai-06-llm-architecture
  - genai-10-rag
  - genai-17-evaluating-llms
references:
  - title: "LLMOps: Operationalizing LLM Applications"
    url: "https://cloud.google.com/architecture/llmops-operationalizing-llm-applications"
    description: "Google Cloud's comprehensive LLMOps guide"
  - title: "Building LLM Applications for Production (Chip Huyen)"
    url: "https://huyenchip.com/2023/04/11/llm-engineering.html"
    description: "Chip Huyen's guide to LLM engineering in production"
  - title: "vLLM: Efficient LLM Serving"
    url: "https://github.com/vllm-project/vllm"
    description: "vLLM documentation for high-throughput LLM inference"
  - title: "LangSmith: LLM Observability"
    url: "https://docs.smith.langchain.com/"
    description: "LangChain's observability platform for LLM applications"
  - title: "Productionizing LLMs (Full Stack Deep Learning)"
    url: "https://fullstackdeeplearning.com/llm-bootcamp/"
    description: "Full Stack Deep Learning's LLM production bootcamp"
knowledge_refs:
  - genai-10-rag
  - genai-06-llm-architecture
  - genai-17-evaluating-llms
---

# LLMOps: Running GenAI in Production

Deploying LLM applications to production requires specialized operations practices — from serving infrastructure to monitoring to cost management.

## The LLMOps Stack

```
Application Layer:    RAG, Agents, Fine-tuning
Orchestration:        LangChain, LlamaIndex, Semantic Kernel
Serving:              vLLM, TGI, Triton, Ollama
Inference Providers:  OpenAI, Anthropic, Together, Replicate
Monitoring:           LangSmith, Weights & Biases, Arize
Infrastructure:       Kubernetes, GPU clusters, Serverless
```

## LLM Serving Options

### API Providers
| Provider | Models | Cost | Latency |
|---|---|---|---|
| OpenAI | GPT-4, GPT-4o | $$$$ | Low |
| Anthropic | Claude 3.5 | $$$ | Low |
| Together AI | Open-source models | $$ | Medium |
| Groq | Llama, Mixtral | $ | Very low |
| Replicate | Many models | $$ | Medium |

### Self-Hosted Serving
| Tool | Throughput | Latency | Features |
|---|---|---|---|
| **vLLM** | Very high | Low | PagedAttention, continuous batching |
| **TGI** | High | Low | Hugging Face serving |
| **Ollama** | Medium | Medium | Easy local deployment |
| **Triton** | Very high | Low | NVIDIA's inference server |

```python
# vLLM serving
from vllm import LLM, SamplingParams

llm = LLM(model="meta-llama/Llama-3-8B-Instruct")
params = SamplingParams(temperature=0.7, max_tokens=512)
outputs = llm.generate(["Hello, how are you?"], params)
```

## Cost Optimization

### Token Management
```python
# Monitor token usage
def count_tokens(text, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Estimate costs
cost_per_1k_tokens = {
    "gpt-4o": 0.0025,
    "gpt-4-turbo": 0.01,
    "claude-3.5-sonnet": 0.003,
}
```

### Caching Strategies
```python
# Semantic cache: cache similar queries
from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))

# Semantic cache: cache by embedding similarity
from langchain.cache import GPTCache
set_llm_cache(GPTCache(init_cache_func=init_gptcache))
```

### Model Selection
| Task | Recommended Model | Cost |
|---|---|---|
| Simple QA | GPT-4o-mini | $ |
| Complex reasoning | GPT-4o | $$$ |
| Code generation | Claude 3.5 Sonnet | $$ |
| Summarization | Llama 3 8B | $ |
| Translation | GPT-4o-mini | $ |

## Prompt Management

### Version Control
```python
# Track prompt versions
PROMPTS = {
    "v1.0": "You are a helpful assistant. Answer the question: {question}",
    "v1.1": "Answer the following question concisely: {question}",
    "v1.2": "You are an expert. Provide a detailed answer to: {question}"
}
```

### A/B Testing
```python
import random

def select_prompt(variant_a, variant_b, traffic_split=0.5):
    if random.random() < traffic_split:
        return variant_a
    return variant_b
```

## Monitoring & Observability

### Key Metrics to Track
| Metric | What It Measures |
|---|---|
| **Latency** | Time to first token, total response time |
| **Throughput** | Requests per second, tokens per second |
| **Cost** | Tokens used, API calls, total spend |
| **Quality** | User ratings, task success rate |
| **Errors** | API failures, rate limits, timeouts |
| **Hallucination rate** | Factual accuracy of responses |

### Tracing
```python
# LangSmith tracing
from langsmith import traceable

@traceable(name="qa_chain")
def qa_chain(question: str):
    docs = retriever.invoke(question)
    answer = llm.invoke(f"Context: {docs}\nQuestion: {question}")
    return answer
```

### Evaluation Pipeline
```python
from ragas import evaluate

def evaluate_rag(test_cases):
    results = evaluate(
        dataset=test_cases,
        metrics=[faithfulness, answer_relevancy, context_precision],
    )
    # Log to monitoring dashboard
    log_metrics(results)
    return results
```

## Production Architecture

```
User Request
    ↓
┌─────────────┐
│   API Gateway  │  Rate limiting, auth, routing
└─────────────┘
    ↓
┌─────────────┐
│  Prompt Mgmt   │  Version control, templates
└─────────────┘
    ↓
┌─────────────┐
│  RAG Pipeline   │  Retrieval, reranking
└─────────────┘
    ↓
┌─────────────┐
│  LLM Serving    │  vLLM / API provider
└─────────────┘
    ↓
┌─────────────┐
│  Post-Processing│  Format, validate, filter
└─────────────┘
    ↓
┌─────────────┐
│  Monitoring     │  Trace, log, alert
└─────────────┘
    ↓
Response
```

## Reliability Patterns

### Retry with Exponential Backoff
```python
import time
import openai

def call_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            return openai.chat.completions.create(
                model="gpt-4", messages=[{"role": "user", "content": prompt}]
            )
        except openai.RateLimitError:
            time.sleep(2 ** attempt)
    raise Exception("Max retries exceeded")
```

### Fallback Models
```python
def call_with_fallback(prompt, models=["gpt-4o", "gpt-4o-mini", "claude-3.5"]):
    for model in models:
        try:
            return call_model(model, prompt)
        except Exception:
            continue
    raise Exception("All models failed")
```

### Output Validation
```python
def validate_output(response, expected_format):
    try:
        parsed = json.loads(response)
        assert all(key in parsed for key in expected_format.keys())
        return parsed
    except (json.JSONDecodeError, AssertionError):
        # Retry with stricter prompt
        return call_with_validation(response, expected_format)
```

## Cost Management

1. **Set budgets**: Monthly token limits per team
2. **Cache aggressively**: Similar queries → same response
3. **Use smaller models**: GPT-4o-mini for simple tasks
4. **Batch requests**: Process in bulk when possible
5. **Monitor daily**: Track costs in real-time

## Further Reading

- Google Cloud's LLMOps guide is comprehensive
- Chip Huyen's article covers practical production challenges
- vLLM is the standard for self-hosted LLM serving
- LangSmith provides full observability for LangChain apps
