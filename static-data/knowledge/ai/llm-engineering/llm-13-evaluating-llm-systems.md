---
slug: llm-13-evaluating-llm-systems
title: "Evaluating LLM Systems"
description: "Measuring what matters — LLM-as-judge, human evaluation, automated benchmarks, and eval frameworks for production."
order: 13
tags:
  - llm-engineering
  - evaluation
  - llm-as-judge
  - benchmarks
prerequisites:
  - llm-04-prompting-systems
  - llm-07-rag-engineering
knowledge_refs:
  - llm-04-prompting-systems
  - llm-07-rag-engineering
  - llm-14-guardrails-and-safety
references:
  - title: "Inspect AI Framework"
    url: "https://inspect.aisi.org.uk/"
    notes: "UK AISI's evaluation framework"
  - title: "LangSmith Evaluation"
    url: "https://www.langchain.com/langsmith/evaluation"
    notes: "Production evaluation platform"
  - title: "LLM-as-a-Judge"
    url: "https://en.wikipedia.org/wiki/LLM-as-a-Judge"
    notes: "Overview of LLM evaluation methods"
  - title: "RAGAS Documentation"
    url: "https://docs.ragas.io/"
    notes: "RAG evaluation metrics"
  - title: "Evidently AI LLM Evaluation Guide"
    url: "https://www.evidentlyai.com/llm-guide/llm-evaluation"
    notes: "Beginner's guide to LLM evaluation"
---

# Evaluating LLM Systems

Evaluating LLM outputs is fundamentally different from traditional software testing. Outputs are non-deterministic, quality is subjective, and "correct" depends on context.

## Evaluation Approaches

### Human Evaluation
The gold standard — but expensive and slow:
- **Likert scales**: rate 1-5 on fluency, accuracy, helpfulness
- **Pairwise comparison**: A or B is better?
- **Expert review**: domain specialists validate accuracy

### LLM-as-a-Judge
Use a stronger model to evaluate weaker ones:
```python
judge_prompt = """
Rate this response on a scale of 1-5:
- Accuracy: Is the information correct?
- Helpfulness: Does it address the user's need?
- Clarity: Is it well-organized and clear?

Response: {model_response}
Reference: {reference_answer}
"""
```

**Known biases to mitigate:**
- **Position bias**: favoring the first option
- **Verbosity bias**: favoring longer responses
- **Self-enhancement**: favoring outputs from the same model

### Automated Benchmarks
| Benchmark | What It Tests |
|-----------|---------------|
| MMLU | Broad knowledge (57 subjects) |
| GSM8K | Mathematical reasoning |
| HumanEval | Code generation |
| TruthfulQA | Factual accuracy |
| MT-Bench | Multi-turn conversation |

## Application-Level Evaluation

Benchmarks test the model; application eval tests your system:

### RAG Evaluation
| Metric | Measures |
|--------|----------|
| Context Precision | Are retrieved docs relevant? |
| Context Recall | Are all relevant docs found? |
| Faithfulness | Is the answer grounded? |
| Answer Relevance | Does it address the query? |

### Agent Evaluation
- **Task completion rate**: did the agent finish the task?
- **Tool usage accuracy**: were the right tools called?
- **Step efficiency**: how many steps to complete?
- **Cost per task**: total tokens and API calls used

## Eval Frameworks

### Inspect AI (UK AISI)
- Code-first, composable framework
- Datasets, solvers, scorers, sandboxes
- Visual transcript debugger

### LangSmith
- Production observability
- Experiment tracking across prompt versions
- Human annotation queues
- CI/CD threshold gating

### RAGAS
- RAG-specific evaluation
- Faithfulness, answer relevance, context metrics
- Synthetic test data generation

## Building an Eval Pipeline

```python
# 1. Create test dataset
test_cases = load_test_cases("eval_dataset.json")

# 2. Run model on each case
results = []
for case in test_cases:
    output = model.generate(case.prompt)
    results.append({"input": case, "output": output})

# 3. Score with LLM judge
for result in results:
    result["score"] = llm_judge.score(result)

# 4. Analyze results
pass_rate = sum(r["score"] >= 4 for r in results) / len(results)
print(f"Pass rate: {pass_rate:.1%}")
```

## Key Takeaways

1. Human evaluation is gold standard but expensive; LLM-as-judge scales well
2. Application-level eval matters more than model benchmarks
3. RAG evaluation requires both retrieval and generation metrics
4. Build eval pipelines into CI/CD to catch regressions
5. Watch for LLM judge biases: position, verbosity, self-enhancement
