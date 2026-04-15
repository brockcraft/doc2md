# doc2md

## What this is (in plain English)

**doc2md** is a small command-line tool that turns a Word document (a `.docx` file) into a **Markdown** text file (a `.md` file). Markdown is easy to read, works well in editors and on GitHub, and is handy for notes, documentation, and moving content out of Word.

It can also pull **images** out of the document and save them into an `images` folder next to your new `.md` file.

You run it from **Terminal** (the command-line app on your Mac). You do not need to know programming to use it once it is set up.

---

## What you need first

1. **A Mac** (these instructions assume macOS and the default shell, **zsh**).
2. **Python 3** — usually already installed. Check by opening Terminal and typing:

   ```bash
   python3 --version
   ```

   You should see something like `Python 3.11` or newer. If not, install Python from [python.org](https://www.python.org/downloads/) or with Homebrew.

3. **Pandoc** — the engine that actually converts the file. Easiest on a Mac with [Homebrew](https://brew.sh/):

   ```bash
   brew install pandoc
   ```

4. **This project’s folder** on your computer — for example after you clone or download the repo, you might have:

   `doc2md.py` sitting in a folder named `doc2md`.

---

## Install the Python piece (one time)

In Terminal, **go into the folder** that contains `doc2md.py` and `requirements.txt`:

```bash
cd /path/to/doc2md
```

Replace `/path/to/doc2md` with your real folder path (see “Find your folder path” below).

Then install the Python helper library:

```bash
python3 -m pip install -r requirements.txt
```

If that complains about permissions, try:

```bash
python3 -m pip install --user -r requirements.txt
```

---

## How to use it (after setup below)

Open Terminal, go to any folder that has your Word file (or stay anywhere if you use full paths to the files).

**Convert one file** — creates `MyReport.md` next to `MyReport.docx`:

```bash
doc2md.py MyReport.docx
```

**Choose a different output name or folder:**

```bash
doc2md.py MyReport.docx ~/Desktop/MyReport.md
```

**See built-in help:**

```bash
doc2md.py -h
```

After a successful run, Terminal prints where it read the file, where it wrote the `.md`, and where it put images.

---

## “Install” it so `doc2md.py` works from any folder

Right now, your Mac only knows how to run commands that live in certain **special folders** listed in an environment variable called **`PATH`**. If `doc2md` is not in one of those folders, you would have to `cd` into the project every time and type something like `python3 doc2md.py ...`, which is easy to mess up.

You want to be able to open Terminal, type **`doc2md.py`**, and have it work **no matter which folder you are in**. To do that, add the folder that **contains** `doc2md.py` to your `PATH`, once.

### Step 1: Find the full path to the `doc2md` folder

**Option A — from Terminal (after you `cd` into the folder):**

```bash
pwd
```

Copy the line it prints (for example `/Users/yourname/Documents/Code/Scripts/doc2md`). That is the path you need.

**Option B — from Finder:**

1. Open the folder that contains `doc2md.py`.
2. **Control-click** the folder icon in the title bar of the window (or the folder in the sidebar).
3. Hold the **Option (⌥)** key — **“Copy … as Pathname”** appears — click it. You now have the full path on the clipboard.

### Step 2: Add that folder to your PATH (one time)

1. Open Terminal.
2. Open your zsh config file in an editor. Nano is simple:

   ```bash
   nano ~/.zshrc
   ```

3. Use the arrow keys to go to the **bottom** of the file.
4. Paste **this line**, but replace `/path/to/doc2md` with the **exact** path you copied (no quotes inside the path unless your path has spaces — if it has spaces, keep the double quotes as shown):

   ```bash
   export PATH="/path/to/doc2md:$PATH"
   ```

   Example if your project lives in your home folder:

   ```bash
   export PATH="$HOME/Documents/Code/Scripts/doc2md:$PATH"
   ```

5. In nano: press **Control+O**, Enter, then **Control+X** to save and exit.

6. Load the new setting **in this Terminal window**:

   ```bash
   source ~/.zshrc
   ```

7. **Open a new Terminal tab or window** and try:

   ```bash
   which doc2md.py
   ```

   You should see a path ending in `doc2md.py`. If you do, you are done.

### Step 3: Use the right command name

- **Good:** `doc2md.py MyFile.docx` — the shell finds the script because of `PATH`.
- **Avoid:** `python3 doc2md.py` from a random folder — Python looks for `doc2md.py` **only in the folder you are standing in**, not in `PATH`, so you get “can’t open file” errors unless you pass the full path to the script.

---

## Quick checks if something fails

| What you see | What to try |
|--------------|-------------|
| `command not found: doc2md.py` | Run `source ~/.zshrc`, open a new Terminal, run `which doc2md.py`. If still empty, fix the path in `~/.zshrc` (typo or wrong folder). |
| `not a file or does not exist` | The **Word file path** is wrong. `cd` to the folder with the `.docx` or use the full path: `doc2md.py /full/path/to/file.docx`. |
| Errors about **pandoc** | Install Pandoc (`brew install pandoc`) and run `pandoc --version` to confirm it works. |
| Errors about **pypandoc** | Run `python3 -m pip install -r requirements.txt` again from the `doc2md` project folder. |

---

## Technical note (for the curious)

Conversion is done with [Pandoc](https://pandoc.org/). This project talks to Pandoc through [pypandoc](https://github.com/JessicaTegner/pypandoc).
