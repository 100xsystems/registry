---
{
  "title": "Retrieval-Augmented Generation (RAG)",
  "description": "Ground answers in your own data: retrieve relevant chunks, stuff the context, generate.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the RAG pipeline",
    "Chunk documents thoughtfully",
    "Retrieve with embeddings and keyword search",
    "Build a RAG chain with LangChain"
  ],
  "knowledge_refs": [
    "generative-ai/genai-09-rlhf-and-alignment",
    "llm-engineering/llm-07-rag-engineering",
    "llm-engineering/llm-08-advanced-rag"
  ],
  "prerequisites": [
    "GENAI-04: Prompt Engineering"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "Transformers, fine-tuning and LLM fundamentals with hands-on code."
    },
    {
      "title": "OpenAI Documentation",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for GPT models, embeddings and function calling."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The Transformer paper that made generative AI possible."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "DeepLearning.AI Short Courses",
      "url": "https://www.deeplearning.ai/short-courses/",
      "description": "Practical AI courses from industry experts."
    }
  ]
}
---

# GENAI-10-RAG: Retrieval-Augmented Generation (RAG)

## Introduction

Ground answers in your own data: retrieve relevant chunks, stuff the context, generate. By the end of this lesson you will be able to: Explain the RAG pipeline; Chunk documents thoughtfully; Retrieve with embeddings and keyword search; Build a RAG chain with LangChain.

## Key Concepts

### 1. Explain the RAG pipeline

Target: Explain the RAG pipeline. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
rag = {
    1: "chunk documents",
    2: "embed chunks",
    3: "retrieve top-k for a question",
    4: "generate with the context",
}
print(rag)
```
### 2. Chunk documents thoughtfully

Target: Chunk documents thoughtfully. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from langchain_community.vectorstores import FAISS

print("vector store ready")
```
### 3. Retrieve with embeddings and keyword search

Target: Retrieve with embeddings and keyword search. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
print("chunker ready")
```
### 4. Build a RAG chain with LangChain

Target: Build a RAG chain with LangChain. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Answer from the context.\nContext: {context}\nQuestion: {question}"
)
print(prompt)
```

## Practice Questions

1. What is the key idea behind "Retrieval-Augmented Generation (RAG)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Retrieval-Augmented Generation (RAG) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Retrieval-Augmented Generation (RAG)"
1. "Provide advanced patterns and performance considerations for Retrieval-Augmented Generation (RAG)"

## Key Takeaways

- Master the core ideas of Retrieval-Augmented Generation (RAG) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
