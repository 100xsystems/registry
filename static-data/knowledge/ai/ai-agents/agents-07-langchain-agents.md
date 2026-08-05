---
slug: agents-07-langchain-agents
title: "Building Agents with LangChain"
description: "Practical guide to building AI agents using LangChain, LangGraph, and the broader LangChain ecosystem."
order: 7
tags:
  - ai-agents
  - langchain
  - langgraph
  - agent-frameworks
  - tool-integration
prerequisites:
  - agents-02-agent-architecture
  - agents-03-tool-use
references:
  - title: "LangChain Documentation"
    author: "LangChain"
    url: "https://python.langchain.com/docs/"
    type: "docs"
    description: "Official LangChain documentation and tutorials."
  - title: "LangGraph Documentation"
    author: "LangChain"
    url: "https://langchain-ai.github.io/langgraph/"
    type: "docs"
    description: "Documentation for LangGraph, the stateful agent orchestration framework."
  - title: "LangChain Deep Agents"
    author: "LangChain"
    url: "https://docs.langchain.com/oss/python/deepagents/overview"
    type: "docs"
    description: "Advanced agent runtime with virtual filesystems and subagents."
  - title: "LangGraph Multi-Agent Concepts"
    author: "LangChain"
    url: "https://langchain-ai.github.io/langgraph/concepts/multi_agent/"
    type: "docs"
    description: "Conceptual guide to multi-agent patterns in LangGraph."
  - title: "Build a LangGraph Agent"
    author: "LangChain"
    url: "https://langchain-ai.github.io/langgraph/tutorials/introduction/"
    type: "docs"
    description: "Step-by-step tutorial for building agents with LangGraph."
related_knowledge:
  - slug: agents-02-agent-architecture
    title: "Agent Architecture"
    lesson_number: 2
  - slug: agents-03-tool-use
    title: "Tool Use"
    lesson_number: 3
  - slug: agents-06-multi-agent-systems
    title: "Multi-Agent Systems"
    lesson_number: 6
knowledge_refs:
  - slug: "llm-01-what-is-llm-engineering"
    title: "Fundamentals of LLMs"
  - slug: "llm-03-llm-apis"
    title: "API Integration"
  - slug: "mlops-10-model-serving"
    title: "Model Serving"
---

# Building Agents with LangChain

LangChain is the most widely adopted open-source framework for building LLM-powered applications, including agents. Combined with LangGraph for stateful orchestration, it provides a comprehensive toolkit for production agent systems.

## LangChain Core Concepts

### Models
LangChain provides a unified interface for interacting with LLMs from multiple providers:
- **ChatOpenAI:** GPT-4, GPT-4o, GPT-3.5-turbo
- **ChatAnthropic:** Claude 3.5 Sonnet, Claude 3 Opus
- **ChatGoogleGenerativeAI:** Gemini models
- **Local models:** Via Ollama, LM Studio, or vLLM

### Prompts
Structured prompt templates with variable substitution:
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that {role}."),
    ("human", "{input}")
])
```

### Tools
Tools are Python functions that agents can call. LangChain provides built-in tools and makes it easy to create custom ones:

```python
from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    """Search the web for current information."""
    # Implementation here
    return results
```

### Chains
LangChain's core abstraction for combining prompts, models, and tools into pipelines:
```python
chain = prompt | model | output_parser
result = chain.invoke({"role": "researcher", "input": "latest AI news"})
```

## Building Agents with LangGraph

LangGraph is LangGraph's framework for building stateful, multi-step agent workflows. It models agent logic as a graph of nodes (functions) and edges (transitions).

### Basic Agent

```python
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")
agent = create_react_agent(model, tools=[search_web, read_file])
result = agent.invoke({"messages": [("human", "What's trending in AI?")]})
```

### Custom Agent with State

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated

class AgentState(TypedDict):
    messages: list
    next_step: str

def researcher(state: AgentState):
    # Research logic
    return {"messages": state["messages"] + [research_result]}

def writer(state: AgentState):
    # Writing logic
    return {"messages": state["messages"] + [written_content]}

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("researcher", researcher)
graph.add_node("writer", writer)
graph.add_edge("researcher", "writer")
graph.add_edge("writer", END)
graph.set_entry_point("researcher")

app = graph.compile()
```

### Human-in-the-Loop
LangGraph supports human approval before sensitive actions:
```python
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

agent = create_react_agent(
    model, tools, checkpointer=MemorySaver()
)

# Before executing a sensitive tool, the agent pauses for human approval
```

## Deep Agents

LangChain's Deep Agents framework extends basic agent capabilities:
- **Virtual Filesystem:** Agents can read, write, and manage files in a sandboxed environment
- **Subagents:** Spawn specialized workers for subtasks
- **Todo Lists:** Built-in task tracking and progress management
- **Context Management:** Automatic summarization and context pruning for long-running tasks

## Production Considerations

### Tracing with LangSmith
LangSmith provides observability for agent execution:
- Track every LLM call, tool invocation, and decision
- Debug agent behavior step-by-step
- Monitor latency, token usage, and costs
- Evaluate agent quality with human feedback

### Error Handling
Robust agents need comprehensive error handling:
```python
@tool
def safe_api_call(url: str) -> str:
    """Make an API call with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Error: {str(e)}"
```

### Memory Management
For long-running agents, implement memory to maintain context:
```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
agent = create_react_agent(model, tools, checkpointer=memory)
```

---

*References:*
1. LangChain, "LangChain Documentation." [Link](https://python.langchain.com/docs/)
2. LangChain, "LangGraph Documentation." [Link](https://langchain-ai.github.io/langgraph/)
3. LangChain, "LangChain Deep Agents." [Link](https://docs.langchain.com/oss/python/deepagents/overview)
4. LangChain, "LangGraph Multi-Agent Concepts." [Link](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
5. LangChain, "Build a LangGraph Agent Tutorial." [Link](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
