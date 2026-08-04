---
slug: genai-07-tokenization
title: "Tokenization & the Vocabulary"
description: "The bridge between human text and model input — BPE, WordPiece, SentencePiece, and why tokenization matters more than you think."
order: 7
tags:
  - generative-ai
  - tokenization
  - bpe
  - wordpiece
  - sentencepiece
prerequisites:
  - genai-03-text-generation-basics
  - genai-06-llm-architecture
references:
  - title: "Hugging Face: Tokenization Algorithms"
    url: "https://huggingface.co/docs/transformers/en/tokenizer_summary"
    description: "Comprehensive overview of BPE, WordPiece, Unigram, and SentencePiece"
  - title: "Hugging Face LLM Course: Byte-Pair Encoding"
    url: "https://huggingface.co/learn/llm-course/en/chapter6/5"
    description: "Step-by-step guide to training a BPE tokenizer from scratch"
  - title: "BPE Tokenizer From Scratch (Sebastian Raschka)"
    url: "https://sebastianraschka.com/blog/2025/bpe-from-scratch.html"
    description: "Educational walkthrough implementing GPT-style BPE tokenization"
  - title: "tiktoken — OpenAI's Fast BPE Tokenizer"
    url: "https://pypi.org/project/tiktoken/"
    description: "Official documentation for OpenAI's high-performance tokenizer"
  - title: "Hugging Face Tokenizers Library"
    url: "https://huggingface.co/docs/tokenizers/quicktour"
    description: "Rust-backed tokenization library with alignment tracking"
knowledge_refs:
  - genai-03-text-generation-basics
  - genai-06-llm-architecture
  - genai-02-probabilistic-generation
---

# Tokenization & the Vocabulary

Tokenization is the process of converting text into the integer sequences that models actually process. It's one of the most underappreciated components of LLMs — and getting it wrong can break everything.

## Why Tokenization Matters

Models don't process raw text — they process tokens:
- "Hello" → [15496]
- "tokenization" → [23668, 1643, 290]
- "🤖" → [12520, 9747]

**Token efficiency** directly affects:
- **Cost**: API pricing is per-token
- **Context length**: Fewer tokens = more content fits
- **Performance**: Poor tokenization hurts model understanding
- **Multilingual**: Non-English text may need 3-5x more tokens

## Byte Pair Encoding (BPE)

The dominant algorithm for modern LLMs (GPT, LLaMA, Mistral):

### How BPE Works

1. Start with individual characters (or bytes) as the vocabulary
2. Count all adjacent pairs in the training corpus
3. Merge the most frequent pair into a new token
4. Repeat until desired vocabulary size

**Example:**
```
Corpus: "low low low low low lowest lowest newer newer newer"

Initial: l o w _ l o w _ l o w _ l o w _ l o w _ l o w e s t _ n e w e r
Step 1:  Merge (l,o) → lo:  lo w _ lo w _ lo w _ lo w _ lo w _ lo w e s t _ n e w e r
Step 2:  Merge (lo,w) → low: low _ low _ low _ low _ low _ low e s t _ n e w e r
Step 3:  Merge (low,_) → low_: low_ low_ low_ low_ low_ low e s t _ n e w e r
Step 4:  Merge (e,r) → er:   low_ low_ low_ low_ low_ low e s t _ n ew er
...
```

### Byte-Level BPE

GPT-2 and later models use **byte-level BPE**:
- Base vocabulary is 256 bytes (not Unicode characters)
- Guarantees zero `<unk>` tokens (any byte sequence is valid)
- Handles emojis, rare symbols, non-Latin scripts

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer
tokens = enc.encode("Hello, world! 🤖")
print(tokens)  # [9906, 11, 1917, 0, 12520, 9747]
print(enc.decode(tokens))  # "Hello, world! 🤖"
```

## WordPiece

Used by BERT and similar encoder models:
- Similar to BPE but uses **likelihood-based scoring**
- Score = frequency(AB) / (frequency(A) × frequency(B))
- Favors merging tokens that co-occur more than expected by chance

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.tokenize("tokenization is important")
# ['token', '##ization', 'is', 'important']
```

## SentencePiece

Google's library that works on raw text (no pre-tokenization):
- Treats spaces as special characters (▁)
- Works with any language (no language-specific rules)
- Supports both BPE and Unigram algorithms
- Used by: T5, XLNet, LLaMA

```python
import sentencepiece as spm
sp = spm.SentencePieceProcessor(model_file='model.model')
tokens = sp.encode("Hello world", out_type=str)
# ['▁Hello', '▁world']
```

## Tokenizer Comparison

| Algorithm | Used By | Base Units | Key Feature |
|---|---|---|---|
| BPE | GPT, LLaMA, Mistral | Characters/bytes | Frequency-based merging |
| WordPiece | BERT, DistilBERT | Characters | Likelihood-based merging |
| SentencePiece | T5, XLNet, LLaMA | Raw text | Language-agnostic |
| Unigram | T5, ALBERT | Subwords | Top-down pruning |
| tiktoken | GPT-4, GPT-4o | Bytes | Ultra-fast Rust implementation |

## Vocabulary Sizes

| Model | Vocab Size | Encoding |
|---|---|---|
| GPT-2 | 50,257 | BPE |
| BERT | 30,522 | WordPiece |
| LLaMA | 32,000 | SentencePiece BPE |
| LLaMA 3 | 128,256 | tiktoken BPE |
| GPT-4 | 100,256 | tiktoken BPE |
| GPT-4o | 200,019 | tiktoken BPE |

**Larger vocabularies**: More efficient tokenization (fewer tokens per text), but larger embedding layer.

## Multilingual Tokenization Challenges

Tokenizers trained primarily on English are inefficient for other languages:

```
English:  "Hello world" → 2 tokens
Hindi:    "नमस्ते दुनिया" → 7 tokens (same meaning!)
Thai:     "สวัสดีชาวโลก" → 12 tokens
```

**Impact**: Non-English users pay more, get less context, and may get worse quality.

**Solutions**:
- Larger vocabularies (LLaMA 3: 128K tokens)
- Multilingual training data
- Language-specific tokenizers

## Tokenization Pitfalls

1. **Trailing whitespace**: "hello" vs "hello " → different tokens
2. **Number handling**: "12345" → ["123", "45"] (model may not understand numbers)
3. **Code formatting**: Indentation, whitespace matters
4. **Special tokens**: Models have specific tokens they expect

## Practical Tips

1. **Always check token count** before sending to API (cost + context)
2. **Use the correct tokenizer** for your model (wrong tokenizer = garbage)
3. **Respect token limits**: Leave room for output tokens
4. **Pre-tokenize for efficiency**: Batch tokenization is faster
5. **Handle special tokens**: `<bos>`, `<eos>`, `<pad>` have special meanings

## Further Reading

- Hugging Face's tokenization guide is the definitive reference
- Sebastian Raschka's BPE walkthrough is excellent for understanding the algorithm
- tiktoken documentation shows production tokenization at scale
- For multilingual: look into SentencePiece and language-specific tokenizers
