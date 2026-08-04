---
slug: genai-12-agents-and-tool-use
title: "Agents & Tool Use"
description: "Building autonomous AI systems that can reason, plan, and use external tools to accomplish complex tasks."
order: 12
tags:
  - generative-ai
  - agents
  - tool-use
  - function-calling
  - react
  - langchain
prerequisites:
  - genai-10-rag
  - genai-04-prompt-engineering
  - genai-03-text-generation-basics
references:
  - title: "ReAct: Synergizing Reasoning and Acting (Yao et al.)"
    url: "https://arxiv.org/abs/2210.03629"
    description: "The foundational ReAct paper establishing reasoning-action loops"
  - title: "Tool Calling with LangChain"
    url: "https://www.langchain.com/blog/tool-calling-with-langchain"
    description: "LangChain's standardized tool-calling interface documentation"
  - title: "Building AI Agents with LangChain (Beginner's Guide)"
    url: "https://medium.com/@aryavr2030/building-ai-agents-with-langchain-a-beginners-guide-for-2026-bd5efe29eecb"
    description: "Modern LangChain agent architecture with LangGraph"
  - title: "Function Calling Documentation (OpenAI)"
    url: "https://platform.openai.com/docs/guides/function-calling"
    description: "OpenAI's official function calling guide"
  - title: "Tool Use Documentation (Anthropic)"
    url: "https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview"
    description: "Anthropic's tool use documentation for Claude"
knowledge_refs:
  - genai-10-rag
  - genai-04-prompt-engineering
  - genai-09-rlhf-and-alignment
---

# Agents & Tool Use

LLM agents combine language models with external tools — search engines, calculators, code interpreters, APIs — to accomplish complex tasks that require more than just text generation.

## What Is an Agent?

An agent is an LLM-based system that operates in a **reasoning-action-observation loop**:

```
User Goal → Agent (LLM)
    ├── Thought: "I need to search for X"
    ├── Action: search("X")
    ├── Observation: [search results]
    ├── Thought: "Now I need to calculate Y"
    ├── Action: calculator(Y)
    ├── Observation: [calculation result]
    └── Final Answer: [response to user]
```

**Key difference from chatbots**: Agents take **actions** in the world, not just generate text.

## Function Calling (Tool Use)

Modern LLMs can output structured function calls:

### OpenAI Function Calling
```python
import openai

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["city"]
            }
        }
    }
]

response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto"
)

# Model outputs a tool call
tool_call = response.choices[0].message.tool_calls[0]
print(tool_call.function.name)      # "get_weather"
print(tool_call.function.arguments)  # '{"city": "Tokyo", "units": "celsius"}'
```

### Anthropic Tool Use
```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=[{
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }]
)
```

## The ReAct Framework

ReAct (Yao et al., 2022) alternates between reasoning traces and actions:

```
Question: What is the elevation range for the area that the eastern 
sector of the Colorado orogeny extends into?

Thought 1: I need to search for the eastern sector of the Colorado orogeny.
Action 1: Search[eastern sector Colorado orogeny]
Observation 1: The eastern sector extends into the High Plains.

Thought 2: Now I need to find the elevation range of the High Plains.
Action 2: Search[High Plains elevation range]
Observation 2: The High Plains rise in elevation from around 1,800 ft 
to 7,000 ft.

Thought 3: The elevation range is 1,800 ft to 7,000 ft.
Action 3: Finish[1,800 ft to 7,000 ft]
```

## Agent Architectures

### ReAct Agent (Text-based)
Uses natural language for reasoning and tool selection:
- Pros: Transparent, debuggable, works with any model
- Cons: Token-heavy, parsing errors possible

### Function Calling Agent (Structured)
Uses native API function calling:
- Pros: Fast, reliable, token-efficient
- Cons: Requires model support, less transparent

### Plan-and-Execute Agent
Plans all steps first, then executes:
```
Plan:
1. Search for latest research on X
2. Summarize the findings
3. Create a report with citations

Execute: [follow the plan step by step]
```

### Multi-Agent Systems
Multiple specialized agents collaborate:
```
Research Agent → finds information
Analysis Agent → processes findings
Writer Agent → creates report
Review Agent → quality checks
```

## LangChain Agents

```python
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

# Define tools
@tool
def search(query: str) -> str:
    """Search the web for current information."""
    return web_search(query)

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    return str(eval(expression))

# Create agent
llm = ChatOpenAI(model="gpt-4")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when needed."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, [search, calculator], prompt)
executor = AgentExecutor(agent=agent, tools=[search, calculator], verbose=True)

result = executor.invoke({"input": "What's the population of France times 3.14?"})
```

## Common Agent Tools

| Tool | Purpose | Example |
|---|---|---|
| Web Search | Find current information | Google, Bing, Tavily |
| Calculator | Mathematical computation | Wolfram Alpha, eval |
| Code Interpreter | Execute code | Python REPL, Jupyter |
| Database Query | Access structured data | SQL, GraphQL |
| File System | Read/write files | Local filesystem |
| APIs | External services | Weather, news, finance |
| Memory | Long-term storage | Vector store, knowledge graph |

## Agent Patterns

### Tool Routing
Agent decides which tool to use based on the query:
```python
# Simple routing
if "calculate" in query.lower():
    return calculator(query)
elif "search" in query.lower():
    return web_search(query)
else:
    return llm.generate(query)
```

### Parallel Tool Calls
Execute multiple tools simultaneously:
```python
import asyncio

async def parallel_tools(query):
    results = await asyncio.gather(
        search_async(query),
        database_query_async(query),
        calculator_async("complex formula")
    )
    return combine_results(results)
```

### Error Recovery
Handle tool failures gracefully:
```python
try:
    result = tool.execute(args)
except ToolError as e:
    # Let the agent know about the error
    observation = f"Tool error: {e}. Please try a different approach."
```

## Evaluating Agents

| Metric | What It Measures |
|---|---|
| **Task completion** | Did the agent accomplish the goal? |
| **Tool selection** | Did it choose the right tools? |
| **Efficiency** | How many steps did it take? |
| **Cost** | How many tokens/API calls? |
| **Safety** | Did it avoid harmful actions? |

## Further Reading

- Yao et al.'s ReAct paper established the reasoning-action paradigm
- LangChain's documentation is the practical starting point
- OpenAI and Anthropic's function calling docs cover the APIs
- For multi-agent: CrewAI and AutoGen are popular frameworks
