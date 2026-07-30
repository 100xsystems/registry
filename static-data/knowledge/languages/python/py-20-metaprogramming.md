---
title: "Metaprogramming and Advanced Features"
description: "Metaclasses, class decorators, __init_subclass__, __set_name__, and dynamic attribute access."
type: lesson
order: 20
duration: "75 min"
difficulty: expert
learning_objectives:
  - "Create metaclasses for class customization"\n  - "Use __init_subclass__ and __set_name__"\n  - "Implement dynamic attribute access"\n  - "Apply class decorators"
knowledge_refs:
  - python/py-20-metaprogramming
prerequisites:
  - "PY-12"
references:
    - title: "Fluent Python — Ch. 23: Metaclasses"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"\n    - title: "Python Reference — Data Model"\n      url: "https://docs.python.org/3/reference/datamodel.html#metaclasses"\n    - title: "Real Python — Metaclasses"\n      url: "https://realpython.com/python-metaclasses/"
---

# PY-20-METAPROGRAMMING: Metaprogramming and Advanced Features


## Metaclasses

A metaclass is the class of a class — it controls how classes are created:
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connected = False

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

