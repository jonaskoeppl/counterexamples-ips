# Positive rates do not force stationary measures to be quasilocal (on a tree)

**Entry:** 0004  
**Source:** question posed by Jonas Köppl; inspired by elliptic regularity  
**Proposed by:** ChatGPT Astra-6, 7 September 2026 (raw output in `raw/`); question and submission by Jonas Köppl  

## Claim

Consider an interacting particle system with finite local state space and finite-range transition rates that are uniformly bounded away from zero. If $\mu$ is a stationary measure for the IPS, then $\mu$ is necessarily quasilocal.

Here $\mu$ is **quasilocal** if its conditional probabilities given the configuration outside finite sets have versions that are continuous in the product topology; equivalently, $\mu$ is consistent with a quasilocal specification. Gibbs measures for absolutely summable interactions are quasilocal.

## Motivation: elliptic regularity

Stationary measures are exactly the solutions of $\mathscr{L}^*\mu = 0$. Rates that are uniformly bounded away from zero play the role of uniform ellipticity, and quasilocality the role of regularity of the solution. For uniformly elliptic equations, every weak solution is regular; the question asks whether the analogous statement holds for interacting particle systems.

## Known results

- **On $\mathbb{Z}^d$ the question is open.**
- Relative-entropy arguments on $\mathbb{Z}^d$ (Holley 1971 for stochastic Ising models; Jahnel–Külske 2019 for non-reversible dynamics, under non-degeneracy conditions) show: if a translation-invariant Gibbs measure is stationary, then translation-invariant stationary measures are Gibbs measures for the same specification. These arguments use that boundaries of large boxes are negligible compared with their volume (amenability).

## Why it is plausible

Positive rates make the dynamics "locally irreducible": every local pattern can be created and destroyed at a definite rate, so one expects stationary measures to have conditional probabilities that depend continuously on the configuration far away, just as uniform ellipticity smooths out solutions of elliptic equations.
