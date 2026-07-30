---
title: "Modules, Packages, and Virtual Environments"
description: "Import system, module creation, packages, virtual environments, and pip dependency management."
type: lesson
order: 9
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Create and import modules and packages"\n  - "Understand the module search path"\n  - "Use virtual environments to isolate dependencies"\n  - "Manage packages with pip"
knowledge_refs:
  - python/py-09-modules-packages
prerequisites:
  - "PY-04"
references:
    - title: "Python Tutorial — 6. Modules"\n      url: "https://docs.python.org/3/tutorial/modules.html"\n    - title: "Python Tutorial — 12. Virtual Environments"\n      url: "https://docs.python.org/3/tutorial/venv.html"\n    - title: "Python Reference — Import System"\n      url: "https://docs.python.org/3/reference/import.html"
---

# PY-09-MODULES-PACKAGES: Modules, Packages, and Virtual Environments


## Creating Modules

Any `.py` file is a module — see [Modules](https://docs.python.org/3/tutorial/modules.html):
```python
# utils.py
def add(a, b): return a + b
PI = 3.14159
```

```python
# main.py
import utils
from utils import PI
print(utils.add(2, 3))  # 5
```

## Packages

A directory with `__init__.py` becomes a package:
```python
mypackage/
  __init__.py
  math/
    __init__.py
    algebra.py
    calculus.py
  string/
    __init__.py
    manip.py
```

## Virtual Environments

```bash
python3 -m venv .venv      # Create
source .venv/bin/activate  # Activate (macOS/Linux)
pip install requests numpy  # Install packages
pip freeze > requirements.txt  # Export
```

