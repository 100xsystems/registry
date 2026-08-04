---
slug: pe-04-few-shot-examples
title: "Few-Shot Examples"
description: "How input-output demonstrations within the prompt guide model behavior without any weight updates — and the strategies for selecting the best examples."
order: 4
tags:
  - prompt-engineering
  - few-shot
  - in-context-learning
  - example-selection
prerequisites:
  - pe-03-roles-and-context
knowledge_refs:
  - pe-03-roles-and-context
    title: "Roles & Context"
  - pe-05-chain-of-thought
    title: "Chain-of-Thought Reasoning"
  - pe-17-domain-specific-prompts
    title: "Domain-Specific Prompting"
references:
  - title: "The Few Shot Prompting Guide — PromptHub"
    url: "https://www.prompthub.us/blog/the-few-shot-prompting-guide"
  - title: "Optimizing AI Agents with Dynamic Few-Shot Prompting"
    url: "https://medium.com/@stefansipinkoski/optimizing-ai-agents-with-dynamic-few-shot-prompting-585919f694cc"
  - title: "Few-Shot, Zero-Shot, and In-Context Learning: Business Value Explained"
    url: "https://medium.com/@amitkharche/few-shot-zero-shot-and-in-context-learning-business-value-explained-541741eb216b"
  - title: "Fairness-guided Few-shot Prompting for Large Language Models"
    url: "https://arxiv.org/abs/2303.13217"
  - title: "Adaptive Few-shot Prompting for Machine Translation"
    url: "https://arxiv.org/abs/2501.01679"
---

## Few-Shot Examples

Few-shot prompting is one of the most powerful techniques in prompt engineering. By providing a small number of input-output demonstrations within the prompt itself, you guide the model's behavior without any weight updates, training, or fine-tuning.

### Zero-Shot vs. Few-Shot

**Zero-shot prompting** gives the model only instructions and the query. It relies entirely on pre-trained knowledge. This works for simple tasks but fails on nuanced or domain-specific ones where the model doesn't know your expected format, tone, or logic.

**Few-shot prompting** includes 2–5 example pairs showing the model exactly what you want. The model learns the pattern from context and applies it to the new input. This leverages **in-context learning (ICL)** — the model's ability to learn from demonstrations without gradient updates.

The difference is dramatic. A zero-shot prompt might produce inconsistent output formats, miss edge cases, or use the wrong tone. A few-shot prompt with well-chosen examples produces structured, consistent, and predictable results.

### How Many Examples?

Research consistently shows diminishing returns beyond 5 examples:

- **0 examples (zero-shot):** Baseline. Works for straightforward tasks.
- **1–2 examples:** Significant improvement. Establishes basic format and style.
- **3–5 examples:** Optimal range for most tasks. Covers common patterns and edge cases.
- **5–8 examples:** Marginal improvement. Only worth it for highly variable tasks.
- **8+ examples:** Usually wastes tokens without accuracy gains.

The sweet spot is **3–5 examples** for most use cases. This balances token cost with performance improvement.

### Example Selection Strategies

Not all examples are equal. The quality and diversity of your examples matter more than the quantity.

**Static Selection:** Hand-picked examples that work for every prompt. Works well for narrow, consistent tasks but fails when user intent varies widely.

**Dynamic Few-Shot (Semantic Retrieval):** Store examples in a vector database. When a query arrives, use embedding similarity to retrieve the most relevant examples for that specific input. This scales better and handles diverse workloads.

**Diversity:** Include examples that cover different patterns. If classifying text, include examples of each category. If generating code, include both simple and complex cases. Include at least one **negative example** showing what you don't want.

**Recency:** Place your strongest, most critical example last. Models exhibit recency bias — they weight the final context window tokens more heavily.

### Example Format Consistency

The format of your examples directly shapes the format of the output. Inconsistency in examples leads to inconsistency in results.

**Rules:**
1. Use the same delimiters, labels, and structure across all examples
2. Separate examples clearly with consistent markers (`---`, `###`, or XML tags)
3. Match the output format of your examples to exactly what you want
4. Include both input and output in the same style as your actual use case

```
INPUT: "The product is amazing but the shipping was terrible"
OUTPUT: {"sentiment": "mixed", "positive": "product quality", "negative": "shipping"}

INPUT: "I love this app, it's so easy to use"
OUTPUT: {"sentiment": "positive", "positive": "usability", "negative": null}

INPUT: "Complete waste of money, doesn't work at all"
OUTPUT: {"sentiment": "negative", "positive": null, "negative": "functionality"}
```

This example set covers three sentiment categories, shows the exact JSON format expected, and demonstrates how to handle edge cases (mixed sentiment, null values).

### Dynamic Few-Shot with Vector Search

For production systems, static examples don't scale. Dynamic few-shot prompting uses semantic similarity to select examples at runtime:

1. **Build an example store:** Create a vector database of input-output pairs, each embedded as vectors.
2. **Embed the query:** Convert the incoming user query to a vector.
3. **Retrieve similar examples:** Use cosine similarity to find the top-K most relevant examples.
4. **Inject into prompt:** Place the retrieved examples before the actual query.

This approach handles diverse inputs while keeping the prompt focused. Tools like LangChain's `SemanticSimilarityExampleSelector` implement this pattern.

### Common Mistakes

- **Too many examples:** Token waste with diminishing returns. Stay under 5 unless necessary.
- **Inconsistent format:** If example 1 uses "Output:" and example 2 uses "Result:", the model gets confused.
- **All positive examples:** Without negative examples, the model doesn't understand boundaries.
- **Wrong order:** Your best example should be last, not first.
- **Relevance mismatch:** Dynamic few-shot with irrelevant examples is worse than static few-shot with good ones.

---

*Continue to learn about chain-of-thought reasoning — how step-by-step thinking dramatically improves model performance on complex problems.*
