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

This script checks if `VIRTUAL_ENV` is set.

- If you are **not** in a virtual environment, it shows warning messages and activation instructions.
- If you are in a virtual environment, it prints environment information and the package install path.

### How to run

```bash
cd ex0
python3 construct.py
```

---

## Exercise 01 - Loading Programs (`ex01/loading.py`)

### What this task does

This script does two things:

1. Checks if required packages are installed:
	- `pandas`
	- `numpy`
	- `matplotlib`
	- `requests`
2. Generates random data, performs a simple analysis, and saves output.

If plotting works, it creates:

- `matrix_analysis.png`

If plotting fails, it creates a text summary file instead.

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

This script validates your runtime setup in multiple steps:

1. Checks if you are inside a virtual environment.
2. Checks if required library is installed (`python-dotenv`).
3. Loads required environment variables from `.env`.
4. Validates allowed values for mode and log level.

If everything is correct, it prints a successful configuration message.

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

- `MATRIX_MODE`: `production`, `development`, `testing`
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