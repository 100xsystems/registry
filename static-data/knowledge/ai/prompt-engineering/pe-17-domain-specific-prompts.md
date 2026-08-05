---
slug: pe-17-domain-specific-prompts
title: "Domain-Specific Prompting"
description: "Tailoring prompts for specialized fields — medical, legal, financial, educational, and technical writing applications."
order: 17
tags:
  - prompt-engineering
  - domain-specific
  - medical
  - legal
  - financial
  - education
prerequisites:
  - pe-03-roles-and-context
knowledge_refs:
  - slug: pe-03-roles-and-context
    title: "Roles & Context"
  - slug: pe-18-safety-in-prompts
    title: "Safety in Prompting"
  - slug: pe-06-structured-outputs
    title: "Structured Outputs"
references:
  - title: "Prompt Engineering in Clinical Practice: Tutorial for Clinicians"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12439060/"
  - title: "Best Practices for Healthcare AI Prompt Engineering"
    url: "https://bastiongpt.com/post/best-practices-for-healthcare-ai-prompts"
  - title: "Legal Prompt Engineering Best Practices for Lawyers"
    url: "https://www.clio.com/resources/ai-for-lawyers/legal-ai-prompt-engineering/"
  - title: "12 Prompting Techniques for Technical Writers"
    url: "https://medium.com/@k.balu124/12-prompting-techniques-for-technical-writers-292835e34810"
  - title: "Prompt Engineering in Healthcare: Best Practices & Trends"
    url: "https://healthtechmagazine.net/article/2025/04/prompt-engineering-in-healthcare-best-practices-strategies-trends-perfcon"
---
## Domain-Specific Prompting

General-purpose prompts fail in specialized domains. Medical, legal, financial, and educational applications require domain-specific vocabulary, compliance constraints, and accuracy standards that generic prompts can't achieve.

### Medical Prompting

Medical applications demand the highest accuracy standards. Errors can harm patients.

**Key principles:**
- Assign clinical roles: "You are a pediatric neurologist evaluating childhood epilepsy"
- Use structured variables: `<PatientAge>`, `<LabResults>`, `<Comorbidities>`
- Force chain-of-thought for differential diagnosis: rule out life-threatening conditions first
- Ground in evidence-based guidelines: "Per 2023 ADA guidelines..."
- Never provide definitive diagnoses — always frame as "differential considerations"

**Example:**
```
You are an endocrinologist creating a treatment plan for newly 
diagnosed Type 2 Diabetes.

Patient: <PatientAge> years old, eGFR <eGFRValue>

Requirements:
- Medication recommendations per 2023 ADA guidelines
- Blood glucose monitoring schedule
- Emergency warning signs
- Format: structured treatment plan with rationale for each decision
```

### Legal Prompting

Legal applications require precision, jurisdiction awareness, and careful framing.

**Key principles:**
- Specify jurisdiction: "Under California law..."
- Be granular: "Analyze the indemnification clause in Section 9" not "review this contract"
- Flag ambiguity: "Highlight any clauses that deviate from standard market norms"
- Never give definitive legal advice — frame as "analysis" and "considerations"
- Include citation requirements: "Cite relevant statutes where applicable"

### Financial Prompting

Financial applications need numerical accuracy, regulatory compliance, and clear formatting.

**Key principles:**
- Specify accounting standards: "Per GAAP" or "Per IFRS"
- Require structured output: tables, metrics, calculations with formulas
- Separate facts from projections: "Distinguish historical data from forecasts"
- Include risk disclosures: "Flag assumptions and sensitivity factors"

### Educational Prompting

Educational applications need pedagogical alignment and appropriate complexity.

**Key principles:**
- Specify audience level: "For 8th-grade students" or "For graduate students"
- Use instructional frameworks: "Use the 5E model (Engage, Explore, Explain, Elaborate, Evaluate)"
- Include assessment: "Include formative assessment questions for each section"
- Avoid misconceptions: "Be precise about common student misunderstandings in this topic"

### Technical Writing Prompting

Technical documentation needs clarity, consistency, and accuracy.

**Key principles:**
- Specify target audience: "For third-party developers integrating our API"
- Require specific sections: parameters, examples, error codes, status responses
- Match existing style: "Follow the format of our existing endpoint documentation"
- Include code examples: "Provide working code snippets in Python and JavaScript"

### Common Mistakes

- **Generic prompts in specialized domains:** "Summarize this medical paper" misses critical clinical nuances
- **Ignoring compliance:** Medical and legal prompts must include regulatory constraints
- **No accuracy verification:** Always add "Verify all facts against authoritative sources"
- **Missing audience specification:** A prompt for clinicians differs dramatically from one for patients

---

*Continue to learn about safety in prompting — content filtering, toxicity prevention, and responsible AI.*
