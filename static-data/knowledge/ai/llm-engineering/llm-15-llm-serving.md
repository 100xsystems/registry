---
slug: llm-15-llm-serving
title: "LLM Serving & Inference"
description: "Serving LLMs at scale — vLLM, TGI, TensorRT-LLM, quantization, batching strategies, and GPU optimization."
order: 15
tags:
  - llm-engineering
  - serving
  - inference
  - vllm
  - quantization
prerequisites:
  - llm-02-llm-architecture-review
  - llm-03-llm-apis
knowledge_refs:
  - llm-02-llm-architecture-review
  - llm-03-llm-apis
  - llm-16-cost-optimization
references:
  - title: "vLLM Documentation"
    url: "https://docs.vllm.ai/en/latest/"
    notes: "PagedAttention-based serving"
  - title: "Hugging Face TGI"
    url: "https://huggingface.co/docs/text-generation-inference"
    notes: "Production text generation"
  - title: "TensorRT-LLM"
    url: "https://nvidia.github.io/TensorRT-LLM/"
    notes: "NVIDIA's optimized inference"
  - title: "LLM Quantization Guide (CAST AI)"
    url: "https://cast.ai/blog/demystifying-quantizations-llms/"
    notes: "GPTQ, AWQ, GGUF comparison"
  - title: "vLLM V1 Architecture"
    url: "https://www.ubicloud.com/blog/life-of-an-inference-request-vllm-v1"
    notes: "Deep dive into vLLM internals"
---

# LLM Serving & Inference

Serving LLMs efficiently is a critical engineering challenge. The right serving infrastructure can reduce costs by 10x and latency by 5x.

## Serving Frameworks

### vLLM
The de facto standard for open-weight LLM serving:
- **PagedAttention**: eliminates KV cache fragmentation
- **Continuous batching**: iter-level scheduling for max throughput
- **Prefix caching**: reuse common prompt prefixes
- **OpenAI-compatible API**: drop-in replacement

```bash
# Start vLLM server
vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 2
```

### Text Generation Inference (TGI)
Hugging Face's production serving solution:
- Built-in quantization (GPTQ, AWQ, bitsandbytes)
- Tensor parallelism across GPUs
- Streaming and token streaming
- Watermarking and token streaming

### TensorRT-LLM
NVIDIA's enterprise-grade inference:
- Compiles models to optimized CUDA kernels
- Maximum throughput on NVIDIA hardware
- FP8 quantization on Hopper GPUs
- Speculative decoding support

## Quantization

Reduce model precision to save memory and increase speed:

| Method | Precision | Quality | Speed | GPU Memory |
|--------|-----------|---------|-------|------------|
| FP16/BF16 | 16-bit | Baseline | Baseline | 2x model size |
| GPTQ | 4-bit | Excellent | Fast | ~0.5x model size |
| AWQ | 4-bit | Best | Fast | ~0.5x model size |
| GGUF | 4-bit | Good | CPU+GPU | ~0.5x model size |
| FP8 | 8-bit | Near-lossless | Very fast | ~1x model size |

### When to Use What
- **GPTQ/AWQ**: GPU serving with maximum quality
- **GGUF**: Local/CPU inference (llama.cpp, Ollama)
- **FP8**: NVIDIA Hopper GPUs (H100/H200)
- **bitsandbytes**: Quick 8-bit/4-bit experimentation

## Batching Strategies

### Static Batching
Group requests, process together, wait for longest:
- Simple but wastes GPU on short sequences

### Continuous Batching
Process at iteration level — add/remove requests dynamically:
- 2-4x throughput improvement
- vLLM and TGI implement this

### Speculative Decoding
Use a small draft model to propose tokens, large model to verify:
- 2-3x speedup for autoregressive generation
- Same quality as the large model alone

## GPU Optimization

### Memory Management
- **KV cache**: typically 60-80% of GPU memory
- **PagedAttention**: reduces KV cache waste to <4%
- **Offloading**: move layers to CPU when GPU is full

### Tensor Parallelism
Split model across multiple GPUs:
```bash
vllm serve model --tensor-parallel-size 4  # Split across 4 GPUs
```

### Quantization + Serving
```bash
# Serve a 4-bit quantized model
vllm serve TheBloke/Llama-2-7B-Chat-AWQ --quantization awq
```

## Key Takeaways

1. vLLM with PagedAttention is the standard for open-weight serving
2. Quantization (AWQ, GPTQ) reduces memory by 4x with minimal quality loss
3. Continuous batching is 2-4x more efficient than static batching
4. Speculative decoding speeds up generation without quality loss
5. Tensor parallelism scales serving across multiple GPUs
