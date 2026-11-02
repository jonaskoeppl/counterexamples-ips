# Positive rates do not force stationary measures to be quasilocal (on a tree) — digest

**Status:** `plausible`  
**Verified by:** — (all finite identities checked in exact arithmetic by `code/verify.py`; proof read through by Claude (Opus 5.5); awaiting human check)  
**AI involvement:** counterexample and proof by ChatGPT Astra-6 (7 September 2026; raw output in `raw/`); digest, the line-versus-tree proposition and the code by Claude (Opus 5.5)  
**PDF:** [`pdf/0004-positive-rates-nonquasilocal-tree.pdf`](../../pdf/0004-positive-rates-nonquasilocal-tree.pdf)  

## Setting

**Graph.** The *directed binary tree*: every vertex $x$ has one parent $p(x)$ and two children. As an undirected graph this is the 3-regular tree $T_3$; the orientation points every edge towards a fixed end. The oriented edges are $(x, p(x))$, and every vertex lies in exactly three of them: once as the child, twice as the parent.

**Dynamics.** Local state space $E = \{0,1,2\}$. On each oriented edge $(x, p(x))$, the ordered pair $(\eta_x, \eta_{p(x)}) \in E^2$ jumps according to one fixed 9-state Markov generator $Q = (q_{ij})$, independently over edges:
$$\mathscr{L}f(\eta) = \sum_{x} \sum_{(c,d) \neq (\eta_x, \eta_{p(x)})} q_{(\eta_x,\eta_{p(x)}),(c,d)} \big[f(\eta^{x,p(x);(c,d)}) - f(\eta)\big].$$
The rates (pair states ordered $00, 01, \dots, 22$):

| from \ to | 00 | 01 | 02 | 10 | 11 | 12 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|
| **00** | — | 2767709/9766950000 | 10385390113/33207630000000 | 589477/1953390000 | 62846/203478125 | 1813959/6511300000 | 4589347/19533900000 | 2536387/9766950000 | 204841/1028100000 |
| **01** | 9391756087/33207630000000 | — | 9595487813/33207630000000 | 4516031/19533900000 | 1545599/6511300000 | 1265009/6511300000 | 5577797/19533900000 | 5102083/19533900000 | 305591/1028100000 |
| **02** | 21707821/74290000000 | 13/50000 | — | 13/50000 | 13/50000 | 13/50000 | 13/50000 | 13/50000 | 13/50000 |
| **10** | 13/50000 | 630401/25000 | 13/50000 | — | 13/50000 | 13/50000 | 13/50000 | 17029/20000 | 13/50000 |
| **11** | 13/50000 | 17809/20000 | 13/50000 | 13/50000 | — | 13/50000 | 13/50000 | 13/50000 | 13/50000 |
| **12** | 13/50000 | 13/50000 | 13/50000 | 13/50000 | 13/50000 | — | 13/50000 | 13/50000 | 13/50000 |
| **20** | 216521/50000 | 13/50000 | 1411131/50000 | 13/50000 | 13/50000 | 13/50000 | — | 13/50000 | 13/50000 |
| **21** | 34733/100000 | 13/50000 | 89301/100000 | 433037/100000 | 13/50000 | 5113/2000 | 13/50000 | — | 13/50000 |
| **22** | 13/50000 | 13/50000 | 17039/100000 | 13/50000 | 13/50000 | 733/100000 | 104209/25000 | 13/50000 | — |

All 72 rates are positive, the smallest is $\varepsilon_* = 1265009/6511300000 \approx 1.9 \cdot 10^{-4}$, and all row sums are below $33$. So every change of an ordered nearest-neighbour pair, in particular every single-site change, happens at rate at least $\varepsilon_*$.

## Statement

**Theorem (ChatGPT Astra-6).** For the two product measures $\nu^A = \bigotimes \pi^A$ and $\nu^B = \bigotimes \pi^B$ with
$$\pi^A = \big(\tfrac{23}{100}, \tfrac{14}{100}, \tfrac{63}{100}\big), \qquad \pi^B = \big(\tfrac{19}{100}, \tfrac{31}{100}, \tfrac12\big),$$
both $\nu^A$ and $\nu^B$ are stationary. Consequently $\mu = \tfrac12 \nu^A + \tfrac12 \nu^B$ is stationary, and $\mu$ is **not quasilocal**: $\mu(\eta_o = 0 \mid \mathcal{F}_{\mathbb{V} \setminus \{o\}})$ has no continuous version.

So the claim in `question.md` is false on the tree, for finite local state space, nearest-neighbour rates and bounded total rates. There are no forbidden transitions: every change of the ordered pair on an edge, in particular every single-site change, happens at rate $\ge \varepsilon_* > 0$, so no quantity is conserved.

## Proof

