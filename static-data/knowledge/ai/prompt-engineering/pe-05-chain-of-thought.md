---
slug: pe-05-chain-of-thought
title: "Chain-of-Thought Reasoning"
description: "How forcing the model to show its work — step-by-step reasoning — dramatically improves performance on complex problems."
order: 5
tags:
  - prompt-engineering
  - chain-of-thought
  - reasoning
  - self-consistency
  - tree-of-thoughts
prerequisites:
  - pe-04-few-shot-examples
knowledge_refs:
  - slug: pe-04-few-shot-examples
    title: "Few-Shot Examples"
  - slug: pe-11-advanced-techniques
    title: "Advanced Prompting Techniques"
  - slug: ml-18-classification-metrics
    title: "Model Evaluation"
references:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., 2022)"
    url: "https://arxiv.org/abs/2201.11903"
  - title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., 2022)"
    url: "https://arxiv.org/abs/2203.11171"
  - title: "Large Language Models are Zero-Shot Reasoners (Kojima et al., 2022)"
    url: "https://arxiv.org/abs/2205.11916"
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Yao et al., 2023)"
    url: "https://arxiv.org/abs/2305.10601"
  - title: "Graph of Thoughts: Solving Elaborate Problems with Large Language Models (Besta et al., 2023)"
    url: "https://arxiv.org/abs/2308.09687"
---

## Chain-of-Thought Reasoning

Chain-of-thought (CoT) prompting is one of the most impactful techniques in prompt engineering. By asking the model to show its reasoning step by step before giving a final answer, you dramatically improve accuracy on complex problems — arithmetic, logic, multi-step analysis, and commonsense reasoning.

### The Core Idea

Standard prompting maps input directly to output: question → answer. CoT adds intermediate reasoning steps: question → reasoning → reasoning → answer.

```
Standard:  "What is 23 × 17?" → "391"

CoT:       "What is 23 × 17?"
           → "Let me break this down:
              23 × 17 = 23 × (10 + 7)
              = 23 × 10 + 23 × 7
              = 230 + 161
              = 391"
```

The intermediate steps force the model to decompose the problem, apply logic incrementally, and catch errors before they compound into wrong answers.

### Why It Works

LLMs generate tokens sequentially. When they jump directly to an answer, they make a single prediction that must encode the entire solution. CoT breaks this into smaller, manageable steps where each step constrains the next.

This works because:
1. **Decomposition:** Complex problems are broken into simpler sub-problems
2. **Explicit reasoning:** The model can verify each step against known facts
3. **Error containment:** A mistake in step 2 doesn't necessarily corrupt step 5
4. **Faithful explanations:** The reasoning chain provides interpretable justification

### Three Flavors of CoT

**Few-Shot CoT:** Include examples with reasoning chains in your prompt. The model learns the pattern and generates similar reasoning for new problems.

```python
# Few-shot CoT example
prompt = """
Q: A jar has 5 marbles. If you add 3 more jars, 
   and each jar has 4 marbles, how many total?
A: Let's think step by step.
   - Start: 1 jar × 5 marbles = 5 marbles
   - Add 3 jars: 3 × 4 marbles = 12 marbles  
   - Total: 5 + 12 = 17 marbles
   Answer: 17

Q: A store has 8 boxes of pens with 12 each.
   If they sell 40 pens, how many remain?
A: Let's think step by step.
"""
```

**Zero-Shot CoT:** Simply append "Let's think step by step" to your prompt. No examples needed. Kojima et al. (2022) showed this single phrase unlocks reasoning capabilities in large models without any demonstrations.

**Self-Consistency CoT:** Generate multiple reasoning paths (using temperature > 0) and take a majority vote on the final answer. Wang et al. (2022) showed this dramatically improves robustness because complex problems often have multiple valid reasoning trajectories.

### Tree-of-Thoughts (ToT)

Yao et al. (2023) generalized CoT into a tree structure where the model can:
- **Generate multiple thoughts** at each step
- **Evaluate** each thought using self-assessment
- **Search** using BFS or DFS, with backtracking when a path is wrong

This is more powerful than linear CoT for problems requiring exploration, planning, or creative problem-solving. The model can "look ahead," evaluate promising paths, and abandon dead ends.

### When to Use CoT

CoT excels at:
- **Arithmetic and math problems** (GSM8K benchmark improvements from ~18% to ~58%)
- **Logic and commonsense reasoning**
- **Multi-step analysis** (code debugging, document analysis)
- **Decision-making with constraints**
- **Tasks requiring justification**

CoT is unnecessary for:
- Simple classification tasks
- Text generation where format matters more than reasoning
- Tasks where the answer is obvious from the input

### Implementation Tips

1. **Be specific about reasoning style.** "Think step by step" is generic. "Analyze each condition separately, then combine your findings" is more targeted.
2. **Combine with few-shot.** Provide one or two examples showing the reasoning chain you want.
3. **Use self-consistency for critical decisions.** Generate 3–5 reasoning paths and vote. This is especially valuable for high-stakes applications.
4. **Set temperature appropriately.** For self-consistency, use temperature 0.7–1.0 to get diverse reasoning paths. For single-path CoT, use temperature 0–0.3 for consistency.
5. **Parse the reasoning chain.** In production, extract the final answer from the reasoning chain programmatically using regex or structured output formatting.

### Common Mistakes

- **Asking for CoT on simple tasks:** It wastes tokens and can introduce errors on easy questions.
- **No structure to reasoning:** Without guidance, the model's reasoning can be rambling and unfocused.
- **Ignoring wrong reasoning:** A correct final answer with flawed reasoning is unreliable. Check the chain.
- **Too many reasoning steps:** For very complex problems, break the task into sub-prompts rather than asking for 20+ reasoning steps in one prompt.

---

*Continue to learn about structured outputs — how to get JSON, tables, and formatted responses from any model.*
