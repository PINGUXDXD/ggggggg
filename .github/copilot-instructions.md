# Copilot Instructions

## Overview

This repository consists of standalone Python scripts, each in the project root. There is no package structure, build system, or automated test harness. The primary workflow is to run scripts individually using Python 3.10+ (required for `match/case` syntax in several files).

## Key Patterns & Structure

- **Scripts are independent:** Each `.py` file is a self-contained CLI program, often menu-driven and interactive, with Spanish-language prompts and output.
- **No external dependencies:** Only the Python standard library is used. Do not add third-party packages or a `requirements.txt`.
- **Entrypoint conventions:** Most scripts are run directly (e.g., `python calculadora.py`). Some use `if __name__ == "__main__":` for entry, as in [calculadora.py](../../calculadora.py).
- **Error handling:** See [ayuda.py](../../ayuda.py) for the preferred pattern—handle `ValueError`, `EOFError`, `IndexError`, and generic `Exception` separately for user input.
- **Menu loops:** Many scripts use `while True:` loops for repeated menu input (see [calculadora.py](../../calculadora.py), [troll.py](../../troll.py)).
- **Function modularity:** [funciones.py](../../funciones.py) contains commented-out modular examples; new logic should be similarly decomposed when possible, but keep interactive code in the main script.
- **Spanish UI:** All prompts, menus, and output should remain in Spanish. Preserve this style in all updates.

## Developer Workflows

- **Manual execution:** Run scripts directly, e.g.:
  - `python calculadora.py`
  - `python ayuda.py`
  - `python <script>.py`
- **No automated tests:** Validation is manual—run the script and check its behavior.
- **Debugging:** Fix syntax/runtime errors in place. Scripts like [OMG.py](../../OMG.py) and [balatro.py](../../balatro.py) have known issues (e.g., misuse of `print` return value, typos in `random.randit`).

## Editing Guidelines

- **No package structure:** Do not create subfolders or modules unless absolutely necessary. All scripts should remain in the root.
- **Add new files only for standalone scripts or clear utility modules.**
- **Preserve interactive CLI style and Spanish prompts.**
- **Do not add external dependencies.**
- **If a script is incomplete or buggy, note this in the change summary and avoid large refactors without confirmation.**

## Examples

- [calculadora.py](../../calculadora.py): Stable, menu-driven calculator with function entrypoint.
- [ayuda.py](../../ayuda.py): Shows robust input error handling.
- [funciones.py](../../funciones.py): Example of modular function decomposition (commented out).

## When in Doubt

- Match the style: simple, procedural, interactive scripts with Spanish UI.
- Use direct file examples for reference.
- Ask for clarification before making broad changes to incomplete scripts.
