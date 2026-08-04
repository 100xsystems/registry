---
slug: genai-02-probabilistic-generation
title: "The Mathematics of Generation"
description: "The probabilistic foundations — from chain rule to sampling strategies that determine how AI creates text."
order: 2
tags:
  - generative-ai
  - probability
  - sampling
  - temperature
  - top-k
  - top-p
prerequisites:
  - genai-01-what-is-generative-ai
  - ml-06-gradient-descent
references:
  - title: "The Curious Case of Neural Text Degeneration (Holtzman et al.)"
    url: "https://arxiv.org/abs/1904.09751"
    description: "The nucleus sampling paper that solved text degeneration in open-ended generation"
  - title: "A Survey of Confidence Estimation and Calibration in LLMs (Geng et al.)"
    url: "https://arxiv.org/abs/2311.08298"
    description: "Comprehensive survey of probability calibration techniques for LLMs"
  - title: "Token Sampling Methods Primer"
    url: "https://aman.ai/primers/ai/token-sampling/"
    description: "Detailed technical primer covering greedy, temperature, top-k, top-p, and beam search"
  - title: "Locally Typical Sampling (Meister et al.)"
    url: "https://aclanthology.org/2023.tacl_a_00536/"
    description: "Information-theoretic alternative to traditional sampling strategies"
  - title: "Softmax Temperature Explanation (Hugging Face)"
    url: "https://huggingface.co/docs/transformers/main/en/main_classes/generation"
    description: "Hugging Face's practical guide to generation parameters and sampling"
knowledge_refs:
  - genai-01-what-is-generative-ai
  - dl-17-transformers
  - ml-07-logistic-regression
---

# The Mathematics of Generation

Every text an LLM produces is drawn from a probability distribution. Understanding this distribution — and how to sample from it — is fundamental to controlling generative AI.

## The Autoregressive Factorization

An LLM decomposes the joint probability of a sequence using the chain rule:

$$P(x_1, x_2, \ldots, x_T) = \prod_{t=1}^{T} P(x_t \mid x_1, \ldots, x_{t-1})$$

Each token depends only on the previous tokens. The model predicts a probability distribution over the entire vocabulary at each step.

**Concrete example:**
```
P("The" | <bos>) = 0.35
P("cat" | "The") = 0.12
P("sat" | "The cat") = 0.08
P("on" | "The cat sat") = 0.25
```

## From Logits to Probabilities

The model's final layer outputs **logits** (unnormalized scores) for each token in the vocabulary:

$$z_i = \text{model}(x_{<t})_i$$

Softmax converts logits to a valid probability distribution:

$$P(x_t = v_i) = \frac{e^{z_i / T}}{\sum_{j \in V} e^{z_j / T}}$$

where $T$ is the **temperature** parameter.

## Decoding Strategies

### Greedy Search
Always pick the highest-probability token:
$$x_t = \arg\max_x P(x \mid x_{<t})$$

- **Pros**: Deterministic, fast
- **Cons**: Repetitive, boring, gets stuck in loops
- **Use for**: Classification, extraction, factual QA

### Beam Search
Maintain $B$ best candidate sequences:
```
Step 1: ["The"] (0.35), ["A"] (0.28), ["It"] (0.15)...
Step 2: ["The cat"] (0.35×0.12), ["The dog"] (0.35×0.10)...
...keep top B sequences at each step
```

- **Pros**: Better quality than greedy
- **Cons**: Still repetitive for open-ended text, expensive
- **Use for**: Translation, summarization (where one "right" answer exists)

### Temperature Scaling
Controls the "creativity" of generation:

$$P_T(x_i) = \frac{e^{z_i / T}}{\sum_j e^{z_j / T}}$$

| Temperature | Effect | Output Character |
|---|---|---|
| $T \to 0$ | Sharpen distribution | Deterministic, focused |
| $T = 1$ | Original distribution | Model's natural behavior |
| $T > 1$ | Flatten distribution | Creative, random, risky |

```python
# Hugging Face
output = model.generate(input_ids, temperature=0.7, do_sample=True)

# OpenAI API
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)
```

### Top-k Sampling
Only consider the $k$ most probable tokens:
$$V^{(k)} = \text{top-}k \text{ tokens by } P(x_t \mid x_{<t})$$

Then renormalize and sample from this restricted vocabulary.

- **Problem**: Fixed $k$ is rigid — sometimes too restrictive (model confident), sometimes too loose (model uncertain)

### Top-p (Nucleus) Sampling
Dynamically select the smallest set of tokens whose cumulative probability exceeds $p$:

$$V^{(p)} = \arg\min_{V' \subseteq V} \left\{ |V'| : \sum_{x \in V'} P(x \mid x_{<t}) \geq p \right\}$$

```python
# Hugging Face
output = model.generate(input_ids, top_p=0.9, do_sample=True)

# OpenAI API
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    top_p=0.9
)
```

**Why top-p is better**: Adapts dynamically — when the model is confident, the pool shrinks; when uncertain, it expands.

### Combining Temperature and Top-p

Most practitioners use both:
- **Temperature 0.7 + Top-p 0.9**: Good default for creative writing
- **Temperature 0.0**: Best for factual tasks, code generation
- **Temperature 1.0 + Top-p 0.95**: Maximum diversity

### Min-P Sampling

A newer method that filters tokens below a probability threshold relative to the most likely token:
$$V^{(\text{min\_p})} = \{x : P(x) \geq \text{min\_p} \cdot P(x_{\text{best}})\}$$

More stable than top-p in practice.

### Repetition Penalty

Prevents loops by penalizing tokens that have already appeared:
$$z_i' = \begin{cases} z_i / \alpha & \text{if } v_i \in \text{generated tokens} \\ z_i & \text{otherwise} \end{cases}$$

where $\alpha > 1$ is the penalty factor.

## Text Degeneration

Without proper sampling, LLMs produce degenerate text:
- **Repetitive loops**: "I think that I think that I think..."
- **Unfavorable priors**: Overusing common phrases
- **Collapse**: Outputting the same token repeatedly

Holtzman et al. (2019) showed this happens because:
1. Beam search optimizes for likely sequences but misses diverse, high-quality ones
2. The model's probability distribution doesn't perfectly match human text distribution
3. Nucleus sampling fixes this by truncating the low-probability tail

## Practical Sampling Recipes

| Task | Temperature | Top-p | Repetition Penalty |
|---|---|---|---|
| Factual QA | 0.0 | 1.0 | 1.0 |
| Code generation | 0.0-0.2 | 0.95 | 1.0 |
| Creative writing | 0.7-1.0 | 0.9 | 1.1-1.2 |
| Brainstorming | 0.9-1.2 | 0.95 | 1.1 |
| Translation | 0.0 | 1.0 | 1.0 |
| Summarization | 0.3-0.5 | 0.9 | 1.0 |

## Probability Calibration

LLMs are often poorly calibrated — their confidence doesn't match their accuracy:

- **Overconfidence**: 99% probability on wrong answer
- **Underconfidence**: 51% probability on right answer

**Temperature scaling** (post-hoc): Find optimal temperature on validation set to calibrate outputs.

**Verbalized confidence**: Ask the model "On a scale of 0-100, how confident are you?" — surprisingly effective for calibration.

## Further Reading

- Holtzman et al. (2019) is essential — nucleus sampling is now the default
- The token sampling primer covers all methods mathematically
- Locally typical sampling offers an information-theoretic alternative
- For production: vLLM and TGI implement optimized sampling
