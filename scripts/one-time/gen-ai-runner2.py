#!/usr/bin/env python3
"""Generate the second batch of complete 21-lesson AI courses (six more domains).

Run from anywhere inside the registry repo:

    python3 scripts/one-time/gen-ai-runner2.py

Creates static-data/knowledge/ai/<slug>/ with a hand-curated index.json
(resources + lesson metadata) and 21 lesson .md files for each domain:
reinforcement-learning, mlops, llm-engineering, ai-agents,
prompt-engineering, ai-safety.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_stub_lib import run_spec  # noqa: E402
from gen_ai_data_d import SPECS as SPECS_D  # noqa: E402
from gen_ai_data_e import SPECS as SPECS_E  # noqa: E402
from gen_ai_data_f import SPECS as SPECS_F  # noqa: E402

ALL_SPECS = SPECS_D + SPECS_E + SPECS_F

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'static-data', 'knowledge', 'ai',
)

# ── Hand-curated resources per hub ─────────────────────────────────────

HUB_RESOURCES: dict[str, dict] = {
    'reinforcement-learning': {
        'name': 'Reinforcement Learning',
        'description': 'From MDPs and dynamic programming to DQN, PPO and multi-agent systems — the complete guide to agents that learn from outcomes.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Reinforcement Learning: An Introduction — Sutton & Barto', 'url': 'http://incompleteideas.net/book/the-book-2nd.html', 'description': 'The canonical RL textbook (free PDF).'},
                    {'title': 'Spinning Up in Deep RL — OpenAI', 'url': 'https://spinningup.openai.com/en/latest/', 'description': 'A practitioner-focused deep RL resource with clean implementations.'},
                    {'title': 'RL Course by David Silver', 'url': 'https://www.davidsilver.uk/teaching/', 'description': 'The classic lecture series on RL fundamentals.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'Stable-Baselines3 Documentation', 'url': 'https://stable-baselines3.readthedocs.io/', 'description': 'Reliable RL algorithm implementations in PyTorch.'},
                    {'title': 'Gymnasium Documentation', 'url': 'https://gymnasium.farama.org/', 'description': 'The standard API for RL environments.'},
                    {'title': 'DeepMind x UCL RL Lecture Series', 'url': 'https://www.deepmind.com/learning-resources/reinforcement-learning-lectures-by-david-silver', 'description': 'Advanced RL topics from DeepMind researchers.'},
                ],
            },
        ],
    },
    'mlops': {
        'name': 'MLOps',
        'description': 'Operationalize machine learning: lifecycle, versioning, pipelines, experiment tracking, serving, Kubernetes and drift monitoring.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'The ML Engineer — Chip Huyen', 'url': 'https://www.oreilly.com/library/view/introduction-to-machine/9781098119478/', 'description': 'The reference book on building ML systems in production.'},
                    {'title': 'Google MLOps Whitepaper', 'url': 'https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning', 'description': 'The canonical description of MLOps levels and practices.'},
                    {'title': 'Made With ML', 'url': 'https://madewithml.com/', 'description': 'Hands-on MLOps course covering the full production lifecycle.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'MLflow Documentation', 'url': 'https://mlflow.org/docs/latest/index.html', 'description': 'Tracking, registries and serving for the ML lifecycle.'},
                    {'title': 'DVC Documentation', 'url': 'https://dvc.org/doc', 'description': 'Data version control for reproducible ML pipelines.'},
                    {'title': 'Kubeflow Documentation', 'url': 'https://www.kubeflow.org/docs/', 'description': 'Kubernetes-native ML workflows.'},
                ],
            },
        ],
    },
    'llm-engineering': {
        'name': 'LLM Engineering',
        'description': 'Build with large language models: tokenization, embeddings, RAG, fine-tuning, evals, agents and production LLM systems.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Hugging Face NLP Course', 'url': 'https://huggingface.co/learn/nlp-course', 'description': 'Transformers, fine-tuning and LLM fundamentals with hands-on code.'},
                    {'title': 'Attention Is All You Need', 'url': 'https://arxiv.org/abs/1706.03762', 'description': 'The Transformer paper that made modern LLMs possible.'},
                    {'title': 'DeepLearning.AI Short Courses', 'url': 'https://www.deeplearning.ai/short-courses/', 'description': 'Practical LLM engineering courses from industry experts.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'OpenAI Documentation', 'url': 'https://platform.openai.com/docs', 'description': 'API reference for GPT models, embeddings and function calling.'},
                    {'title': 'LangChain Documentation', 'url': 'https://python.langchain.com/docs', 'description': 'Frameworks for RAG, agents and LLM applications.'},
                    {'title': 'LlamaIndex Documentation', 'url': 'https://docs.llamaindex.ai/', 'description': 'Data framework for connecting LLMs to your data.'},
                ],
            },
        ],
    },
    'ai-agents': {
        'name': 'AI Agents',
        'description': 'Design agents that reason, use tools and act: agent loops, tool use, memory, planning, multi-agent systems and agent frameworks.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Anthropic — Building Effective Agents', 'url': 'https://www.anthropic.com/research/building-effective-agents', 'description': 'The canonical essay on agent architectures and patterns.'},
                    {'title': 'OpenAI — A Practical Guide to Building Agents', 'url': 'https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf', 'description': 'Production agent patterns: delegation, orchestration, guardrails.'},
                    {'title': 'DeepLearning.AI — AI Agents in LangGraph', 'url': 'https://www.deeplearning.ai/short-courses/', 'description': 'Hands-on agent building with graph-based orchestration.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'LangGraph Documentation', 'url': 'https://langchain-ai.github.io/langgraph/', 'description': 'Low-level orchestration framework for agent state machines.'},
                    {'title': 'CrewAI Documentation', 'url': 'https://docs.crewai.com/', 'description': 'Role-based multi-agent framework.'},
                    {'title': 'OpenAI Agents SDK', 'url': 'https://openai.github.io/openai-agents-python/', 'description': 'Lightweight agent framework with handoffs and guardrails.'},
                ],
            },
        ],
    },
    'prompt-engineering': {
        'name': 'Prompt Engineering',
        'description': 'Get the best out of language models: system prompts, few-shot, chain-of-thought, structured outputs, and evaluation.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'OpenAI Prompt Engineering Guide', 'url': 'https://platform.openai.com/docs/guides/prompt-engineering', 'description': 'Official strategies for reliable, high-quality outputs.'},
                    {'title': 'Anthropic Prompt Engineering Overview', 'url': 'https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview', 'description': 'The Claude cookbook of prompting techniques.'},
                    {'title': 'Prompt Engineering Guide — DAIR.AI', 'url': 'https://www.promptingguide.ai/', 'description': 'A community guide to state-of-the-art prompting techniques.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'OpenAI Structured Outputs', 'url': 'https://platform.openai.com/docs/guides/structured-outputs', 'description': 'Reliable JSON and schema-conforming model outputs.'},
                    {'title': 'Anthropic Context Engineering', 'url': 'https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents', 'description': 'Engineering the context window for better agents.'},
                    {'title': 'OpenAI Function Calling', 'url': 'https://platform.openai.com/docs/guides/function-calling', 'description': 'Connect models to tools with structured arguments.'},
                ],
            },
        ],
    },
    'ai-safety': {
        'name': 'AI Safety',
        'description': 'Understand the risks of AI systems and the practices that keep them aligned, robust and fair — from evals to governance.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Anthropic Alignment Science', 'url': 'https://www.anthropic.com/research/alignment-science', 'description': 'Research on making AI systems honest, harmless and helpful.'},
                    {'title': 'OpenAI Evals', 'url': 'https://github.com/openai/evals', 'description': 'A framework for evaluating LLMs and agent systems.'},
                    {'title': 'AI Safety Fundamentals', 'url': 'https://aisafetyfundamentals.com/', 'description': 'Structured courses on alignment and AI governance.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'The Alignment Problem — Brian Christian', 'url': 'https://brianchristian.org/the-alignment-problem/', 'description': 'The history and science of aligning AI with human values.'},
                    {'title': 'EU AI Act Overview', 'url': 'https://artificialintelligenceact.eu/', 'description': 'The landmark AI regulation explained.'},
                    {'title': 'NIST AI Risk Management Framework', 'url': 'https://www.nist.gov/itl/ai-risk-management-framework', 'description': 'A framework for managing AI-related risks.'},
                ],
            },
        ],
    },
}


def build_index(spec: dict) -> None:
    """Write the hub index.json (must exist before the lesson generator runs)."""
    slug = spec['lang']
    hub_dir = os.path.join(BASE, slug)
    os.makedirs(hub_dir, exist_ok=True)

    res = HUB_RESOURCES[slug]
    index = {
        'slug': slug,
        'name': res['name'],
        'description': res['description'],
        'categories': res['categories'],
        'lessons': [],
    }
    with open(os.path.join(hub_dir, 'index.json'), 'w') as fh:
        json.dump(index, fh, indent=2, ensure_ascii=False)
    print(f'[{slug}] wrote index.json')


if __name__ == '__main__':
    assert len(ALL_SPECS) == 6, f'expected 6 AI course specs, got {len(ALL_SPECS)}'
    os.makedirs(BASE, exist_ok=True)
    for spec in ALL_SPECS:
        build_index(spec)
        run_spec(spec, os.path.join(BASE, spec['lang']))
    print('Done. 6 more AI courses generated (12 total).')
