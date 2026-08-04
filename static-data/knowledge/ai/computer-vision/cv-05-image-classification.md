---
slug: cv-05-image-classification
title: "Image Classification"
description: "The foundation of computer vision — from softmax outputs to training pipelines and evaluation metrics."
order: 5
tags:
  - computer-vision
  - classification
  - softmax
  - cross-entropy
  - training-pipeline
prerequisites:
  - cv-02-image-representation
  - cv-04-image-augmentation
  - dl-09-building-an-mlp-in-pytorch
references:
  - title: "CS231n: Image Classification"
    url: "https://cs231n.github.io/classification/"
    description: "Stanford's foundational image classification notes"
  - title: "PyTorch Image Classification Tutorial"
    url: "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"
    description: "Official PyTorch tutorial on CIFAR-10 classification"
  - title: "ImageNet Large Scale Visual Recognition Challenge"
    url: "https://www.image-net.org/challenges/LSVRC/"
    description: "The benchmark that drove CV progress"
  - title: "timm: PyTorch Image Models"
    url: "https://github.com/huggingface/pytorch-image-models"
    description: "Ross Wightman's comprehensive model zoo"
  - title: "torchvision Models"
    url: "https://pytorch.org/vision/stable/models.html"
    description: "Official pretrained vision models"
knowledge_refs:
  - cv-04-image-augmentation
  - dl-12-convolutional-networks
  - dl-14-transfer-learning
---

# Image Classification

Image classification is the most fundamental computer vision task — assigning a label to an entire image. Every other vision task builds on classification concepts.

## The Classification Pipeline

```
Input Image (224×224×3)
    ↓
[Preprocessing] → Normalize, augment
    ↓
[Feature Extractor] → CNN or ViT backbone
    ↓
[Classifier Head] → Linear + Softmax
    ↓
Output: [p₁, p₂, ..., pₖ] (probabilities for K classes)
```

## Softmax and Cross-Entropy

### Softmax
Converts logits to probabilities:
$$P(y = k) = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$

```python
import torch.nn.functional as F

logits = torch.tensor([2.0, 1.0, 0.5])
probs = F.softmax(logits, dim=0)
print(probs)  # [0.596, 0.219, 0.185]
```

### Cross-Entropy Loss
Measures the difference between predicted and true distribution:
$$\mathcal{L} = -\sum_{k=1}^{K} y_k \log(\hat{y}_k)$$

```python
# PyTorch combines LogSoftmax + NLLLoss
criterion = nn.CrossEntropyLoss()

logits = model(images)  # Raw output, no softmax!
loss = criterion(logits, labels)  # Labels are class indices
```

**Critical**: `CrossEntropyLoss` expects raw logits, not softmax outputs.

## Complete Training Pipeline

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader

# 1. Data
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

test_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

train_dataset = datasets.CIFAR10('./data', train=True, download=True, transform=train_transform)
test_dataset = datasets.CIFAR10('./data', train=False, transform=test_transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=256, shuffle=False)

# 2. Model (transfer learning)
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
model.fc = nn.Linear(model.fc.in_features, 10)  # 10 classes
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# 3. Loss, optimizer, scheduler
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=10)

# 4. Training loop
for epoch in range(10):
    model.train()
    total_loss, correct, total = 0, 0, 0
    
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        correct += (outputs.argmax(1) == labels).sum().item()
        total += labels.size(0)
    
    scheduler.step()
    
    # 5. Evaluation
    model.eval()
    val_correct, val_total = 0, 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            val_correct += (outputs.argmax(1) == labels).sum().item()
            val_total += labels.size(0)
    
    print(f"Epoch {epoch+1}: loss={total_loss/len(train_loader):.4f}, "
          f"train_acc={correct/total:.4f}, val_acc={val_correct/val_total:.4f}")
```

## Evaluation Metrics

### Top-1 Accuracy
The predicted class must be exactly correct:
```python
top1_correct = (predictions.argmax(1) == labels).sum().item()
top1_acc = top1_correct / len(labels)
```

### Top-5 Accuracy
The correct class must be among the top 5 predictions:
```python
top5_correct = predictions.topk(5, dim=1).indices.eq(labels.unsqueeze(1)).any(1).sum().item()
top5_acc = top5_correct / len(labels)
```

### Per-Class Accuracy
Identifies which classes are problematic:
```python
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_true, y_pred, target_names=class_names))
```

### Confusion Matrix
Visualizes which classes are confused:
```python
from sklearn.metrics import ConfusionMatrixDisplay
cm = confusion_matrix(y_true, y_pred)
ConfusionMatrixDisplay(cm, display_labels=class_names).plot(xticks_rotation=45)
```

## Common Pitfalls

1. **Using softmax with CrossEntropyLoss**: Double-softmax → wrong gradients
2. **Forgetting to normalize**: Model expects ImageNet normalization
3. **Not switching eval mode**: Dropout/BatchNorm behave differently
4. **Data leakage**: Augmenting test data
5. **Class imbalance**: Use weighted loss or oversampling

## Practical Tips

1. **Start with transfer learning**: ResNet/EfficientNet pretrained on ImageNet
2. **Use AdamW + cosine schedule**: Strong default optimizer
3. **Monitor train/val gap**: Large gap = overfitting
4. **Try test-time augmentation**: Average predictions over augmented views
5. **Use confusion matrix**: Find which classes confuse the model

## Further Reading

- CS231n classification notes are the foundational reference
- PyTorch's CIFAR-10 tutorial is the hands-on starting point
- timm provides 1000+ pretrained vision models
- For competition-winning techniques: look at Kaggle image classification solutions
