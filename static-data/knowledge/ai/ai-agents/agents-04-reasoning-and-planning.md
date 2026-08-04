---
slug: agents-04-reasoning-and-planning
title: "Reasoning and Planning"
description: "How AI agents think ahead, decompose tasks, and make decisions through chain-of-thought, tree-of-thought, and planning algorithms."
order: 4
tags:
  - ai-agents
  - reasoning
  - planning
  - chain-of-thought
  - tree-of-thought
  - task-decomposition
prerequisites:
  - agents-01-what-are-ai-agents
  - agents-02-agent-architecture
references:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    author: "Jason Wei et al. (Google Research)"
    url: "https://arxiv.org/abs/2201.11903"
    type: "paper"
    description: "Foundational paper introducing Chain-of-Thought prompting."
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    author: "Shunyu Yao et al. (Princeton)"
    url: "https://arxiv.org/abs/2305.10601"
    type: "paper"
    description: "Introduces Tree-of-Thoughts for multi-path reasoning."
  - title: "Understanding the Planning of LLM Agents: A Survey"
    author: "Xu Huang et al."
    url: "https://arxiv.org/abs/2402.02716"
    type: "paper"
    description: "Comprehensive survey of LLM agent planning methods."
  - title: "A Survey of Chain of Thought Reasoning: Advances, Frontiers and Future"
    author: "Zheng Chu et al. (ACL 2024)"
    url: "https://arxiv.org/abs/2309.15402"
    type: "paper"
    description: "Taxonomy and review of modern CoT paradigms."
  - title: "Large Language Models for Planning: A Comprehensive Survey"
    author: "Pengfei Cao et al."
    url: "https://arxiv.org/abs/2505.19683"
    type: "paper"
    description: "Systematic review of LLM planning methodologies."
related_knowledge:
  - slug: agents-02-agent-architecture
    title: "Agent Architecture"
    lesson_number: 2
  - slug: agents-05-memory-systems
    title: "Memory Systems"
    lesson_number: 5
  - slug: agents-17-agent-design-patterns
    title: "Agent Design Patterns"
    lesson_number: 17
knowledge_refs:
  - slug: "genai-05-in-context-learning"
    title: "In-Context Learning"
  - slug: "ml-15-reinforcement-learning-from-human-feedback"
    title: "RLHF"
  - slug: "dl-09-attention-mechanisms"
    title: "Attention Mechanisms"
---

# Reasoning and Planning

Reasoning and planning are the cognitive capabilities that transform an LLM from a text generator into an effective problem-solver. Through techniques like chain-of-thought, tree-of-thought, and task decomposition, agents can tackle complex, multi-step goals that require foresight and deliberate decision-making.

## Chain-of-Thought (CoT) Reasoning

Chain-of-Thought prompting — introduced by Jason Wei and colleagues at Google — transforms how LLMs approach complex problems by requiring intermediate reasoning steps rather than jumping straight to an answer.

### How CoT Works
Instead of: "What is 23 × 17?" → "391"

CoT produces: "23 × 17 = 23 × 10 + 23 × 7 = 230 + 161 = 391"

### CoT for Agents
In agentic systems, basic CoT extends into dynamic, multi-step execution loops. The ReAct pattern — Reasoning and Acting — alternates between:
- Reasoning about what to do next (CoT)
- Calling external tools or APIs
- Observing environment feedback

This grounded reasoning loop reduces hallucinations by anchoring the model's thinking in real-world data.

### When CoT Falls Short
CoT follows a single linear path through a problem. When the first line of reasoning hits a dead end, there's no mechanism to backtrack. This limitation motivates more advanced approaches.

## Tree-of-Thought (ToT)

Tree-of-Thoughts generalizes linear CoT by exploring **multiple reasoning paths simultaneously** in a tree structure:

### Three Key Components

1. **Thought Generation:** The model generates multiple distinct next steps (branches) rather than a single continuation. For example, given a puzzle state, it might propose three different moves.

2. **State Evaluation:** Each thought path is evaluated for progress toward the goal. This can use:
   - Self-evaluation prompts ("Rate how close this path is to a solution: 1-10")
   - Voting mechanisms across multiple evaluations
   - Heuristic scoring functions

3. **Search Algorithms:** Integrated with classic search strategies:
   - **Breadth-First Search (BFS):** Explores all paths at the current depth before moving deeper. Thorough but expensive.
   - **Depth-First Search (DFS):** Follows one path as deep as possible before backtracking. Fast but may miss better solutions.
   - **Monte Carlo Tree Search (MCTS):** Balances exploration and exploitation by sampling paths based on their estimated value.

### ToT in Practice
Tree-of-Thought enables agents to:
- Look ahead before committing to a course of action
- Backtrack from dead ends without starting over
- Make deliberate decisions when multiple valid approaches exist

## Planning Algorithms

### Task Decomposition
Breaking monolithic goals into smaller, manageable, sequentially ordered subtasks. This is perhaps the most critical planning skill for agents:

**User Goal:** "Build a REST API for a todo application"
**Decomposed Plan:**
1. Define the data model (Todo entity with fields)
2. Set up the project structure (package.json, folder layout)
3. Implement CRUD routes (GET, POST, PUT, DELETE)
4. Add input validation and error handling
5. Write tests for each endpoint
6. Create documentation

### Plan-and-Solve
A prompting strategy where the agent first generates a complete plan, then executes each step sequentially. This reduces errors by front-loading the reasoning.

### Re-planning
When an action fails or the environment changes unexpectedly, effective agents don't just retry — they revise the entire plan. This adaptive planning is what separates robust agents from fragile ones.

## Goal Setting and Subgoal Generation

Advanced agents perform autonomous goal formulation, translating vague user requests into crisp, measurable subgoals:

**Vague Request:** "Make this codebase better"
**Agent's Subgoals:**
1. Identify specific issues (unused imports, duplicate code, missing types)
2. Prioritize by impact (security > performance > readability)
3. Create a structured refactoring plan
4. Execute changes incrementally with tests at each step
5. Verify no regressions before marking complete

## Combining Reasoning with Memory

Planning doesn't happen in isolation. Effective agents combine reasoning with their memory systems:
- **Short-term memory** holds the current conversation and recent tool outputs
- **Long-term memory** provides historical context, past decisions, and learned patterns
- **Working memory** maintains the current plan and tracks which steps are complete

This integration allows agents to make informed decisions based on both current inputs and accumulated knowledge.

---

*References:*
1. Jason Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS 2022. [Link](https://arxiv.org/abs/2201.11903)
2. Shunyu Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models," NeurIPS 2023. [Link](https://arxiv.org/abs/2305.10601)
3. Xu Huang et al., "Understanding the Planning of LLM Agents: A Survey," 2024. [Link](https://arxiv.org/abs/2402.02716)
4. Zheng Chu et al., "A Survey of Chain of Thought Reasoning: Advances, Frontiers and Future," ACL 2024. [Link](https://arxiv.org/abs/2309.15402)
5. Pengfei Cao et al., "Large Language Models for Planning: A Comprehensive Survey," 2025. [Link](https://arxiv.org/abs/2505.19683)
