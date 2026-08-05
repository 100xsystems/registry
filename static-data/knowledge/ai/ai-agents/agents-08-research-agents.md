---
slug: agents-08-research-agents
title: "Building a Research Agent"
description: "How to build AI agents that search the web, synthesize information from multiple sources, and generate comprehensive reports."
order: 8
tags:
  - ai-agents
  - research-agent
  - web-search
  - information-synthesis
  - report-generation
prerequisites:
  - agents-06-multi-agent-systems
  - agents-07-langchain-agents
references:
  - title: "Open Deep Research"
    author: "LangChain"
    url: "https://www.langchain.com/blog/open-deep-research"
    type: "article"
    description: "Technical breakdown of LangChain's 3-phase deep research architecture."
  - title: "Building a Multi-Agent Deep Research Agent with LangGraph"
    author: "Data Science Collective"
    url: "https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12"
    type: "article"
    description: "Practical walkthrough of 12 specialized agent roles for deep research."
  - title: "Build a Deep Research Agent"
    author: "LangChain Docs"
    url: "https://docs.langchain.com/oss/python/deepagents/deep-research"
    type: "docs"
    description: "Official tutorial for building a multi-step web research agent."
  - title: "How to Build a Multi-Agent Research Assistant in Python"
    author: "Machine Learning Mastery"
    url: "https://machinelearningmastery.com/how-to-build-a-multi-agent-research-assistant-in-python/"
    type: "article"
    description: "Code-driven guide using OpenAI Agents SDK and Olostep APIs."
  - title: "LangChain Deep Agents Quickstart"
    author: "LangChain"
    url: "https://docs.langchain.com/oss/python/deepagents/quickstart"
    type: "docs"
    description: "Setup guide for core file system tools and search configurations."
related_knowledge:
  - slug: agents-06-multi-agent-systems
    title: "Multi-Agent Systems"
    lesson_number: 6
  - slug: agents-07-langchain-agents
    title: "Building Agents with LangChain"
    lesson_number: 7
  - slug: agents-09-browser-agents
    title: "Browser Automation Agents"
    lesson_number: 9
knowledge_refs:
  - slug: "llm-07-rag-engineering"
    title: "Information Retrieval"
  - slug: "nlp-19-summarization"
    title: "Text Summarization"
  - slug: "genai-10-rag"
    title: "RAG"
---

# Building a Research Agent

Research agents automate the process of gathering information from multiple sources, synthesizing findings, and producing comprehensive reports. They represent one of the most practical and high-value agent applications.

## The Three-Phase Architecture

Production research agents follow a consistent three-phase pattern:

### Phase 1: Scoping
Before searching, the agent clarifies the research goal:
- Parse the user's request into specific research questions
- Identify key topics, entities, and relationships to investigate
- Generate a **Research Brief** that acts as the north star for the entire run
- Ask clarifying questions if the request is ambiguous

This phase prevents wasted effort on irrelevant searches and ensures the research stays focused.

### Phase 2: Research
The agent gathers information through parallel and sequential search operations:

**Search Strategy:**
- Use multiple search APIs (Tavily, Brave, SerpAPI) for diversity
- Crawl full pages for depth beyond search snippets
- Extract key facts, quotes, and data points
- Track sources with unique IDs for citation management

**Multi-Agent Research:**
For complex topics, deploy specialized sub-agents:
- **Evidence Gatherer:** Finds primary sources and data
- **Context Explorer:** Provides background and historical context
- **Skeptic:** Identifies counterarguments and limitations
- **Comparator:** Evaluates competing claims and perspectives

Each specialist operates with an isolated context window, preventing information overload.

### Phase 3: Synthesis
The agent compiles findings into a coherent report:
- Organize information by theme or chronology
- Cross-reference claims across sources
- Generate citations with proper attribution
- Flag areas of uncertainty or conflicting evidence

## Citation Management

A critical challenge in research agents is citation accuracy. Production systems implement:

1. **Citation Registry:** All sources are assigned unique IDs during research
2. **Citation Audit:** Before final output, a verification step checks that every claim has a corresponding source
3. **Citation Enforcement:** The report writer is restricted to citing only audited sources from the registry

This prevents hallucinated citations and ensures every claim is verifiable.

## Building a Research Agent

### Simple Research Agent

```python
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import TavilySearchResults

tools = [TavilySearchResults(max_results=5)]
model = ChatOpenAI(model="gpt-4o")

agent = create_react_agent(
    model, tools,
    state_modifier="You are a research agent. Search the web, gather evidence, and provide comprehensive answers with citations."
)
```

### Multi-Agent Research System

```python
from langgraph.graph import StateGraph, END

def scope_research(state):
    """Phase 1: Define research questions"""
    questions = model.invoke(f"Break down this topic into research questions: {state['topic']}")
    return {"questions": questions.content}

def gather_evidence(state):
    """Phase 2: Search and collect evidence"""
    evidence = []
    for question in state["questions"]:
        results = search_tool.invoke(question)
        evidence.append(results)
    return {"evidence": evidence}

def synthesize_report(state):
    """Phase 3: Write the final report"""
    report = model.invoke(f"Write a comprehensive report based on: {state['evidence']}")
    return {"report": report.content}

# Build the graph
graph = StateGraph(dict)
graph.add_node("scope", scope_research)
graph.add_node("research", gather_evidence)
graph.add_node("synthesize", synthesize_report)
graph.add_edge("scope", "research")
graph.add_edge("research", "synthesize")
graph.add_edge("synthesize", END)
graph.set_entry_point("scope")

app = graph.compile()
```

## Advanced Techniques

### Iterative Deepening
Start with broad searches, then drill deeper into promising areas:
1. Initial search → identify key themes
2. Focused search on each theme → gather detailed evidence
3. Gap analysis → search for missing information
4. Final synthesis

### Source Diversity
Ensure information comes from multiple perspectives:
- Academic papers for rigor
- Industry reports for practical insights
- News articles for current events
- Primary sources for accuracy

### Fact Verification
Cross-reference claims across multiple sources before including them in the report. Flag any claims that appear in only one source.

---

*References:*
1. LangChain, "Open Deep Research." [Link](https://www.langchain.com/blog/open-deep-research)
2. Data Science Collective, "Building a Multi-Agent Deep Research Agent with LangGraph." [Link](https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12)
3. LangChain, "Build a Deep Research Agent." [Link](https://docs.langchain.com/oss/python/deepagents/deep-research)
4. Machine Learning Mastery, "How to Build a Multi-Agent Research Assistant in Python." [Link](https://machinelearningmastery.com/how-to-build-a-multi-agent-research-assistant-in-python/)
5. LangChain, "Deep Agents Quickstart." [Link](https://docs.langchain.com/oss/python/deepagents/quickstart)
