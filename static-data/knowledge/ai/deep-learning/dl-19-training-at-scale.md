---
slug: dl-19-training-at-scale
title: "Training at Scale"
description: "Distributed training, mixed precision, gradient accumulation — techniques for training large models efficiently."
order: 19
tags:
  - deep-learning
  - distributed-training
  - mixed-precision
  - scaling
  - infrastructure
prerequisites:
  - dl-10-the-training-loop
  - dl-07-optimizers
  - dl-08-pytorch-tensors-and-autograd
references:
  - title: "PyTorch Distributed Tutorial"
    url: "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"
    description: "Official PyTorch tutorial on distributed data parallel training"
  - title: "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"
    url: "https://arxiv.org/abs/1910.02054"
    description: "Rajbhandari et al.'s ZeRO optimizer for memory-efficient training"
  - title: "Mixed Precision Training (Micikevicius et al.)"
    url: "https://arxiv.org/abs/1710.03740"
    description: "The foundational mixed precision training paper"
  - title: "Scaling Laws for Neural Language Models"
    url: "https://arxiv.org/abs/2001.08361"
    description: "Kaplan et al.'s scaling laws — how performance scales with compute"
  - title: "DeepSpeed Documentation"
    url: "https://www.deepspeed.ai/"
    description: "Microsoft's library for distributed training and inference optimization"
knowledge_refs:
  - dl-10-the-training-loop
  - dl-07-optimizers
  - dl-08-pytorch-tensors-and-autograd
---

# Training at Scale

Modern deep learning models are too large for single GPUs. Training at scale requires distributed training, memory optimization, and careful coordination across hardware.

## Why Scale?

- **GPT-3**: 175B parameters, 3.14 × 10²³ FLOPs
- **Single A100 GPU**: 312 TFLOPS FP16 → would take ~33 years
- **1024 A100s**: Training completes in weeks

Scaling isn't just about speed — it's about **feasibility**.

## Distributed Data Parallel (DDP)

The most common approach: replicate the model on each GPU, process different data, synchronize gradients:

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):
    dist.init_process_group("nccl", rank=rank, world_size=world_size)
    torch.cuda.set_device(rank)

def train(rank, world_size):
    setup(rank, world_size)
    model = MyModel().to(rank)
    model = DDP(model, device_ids=[rank])
    
    sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank)
    loader = DataLoader(dataset, batch_size=32, sampler=sampler)
    
    for epoch in range(num_epochs):
        sampler.set_epoch(epoch)
        for batch in loader:
            loss = model(batch)
            loss.backward()   # Gradients synced automatically
            optimizer.step()
            optimizer.zero_grad()
```

**How DDP works:**
1. Each GPU has a full model copy
2. Each GPU processes a different data shard
3. After backward pass, gradients are averaged across all GPUs (AllReduce)
4. Each GPU updates its copy identically

## Data Parallelism vs. Model Parallelism

| Type | How It Works | When to Use |
|---|---|---|
| Data Parallelism | Replicate model, split data | Model fits in one GPU |
| Model Parallelism | Split model across GPUs | Model too large for one GPU |
| Pipeline Parallelism | Split model by layers | Sequential architectures |
| Tensor Parallelism | Split individual layers | Very large layers (attention, FFN) |
| ZeRO | Shard optimizer states + gradients | Large models, limited memory |

## Mixed Precision Training

Use FP16 (half) for forward/backward, FP32 for weight updates:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for data, target in loader:
    optimizer.zero_grad()
    
    with autocast():
        output = model(data)
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(optimizer)
    scaler.update()
```

**Benefits:**
- 2x less memory (FP16 = 2 bytes, FP32 = 4 bytes)
- 1.5-3x faster (tensor cores optimized for FP16)
- Same model quality (with loss scaling)

**AMP (Automatic Mixed Precision)** automatically determines which operations use FP16 vs FP32.

## Gradient Accumulation

For larger effective batch sizes when GPU memory is limited:

```python
accumulation_steps = 8  # Effective batch = 32 * 8 = 256

optimizer.zero_grad()
for i, (data, target) in enumerate(loader):
    with autocast():
        loss = model(data) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

## Gradient Checkpointing

Trade compute for memory by recomputing activations during backward pass:

```python
from torch.utils.checkpoint import checkpoint

class LargeModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = LargeBlock()
        self.block2 = LargeBlock()
        self.block3 = LargeBlock()
    
    def forward(self, x):
        # checkpoint re-runs forward during backward
        x = checkpoint(self.block1, x, use_reentrant=False)
        x = checkpoint(self.block2, x, use_reentrant=False)
        x = checkpoint(self.block3, x, use_reentrant=False)
        return x
```

**Trade-off**: ~30% more compute, ~60% less memory. Essential for training very deep models.

## ZeRO (Zero Redundancy Optimizer)

Shard optimizer states and gradients across GPUs:

| Stage | What's Sharded | Memory Savings |
|---|---|---|
| ZeRO-1 | Optimizer states | 4x |
| ZeRO-2 | + Gradients | 8x |
| ZeRO-3 | + Parameters | N× (N = number of GPUs) |

```python
import deepspeed

model_engine, optimizer, _, _ = deepspeed.initialize(
    model=model,
    model_parameters=model.parameters(),
    config=ds_config
)

# Training loop
for data, target in loader:
    loss = model_engine(data)
    model_engine.backward(loss)
    model_engine.step()
```

## Communication Patterns

| Pattern | Description | Used By |
|---|---|---|
| AllReduce | Average gradients across all GPUs | DDP |
| AllGather | Collect all shards | ZeRO-3 |
| ReduceScatter | Sum and scatter gradients | ZeRO-1 |
| AllToAll | Custom communication | Pipeline parallel |

## Scaling Laws

Performance follows power laws with compute:
$$L(C) \approx \left(\frac{C_0}{C}\right)^{\alpha_N}$$

where $L$ is loss, $C$ is compute, and $\alpha_N \approx 0.076$.

**Key insight**: To double performance, you need ~10x more compute. This drives the trend toward larger models and datasets.

## Practical Guidelines

1. **Start with DDP** — it's simplest and works for most models
2. **Use mixed precision** — always, on modern GPUs
3. **Gradient accumulation** — when batch size > GPU memory
4. **Gradient checkpointing** — when model is very deep
5. **ZeRO-2** — for models > 1B parameters
6. **Monitor GPU utilization** — aim for > 80%
7. **Profile before optimizing** — find the actual bottleneck

## Common Pitfalls

1. **Not using DDP's sampler**: Data will be duplicated across GPUs
2. **Forgetting `model.train()` after DDP wrap**: BatchNorm breaks
3. **Uneven batch sizes**: Last batch causes AllReduce hangs
4. **Not setting `find_unused_parameters=True`**: Some architectures need this
5. **Wrong learning rate scaling**: Linear scaling rule: lr × num_gpus

## Further Reading

- PyTorch DDP tutorial is the starting point for distributed training
- DeepSpeed documentation covers ZeRO and pipeline parallelism
- Kaplan et al.'s scaling laws predict model performance from compute budget
- For very large models: Megatron-LM and DeepSpeed pipeline parallelism
