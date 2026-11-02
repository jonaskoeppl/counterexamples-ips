# Symmetric exclusion on two half-spaces of $\mathbb{Z}^3$: a non-reversible stationary measure — digest

**Status:** `plausible`  
**Verified by:** — (Theorem 8.1 read through step by step by Claude (Opus 5.5); Theorem 8.3 only summarised; awaiting human check)  
**AI involvement:** counterexample and proofs by ChatGPT Astra-6 (raw output in `raw/`); digest written by Claude (Opus 5.5) from Section 8 of that output  
**PDF:** [`pdf/0002-sep-two-half-spaces-z3.pdf`](../../pdf/0002-sep-two-half-spaces-z3.pdf)  

## Setting

Let $H_+ = \{x \in \mathbb{Z}^3 : x_1 \ge 1\}$, $H_- = \{x \in \mathbb{Z}^3 : x_1 \le 0\}$, $o_- = (0,0,0)$, $o_+ = (1,0,0)$. Let $G$ be the graph on $\mathbb{Z}^3$ whose edges are the nearest-neighbour bonds inside $H_+$, the nearest-neighbour bonds inside $H_-$, and the single **bridge** $\{o_-, o_+\}$. So $G$ is two half-spaces joined by one edge.

The symmetric simple exclusion process (SEP) on $G$ exchanges the values at the endpoints of each edge of $G$ at rate $1$ (rate $0$ on all other bonds of $\mathbb{Z}^3$). Spins are $\eta_x \in \{-1,+1\}$, with $+1$ meaning "occupied". Since the rates are constant on the edges, a measure is reversible iff it is invariant under each exchange $\theta_b$, $b$ an edge of $G$. All Bernoulli product measures $\nu_\rho$ with constant density are reversible.

## Statement

**Theorem (8.1 in the source).** Let $0 < \rho_- < \rho_+ < 1$. SEP on $G$ has a stationary measure $\mu^*$ that is **not reversible** and has **finite energy** with constant $\delta = \min\{\rho_-, 1-\rho_+\}$, i.e. $\mu^*(\eta_y = s \mid \eta_\Lambda = \sigma) \ge \delta$ for all finite $\Lambda$, $y \notin \Lambda$, $s$, $\sigma$.

Moreover $\mu^*(\eta_x = +1) \to \rho_\pm$ as $|x| \to \infty$ in $H_\pm$.

## Proof (summary of the source)

1. **A non-constant bounded harmonic function.** Simple random walk $X$ on $G$ is transient: folding $\mathbb{Z}^3$ along $\{x_1 = \tfrac12\}$ maps simple random walk on $\mathbb{Z}^3$ to a walk on $H_+$ that only adds self-loops, so $H_+$ is transient, and $G \supseteq H_+$ is transient by Rayleigh monotonicity. Hence $X$ crosses the bridge only finitely often, and
   $$\alpha(x) := P_x(X \text{ eventually stays in } H_+)$$
   is harmonic on $G$ with $0 \le \alpha \le 1$. The reflection $x \mapsto (1-x_1, x_2, x_3)$ swaps $H_\pm$, so $\alpha(\bar x) = 1 - \alpha(x)$; and $\alpha > \tfrac12$ somewhere, because a walk started far out in $H_+$ avoids $o_+$ with probability close to $1$. So $\alpha$ is not constant. Put $\beta := \rho_- + (\rho_+ - \rho_-)\alpha$, harmonic with values in $[\rho_-, \rho_+]$.
2. **The density is preserved.** Start from the product measure $\nu_\beta$ with $\nu_\beta(\eta_x = +1) = \beta(x)$. For SEP the one-point function $u_t(x) = (\nu_\beta T_t)(\eta_x = +1)$ solves $\tfrac{d}{dt}u_t = \Delta_G u_t$, and $\beta$ is a stationary solution; a Grönwall argument gives $u_t = \beta$ for all $t$.
3. **A stationary limit.** Any weak limit $\mu^*$ of Cesàro averages $\tfrac1{T_n}\int_0^{T_n} \nu_\beta T_t\,dt$ is stationary (Feller property), with $\mu^*(\eta_x = +1) = \beta(x)$.
4. **Not reversible.** Reversibility would give $\theta_b$-invariance for every edge $b = \{x,y\}$, hence $\beta(x) = \beta(y)$ along edges, hence $\beta$ constant on the connected graph $G$: contradiction.
5. **Finite energy.** In the stirring construction, $\eta_t(x) = \eta_0(\pi_t^{-1}(x))$ for a random bijection $\pi_t$ independent of $\eta_0$. Conditionally on $\pi_t$ the spins are independent with densities in $[\rho_-, \rho_+]$; this bound survives averaging and weak limits. $\square$

## Mechanism

