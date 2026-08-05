---
slug: agents-14-human-in-the-loop
title: "Human-in-the-Loop Patterns"
description: "How to integrate human oversight, approval workflows, and feedback loops into AI agent systems."
order: 14
tags:
  - ai-agents
  - human-in-the-loop
  - approval-workflows
  - feedback-loops
  - mixed-initiative
prerequisites:
  - agents-13-safety-and-control
  - agents-06-multi-agent-systems
references:
  - title: "Human-in-the-Loop for AI Agents"
    author: "LangChain"
    url: "https://python.langchain.com/docs/how_to/human_in_the_loop/"
    type: "docs"
    description: "Practical guide to implementing human approval in LangGraph agents."
  - title: "Building Effective Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    type: "article"
    description: "Covers human-in-the-loop patterns in agent architecture."
  - title: "Human-in-the-loop machine learning: a survey"
    author: "Dustin Arendt et al."
    url: "https://arxiv.org/abs/2108.05234"
    type: "paper"
    description: "Comprehensive survey of HITL paradigms and design patterns."
  - title: "Mixed-Initiative Interaction"
    author: "Eric Horvitz"
    url: "https://www.microsoft.com/en-us/research/publication/principles-of-mixed-initiative-user-interfaces/"
    type: "paper"
    description: "Foundational work on mixed-initiative interaction design."
  - title: "Letta: Stateful LLM Agents with Human-in-the-Loop"
    author: "Letta"
    url: "https://docs.letta.com/"
    type: "docs"
    description: "Framework for stateful agents with human approval checkpoints."
related_knowledge:
  - slug: agents-13-safety-and-control
    title: "Agent Safety & Control"
    lesson_number: 13
  - slug: agents-12-evaluating-agents
    title: "Evaluating Agents"
    lesson_number: 12
  - slug: agents-15-agent-observability
    title: "Agent Observability"
    lesson_number: 15
knowledge_refs:
  - slug: "safety-17-values-alignment"
    title: "Values Alignment"
  - slug: "safety-04-alignment"
    title: "Alignment"
  - slug: "llm-09-fine-tuning-practice"
    title: "Fine-Tuning"
---

# Human-in-the-Loop Patterns

Human-in-the-Loop (HITL) ensures that AI agents remain under human control for critical decisions. Rather than fully autonomous execution, HITL patterns insert human oversight at strategic points — balancing efficiency with safety and accountability.

## When HITL Is Necessary

Not every agent action requires human oversight. The key is identifying which actions are:
- **Irreversible:** Deleting data, sending emails, making payments
- **High-impact:** Changes affecting many users or systems
- **Ambiguous:** Situations where the agent's confidence is low
- **Regulatory:** Actions subject to compliance requirements

## Core HITL Patterns

### Approval Checkpoints
The agent pauses before executing a sensitive action and waits for human approval:
```
Agent: "I found a bug in the authentication module. 
        Shall I fix it by adding input validation?"
        
Human: [Approve] [Reject] [Modify]

Agent: Applies the fix only after approval.
```

### Interactive Correction
The agent presents its plan or draft output, and the human refines it before final execution:
```
Agent: "Here's my research summary. Should I:
        1. Add more detail on the performance section?
        2. Remove the technical appendix?
        3. Proceed as-is?"

Human: "Add more detail on performance, keep the appendix."
```

### Mixed-Initiative
Both agent and human can initiate actions at any time:
- Agent suggests improvements while human works
- Human can override agent decisions mid-task
- Agent can flag issues for human attention

### Feedback Loops
Humans provide feedback that the agent uses to improve:
- **Corrective feedback:** "That's wrong — use this approach instead"
- **Preferential feedback:** "I like this style, but not that one"
- **Implicit feedback:** Accepting or rejecting suggestions over time

## Implementation in LangGraph

```python
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-sonnet-4-20250514")

# Enable interrupt_before for sensitive tools
agent = create_react_agent(
    model, tools=[send_email, delete_file, run_query],
    checkpointer=MemorySaver(),
    interrupt_before=["send_email", "delete_file"]  # Pause before these tools
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
result = agent.invoke({"messages": [("human", "Send a summary to the team")]})

# Agent pauses before send_email — human reviews
# Human approves or rejects
agent.invoke(None, config)  # Continue after human decision
```

## Design Principles

### Fail-Closed by Default
When in doubt, don't execute. Timeouts should equal auto-reject, never auto-approve.

### Granular Permissions
Different actions require different levels of oversight:
- **Auto-execute:** Read-only operations, low-risk queries
- **Notify:** Non-critical actions (logging, caching)
- **Approve:** Destructive actions, external communications
- **Block:** Actions outside allowed scope

### Transparent Reasoning
When pausing for human input, the agent should clearly explain:
- What it plans to do
- Why this action requires approval
- What the risks are
- What alternatives exist

### Minimal Friction
HITL should add safety without crippling usability:
- Batch similar approvals together
- Remember human preferences for recurring decisions
- Allow delegation (approve once, apply to similar future cases)

## Scaling HITL

### Tiered Review
Route different actions to different review levels:
- **Automated checks** for routine actions
- **Junior reviewer** for moderate-risk actions
- **Senior reviewer** for high-impact actions

### Asynchronous Review
For non-urgent actions, queue decisions for human review:
- Agent continues with other work
- Human reviews at their convenience
- Agent resumes after approval

---

*References:*
1. LangChain, "Human-in-the-Loop for AI Agents." [Link](https://python.langchain.com/docs/how_to/human_in_the_loop/)
2. Anthropic Engineering, "Building Effective Agents." [Link](https://www.anthropic.com/engineering/building-effective-agents)
3. Dustin Arendt et al., "Human-in-the-loop machine learning: a survey," 2021. [Link](https://arxiv.org/abs/2108.05234)
4. Eric Horvitz, "Principles of Mixed-Initiative User Interfaces," Microsoft Research. [Link](https://www.microsoft.com/en-us/research/publication/principles-of-mixed-initiative-user-interfaces/)
5. Letta, "Stateful LLM Agents with Human-in-the-Loop." [Link](https://docs.letta.com/)
