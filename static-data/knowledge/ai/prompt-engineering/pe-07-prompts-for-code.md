---
slug: pe-07-prompts-for-code
title: "Prompting for Code"
description: "Techniques for generating, reviewing, refactoring, and debugging code with LLMs — from simple snippets to complex architectural decisions."
order: 7
tags:
  - prompt-engineering
  - code-generation
  - code-review
  - debugging
prerequisites:
  - pe-06-structured-outputs
knowledge_refs:
  - pe-06-structured-outputs
    title: "Structured Outputs"
  - pe-04-few-shot-examples
    title: "Few-Shot Examples"
  - pe-11-advanced-techniques
    title: "Advanced Prompting Techniques"
references:
  - title: "OpenAI — Best Practices for Code Generation"
    url: "https://platform.openai.com/docs/guides/code-generation"
  - title: "Anthropic — Claude for Code"
    url: "https://docs.anthropic.com/en/docs/build-with-claude/claude-for-code"
  - title: "Google — Gemini Code Assist Prompting Guide"
    url: "https://cloud.google.com/gemini/docs/codeassist/customization"
  - title: "Simon Willison — How I Use LLMs for Code"
    url: "https://simonwillison.net/2024/Apr/3/llm-code/"
  - title: "GitHub Copilot Prompting Guide"
    url: "https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot"
---

## Prompting for Code

LLMs have transformed how developers write, review, and debug code. But getting useful code output requires specific prompting techniques that differ from general text generation.

### Code Generation Prompts

The most effective code prompts are specific, contextual, and include constraints:

**Include the language and framework:** "Write a Python FastAPI endpoint that..." is better than "Write an API that..."

**Provide context:** Share the existing code structure, database schema, or API contract the code needs to work with.

**Specify edge cases:** "Handle empty inputs, null values, and rate limiting" produces more robust code than generic generation.

```python
# Good prompt for code generation
prompt = """
Write a Python function using FastAPI that:
- Takes a POST request at /api/analyze with a JSON body: {"text": str, "language": str}
- Validates input (text must be non-empty, language must be one of: en, es, fr)
- Returns {"word_count": int, "char_count": int, "language": str}
- Returns 422 with specific error message on validation failure
- Includes type hints and a docstring
"""
```

### Code Review Prompts

Code review prompts should be structured to catch different categories of issues:

```markdown
Review this code for:
1. Security vulnerabilities (SQL injection, XSS, auth flaws)
2. Performance bottlenecks (N+1 queries, unnecessary allocations)
3. Error handling gaps (missing try/catch, silent failures)
4. Style and readability (naming, structure, comments)
5. Testing gaps (what edge cases should be tested?)

For each finding, provide:
- Line number or section
- Severity (Critical/High/Medium/Low)
- The specific issue
- A concrete fix with code
```

### Refactoring Prompts

When refactoring, provide the before state and the desired after state:

- "Refactor this function to use async/await instead of callbacks"
- "Extract this 200-line function into smaller, testable functions"
- "Convert this class to use dependency injection"

### Debugging Prompts

The most effective debugging prompts include the error, the code, and the context:

```markdown
This code throws an error. Help me fix it:

Error: `TypeError: Cannot read property 'map' of undefined`
at line 15 of UserList.tsx

Code: [paste the component]

Context: This happens intermittently. It seems to happen when the 
API returns an empty response, but sometimes it works fine with 
empty responses.
```

### Few-Shot for Code

Code generation benefits enormously from few-shot examples. Show the model a snippet of code in your project's style, and it will match that style:

- Same naming conventions
- Same error handling patterns
- Same documentation style
- Same architectural patterns

### Common Mistakes

- **Vague requirements:** "Write a login function" gives you a toy example. Specify the auth provider, token storage, error handling, and UI behavior.
- **No context:** Generating code without showing existing code structure leads to incompatible results.
- **Asking for too much:** Break complex features into smaller, testable code generation tasks.
- **Not specifying testing:** Always ask for test cases alongside code generation.

---

*Continue to learn about prompting for image generation across DALL-E, Stable Diffusion, and Midjourney.*
