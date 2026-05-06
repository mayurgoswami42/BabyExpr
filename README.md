# BabyExpr 🍼

**A tiny arithmetic expression interpreter built from scratch in Python — no external libraries, no parser generators.**

BabyExpr was created as a practical exercise to understand Abstract Syntax Trees (ASTs), recursive parsing, and evaluation, while also being a personal milestone: **finishing a self‑imposed project without quitting halfway**.

---

## 🚀 What It Does

- Evaluates arithmetic expressions with correct operator precedence (`* /` before `+ -`)
- Supports parentheses for grouping `(1 + 2) * 3`
- Handles variables and assignment: `x = 5`, `y = x * 2`
- Interactive Read‑Eval‑Print Loop (REPL)
- Clear error messages for:
  - Division by zero
  - Undefined variables
  - Syntax errors (missing operands, bad expressions)

---

## 🧠 Why It Exists

I used to have a pattern of starting projects and abandoning them in the middle. BabyExpr was deliberately scoped to be **completable** — small enough to finish in a few days, yet deep enough to teach:

- How a **lexer** turns raw text into tokens
- How a **parser** builds an **Abstract Syntax Tree** from a flat token list
- How an **evaluator** walks that tree to compute a result
- How variable **scoping / symbol tables** work internally

All of this is implemented **by hand**, following only the rules of the language — no `dataclasses`, no `typing`, no third‑party libraries.

---

## 📦 Installation

You only need **Python 3.6+**.  
Clone the repository and run the REPL:

```bash
git clone https://github.com/mayurgoswami42/BabyExpr.git
cd BabyExpr
python main.py