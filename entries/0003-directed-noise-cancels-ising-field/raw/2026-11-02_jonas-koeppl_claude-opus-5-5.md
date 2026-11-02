# Raw output

**Model:** Claude Opus 5.5 (`claude-opus-5-5`), working from a recollection by Jonas Köppl  
**Date:** 2026-11-02  
**Interface / settings:** Claude desktop app (Cowork); the Bérard–Dembin–Marêché paper (arXiv:2510.11424) was attached  
**Submitted by:** Jonas Köppl  

## Provenance

Jonas had found this counterexample earlier, in a discussion that was not recorded. In this session he recalled the idea and the construction was redone from scratch.

## Prompt

```
I remember that I had a counterexample to a generalisation of a result by Dembin-Berard-Mareche on perturbing interacting particle systems with directed noise, do you still have it?
```

```
Then let us come up with it again from scratch, I still remember most of the details. The assumption of the IPS being absorbing cannot be dropped in this result, because one can take the Ising model with an external field that gets cancelled by the directed noise and then ends up with a dynamics that has the supercritical Ising model as reversible measures so it cannot be ergodic. For this one doesnt use Glauber dynamics, but just fixes e.g. the rate from -1 to +1 constant to 1 and makes the other rate depend on the surroundings of the site.
```

## Output

The output of this session is the write-up in `../digest.md` (with the PDF in `pdf/` and the simulation in `../code/`); no separate transcript was kept. One detail differs from the recollection: for noise towards $-1$ (i.e. towards $0$, as in Bérard–Dembin–Marêché), the rate that must be constant is the rate $+1 \to -1$, in the direction of the noise. The recollection (constant rate $-1 \to +1$) is the same construction after the global spin flip, with noise towards $+1$.
