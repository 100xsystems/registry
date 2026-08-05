---
slug: safety-07-hallucination
title: "Hallucination & Factualness"
description: "Why AI systems generate false information and how to ground them in reality — types of hallucination, detection, and prevention strategies."
order: 7
tags:
  - ai-safety
  - hallucination
  - factualness
  - grounding
  - citations
prerequisites:
  - safety-03-interpretability
knowledge_refs:
  - slug: safety-03-interpretability
    title: "Interpretability & Explainability"
  - slug: safety-05-robustness
    title: "Robustness & Adversarial Examples"
  - slug: llm-07-rag-engineering
    title: "RAG Engineering"
references:
  - title: "A Survey on Hallucination in Large Language Models"
    url: "https://arxiv.org/abs/2311.05232"
  - title: "FActScore: Fine-grained Atomic Evaluation of Factual Precision"
    url: "https://arxiv.org/abs/2305.14251"
  - title: "TruthfulQA: Measuring How Models Mimic Human Falsehoods"
    url: "https://arxiv.org/abs/2109.07958"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    url: "https://arxiv.org/abs/2005.11401"
  - title: "SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection"
    url: "https://arxiv.org/abs/2303.01767"
---
## Hallucination & Factualness

Hallucination is when an AI system generates confident, fluent, but completely false information. It's one of the most dangerous failures in AI because the output looks indistinguishable from accurate information.

### Types of Hallucination

**Intrinsic hallucination:** The output contradicts the source material. If the source says "Event X happened in 2019" and the model says "2021," that's intrinsic.

**Extrinsic hallucination:** The output introduces information not present in the source material. The model "fills in" details that weren't in the input — plausible but false.

**Factual hallucination:** The model states something that contradicts established real-world knowledge. "The Eiffel Tower is in London" is factually hallucinated.

**Faithfulness hallucination:** The model's output isn't grounded in the provided context, even when instructed to use only that context.

### Why Hallucination Happens

**Training data memorization:** Models learn patterns from training data. They can't always distinguish between "this pattern appeared in training" and "this is true."

**Probability over certainty:** Language models generate the most likely next token, not the most accurate one. Fluent text is rewarded even when factually wrong.

**Knowledge cutoff:** Models have a training cutoff date. They don't know about events after that date and may hallucinate plausible but false information about recent events.

**Insufficient context:** When the model doesn't have enough information, it fills in gaps with plausible-sounding content rather than saying "I don't know."

### Detection Methods

**SelfCheckGPT:** Uses multiple sampling to check if the model gives consistent answers. If sampling the same question multiple times produces different facts, the model is likely hallucinating.

**FActScore:** Evaluates factual precision by breaking long-form text into atomic facts and verifying each one against a knowledge source.

**LLM-as-judge:** Use a second model to verify claims against trusted sources.

**Citation verification:** When the model provides sources, verify they actually exist and say what the model claims.

### Prevention Strategies

**Retrieval-Augmented Generation (RAG):** Ground model responses in retrieved documents. This is the most effective practical defense against hallucination.

**Instruction tuning:** Train models to say "I don't know" when uncertain rather than guessing.

**Confidence calibration:** Train models to express uncertainty appropriately rather than presenting all outputs with equal confidence.

**Structured outputs:** Force models to cite sources and provide evidence for their claims.

### Common Mistakes

- **Trusting fluent text:** Fluency is not accuracy. A well-written paragraph can be entirely false.
- **Not verifying sources:** When a model cites references, always check they exist and say what the model claims.
- **Ignoring the knowledge cutoff:** Models don't know recent events. Don't ask them about today's news.
- **No grounding:** Without RAG or external knowledge, models will hallucinate by default when they don't know something.

---

*Continue to learn about AI governance — the policies and frameworks that regulate AI deployment.*
