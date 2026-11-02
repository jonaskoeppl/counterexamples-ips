"""Exact-arithmetic audit for entry 0004 (all finite identities used in the proof).

Usage: python3 verify.py            (reads ../raw/2026-09-07_chatgpt-astra-6.tex)
"""
from fractions import Fraction as F

from tree_model import PI_A, PI_B, STATES, V_A, V_B, h, rates, table

Q = rates()
off = [Q[i][j] for i in range(9) for j in range(9) if i != j]
checks = {
    'diagonal of the table is empty': all(Q[i][i] is None for i in range(9)),
    '72 off-diagonal rates, all > 0': len(off) == 72 and all(q > 0 for q in off),
    'minimum rate = 1265009/6511300000': min(off) == F(1265009, 6511300000),
    'largest row sum < 33': max(sum(q for q in row if q is not None) for row in Q) < 33,
    'pi^A and pi^B are distinct probability vectors': sum(PI_A) == 1 and sum(PI_B) == 1 and PI_A != PI_B,
}
for name, pi, v, lab in (('A', PI_A, V_A, 'tab:hA'), ('B', PI_B, V_B, 'tab:hB')):
    printed = table(lab)
    checks[f'sum_a pi^{name}_a v^{name}(a) = 0'] = sum(p * x for p, x in zip(pi, v)) == 0
    checks[f'h_pi^{name}(a,b) = v^{name}(b) - 2 v^{name}(a) for all 9 pairs'] = all(
        h(Q, pi, a, b) == v[b] - 2 * v[a] for a, b in STATES)
    checks[f'printed table of h_pi^{name} agrees with the definition'] = all(
        h(Q, pi, a, b) == printed[a][b] for a, b in STATES)

for k, ok in checks.items():
    print(('PASS  ' if ok else 'FAIL  ') + k)
print(f'\nminimum rate = {float(min(off)):.6g}, largest row sum = '
      f'{float(max(sum(q for q in row if q is not None) for row in Q)):.6g}')
print('ALL CHECKS PASS' if all(checks.values()) else 'SOME CHECK FAILED')
