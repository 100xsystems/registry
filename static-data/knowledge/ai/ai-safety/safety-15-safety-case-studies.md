---
slug: safety-15-safety-case-studies
title: "AI Safety Case Studies"
description: "Real-world AI failures and what we learned — autonomous vehicles, algorithmic trading, hiring bias, and predictive policing."
order: 15
tags:
  - ai-safety
  - case-studies
  - failures
  - incidents
  - lessons-learned
prerequisites:
  - safety-14-societal-impact
knowledge_refs:
  - safety-14-societal-impact
    title: "Societal Impact of AI"
  - safety-11-red-teaming
    title: "Red Teaming"
  - safety-02-bias-and-fairness
    title: "Bias & Fairness"
references:
  - title: "The Mechanisms of AI Harm — CSET"
    url: "https://cset.georgetown.edu/publication/the-mechanisms-of-ai-harm-lessons-learned-from-ai-incidents/"
  - title: "AI Safety, Ethics, and Society — Dan Hendrycks"
    url: "https://www.aisafetybook.com/textbook/organizational-risks"
  - title: "15 AI Project Failures and How to Avoid Them"
    url: "https://www.pertamapartners.com/insights/ai-project-failure-case-studies"
  - title: "AI Incident Database"
    url: "https://incidentdatabase.ai/"
  - title: "Uber Self-Driving Fatal Crash — NTSB Report"
    url: "https://www.ntsb.gov/investigations/Pages/HAR1902.aspx"
---

## AI Safety Case Studies

The best way to understand AI safety is to study what went wrong. Real-world failures teach lessons that theoretical frameworks can't.

### Case Study: Uber Self-Driving Fatal Crash (2018)

An Uber autonomous vehicle struck and killed a pedestrian in Tempe, Arizona. The AI detected the pedestrian 6 seconds before impact but repeatedly misclassified her — alternating between vehicle, bicycle, and unknown object. Emergency braking had been disabled to prevent "erratic driving." The safety driver was distracted.

**Root causes:**
- Safety-performance tradeoffs: disabling safety overrides for operational smoothness
- Automation complacency: humans can't effectively monitor monotonous tasks
- Inadequate testing: the system wasn't tested against real-world edge cases

**Lesson:** Safety shortcuts in safety-critical systems can be fatal. Physical AI deployment requires orders of magnitude more rigorous testing than software.

### Case Study: Knight Capital Trading Disaster (2012)

During a software upgrade, engineers failed to remove a dormant legacy code path. When activated, the algorithm executed 4 million erroneous trades in 45 minutes, causing a **$440 million loss** — nearly four times the company's annual earnings. Knight Capital required an emergency buyout to survive.

**Root causes:**
- Inadequate deployment procedures
- No real-time kill switch or circuit breaker
- Legacy code that wasn't properly deprecated

**Lesson:** High-speed autonomous systems require automated circuit breakers and pristine deployment hygiene.

### Case Study: Amazon Resume Screening (2018)

Amazon built an automated resume screening tool trained on a decade of hiring data. Because the tech workforce was male-dominated, the AI learned to penalize resumes containing "women's" (as in "women's chess club captain") and downgrade graduates from women-only colleges.

**Root causes:**
- Historical data bias: the algorithm optimized for patterns in past prejudice
- No fairness constraints or demographic auditing

**Lesson:** AI can't learn its way out of discriminatory patterns in training data. Proactive auditing and fairness constraints are mandatory.

### Case Study: Zillow iBuying Collapse (2021)

Zillow deployed AI to automate home-buying at scale. When the housing market experienced pandemic-era volatility, pricing models failed to adapt. Zillow bought thousands of homes at inflated prices and was forced to dump inventory at a **$569 million loss**, shutting down the division and laying off 2,000 people.

**Root causes:**
- Overconfidence in models trained on stable historical conditions
- No volatility detection or human oversight checkpoints

**Lesson:** Models trained on normal distributions fail catastrophically during tail events unless equipped with volatility triggers.

### Common Patterns Across Failures

1. **Organizational failures dominate:** Most AI failures stem from corporate pressure, ethical blindness, and missing governance — not just technical errors.
2. **Safety-performance tradeoffs:** Companies repeatedly sacrifice safety for operational metrics.
3. **Automation complacency:** Humans supervising AI systems become less vigilant over time.
4. **Missing kill switches:** Many deployed systems lacked emergency shutdown capabilities.

### Common Mistakes

- **Assuming it won't happen to us:** Every company that had an AI failure thought they had it under control.
- **Blaming the technology:** The technology worked as designed. The failure was in how it was designed, tested, and deployed.
- **No incident response plan:** Without a plan for AI failures, the response is chaos.

---

*Continue to learn about data governance — managing the data that powers AI systems.*
