"""Shared parser for entry 0004: reads the rate table and the data of the counterexample
from the LaTeX source in ../raw/ (exact rationals)."""
import re
from fractions import Fraction as F
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / 'raw' / '2026-09-07_chatgpt-astra-6.tex'

STATES = [(a, b) for a in range(3) for b in range(3)]   # pair (a, b) has index 3a + b
PI_A = (F(23, 100), F(14, 100), F(63, 100))
PI_B = (F(19, 100), F(31, 100), F(1, 2))
V_A = (F(-45787, 3680), F(87917, 100000), F(434699, 100000))
V_B = (F(-12245721, 950000), F(44491, 50000), F(21733, 5000))


def _cell(c):
    c = c.strip()
    if c in ('--', '-'):
        return None
    neg = c.lstrip('$').startswith('-')
    m = re.search(r'\\frac\{(\d+)\}\{(\d+)\}', c)
    v = F(int(m.group(1)), int(m.group(2))) if m else F(re.sub(r'[^0-9/]', '', c))
    return -v if neg else v


def table(label, path=RAW):
    src = Path(path).read_text()
    i = src.index(r'\label{' + label + '}')
    body = src[src.index(r'\midrule', i):src.index(r'\bottomrule', i)]
    rows = []
    for line in body.split('\n')[1:]:
        line = line.strip().rstrip('\\').strip()
        if line:
            rows.append([_cell(c) for c in line.split('&')[1:]])
    return rows


def rates(path=RAW):
    """9x9 matrix Q of off-diagonal pair-transition rates (None on the diagonal)."""
    Q = table('tab:Q', path)
    assert len(Q) == 9 and all(len(r) == 9 for r in Q)
    return Q


def h(Q, pi, a, b):
    """Adjoint defect h_pi(a, b) of the edge generator relative to the pair-product law."""
    i = 3 * a + b
    inflow = sum(pi[c] * pi[d] * Q[3 * c + d][i] for (c, d) in STATES if (c, d) != (a, b))
    outflow = sum(Q[i][3 * c + d] for (c, d) in STATES if (c, d) != (a, b))
    return inflow / (pi[a] * pi[b]) - outflow
