---
slug: agents-10-coding-agents
title: "Coding Agents"
description: "How AI agents write, review, debug, and test code — from IDE assistants to fully autonomous software engineers."
order: 10
tags:
  - ai-agents
  - coding-agents
  - swe-bench
  - code-generation
  - code-review
prerequisites:
  - agents-03-tool-use
  - agents-04-reasoning-and-planning
references:
  - title: "SWE-bench: Can Language Models Resolve Real-world Github Issues?"
    author: "Carlos E. Jimenez et al."
    url: "https://www.swebench.com/original.html"
    type: "paper"
    description: "Benchmark for evaluating AI systems on real-world GitHub issues."
  - title: "Devin AI"
    author: "Cognition Labs"
    url: "https://en.wikipedia.org/wiki/Devin_AI"
    type: "article"
    description: "Overview of Cognition Labs' autonomous AI software engineer."
  - title: "Cursor (company)"
    author: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Cursor_(company)"
    type: "article"
    description: "Background on Cursor, the AI-first code editor."
  - title: "Cursor AI: Everything You Should Know"
    author: "daily.dev"
    url: "https://daily.dev/blog/cursor-ai-everything-you-should-know-about-the-new-ai-code-editor-in-one-place/"
    type: "article"
    description: "Deep-dive technical review of Cursor's features and architecture."
  - title: "UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench"
    author: "ACL Anthology"
    url: "https://aclanthology.org/2025.acl-long.189.pdf"
    type: "paper"
    description: "Peer-reviewed research on evaluation frameworks for coding agents."
related_knowledge:
  - slug: agents-03-tool-use
    title: "Tool Use"
    lesson_number: 3
  - slug: agents-08-research-agents
    title: "Building a Research Agent"
    lesson_number: 8
  - slug: agents-12-evaluating-agents
    title: "Evaluating Agents"
    lesson_number: 12
knowledge_refs:
  - slug: "languages/typescript"
    title: "TypeScript"
  - slug: "languages/python"
    title: "Python"
  - slug: "mlops-17-testing-ml-systems"
    title: "Testing ML Systems"
---

# Coding Agents

Coding agents represent a paradigm shift from simple autocomplete to autonomous software engineering partners. They can explore entire codebases, plan changes across multiple files, write code, run tests, and iterate based on failures.

## Evolution of AI Coding Tools

### Generation 1: Autocomplete
Early tools like GitHub Copilot completed lines based on context. They were helpful but limited to local, single-line suggestions.

### Generation 2: Chat Assistants
Tools like ChatGPT and Claude could explain code, suggest improvements, and generate snippets — but required manual copying and lacked repository awareness.

### Generation 3: Agentic Coding
Modern coding agents operate autonomously within repositories:
- **Explore** entire codebases via RAG and semantic search
- **Plan** changes across multiple files
- **Edit** code with full file awareness
- **Run** tests in sandboxed environments
- **Iterate** based on test failures and compiler errors

## The SWE-bench Benchmark

SWE-bench, introduced by Jimenez et al., evaluates whether AI systems can resolve real-world GitHub issues. Given an issue description and a codebase, the agent must generate a git patch that passes specific unit tests.

**Key variants:**
- **SWE-bench Lite:** 300 curated instances for faster evaluation
- **SWE-bench Verified:** Human-validated task subsets
- **SWE-bench Multimodal:** Issues requiring understanding of UI screenshots

Top-performing agents now solve 40-50% of SWE-bench Verified instances, approaching human-level performance on well-defined bug fixes.

## Major Coding Agents

### Devin (Cognition Labs)
One of the first fully autonomous AI software engineers:
- Operates in a sandboxed environment with shell, editor, and browser
- Plans, writes code, runs tests, searches documentation, and manages git workflows
- Accepts natural language prompts or Jira/Linear ticket links
- Produces pull requests autonomously

### Cursor (Anysphere)
An AI-first code editor built as a VS Code fork:
- **Composer Mode:** Multi-file edits scoped to natural language prompts
- **Agent Mode:** Background tasks for running tests, fixing failures, opening PRs
- **MCP Support:** Integrates external tools and documentation at inference time
- **BugBot:** Automated code review on pull requests

### Claude Code
Anthropic's CLI-based coding agent:
- Terminal-native workflow
- Full repository awareness via file system access
- Iterative test-driven development
- Integration with existing development workflows

## Building a Coding Agent

### Basic Coding Agent

```python
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

@tool
def read_file(path: str) -> str:
    """Read the contents of a file."""
    with open(path) as f:
        return f.read()

@tool
def write_file(path: str, content: str) -> str:
    """Write content to a file."""
    with open(path, "w") as f:
        f.write(content)
    return f"Written to {path}"

@tool
def run_command(cmd: str) -> str:
    """Run a shell command."""
    import subprocess
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr

model = ChatAnthropic(model="claude-sonnet-4-20250514")
agent = create_react_agent(model, [read_file, write_file, run_command])
```

### Test-Driven Development Loop

```python
def tde_agent(task: str):
    """Test-driven development agent."""
    # Plan
    plan = agent.invoke({"messages": [("human", f"Plan how to implement: {task}")]})

    # Implement
    agent.invoke({"messages": [("human", f"Implement the plan: {plan}")]})

    # Test
    test_result = run_command("pytest")

    # Fix until tests pass
    max_iterations = 10
    for i in range(max_iterations):
        if "passed" in test_result:
            break
        test_result = agent.invoke({
            "messages": [("human", f"Fix failing tests: {test_result}")]
        })
```

## Code Review Agents

Automated code review catches issues before human reviewers:
- **Logic flaws:** Incorrect conditions, edge cases, race conditions
- **Security vulnerabilities:** SQL injection, XSS, hardcoded secrets
- **Style regressions:** Inconsistent formatting, naming violations
- **Performance issues:** N+1 queries, unnecessary allocations

Review agents integrate with GitHub/GitLab to automatically comment on pull requests.

## Test Generation Agents

Agents that automatically generate tests:
- Unit tests for new functions
- Integration tests for API endpoints
- Edge case tests for boundary conditions
- Regression tests for reported bugs

---

*References:*
1. Carlos E. Jimenez et al., "SWE-bench: Can Language Models Resolve Real-world Github Issues?" [Link](https://www.swebench.com/original.html)
2. Cognition Labs, "Devin AI." [Link](https://en.wikipedia.org/wiki/Devin_AI)
3. Anysphere, "Cursor." [Link](https://en.wikipedia.org/wiki/Cursor_(company))
4. daily.dev, "Cursor AI: Everything You Should Know." [Link](https://daily.dev/blog/cursor-ai-everything-you-should-know-about-the-new-ai-code-editor-in-one-place/)
5. ACL Anthology, "UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench." [Link](https://aclanthology.org/2025.acl-long.189.pdf)
