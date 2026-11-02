"""Heuristic experiment for entry 0004: line versus tree.

For two product laws pi^A, pi^B on {0,1,2}, look for pair-update rates Q (all >= 1e-3) such that
both product measures satisfy the balance condition
    tree (one parent, two children):  h_pi(a,b) = v(b) - 2 v(a),  sum_a pi_a v(a) = 0,
    line (one parent, one child):     h_pi(a,b) = v(b) - v(a).
On the line this condition is equivalent to stationarity, and the entropy argument in digest.md
shows it cannot hold for two distinct pi. This is a linear feasibility problem (scipy/HiGHS).

Usage: python3 lp_tree_vs_line.py
"""
import numpy as np
from scipy.optimize import linprog
from itertools import product
states = [(a, b) for a in range(3) for b in range(3)]
offd = [(i, j) for i in range(9) for j in range(9) if i != j]
col = {ij: k for k, ij in enumerate(offd)}
nq = len(offd)

def run(piA, piB, children, eps=1e-3):
    # variables: q (72), vA (3), vB (3)
    n = nq + 6
    Aeq, beq = [], []
    for s, pi in enumerate((piA, piB)):
        for (a, b) in states:
            i = 3 * a + b
            row = np.zeros(n)
            for (c, d) in states:
                if (c, d) == (a, b):
                    continue
                j = 3 * c + d
                row[col[(j, i)]] += pi[c] * pi[d] / (pi[a] * pi[b])   # inflow
                row[col[(i, j)]] -= 1.0                                # outflow
            off = nq + 3 * s
            # h(a,b) - [v(b) - children * v(a)] = 0
            row[off + b] -= 1.0
            row[off + a] += children
            Aeq.append(row); beq.append(0.0)
        if children != 1:   # mean-zero condition needed for the tree version
            row = np.zeros(n); row[nq + 3 * s: nq + 3 * s + 3] = pi
            Aeq.append(row); beq.append(0.0)
    bounds = [(eps, None)] * nq + [(None, None)] * 6
    res = linprog(np.zeros(n), A_eq=np.array(Aeq), b_eq=np.array(beq), bounds=bounds, method='highs')
    return res.status  # 0 = feasible, 2 = infeasible

piA, piB = (0.23, 0.14, 0.63), (0.19, 0.31, 0.5)
print('tree balance v(b)-2v(a):', 'feasible' if run(piA, piB, 2) == 0 else 'infeasible')
print('Z balance    v(b)- v(a):', 'feasible' if run(piA, piB, 1) == 0 else 'infeasible')
rng = np.random.default_rng(0)
cnt = {1: 0, 2: 0}
for _ in range(200):
    p = rng.dirichlet(np.ones(3)); q = rng.dirichlet(np.ones(3))
    for ch in (1, 2):
        cnt[ch] += run(p, q, ch) == 0
print('random pairs (pi^A, pi^B), feasible out of 200:  Z-type:', cnt[1], ' tree-type:', cnt[2])
