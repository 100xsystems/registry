---
slug: dl-10-the-training-loop
title: "The Training Loop in Depth"
description: "Understanding every detail of the training loop — batch processing, gradient accumulation, mixed precision, and monitoring."
order: 10
tags:
  - deep-learning
  - training-loop
  - debugging
  - monitoring
prerequisites:
  - dl-09-building-an-mlp-in-pytorch
  - dl-07-optimizers
  - dl-06-loss-functions
references:
  - title: "PyTorch Training Loop Tutorial"
    url: "https://pytorch.org/tutorials/beginner/basics/optimizers_tutorial.html"
    description: "Official tutorial on the training loop and optimization"
  - title: "A Recipe for Training Neural Networks (Karpathy)"
    url: "https://karpathy.github.io/2019/04/25/recipe/"
    description: "Karpathy's famous recipe for debugging and training neural networks"
  - title: "fast.ai: Training Loop Deep Dive"
    url: "https://docs.fast.ai/basic_data.html"
    description: "fast.ai's detailed treatment of data loading and training"
  - title: "WandB: Effective Training Documentation"
    url: "https://docs.wandb.ai/guides/training/"
    description: "Weights & Biases guide on experiment tracking and monitoring"
  - title: "How to Train Your ResNet (FB AI Research)"
    url: "https://github.com/facebookresearch/OpenImages"
    description: "Practical tips from FAIR on training large vision models"
knowledge_refs:
  - dl-09-building-an-mlp-in-pytorch
  - dl-07-optimizers
  - dl-19-training-at-scale
---

# The Training Loop in Depth

The training loop is where everything comes together. Understanding its nuances — what happens at each step, what can go wrong, and how to debug it — is what separates practitioners who can build working models from those who can't.

## Anatomy of a Training Loop

```python
for epoch in range(num_epochs):
    # --- Training phase ---
    model.train()
    train_loss = 0
    
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        
        # 1. Forward pass
        output = model(data)
        loss = criterion(output, target)
        
        # 2. Backward pass
        optimizer.zero_grad()  # Clear gradients
        loss.backward()         # Compute gradients
        
        # 3. Gradient processing
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        # 4. Update weights
        optimizer.step()
        
        # 5. Bookkeeping
        train_loss += loss.item()
    
    # --- Validation phase ---
    model.eval()
    val_loss = 0
    correct = 0
    
    with torch.no_grad():
        for data, target in val_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            val_loss += criterion(output, target).item()
            correct += (output.argmax(1) == target).sum().item()
    
    # 6. Learning rate scheduling
    scheduler.step()
    
    # 7. Logging
    avg_train_loss = train_loss / len(train_loader)
    val_acc = correct / len(val_dataset)
    print(f"Epoch {epoch}: train_loss={avg_train_loss:.4f}, val_acc={val_acc:.4f}")
```

## Step-by-Step Breakdown

### 1. Forward Pass
Data flows through the model to produce predictions. PyTorch's autograd records the computation graph for backward pass.

```python
output = model(data)  # All layer computations recorded
```

### 2. Loss Computation
Compare prediction to ground truth using the loss function.

```python
loss = criterion(output, target)  # Returns a scalar tensor
```

### 3. Zero Gradients
**Must be done before backward pass.** PyTorch accumulates gradients by default (useful for gradient accumulation, but requires explicit zeroing).

```python
optimizer.zero_grad()  # OR model.zero_grad() OR set_to_none=True
# For slightly better performance:
optimizer.zero_grad(set_to_none=True)  # Sets gradients to None instead of zero
```

### 4. Backward Pass
Compute gradients via backpropagation.

```python
loss.backward()  # Computes d(loss)/d(param) for all parameters with requires_grad=True
```

### 5. Gradient Clipping
Prevent exploding gradients (especially important for RNNs and transformers).

