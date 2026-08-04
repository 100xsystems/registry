---
slug: llm-10-function-calling
title: "Function Calling & Structured Outputs"
description: "Connecting LLMs to the real world — tool use, function calling, JSON mode, and multi-step tool chains."
order: 10
tags:
  - llm-engineering
  - function-calling
  - tool-use
  - structured-outputs
prerequisites:
  - llm-03-llm-apis
  - llm-04-prompting-systems
knowledge_refs:
  - llm-03-llm-apis
  - llm-04-prompting-systems
  - llm-11-llm-agents
references:
  - title: "OpenAI Function Calling Guide"
    url: "https://platform.openai.com/docs/guides/function-calling"
    notes: "Official function calling documentation"
  - title: "Structured Outputs with Pydantic"
    url: "https://dida.do/blog/structured-outputs-with-openai-and-pydantic"
    notes: "Pydantic integration for schema enforcement"
  - title: "OpenAI Cookbook: Function Calling"
    url: "https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb"
    notes: "Official cookbook examples"
  - title: "Anthropic Tool Use"
    url: "https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview"
    notes: "Claude's tool use documentation"
  - title: "Function Calling Comparison: GPT, Claude, Gemini"
    url: "https://ofox.ai/blog/function-calling-tool-use-complete-guide-2026/"
    notes: "Cross-provider comparison"
---

# Function Calling & Structured Outputs

Function calling lets LLMs interact with external tools — APIs, databases, code execution, and more. It's the bridge between language understanding and real-world action.

## The Function Calling Loop

```
1. Define tools (JSON Schema)
2. Send prompt + tools to LLM
3. LLM returns tool_call (if needed)
4. Execute function locally
5. Send result back to LLM
6. LLM generates final response
```

## Defining Tools

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"},
                "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        }
    }
}]
```

## Using Function Calling

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto"
)

# Check if model wants to call a function
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    
    # Execute the function
    result = get_weather(**arguments)
    
    # Send result back
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "What's the weather in Tokyo?"},
            response.choices[0].message,
            {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)}
        ],
        tools=tools
    )
```

## Parallel Function Calling

The model can call multiple functions in one turn:

```python
# User: "What's the weather in Tokyo and London?"
# Model returns two tool_calls:
[
    {"function": {"name": "get_weather", "arguments": {"location": "Tokyo"}}},
    {"function": {"name": "get_weather", "arguments": {"location": "London"}}}
]
```

Execute both concurrently, then return results together.

## Structured Outputs

### JSON Mode
Guarantees valid JSON but not schema compliance:
```python
response_format={"type": "json_object"}
```

### Structured Outputs (strict)
Constrained decoding enforces exact schema:
```python
response_format={
    "type": "json_schema",
    "json_schema": {
        "name": "weather_response",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "temperature": {"type": "number"},
                "condition": {"type": "string"}
            },
            "required": ["temperature", "condition"]
        }
    }
}
```

## Pydantic Integration

```python
from pydantic import BaseModel

class WeatherResponse(BaseModel):
    temperature: float
    condition: str
    humidity: int

# Convert to OpenAI schema
schema = WeatherResponse.model_json_schema()

response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[...],
    response_format=WeatherResponse
)
weather = response.choices[0].message.parsed  # WeatherResponse instance
```

## Error Handling

```python
try:
    result = execute_tool(tool_call)
except Exception as e:
    # Return error to model so it can retry or explain
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"Error: {str(e)}"
    })
```

## Key Takeaways

1. Function calling lets LLMs invoke external tools
2. The loop: define tools → model calls → execute → return result → model responds
3. Parallel function calling enables multi-tool queries in one turn
4. Structured outputs guarantee schema-compliant responses
5. Always handle errors gracefully and return them to the model
