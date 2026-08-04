---
slug: dl-09-building-an-mlp-in-pytorch
title: "Building an MLP in PyTorch"
description: "Your first complete neural network — from data loading to training loop to evaluation, using PyTorch's nn module."
order: 9
tags:
  - deep-learning
  - pytorch
  - mlp
  - neural-network
  - nn-module
prerequisites:
  - dl-08-pytorch-tensors-and-autograd
  - dl-06-loss-functions
  - dl-07-optimizers
references:
  - title: "PyTorch: Building a Neural Network in 60 Seconds"
    url: "https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html"
    description: "Official tutorial on building and training a model"
  - title: "PyTorch nn.Module Documentation"
    url: "https://pytorch.org/docs/stable/nn.html"
    description: "Complete reference for all nn layers, loss functions, and utilities"
  - title: "Writing a Training Loop from Scratch"
    url: "https://pytorch.org/tutorials/beginner/basics/optimizers_tutorial.html"
    description: "Tutorial on training loops, optimizers, and loss computation"
  - title: "MNIST with PyTorch (from scratch)"
    url: "https://nextjournal.com/gkoehler/pytorch-mnist/"
    description: "Step-by-step MNIST classification with MLP"
  - title: "Lightning Your PyTorch Code"
    url: "https://lightning.ai/docs/pytorch/stable/"
    description: "PyTorch Lightning for reducing boilerplate in training loops"
knowledge_refs:
  - dl-08-pytorch-tensors-and-autograd
  - dl-06-loss-functions
  - dl-07-optimizers
---

# Building an MLP in PyTorch

This lesson walks through building a complete multi-layer perceptron (MLP) from scratch — from data loading to training to evaluation. By the end, you'll have a working MNIST classifier.

## The Full Pipeline

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets, transforms
```

## Step 1: Load and Prepare Data

```python
# MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),                    # Convert to tensor [0, 1]
    transforms.Normalize((0.1307,), (0.3081,))  # MNIST mean/std
])

train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('./data', train=False, transform=transform)

# DataLoaders for batching
train_loader = DataLoader(train_data, batch_size=128, shuffle=True)
test_loader = DataLoader(test_data, batch_size=256, shuffle=False)
```

**Key concepts:**
- `transforms.ToTensor()`: Converts PIL Image to tensor, scales to [0, 1]
- `transforms.Normalize()`: Standardizes to zero mean, unit variance
- `DataLoader`: Handles batching, shuffling, and multi-processing
- `shuffle=True` for training (randomize order), `False` for testing (reproducibility)

## Step 2: Define the Model

```python
class MLP(nn.Module):
    def __init__(self, input_dim=784, hidden1=256, hidden2=128, num_classes=10):
        super().__init__()
        self.flatten = nn.Flatten()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, hidden1),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden1, hidden2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden2, num_classes)
        )
    
    def forward(self, x):
        x = self.flatten(x)      # (B, 1, 28, 28) → (B, 784)
        return self.layers(x)

model = MLP()
print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")
```

**Design choices:**
- `nn.Flatten()`: Reshapes image (1×28×28) to vector (784)
- `nn.Dropout(0.2)`: Randomly zeros 20% of activations during training (regularization)
- `nn.Sequential`: Chains layers in order — clean and readable
- No activation on output: `nn.CrossEntropyLoss` expects raw logits

## Step 3: Loss Function and Optimizer

```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)

