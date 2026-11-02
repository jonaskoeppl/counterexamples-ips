# counterexamples-ips

A collection of **counterexamples for interacting particle systems (IPS)**, in the setting of Tom Liggett's books:

- T. M. Liggett, *Interacting Particle Systems*, Springer, 1985 (reprinted 2005).
- T. M. Liggett, *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes*, Springer, 1999.
- T. M. Liggett, *Continuous Time Markov Processes: An Introduction*, AMS, 2010.

The aim is to sharpen intuition. A good counterexample shows *why* a plausible statement fails, which hypothesis is doing the work, and what the correct statement might be. Entries can be found by humans or produced with the help of AI systems. Either way, what matters is that a human can read the entry, check it, and come away understanding something.

A summary of all entries, one paragraph each with links to the full write-ups, is in [`pdf/overview.pdf`](pdf/overview.pdf).

---

## Possible future directions

Questions we plan to look at. Entries that already address part of a question are linked under it.

### 1. Does adding noise preserve ergodicity?

Let $c(x,\eta)$ be the rates of an ergodic spin system, and consider the perturbed system with rates $c(x,\eta) + \varepsilon$ (independent spin flips at rate $\varepsilon > 0$, superposed on the original dynamics). Is the perturbed system still ergodic? Variants worth separating:

- attractive vs. non-attractive rates;
- symmetric noise vs. noise that favours one spin value;
- uniform-in-$\varepsilon$ statements vs. small/large-$\varepsilon$ statements;
- the analogous question for exclusion-type or mixed dynamics, and for probabilistic cellular automata.

Intuition says that noise only helps mixing. This is the intuition we want to test. A related but different phenomenon is Gács' counterexample to the positive rates conjecture (P. Gács, *J. Stat. Phys.* 103, 2001), where non-ergodicity survives all small noise.

First result: noise towards one spin value can destroy ergodicity of a monotone system without absorbing state ([entry 0003](entries/0003-directed-noise-cancels-ising-field/)).

### 2. Is every stationary measure reversible as soon as one reversible measure exists?

For stochastic Ising models on $\mathbb{Z}^d$ (spin systems that are reversible with respect to the Gibbs measures of a finite-range interaction):

- Holley (1971): every **translation-invariant** stationary measure is a Gibbs measure, in every dimension;
- Holley and Stroock (1977): for $d \le 2$, **every** stationary measure is a Gibbs measure, and hence reversible.

Whether the second statement holds for $d \ge 3$ is open (see Liggett 1985, Ch. IV). More generally: if an IPS has at least one reversible measure, must every stationary measure be reversible? And under which hypotheses (finite range, strictly positive rates, translation-invariant rates, spin system vs. conservative dynamics)?

Some care is needed even to state this correctly. For instance, for nearest-neighbour asymmetric simple exclusion on $\mathbb{Z}$, the blocking measures are reversible, while the Bernoulli product measures are stationary but not reversible (Liggett 1999, Part III). So any positive statement needs hypotheses that rule out conservative dynamics of this kind. Writing down cases like this, and finding out exactly where the boundary lies, is the purpose of this repository. See [entry 0001](entries/0001-asep-blocking-vs-product-measures/) (ASEP) and [entry 0002](entries/0002-sep-two-half-spaces-z3/) (a finite-energy example for symmetric exclusion on a transient subgraph of $\mathbb{Z}^3$).

## Counterexamples

A summary of all entries, one paragraph each with links to the full write-ups, is in [`pdf/overview.pdf`](pdf/overview.pdf).

- **[0001 – One reversible measure, but a non-reversible stationary measure (ASEP on $\mathbb{Z}$)](entries/0001-asep-blocking-vs-product-measures/)** · `plausible` · [PDF](pdf/0001-asep-blocking-vs-product-measures.pdf)  
  If an IPS has a reversible measure, is every stationary measure reversible? Not for conservative dynamics: for nearest-neighbour asymmetric simple exclusion the blocking measures are reversible, while the Bernoulli product measures are stationary, carry a current, and are not reversible.
- **[0002 – Symmetric exclusion on two half-spaces of $\mathbb{Z}^3$](entries/0002-sep-two-half-spaces-z3/)** · `plausible` · [PDF](pdf/0002-sep-two-half-spaces-z3.pdf)  
  Two half-spaces of $\mathbb{Z}^3$ joined by a single bond act as transient reservoirs at different densities. Symmetric exclusion then has a stationary measure with finite energy that carries a current through the bridge and is not reversible, so recurrence cannot be dropped from the conservative version of Holley–Stroock. Found by ChatGPT Astra-6.
- **[0003 – Directed noise can destroy ergodicity](entries/0003-directed-noise-cancels-ising-field/)** · `plausible` · [PDF](pdf/0003-directed-noise-cancels-ising-field.pdf)  
  The absorbing state in Bérard–Dembin–Marêché's sharpness theorem cannot be dropped. For an Ising-type dynamics with constant down-rate, directed noise is the same as lowering the external field: an ergodic system at field $h = \tfrac12\log(1+\varepsilon) > 0$ becomes, after adding noise of rate $\varepsilon$, a system at zero field, which for $d \ge 2$, $\beta > \beta_c$ has two stationary measures.

