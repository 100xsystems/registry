---
{
  "title": "Async IO with asyncio",
  "description": "Write coroutines with async/await",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write coroutines with async/await",
    "Run concurrent tasks with asyncio.gather",
    "Use async context managers and async iterators",
    "Integrate async with synchronous code"
  ],
  "knowledge_refs": [
    "python/py-18-async-asyncio"
  ],
  "prerequisites": [
    "PY-17"
  ],
  "references": [
    {
      "title": "Python Library — asyncio",
      "url": "https://docs.python.org/3/library/asyncio.html"
    },
    {
      "title": "PEP 492 — async/await",
      "url": "https://peps.python.org/pep-0492/"
    },
    {
      "title": "Real Python — Async IO",
      "url": "https://realpython.com/async-io-python/"
    },
    {
      "title": "aiohttp Docs",
      "url": "https://docs.aiohttp.org/"
    }
  ]
}
---

# PY-18-ASYNC-ASYNCIO: Async IO with asyncio

## Introduction

asyncio (3.4+) provides async/await for concurrent I/O without threads. Single-threaded cooperative multitasking. Ideal for network requests, file I/O, database queries. Python 3.7+ provides a high-level API.

## Key Concepts

### 1. Coroutines with async/await

async def defines a coroutine. await suspends execution until the awaited coroutine completes. Coroutines must be run with asyncio.run(). Never call a coroutine directly.

```python
import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(1)  # non-blocking wait
    print("Done!")
    return {"data": 42}

# run the coroutine
result = asyncio.run(fetch_data())
print(result)  # {"data": 42}
```

### 2. Running Tasks Concurrently

asyncio.create_task() schedules a coroutine to run in the background. asyncio.gather() runs multiple coroutines concurrently and returns results. asyncio.wait() for more control.

```python
import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)  # simulate HTTP
    return f"Data from {url}"

async def main():
    urls = ["a.com", "b.com", "c.com"]

    # run concurrently
    results = await asyncio.gather(*[fetch_url(u) for u in urls])
    print(results)  # all 3 done in ~1s not 3s

    # create tasks for background work
    tasks = [asyncio.create_task(fetch_url(u)) for u in urls]
    done = await asyncio.gather(*tasks)

asyncio.run(main())
```

### 3. Async Context Managers and Iterators

async with for async context managers (e.g., aiohttp.ClientSession). async for for async iterators. Define with __aenter__/__aexit__ and __aiter__/__anext__.

```python
import aiohttp
import asyncio

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# async iterator
class AsyncRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.i += 1
        return self.i

async def main():
    async for num in AsyncRange(5):
        print(num)  # 1, 2, 3, 4, 5
```

### 4. Async Timeouts and Error Handling

asyncio.wait_for() adds timeouts. asyncio.shield() protects tasks from cancellation. asyncio.timeout() (3.11+) is a context manager. Handle exceptions within individual tasks.

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(10)
    return "Done"

async def main():
    # timeout after 2 seconds
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
    except asyncio.TimeoutError:
        print("Operation timed out!")

    # shield a task from cancellation
    task = asyncio.create_task(slow_operation())
    protected = asyncio.shield(task)

    # gathering with return_exceptions
    results = await asyncio.gather(
        task1(), task2(), task3(),
        return_exceptions=True
    )
```

### 5. async with Synchronous Code

asyncio.to_thread() runs sync code in a thread pool. asyncio.run_coroutine_threadsafe() schedules coroutines from sync code. loop.run_in_executor() for blocking operations.

```python
import asyncio
import time

# run blocking sync code without blocking the event loop
async def blocking_task():
    # asyncio.to_thread() runs in a thread (3.9+)
    result = await asyncio.to_thread(time.sleep, 5)
    return result

# from sync code, schedule coroutine on event loop
async def work():
    return 42

loop = asyncio.new_event_loop()
future = asyncio.run_coroutine_threadsafe(work(), loop)
result = future.result()  # blocks until done
```

## Practice Questions

1. What is the difference between async/await and threading?
1. What does asyncio.gather do? How is it different from create_task?
1. When would you use async for vs regular for?
1. How do you add a timeout to an async operation?

## LLM Prompts for Deeper Understanding

1. "Explain Python asyncio: event loop, coroutines, tasks, futures"
1. "Show async context managers and async iterators with real examples"
1. "Teach asyncio.gather, wait, wait_for, shield, and timeouts"

## Key Takeaways

- async/await enables cooperative multitasking without threads
- asyncio.gather runs coroutines concurrently; create_task for background
- Use asyncio.to_thread() to call blocking sync code from async