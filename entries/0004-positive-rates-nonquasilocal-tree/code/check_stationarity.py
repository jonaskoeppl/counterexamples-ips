"""Independent numerical check of the tree-divergence lemma for entry 0004.

Take a vertex o, its parent p and its two children c1, c2 (the set A), together with all
vertices adjacent to them: 10 vertices and 9 oriented edges. For every configuration xi on A,
compute  w(xi) = int L 1{eta_A = xi} d nu_pi  by brute force (floating point).
Stationarity of nu_pi requires w = 0. A non-stationary product measure serves as a control.

Usage: python3 check_stationarity.py
"""
import numpy as np

from tree_model import PI_A, PI_B, rates

Q = np.array([[0.0 if q is None else float(q) for q in row] for row in rates()])
# 0 = o, 1 = p, 2 = c1, 3 = c2 (the set A); 4 = parent of p; 5 = sibling of o;
# 6, 7 = children of c1; 8, 9 = children of c2. Oriented edges are (child, parent).
EDGES = [(0, 1), (2, 0), (3, 0), (1, 4), (5, 1), (6, 2), (7, 2), (8, 3), (9, 3)]
A = (0, 1, 2, 3)


def defect(pi):
    P = np.ones([3] * 10)
    for k in range(10):
        shape = [1] * 10
        shape[k] = 3
        P = P * np.asarray(pi, dtype=float).reshape(shape)
    M = np.zeros_like(P)
    for x, p in EDGES:
        for a in range(3):
            for b in range(3):
                src = [slice(None)] * 10
                src[x], src[p] = a, b
                mass = P[tuple(src)]
                for c in range(3):
                    for d in range(3):
                        if (c, d) != (a, b):
                            q = Q[3 * a + b, 3 * c + d]
                            dst = [slice(None)] * 10
                            dst[x], dst[p] = c, d
                            M[tuple(dst)] += q * mass
                            M[tuple(src)] -= q * mass
    return M.sum(axis=tuple(k for k in range(10) if k not in A))


for name, pi in (('nu^A', PI_A), ('nu^B', PI_B), ('control: uniform product', (1/3, 1/3, 1/3))):
    print(f'{name:26s} max_xi |int L 1_xi d nu| = {np.abs(defect([float(x) for x in pi])).max():.2e}')
