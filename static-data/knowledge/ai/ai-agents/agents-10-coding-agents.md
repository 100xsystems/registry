---
{
  "title": "Coding Agents",
  "description": "Agents that read, edit and run code: repo context, patch generation and verification.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Describe the coding agent loop",
    "Provide repo context via retrieval",
    "Generate and apply patches",
    "Verify with tests and lint"
  ],
  "knowledge_refs": [
    "ai-agents/agents-10-coding-agents"
  ],
  "prerequisites": [
    "AGENTS-08: Building a Research Agent"
  ],
  "references": [
    {
      "title": "LangChain Agents",
      "url": "https://python.langchain.com/docs/how_to/#agents",
      "description": "Agent frameworks, tools and memory patterns."
    },
    {
      "title": "OpenAI Agents Documentation",
      "url": "https://platform.openai.com/docs/guides/agents",
      "description": "Function calling and agent loop patterns."
    },
    {
      "title": "ReAct: Synergizing Reasoning and Acting",
      "url": "https://arxiv.org/abs/2210.03629",
      "description": "The paper behind reasoning-acting agent loops."
    },
    {
      "title": "Anthropic — Building Effective Agents",
      "url": "https://www.anthropic.com/research/building-effective-agents",
      "description": "A practical guide to agent architecture."
    },
    {
      "title": "CrewAI Documentation",
      "url": "https://docs.crewai.com/",
      "description": "Multi-agent orchestration framework."
    }
  ]
}
---

# AGENTS-10-CODING-AGENTS: Coding Agents

## Introduction

Agents that read, edit and run code: repo context, patch generation and verification. By the end of this lesson you will be able to: Describe the coding agent loop; Provide repo context via retrieval; Generate and apply patches; Verify with tests and lint.

## Key Concepts

### 1. Describe the coding agent loop

Target: Describe the coding agent loop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import subprocess

out = subprocess.run(["git", "diff"], capture_output=True, text=True)
print("diff lines:", len(out.stdout.splitlines()))
```
### 2. Provide repo context via retrieval

Target: Provide repo context via retrieval. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("retrieve relevant files before suggesting edits")
```
### 3. Generate and apply patches

Target: Generate and apply patches. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
def apply_patch(patch: str):
    return f"applied {len(patch.splitlines())} lines"

print(apply_patch("+def foo(): pass"))
```
### 4. Verify with tests and lint

Target: Verify with tests and lint. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("verify: run tests + linter before accepting the change")
```

## Practice Questions

1. What is the key idea behind "Coding Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Coding Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with Coding Agents"
1. "Provide advanced patterns and performance considerations for Coding Agents"

## Key Takeaways

- Master the core ideas of Coding Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
