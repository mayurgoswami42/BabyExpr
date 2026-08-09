# Contributing to BabyExpr

First off — thank you for wanting to contribute! BabyExpr is a learning project,
so beginner contributions (even small ones) are very welcome. This guide will
walk you through everything, including if this is your **first ever pull request**.

---

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Getting Started (First Time on GitHub)](#getting-started-first-time-on-github)
- [Development Setup](#development-setup)
- [Code Style Guide](#code-style-guide)
- [Writing Tests](#writing-tests)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Code Review Process](#code-review-process)
- [Code of Conduct](#code-of-conduct)

---

## Ways to Contribute

You don't have to write code to contribute:

- 🐛 **Report bugs** — open an [Issue](../../issues) describing what broke
- 💡 **Suggest features** — open an Issue with the `enhancement` label
- 📝 **Improve documentation** — fix typos, clarify the README, add examples
- ✅ **Add tests** — even one new test case is a valid, welcome PR
- 🔧 **Fix bugs / add features** — see the [Issues](../../issues) tab for
  things labeled `good first issue`

If you're new to open source, look for issues labeled **`good first issue`** —
these are scoped to be small and beginner-friendly.

---

## Getting Started (First Time on GitHub)

If you've never made a pull request before, here's the full process:

1. **Fork the repo** — click the "Fork" button at the top right of the
   [BabyExpr page](https://github.com/mayurgoswami42/BabyExpr). This creates
   your own copy of the project under your GitHub account.

2. **Clone your fork** to your computer:
   ```bash
   git clone https://github.com/<your-username>/BabyExpr.git
   cd BabyExpr
   ```

3. **Create a new branch** for your change — never work directly on `main`:
   ```bash
   git checkout -b fix/division-by-zero-message
   ```
   Use a short, descriptive branch name (see naming convention below).

4. **Make your changes**, then stage and commit them:
   ```bash
   git add .
   git commit -m "fix: improve division by zero error message"
   ```

5. **Push your branch** to your fork:
   ```bash
   git push origin fix/division-by-zero-message
   ```

6. **Open a Pull Request** — go to your fork on GitHub, you'll see a
   "Compare & pull request" button. Click it, fill in the template, and submit.

That's it! A maintainer will review your PR and may ask for changes before
merging — that's normal and part of learning, not a rejection.

### Branch naming convention

| Prefix      | Use for                         | Example                       |
|-------------|----------------------------------|-------------------------------|
| `feature/`  | New features                     | `feature/modulo-operator`     |
| `fix/`      | Bug fixes                        | `fix/negative-number-parsing` |
| `docs/`     | Documentation only               | `docs/update-readme-examples` |
| `test/`     | Adding or fixing tests           | `test/division-by-zero`       |
| `refactor/` | Code cleanup, no behavior change | `refactor/rename-token-types` |

---

## Development Setup

**Requirements:** Python 3.6+, no external packages needed.

```bash
git clone https://github.com/<your-username>/BabyExpr.git
cd BabyExpr
python main.py
```

That's the whole setup — BabyExpr has zero dependencies by design.

---

## Code Style Guide

Consistency matters more than personal preference here. Please follow these
conventions so the codebase stays readable for everyone (especially beginners
reading it to learn):

### Naming conventions

| Element                  | Convention          | Example                          |
|--------------------------|---------------------|----------------------------------|
| Variables                | `snake_case`        | `token_list`, `current_char`     |
| Functions / methods      | `snake_case`        | `def parse_expression():`        |
| Classes                  | `PascalCase`        | `class Lexer:`, `class TokenType:` |
| Constants                | `UPPER_SNAKE_CASE`  | `MAX_RECURSION_DEPTH = 100`      |
| Private/internal helpers | leading underscore  | `_advance()`, `_peek()`          |

> **Note:** Python's own convention for classes is `PascalCase` (also called
> "UpperCamelCase"), not lowercase `camelCase` — e.g. `class TokenType`, not
> `class tokenType`. This matches standard Python style (PEP 8) and is what
> we use throughout BabyExpr.

### General style rules

- **Indentation:** 4 spaces, no tabs.
- **Line length:** keep under ~100 characters where reasonable.
- **Docstrings:** every public function/class should have a one-line docstring
  explaining what it does:
  ```python
  def tokenize(source: str) -> list:
      """Convert raw source text into a list of tokens."""
      ...
  ```
- **No bare `except:`** — always catch a specific exception
  (`except ZeroDivisionError:`, not `except:`).
- **One statement per line** — avoid semicolons or cramming logic into one line.
- **Avoid magic numbers** — use named constants instead of unexplained literals.
- **Comments explain *why*, not *what*** — the code should already say what
  it does; comments should clarify intent or edge cases.

### Formatting tool (recommended)

We recommend formatting your code with [`black`](https://pypi.org/project/black/)
before committing, so style stays consistent automatically:

```bash
pip install black
black .
```

This isn't strictly required to submit a PR, but it saves review time.

---

## Writing Tests

BabyExpr uses Python's built-in [`unittest`](https://docs.python.org/3/library/unittest.html)
module — no extra install needed.

### Test file layout

```
BabyExpr/
├── main.py
├── utils/
│   └── ...
└── tests/
    ├── __init__.py
    ├── test_lexer.py
    ├── test_parser.py
    └── test_evaluator.py
```

Put tests in the `tests/` folder (create it if it doesn't exist yet), one
file per component you're testing. Name test files `test_<thing>.py` and
test functions `test_<behavior>`.

### Example test

```python
# tests/test_evaluator.py
import unittest
from main import evaluate  # adjust import to match actual module path

class TestEvaluator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate("2 + 3"), 5)

    def test_operator_precedence(self):
        self.assertEqual(evaluate("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate("(2 + 3) * 4"), 20)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("5 / 0")

    def test_variable_assignment(self):
        self.assertEqual(evaluate("x = 5"), 5)
        self.assertEqual(evaluate("x * 2"), 10)

if __name__ == "__main__":
    unittest.main()
```

> Adjust the `import` line to match whatever your `evaluate`/`run` entry
> point is actually called in `main.py`.

### Running tests

Run a single file:
```bash
python -m unittest tests/test_evaluator.py
```

Run the whole test suite:
```bash
python -m unittest discover tests
```

All tests should pass (`OK` at the bottom) before you open a PR. If you're
fixing a bug, ideally add a test that would have caught it.

### What to test

- Normal/expected behavior ("happy path")
- Edge cases (empty input, very large numbers, deeply nested parentheses)
- Error cases (division by zero, undefined variables, syntax errors) — make
  sure the interpreter fails *gracefully*, not with a crash/traceback

---

## Commit Message Guidelines

Use short, present-tense, descriptive messages. Prefixing with a type helps
readability:

```
feat: add support for modulo operator
fix: correct precedence of unary minus
docs: add examples to README
test: add tests for undefined variable errors
refactor: rename Token fields to snake_case
```

---

## Submitting a Pull Request

Before opening a PR, check:

- [ ] Code follows the [style guide](#code-style-guide) above
- [ ] You tested your change manually (`python main.py`)
- [ ] You added/updated tests if you changed behavior
- [ ] All existing tests still pass (`python -m unittest discover tests`)
- [ ] Your PR description explains **what** changed and **why**
- [ ] You linked the related Issue, if any (e.g. `Closes #12`)

Keep PRs small and focused — one feature or fix per PR is much easier to
review than five things bundled together.

---

## Code Review Process

- All contributions are merged via Pull Request — nobody (including
  maintainers) pushes directly to `main`.
- A maintainer will review your PR, possibly leaving comments or requesting
  changes. This is a normal part of the process, not a rejection — treat it
  as a conversation.
- Once approved, a maintainer will merge it. You'll then show up in the
  [Contributors](../../graphs/contributors) list. 🎉

---

## Code of Conduct

Be kind, be patient, and remember most people opening PRs here are learning
GitHub for the first time. Constructive feedback only — no put-downs about
code quality or experience level. Questions are always welcome, in Issues or
PR comments.

---

Thanks again for contributing to BabyExpr! 🚀