```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

### 6. Optimizer Step
Update parameters using computed gradients.

```python
optimizer.step()  # Applies the update rule (SGD, Adam, AdamW, etc.)
```

## Batch Size and Memory

**Larger batches:**
- Better GPU utilization (more parallelism)
- More stable gradients (less noise)
- But: more memory, may generalize worse

**Smaller batches:**
- Regularization effect (gradient noise)
- Faster convergence per epoch (more updates)
- But: less GPU utilization, noisier gradients

```python
# Find the largest batch size that fits in GPU memory
# Start small, increase until OOM, then back off
for batch_size in [32, 64, 128, 256, 512]:
    try:
        data = torch.randn(batch_size, 3, 224, 224).to(device)
        output = model(data)
        print(f"batch_size={batch_size} works")
    except RuntimeError as e:
        if "out of memory" in str(e):
            print(f"batch_size={batch_size} OOM")
            break
```

## Gradient Accumulation

For larger effective batch sizes when memory is limited:

```python
accumulation_steps = 4
optimizer.zero_grad()

for i, (data, target) in enumerate(train_loader):
    output = model(data.to(device))
    loss = criterion(output, target.to(device)) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

**Effective batch size** = `batch_size × accumulation_steps × num_gpus`

## Mixed Precision Training

Use FP16 for forward/backward, FP32 for weight updates:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
model.train()

for data, target in train_loader:
    data, target = data.to(device), target.to(device)
    
    optimizer.zero_grad()
    
    with autocast():  # FP16 forward pass
        output = model(data)
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()  # FP16 backward pass
    scaler.unscale_(optimizer)     # Unscale before clipping
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(optimizer)         # FP32 weight update
    scaler.update()
```

**Benefits**: 2x less memory, 1.5-3x faster on modern GPUs (V100, A100).

## Monitoring and Debugging

### Loss Curves

```python
# Track training and validation loss
# Healthy: both decrease, converge
# Overfitting: train loss ↓, val loss ↑
# Underfitting: both high, barely decreasing
# Divergence: train loss → NaN or ↑
```

### Gradient Statistics

```python
# Monitor gradient magnitudes
for name, p in model.named_parameters():
    if p.grad is not None:
        writer.add_scalar(f'grad_norm/{name}', p.grad.norm(), step)
```

**Healthy**: Gradient norms around 0.01-1.0
**Vanishing**: Gradient norms < 1e-6
**Exploding**: Gradient norms > 100

### Activation Statistics

```python
# Hook to monitor activations
def print_stats(module, input, output):
    if isinstance(output, torch.Tensor):
        print(f"{module.__class__.__name__}: "
              f"mean={output.mean():.3f}, std={output.std():.3f}")

model.apply(print_stats)
```

### Learning Rate Tracking

```python
for param_group in optimizer.param_groups:
    writer.add_scalar('lr', param_group['lr'], step)
```

## Common Bugs and Fixes

| Symptom | Likely Cause | Fix |
|---|---|---|
| Loss = NaN | Exploding gradients, bad data | Gradient clipping, check data |
| Loss doesn't decrease | LR too high/low, bad architecture | Learning rate finder, simpler model |
| Train loss << val loss | Overfitting | More data, regularization, early stopping |
| Loss oscillates wildly | LR too high | Reduce learning rate |
| Accuracy stuck at random | Model not learning | Check data, loss function, gradients |
| OOM (out of memory) | Batch too large | Reduce batch size, gradient accumulation |
| Very slow training | Small batch, no mixed precision | Larger batch, AMP, DataLoader workers |

## Karpathy's Recipe

1. Start with a simple model on a single batch — overfit it
2. Gradually add complexity (more data, regularization)
3. If something breaks, go back to step 1
4. Monitor training/validation loss curves
5. Use learning rate finder
6. Never train a model you don't understand

## Checkpointing and Early Stopping

```python
best_val_loss = float('inf')
patience_counter = 0

for epoch in range(max_epochs):
    train_loss = train_epoch(model, train_loader, optimizer, criterion, device)
    val_loss = evaluate_loss(model, val_loader, criterion, device)
    
    # Save best model
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), 'best_model.pth')
        patience_counter = 0
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print(f"Early stopping at epoch {epoch}")
            break

# Load best model
model.load_state_dict(torch.load('best_model.pth'))
```

## Further Reading

- Karpathy's recipe is essential reading for every practitioner
- WandB documentation covers experiment tracking in depth
- PyTorch Lightning eliminates most of this boilerplate automatically
- For production: TorchServe and Triton handle model serving
