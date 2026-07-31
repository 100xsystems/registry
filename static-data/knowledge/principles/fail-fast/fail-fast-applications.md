---
title: "Fail Fast in Production: Validation and Startup Checks"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Validate config and dependencies at startup"
  - "Design CI checks that fail fast"
  - "Use canary deploys to fail fast in production"
  - "Distinguish fast failure from flapping"
prerequisites:
  []
knowledge_refs:
  - "principles/fail-fast"
---

# Fail Fast in Production: Validation and Startup Checks

## Startup Validation

A service should refuse to start rather than run in a broken state: config schema validated, required secrets present, database reachable, feature flags defined. Start-failure is loud, recoverable, and trivially visible in the deploy pipeline.

```go
// Refuse to start on invalid config — fail fast at deploy time
type Config struct {
    DBURL      string `json:"db_url" validate:"required"`
    MaxRetries int    `json:"max_retries" validate:"gte=0,lte=5"`
}

func main() {
    cfg := loadConfig()
    if err := validate.Struct(cfg); err != nil {
        log.Fatalf("invalid config: %v", err)   // do not start broken
    }
    run(cfg)
}
```

## Failing the Pipeline

CI is the fastest place to fail: lint, typecheck, unit tests, contract tests, and a smoke deploy all fail in minutes, before users are involved. Production fail-fast is the canary: release to 1% of traffic, watch error rates for minutes, and roll back automatically on spikes.

The trap is flapping — failing on transient blips and rolling back healthy releases. Fail-fast at the pipeline level uses thresholds, minimum sample sizes, and grace periods.

## Practice: Harden the Deploy Pipeline

A misconfigured flag ships to production and only breaks the checkout at 2am, three hours after deploy.

**Task 1:** Add startup config validation so the deploy itself fails.

**Task 2:** Design the canary: traffic %, error-rate threshold, rollback trigger, and grace period.

**Task 3:** Add contract tests to CI that catch the drift before deploy.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why "the deploy must fail, not the service" is the goal of startup validation. Ask me to rank pipeline gates by speed.

**Prompt 2 — Implementation Design:**
> Design a feature-flag rollout gate: flags validate at startup, canaries validate at 1%/10%/50%, and a broken flag rolls back automatically. What thresholds and windows?

**Prompt 3 — Boundary Testing:**
> A startup check depends on a database that is legitimately down during a maintenance window. How do you fail fast without blocking maintenance?

## Key Takeaways

- Fail at deploy time, not runtime
- CI gates and canaries are production fail-fast
- Avoid flapping with thresholds and grace periods
- Startup config validation catches the cheapest bugs

## Further Reading

- [Twelve-Factor App — Fail Fast](https://12factor.net/)
- [Canary Deployment — Martin Fowler](https://martinfowler.com/bliki/CanaryRelease.html)
