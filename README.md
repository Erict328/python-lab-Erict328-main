# Python Lab

This lab will give you practice with some basic Python features to prepare you for the rest of the assignments this semester.

### Data

The data used for this app can be found in `app/data.py`. You can reference this file during development to see the structure of the data.

## Getting started

Clone the repository and install dependencies with `uv`:

```bash
git clone https://github.com/uwf-cen3031-fa2025/python-lab-your_username
cd python-lab-your_username
uv sync  # Install dependencies into a virtual environment
```

## Running problems

From the project root (the folder with `pyproject.toml` and the `app/` directory), run:

```bash
# Run all problems (default)
uv run python -m app.main

# Run a single problem
uv run python -m app.main 1

# Run multiple problems
uv run python -m app.main 2 4

# Run the bonus problem
uv run python -m app.main bonus
```

If you run without any arguments, it will execute **all problems** by default.

## Checking your work

Use `pytest` to check your solutions against the provided tests:

```bash
uv run pytest
```
## Why use uv run?

Prefacing commands with uv run ensures they run inside the project’s virtual environment:

* You don’t need to activate ```.venv``` manually.

* All dependencies installed with ```uv sync``` are automatically available.

* Commands like ```python``` and ```pytest``` always use the correct versions for this project. 
This keeps your setup consistent.