---
title: "Concurrency with Threading and Multiprocessing"
description: "Threading, thread safety, the GIL, multiprocessing, and choosing the right concurrency model."
type: lesson
order: 17
duration: "75 min"
difficulty: advanced
learning_objectives:
  - "Create threads with threading module"\n  - "Use locks and queues for thread safety"\n  - "Understand the GIL limitations"\n  - "Use multiprocessing for CPU-bound tasks"
knowledge_refs:
  - python/py-17-concurrency-threads
prerequisites:
  - "PY-08"
references:
    - title: "Python Docs — threading"\n      url: "https://docs.python.org/3/library/threading.html"\n    - title: "Python Docs — multiprocessing"\n      url: "https://docs.python.org/3/library/multiprocessing.html"\n    - title: "Fluent Python — Ch. 19: Concurrency Models"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-17-CONCURRENCY-THREADS: Concurrency with Threading and Multiprocessing


## Threading (I/O-bound)

```python
import threading

def worker(name):
    print(f"Worker {name} starting")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
```

## Thread Safety with Lock

```python
lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1
```

## Multiprocessing (CPU-bound)

```python
from multiprocessing import Pool

def square(n): return n * n
with Pool(4) as p:
    results = p.map(square, range(100))
```

