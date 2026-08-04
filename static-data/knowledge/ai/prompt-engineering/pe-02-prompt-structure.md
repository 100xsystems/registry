---
slug: pe-02-prompt-structure
title: "Prompt Structure"
description: "The anatomy of an effective prompt — instruction, context, input, output format, and examples — and how to organize them for maximum clarity."
order: 2
tags:
  - prompt-engineering
  - prompt-structure
  - system-prompts
  - output-formatting
prerequisites:
  - pe-01-what-is-prompt-engineering
knowledge_refs:
  - pe-01-what-is-prompt-engineering
    title: "What Is Prompt Engineering?"
  - pe-03-roles-and-context
    title: "Roles & Context"
  - pe-06-structured-outputs
    title: "Structured Outputs"
references:
  - title: "OpenAI — Best Practices for Prompt Engineering"
    url: "https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api"
  - title: "Anthropic — Effective Context Engineering for AI Agents"
    url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - title: "The Complete Guide to Prompt Engineering Frameworks"
    url: "https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/"
  - title: "COSTAR Framework for Prompt Engineering"
    url: "https://www.prompthub.us/blog/the-costar-framework"
  - title: "DAIR.AI Prompt Engineering Guide — Techniques"
    url: "https://www.promptingguide.ai/techniques"
---

## Prompt Structure

A well-engineered prompt is not a casual question — it's a structured document with distinct semantic blocks, each serving a specific purpose. Understanding this anatomy is the foundation of reliable prompt engineering.

### The Five Components

Every effective prompt contains some combination of these five parts:

```
┌─────────────────────────────────────┐
│  1. INSTRUCTION (What to do)        │
├─────────────────────────────────────┤
│  2. CONTEXT (Background info)       │
├─────────────────────────────────────┤
│  3. INPUT DATA (What to process)    │
├─────────────────────────────────────┤
│  4. OUTPUT FORMAT (How to respond)  │
├─────────────────────────────────────┤
│  5. EXAMPLES (Demonstrations)       │
└─────────────────────────────────────┘
```

**1. Instruction:** The core directive telling the model what action to perform. "Summarize," "Extract," "Classify," "Rewrite as JSON," "Write Python code that..." — this is always present.

**2. Context:** Background information that grounds the model. This might be a document you want it to analyze, the topic you're discussing, or constraints it must follow.

**3. Input Data:** The actual text, code, or query the model needs to process. This is separated from instructions using delimiters to prevent confusion.

**4. Output Format:** Explicit instructions on how the response should be structured — JSON, bullet points, a specific template, word count limits, or language style.

**5. Examples:** Optional but powerful demonstrations showing the model exactly what you want. Even one example can dramatically improve consistency.

### System Messages vs. User Messages

Modern LLM APIs separate inputs into two distinct channels:

**System Messages** set the persistent, global behavior. They define the AI's persona, establish guardrails, specify formatting requirements, and outline operational rules. System messages remain authoritative throughout the entire conversation. They're the "constitution" of the interaction.

**User Messages** represent the immediate task. They contain the prompt template variables, external context (like retrieved documents in RAG), and conversational turns from the end user.

This separation is critical. Mixing system instructions into user messages makes them easier to override. Keeping them separate maintains consistent behavior across turns.

### Delimiters and XML Tags

LLMs parse raw text sequentially, which means if your instructions and data aren't clearly separated, the model can confuse them — or worse, become vulnerable to prompt injection.

**Standard delimiters** like triple quotes (`"""`), triple hashes (`###`), or markdown code blocks work for simple cases. They wall off input data from instructions so the model can distinguish between what to process and what to do.

**XML tags** (recommended by Anthropic) are more robust. Wrapping different prompt sections in tags like `<instructions>`, `<context>`, `<documents>`, and `<output_format>` gives the model clean semantic boundaries. LLMs understand XML parsing natively, making complex multi-section prompts much more reliable.

```xml
<instructions>
Classify the following customer support message into one of: 
BILLING, TECHNICAL, FEATURE_REQUEST, or OTHER.
</instructions>

<customer_message>
I keep getting error 403 when trying to export my report.
</customer_message>

<output_format>
Respond with a JSON object containing:
- category: one of the four categories
- confidence: a number between 0 and 1
- reasoning: a one-sentence explanation
</output_format>
```

### Prompt Engineering Frameworks

Several frameworks have emerged to systematize prompt design:

**COSTAR Framework:** Context, Objective, Style, Tone, Audience, Response format. Forces you to think through every dimension of the prompt.

**RACE Framework:** Role, Action, Context, Expectation. Simpler and faster for common tasks.

**CRISPE Framework:** Capacity/role, Insight, Statement, Personality, Experiment. More detailed, useful for complex multi-turn systems.

These frameworks aren't rigid rules — they're checklists to ensure you haven't forgotten a critical component. The best prompt engineers internalize them and adapt as needed.

### Design Principles

1. **Clarity over brevity.** A longer, clearer prompt beats a short, ambiguous one every time.
2. **Separate instructions from data.** Always use delimiters. Never assume the model can tell the difference.
3. **Be specific about output format.** Don't leave formatting to chance. Specify JSON, Markdown, exact field names, or provide a template.
4. **Put instructions first.** Lead with what you want the model to do. Context and data come after.
5. **Use positive instructions.** "Write in a professional tone" works better than "Don't be casual."

### Common Mistakes

- **Vague instructions:** "Help me with this" gives you generic help. "Analyze this SQL query for performance bottlenecks and suggest three specific optimizations" gives you useful output.
- **No output format:** Without explicit formatting, the model chooses its own — usually a wall of text.
- **Buried instructions:** If your instruction is in the middle of a long prompt, the model may miss it.
- **Ignoring system prompts:** System messages are powerful. Use them for persistent behavior rather than repeating instructions in every user message.

---

*Continue to learn about roles and context — how persona assignment shapes model behavior.*
