---
slug: pe-11-advanced-techniques
title: "Advanced Prompting Techniques"
description: "Self-consistency, meta-prompting, prompt chaining, skeleton-of-thought, and directional stimulus prompting — techniques that push beyond basic prompting."
order: 11
tags:
  - prompt-engineering
  - self-consistency
  - prompt-chaining
  - meta-prompting
  - skeleton-of-thought
prerequisites:
  - pe-05-chain-of-thought
knowledge_refs:
  - pe-05-chain-of-thought
    title: "Chain-of-Thought Reasoning"
  - pe-17-domain-specific-prompts
    title: "Domain-Specific Prompting"
  - pe-20-production-prompting
    title: "Prompt Engineering in Production"
references:
  - title: "PromptHub — Prompt Chaining Guide"
    url: "https://www.prompthub.us/blog/prompt-chaining-guide"
  - title: "PromptHub — Reducing Latency with Skeleton of Thought"
    url: "https://www.prompthub.us/blog/reducing-latency-with-skeleton-of-thought-prompting"
  - title: "Learn Prompting — Skeleton-of-Thought"
    url: "https://learnprompting.org/docs/advanced/decomposition/skeleton_of_thoughts"
  - title: "IBM — Prompt Engineering Techniques"
    url: "https://www.ibm.com/think/topics/prompt-engineering-techniques"
  - title: "PromptingGuide.ai — Self-Consistency"
    url: "https://www.promptingguide.ai/techniques/consistency"
---

## Advanced Prompting Techniques

Beyond zero-shot, few-shot, and chain-of-thought, there's a richer landscape of prompting strategies. These advanced techniques tackle specific challenges: reducing latency, improving reliability through ensemble methods, and decomposing complex tasks into manageable pipelines.

### Self-Consistency

Self-consistency replaces greedy decoding (taking the single highest-probability token) with a sampling-based ensemble. Instead of one reasoning path, you generate multiple paths at higher temperature and take a majority vote on the final answer.

**Why it works:** Complex problems often have multiple valid reasoning trajectories. If 5 out of 7 independent paths arrive at the same answer, that answer is far more likely to be correct than a single path's conclusion.

**Implementation:**
```python
# Generate 5 reasoning paths at temperature 0.7
paths = []
for _ in range(5):
    response = llm.generate(prompt, temperature=0.7)
    answer = extract_answer(response)
    paths.append(answer)

# Majority vote
from collections import Counter
final_answer = Counter(paths).most_common(1)[0][0]
```

Self-consistency is especially valuable for mathematical reasoning, logical puzzles, and any task where a wrong step early cascades into a wrong answer.

### Meta-Prompting

Meta-prompting uses an LLM to generate, optimize, or review prompts for another task. Instead of hand-crafting prompts, you ask the model to create them.

**Use cases:**
- "Write a system prompt for a customer support chatbot that handles billing inquiries"
- "Review this prompt and suggest improvements for clarity and completeness"
- "Generate 5 few-shot examples for this classification task"

This is particularly powerful for bootstrapping: use a strong model (GPT-4, Claude) to generate prompts that are then deployed to cheaper, faster models.

### Prompt Chaining

Prompt chaining decomposes a complex task into a pipeline of smaller, focused sub-tasks. The output of one prompt feeds into the next.

```
[Step 1: Extract key facts] → [Step 2: Classify sentiment] → [Step 3: Generate response]
```

**Benefits:**
- Each step is focused and testable independently
- Reduces hallucination (smaller context = more reliable)
- Allows different models or parameters for each step
- Easier to debug when something goes wrong

**Example pipeline for document analysis:**
1. "Extract all dates, names, and monetary values from this document"
2. "Classify each extracted entity as: PERSON, DATE, MONETARY_AMOUNT, ORGANIZATION"
3. "Generate a summary table of all extracted entities grouped by type"

### Skeleton-of-Thought (SoT)

Developed by Microsoft and Tsinghua researchers, SoT reduces inference latency by parallelizing generation:

1. **Skeleton phase:** The model quickly outputs a structured outline (3–10 bullet points)
2. **Expansion phase:** Each point is expanded independently and concurrently via parallel API calls

This achieves up to 2× speedup while maintaining comparable quality. It's ideal for long-form content, summaries, and knowledge-retrieval tasks where the overall structure is predictable.

### Directional Stimulus Prompting (DSP)

DSP guides models using subtle hints or keywords rather than explicit instructions. Instead of "Write a formal email about X," you might provide keywords like "professional," "urgent," "deadline" as directional signals.

This is useful when you want to influence tone or perspective without constraining the model's creative freedom.

### Choosing the Right Technique

| Technique | Best For | Complexity |
|---|---|---|
| Self-consistency | Math, logic, high-stakes decisions | Medium |
| Meta-prompting | Bootstrapping, prompt optimization | Low |
| Prompt chaining | Multi-step analysis, pipeline tasks | Medium |
| Skeleton-of-thought | Long-form content, latency reduction | High |
| Directional stimulus | Tone control, subtle guidance | Low |

### Common Mistakes

- **Over-chaining:** Too many steps in a pipeline accumulates errors. Keep chains to 3–5 steps maximum.
- **Self-consistency on simple tasks:** It's wasteful for straightforward questions. Reserve it for complex reasoning.
- **Ignoring cost:** Each self-consistency path is a separate API call. Budget accordingly.

---

*Continue to learn about prompt injection defense — protecting your systems from adversarial attacks.*
