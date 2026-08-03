---
{
  "title": "Generative Adversarial Networks",
  "description": "Two networks in a zero-sum game: the generator fools the discriminator, and both improve.",
  "type": "lesson",
  "order": 14,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the generator-discriminator game",
    "Train a simple GAN",
    "Handle mode collapse and instability",
    "Compare GANs to diffusion"
  ],
  "knowledge_refs": [
    "generative-ai/genai-13-diffusion-models",
    "ai-safety/safety-05-robustness",
    "deep-learning/dl-12-convolutional-networks"
  ],
  "prerequisites": [
    "DL-12: Convolutional Networks"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "Transformers, fine-tuning and LLM fundamentals with hands-on code."
    },
    {
      "title": "OpenAI Documentation",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for GPT models, embeddings and function calling."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The Transformer paper that made generative AI possible."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "DeepLearning.AI Short Courses",
      "url": "https://www.deeplearning.ai/short-courses/",
      "description": "Practical AI courses from industry experts."
    }
  ]
}
---

# GENAI-14-GANS: Generative Adversarial Networks

## Introduction

Two networks in a zero-sum game: the generator fools the discriminator, and both improve. By the end of this lesson you will be able to: Explain the generator-discriminator game; Train a simple GAN; Handle mode collapse and instability; Compare GANs to diffusion.

## Key Concepts

### 1. Explain the generator-discriminator game

Target: Explain the generator-discriminator game. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(100, 256), nn.ReLU(), nn.Linear(256, 784), nn.Tanh())
    def forward(self, z):
        return self.net(z)

print(Generator())
```
### 2. Train a simple GAN

Target: Train a simple GAN. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(784, 256), nn.LeakyReLU(0.2), nn.Linear(256, 1), nn.Sigmoid())
    def forward(self, x):
        return self.net(x)

print(Discriminator())
```
### 3. Handle mode collapse and instability

Target: Handle mode collapse and instability. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

z = torch.randn(8, 100)  # latent noise
fake = Generator()(z)
print("fake images:", fake.shape)
```
### 4. Compare GANs to diffusion

Target: Compare GANs to diffusion. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch.nn as nn

# GAN loss: binary cross-entropy on real vs fake
loss = nn.BCELoss()
print("adversarial objective ready")
```

## Practice Questions

1. What is the key idea behind "Generative Adversarial Networks"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generative Adversarial Networks with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generative Adversarial Networks"
1. "Provide advanced patterns and performance considerations for Generative Adversarial Networks"

## Key Takeaways

- Master the core ideas of Generative Adversarial Networks through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
