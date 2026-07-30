---
title: "Classes and Object-Oriented Programming"
description: "Class definitions, inheritance, polymorphism, special methods, dataclasses, and OOP design patterns."
type: lesson
order: 10
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Define classes with constructors and methods"\n  - "Implement inheritance and multiple inheritance"\n  - "Use special methods for operator overloading"\n  - "Simplify with dataclasses"
knowledge_refs:
  - python/py-10-classes-oop
prerequisites:
  - "PY-04"
references:
    - title: "Python Tutorial — 9. Classes"\n      url: "https://docs.python.org/3/tutorial/classes.html"\n    - title: "Fluent Python — Ch. 11: A Pythonic Object"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"\n    - title: "Python Reference — Data Model"\n      url: "https://docs.python.org/3/reference/datamodel.html"
---

# PY-10-CLASSES-OOP: Classes and Object-Oriented Programming


## Class Basics

See [Classes Tutorial](https://docs.python.org/3/tutorial/classes.html):
```python
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name: str, age: int):
        self.name = name  # Instance variable
        self.age = age
    
    def bark(self) -> str:
        return f"{self.name} says Woof!"

rex = Dog("Rex", 3)
print(rex.bark())  # Rex says Woof!
```

## Inheritance

```python
class Poodle(Dog):
    def __init__(self, name, age, cuteness=10):
        super().__init__(name, age)
        self.cuteness = cuteness
    
    def bark(self) -> str:
        return f"{self.name} says Yip! ✨"
```

## Special Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self): return f"Vector({self.x}, {self.y})"
    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other): return self.x == other.x and self.y == other.y

v1 = Vector(1, 2); v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

## Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""
```

