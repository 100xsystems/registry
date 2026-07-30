---
{
  "title": "Data Serialization: JSON, CSV, and Pydantic",
  "description": "Serialize/deserialize JSON with json module",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Serialize/deserialize JSON with json module",
    "Read/write CSV files with csv module",
    "Use dataclasses for structured data",
    "Validate data with Pydantic"
  ],
  "knowledge_refs": [
    "python/py-16-data-serialization"
  ],
  "prerequisites": [
    "PY-08",
    "PY-10"
  ],
  "references": [
    {
      "title": "Python Library — json",
      "url": "https://docs.python.org/3/library/json.html"
    },
    {
      "title": "Python Library — csv",
      "url": "https://docs.python.org/3/library/csv.html"
    },
    {
      "title": "Python Library — dataclasses",
      "url": "https://docs.python.org/3/library/dataclasses.html"
    },
    {
      "title": "Pydantic Docs",
      "url": "https://docs.pydantic.dev/"
    }
  ]
}
---

# PY-16-DATA-SERIALIZATION: Data Serialization: JSON, CSV, and Pydantic

## Introduction

Data serialization is critical for APIs, configuration files, and data processing. Python provides json and csv in the standard library. dataclasses define schemas; Pydantic adds validation.

## Key Concepts

### 1. JSON: Serialization and Deserialization

json.dumps() serializes Python objects to JSON strings. json.dump() writes to files. json.loads() parses JSON strings. json.load() reads files. Custom serialization via default parameter.

```python
import json

data = {"name": "Alice", "scores": [85, 92, 78], "active": True}

# serialize
json_str = json.dumps(data, indent=2)
print(json_str)

# deserialize
parsed = json.loads(json_str)
print(parsed["name"])  # Alice

# file I/O
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)

# custom serializer
from datetime import datetime
json.dumps(datetime.now(), default=str)
```

### 2. CSV: Reading and Writing

csv.reader yields rows as lists; csv.DictReader yields dicts. csv.writer writes rows; csv.DictWriter writes from dicts. Handle different delimiters and quoting styles.

```python
import csv

# reading as dicts
with open("users.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["email"])

# writing dicts
with open("output.csv", "w", newline="") as f:
    fields = ["name", "email", "age"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow({"name": "Alice", "email": "a@b.com", "age": 30})

# custom delimiter
reader = csv.reader(f, delimiter="|")
```

### 3. dataclasses for Structured Data

dataclasses auto-generate boilerplate. frozen=True for immutability. field() for default values and metadata. __post_init__ for validation. asdict() and astuple() for conversion.

```python
from dataclasses import dataclass, field, asdict

@dataclass
class User:
    name: str
    email: str
    age: int
    tags: list = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age must be positive")

user = User("Alice", "a@b.com", 30)
print(asdict(user))  # dict for JSON serialization
```

### 4. Pydantic for Validation

Pydantic (third-party) provides runtime validation with type coercion. BaseModel with type-annotated fields. Automatic JSON parsing with model_validate_json(). Custom validators.

```python
from pydantic import BaseModel, EmailStr, Field, field_validator

class User(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str
    age: int = Field(ge=0, le=150)
    tags: list[str] = []

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v.lower()

# automatic parsing from JSON
data = '{"name": "Alice", "email": "A@B.com", "age": 30}'
user = User.model_validate_json(data)
print(user.email)  # a@b.com (lowercased by validator)
```

## Practice Questions

1. Difference between json.dumps and json.dump? json.loads vs json.load?
1. How does csv.DictWriter differ from csv.writer?
1. What does @dataclass auto-generate? How to make it immutable?
1. How does Pydantic differ from dataclasses? When use each?

## LLM Prompts for Deeper Understanding

1. "Explain JSON serialization: dumps/dump/loads/load and custom encoders"
1. "Show CSV reading/writing with DictReader/DictWriter and dialects"
1. "Teach Pydantic vs dataclasses: validation, serialization, use cases"

## Key Takeaways

- json module handles dumps/dump/loads/load with indentation support
- CSV module supports DictReader/DictWriter for labeled columns
- Pydantic adds runtime validation; dataclasses are lightweight schemas