## What we collect

Each question in this repository is documented in three layers:

1. **Raw AI outputs.** Unedited transcripts of AI-generated attempts (proofs, constructions, counterexamples, failed arguments). They are kept verbatim, including mistakes, so that the provenance of an idea is transparent and so we can learn what such systems get right and wrong.
2. **Digestions.** Human-written (or human-checked) accounts of what the raw output actually shows: a clean statement, a verified construction, the key mechanism, and a short "why intuition fails here" section. A digestion is the part of an entry meant to be read.
3. **Follow-up questions.** New problems raised by the counterexample: weakened or strengthened versions of the original claim, missing hypotheses, borderline cases, and connections to known open problems.

## Repository layout

```
counterexamples-ips/
├── README.md
├── CONTRIBUTING.md            # conventions and review process
├── entries/
│   └── NNNN-short-slug/       # one folder per question
│       ├── question.md        # the claim being tested, with references
│       ├── raw/               # verbatim AI outputs, one file per run
│       │   └── YYYY-MM-DD_model-name.md
│       ├── digest.md          # the cleaned-up, verified counterexample
│       ├── followups.md       # questions raised by this entry
│       └── code/              # optional: simulations and figures
├── pdf/                       # PDF of each counterexample (NNNN-short-slug.pdf) and overview.pdf
├── problems/                  # open problems and future directions not yet tied to an entry
└── templates/                 # templates for question.md, digest.md, followups.md
```

Entry folders are numbered in order of creation (`0001-…`, `0002-…`) and get a short descriptive slug, e.g. `0001-asep-blocking-vs-product-measures`.

## Format of an entry

**`question.md`**

- The claim, stated precisely: state space, rates or generator, and which notion is meant (stationary, reversible, ergodic, attractive, translation invariant, …).
- Where the question comes from (a section of Liggett, a paper, a seminar discussion).
- What is known: partial positive results and the regimes where the claim holds.

**`raw/*.md`**

- Model name and version, date, and the full prompt(s) used.
- The output, copied **verbatim**. Fix nothing here; comments go into the digest.

**`digest.md`**

- **Status** (see below).
- **Statement**: the counterexample as a precise proposition.
- **Construction and proof**: complete and self-contained, or with exact references.
- **Mechanism**: one or two paragraphs, plus a picture or simulation if it helps, explaining what goes wrong.
- **Which hypothesis breaks**: what would need to be added to rescue the claim.
- **Assessment of the raw output**: what was correct, what was wrong or missing, and how much human input the final argument needed.

**`followups.md`**

- A numbered list of new questions, each tagged `open`, `known` (with a reference), or `resolved in entry NNNN`.

### Status labels

| Label | Meaning |
|---|---|
| `verified` | The counterexample has been checked in full by at least one human (name in the digest). |
| `plausible` | The argument looks right, but some steps are still unchecked. |
| `unchecked` | Raw output only; no digestion yet. |
| `refuted` | The proposed counterexample is wrong. Kept on purpose, with an explanation, because failed attempts are informative too. |

## Conventions

- Notation follows Liggett (1985) unless an entry says otherwise. Configurations are $\eta \in \{0,1\}^S$ (often $S = \mathbb{Z}^d$), flip rates are $c(x,\eta)$, the generator is $\Omega$ (or $L$), the semigroup is $S(t)$, the set of stationary measures is $\mathcal{I}$, and the translation-invariant ones are $\mathcal{S}$.
- "Ergodic" means: there is a unique stationary measure $\mu$, and $\nu S(t) \to \mu$ weakly for every initial distribution $\nu$ (Liggett's convention). Entries that use a weaker notion must say so.
- Mathematics is written in GitHub-flavoured Markdown with `$…$` / `$$…$$`. Longer arguments can also go in a LaTeX file in the entry folder, together with the compiled PDF.
- Each counterexample with status `plausible` or `verified` should also have a PDF version in `pdf/NNNN-short-slug.pdf`, regenerated whenever the digest changes. New entries are added to the list above and to `pdf/overview.tex`, and `pdf/overview.pdf` is rebuilt.
- Simulation code, if any, goes in `entries/NNNN-…/code/` and should run from a fresh checkout.

## Contributing

Contributions are welcome, including single raw outputs without a digestion.

1. Open an issue that states the question (or pick an existing one from `problems/`).
2. Add an entry folder following the layout above. Raw outputs may be added with status `unchecked`.
3. Digestions should be reviewed by someone other than the author before they are marked `verified`.
4. Please cite sources precisely (book, chapter, theorem number), and declare AI involvement in every entry.

## Citing

If you use material from this repository, please cite the repository and the specific entry, and credit the people (and, where relevant, the AI systems) listed in it.

## License

MIT, see [`LICENSE`](LICENSE).
