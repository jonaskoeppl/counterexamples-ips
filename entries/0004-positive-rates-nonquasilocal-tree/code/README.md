# Code for entry 0004

All scripts read the rate table from `../raw/2026-09-07_chatgpt-astra-6.tex` (the raw output). Run them from this folder.

| Script | What it does | Needs |
|---|---|---|
| `verify.py` | Exact-arithmetic audit: positivity and minimum of the 72 rates, the two mean-zero identities, the 18 balance identities $h_\pi(a,b) = v(b) - 2v(a)$, and agreement with the printed $h$-tables. | Python 3 (standard library) |
| `check_stationarity.py` | Independent brute-force check that $\int \mathscr{L} f\, d\nu = 0$ for both product measures and all functions $f$ of four neighbouring sites; a non-stationary product measure is included as a control. | numpy |
| `lp_tree_vs_line.py` | Heuristic experiment: for random pairs $(\pi^A, \pi^B)$, are there positive rates making both product measures balanced? Tree balance: almost always yes; line balance: never. | numpy, scipy |
| `tree_model.py` | Shared parser and the definition of $h_\pi$. | — |
