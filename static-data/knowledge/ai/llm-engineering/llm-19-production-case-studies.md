---
slug: llm-19-production-case-studies
title: "LLM Production Case Studies"
description: "Real-world LLM deployments — lessons learned from building copilots, chatbots, and AI-powered products at scale."
order: 19
tags:
  - llm-engineering
  - case-studies
  - production
  - architecture
prerequisites:
  - llm-18-building-a-copilot
  - llm-13-evaluating-llm-systems
knowledge_refs:
  - llm-18-building-a-copilot
  - llm-13-evaluating-llm-systems
  - llm-16-cost-optimization
references:
  - title: "How GitHub Copilot Works"
    url: "https://github.blog/2023-05-15-how-github-copilot-is-getting-better-at-understanding-your-code/"
    notes: "Copilot's context engineering"
  - title: "Stripe Radar with LLMs"
    url: "https://stripe.com/blog/ml-fraud-detection"
    notes: "LLMs in fraud detection"
  - title: "Intercom Fin AI Agent"
    url: "https://www.intercom.com/fin"
    notes: "AI-powered customer support"
  - title: "Notion AI Architecture"
    url: "https://www.notion.so/blog/notion-ai"
    notes: "AI features in productivity tools"
  - title: "Replit Agent"
    url: "https://blog.replit.com/replit-agent"
    notes: "Full-stack AI coding agent"
---

# LLM Production Case Studies

Learning from real-world deployments reveals practical patterns and pitfalls that no tutorial covers.

## Case Study 1: GitHub Copilot

### Architecture
- **Context**: current file + open files + recently edited files
- **Model**: Codex (GPT-3 fine-tuned on code)
- **Latency target**: < 200ms for autocomplete
- **Scale**: millions of suggestions per day

### Key Decisions
1. **Small context window**: only send relevant code (cost + latency)
2. **Speculative decoding**: draft with small model, verify with large
3. **Acceptance learning**: use accepted suggestions to improve
4. **Privacy**: don't store individual code snippets

### Lessons Learned
- Context quality matters more than model size
- Users accept ~30% of suggestions
- Latency is as important as quality
- Enterprise customers need data residency

## Case Study 2: Intercom Fin (Customer Support)

### Architecture
- **RAG**: retrieve from help center articles
- **Agent**: escalate complex issues to humans
- **Guardrails**: prevent hallucinated answers

### Key Decisions
1. **Confidence threshold**: only answer when confidence > 80%
2. **Source attribution**: always show where the answer came from
3. **Human handoff**: smooth transfer to support team
4. **Continuous learning**: feedback loop from human agents

### Results
- Resolves 50%+ of conversations automatically
- 90%+ customer satisfaction
- 2 minute average resolution time

## Case Study 3: Notion AI

### Architecture
- **In-context**: current page + workspace context
- **Features**: writing, summarizing, translating, brainstorming
- **Model**: GPT-4 with custom prompting

### Key Decisions
1. **Feature flags**: gradual rollout of AI features
2. **User opt-in**: AI is optional, not default
3. **Quality over speed**: longer latency acceptable for quality
4. **Workspace-aware**: understands Notion's data model

### Lessons Learned
- Users prefer AI that understands their data
- Quality expectations are high for writing assistants
- Cost management is critical at scale

## Case Study 4: Replit Agent

### Architecture
- **Multi-file editing**: plan and execute across files
- **Sandboxed execution**: run code in containers
- **Error recovery**: iterate until code works

### Key Decisions
1. **Agent loop**: plan → code → test → fix → repeat
2. **File awareness**: full project context
3. **Interactive debugging**: ask user for clarification
4. **Progressive disclosure**: show changes incrementally

### Lessons Learned
- Full-stack agents need rich tool use
- Error recovery is essential
- Users want transparency into the agent's thinking

## Common Patterns Across Case Studies

| Pattern | Description |
|---------|-------------|
| **Context engineering** | Curate what the model sees |
| **Confidence gating** | Only act when confident |
| **Human-in-the-loop** | Escalate when uncertain |
| **Progressive rollout** | Ship gradually, monitor closely |
| **Feedback loops** | Learn from user behavior |
| **Cost awareness** | Optimize at every layer |

## Key Takeaways

1. Context quality is the universal differentiator
2. Confidence gating prevents costly mistakes
3. Human-in-the-loop builds trust and catches errors
4. Progressive rollout reduces risk
5. Feedback loops enable continuous improvement
