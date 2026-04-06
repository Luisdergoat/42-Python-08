## This project has been created as part of the 42 curriculum by lunsold
---

![42 Badge](https://img.shields.io/badge/42-Project-blue)
![Language](https://img.shields.io/badge/Language-python-orange)
# 42-Python-08

Simple exercises about Python environments, dependencies, and configuration checks.

## Project Goal

This repository contains 3 small tasks:

- `ex0`: Check if you are inside a virtual environment.
- `ex01`: Check Python package dependencies and run a small data analysis.
- `ex02`: Validate environment setup and configuration variables.

Each exercise is independent and can be run on its own.

---

## Exercise 00 - Construct (`ex0/construct.py`)

### What this task does

This script checks whether `VIRTUAL_ENV` is set.

- Outside a virtual environment, it prints Matrix-themed warnings and exact activation steps for Unix and Windows.
- Inside a virtual environment, it prints the current interpreter, environment name/path, and the resolved `site-packages` location.

### How to run

```bash
cd ex0
python3 construct.py
```

---

## Exercise 01 - Loading Programs (`ex01/loading.py`)

### What this task does

This script demonstrates dependency loading and a small Matrix data workflow:

1. Checks required packages with versions:
	- `pandas`
	- `numpy`
	- `matplotlib`
	- `requests` is optional and only relevant if you decide to fetch external API data.
2. Shows a clear `pip` vs `Poetry` dependency-management comparison in the program output.
3. Generates Matrix data with `numpy` (1000 points), analyzes it with `pandas`, and renders a plot with `matplotlib`.

On success, it creates:

- `matrix_analysis.png`

If required dependencies are missing, it exits gracefully and shows install instructions for both `pip` and `Poetry`.

### Install dependencies

Use one of these options inside `ex01`:

```bash
pip install -r requirements.txt
```

or

```bash
poetry install
```

### How to run

```bash
cd ex01
python3 loading.py
```

---

## Exercise 02 - Oracle (`ex02/oracle.py`)

### What this task does

This script implements secure configuration loading for local development and production:

1. Loads settings via `python-dotenv` from `.env` (or environment variables).
2. Applies environment-variable overrides over `.env` values.
3. Validates configuration and prints visible differences between `development` and `production` modes.
4. Prints security checks and friendly warnings for missing configuration.

It avoids hardcoded secrets and is designed to work with `.env.example` plus a gitignored real `.env`.

### Required environment variables

Create a `.env` file (for example in `ex02/`) with:

```env
MATRIX_MODE=development
DATABASE_URL=sqlite:///matrix.db
API_KEY=your_key_here
LOG_LEVEL=INFO
ZION_ENDPOINT=https://zion.example/api
```

Allowed values:

- `MATRIX_MODE`: `production`, `development`
- `LOG_LEVEL`: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`

### Install dependency

```bash
pip install python-dotenv
```

### How to run

```bash
cd ex02
python3 oracle.py
```

---

## Recommended Workflow

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate
```

Then run each exercise from its folder.

---

## Summary

- `ex0` teaches virtual environment detection.
- `ex01` teaches dependency checks and simple package usage.
- `ex02` teaches configuration loading and validation.