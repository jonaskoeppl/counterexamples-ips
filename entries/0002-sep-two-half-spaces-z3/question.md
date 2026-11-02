# Symmetric exclusion on two half-spaces of $\mathbb{Z}^3$: a non-reversible stationary measure

**Entry:** 0002  
**Source:** *Stationary measures of stochastic Ising models in one and two dimensions: an alternative proof of the Holley–Stroock theorem*, Section 8 (see `raw/`); Liggett 1985, Ch. IV and VIII  
**Proposed by:** ChatGPT Astra-6 (raw output in `raw/`); submitted by Jonas Köppl  

## Claim

Consider exchange (Kawasaki-type) dynamics on a connected graph of bounded degree, with rates that are positive on every edge. If a stationary measure has finite energy, then it is reversible.

## Known results

- On $\mathbb{Z}^d$ with $d \le 2$, and more generally on recurrent graphs of bounded degree, every stationary measure with finite energy of an exchange dynamics associated with a finite-range potential is reversible (Section 7 of the source, Theorem 7.3 and Remark 7.7). This is the conservative analogue of Holley–Stroock (1977).
- For symmetric simple exclusion with symmetric irreducible rates, the extremal stationary measures are indexed by the bounded harmonic functions of one random walk (Liggett 1973, 1974; Liggett 1985, Ch. VIII). If these are constant, every stationary measure is a mixture of Bernoulli product measures, hence reversible.

## Why it is plausible

The Holley–Stroock argument for $d \le 2$ only uses recurrence through a capacity bound, and finite energy rules out the obvious degenerate counterexamples (point masses, blocking measures). One might hope that in $d \ge 3$ the statement still holds, with a better argument. The entry shows that, at the level of graphs, transience alone already breaks it.
