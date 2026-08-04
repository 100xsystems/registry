---
slug: genai-05-in-context-learning
title: "In-Context Learning"
description: "How LLMs learn from examples in the prompt without weight updates — the most surprising capability of large models."
order: 5
tags:
  - generative-ai
  - in-context-learning
  - few-shot
  - meta-learning
  - emergence
prerequisites:
  - genai-03-text-generation-basics
  - genai-02-probabilistic-generation
references:
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    url: "https://arxiv.org/abs/2005.14165"
    description: "Brown et al.'s GPT-3 paper establishing in-context learning as a paradigm"
  - title: "Rethinking the Role of Demonstrations in ICL"
    url: "https://arxiv.org/abs/2202.12837"
    description: "Min et al.'s surprising finding that labels matter more than input-label mappings"
  - title: "What Makes Good In-Context Examples for GPT-3"
    url: "https://arxiv.org/abs/2103.10360"
    description: "Liu et al.'s study on example selection strategies"
  - title: "In-Context Learning and Induction Heads (Olsson et al.)"
    url: "https://arxiv.org/abs/2209.11895"
    description: "Anthropic's mechanistic explanation of how ICL works inside transformers"
  - title: "Large Language Models are Zero-Shot Reasoners"
    url: "https://arxiv.org/abs/2205.11916"
    description: "Kojima et al.'s 'Let's think step by step' zero-shot reasoning paper"
knowledge_refs:
  - genai-03-text-generation-basics
  - genai-04-prompt-engineering
  - genai-06-llm-architecture
---

# In-Context Learning

In-context learning (ICL) is the ability of LLMs to learn new tasks from examples provided in the prompt — without any weight updates. It's arguably the most surprising and important capability to emerge from scaling language models.

## What Is In-Context Learning?

Traditional machine learning requires:
1. Collect labeled data
2. Train/update model weights
3. Deploy updated model

In-context learning requires:
1. Write examples in the prompt
2. Get correct predictions — **immediately**

```
Traditional ML:
  Data → Training → Updated Model → Predictions

In-Context Learning:
  Examples in prompt → Model → Predictions (no training!)
```

## The GPT-3 Discovery

Brown et al. (2020) discovered that GPT-3 (175B parameters) could perform tasks from just a few examples in the prompt:

**Zero-shot:**
```
Translate English to French:
cheese →
```

**One-shot:**
```
Translate English to French:
sea otter → loutre de mer
cheese →
```

**Few-shot:**
```
Translate English to French:
sea otter → loutre de mer
peppermint → menthe poivrée
plush girafe → girafe en peluche
cheese →
```

The model learns the translation pattern from the examples and applies it — **without any gradient updates**.

## Why ICL Is Surprising

1. **No weight updates**: The model's parameters don't change
2. **No gradient computation**: Just forward passes
3. **No task-specific training**: Same model, different tasks
4. **Emergent capability**: Only appears above ~1B parameters

This challenges the traditional ML paradigm where learning = weight updates.

## How ICL Works (Mechanistic Understanding)

Olsson et al. (2022) at Anthropic found that ICL works through **induction heads** — attention patterns that implement a specific algorithm:

```
Induction Head Pattern:
  Attention head looks for: [A][B]...[A] → predicts [B]

Example:
  "The cat sat on the mat. The dog sat on the"
                                          ↑
  The model has seen "sat on the" follow "cat", 
  so after "dog sat on the", it predicts "mat"
```

**Two-head circuit:**
1. **Previous token head**: Copies information about the previous token
2. **Induction head**: Matches patterns and completes them

This simple mechanism, scaled across many layers and heads, produces the sophisticated in-context learning behavior.

## Types of In-Context Learning

### Task Specification via Examples
The most common form — provide input-output pairs:
```
Classify the sentiment:

"I love this movie!" → Positive
"This is terrible." → Negative
"It was okay." → Neutral

"The special effects were amazing!" →
```

### Instruction Following
Natural language instructions instead of examples:
```
Classify the sentiment of the following review as Positive, Negative, or Neutral.
Return only the label.

Review: "The special effects were amazing!"
```

### Pattern Completion
Complete a pattern established in the prompt:
```
1 → one
2 → two
3 →
```

### Analogical Reasoning
Solve new problems by analogy:
```
Q: If a car needs 3 liters to travel 100km, how much for 350km?
A: 10.5 liters

Q: If a machine produces 5 units per hour, how many in 8 hours?
A:
```

## Factors Affecting ICL Performance

### Number of Examples
| Examples | Performance | Use Case |
|---|---|---|
| 0 (zero-shot) | Baseline | Simple, well-known tasks |
| 1-3 (one/few-shot) | Significant boost | Most practical tasks |
| 5-10 | Optimal range | Complex or ambiguous tasks |
| 10+ | Diminishing returns | Very specialized domains |

### Example Selection
Not all examples are equal:
- **Diverse examples**: Cover edge cases and different patterns
- **Representative examples**: Match the distribution of test inputs
- **Clear examples**: Unambiguous input-label mappings
- **Relevant examples**: Similar to the actual query

### Example Ordering
Order matters more than expected:
- **Put the most similar example last**: Recency bias helps
- **Mix positive and negative examples**: Balanced representation
- **Avoid clustering by class**: Randomize order

### Label Accuracy
Min et al. (2022) found a surprising result: **random labels work almost as well as correct labels** for few-shot classification. What matters more is:
- The format of the examples
- The distribution of inputs
- The task description

## In-Context Learning vs. Fine-Tuning

| Aspect | ICL | Fine-Tuning |
|---|---|---|
| Data needed | 0-20 examples | 100-1000+ examples |
| Compute | Forward pass only | Backward pass + GPU hours |
| Task switching | Change prompt | Retrain model |
| Cost | Per-query (tokens) | One-time training + inference |
| Performance | Good for simple tasks | Better for complex tasks |
| Customization | Limited | Full control |

**Rule of thumb**: Start with ICL. Fine-tune only if ICL isn't sufficient.

## Practical Tips

1. **Start with 3-5 examples**: Usually sufficient for most tasks
2. **Include edge cases**: Examples that cover unusual inputs
3. **Use the same format**: Consistent input-output structure
4. **Be explicit about output**: "Return only the label" prevents extra text
5. **Try different orderings**: Example order affects performance
6. **Combine with CoT**: Few-shot + chain-of-thought is powerful

## ICL Limitations

- **Context window**: Limited by model's max context length
- **No learning across queries**: Each prompt is independent
- **Fragile**: Small prompt changes can cause large output changes
- **No guarantees**: Model may not follow the pattern
- **Cost**: Every example costs tokens

## Further Reading

- Brown et al. (2020) established ICL as a paradigm — foundational reading
- Min et al. (2022) challenged assumptions about what makes ICL work
- Olsson et al. (2022) explained the mechanism — induction heads
- Kojima et al. (2022) showed zero-shot CoT works surprisingly well
