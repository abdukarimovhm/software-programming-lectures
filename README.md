# Software Programming (IGS1931) — Lectures

Public lecture materials for *Software Programming* (IGS1931), Inha University.

This repo holds **Thursday lecture** notebooks only — no labs, no solution
keys. One folder per week, e.g. `week02-functions/`. Each notebook is
meant to be opened and run in Google Colab during its own class, then
continued locally afterward.

## Lectures

| Week | Topic | Notebook |
|---|---|---|
| Week 2 | Functions — From Repetition to Reuse | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abdukarimovhm/software-programming-lectures/blob/main/week02-functions/functions_intro_student.ipynb) |

## Getting a Working Copy

Pick whichever fits your machine.

### Option A — Google Colab (fastest, works on shared lab PCs)

Running code in Colab requires signing into a Google account. On a shared
lab PC, don't sign into your personal or student account in the regular
browser window — use an incognito/private window instead, so nothing
stays logged in for the next person:

1. Open a new **Incognito/Private window** (Ctrl+Shift+N / Cmd+Shift+N).
2. Sign in with your **student email** — just for this session.
3. Click the Colab badge above for the notebook you need.
4. Immediately do **File → Save a copy in Drive**. That creates your own
   private, editable copy — editing the shared link directly will
   conflict with everyone else opening the same one.
5. When you're done, sign out of the Google account and close the
   incognito window.

### Option B — Clone the whole repo

```bash
git clone https://github.com/abdukarimovhm/software-programming-lectures.git
```

### Option C — Download just the one file you need

On GitHub, open the week's folder → open the `.ipynb` file → click the
**Download raw file** button (the down-arrow icon above the file), or
right-click the "Raw" link and choose "Save Link As…".

Once you have the file (Option B or C), skip to **Running Locally** below.

## Running Locally (VS Code / PyCharm + venv)

Once you're past the first Colab session for a topic, work locally instead:

1. **Get the files** — see **Getting a Working Copy** above (Option B or C).
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
