# doc2md

This is a **command-line tool** that creates a **Markdown** (`.md`) file from a **Word** (`.docx`) file. You run it in **Terminal** from the folder that contains your document (or use full paths). By default it writes a Markdown file with the **same name** as the Word file, in the **same folder**—for example:

```bash
doc2md.py yourwordfile.docx
```

That produces `yourwordfile.md` next to `yourwordfile.docx`. (If you set up the optional `doc2md` symlink, you can run `doc2md` instead.) Simple!

---

## Why doc2md

AI tools work best with **clean, readable text**. A `.docx` may look simple in Word, but underneath it is a busy package: XML, styles, metadata, relationships, numbering rules, and embedded objects. That is fine for editing, but it is a poor fit when you need software to **read, summarize, search, chunk, compare, or transform** the actual content.

**doc2md** exists to turn Word documents into **Markdown**—plain text that still carries what most AI workflows care about: headings, lists, paragraphs, links, tables, and basic structure. For many AI tasks, that makes the material easier to process and easier to reason about.

### Why Markdown helps with AI work

- **Simpler than `.docx`.** You are not asking every tool to reverse-engineer Word’s internals; you get a straightforward text representation that is easier to inspect, store, diff, and pipe into other programs.
- **Often more token-efficient.** Models are billed on the text they process. A solid Markdown export usually drops a lot of formatting noise, so more of the context window goes to real content.
- **Better for chunking and retrieval.** If you use embeddings, RAG, vector search, or anything that splits a document into sections, Markdown makes boundaries clearer—headings and lists are explicit, so splits tend to line up with how humans think about the document.
- **Easier to automate.** Plain text plays nicely with scripts, version control, `grep`, `diff`, and Unix-style pipelines—useful for repeated AI passes, prompt pipelines, and batch jobs.
- **Easier for humans to sanity-check.** If you want to see roughly what an AI is “reading,” Markdown is far friendlier than raw XML or opaque binary formats.

### Why `doc2md.py` specifically

`doc2md.py` is a **small command-line wrapper** around [Pandoc](https://pandoc.org/) so you can convert Word to AI-friendly Markdown without memorizing Pandoc flags.

It is a good fit when you want to:

- prepare documents for summarization or rewriting  
- build a corpus for search or retrieval  
- trim noise before sending content to an LLM  
- inspect document content as plain text  
- produce a cleaner intermediate format for automation  

This project is **not** trying to replace Word. It gives you a **working format** tuned for AI-related tasks.

### A practical way to think about it

Use the **`.docx`** as the file people edit, share, and print.  
Use the **`.md`** as the file systems read, chunk, index, and run agents against.

That split is often the sweet spot: Word for authoring and final layout, Markdown for analysis, transformation, and agent workflows.

### Important limitation

Markdown cannot perfectly represent **every** Word feature. Complex tables, comments, tracked changes, text boxes, floating objects, and layout-heavy pieces may not convert cleanly. When exact formatting or Word-only features matter, keep the original `.docx` as the source of truth.

For many AI-oriented jobs, **clear structure beats pixel-perfect fidelity**. That is the gap `doc2md.py` is meant to fill.

---

## What this tool is (in plain English)

This repo ships **`doc2md.py`**, a script that turns a Word file (`.docx`) into a Markdown file (`.md`). Markdown is also easy to read in editors, diff in Git, and publish on sites like GitHub.

The script pulls **images** out of the document and saves them in an **`images`** folder next to the new `.md` file.

You run it from **Terminal** on your Mac. You do not need to know how to program—only how to follow the setup steps below.

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

## License

**doc2md** (this repository, including `doc2md.py`) is licensed under the **GNU General Public License v2.0 or later** (`GPL-2.0-or-later`). The full license text is in the [`LICENSE`](LICENSE) file in this repo.

That choice matches how **[Pandoc](https://pandoc.org/)** is distributed: Pandoc itself is under the **GPL v2** (and, like other GNU projects, may be used under **GPL v2 or any later version** at your option). This script invokes Pandoc as a separate program on your machine.

**[pypandoc](https://github.com/JessicaTegner/pypandoc)** (the Python library used here) is under the **MIT License**, which is **compatible** with GPLv2+ when combined in this way. pypandoc’s license applies to the pypandoc source you get from PyPI; it does not change the GPL terms for this project’s own code.

This is not legal advice. If you redistribute combined works or have compliance questions, consult a lawyer or your organization’s open-source policy.

---

## Technical note (for the curious)

Conversion is done with [Pandoc](https://pandoc.org/). This project talks to Pandoc through [pypandoc](https://github.com/JessicaTegner/pypandoc).
