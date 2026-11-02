# One reversible measure, but a non-reversible stationary measure: exclusion processes

**Entry:** 0001  
**Source:** Holley–Stroock question (Liggett 1985, Ch. IV); exclusion processes (Liggett 1985, Ch. VIII; Liggett 1999, Part III)  
**Proposed by:** Claude (Opus 5.5), during repository setup; see `raw/`  

## Claim

Let $(\eta_t)$ be an interacting particle system on $\{0,1\}^{\mathbb{Z}^d}$ with translation-invariant, finite-range rates. If the process has at least one reversible measure, then every stationary measure is reversible.

## Known results

- For stochastic Ising models (positive-rate spin systems reversible with respect to the Gibbs measures of a finite-range potential), every translation-invariant stationary measure is Gibbs, hence reversible, in all $d$ (Holley 1971). For $d \le 2$ every stationary measure is Gibbs (Holley–Stroock 1977). For $d \ge 3$ the question is open.
- For symmetric exclusion on $\mathbb{Z}^d$ with irreducible $p(\cdot,\cdot)$, every stationary measure is a mixture of Bernoulli product measures $\nu_\rho$, all of which are reversible (Liggett 1985, Ch. VIII).

## Why it is plausible

The Holley–Stroock results suggest that reversibility, once present, is "rigid": the dynamics cannot support a stationary state with a non-zero probability flux. The aim of this entry is to see that the claim in the generality stated above is false, and that the counterexample uses a conservation law in an essential way.
