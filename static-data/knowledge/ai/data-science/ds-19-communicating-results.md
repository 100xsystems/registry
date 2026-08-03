---
{
  "title": "Communicating Results",
  "description": "Turn analysis into decisions: structure a finding, choose the right chart, and write for stakeholders.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Structure findings with the answer first",
    "Match message to audience",
    "Write plain-language takeaways from a model",
    "Present numbers with appropriate uncertainty"
  ],
  "knowledge_refs": [
    "data-science/ds-08-data-visualization",
    "data-science/ds-18-model-evaluation",
    "data-science/ds-11-hypothesis-testing"
  ],
  "prerequisites": [
    "DS-18: Model Evaluation Metrics"
  ],
  "references": [
    {
      "title": "Storytelling with Data Blog",
      "url": "https://www.storytellingwithdata.com/blog",
      "description": "Cole Nussbaumer Knaflic's principles for decluttered, decision-focused charts."
    },
    {
      "title": "The Quartz Guide to Bad Data",
      "url": "https://github.com/Quartz/bad-data-guide",
      "description": "A field guide to spotting bad data and bad data claims."
    },
    {
      "title": "The Economist — How to Use Charts",
      "url": "https://www.economist.com/graphic-detail",
      "description": "Exemplary data journalism to learn from."
    }
  ]
}
---

# DS-19-COMMUNICATING-RESULTS: Communicating Results

## Introduction

A brilliant analysis that nobody understands changes nothing. **Communication is the last mile of data science**: the skill of turning models and statistics into decisions stakeholders act on. The good news is that the craft is teachable and follows consistent rules — answer first, match the audience, declutter the chart, and state uncertainty honestly. This lesson gives you the framework used by professional data communicators like Cole Nussbaumer Knaflic [1].

## Key Concepts

### 1. The answer first

The single biggest upgrade: **lead with the conclusion, not the journey.**

- ❌ "I loaded the data, cleaned it, tried logistic regression and random forest, and then…"
- ✅ "Customers who haven't ordered in 60 days are 3× more likely to churn. Here's the evidence and what we should do."

Your stakeholder wants the decision-relevant answer in the first minute; the methodology belongs in an appendix. The "executive summary first" structure (BLUF — Bottom Line Up Front) is the professional standard.

### 2. Know your audience

- **Executives**: the decision, the confidence, the cost. One chart, three bullets.
- **Product/engineering**: the mechanism, the edge cases, the data pipeline.
- **Other analysts**: methods, metrics, assumptions — full transparency.

Same analysis, three different presentations. If you can only prepare one, prepare the executive one — that's the one that gets funded.

### 3. Charting for decisions

Every chart you present should answer one question (see the visualization lesson for the mechanics). The communication-specific rules [1]:

1. **Declutter relentlessly** — remove gridlines, borders, and legends that fight the message.
2. **Use color as a spotlight** — highlight the finding; keep the rest muted.
3. **Write the takeaway in the title** — "Churn spikes after 60 days of inactivity" beats "Orders over time."
4. **Label directly** — put text next to the data points people should notice.

If a viewer needs a caption to know what to look at, the chart failed.

### 4. Numbers with uncertainty

Data science results are estimates, and your credibility depends on saying so:

- Report confidence intervals or error bars, not just point estimates.
- Distinguish *correlation* from *causation* in your language (see the correlation lesson).
- For model metrics, say what they were measured on: "AUC 0.88 on a 20% held-out test set."

Vague confidence ("this model is great") is punished harder by stakeholders than hedged honesty ("the model is strong in 3 of 5 segments; we should test segment 4 before rollout").

### 5. The one-page template

For any significant finding, a single page that contains:

1. **The answer** (one sentence, decision-focused).
2. **The evidence** (one chart + the key numbers).
3. **The risks/limits** (what could be wrong, what wasn't tested).
4. **The ask** (what decision or next step you recommend).

If you can write that page, you can present it, email it, or turn it into slides — the discipline is the same.

## Practice Questions

1. Rewrite this lead: "We ran a t-test comparing checkout page variants. The p-value was 0.012." What's the answer-first version?
2. How does a chart for an executive differ from one for a fellow analyst?
3. Why is "AUC 0.88" an incomplete statement of model performance?
4. Draft a one-page template for: "Should we launch a loyalty program?"

## LLM Prompts for Deeper Understanding

1. "Show me before-and-after examples of decluttering a data chart."
2. "Write a stakeholder update that communicates a model's limitations honestly."
3. "What are the most common ways data science presentations mislead without lying?"

## Key Takeaways

- Lead with the answer; methodology goes in the appendix.
- Adapt every presentation to its audience — executives want decisions.
- Decluttered charts with answer-in-title are the professional standard.
- State uncertainty and limits honestly — credibility is the real product.
- One-page structure: answer, evidence, risks, ask.

## Footnotes & Attribution

1. Cole Nussbaumer Knaflic, *Storytelling with Data* — principles via the official blog. [https://www.storytellingwithdata.com/blog](https://www.storytellingwithdata.com/blog)
2. Quartz, *The Quartz Guide to Bad Data*. [https://github.com/Quartz/bad-data-guide](https://github.com/Quartz/bad-data-guide)
3. The Economist, *Graphic Detail*. Exemplary data visualization journalism. [https://www.economist.com/graphic-detail](https://www.economist.com/graphic-detail)
