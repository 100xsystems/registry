---
slug: safety-12-guardrails
title: "Guardrails & Content Moderation"
description: "Runtime safety systems for AI — NeMo Guardrails, Llama Guard, content filtering, multi-layered safety, and output validation."
order: 12
tags:
  - ai-safety
  - guardrails
  - content-moderation
  - safety-systems
prerequisites:
  - safety-11-red-teaming
knowledge_refs:
  - slug: safety-11-red-teaming
    title: "Red Teaming"
  - slug: safety-10-safety-evaluations
    title: "Safety Evaluations"
  - slug: pe-12-prompt-injection-defense
    title: "Prompt Injection Defense"
references:
  - title: "NVIDIA NeMo Guardrails"
    url: "https://github.com/NVIDIA/NeMo-Guardrails"
  - title: "Meta — Llama Guard"
    url: "https://ai.meta.com/blog/llama-guard-llm-based-input-output-safeguard-for-language-model-apps/"
  - title: "Azure AI Content Safety"
    url: "https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview"
  - title: "Guardrails AI"
    url: "https://www.guardrailsai.com/"
  - title: "Anthropic — Core Views on AI Safety"
    url: "https://www.anthropic.com/research#702-core-views-on-ai-safety"
---
## Guardrails & Content Moderation

Guardrails are runtime safety systems that monitor, filter, and control AI inputs and outputs. They're the last line of defense between a potentially unsafe model and a real user.

### Why Guardrails Matter

Models can't be perfectly safe through training alone. Guardrails provide:
- **Defense in depth:** Even if the model is jailbroken, guardrails catch harmful outputs
- **Real-time protection:** Content filtering happens at request time, not just during training
- **Configurable safety:** Different applications need different safety thresholds
- **Auditability:** Guardrails create logs of what was blocked and why

### Types of Guardrails

**Input guardrails (pre-LLM):**
- Prompt injection detection
- Toxicity filtering
- PII detection and redaction
- Topic restriction (block certain topics entirely)

**Output guardrails (post-LLM):**
- Harmful content detection
- Hallucination detection
- Factual verification
- Format validation

**Behavioral guardrails (model-level):**
- Role adherence (does the model stay in character?)
- Tool use validation (does the model only use approved tools?)
- Escalation rules (when should the model refuse or escalate to a human?)

### Prominent Guardrail Systems

**NVIDIA NeMo Guardrails:** Programmable guardrails for LLM applications. Define rules in Colang (a domain-specific language) that control what the model can say, what topics it can discuss, and how it responds to edge cases.

**Meta Llama Guard:** A fine-tuned LLM specifically designed to classify inputs and outputs as safe or unsafe across multiple safety categories. Used as a judge to filter harmful content.

**Azure AI Content Safety:** Microsoft's multi-severity content moderation API. Screens text and images for hate, violence, self-harm, and sexual content with configurable severity levels.

**Guardrails AI:** Open-source framework for defining output validation, topic checking, and content filtering as composable modules.

### Multi-Layered Safety

No single guardrail catches everything. Production systems stack multiple layers:

```
User Input → [Input Filter] → [Prompt Injection Detector] → LLM → [Output Filter] → [Toxicity Check] → [Format Validator] → User
```

Each layer catches different failure modes. If one layer misses something, the next might catch it.

### Common Mistakes

- **Single-layer guardrails:** Relying on just the model's safety training or just an output filter.
- **Over-restrictive filtering:** Blocking legitimate use cases in the name of safety.
- **No logging:** Without tracking what guardrails block, you can't identify false positives or improve the system.
- **Ignoring adversarial bypasses:** Guardrails can be bypassed with creative prompting. Regular red-teaming of guardrails is essential.

---

*Continue to learn about auditing AI systems — formal frameworks for verifying safety and compliance.*
