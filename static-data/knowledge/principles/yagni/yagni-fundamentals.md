---
title: "YAGNI: You Ain't Gonna Need It"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define YAGNI"
  - "Recognize speculative generality"
  - "Explain the carrying cost of unused code"
  - "Apply the \"build it when needed\" discipline"
prerequisites:
  - "principles/kiss"
  - "principles/dry"
knowledge_refs:
  - "principles/yagni"
---

# YAGNI: You Ain't Gonna Need It

## The Principle

YAGNI says do not build functionality you predict you will need — build it when you actually need it. Speculative features (config knobs for imagined requirements, abstraction layers for hypothetical variants, unused parameters) cost more than they ever return.

The cost is not just the writing: every speculative feature must be reviewed, tested, documented, integrated, and maintained — forever. Most predicted features never arrive, and the ones that do arrive different from the prediction.

```python
# Speculative: parameters and paths for imagined futures
def process(data, mode='fast', use_cache=False, retry_policy=None,
            notify=None, format='json'):     # 6 knobs, 1 used
    ...

# YAGNI: build what is used today
def process(data):                            # one path
    ...
```

## YAGNI vs Preparedness

YAGNI is not "no design" — it is "no speculative construction". Interfaces that express the real current boundary are design; interfaces that pre-empt a variant that does not exist yet are speculation. The discipline: name the concrete trigger that would justify building it.

## Practice: Prune the Speculation

A feature ships with an abstraction layer, a config DSL, and three unused flags "for future flexibility".

**Task 1:** List the speculative pieces and the trigger that would justify each.

**Task 2:** Remove the pieces with no near-term trigger.

**Task 3:** Write the team rule: what evidence justifies building ahead?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why speculative code is not free. Start with maintenance cost.

**Prompt 2 — Compare & Contrast:**
> Compare YAGNI with DRY and with "rule of three". When does DRY tempt you into YAGNI violations?

**Prompt 3 — Boundary Testing:**
> An interface with one implementation is a YAGNI violation to some, sound DIP to others. Design the decision rule that resolves the debate.

## Key Takeaways

- Do not build for imagined futures
- Speculative code carries a permanent maintenance tax
- Name the concrete trigger before building ahead
- YAGNI is discipline, not laziness

## Further Reading

- [YAGNI — Martin Fowler](https://martinfowler.com/bliki/Yagni.html)
- [You Aren't Gonna Need It — Wikipedia](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)
