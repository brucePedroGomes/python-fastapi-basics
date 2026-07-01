# Python FastAPI Basics

A small FastAPI project that shows the most common FastAPI features:

- path operations with `GET` and `POST`
- request and response models with Pydantic
- automatic validation from Python type hints
- dependency injection with `Depends`
- custom HTTP middleware
- CORS middleware
- custom exception handling
- automatic OpenAPI docs
- tests with `TestClient`

## Requirements

- Python 3.10+

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:

- API: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc docs: http://127.0.0.1:8000/redoc

## Test

```bash
pytest
```

## Main Files

- `app/main.py`: creates the FastAPI app, middleware, exception handler, and root routes.
- `app/routers/items.py`: keeps item routes separate from the main app.
- `app/schemas.py`: defines Pydantic models for input and output data.
- `app/dependencies.py`: shows reusable dependencies.
- `tests/test_main.py`: tests the API with FastAPI `TestClient`.

## Useful FastAPI Ideas

FastAPI uses normal Python type hints to validate requests and document your API.
If a request body, path parameter, or query parameter has the wrong type, FastAPI
returns a clear validation error.

Middleware runs before and after each request. In this project, the custom
middleware adds an `X-Process-Time` response header.

Dependencies let you share logic between routes. In this project, the
`get_api_version` dependency is used by item routes.

FastAPI creates OpenAPI documentation automatically. You can see and test the API
from `/docs` without writing extra documentation code.
