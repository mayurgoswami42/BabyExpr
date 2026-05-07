# BabyExpr 🍼

**A tiny arithmetic expression interpreter built from scratch in Python — zero dependencies, no parser generators.**

BabyExpr is a minimal but complete interpreter for arithmetic expressions with variables. It's a hands-on exploration of how programming languages are parsed and executed, implemented in pure, readable Python.

---

## 🚀 Features

- Infix arithmetic with correct operator precedence (`* /` before `+ -`)
- Parentheses grouping `(1 + 2) * 3`
- Variables and assignment `x = 5`, `y = x * 2`
- Float and integer number literals
- Interactive Read‑Eval‑Print Loop (REPL)
- Clear, non‑crashing error handling for:
  - Division by zero
  - Undefined variables
  - Syntax errors (missing operands, unknown operators, unmatched parentheses)

---

## 🧠 Learning Goals

BabyExpr was built from scratch to deeply understand:

- **Lexical analysis** – turning raw text into tokens
- **Parsing** – building an Abstract Syntax Tree (AST) using recursive descent with precedence
- **Tree evaluation** – walking the AST and computing results
- **Symbol tables** – storing and looking up variables

No external parsing libraries or code generators are used — everything is hand‑written.

---

## 📦 Installation

Requires **Python 3.6+**. No additional packages needed.

```bash
git clone https://github.com/mayurgoswami42/BabyExpr.git
cd BabyExpr
python main.py