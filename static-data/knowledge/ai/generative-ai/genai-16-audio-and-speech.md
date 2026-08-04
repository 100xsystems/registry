---
slug: genai-16-audio-and-speech
title: "Generative Audio & Speech"
description: "Text-to-speech, voice cloning, music generation, and the models behind ElevenLabs and Suno."
order: 16
tags:
  - generative-ai
  - audio
  - text-to-speech
  - voice-cloning
  - music-generation
prerequisites:
  - genai-01-what-is-generative-ai
  - genai-06-llm-architecture
references:
  - title: "Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions (Tacotron 2)"
    url: "https://arxiv.org/abs/1712.05884"
    description: "Shen et al.'s Tacotron 2 paper for neural text-to-speech"
  - title: "High Fidelity Neural Audio Synthesis (WaveNet)"
    url: "https://arxiv.org/abs/1609.03499"
    description: "van den Oord et al.'s WaveNet paper for raw audio generation"
  - title: "AudioLM: a Language Modeling Approach to Audio Generation"
    url: "https://arxiv.org/abs/2209.03143"
    description: "Google's AudioLM treating audio as a language modeling problem"
  - title: "Jukebox: A Generative Model for Music"
    url: "https://arxiv.org/abs/2005.00878"
    description: "OpenAI's Jukebox for music generation"
  - title: "MusicLM: Generating Music From Text"
    url: "https://arxiv.org/abs/2301.11325"
    description: "Google's MusicLM for text-to-music generation"
knowledge_refs:
  - genai-06-llm-architecture
  - genai-03-text-generation-basics
  - genai-13-diffusion-models
---

# Generative Audio & Speech

AI-generated audio spans text-to-speech, voice cloning, music composition, and sound effects. The field is rapidly converging on transformer-based architectures that treat audio as sequences of tokens.

## Text-to-Speech (TTS)

### The TTS Pipeline
```
Text → Text Encoder → Acoustic Model → Vocoder → Waveform
```

**Modern approach**: End-to-end models that go directly from text to audio tokens:

### Tacotron 2 (Google)
- Sequence-to-sequence model with attention
- Text → Mel spectrogram → WaveNet vocoder
- Natural-sounding speech

### VALL-E (Microsoft)
- Treats speech as discrete tokens (like language)
- Can clone a voice from just 3 seconds of audio
- Uses a two-stage architecture: AR for coarse tokens, NAR for refinement

### Bark (Suno)
- GPT-style model for speech generation
- Generates audio tokens autoregressively
- Supports multi-speaker, emotions, sound effects

```python
# Bark TTS example
from bark import SAMPLE_RATE, generate_audio, preload_models

preload_models()
audio_array = generate_audio("Hello, this is a test of AI speech generation!")
```

### ElevenLabs
- Proprietary high-fidelity TTS
- Voice cloning from minimal samples
- Real-time streaming generation

## Voice Cloning

### Zero-Shot Voice Cloning
Clone any voice from a short reference audio:
```
Reference audio (3-10 seconds) + Target text → Cloned speech
```

**VALL-E approach**:
1. Encode reference audio into discrete tokens
2. Use as prefix for autoregressive generation
3. Generate new speech in the cloned voice

### Fine-Tuned Voice Cloning
Train on more data for higher fidelity:
- 10-30 minutes of audio → very high quality cloning
- Requires speaker verification consent

## Audio Language Models

The latest approach treats audio as a language modeling problem:

### AudioLM
- Audio → Semantic tokens + Acoustic tokens
- Generate semantic tokens (what to say) then acoustic tokens (how it sounds)
- Preserves speaker identity and prosody

### MusicLM
- Text → Music generation
- Hierarchical sequence-to-sequence approach
- Generates 24kHz audio at 24 tokens/second

```python
# Example: Music generation with MusicLM-style approach
prompt = "A jazz piano trio playing a slow ballad"
# Model generates audio tokens autoregressively
# Decode to waveform using audio codec
```

## Audio Codecs (Tokenization for Audio)

Just like text tokenization, audio needs tokenization:

| Codec | Rate | Quality | Use Case |
|---|---|---|---|
| EnCodec | 24 tokens/sec | High | Music, speech |
| DAC | 21.5 tokens/sec | Very high | High-fidelity audio |
| SoundStream | 24 tokens/sec | High | Real-time streaming |

```python
# Encode audio to tokens
import torch
from encodec import EncodecModel

model = EncodecModel.encodec_model_24khz()
audio = torch.randn(1, 1, 24000)  # 1 second at 24kHz
encoded = model.encode(audio)
# encoded.audio_codes.shape: (1, 1, frames) — discrete tokens
```

## Music Generation

### Models
- **Suno**: Text-to-music with vocals and instruments
- **Udio**: High-quality music generation
- **MusicLM**: Google's text-to-music
- **Jukebox**: OpenAI's music generation
- **Stable Audio**: Diffusion-based audio generation

### Capabilities
- Generate full songs from text descriptions
- Control genre, tempo, instruments, mood
- Generate vocals and accompaniment
- Extend or remix existing music

## Sound Effects Generation

### AudioPaLM / AudioLDM
- Generate sound effects from text descriptions
- "A dog barking followed by a car horn"
- Useful for game development, film production

## Speech-to-Speech (Real-Time)

### Voice Conversion
- Change speaker identity while preserving content
- Real-time voice conversion for calls
- Character voice acting from reference audio

### Speech-to-Speech Translation
- Translate speech while preserving speaker voice
- Real-time multilingual communication
- Meta's SeamlessExpressive model

## Practical Applications

| Application | Technology | Examples |
|---|---|---|
| Accessibility | TTS | Screen readers, audiobooks |
| Content creation | Music gen | Background music, podcasts |
| Gaming | Sound FX | Dynamic soundscapes |
| Localization | Voice cloning | Dubbing in multiple languages |
| Customer service | TTS + STT | AI phone agents |
| Entertainment | Voice synthesis | Virtual characters |

## Practical Tips

1. **For TTS**: Use OpenAI TTS API or ElevenLabs for quality
2. **For voice cloning**: Ensure consent and ethical use
3. **For music**: Suno and Udio lead in quality
4. **Audio tokens**: EnCodec is the standard codec for research
5. **Streaming**: Use chunked generation for real-time applications

## Further Reading

- WaveNet pioneered neural audio generation
- Tacotron 2 established modern TTS architectures
- VALL-E showed voice cloning from minimal samples
- AudioLM and MusicLM treat audio as a language modeling problem
