---
slug: pe-03-roles-and-context
title: "Roles & Context"
description: "How persona assignment, expertise calibration, and background context shape model behavior and output quality."
order: 3
tags:
  - prompt-engineering
  - role-prompting
  - persona
  - context-engineering
prerequisites:
  - pe-02-prompt-structure
knowledge_refs:
  - slug: pe-02-prompt-structure
    title: "Prompt Structure"
  - slug: pe-04-few-shot-examples
    title: "Few-Shot Examples"
  - slug: pe-17-domain-specific-prompts
    title: "Domain-Specific Prompting"
references:
  - title: "Learn Prompting — Role Prompting"
    url: "https://learnprompting.org/docs/advanced/zero_shot/role_prompting"
  - title: "PromptHub — Role-Prompting: Does Adding Personas Really Make a Difference?"
    url: "https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference"
  - title: "GeeksforGeeks — Role-Based Prompting"
    url: "https://www.geeksforgeeks.org/artificial-intelligence/role-based-prompting/"
  - title: "Learn Prompting — Few-Shot Prompting"
    url: "https://learnprompting.org/docs/basics/few_shot"
  - title: "IBM Think — What Is Few-Shot Prompting?"
    url: "https://www.ibm.com/think/topics/few-shot-prompting"
---
## Roles & Context

Two of the most powerful levers in prompt engineering are **role assignment** (telling the model who it is) and **context provision** (telling the model what it knows). Together, they shape the model's tone, depth, expertise, and perspective more than any other technique.

### Role Prompting

Role prompting is the technique of assigning the model a specific persona: "You are a senior tax attorney," "Act as an experienced mathematics teacher," "Pretend you are a security engineer reviewing this code."

**Why it works:** When you assign a role, you shift the model's probability distribution over vocabulary, style, and implicit knowledge. A model prompted as "a friendly tutor" uses simpler language, more analogies, and encouraging tone. The same model prompted as "a senior engineer" uses technical jargon, assumes domain knowledge, and provides concise answers.

**What research shows:** Role prompting is highly effective for:
- **Stylistic and creative tasks:** Tone, format, and delivery change dramatically based on persona
- **Domain-specific tasks:** When you specify "you are an expert in X," the model draws on more specialized training data patterns
- **Multi-perspective tasks:** Assigning different roles to multiple agents produces diverse viewpoints

However, role prompting alone doesn't improve factual accuracy or reasoning on benchmarks like MMLU. For those, you need reasoning techniques (chain-of-thought, few-shot examples) combined with role assignment.

### Setting Expertise Level

How you calibrate the model's assumed expertise level directly controls the depth of response:

- **"Explain to a high school student"** → analogies, simple vocabulary, step-by-step
- **"Explain to a software engineer"** → technical terminology, assumed knowledge, concise
- **"Explain to a domain expert"** → jargon-heavy, minimal explanation, focuses on nuances and edge cases

This isn't just about simplification — it's about matching the model's output to your audience. A data scientist reading a technical blog post needs different language than a product manager reading an executive summary.

### Context Engineering

Context is the information you provide beyond the core instruction. It grounds the model in reality and prevents hallucination.

**Types of context:**
- **Document context:** Files, code, articles, or data the model should reference
- **Situational context:** Current state, user history, or environmental constraints
- **Conversational context:** Previous messages in the conversation (for multi-turn systems)
- **Retrieved context:** Documents fetched via RAG (Retrieval-Augmented Generation)

**Best practices:**
1. **Be explicit about what context applies.** "Based on the following document, answer..." is clearer than just pasting the document.
2. **Don't overload context.** Too much irrelevant context confuses the model. Only include what's necessary.
3. **Use structured delimiters.** XML tags or clear separators prevent context from being confused with instructions.
4. **Reference specific parts.** "Focus on section 3 of the document" is better than "based on the document."

### Combining Roles and Context

The most effective prompts combine role assignment with carefully curated context:

```xml
<role>
You are a senior security engineer at a fintech startup. 
You have 10 years of experience in application security 
and specialize in OWASP Top 10 vulnerabilities.
</role>

<context>
A junior developer submitted the following code for review 
as part of a payment processing feature. The code handles 
user authentication and payment token generation.
</context>

<code>
{{code_snippet}}
</code>

<instructions>
Review this code for security vulnerabilities. Focus on:
1. Authentication flaws
2. Input validation gaps
3. Cryptographic misuse
4. OWASP Top 10 compliance

For each finding, provide:
- Severity (CRITICAL/HIGH/MEDIUM/LOW)
- The specific vulnerability
- A concrete code fix
</instructions>
```

This prompt works because the role sets the expertise level, the context provides the domain, and the instructions specify exactly what to do with both.

### Few-Shot Role Examples

When combining roles with few-shot examples, the model learns both *who it is* and *how it should behave* simultaneously. Place your most critical example last — models exhibit recency bias and weight the final context window tokens more heavily.

Keep examples diverse. Include at least one edge case or negative example showing what *not* to do. This helps the model understand boundaries as well as targets.

### Common Mistakes

- **Generic roles:** "You are an AI assistant" adds nothing. Specific roles ("You are a database performance engineer") trigger more specialized responses.
- **Mismatched expertise:** Asking a model to role-play as a "beginner" when you need expert-level analysis wastes the model's capabilities.
- **Context without instructions:** Dumping context without telling the model what to do with it produces unfocused output.
- **Too much context:** Overloading with 10,000 tokens of context when only 500 are relevant dilutes the signal.

---

*Continue to learn about few-shot examples — how demonstrations guide model behavior without any training.*
