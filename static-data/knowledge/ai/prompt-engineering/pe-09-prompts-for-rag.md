---
slug: pe-09-prompts-for-rag
title: "Prompting for RAG"
description: "Techniques for Retrieval-Augmented Generation — grounding LLM responses in retrieved context while maintaining faithfulness and accuracy."
order: 9
tags:
  - prompt-engineering
  - rag
  - retrieval-augmented-generation
  - grounding
  - faithfulness
prerequisites:
  - pe-06-structured-outputs
knowledge_refs:
  - pe-06-structured-outputs
    title: "Structured Outputs"
  - pe-10-system-prompts
    title: "System Prompts in Production"
  - llm-07-rag-engineering
    title: "RAG Engineering"
references:
  - title: "Anthropic — Prompt Engineering for RAG"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/retrieval-augmented-generation"
  - title: "RAGAS — Evaluation Framework for RAG"
    url: "https://docs.ragas.io/en/latest/"
  - title: "LangChain — RAG Prompt Templates"
    url: "https://python.langchain.com/docs/how_to/rag_prompt/"
  - title: "LlamaIndex — Prompt Engineering for RAG"
    url: "https://docs.llamaindex.ai/en/stable/optimizing/production_rag/"
  - title: "TruLens — RAG Evaluation Guide"
    url: "https://truLens.org/trulens/getting_started/quickstart/"
---

## Prompting for RAG

Retrieval-Augmented Generation (RAG) combines the knowledge retrieval of search engines with the reasoning of LLMs. The prompt engineering challenge is different from standard prompting: you're injecting external context and need the model to use it faithfully without hallucinating.

### The RAG Prompt Structure

A RAG prompt typically contains:

```xml
<instructions>
Answer the user's question based ONLY on the provided context. 
If the context doesn't contain enough information, say "I don't have 
enough information to answer this question."
Cite your sources using [1], [2], etc.
</instructions>

<context>
[Retrieved document chunk 1]
[Retrieved document chunk 2]
[Retrieved document chunk 3]
</context>

<question>
[User's question]
</question>
```

### Key Techniques

**Grounding instructions:** Explicitly tell the model to use only the provided context. "Answer based on the context below" or "Use ONLY the information in these documents" reduces hallucination.

**Citation prompting:** Ask the model to cite which source supports each claim. This makes it easy to verify accuracy and builds user trust.

**Handling missing information:** Instruct the model on what to do when the context is insufficient. A model that says "I don't know" is more useful than one that confidently hallucinates.

**Context ordering:** Place the most relevant chunks first and last (the "lost in the middle" problem means context in the center of long prompts gets less attention).

### Faithfulness Evaluation

For production RAG systems, you need to evaluate whether the model is actually using the context:

- **RAGAS framework:** Measures faithfulness, answer relevancy, and context precision
- **TruLens:** Provides feedback functions for grounding, relevance, and toxicity
- **LLM-as-judge:** Use a second model to verify that claims in the response are supported by the context

### Common Mistakes

- **Ignoring chunk ordering:** The model pays less attention to context in the middle of a long prompt.
- **No grounding instruction:** Without explicit instructions, the model may ignore context and use its training data.
- **Too much context:** More context isn't always better. Irrelevant chunks can confuse the model and dilute relevant signals.
- **Not handling edge cases:** What happens when retrieval returns no results? The model should degrade gracefully.

---

*Continue to learn about system prompts in production — guardrails, versioning, and monitoring.*
