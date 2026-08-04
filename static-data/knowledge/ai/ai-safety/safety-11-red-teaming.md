---
slug: safety-11-red-teaming
title: "Red Teaming"
description: "Adversarial testing to find AI safety failures before deployment — human red teams, automated red-teaming, and systematic attack frameworks."
order: 11
tags:
  - ai-safety
  - red-teaming
  - adversarial-testing
  - security
prerequisites:
  - safety-10-safety-evaluations
knowledge_refs:
  - safety-10-safety-evaluations
    title: "Safety Evaluations"
  - safety-12-guardrails
    title: "Guardrails & Content Moderation"
  - safety-05-robustness
    title: "Robustness & Adversarial Examples"
references:
  - title: "AI Red-Teaming Design: Threat Models and Tools — CSET"
    url: "https://cset.georgetown.edu/article/ai-red-teaming-design-threat-models-and-tools/"
  - title: "Microsoft AI Red Team"
    url: "https://learn.microsoft.com/en-us/security/ai-red-team/"
  - title: "MITRE ATLAS"
    url: "https://atlas.mitre.org/"
  - title: "What Is AI Red Teaming? — Palo Alto Networks"
    url: "https://www.paloaltonetworks.com/cyberpedia/what-is-ai-red-teaming"
  - title: "NIST AI 100-2: Adversarial Machine Learning"
    url: "https://csrc.nist.gov/pubs/ai/100/2/e2025/final"
---

## Red Teaming

Red teaming is the practice of deliberately attacking an AI system to find failures before real adversaries do. It's adversarial testing with a creative, human-driven component that automated benchmarks can't replicate.

### What Makes AI Red Teaming Different

Traditional software red testing targets infrastructure — network vulnerabilities, access controls, SQL injection. AI red teaming targets **probabilistic behavior and semantic vulnerabilities**:
- Can the model be tricked into generating harmful content?
- Can prompt injection bypass safety instructions?
- Can the model be manipulated to leak training data?
- Can the model's behavior be hijacked through multi-turn conversations?

### Human vs. Automated Red Teaming

**Human red teams** bring multidisciplinary expertise — security researchers, ML engineers, sociologists, domain specialists. They think creatively, combining techniques and adapting strategies in real time. They find novel attack vectors that no one thought to test.

**Automated red-teaming** scales evaluation. Tools generate thousands of adversarial prompts, measure attack success rates, and systematically explore the attack surface. Microsoft's PyRIT (Python Risk Identification Tool) automates generative AI red-teaming with iterative attack loops.

**Hybrid approaches** combine both: automated tools generate candidate attacks, human experts evaluate and refine the most promising ones.

### Red Team Methodology

1. **Define the threat model:** What are you protecting against? Who are the adversaries? What are the potential harms?
2. **Scope the exercise:** Single model, multi-step agent workflow, API, or full application stack?
3. **Design attack categories:** Prompt injection, jailbreaks, data extraction, bias triggering, hallucination induction
4. **Execute and document:** Record every attack vector, success rate, and impact
5. **Remediate and retest:** Fix the vulnerabilities and verify the fixes work

### Key Frameworks

**MITRE ATLAS:** The standard knowledge base mapping adversary tactics and techniques against AI systems. Based on real-world threat observations.

**Garak:** Open-source tool for benchmark-style red-teaming of LLMs. Tests for known vulnerability categories.

**Inspect:** UK AISI's evaluation harness for systematic safety testing.

### Common Mistakes

- **Treating red-teaming as one-time:** Attack methods evolve. Red-teaming must be continuous.
- **Only testing happy paths:** The most dangerous failures come from adversarial inputs, not normal usage.
- **No remediation pipeline:** Finding vulnerabilities without fixing them is just documentation.

---

*Continue to learn about guardrails — the runtime safety systems that protect AI in production.*
