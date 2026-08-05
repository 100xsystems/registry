---
slug: safety-08-governance
title: "AI Governance & Policy"
description: "The regulatory landscape for AI — EU AI Act, NIST AI RMF, OECD principles, and international approaches to governing AI systems."
order: 8
tags:
  - ai-safety
  - governance
  - policy
  - eu-ai-act
  - nist
  - regulation
prerequisites:
  - safety-01-why-ai-safety
knowledge_refs:
  - slug: safety-01-why-ai-safety
    title: "Why AI Safety Matters"
  - slug: safety-14-societal-impact
    title: "Societal Impact of AI"
  - slug: safety-19-responsible-products
    title: "Building Responsible AI Products"
references:
  - title: "EU AI Act — Official Text"
    url: "https://artificialintelligenceact.eu/the-act/"
  - title: "NIST AI Risk Management Framework 1.0"
    url: "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10"
  - title: "NIST AI RMF Generative AI Profile"
    url: "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"
  - title: "OECD AI Principles"
    url: "https://www.oecd.org/en/topics/sub-issues/ai-principles.html"
  - title: "Global Partnership on Artificial Intelligence (GPAI)"
    url: "https://en.wikipedia.org/wiki/Global_Partnership_on_Artificial_Intelligence"
---
## AI Governance & Policy

As AI systems become more powerful and pervasive, governance frameworks ensure they're deployed responsibly. The regulatory landscape is evolving rapidly, with different regions taking different approaches.

### The EU AI Act

The EU AI Act is the world's first comprehensive AI law. It uses a risk-based approach:

**Unacceptable risk (banned):**
- Social scoring systems
- Cognitive behavioral manipulation of vulnerable groups
- Real-time remote biometric identification in public spaces (with narrow exceptions)

**High risk (strict requirements):**
- Healthcare AI, critical infrastructure, education, law enforcement
- Must pass conformity assessments
- Requires risk management systems, data governance, human oversight

**Limited risk (transparency obligations):**
- Chatbots must disclose they're AI
- Deepfakes must be labeled
- AI-generated content must be identified

**Minimal risk (voluntary codes):**
- Most AI applications fall here
- Encouraged to follow voluntary codes of conduct

**General-Purpose AI (GPAI):**
- Foundation models face transparency and evaluation requirements
- Models with systemic risk face additional obligations

### NIST AI Risk Management Framework

The NIST AI RMF is a voluntary US framework with four core functions:

**Govern:** Establish policies, roles, and accountability for AI risk management.

**Map:** Identify and assess risks in context — what could go wrong and who it affects.

**Measure:** Quantify and track risk metrics — accuracy, bias, robustness, privacy.

**Manage:** Respond to and mitigate identified risks — monitoring, updating, decommissioning.

The Generative AI Profile extends this framework to address hallucinations, copyright, misuse, and data leakage specific to foundation models.

### OECD AI Principles

The first intergovernmental standard on AI (adopted 2019, updated 2024):
- AI should be innovative and trustworthy
- AI should respect human rights and democratic values
- Transparency and explainability are essential
- Robustness, security, and safety are required
- Accountability is necessary for AI actors

### International Approaches

- **EU:** Prescriptive, legally binding regulation
- **US:** Voluntary frameworks, sector-specific rules
- **China:** Strict content control, mandatory algorithm registration
- **UK:** Principles-based, sector-regulated approach
- **G7 Hiroshima Process:** International coordination on AI safety

### Common Mistakes

- **Ignoring jurisdiction:** AI deployed globally must comply with multiple regulatory frameworks.
- **Treating governance as optional:** Even voluntary frameworks become de facto requirements through market pressure.
- **No documentation:** Without model cards, data sheets, and risk assessments, compliance is impossible.

---

*Continue to learn about transparency — making AI decisions visible and accountable.*
