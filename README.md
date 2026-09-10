# Software Programming (IGS1931) — Lectures

Public lecture materials for *Software Programming* (IGS1931), Inha University.

This repo holds **Thursday lecture** notebooks only — no labs, no solution
keys. One folder per week, e.g. `week02-functions/`. Each notebook is
meant to be opened and run in Google Colab during its own class.

**Before you edit anything in Colab:** click the Colab badge below, then
immediately do **File → Save a copy in Drive**. That gives you your own
private copy to work in — editing the shared version directly will
conflict with everyone else opening the same link.

Starting the following class, download the notebook (or `git clone` this
repo) and continue the exercises locally using PyCharm or VS Code — see
**Running Locally** below.

## Lectures

| Week | Topic | Notebook |
|---|---|---|
| Week 2 | Functions — From Repetition to Reuse | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abdukarimovhm/software-programming-lectures/blob/main/week02-functions/functions_intro_student.ipynb) |

## Running Locally (VS Code / PyCharm + venv)

Once you're past the first Colab session for a topic, work locally instead:

1. **Get the files.** Either:
   - `git clone https://github.com/abdukarimovhm/software-programming-lectures.git`, or
   - just download the one notebook you need (its folder → the `.ipynb`
     file → the "Download raw file" button on GitHub).
2. **Create a virtual environment** (once per machine, from the repo
   folder):
   ```bash
   python -m venv venv
   ```
3. **Activate it** — every time you come back to work:
   - macOS/Linux: `source venv/bin/activate`
   - Windows (PowerShell): `venv\Scripts\Activate.ps1`
   - Windows (cmd.exe): `venv\Scripts\activate.bat`
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Open the notebook:**
   - **VS Code:** install the *Python* and *Jupyter* extensions, open the
     repo folder, open the `.ipynb` file, and pick your `venv` as the
     kernel (top-right of the notebook toolbar) before running any cell.
   - **PyCharm (Professional):** open the repo folder as a project, open
     the `.ipynb` file, and set the `venv` you created as the project's
     Python interpreter (Settings → Project → Python Interpreter) before
     running cells. *(PyCharm Community doesn't support `.ipynb` files
     directly — use VS Code or plain Jupyter instead.)*
   - **Plain Jupyter** (any editor): with the venv activated, run
     `jupyter notebook` and open the file from the browser tab it opens.

You only need to repeat steps 2-3 (create/activate) once per machine —
after that, just activate the existing `venv` each session.
