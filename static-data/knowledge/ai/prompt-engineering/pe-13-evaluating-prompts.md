---
slug: pe-13-evaluating-prompts
title: "Evaluating Prompts"
description: "Systematic testing and measurement of prompt quality — golden datasets, LLM-as-judge, A/B testing, and evaluation frameworks."
order: 13
tags:
  - prompt-engineering
  - evaluation
  - testing
  - llm-as-judge
  - ab-testing
prerequisites:
  - pe-12-prompt-injection-defense
knowledge_refs:
  - pe-12-prompt-injection-defense
    title: "Prompt Injection Defense"
  - pe-14-prompt-versioning
    title: "Prompt Versioning & Management"
  - pe-20-production-prompting
    title: "Prompt Engineering in Production"
references:
  - title: "Evidently AI — LLM-as-a-Judge: A Complete Guide"
    url: "https://www.evidentlyai.com/llm-guide/llm-as-a-judge"
  - title: "GrowthBook — AI Evals vs. A/B Testing"
    url: "https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai"
  - title: "Maxim AI — Prompt Evaluation Frameworks"
    url: "https://www.getmaxim.ai/articles/prompt-evaluation-frameworks-measuring-quality-consistency-and-cost-at-scale/"
  - title: "Mirascope — Prompt Evaluation: Methods, Tools, and Best Practices"
    url: "https://mirascope.com/blog/prompt-evaluation"
  - title: "Patronus AI — AI LLM Test Prompts: Best Practices"
    url: "https://www.patronus.ai/llm-testing/ai-llm-test-prompts"
---

## Evaluating Prompts

Prompt evaluation transforms prompt engineering from an intuitive "vibe check" into a rigorous engineering discipline. Because LLMs are probabilistic, small variations in instructions can drastically change behavior. You need systematic measurement.

### The Two Types of Evaluation

**Evals (offline testing)** check *competence*: Can the model perform the task accurately and safely according to instructions? This happens before deployment using test datasets.

**A/B testing (online testing)** checks *value*: Do users care? Do metrics like retention, task completion, or revenue improve? This happens after deployment with real traffic.

You need both. A prompt that's highly accurate but users hate is just as bad as one users love but gives wrong answers.

### Golden Datasets

A golden dataset is a curated set of test cases with known correct answers. It's the foundation of systematic evaluation.

**What to include:**
- Happy path cases (typical inputs)
- Edge cases (empty inputs, extreme values, ambiguous queries)
- Adversarial inputs (injection attempts, jailbreaks)
- Multi-turn conversations (context-dependent tasks)
- Real-world distribution (match actual user patterns)

**Size:** Start with 50–100 cases. Expand based on failure modes you discover.

### LLM-as-Judge

Using a powerful LLM (GPT-4, Claude) to evaluate the outputs of your target system. The judge receives the input, the output, and evaluation criteria, then scores or compares responses.

**Two paradigms:**
- **Pairwise comparison:** Present two responses side-by-side and ask which is better. More reliable for relative quality assessment.
- **Direct scoring:** Rate a single response on a scale or pass/fail. Binary pass/fail with reasoning is often more reliable than numeric scales.

**Best practices:**
- Provide explicit rubrics, not vague criteria
- Use multiple judges and aggregate for reliability
- Calibrate judges against human evaluations regularly

### Metrics

**Quality metrics:**
- Faithfulness/groundedness (adherence to source material)
- Relevance (alignment with user intent)
- Correctness (factual accuracy)
- Completeness (all aspects addressed)

**Consistency metrics:**
- Output stability across repeated runs
- Format consistency (does it always return valid JSON?)
- Behavioral consistency across prompt versions

**Cost metrics:**
- Token consumption per request
- Latency (time-to-first-token, total generation time)
- API cost per request

### Evaluation Pipeline

A mature pipeline runs in stages:

1. **Offline CI/CD:** Run prompt variations against golden datasets. Automated assertions catch regressions before deployment.
2. **Shadow mode:** Deploy prompts to process live traffic without surfacing results. Capture real-world behavior and latency.
3. **Canary rollout:** Expose new prompts to a small cohort while monitoring guardrail metrics.
4. **Full A/B test:** Evaluate downstream business impact with statistical significance.

### Common Mistakes

- **No evaluation at all:** "It works in the playground" is not production-ready.
- **Testing only happy paths:** Edge cases and adversarial inputs are where failures hide.
- **Ignoring cost:** A prompt that's 10% more accurate but 10× more expensive may not be worth it.
- **One-time evaluation:** Models change, user behavior evolves. Evaluation must be continuous.

---

*Continue to learn about prompt versioning and management — treating prompts as production software.*
