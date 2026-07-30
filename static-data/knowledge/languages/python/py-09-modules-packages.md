---
{
  "title": "Modules and Packages",
  "description": "Create and import modules",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and import modules",
    "Understand package structure with __init__.py",
    "Use if __name__ guard for script/module duality",
    "Manage dependencies with venv and pip"
  ],
  "knowledge_refs": [
    "python/py-09-modules-packages"
  ],
  "prerequisites": [
    "PY-01"
  ],
  "references": [
    {
      "title": "Python Tutorial — Modules",
      "url": "https://docs.python.org/3/tutorial/modules.html"
    },
    {
      "title": "Python Tutorial — Packages",
      "url": "https://docs.python.org/3/tutorial/modules.html#packages"
    },
    {
      "title": "Python Tutorial — Standard Library",
      "url": "https://docs.python.org/3/tutorial/stdlib.html"
    },
    {
      "title": "Real Python — Modules",
      "url": "https://realpython.com/python-modules-packages/"
    }
  ]
}
---

# PY-09-MODULES-PACKAGES: Modules and Packages

## Introduction

Modules are .py files; packages are directories with __init__.py. Python imports find modules via sys.path. The if __name__ guard lets files work as both scripts and importable modules.

## Key Concepts

### 1. Module Creation and Import

Any .py file is a module. Use import module, from module import name, or from module import * (avoid). Python caches imports in sys.modules — only executes once.

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"
VERSION = "1.0.0"

# main.py
import mymodule
print(mymodule.greet("Alice"))
print(mymodule.VERSION)

# selective import
from mymodule import greet
greet("Bob")
```

### 2. Package Structure with __init__.py

A directory with __init__.py is a package. __init__.py can export names, run setup code. Use relative imports (from . import sibling) within packages.

```python
mypackage/
    __init__.py        # package setup, exports
    module_a.py        # defines func_a()
    module_b.py        # defines func_b()
    subpackage/
        __init__.py    # subpackage setup
        module_c.py    # defines func_c()

# __init__.py
from .module_a import func_a
from .module_b import func_b
__all__ = ["func_a", "func_b"]

# usage
from mypackage import func_a
from mypackage.subpackage import module_c
```

### 3. if __name__ and sys.path

__name__ is the modules name. "__main__" when run directly. sys.path lists directories Python searches for imports. PYTHONPATH env var adds directories.

```python
# script.py — works as script AND import
def main():
    print("Running as script")

if __name__ == "__main__":
    main()

# check module search path
import sys
print(sys.path)  # list of search directories

# add a path
sys.path.insert(0, "/custom/path")
```

### 4. Third-Party Packages and Dependency Management

pip installs from PyPI. Create requirements.txt with pip freeze. Use venv for isolation. pip-compile and poetry for reproducible builds.

```python
$ pip install requests flask django
$ pip freeze > requirements.txt
$ pip install -r requirements.txt

# in Python
import requests
resp = requests.get("https://api.github.com")
resp.json()

$ python3 -m venv .venv
$ source .venv/bin/activate
```

## Practice Questions

1. What makes a directory a package vs a module?
1. What does if __name__ == __main__ do? Why use it?
1. What is sys.path? How to add custom import paths?
1. Why use requirements.txt and venv?

## LLM Prompts for Deeper Understanding

1. "Explain Python import system: absolute, relative, and circular imports"
1. "Show package design patterns: __init__, __all__, namespace packages"
1. "Teach venv, pip, requirements.txt, and pyproject.toml"

## Key Takeaways

- Any .py file is a module; any dir with __init__.py is a package
- __name__ == "__main__" guard enables dual script/module use
- Use venv per project + pip freeze > requirements.txt