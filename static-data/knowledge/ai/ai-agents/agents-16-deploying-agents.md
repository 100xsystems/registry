---
slug: agents-16-deploying-agents
title: "Deploying Agents"
description: "How to deploy AI agents to production with proper infrastructure, containerization, scaling, and monitoring."
order: 16
tags:
  - ai-agents
  - deployment
  - containers
  - cloud
  - scaling
prerequisites:
  - agents-07-langchain-agents
  - agents-13-safety-and-control
  - agents-15-agent-observability
references:
  - title: "Deploying AI Agents at Scale"
    author: "Runpod"
    url: "https://www.runpod.io/articles/guides/deploying-ai-agents-at-scale-building-autonomous-workflows"
    type: "article"
    description: "Building autonomous workflows with infrastructure guidance."
  - title: "Deploying AI Agents to Production"
    author: "Machine Learning Mastery"
    url: "https://machinelearningmastery.com/deploying-ai-agents-to-production-architecture-infrastructure-and-implementation-roadmap/"
    type: "article"
    description: "Architecture, infrastructure, and implementation roadmap."
  - title: "Building AI Agents on AWS Serverless"
    author: "AWS"
    url: "https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/"
    type: "article"
    description: "Serverless agent deployment patterns on AWS."
  - title: "Deploy Your App to Cloud"
    author: "LangSmith"
    url: "https://docs.langchain.com/langsmith/deployment-quickstart"
    type: "docs"
    description: "LangSmith deployment quickstart guide."
  - title: "LangGraph Deployment"
    author: "LangChain"
    url: "https://docs.langchain.com/oss/python/langgraph/deploy"
    type: "docs"
    description: "LangGraph deployment documentation."
related_knowledge:
  - slug: agents-07-langchain-agents
    title: "Building Agents with LangChain"
    lesson_number: 7
  - slug: agents-15-agent-observability
    title: "Agent Observability"
    lesson_number: 15
  - slug: agents-19-agent-cost-and-scale
    title: "Agent Cost & Scale"
    lesson_number: 19
knowledge_refs:
  - slug: "mlops-11-containerization"
    title: "Containerization"
  - slug: "mlops-12-kubernetes-basics"
    title: "Kubernetes"
  - slug: "mlops-13-deployment-strategies"
    title: "Deployment Strategies"
---

# Deploying Agents

Deploying AI agents to production requires careful consideration of architecture, state management, infrastructure, and observability. The deployment decisions you make determine whether your agent is reliable, scalable, and cost-effective.

## The Two-Layer Compute Model

Agent deployments involve two distinct compute layers with different infrastructure needs:

### LLM Inference Layer
- GPU-bound (requires high VRAM)
- Scales with token generation and concurrent requests
- Can be self-hosted (vLLM, TGI) or managed (OpenAI, Anthropic, Bedrock)

### Agent Orchestration Layer
- CPU-bound Python runtimes (FastAPI, LangGraph)
- No GPU required
- Scales with concurrent user sessions and tool-call volume

Separating these layers allows independent scaling and cost optimization.

## State Management

### Stateless Request-Response
Best for one-off tasks: document analysis, classification, data extraction. Easy to horizontally scale behind load balancers.

### Stateful Session-Based Agents
Necessary for conversational or multi-step workflows. State must be externalized:
- **Short-term memory:** Redis for working state
- **Long-term memory:** PostgreSQL, vector databases (Qdrant, Pinecone)
- **Checkpointer:** LangGraph checkpointers for resume-after-interruption

### Event-Driven Asynchronous Agents
For background tasks exceeding HTTP timeouts:
- Message queues (RabbitMQ, AWS SQS, Celery)
- Webhook/Slack completion notifications
- Batch processing pipelines

## Containerization

Package agents in Docker for parity between local development and production:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Cloud Deployment Options

### Serverless Containers (Cloud Run, Fargate, Render)
- Scale-to-zero for cost savings
- Excellent for bursty traffic
- Watch out for timeout limits (Lambda: 15 minutes)

### Container Orchestration (ECS, Kubernetes)
- Persistent background workers
- Zero cold starts
- Better for stateful, always-on agents

### Managed Agent Platforms (LangGraph Cloud, CrewAI Enterprise)
- Built-in persistence, cron jobs, webhooks
- Managed infrastructure and scaling
- Native observability integration

## Tool Integration with MCP

Modern deployments decouple tools from agent logic using MCP:
- Agents operate as MCP clients
- Tools hosted on distributed MCP servers (HTTP/SSE or Lambda)
- Granular OAuth/IAM authorization per tool
- Independent scaling of tool infrastructure

## Production Checklist

- **Observability:** Structured tracing for every LLM call and tool invocation
- **Cost Governance:** Token usage alerts, daily budget caps, model routing
- **Error Handling:** Retry logic, circuit breakers, graceful degradation
- **Security:** Sandboxed execution, input validation, least-privilege tools
- **Testing:** Regression test suite from production traces
- **Rollback:** Ability to revert to previous agent versions quickly

---

*References:*
1. Runpod, "Deploying AI Agents at Scale." [Link](https://www.runpod.io/articles/guides/deploying-ai-agents-at-scale-building-autonomous-workflows)
2. Machine Learning Mastery, "Deploying AI Agents to Production." [Link](https://machinelearningmastery.com/deploying-ai-agents-to-production-architecture-infrastructure-and-implementation-roadmap/)
3. AWS, "Building AI Agents on AWS Serverless." [Link](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)
4. LangSmith, "Deploy Your App to Cloud." [Link](https://docs.langchain.com/langsmith/deployment-quickstart)
5. LangChain, "LangGraph Deployment." [Link](https://docs.langchain.com/oss/python/langgraph/deploy)
