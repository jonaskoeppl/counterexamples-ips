# Contributing

## Adding an entry

1. Open an issue stating the question, or pick one from `problems/`.
2. Copy `templates/` to `entries/NNNN-short-slug/` (next free number, short descriptive slug).
3. Fill in `question.md`. Add raw AI outputs to `raw/`, one file per run, named `YYYY-MM-DD_model-name.md`.
4. Add a row to the index in `entries/README.md`.
5. Once the digest is `plausible` or `verified`, add a PDF version as `pdf/NNNN-short-slug.pdf` (see `pdf/README.md`).
6. If the entry comes from a file in `problems/`, link the entry there.

## Rules

- **Raw outputs are verbatim.** Never edit them; put corrections and comments in `digest.md`.
- **Declare AI involvement** in every digest.
- **Review:** a digest may be marked `verified` only after someone other than its author has checked it in full.
- **Refuted attempts stay.** Mark them `refuted` and explain the error.
- **Cite precisely:** book, chapter, theorem number, or paper with page.
- Notation follows Liggett (1985) unless stated otherwise.
- Code goes in `entries/NNNN-…/code/` and should run from a fresh checkout.
