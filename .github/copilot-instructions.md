# Copilot Instructions

- This repository is a set of standalone Python scripts, not a packaged application. Most logic lives in root files like `calculadora.py`, `ayuda.py`, `troll.py`, `matenme.py`, `GG.py`, `OMG.py`, and `balatriño.py`.
- There is no CI/test harness, no `requirements.txt`, and no build system. The expected workflow is manual execution with Python.
- Use Python 3.10+ because several scripts use `match/case` syntax (`calculadora.py`, `troll.py`, `OMGg.py`, etc.).
- Run individual scripts with:
  - `python calculadora.py`
  - `python ayuda.py`
  - `python <script>.py`
- Prefer preserving existing interactive Spanish UI style and prompt text when updating scripts.

## Codebase patterns

- Many files are menu-driven CLI exercises with `while True:` loops and user input.
- `calculadora.py` is the most complete example of a stable script: it uses a named function and `if __name__ == "__main__":` for entry.
- `ayuda.py` shows the preferred error-handling pattern for user input: separate `ValueError`, `EOFError`, `IndexError`, and generic `Exception` branches.
- `funciones.py` contains commented-out examples of modular operation functions; new logic should follow that decomposed style when appropriate.

## Key points for editing

- Do not assume a package structure. Add new files only if they are standalone scripts or clearly needed utility modules.
- Keep the root directory as the main project surface.
- Fix syntax/runtime issues in place when they are obvious, especially in interactive scripts.
- Be cautious with scripts that appear incomplete or buggy, for example:
  - `OMG.py` uses `select=int(print("seleccione una fruta: "))`, which returns `None`.
  - `balatro.py` has `random.randit` and invalid numeric literal syntax.
- Avoid adding external dependencies; the repository currently uses only Python standard library features.

## Workflows

- No tests to run; validation is typically manual by executing the script and checking its menu/input behavior.
- When adding new logic, favor a simple function entrypoint and preserve the Spanish prompts/menu labels.
- If a script is converted to a reusable module, keep the original interactive behavior separated from the function definitions.

## When in doubt

- Match the repository’s existing style: simple procedural scripts, Spanish prompts, and interactive command-line menus.
- Use direct file examples rather than generic advice.
- If a script is clearly incomplete, note that in the change summary and avoid broad refactors without user confirmation.