**Lemma 1 (adjoint identity).** For a product measure $\nu_\pi$ with full support and an oriented edge $e = (x, p(x))$ with generator part $K_e$,
$$\int K_e f \, d\nu_\pi = \int f(\eta)\, h_\pi(\eta_x, \eta_{p(x)}) \, d\nu_\pi(\eta), \qquad h_\pi(a,b) := \frac{1}{\pi_a\pi_b} \sum_{(c,d) \neq (a,b)} \pi_c\pi_d\, q_{(c,d),(a,b)} - \sum_{(c,d) \neq (a,b)} q_{(a,b),(c,d)}.$$
This is a change of variables on the pair: incoming flow divided by the pair weight, minus outgoing rate.

**Lemma 2 (tree-divergence criterion).** If there is $v : E \to \mathbb{R}$ with $\sum_a \pi_a v(a) = 0$ and
$$h_\pi(a,b) = v(b) - 2v(a) \qquad \text{for all } a, b \in E,$$
then $\nu_\pi$ is stationary.

*Proof.* Let $f$ be local with support in a finite set $A$. Only edges touching $A$ contribute to $\int \mathscr{L} f\, d\nu_\pi$. By Lemma 1, each contributes $\int f \cdot (v(\eta_{p(x)}) - 2v(\eta_x))\, d\nu_\pi$, and integrating out an endpoint outside $A$ kills its term because $v$ has mean zero. Collect the remaining terms by vertices of $A$: each $y \in A$ is the child of exactly one edge (term $-2v(\eta_y)$) and the parent of exactly two edges (terms $+v(\eta_y)$ each), so everything cancels and $\int \mathscr{L} f\, d\nu_\pi = 0$. Since local functions form a core for the generator (Liggett 1985, Ch. I), $\nu_\pi$ is stationary. $\square$

**Step 3 (finite identities).** With
$$v^A = \big(-\tfrac{45787}{3680}, \tfrac{87917}{100000}, \tfrac{434699}{100000}\big), \qquad v^B = \big(-\tfrac{12245721}{950000}, \tfrac{44491}{50000}, \tfrac{21733}{5000}\big),$$
both mean-zero conditions and all $2 \times 9$ balance identities hold exactly. This is verified in exact rational arithmetic by [`code/verify.py`](code/verify.py). As an independent check, [`code/check_stationarity.py`](code/check_stationarity.py) computes $\int \mathscr{L} f\, d\nu$ by brute force for all functions $f$ of a vertex, its parent and its two children: the result is $\lesssim 10^{-15}$ for $\nu^A$ and $\nu^B$, and $0.5$ for a non-stationary control.

**Step 4 (not quasilocal).** By the law of large numbers, the density of $0$s outside $o$ is $\tfrac{23}{100}$ under $\nu^A$ and $\tfrac{19}{100}$ under $\nu^B$, so a tail event $T_A$ tells the two components apart. Hence
$$\mu(\eta_o = 0 \mid \mathcal{F}_{\mathbb{V}\setminus\{o\}}) = \tfrac{23}{100}\, \mathbf 1_{T_A} + \tfrac{19}{100}\, \mathbf 1_{T_A^c} \quad \mu\text{-a.s.}$$
A continuous version $g$ would equal $\tfrac{23}{100}$ on a set of full $\nu^A$-measure and $\tfrac{19}{100}$ on a set of full $\nu^B$-measure. Both measures have full support, so both sets are dense, and continuity forces $g \equiv \tfrac{23}{100}$ and $g \equiv \tfrac{19}{100}$: a contradiction. $\square$

## Why a tree? The same mechanism is impossible on $\mathbb{Z}$

The construction needs two distinct product measures that are stationary for the *same* positive-rate dynamics. On the line this cannot happen.

**Proposition (added in this digest).** Consider a translation-invariant nearest-neighbour pair-update IPS on $\mathbb{Z}$: the pair $(\eta_x, \eta_{x+1})$ jumps according to a fixed irreducible generator $Q$ on $E^2$, with $E$ finite. Then at most one product measure with full support is stationary.

*Proof.* (i) *Stationarity is a coboundary condition.* Apply Lemma 1 on $\mathbb{Z}$ (each vertex has one parent and one child) and test with functions of the sites in an interval $[m, n]$. For $n = m$ and $n = m+1$ this shows that $\nu_\pi$ is stationary iff $h_\pi(a,b) = v(b) - v(a)$ for some $v$.