The two half-spaces act as two **reservoirs** at different densities $\rho_-$ and $\rho_+$, connected by a single wire. Because $\mathbb{Z}^3$-half-spaces are transient, a reservoir is never "drained" through the bridge: particles that cross wander off to infinity rather than coming back. So the density difference persists, and in the stationary state a **current flows through the bridge**. A non-zero current is incompatible with reversibility.

In $d \le 2$ (or on any recurrent graph) this fails: bounded harmonic functions are constant, there is only one "end density", and every stationary measure of SEP is a mixture of Bernoulli measures (Remark 8.2(d) of the source, Caccioppoli inequality).

In short: **for SEP on a graph, non-reversible stationary measures come from non-constant bounded harmonic functions**, and transience of $\mathbb{Z}^3$ is what allows such functions once the graph has two "ends" joined by a bottleneck.

## Interacting version (Theorem 8.3 in the source; summary only)

Let $J$ be a potential of range $L$ with $\sum_F |J_F| < \infty$, and give the edges of $G$ the exchange rates $c_b(\eta) = \exp\big(\tfrac12 \sum_F J_F(\chi_F(\eta) - \chi_F(\eta^{xy}))\big)$ (rate $0$ off $G$). Then the measure proportional to $e^{-\Phi}\nu_\rho$, $\Phi = \sum_F J_F\chi_F$, is reversible, but there is also a stationary measure $\mu$ with $|\mu(\eta_x = +1) - \beta(x)| \le \gamma(x) \to 0$ as $|x| \to \infty$; so the densities at the two ends differ and $\mu$ is not reversible. The proof couples the interacting dynamics with SEP via a graphical construction; disagreements are controlled by the Green's function of $X$. Whether this $\mu$ has finite energy is left open in the source.

## Which hypothesis breaks

- The graph is **not $\mathbb{Z}^3$**: the rates vanish on all bonds crossing $\{x_1 = \tfrac12\}$ except the bridge. With rates bounded away from zero on all bonds of $\mathbb{Z}^3$ (even inhomogeneous ones), bounded harmonic functions are constant (elliptic Harnack inequality), and every stationary measure of the corresponding exclusion process is reversible (Remark 8.2(e)).
- The dynamics is **conservative**. The densities at the two ends are maintained because particles are conserved. For spin flips, different "phases" at the two ends would be realised by Gibbs states, which are reversible (Remark 8.4(e)). So the entry does **not** settle the Holley–Stroock question in $d \ge 3$.
- It does show that **recurrence cannot be dropped** from the graph version of the conservative Holley–Stroock theorem (Remark 8.2(c)): $G$ is connected, of bounded degree, the rates are positive on its edges, and $\mu^*$ has finite energy.

## Comparison with entry 0001

Entry 0001 (ASEP on $\mathbb{Z}$) also has a reversible measure and a non-reversible stationary measure, but there the non-reversibility comes from an *asymmetric* drift, and the reversible (blocking) measures have no finite energy. Here the dynamics is *symmetric*, all Bernoulli measures are reversible, the non-reversible measure has finite energy, and the current is created by the geometry (two transient ends) instead.

## Assessment of the raw output

The whole construction, including both theorems and their proofs, comes from ChatGPT Astra-6; the digest only condenses it. Theorem 8.1 is clean and self-contained; each step uses only standard facts (transience of $\mathbb{Z}^3$, Rayleigh monotonicity, the linear equation for the one-point function of SEP, the stirring construction). Points worth double-checking: the argument that $h(x) < \tfrac12$ for some $x$ (Step 1), and the Grönwall step (Step 2) with $\varphi \le 12\int_0^t \varphi$. Theorem 8.3 (coupling with interacting dynamics) has not been checked in detail.

## References

- ChatGPT Astra-6, *Stationary measures of stochastic Ising models in one and two dimensions: an alternative proof of the Holley–Stroock theorem*, AI-generated manuscript, 2026, Section 8 (in `raw/`).
- R. Holley, D. Stroock, In one and two dimensions, every stationary measure for a stochastic Ising model is a Gibbs state, *Comm. Math. Phys.* 55 (1977).
- T. M. Liggett, A characterization of the invariant measures for an infinite particle system with interactions, *Trans. Amer. Math. Soc.* 179 (1973), 433–453; II, *ibid.* 198 (1974), 201–213.
- T. M. Liggett, *Interacting Particle Systems*, Springer, 1985, Ch. VIII.
- R. Lyons, Y. Peres, *Probability on Trees and Networks*, Cambridge University Press, 2016, Ch. 2.
- T. Delmotte, Parabolic Harnack inequality and estimates of Markov chains on graphs, *Rev. Mat. Iberoam.* 15 (1999).
- P. Lammers, F. L. Toninelli, Non-reversible stationary states for majority voter and Ising dynamics on trees, *Electron. J. Probab.* 29 (2024).
