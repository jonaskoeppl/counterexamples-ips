# PDF versions

Compiled PDF versions of the counterexamples, one file per entry, for reading and printing.

- File name: `NNNN-short-slug.pdf`, matching the entry folder in `entries/`.
- Content: the entry's `digest.md` (or its LaTeX write-up, if there is one), typeset with the question at the top.
- Only add a PDF once the digest has status `plausible` or `verified`. Note the status on the first page.
- When a digest changes, regenerate its PDF in the same commit, so that the two never disagree.

`overview.pdf` (source: `overview.tex`) collects all entries, with one paragraph on each question and links to the full write-ups. Add each new entry to `overview.tex` and rebuild it with `pdflatex overview.tex`.

The Markdown/LaTeX sources in `entries/` are authoritative; the files here are derived from them.
