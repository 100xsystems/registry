---
{
  "title": "Classes and Object-Oriented Programming",
  "description": "Define classes with __init__, methods, properties",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes with __init__, methods, properties",
    "Use inheritance, super(), and MRO",
    "Write @property decorators and descriptors",
    "Implement dunder methods for operator overloading"
  ],
  "knowledge_refs": [
    "python/py-10-classes-oop"
  ],
  "prerequisites": [
    "PY-04"
  ],
  "references": [
    {
      "title": "Python Tutorial — Classes",
      "url": "https://docs.python.org/3/tutorial/classes.html"
    },
    {
      "title": "Python Reference — Data Model",
      "url": "https://docs.python.org/3/reference/datamodel.html"
    },
    {
      "title": "Real Python — Classes",
      "url": "https://realpython.com/python3-object-oriented-programming/"
    },
    {
      "title": "Real Python — Property",
      "url": "https://realpython.com/python-property/"
    }
  ]
}
---

# PY-10-CLASSES-OOP: Classes and Object-Oriented Programming

## Introduction

Python OOP uses classes, inheritance, and duck typing. The data model (dunder methods) lets custom objects behave like built-in types. Properties provide controlled attribute access.

## Key Concepts

### 1. Classes and __init__

class defines a type. __init__ initializes instances. self is the instance reference (explicit parameter). Instance vs class vs static methods use different decorators.

```python
class User:
    # class variable — shared by all instances
    role = "user"

    def __init__(self, name: str, age: int):
        self.name = name        # instance variable
        self.age = age

    def greet(self) -> str:
        return f"Hi, I am {self.name}"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

    @staticmethod
    def validate_name(name):
        return len(name) >= 2

alice = User("Alice", 30)
print(alice.greet())
bob = User.from_dict({"name": "Bob", "age": 25})
```

### 2. Inheritance and MRO

Python supports multiple inheritance. Method Resolution Order (MRO) uses C3 linearization. super() delegates to the next class in MRO. Use __mro__ to inspect order.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # delegates to Person
        self.emp_id = emp_id

# Multiple inheritance
class Manager(Employee, Person):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

# MRO order
print(Manager.__mro__)
# Manager -> Employee -> Person -> object
```

### 3. @property and Descriptors

Property decorator creates computed attributes with getter/setter/deleter. Descriptors (__get__, __set__) provide reusable attribute behavior. Use __slots__ for memory optimization.

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(100)
print(t.fahrenheit)  # 212
t.celsius = 0
print(t.fahrenheit)  # 32
```

### 4. Dunder Methods (Operator Overloading)

Special methods let objects integrate with Python operators. __str__, __repr__, __len__, __getitem__, __iter__, __enter__/__exit__, __call__, comparison methods.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __bool__(self):
        return self.x != 0 or self.y != 0

v = Vector(3, 4)
print(v + Vector(1, 2))  # Vector(4, 6)
print(v * 3)            # Vector(9, 12)
print(abs(v))           # 5.0
```

### 5. Dataclasses (3.7+)

@dataclass auto-generates __init__, __repr__, __eq__, and more. Use frozen=True for immutability. field() for defaults. __post_init__ for validation.

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: list = field(default_factory=list)

    @property
    def total_value(self):
        return self.price * self.quantity

p = Product("Widget", 9.99, 100)
print(p)           # auto __repr__
print(p == Product("Widget", 9.99, 100))  # auto __eq__
```

## Practice Questions

1. What is the difference between @classmethod and @staticmethod?
1. How does super() work with multiple inheritance?
1. What does @property do? How do you make a setter?
1. What dunder methods would you implement to make a class iterable?

## LLM Prompts for Deeper Understanding

1. "Explain Python MRO (C3 linearization) with multiple inheritance diagrams"
1. "Show property decorators, descriptors, and __slots__ patterns"
1. "Teach dataclasses with field(), frozen, __post_init__"

## Key Takeaways

- class defines types; __init__ initializes; self is the instance
- super() delegates to next class in MRO chain
- @dataclass auto-generates __init__, __repr__, __eq__