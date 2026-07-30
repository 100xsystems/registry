---
title: "Working with JSON, CSV, and APIs"
description: "JSON handling, CSV processing, REST APIs with requests, data validation, and pipeline patterns."
type: lesson
order: 16
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Read/write JSON and CSV"\n  - "Consume REST APIs with requests"\n  - "Validate data with dataclasses"\n  - "Build data processing pipelines"
knowledge_refs:
  - python/py-16-data-apis
prerequisites:
  - "PY-08"
references:
    - title: "Python Docs — json"\n      url: "https://docs.python.org/3/library/json.html"\n    - title: "Python Docs — csv"\n      url: "https://docs.python.org/3/library/csv.html"\n    - title: "Real Python — Python requests"\n      url: "https://realpython.com/python-requests/"
---

# PY-16-DATA-APIS: Working with JSON, CSV, and APIs


## JSON

```python
import json
data = '{"name": "Alice", "age": 30}'
parsed = json.loads(data)
print(json.dumps(parsed, indent=2))
```

## CSV

```python
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
```

## Requests

```python
import requests
resp = requests.get("https://api.github.com/users/python")
if resp.status_code == 200:
    data = resp.json()
    print(data["public_repos"])
```

