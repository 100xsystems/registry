---
{
  "title": "Generative Audio & Speech",
  "description": "Text-to-speech, voice cloning and music generation with modern neural audio models.",
  "type": "lesson",
  "order": 16,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the TTS pipeline (text → tokens → waveform)",
    "Run a pretrained TTS model",
    "Understand audio tokenization",
    "Discuss voice-cloning ethics"
  ],
  "knowledge_refs": [
    "generative-ai/genai-15-vision-language-models",
    "nlp/nlp-10-pos-tagging"
  ],
  "prerequisites": [
    "GENAI-03: Text Generation Fundamentals"
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

# GENAI-16-AUDIO-AND-SPEECH: Generative Audio & Speech

## Introduction

Text-to-speech, voice cloning and music generation with modern neural audio models. By the end of this lesson you will be able to: Explain the TTS pipeline (text → tokens → waveform); Run a pretrained TTS model; Understand audio tokenization; Discuss voice-cloning ethics.

## Key Concepts

### 1. Explain the TTS pipeline (text → tokens → waveform)

Target: Explain the TTS pipeline (text → tokens → waveform). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

# Audio as waveforms and spectrograms
wave = torch.randn(16000)
print("1 second at 16kHz:", wave.shape)
```
### 2. Run a pretrained TTS model

Target: Run a pretrained TTS model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import pipeline

tts = pipeline("text-to-speech", model="facebook/mms-tts-eng")
out = tts("Hello world")
print("sample rate:", out["sampling_rate"])
```
### 3. Understand audio tokenization

Target: Understand audio tokenization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Spectrogram: frequency content over time
sr = 16000
freqs = np.fft.rfftfreq(1024, 1 / sr)
print("spectrogram bins:", len(freqs))
```
### 4. Discuss voice-cloning ethics

Target: Discuss voice-cloning ethics. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("voice cloning requires consent")
```

## Practice Questions

1. What is the key idea behind "Generative Audio & Speech"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generative Audio & Speech with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generative Audio & Speech"
1. "Provide advanced patterns and performance considerations for Generative Audio & Speech"

## Key Takeaways

- Master the core ideas of Generative Audio & Speech through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
