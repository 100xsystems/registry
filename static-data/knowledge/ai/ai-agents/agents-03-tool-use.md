---
slug: agents-03-tool-use
title: "Tool Use & Function Calling"
description: "How agents interact with the world — defining tools, executing function calls, error handling, and tool orchestration patterns."
order: 3
tags:
  - ai-agents
  - tool-use
  - function-calling
  - orchestration
prerequisites:
  - agents-02-agent-architecture
knowledge_refs:
  - agents-02-agent-architecture
  - agents-04-reasoning-and-planning
references:
  - title: "Tool Use with Claude"
    url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview"
    notes: "Anthropic's tool use documentation"
  - title: "OpenAI Function Calling"
    url: "https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api"
    notes: "OpenAI's function calling guide"
  - title: "AI Agent Orchestration Patterns (Azure)"
    url: "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns"
    notes: "Enterprise orchestration patterns"
  - title: "Agent Error Handling Patterns"
    url: "https://blog.jztan.com/ai-agent-error-handling-patterns/"
    notes: "Production error handling"
  - title: "Model Context Protocol (MCP)"
    url: "https://modelcontextprotocol.io/"
    notes: "Standard protocol for tool integration"
---

# Tool Use & Function Calling

Tools transform LLMs from text generators into action-taking agents. Function calling is the mechanism that lets agents interact with the real world.

## The Tool Use Lifecycle

```
1. Agent reasons → "I need to search the web"
2. Agent outputs → tool_call: {name: "web_search", args: {query: "..."}}
3. Application executes → runs web_search function
4. Application returns → tool_result: "search results..."
5. Agent continues → reasons about results, generates response
```

## Defining Tools

### OpenAI Format
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    }
}]
```

### Anthropic Format
```python
tools = [{
    "name": "get_weather",
    "description": "Get current weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
        "required": ["location"]
    }
}]
```

## Tool Design Best Practices

1. **Clear descriptions**: the model decides when to use tools based on descriptions
2. **Minimal parameters**: fewer parameters = fewer errors
3. **Type safety**: use JSON Schema for strict validation
4. **Idempotency**: safe to retry on failure
5. **Graceful errors**: return informative error messages

## Tool Orchestration Patterns

### Sequential
```
Tool A → Tool B → Tool C → Result
```
Each tool depends on the previous result.

### Parallel (Fan-Out)
```
         ┌→ Tool A ─┐
Input →  ├→ Tool B ─┤→ Merge → Result
         └→ Tool C ─┘
```
Run independent tools simultaneously.

### Maker-Checker
```
Agent proposes action → Validator reviews → Execute if approved
```
Safety check before high-risk operations.

### Retry with Fallback
```
Try Tool A → Failed → Try Tool B → Failed → Ask user
```
Graceful degradation when tools fail.

## Error Handling

```python
def execute_tool(tool_call):
    try:
        result = tool_registry[tool_call.name](**tool_call.arguments)
        return {"success": True, "data": result}
    except ValidationError as e:
        return {"success": False, "error": f"Invalid arguments: {e}"}
    except TimeoutError:
        return {"success": False, "error": "Tool timed out, try again"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {e}"}
```

## Model Context Protocol (MCP)

A standard protocol for tool integration:
- Define tools as MCP servers
- Agents discover and use tools dynamically
- Enables tool sharing across agents and platforms
- Backed by Anthropic, OpenAI, and others

## Key Takeaways

1. Tool use transforms LLMs from text generators into action-taking agents
2. The lifecycle: reason → call tool → execute → observe → continue
3. Tool descriptions are critical — the model uses them to decide when to call
4. Orchestration patterns: sequential, parallel, maker-checker, retry
5. Always handle errors gracefully and return informative messages to the agent
