---
slug: agents-13-safety-and-control
title: "Agent Safety & Control"
description: "How to keep AI agents safe through guardrails, sandboxing, permission systems, and output validation."
order: 13
tags:
  - ai-agents
  - safety
  - guardrails
  - sandboxing
  - permission-systems
prerequisites:
  - agents-01-what-are-ai-agents
  - agents-03-tool-use
references:
  - title: "AI Agent Security Cheat Sheet"
    author: "OWASP"
    url: "https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html"
    type: "docs"
    description: "Canonical security standard for agent tool configuration, memory isolation, and validation."
  - title: "OWASP Top 10 for Agentic Applications 2026"
    author: "OWASP"
    url: "https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/"
    type: "article"
    description: "Risk taxonomy for autonomous AI systems including goal hijack and tool misuse."
  - title: "AI Agent Sandboxing & Progressive Enforcement"
    author: "ARMO"
    url: "https://www.armosec.io/blog/ai-agent-sandboxing-progressive-enforcement-guide/"
    type: "article"
    description: "Enterprise architecture guide for kernel-level behavioral sandboxing."
  - title: "AI Agent Guardrails That Actually Work"
    author: "Traversaal"
    url: "https://blog.traversaal.ai/ai-agent-guardrails-defense-in-depth-architecture-guide/"
    type: "article"
    description: "Three-layer defense-in-depth architecture for agent safety."
  - title: "AI Agent Standards Initiative"
    author: "NIST"
    url: "https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative"
    type: "docs"
    description: "U.S. government standards framework for agent identity and authorization."
related_knowledge:
  - slug: agents-03-tool-use
    title: "Tool Use"
    lesson_number: 3
  - slug: agents-14-human-in-the-loop
    title: "Human-in-the-Loop Patterns"
    lesson_number: 14
  - slug: ai-safety-01-why-ai-safety
    title: "Why AI Safety Matters"
    lesson_number: 1
knowledge_refs:
  - slug: "ai-safety-04-alignment"
    title: "Alignment"
  - slug: "ai-safety-05-robustness"
    title: "Robustness"
  - slug: "ai-safety-12-guardrails"
    title: "Guardrails"
---

# Agent Safety & Control

As AI agents gain autonomy — executing code, accessing databases, making API calls — safety and control become paramount. A single misconfigured tool or prompt injection attack can cause catastrophic damage.

## Why Prompt-Based Guardrails Fail

Relying on system prompts for security ("Never execute arbitrary shell commands") is fundamentally insecure:
- **Same-Context Vulnerability:** Security instructions and malicious payloads occupy the same context window. Indirect prompt injection (e.g., a rogue website containing "Ignore previous instructions") can override natural language guardrails.

**The Rule:** Prompt instructions are UI, not security. All robust controls must live outside the LLM context within programmatic infrastructure.

## The Three-Layer Defense Stack

### Layer 1: Input Validation (Pre-Model)
Screen incoming messages, retrieved documents, and external API payloads before the LLM processes them:
- Detect prompt injection patterns and malicious delimiters
- Filter PII and sensitive information
- Validate input format and length constraints

### Layer 2: Output Validation (Post-Model, Pre-Action)
Inspect model-generated outputs before execution:
- Validate tool call arguments against schemas
- Detect data exfiltration patterns
- Catch hallucinated parameters that would cause errors

### Layer 3: Execution-Layer Enforcement
Intercept actions at the exact moment a tool is invoked:
- **Capability Manifests:** Hardcoded allowlists of which agents can invoke which tools
- **Parameter Restrictions:** Read-only access, restricted file paths, blocked file types
- **Automatic Blocking:** Any invocation outside the allowlist is dropped regardless of LLM intent

## Sandboxing

### Container Isolation
Standard containers restrict where code runs but cannot prevent misuse of legitimate permissions.

### Behavioral Sandboxing
Controls what an agent does at the kernel level using eBPF or microVMs:
- Monitor API calls and network destinations
- Track process executions
- Enforce behavioral profiles built during observation phases

### Progressive Enforcement
1. **Discovery:** Inventory all autonomous workloads
2. **Observation:** Run in visibility-only mode to build behavioral baselines
3. **Selective Enforcement:** Promote high-confidence profiles into strict policies
4. **Full Least Privilege:** Enforce ongoing boundary constraints

## Rate Limiting and Circuit Breakers

Runaway agent loops can cause "Denial of Wallet" — massive financial costs from infinite tool-calling cycles:

- **Hard Spend Ceilings:** Enforce per-session budgets ($0.50 or 20 actions/minute)
- **Action Quotas:** Limit total tool calls per task
- **Circuit Breakers:** Automatically isolate agents when failure rates exceed thresholds
- **Timeout Enforcement:** Auto-reject on timeout, never auto-approve

## Safe Tool Execution

### Least-Privilege Principle
Agents should never have broad, open-ended access:
- Use read-only file access by default
- Restrict database queries to specific tables
- Limit API calls to required endpoints
- Block sensitive file extensions (`.env`, `.key`, `.pem`)

### Tool-Call Logging
Log every tool invocation with full arguments and results. This creates an audit trail for post-incident analysis and helps identify anomalous behavior patterns.

---

*References:*
1. OWASP, "AI Agent Security Cheat Sheet." [Link](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)
2. OWASP, "Top 10 for Agentic Applications 2026." [Link](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
3. ARMO, "AI Agent Sandboxing & Progressive Enforcement." [Link](https://www.armosec.io/blog/ai-agent-sandboxing-progressive-enforcement-guide/)
4. Traversaal, "AI Agent Guardrails That Actually Work." [Link](https://blog.traversaal.ai/ai-agent-guardrails-defense-in-depth-architecture-guide/)
5. NIST, "AI Agent Standards Initiative." [Link](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative)
