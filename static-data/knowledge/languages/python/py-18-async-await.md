---
title: "Async/Await and Asyncio"
description: "Coroutines, async/await, event loop, tasks, futures, and async I/O with asyncio and aiohttp."
type: lesson
order: 18
duration: "75 min"
difficulty: advanced
learning_objectives:
  - "Write coroutines with async/await"\n  - "Manage the event loop and tasks"\n  - "Use asyncio.gather and asyncio.create_task"\n  - "Build async HTTP clients"
knowledge_refs:
  - python/py-18-async-await
prerequisites:
  - "PY-17"
references:
    - title: "Python Docs — asyncio"\n      url: "https://docs.python.org/3/library/asyncio.html"\n    - title: "Fluent Python — Ch. 20: Async Programming"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"\n    - title: "Real Python — Async IO"\n      url: "https://realpython.com/async-io-python/"
---

# PY-18-ASYNC-AWAIT: Async/Await and Asyncio


## Basic Coroutine

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```

## Running Multiple Tasks

```python
async def fetch(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

