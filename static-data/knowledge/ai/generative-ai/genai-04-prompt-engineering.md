---
slug: genai-04-prompt-engineering
title: "Prompt Engineering"
description: "The art and science of communicating with AI — from basic prompts to advanced techniques that unlock model capabilities."
order: 4
tags:
  - generative-ai
  - prompt-engineering
  - chain-of-thought
  - few-shot
  - system-prompts
prerequisites:
  - genai-03-text-generation-basics
  - genai-01-what-is-generative-ai
references:
  - title: "OpenAI Prompt Engineering Guide"
    url: "https://platform.openai.com/docs/guides/prompt-engineering"
    description: "Official OpenAI guide with strategies and best practices"
  - title: "Chain-of-Thought Prompting Elicits Reasoning (Wei et al.)"
    url: "https://arxiv.org/abs/2201.11903"
    description: "Wei et al.'s seminal paper on chain-of-thought reasoning"
  - title: "Anthropic Prompt Engineering Documentation"
    url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering"
    description: "Anthropic's comprehensive prompt engineering guide for Claude"
  - title: "Tree of Thoughts: Deliberate Problem Solving with LLMs"
    url: "https://arxiv.org/abs/2305.10601"
    description: "Yao et al.'s tree-of-thoughts paper for complex reasoning"
  - title: "Prompt Engineering Guide (DAIR.AI)"
    url: "https://www.promptingguide.ai/"
    description: "Community-maintained comprehensive guide to prompt engineering techniques"
knowledge_refs:
  - genai-03-text-generation-basics
  - genai-05-in-context-learning
  - genai-09-rlhf-and-alignment
---

# Prompt Engineering

Prompt engineering is the practice of designing inputs to large language models to elicit desired outputs. It's the primary interface between humans and AI — and getting it right can mean the difference between useless and transformative results.

## Why Prompt Engineering Matters

A model's output is entirely determined by its input prompt. The same model can:
- Fail completely with a vague prompt
- Produce expert-level output with a well-crafted prompt

**Example:**
```
Bad: "Write about AI"
Good: "Write a 500-word technical blog post explaining transformer architecture 
to a software engineer with 5 years of experience. Include code examples in 
PyTorch and cite 3 recent papers."
```

## Core Techniques

### Zero-Shot Prompting
Give the task directly without examples:
```
Classify the sentiment of this review as positive, negative, or neutral:
"The camera quality is amazing but the battery life is disappointing."
```

### Few-Shot Prompting
Provide examples to demonstrate the pattern:
```
Classify sentiments:

Review: "I love this product!" → Positive
Review: "Terrible experience." → Negative
Review: "It's okay, nothing special." → Neutral

Review: "The camera quality is amazing but the battery life is disappointing." →
```

**Why it works**: The model learns the pattern from examples and applies it to new inputs.

### Chain-of-Thought (CoT) Prompting
Ask the model to show its reasoning:
```
Question: If a train travels at 60 mph for 2.5 hours, how far does it go?

Let's think step by step:
1. Distance = Speed × Time
2. Speed = 60 mph
3. Time = 2.5 hours
4. Distance = 60 × 2.5 = 150 miles

Answer: 150 miles
```

**Impact**: CoT improves accuracy on math, logic, and reasoning tasks by 20-40%.

### Zero-Shot Chain-of-Thought
Simply add "Let's think step by step":
```
Question: Roger has 5 tennis balls. He buys 2 more cans of 3. How many does he have now?

Let's think step by step.
```

This surprisingly effective technique was discovered by Kojima et al. (2022).

## System Prompts

The system prompt sets the model's behavior, personality, and constraints:

```
System: You are a senior Python developer with 15 years of experience. 
You write clean, well-documented code following PEP 8. You always explain 
your reasoning and suggest best practices. Never use deprecated libraries.

User: Write a function to parse CSV files.
```

**Best practices for system prompts:**
1. **Be specific about role**: "You are a senior engineer" not "You are helpful"
2. **Define constraints**: What the model should and shouldn't do
3. **Set output format**: JSON, markdown, specific structure
4. **Include examples**: Show the desired output format
5. **Specify tone**: Professional, casual, technical

## Advanced Techniques

### Self-Consistency
Generate multiple responses and take the majority vote:
```python
responses = [generate(prompt, temperature=0.7) for _ in range(5)]
answer = majority_vote(responses)
```

### Tree of Thoughts (ToT)
Explore multiple reasoning paths:
```
Problem: Plan a 3-day trip to Tokyo

Thought 1: Day 1 - Shibuya & Harajuku
  Branch A: Morning shrine, afternoon shopping
  Branch B: Morning market, afternoon park

Thought 2: Day 2 - Asakusa & Akihabara
  Branch A: Temple morning, anime afternoon
  Branch B: River cruise, electronics shopping

Evaluate each branch and select the best combination
```

### ReAct (Reasoning + Acting)
Combine reasoning with tool use:
```
Thought: I need to find the current population of Tokyo.
Action: Search("Tokyo population 2024")
Observation: Tokyo's population is approximately 13.96 million.
Thought: Now I can answer the question.
Action: Finish("Tokyo has approximately 13.96 million people.")
```

### Meta-Prompting
Ask the model to improve your prompt:
```
I want to write a prompt that helps me debug Python code effectively. 
What information should I include in my prompt to get the best debugging help?
```

## Prompt Structure Templates

### The CRISPE Framework
- **C**apacity: Define the model's role
- **R**equest: What you want
- **I**nsight: Context and background
- **S**tatement: Specific requirements
- **P**ersonality: Tone and style
- **E**xperiment: Try multiple versions

### The RISEN Framework
- **R**ole: Who should the model be?
- **I**nstructions: What should it do?
- **S**teps: How should it proceed?
- **E**xpectation: What output format?
- **N**arrowing: Constraints and boundaries

## Common Prompting Mistakes

1. **Being too vague**: "Write something about AI" → useless output
2. **Overloading**: Asking 5 things at once → confused output
3. **No format specification**: Model outputs essay when you wanted bullet points
4. **Ignoring context**: Not providing enough background
5. **Not iterating**: First prompt rarely produces perfect results

## Prompt Engineering by Task

| Task | Key Technique | Example Addition |
|---|---|---|
| Classification | Few-shot with labels | "Classify as: positive/negative/neutral" |
| Summarization | Specify length + focus | "Summarize in 3 bullet points focusing on..." |
| Code generation | Include constraints | "Use type hints, add docstrings, follow PEP 8" |
| Analysis | Chain-of-thought | "Analyze step by step, consider pros and cons" |
| Creative writing | Set tone + constraints | "Write in a playful tone, 200 words max" |
| Data extraction | Specify format | "Return as JSON with keys: name, date, amount" |

## Evaluating Prompts

1. **Consistency**: Does it produce similar quality across runs?
2. **Robustness**: Does it work with slight input variations?
3. **Edge cases**: How does it handle unusual inputs?
4. **Safety**: Does it produce harmful content when adversarially prompted?
5. **Cost**: How many tokens does it consume?

## Further Reading

- OpenAI's guide is the definitive starting point
- Wei et al.'s CoT paper fundamentally changed prompting practice
- DAIR.AI's prompting guide covers every technique comprehensively
- For production: prompt templates + evaluation pipelines are essential