(ii) *Entropy.* Let $\nu_\pi$ and $\nu_{\pi'}$ both be stationary, and write $w = \pi \otimes \pi$, $w' = \pi' \otimes \pi'$, $r = w'/w$. For the 9-state chain with generator $Q$, the time derivative of the relative entropy $H(w' e^{tQ} \mid w e^{tQ})$ at $t = 0$ equals
$$\sum_s (w'Q)(s) \log r(s) - \sum_s r(s)\,(wQ)(s) = -\sum_{s \neq s'} w(s')\,Q(s',s)\,\big[r(s) - r(s') - r(s')\log\tfrac{r(s)}{r(s')}\big] \le 0,$$
with equality only if $r$ is constant (irreducibility). By (i), $(wQ)(a,b) = w(a,b)\,(v(b) - v(a))$ and $(w'Q)(a,b) = w'(a,b)\,(v'(b) - v'(a))$. Since $\log r(a,b) = \ell(a) + \ell(b)$ with $\ell = \log(\pi'/\pi)$, and $a, b$ are i.i.d. under $w'$, both sums on the left vanish by symmetry. Hence $r$ is constant and $\pi' = \pi$. $\square$

On the tree the weights are $(-2, +1)$ instead of $(-1, +1)$, and the same computation gives $-\mathbb{E}_{\pi'}[v'\ell] + \mathbb{E}_{\pi'}[v]$, which need not vanish. A quick linear-programming experiment ([`code/lp_tree_vs_line.py`](code/lp_tree_vs_line.py)) confirms the contrast: for 200 random pairs $(\pi^A, \pi^B)$, positive rates with both balance conditions exist in 199 cases on the tree and in none on the line.

## Mechanism

- **Branching lets "flux" escape to infinity.** On the tree, every vertex has one parent and two children, so the defect $v(b) - 2v(a)$ sums to zero over any finite set even though it is not a coboundary. In entropy terms: on $\mathbb{Z}^d$ the boundary of a box is negligible compared with its volume, and relative-entropy arguments pin down translation-invariant stationary measures (Holley; Jahnel–Külske). On the non-amenable tree the boundary is as large as the volume, and the argument breaks down.
- **Mixing two "phases" destroys quasilocality.** Once two stationary product measures with different densities coexist, their mixture remembers in its tail which component is present. The one-site conditional probability then depends on information at infinity and cannot be continuous.
- **Elliptic analogy.** Positive rates give local irreducibility, the analogue of ellipticity. But quasilocality is not a local property: it concerns the influence of infinity. On trees, as on hyperbolic space for elliptic equations, the boundary at infinity is large enough to carry several "boundary values" (compare entry 0002, where transience produced non-constant bounded harmonic functions).

## Which hypothesis breaks

- **The graph is the 3-regular tree, not $\mathbb{Z}^d$.** The proposition above shows that this mechanism (two stationary product measures) fails on $\mathbb{Z}$.
- **The rates use an orientation** towards a fixed end of the tree, so they are invariant only under the automorphisms that fix this end.
- **Pair updates:** both endpoints of an edge may change in one jump. The source notes that the case where only one site changes per jump (spin systems) is not covered.
- **The non-quasilocal measure is a mixture**; its extremal components are product measures and hence quasilocal.

## What this does *not* show

The question on $\mathbb{Z}^d$ remains open. The example shows that a proof on $\mathbb{Z}^d$ has to use the geometry of $\mathbb{Z}^d$ (e.g. amenability), not just positivity and finite range of the rates.

## Assessment of the raw output

The construction is fully explicit and the proof only needs finite rational identities plus elementary probability. All identities were re-verified independently in exact arithmetic (`code/verify.py`); the printed tables in the source agree with the definitions. Two small gaps in the source: (a) the step "$\int \mathscr{L} f\, d\nu = 0$ for all local $f$ implies stationarity" needs that local functions form a core (true here, Liggett 1985, Ch. I); (b) the source does not explain why a tree is needed — the proposition above fills this in. The rates look computer-generated (large rational numbers solving a linear system), presumably found by ChatGPT Astra-6 with a solver. The source is careful about scope, in particular about single-site updates.

## References

- ChatGPT Astra-6, *A strictly positive finite-range continuous-time IPS with a stationary non-quasilocal measure*, AI-generated note, 7 September 2026 (in `raw/`).
- R. Holley, Free energy in a Markovian model of a lattice spin system, *Comm. Math. Phys.* 23 (1971).
- B. Jahnel, C. Külske, Attractor properties for irreversible and reversible interacting particle systems, *Comm. Math. Phys.* 366 (2019).
- T. M. Liggett, *Interacting Particle Systems*, Springer, 1985, Ch. I.
- H.-O. Georgii, *Gibbs Measures and Phase Transitions*, de Gruyter, 1988 (2nd ed. 2011): quasilocality and specifications.
- P. Gács, Reliable cellular automata with self-organization, *J. Stat. Phys.* 103 (2001).
- A. L. Toom, Stable and attractive trajectories in multicomponent systems, in *Multicomponent Random Systems*, Adv. Probab. Related Topics 6 (1980).
