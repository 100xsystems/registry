---
slug: mlops-19-cost-and-performance
title: "Cost & Performance Optimization"
description: "Making ML systems efficient — GPU optimization, model compression, quantization, inference optimization, and cost monitoring."
order: 19
tags:
  - mlops
  - cost-optimization
  - quantization
  - inference-optimization
  - gpu-optimization
prerequisites:
  - mlops-10-model-serving
knowledge_refs:
  - slug: mlops-10-model-serving
    title: "Model Serving APIs"
  - slug: mlops-08-training-at-scale
    title: "Training at Scale"
  - slug: mlops-18-governance
    title: "Data & Model Governance"
references:
  - title: "Cost-Efficient AI Inference Cloud Strategies — GMI Cloud"
    url: "https://www.gmicloud.ai/en/blog/cost-efficient-ai-inference-cloud-strategies-in-2026"
  - title: "Optimizing Inference Costs: The Complete Guide — Mirantis"
    url: "https://www.mirantis.com/blog/inference-costs/"
  - title: "Optimizing Your LLM in Production — Hugging Face"
    url: "https://huggingface.co/blog/optimize-llm"
  - title: "Introduction to AI Model Optimization — Pruna AI"
    url: "https://huggingface.co/blog/PrunaAI/introduction-to-ai-model-optimization-techniques"
  - title: "KV Cache Quantization — Hugging Face"
    url: "https://huggingface.co/blog/kv-cache-quantization"
---
## Cost & Performance Optimization

Inference accounts for 80–90% of total AI compute spend. Without optimization, costs scale linearly with usage. Smart optimization can cut costs 50–90% while maintaining quality.

### GPU Optimization

**Right-sizing:** Match GPU to workload. Don't use H100s for small models.

**Spot instances:** Preemptible GPUs cut costs 30–70% for fault-tolerant batch workloads.

**Auto-scaling:** Scale based on queue depth, not raw GPU utilization.

**Batching:** Dynamic batching pushes GPU utilization from 30–50% to 80–95%.

### Model Compression

**Quantization:** Reduce precision from FP32/BF16 to INT8/FP8/INT4:
- 70B model: FP16 needs 140GB (multi-GPU), INT4 needs ~35GB (single GPU)
- Minimal quality loss for most tasks

**Pruning:** Remove redundant weights. Structured sparsity (NVIDIA 2:4) maintains hardware acceleration.

**Knowledge distillation:** Train a smaller model to mimic a larger one.

### Inference Optimization

**vLLM:** PagedAttention eliminates KV-cache memory fragmentation, recovering 60–80% wasted memory. Continuous batching maximizes GPU utilization.

**FlashAttention:** Rewrites attention computation to use fast SRAM instead of slow VRAM. Scales linearly with sequence length instead of quadratically.

**Speculative decoding:** Small "draft" model proposes tokens, large model verifies. Faster than large model alone.

### Cost Monitoring

Track cost per:
- Request
- Token
- User
- Workflow

Set budgets and alerts. Combine infrastructure metrics with business KPIs for FinOps visibility.

### Common Mistakes

- **Over-provisioning:** Using the most expensive GPU for every workload.
- **No batching:** Single-request inference wastes GPU capacity.
- **Ignoring quantization:** INT8/INT4 is nearly free performance for most use cases.
- **No cost monitoring:** Without tracking, cost spirals are invisible.

---

*Continue to learn about LLMOps — the emerging discipline of operating large language models.*
