# doc2md

Convert documents (for example `.docx`) to Markdown with [Pandoc](https://pandoc.org/), via [pypandoc](https://github.com/JessicaTegner/pypandoc).

## Requirements

- Python 3
- [Pandoc](https://pandoc.org/installing.html) on your `PATH` (macOS: `brew install pandoc`)

## Install

```bash
pip install -r requirements.txt
```

Optional: put this directory on your `PATH` and run `doc2md.py` from anywhere.

## Usage

```bash
./doc2md.py report.docx              # writes report.md next to the input
./doc2md.py report.docx out/notes.md # explicit output path
```

Embedded media is written to an `images` folder beside the output Markdown file.