# Optional: learning rate scheduler
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=10)
```

**Why these choices:**
- `CrossEntropyLoss`: Standard for multi-class classification, numerically stable
- `AdamW`: Fast convergence, proper weight decay
- `lr=1e-3`: Good starting point for Adam-family optimizers
- `weight_decay=0.01`: L2 regularization

## Step 4: Training Loop

```python
def train_epoch(model, loader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    
    for batch_x, batch_y in loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        
        optimizer.zero_grad()           # Reset gradients
        output = model(batch_x)          # Forward pass
        loss = criterion(output, batch_y) # Compute loss
        loss.backward()                  # Backward pass
        optimizer.step()                 # Update weights
        
        total_loss += loss.item() * batch_x.size(0)
        correct += (output.argmax(dim=1) == batch_y).sum().item()
        total += batch_x.size(0)
    
    return total_loss / total, correct / total

# Run training
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

for epoch in range(10):
    train_loss, train_acc = train_epoch(model, train_loader, optimizer, criterion, device)
    scheduler.step()
    print(f"Epoch {epoch+1}: loss={train_loss:.4f}, acc={train_acc:.4f}")
```

**The 5 steps explained:**
1. `zero_grad()`: Clear accumulated gradients from previous iteration
2. Forward pass: Compute prediction
3. Compute loss: Measure how wrong the prediction is
4. `backward()`: Compute gradients via backpropagation
5. `step()`: Update weights using computed gradients

## Step 5: Evaluation

```python
@torch.no_grad()  # Disable gradient computation for efficiency
def evaluate(model, loader, device):
    model.eval()
    correct = 0
    total = 0
    
    for batch_x, batch_y in loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        output = model(batch_x)
        correct += (output.argmax(dim=1) == batch_y).sum().item()
        total += batch_x.size(0)
    
    return correct / total

test_acc = evaluate(model, test_loader, device)
print(f"Test Accuracy: {test_acc:.4f}")
```

**Key differences from training:**
- `model.eval()`: Disables dropout and batch normalization updates
- `@torch.no_grad()`: Saves memory and computation (no gradient tracking)
- No optimizer or loss computation needed

## Step 6: Save and Load

```python
# Save model
torch.save(model.state_dict(), 'mnist_mlp.pth')

# Load model
model = MLP()
model.load_state_dict(torch.load('mnist_mlp.pth'))
model.eval()
```

**Best practice**: Save only `state_dict()` (weights), not the entire model. This is more portable and flexible.

## Common Patterns and Gotchas

### train() vs eval() Mode

```python
model.train()  # Dropout active, BatchNorm uses batch statistics
model.eval()   # Dropout off, BatchNorm uses running statistics
```

**Critical**: Forgetting to switch modes is a common bug. Dropout during evaluation makes predictions non-deterministic.

### Device Management

```python
# Always move model and data to the same device
model = model.to(device)
for batch in dataloader:
    batch = {k: v.to(device) for k, v in batch.items()}
    output = model(batch)
```

### Gradient Clipping

```python
# Prevent exploding gradients
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

### Mixed Precision Training

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
for batch in dataloader:
    optimizer.zero_grad()
    with autocast():
        loss = criterion(model(batch.x.to(device)), batch.y.to(device))
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

## Complete Training Script

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Data
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('./data', train=False, transform=transform)
train_loader = DataLoader(train_data, batch_size=128, shuffle=True)
test_loader = DataLoader(test_data, batch_size=256)

# Model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 256), nn.ReLU(), nn.Dropout(0.2),
    nn.Linear(256, 128), nn.ReLU(), nn.Dropout(0.2),
    nn.Linear(128, 10)
).to(device)

# Training
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-3)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=10)

for epoch in range(10):
    model.train()
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        loss = criterion(model(x), y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    scheduler.step()
    
    model.eval()
    with torch.no_grad():
        correct = sum(model(x.to(device)).argmax(1) == y.to(device) for x, y in test_loader)
        acc = correct.item() / len(test_data)
    print(f"Epoch {epoch+1}: test_acc={acc:.4f}")
```

## What's Next

Now that you can build and train networks, the next lesson covers **regularization for deep learning** — preventing overfitting in large networks.

## Further Reading

- PyTorch tutorials are the definitive starting point
- PyTorch Lightning eliminates boilerplate for larger projects
- Lightning AI's tutorials show production-quality training patterns
- For distributed training: see PyTorch's DDP (DistributedDataParallel) documentation
