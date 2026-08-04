---
slug: safety-09-transparency
title: "Transparency & Disclosure"
description: "Making AI decisions visible — model cards, data sheets, disclosure requirements, and content watermarking."
order: 9
tags:
  - ai-safety
  - transparency
  - disclosure
  - model-cards
  - watermarking
prerequisites:
  - safety-08-governance
knowledge_refs:
  - safety-08-governance
    title: "AI Governance & Policy"
  - safety-03-interpretability
    title: "Interpretability & Explainability"
  - safety-13-auditing-models
    title: "Auditing AI Systems"
references:
  - title: "Model Cards for Model Reporting (Mitchell et al., 2019)"
    url: "https://arxiv.org/abs/1802.08100"
  - title: "Datasheets for Datasets (Gebru et al., 2021)"
    url: "https://arxiv.org/abs/1803.09010"
  - title: "Google Model Cards"
    url: "https://modelcards.withgoogle.com/"
  - title: "EU AI Act — Transparency Requirements"
    url: "https://artificialintelligenceact.eu/the-act/"
  - title: "C2PA — Content Provenance and Authenticity"
    url: "https://c2pa.org/"
---

## Transparency & Disclosure

Transparency is the practice of making AI systems' capabilities, limitations, and decision-making processes visible to users, regulators, and affected parties. Without transparency, accountability is impossible.

### Why Transparency Matters

**User trust:** People need to know when they're interacting with AI and how the AI makes decisions.

**Accountability:** When AI causes harm, transparency enables investigation and redress.

**Regulation:** The EU AI Act requires transparency for high-risk AI systems — users must be told when AI is being used in consequential decisions.

**Market trust:** Companies deploying AI transparently face less regulatory backlash and build more user trust.

### Model Cards

Model cards (Mitchell et al., 2019) are standardized documents that describe:
- What the model does
- How it was trained
- What data it was trained on
- Where it performs well and where it fails
- Known biases and limitations

Google publishes model cards for all its AI models. They've become an industry standard for model documentation.

### Data Sheets for Datasets

Data sheets (Gebru et al., 2021) document:
- Motivation for creating the dataset
- Composition and collection process
- Preprocessing and cleaning steps
- Uses and distribution
- Maintenance and update plans

Without knowing what data a model was trained on, you can't assess its biases or limitations.

### Disclosure Requirements

The EU AI Act mandates specific disclosures:

**Chatbots:** Must disclose they're AI, not human.

**Deepfakes:** Must be labeled as AI-generated.

**High-risk AI:** Users must be informed when AI is used in decisions affecting them (hiring, lending, law enforcement).

**Emotion recognition:** Must be disclosed when used in workplaces or educational institutions.

### Content Watermarking

As AI-generated content becomes indistinguishable from human-created content, watermarking becomes essential:

**C2PA (Content Provenance and Authenticity):** Industry standard for embedding provenance metadata in images, video, and audio. Shows when content was created, by what tool, and whether it's been modified.

**Statistical watermarking:** Embedding invisible patterns in AI-generated text that can be detected by specialized tools.

**Invisible watermarks:** Embedding information in AI-generated images that survives compression, cropping, and editing.

### Transparency Pitfalls

- **Transparency theater:** Publishing documents that look comprehensive but don't actually explain anything meaningful.
- **Overwhelming detail:** Too much technical detail makes transparency useless for non-experts.
- **Ignoring limitations:** A model card that only lists strengths isn't transparent.

### Common Mistakes

- **No model documentation:** Deploying without model cards or data sheets.
- **Hidden AI use:** Using AI in consequential decisions without informing affected people.
- **Assuming transparency is enough:** Transparency without accountability is just disclosure.

---

*Continue to learn about safety evaluations — systematically testing AI systems for safety.*
