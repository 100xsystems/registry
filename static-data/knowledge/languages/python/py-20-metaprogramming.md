---
{
  "title": "Metaprogramming: Metaclasses and Descriptors",
  "description": "Understand metaclasses (type) and class creation",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand metaclasses (type) and class creation",
    "Use __init_subclass__ for class customization",
    "Implement descriptors with __get__/__set__",
    "Apply __prepare__ for ordered class dicts"
  ],
  "knowledge_refs": [
    "python/py-20-metaprogramming"
  ],
  "prerequisites": [
    "PY-10",
    "PY-12"
  ],
  "references": [
    {
      "title": "Python Reference — Data Model",
      "url": "https://docs.python.org/3/reference/datamodel.html#metaclasses"
    },
    {
      "title": "Real Python — Metaclasses",
      "url": "https://realpython.com/python-metaclasses/"
    },
    {
      "title": "Real Python — Descriptors",
      "url": "https://realpython.com/python-descriptors/"
    }
  ]
}
---

# PY-20-METAPROGRAMMING: Metaprogramming: Metaclasses and Descriptors

## Introduction

Metaprogramming writes code that manipulates other code. Metaclasses (the type of classes) control class creation. Descriptors control attribute access. These are advanced topics for library/framework authors.

## Key Concepts

### 1. Metaclasses: type and __new__

type is the default metaclass. A custom metaclass inherits from type and overrides __new__ or __init__. Metaclasses run when the class statement completes. Use for class validation, registration, or API generation.

```python
class ValidatedMeta(type):
    def __new__(mcs, name, bases, namespace):
        # validate class definition
        if "process" not in namespace:
            raise TypeError(f"{name} must define process()")
        return super().__new__(mcs, name, bases, namespace)

class Base(metaclass=ValidatedMeta):
    def process(self):
        pass  # OK

# class Bad(metaclass=ValidatedMeta):
#     pass  # TypeError! no process()
```

### 2. __init_subclass__ — Subclass Registration

__init_subclass__ (3.6+) runs when a subclass is created. Simpler than metaclasses for common cases. Automatically registers subclasses. Pass keyword arguments to customize.

```python
class PluginBase:
    _plugins = {}

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if name:
            PluginBase._plugins[name] = cls

class EmailPlugin(PluginBase, name="email"):
    def send(self, msg):
        print(f"Email: {msg}")

class SMSPlugin(PluginBase, name="sms"):
    def send(self, msg):
        print(f"SMS: {msg}")

print(PluginBase._plugins)  # {"email": EmailPlugin, "sms": SMSPlugin}
```

### 3. Descriptors: __get__ and __set__

A descriptor is an object that implements __get__, __set__, or __delete__. Property, classmethod, staticmethod are built-in descriptors. Custom descriptors manage attribute access logic.

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return getattr(obj, self._name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        setattr(obj, self._name, value)

class Order:
    quantity = PositiveNumber()
    price = PositiveNumber()

o = Order()
o.quantity = 5    # OK
# o.quantity = -1  # ValueError
```

### 4. __prepare__ — Ordered Namespace

__prepare__ returns the namespace dict used during class body execution. Use an OrderedDict to preserve class attribute order (3.6+ dicts maintain insertion order anyway).

```python
from collections import OrderedDict

class OrderedMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()  # preserves declaration order

    def __new__(mcs, name, bases, namespace):
        namespace["_order"] = list(namespace.keys())
        return super().__new__(mcs, name, bases, namespace)

class Field(metaclass=OrderedMeta):
    name = "first"
    email = "second"
    age = "third"

print(Field._order)  # ["__module__", "__qualname__", "name", "email", "age"]
```

## Practice Questions

1. What is a metaclass? What is the default metaclass in Python?
1. How does __init_subclass__ differ from a metaclass?
1. What is a descriptor? How does @property use descriptors?
1. What does __set_name__ do in a descriptor?

## LLM Prompts for Deeper Understanding

1. "Explain metaclasses: type, __new__, __init__, __prepare__"
1. "Show __init_subclass__ for plugin registration and subclass tracking"
1. "Teach descriptors: __get__, __set__, __delete__, __set_name__"

## Key Takeaways

- Metaclasses (type subclasses) control class creation
- __init_subclass__ is simpler than metaclasses for subclass tracking
- Descriptors (__get__/__set__) manage attribute access logic