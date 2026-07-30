---
{
  "title": "Concurrency: Threading and Multiprocessing",
  "description": "Create and manage threads with threading module",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create and manage threads with threading module",
    "Use ThreadPoolExecutor for parallel execution",
    "Understand GIL limitations and multiprocessing",
    "Use locks, queues, and semaphores for safety"
  ],
  "knowledge_refs": [
    "python/py-17-concurrency-threads"
  ],
  "prerequisites": [
    "PY-08"
  ],
  "references": [
    {
      "title": "Python Library — threading",
      "url": "https://docs.python.org/3/library/threading.html"
    },
    {
      "title": "Python Library — multiprocessing",
      "url": "https://docs.python.org/3/library/multiprocessing.html"
    },
    {
      "title": "Python Library — concurrent.futures",
      "url": "https://docs.python.org/3/library/concurrent.futures.html"
    },
    {
      "title": "Real Python — Threading",
      "url": "https://realpython.com/intro-to-python-threading/"
    }
  ]
}
---

# PY-17-CONCURRENCY-THREADS: Concurrency: Threading and Multiprocessing

## Introduction

Python provides threads (I/O-bound concurrency) and processes (CPU-bound parallelism). The GIL limits threads to one CPU core at a time. concurrent.futures provides a high-level interface for both.

## Key Concepts

### 1. Threading Basics

threading.Thread creates a thread. start() begins execution; join() waits for completion. daemon threads exit when main thread exits. Threads share memory, requiring locks for safety.

```python
import threading
import time

def worker(name, delay):
    print(f"{name} starting")
    time.sleep(delay)
    print(f"{name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"T{i}", i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # wait for all to finish
print("All done")
```

### 2. Thread Safety: Locks and Queues

threading.Lock prevents race conditions. Use with lock: (context manager) for safe access. queue.Queue provides thread-safe FIFO for producer-consumer patterns.

```python
import threading
from queue import Queue

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # exclusive access
            counter += 1

# thread-safe queue
q = Queue()

def producer():
    for i in range(10):
        q.put(i)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Got {item}")
        q.task_done()
```

### 3. ThreadPoolExecutor

concurrent.futures.ThreadPoolExecutor manages a pool of threads. submit() returns a Future; map() applies function to iterable. As completed via as_completed().

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch_url(url):
    time.sleep(1)  # simulate HTTP request
    return f"Data from {url}"

urls = ["http://a.com", "http://b.com", "http://c.com"]

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_url = {executor.submit(fetch_url, u): u for u in urls}
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            print(f"{url}: {data}")
        except Exception as e:
            print(f"{url} failed: {e}")
```

### 4. Multiprocessing for CPU-Bound Tasks

multiprocessing bypasses the GIL by using separate processes. Pool.map() distributes work. Process has same API as Thread. Shared memory via Value, Array, or Manager.

```python
from multiprocessing import Pool, cpu_count

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

numbers = range(1, 100000)

with Pool(cpu_count()) as pool:
    results = pool.map(is_prime, numbers)
    print(f"Found {sum(results)} primes")
```

### 5. ProcessPoolExecutor

concurrent.futures.ProcessPoolExecutor provides the same API as ThreadPoolExecutor but uses processes. Best for CPU-intensive work. Use the same submit/map/as_completed interface.

```python
from concurrent.futures import ProcessPoolExecutor

def compute(intensive_task(x):
    # CPU-heavy computation
    return sum(i * i for i in range(x))

with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(compute, range(1000, 1100)))
    print(f"Computed {len(results)} results")
```

## Practice Questions

1. What is the GIL? How does it affect threads vs processes?
1. When would you use threading vs multiprocessing?
1. Why use queue.Queue with threads?
1. What is the difference between ThreadPoolExecutor and ProcessPoolExecutor?

## LLM Prompts for Deeper Understanding

1. "Explain GIL limitations and when threading vs multiprocessing applies"
1. "Show thread safety: Lock, RLock, Semaphore, Queue, Event"
1. "Teach concurrent.futures: ThreadPoolExecutor, ProcessPoolExecutor, Future"

## Key Takeaways

- Threading for I/O-bound; multiprocessing for CPU-bound (bypasses GIL)
- Use Lock for shared memory safety; Queue for producer-consumer
- concurrent.futures provides unified interface for threads and processes