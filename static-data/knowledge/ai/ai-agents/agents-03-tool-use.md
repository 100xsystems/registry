---
slug: agents-03-tool-use
title: "Tool Use"
description: "How AI agents interact with external systems through function calling, tool definitions, and the Model Context Protocol."
order: 3
tags:
  - ai-agents
  - tool-use
  - function-calling
  - mcp
  - tool-orchestration
prerequisites:
  - agents-02-agent-architecture
references:
  - title: "Tool use with Claude"
    author: "Anthropic"
    url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview"
    type: "docs"
    description: "Comprehensive guide to tool use with Claude models."
  - title: "Function Calling in the OpenAI API"
    author: "OpenAI"
    url: "https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api"
    type: "docs"
    description: "OpenAI's function calling documentation and best practices."
  - title: "Introducing the Model Context Protocol"
    author: "Anthropic"
    url: "https://www.anthropic.com/news/model-context-protocol"
    type: "article"
    description: "Announcement of MCP as an open standard for agent-tool integration."
  - title: "Model Context Protocol (MCP) Specification"
    author: "Anthropic"
    url: "https://docs.anthropic.com/en/docs/agents-and-tools/mcp"
    type: "docs"
    description: "Technical specification for the Model Context Protocol."
  - title: "Writing Effective Tools for AI Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/writing-tools-for-agents"
    type: "article"
    description: "Best practices for designing tools that agents can use effectively."
related_knowledge:
  - slug: agents-02-agent-architecture
    title: "Agent Architecture"
    lesson_number: 2
  - slug: agents-04-reasoning-and-planning
    title: "Reasoning and Planning"
    lesson_number: 4
  - slug: agents-07-langchain-agents
    title: "Building Agents with LangChain"
    lesson_number: 7
knowledge_refs:
  - slug: "llm-01-fundamentals-of-llms"
    title: "Fundamentals of LLMs"
  - slug: "genai-14-api-integration"
    title: "API Integration"
  - slug: "mlops-10-model-serving"
    title: "Model Serving"
---

# Tool Use

Tool use — often implemented as function calling — allows AI agents to interact with external systems: APIs, databases, file systems, and web services. Instead of merely generating text, agents recognize when external action is needed and return structured payloads that trigger real-world operations.

## The Tool Calling Lifecycle

Tool use follows a structured round-trip between the model and the application:

### 1. Tool Definition
Tools are declared using JSON Schema objects specifying:
- **Name:** A clear identifier (e.g., `search_web`, `read_file`)
- **Description:** Instructions for the model on when and how to use it
- **Parameters:** Required and optional arguments with types and constraints

```json
{
  "name": "search_web",
  "description": "Search the web for current information. Use for factual queries.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query"
      },
      "max_results": {
        "type": "integer",
        "description": "Maximum number of results to return"
      }
    },
    "required": ["query"]
  }
}
```

### 2. User Request
The user provides a prompt that may or may not require tool use.

### 3. Model Evaluation
The application sends the prompt along with available tool definitions. The model evaluates whether a tool is needed based on the user's intent.

### 4. Tool Call Generation
If a tool matches, the model halts generation and returns structured arguments:
```json
{
  "tool": "search_web",
  "arguments": {
    "query": "latest advances in AI agents 2024",
    "max_results": 5
  }
}
```

### 5. Execution
The application intercepts the tool call, executes the actual code or API request, and obtains the result.

### 6. Result Injection
The application sends a follow-up request containing the original conversation plus the tool output.

### 7. Final Response
The model synthesizes the tool result into a natural language answer for the user.

## Tool Selection Strategies

### Auto Selection (Default)
The model independently decides whether to answer conversationally or call a tool based on context and system prompts. This is the most common mode.

### Forced Tool Use
Developers can override auto-selection by requiring a specific tool call or forcing any tool use. Useful when the agent must always retrieve fresh data before responding.

### Prompt Steering
If a model under-utilizes tools, system prompt instructions can adjust the triggering threshold: "Always use the search tool before answering factual queries."

## Parallel Tool Use

Modern agent frameworks support invoking multiple independent tools simultaneously in a single model turn. For example, querying weather in three different cities at once, then combining results into a single response. The orchestrator handles batching execution and feeding all results back together.

## The Model Context Protocol (MCP)

MCP, developed by Anthropic and donated to the Agentic AI Foundation under the Linux Foundation, is an open standard for agent-tool integration. It functions as a "USB-C port for AI," establishing a standardized client-server architecture:

- **MCP Hosts/Clients:** Applications like Claude Desktop or custom agents
- **MCP Servers:** Exposing capabilities (filesystems, databases, APIs)

MCP standardizes three main capabilities:
- **Resources:** Reading context and data
- **Prompts:** Template workflows for common operations
- **Tools:** Executable functions that agents can invoke

MCP eliminates the need for custom integrations, allowing agents to connect to any compliant server with a single protocol.

## Tool Design Best Practices

Anthropic's engineering team recommends these principles for designing tools that agents use effectively:

**Token Efficiency:** Return high-signal context — summaries, filtered results, paginated data — rather than dumping entire database tables into the context window.

**Poka-Yoke (Mistake-Proofing):** Design parameters to minimize agent errors. Use absolute file paths instead of relative ones. Provide enumerated options instead of free-text fields when possible.

**Namespacing:** Group related tools under prefixes to prevent confusion when models have access to dozens of tools. For example, `jira_create_issue` and `jira_search_issues` clearly belong together.

**Clear Descriptions:** Tool descriptions are instructions for the model. Be precise about when to use each tool, what edge cases to watch for, and what the expected output format is.

---

*References:*
1. Anthropic, "Tool use with Claude." [Link](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
2. OpenAI, "Function Calling in the OpenAI API." [Link](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api)
3. Anthropic, "Introducing the Model Context Protocol." [Link](https://www.anthropic.com/news/model-context-protocol)
4. Anthropic, "Model Context Protocol (MCP) Specification." [Link](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
5. Anthropic Engineering, "Writing Effective Tools for AI Agents." [Link](https://www.anthropic.com/engineering/writing-tools-for-agents)
