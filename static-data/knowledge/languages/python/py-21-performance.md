---
title: "Performance: Profiling, Optimization, and C Extensions"
description: "Profiling with cProfile, optimizing hot paths, using Cython, Numba, and when to drop to C."
type: lesson
order: 21
duration: "75 min"
difficulty: expert
learning_objectives:
  - "Profile Python code with cProfile"\n  - "Optimize with algorithmic improvements"\n  - "Use Cython for C-level performance"\n  - "Apply profiling-driven optimization"
knowledge_refs:
  - python/py-21-performance
prerequisites:
  - "PY-15"
references:
    - title: "Python Docs — cProfile"\n      url: "https://docs.python.org/3/library/profile.html"\n    - title: "Cython Documentation"\n      url: "https://cython.readthedocs.io/"
---

# PY-21-PERFORMANCE: Performance: Profiling, Optimization, and C Extensions


## Profiling with cProfile

```bash
python3 -m cProfile -o profile.stats my_script.py
python3 -c "import pstats; p = pstats.Stats('profile.stats'); p.sort_stats('time').print_top(10)"
```

## Optimization Tips

1. **Use local variables** — local lookups are faster than global
2. **Avoid `+` for string concatenation** in loops — use `"".join()`
3. **Use list comprehensions** over manual `for` loops
4. **Use `in` for set/dict membership** — O(1) vs O(n) for lists

```python
# Slow
s = ""
for chunk in chunks:
    s += chunk

# Fast
s = "".join(chunks)
```

