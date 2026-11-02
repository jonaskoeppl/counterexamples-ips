# Directed noise can destroy ergodicity: the absorbing state in Bérard–Dembin–Marêché cannot be dropped

**Entry:** 0003  
**Source:** J. Bérard, B. Dembin, L. Marêché, *Sharpness for monotone absorbing interacting particle systems*, arXiv:2510.11424 (2025), Theorem 1.1 and Section 1.5  
**Proposed by:** Jonas Köppl; details worked out with Claude (Opus 5.5), see `raw/`  

## Setting

Finite-range spin systems on $\{0,1\}^{\mathbb{Z}^d}$ with rates $c_1$ (flip $0 \to 1$) and $c_0$ (flip $1 \to 0$) that are **monotone**: $c_1$ is increasing and $c_0$ is decreasing in the configuration. For $\varepsilon > 0$, $L_\varepsilon$ denotes the generator with $c_0$ replaced by $c_0 + \varepsilon$, i.e. with additional **directed noise** that sets each site to $0$ at rate $\varepsilon$.

## Claim

Let $L$ be monotone and **ergodic** (we do *not* assume that $\mathbf 0$ is absorbing). Then for every $\varepsilon > 0$ the IPS with generator $L_\varepsilon$ is ergodic, and even exponentially ergodic.

## Known results

- **Bérard–Dembin–Marêché, Theorem 1.1:** the claim holds if, in addition, $\mathbf 0$ is absorbing ($c_1(\mathbf 0) = 0$). In that case ergodicity of $L_\varepsilon$ is immediate from monotone coupling ($L_\varepsilon$ lies below $L$, and ergodicity means convergence to $\delta_{\mathbf 0}$); the content of the theorem is *exponential* ergodicity, proved with the OSSS inequality. The discrete-time analogue for probabilistic cellular automata is due to Hartarsky (2022).
- **Bérard–Dembin–Marêché, Section 1.5 (open question):** can the result be extended beyond systems with absorbing states? Does a monotone ergodic IPS always admit an *arbitrarily small* perturbation that is exponentially ergodic?

## Why it is plausible

Noise towards one value adds randomness that does not depend on the configuration, so one expects it to help the system forget its initial condition. In the absorbing case, it pushes towards the unique stationary measure $\delta_{\mathbf 0}$ and can only help.
