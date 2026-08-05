---
slug: pe-18-safety-in-prompts
title: "Safety in Prompting"
description: "Content filtering, toxicity prevention, bias mitigation, and responsible AI — building systems that are safe by design."
order: 18
tags:
  - prompt-engineering
  - safety
  - content-filtering
  - bias-mitigation
  - responsible-ai
prerequisites:
  - pe-12-prompt-injection-defense
knowledge_refs:
  - slug: pe-12-prompt-injection-defense
    title: "Prompt Injection Defense"
  - slug: pe-10-system-prompts
    title: "System Prompts in Production"
  - slug: safety-01-why-ai-safety
    title: "AI Safety Fundamentals"
references:
  - title: "Azure AI Content Safety — Microsoft Learn"
    url: "https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview"
  - title: "OWASP Top 10 for Large Language Model Applications"
    url: "https://owasp.org/www-project-top-10-for-large-language-model-applications/"
  - title: "Constitutional AI: Harmlessness from AI Feedback — Anthropic"
    url: "https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback"
  - title: "Claude's Constitution — Anthropic"
    url: "https://www.anthropic.com/news/claudes-constitution"
  - title: "NIST AI Risk Management Framework"
    url: "https://www.nist.gov/itl/ai-risk-management-framework"
---

## Safety in Prompting

Safety isn't an add-on — it's a core requirement of production prompt engineering. Content filtering, toxicity prevention, bias mitigation, and alignment techniques ensure your AI systems are safe by design.

### Content Filtering

Modern deployments screen both inputs and outputs for harmful categories:
- Hate speech and discrimination
- Sexual content
- Violence and graphic content
- Self-harm and suicide
- Personal information (PIE, PII)

**Input filtering** catches harmful requests before they reach the model. **Output filtering** catches harmful responses before they reach users. Both are necessary.

### Toxicity Prevention

Toxicity can manifest in subtle ways beyond obvious harmful content:
- Stereotyping and generalization
- Condescending or dismissive tone
- Culturally insensitive framing
- Aggressive or hostile language patterns

**Strategies:**
- Add explicit safety constraints in system prompts: "Never generate content that promotes discrimination"
- Use guardrail models to screen outputs
- Regular red-teaming to discover failure modes
- Human review for high-risk applications

### Bias Mitigation

LLMs inherit biases from training data. Prompt engineering can mitigate some biases:

- **Explicit fairness instructions:** "Provide balanced perspectives without favoring any demographic group"
- **Diverse framing:** Ask the model to consider multiple viewpoints
- **Counter-stereotypical examples:** In few-shot examples, include diverse representation
- **Adversarial testing:** Deliberately test for biased outputs across demographics

### Responsible AI Frameworks

**NIST AI Risk Management Framework** provides four core functions:
- **Govern:** Establish policies, roles, and accountability
- **Map:** Identify and assess risks in context
- **Measure:** Quantify and track risk metrics
- **Manage:** Respond to and mitigate identified risks

**Constitutional AI (Anthropic):** Models learn safety through written principles (a "constitution") combined with self-critique and revision. This makes alignment transparent and adjustable.

### Practical Safety Patterns

```xml
<system_instructions>
You are a helpful assistant. Always follow these safety rules:
1. Never generate content that promotes violence or discrimination
2. If asked about harmful activities, explain why they're dangerous
3. Protect user privacy — never request or store personal information
4. Acknowledge uncertainty rather than guessing on sensitive topics
5. When in doubt, err on the side of caution
</system_instructions>
```

### Common Mistakes

- **Relying solely on model safety training:** Models can be jailbroken. You need application-level protections
- **Over-censoring:** Too-aggressive filtering blocks legitimate use cases
- **Ignoring cultural context:** Safety standards vary across cultures and regions
- **No human oversight:** Automated systems miss nuanced safety issues

---

*Continue to learn about optimizing prompts for cost — making them efficient without sacrificing quality.*
