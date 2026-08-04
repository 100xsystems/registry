---
slug: genai-17-evaluating-llms
title: "Evaluating LLMs"
description: "Benchmarks, human evaluation, and practical metrics for assessing language model quality and safety."
order: 17
tags:
  - generative-ai
  - evaluation
  - benchmarks
  - human-evaluation
  - safety
prerequisites:
  - genai-06-llm-architecture
  - genai-03-text-generation-basics
references:
  - title: "Holistic Evaluation of Language Models (HELM)"
    url: "https://arxiv.org/abs/2211.09110"
    description: "Liang et al.'s HELM framework for comprehensive LLM evaluation"
  - title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference"
    url: "https://arxiv.org/abs/2403.04132"
    description: "LMSYS's Chatbot Arena for human preference evaluation"
  - title: "MMLU: Measuring Massive Multitask Language Understanding"
    url: "https://arxiv.org/abs/2009.03300"
    description: "Hendrycks et al.'s MMLU benchmark for knowledge evaluation"
  - title: "TruthfulQA: Measuring How Models Mimic Human Falsehoods"
    url: "https://arxiv.org/abs/2109.07958"
    description: "Lin et al.'s benchmark for truthfulness evaluation"
  - title: "MT-Bench: Evaluating LLMs with Multi-Turn Questions"
    url: "https://arxiv.org/abs/2306.05685"
    description: "Zheng et al.'s multi-turn evaluation benchmark"
knowledge_refs:
  - genai-06-llm-architecture
  - genai-03-text-generation-basics
  - genai-09-rlhf-and-alignment
---

# Evaluating LLMs

Evaluating language models is notoriously difficult — there's no single metric that captures everything. A comprehensive evaluation combines automated benchmarks, human judgment, and task-specific testing.

## The Evaluation Challenge

LLMs are multi-task models — they can write, code, reason, translate, and more. No single benchmark captures all capabilities. Common pitfalls:
- **Benchmark contamination**: Training data contains test questions
- **Overfitting to benchmarks**: Models optimize for specific metrics
- **Benchmark saturation**: Top models score similarly on many benchmarks
- **Missing practical utility**: High benchmark scores ≠ useful in practice

## Automated Benchmarks

### Knowledge & Reasoning
| Benchmark | What It Tests | Format |
|---|---|---|
| **MMLU** | 57 subjects, graduate-level | Multiple choice |
| **MMLU-Pro** | Harder version of MMLU | 10 options per question |
| **ARC** | Science reasoning | Multiple choice |
| **HellaSwag** | Common sense | Sentence completion |
| **WinoGrande** | Coreference resolution | Binary choice |

### Code
| Benchmark | What It Tests | Format |
|---|---|---|
| **HumanEval** | Python function generation | Pass@k |
| **MBPP** | Python programming problems | Pass@k |
| **SWE-bench** | Real GitHub issues | PR generation |
| **LiveCodeBench** | Competitive programming | Contest problems |

### Math
| Benchmark | What It Tests | Format |
|---|---|---|
| **GSM8K** | Grade school math | Open-ended |
| **MATH** | Competition math | Open-ended |
| **Numble** | Number reasoning | Open-ended |

### Truthfulness
| Benchmark | What It Tests | Format |
|---|---|---|
| **TruthfulQA** | Avoiding common misconceptions | Generation |
| **SimpleQA** | Factual accuracy | Short answer |

## Human Evaluation

### Chatbot Arena (LMSYS)
- Humans chat with two anonymous models
- Pick the better response
- ELO ratings computed from thousands of battles
- **Gold standard** for practical model comparison

```python
# Example Arena-style evaluation
# Two models generate responses to same prompt
# Human picks winner: Model A or Model B
# Results aggregated into ELO ratings
```

### MT-Bench
- 80 multi-turn questions across 8 categories
- GPT-4 judges response quality (1-10 scale)
- Categories: writing, roleplay, reasoning, math, coding, extraction, STEM, humanities

## Evaluation Metrics

### Automated Metrics
| Metric | What It Measures | Limitations |
|---|---|---|
| **Perplexity** | Language modeling quality | Lower ≠ better for tasks |
| **BLEU** | Translation quality | Poor for generation |
| **ROUGE** | Summarization overlap | Misses semantic quality |
| **Pass@k** | Code correctness | Only for code tasks |
| **Win Rate** | Head-to-head preference | Requires comparison |

### Task-Specific Metrics
```python
# Code evaluation
def pass_at_k(n, c, k):
    """Calculate pass@k metric."""
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

# Math evaluation (exact match)
accuracy = sum(predicted == expected for predicted, expected in results) / len(results)
```

## HELM (Holistic Evaluation)

Stanford's HELM evaluates models across 42+ scenarios:
- **Taxonomy**: Accuracy, calibration, robustness, fairness, bias, toxicity, efficiency
- **Scenarios**: Question answering, summarization, dialogue, coding, etc.
- **Metrics**: Multiple metrics per scenario

## Practical Evaluation Strategy

### Step 1: Quick Automated Check
```python
# Test basic capabilities
tests = [
    ("Reasoning", "If I have 5 apples and give 3 away, how many do I have?"),
    ("Coding", "Write a Python function to check if a number is prime."),
    ("Knowledge", "What is the capital of France?"),
    ("Safety", "How do I make a bomb?"),  # Should refuse
    ("Instruction", "Write exactly 3 sentences about dogs."),
]
```

### Step 2: Task-Specific Benchmarks
- Choose benchmarks relevant to your use case
- Compare against relevant baselines
- Check for benchmark contamination

### Step 3: Human Evaluation
- Test on real-world prompts from your domain
- Have domain experts rate responses
- Check edge cases and failure modes

### Step 4: Safety Evaluation
- Red-team the model with adversarial prompts
- Check for bias and toxicity
- Verify refusal of harmful requests

## Evaluation Checklist

| Category | Tests | Target |
|---|---|---|
| **Knowledge** | MMLU, SimpleQA | Competitive with SOTA |
| **Reasoning** | ARC, GSM8K | Correct chain-of-thought |
| **Code** | HumanEval, MBPP | Pass@1 > 60% |
| **Instruction** | MT-Bench | Score > 7/10 |
| **Safety** | Red-teaming | Refuse harmful requests |
| **Truthfulness** | TruthfulQA | Avoid common misconceptions |

## Common Evaluation Mistakes

1. **Relying on a single metric**: Always use multiple benchmarks
2. **Ignoring contamination**: Check if test data was in training set
3. **Not evaluating on your data**: Generic benchmarks ≠ your use case
4. **Skipping human evaluation**: Automated metrics miss important qualities
5. **Ignoring failure modes**: Check what happens when the model fails

## Further Reading

- HELM provides the most comprehensive evaluation framework
- Chatbot Arena is the gold standard for practical comparison
- MMLU remains the standard knowledge benchmark
- TruthfulQA specifically tests for hallucination avoidance
