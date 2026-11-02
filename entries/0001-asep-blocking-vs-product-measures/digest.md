# One reversible measure, but a non-reversible stationary measure: exclusion processes — digest

**Status:** `plausible`  
**Verified by:** — (proofs below written out by Claude; awaiting human check)  
**AI involvement:** idea and write-up by Claude (Opus 5.5); see `raw/`  
**PDF:** [`pdf/0001-asep-blocking-vs-product-measures.pdf`](../../pdf/0001-asep-blocking-vs-product-measures.pdf)  

## Setting

Nearest-neighbour asymmetric simple exclusion process (ASEP) on $\mathbb{Z}$: each particle jumps to the right at rate $p$ and to the left at rate $q$, with $p > q > 0$, a jump being suppressed if the target site is occupied. The generator acts on cylinder functions as
$$
\Omega f(\eta) = \sum_{x\in\mathbb{Z}} \Big( p\,\eta(x)\big(1-\eta(x+1)\big) + q\,\eta(x+1)\big(1-\eta(x)\big) \Big)\,\big(f(\eta^{x,x+1}) - f(\eta)\big),
$$
where $\eta^{x,x+1}$ is $\eta$ with the values at $x$ and $x+1$ exchanged. Write $\lambda = p/q > 1$.

## Statement

**Proposition.** For ASEP on $\mathbb{Z}$ with $p > q$:

1. For every $c > 0$, the product measure $\mu_c$ with marginals
   $$\mu_c\big(\eta(x) = 1\big) = \rho_x := \frac{c\lambda^x}{1 + c\lambda^x}$$
   (a *blocking measure*) is reversible.
2. For every $\rho \in (0,1)$, the Bernoulli product measure $\nu_\rho$ is stationary but not reversible.

Hence the claim in `question.md` fails: this process has (many) reversible measures and also stationary measures that are not reversible.

## Proof

**(1) Blocking measures are reversible.** For product measures and exclusion dynamics it suffices to check detailed balance across each bond (Liggett 1985, Ch. VIII): for every $x$,
$$
p\,\rho_x(1-\rho_{x+1}) = q\,\rho_{x+1}(1-\rho_x).
$$
Since $\rho_y/(1-\rho_y) = c\lambda^y$, the ratio $\dfrac{\rho_{x+1}(1-\rho_x)}{\rho_x(1-\rho_{x+1})} = \lambda = p/q$, which is exactly the required identity.

**(2) Bernoulli measures are stationary.** This holds for every exclusion process with translation-invariant $p(\cdot,\cdot)$ (Liggett 1985, Ch. VIII).

**(2) Bernoulli measures are not reversible.** Reversibility of $\nu$ means $\int f\,\Omega g\,d\nu = \int g\,\Omega f\,d\nu$ for all cylinder functions $f,g$. Take
$$
f(\eta) = \eta(0)\big(1-\eta(1)\big), \qquad g(\eta) = \big(1-\eta(0)\big)\eta(1).
$$
On $\{f = 1\}$ we have $g = 0$, and the only transition that changes $\eta$ into a configuration with $g = 1$ is the jump of the particle at $0$ to $1$, at rate $p$ (all other transitions touching sites $0$ or $1$ either are blocked or lead to $(\eta(0),\eta(1)) \in \{(0,0),(1,1)\}$). So $f\,\Omega g = p f$, and similarly $g\,\Omega f = q g$. Therefore
$$
\int f\,\Omega g\,d\nu_\rho = p\,\rho(1-\rho) \neq q\,\rho(1-\rho) = \int g\,\Omega f\,d\nu_\rho
$$
whenever $0 < \rho < 1$. $\square$

## Mechanism

Reversibility means zero net probability current across every bond. Under $\nu_\rho$, the current across a bond is $(p-q)\rho(1-\rho) > 0$: a translation-invariant state with a drift necessarily transports particles, so it cannot be reversible. The blocking measures avoid this by "piling up" the particles: $\rho_x \to 0$ as $x \to -\infty$ and $\rho_x \to 1$ as $x \to +\infty$, and the exclusion rule exactly balances the drift on every bond. The conservation of particles is what allows these two kinds of stationary state to coexist: they live in different "sectors" of the state space, which the dynamics never connects.

## Even simpler, but degenerate

For *any* exclusion process, the point masses $\delta_{\mathbf 0}$ (empty) and $\delta_{\mathbf 1}$ (full) are trivially reversible. So for asymmetric exclusion on $\mathbb{Z}^d$, in any dimension, the claim already fails with these. The blocking measures show that the failure is not just an artefact of absorbing configurations.

## Remark: a full-support version in $d \ge 2$

On $\mathbb{Z}^2$, let particles jump to $x \pm e_1$ at rates $p$ and $q$ ($p > q$), and to $x \pm e_2$ at rate $r$ each. The product measure with $\rho_x/(1-\rho_x) = \lambda^{x_1}$ satisfies detailed balance on every bond (ratio $\lambda = p/q$ on horizontal bonds, ratio $1 = r/r$ on vertical ones), so it is reversible, and it has full support. The Bernoulli measures $\nu_\rho$ are again stationary and not reversible (same computation). *(Sketch; to be checked.)*

## Which hypothesis breaks

The claim needs to exclude **conservative dynamics**. In the Holley–Stroock setting the rates are positive spin-flip rates: there is no conservation law, and hence no decomposition of the state space into sectors with different stationary behaviour. The counterexample also shows that "there is a reversible measure" should probably be replaced by a more specific hypothesis, e.g. that the process is a stochastic Ising model (reversible with respect to the Gibbs measures of a given potential).

## Assessment of the raw output

The raw output stated the counterexample correctly in one sentence, with a reference (Liggett 1999, Part III) that was not pinned down to a theorem number and was flagged by the model itself as written from memory. The proofs above, the degenerate example and the $d \ge 2$ remark were added afterwards, also by Claude. No human check has been done yet.

## References

- R. Holley, Free energy in a Markovian model of a lattice spin system, *Comm. Math. Phys.* 23 (1971).
- R. Holley, D. Stroock, In one and two dimensions, every stationary measure for a stochastic Ising model is a Gibbs state, *Comm. Math. Phys.* 55 (1977).
- T. M. Liggett, Coupling the simple exclusion process, *Ann. Probab.* 4 (1976).
- T. M. Liggett, *Interacting Particle Systems*, Springer, 1985, Ch. IV and VIII.
- T. M. Liggett, *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes*, Springer, 1999, Part III.
