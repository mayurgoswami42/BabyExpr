# BabyExpr

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)
![Dependencies](https://img.shields.io/badge/dependencies-0-success.svg)

**A tiny arithmetic expression interpreter written from scratch in pure Python. No external libraries, no parser generators — just hand‑written lexer, parser, and evaluator.**

BabyExpr is a minimal but fully functional programming language that performs arithmetic operations, respects operator precedence, handles parentheses, and stores variables. It’s designed as a crystal‑clear example of how interpreters work under the hood.

---

## Features

- Infix arithmetic with correct precedence (`* /` before `+ -`)
- Parentheses grouping `(1 + 2) * 3`
- Variables and assignment: `x = 5`, `y = x * 2`
- Support for integer and floating‑point number literals
- Interactive Read‑Eval‑Print Loop (REPL)
- Robust, non‑crashing error handling:
  - Division by zero
  - Undefined variables
  - Syntax errors (missing operands, unknown operators, unmatched parentheses)

---

## Why BabyExpr?

This project was built to deeply understand the internals of programming languages:

- **Lexical analysis** – converting raw text into tokens
- **Recursive descent parsing** – constructing an Abstract Syntax Tree (AST) with operator precedence
- **Tree evaluation** – walking the AST and computing results
- **Symbol tables** – storing and looking up variables

Everything is crafted by hand — no parser generators, no data‑class helpers, zero import dependencies.

---

## Installation

**Requirements:** Python 3.6 or newer. No extra packages.

```bash
git clone https://github.com/mayurgoswami42/BabyExpr.git
cd BabyExpr
python main.py
