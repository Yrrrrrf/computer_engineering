# [FastAPI](https://fastapi.tiangolo.com/)

Is a modern, fast (high-performance), web framework for building [[application programming interface|APIs]] with Python 3.6+ based on standard [[python]] type hints.

Is able to create [[REST]] APIs.

## Installation

```bash
pip install fastapi
```

## Usage

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)