"""Illustration for entry 0003: directed noise cancelling the field of an Ising-type spin system.

Spin system on the torus (Z/nZ)^2 with spins +1/-1 and, writing S_x for the sum of the four
neighbouring spins,

    rate(-1 -> +1) = (1 + eps) * exp(2 * beta * S_x)        (depends on the neighbourhood)
    rate(+1 -> -1) = 1 + noise                               (constant)

noise = 0   : the process L, reversible for Ising(beta, h) with h = log(1 + eps) / 2 > 0.
noise = eps : the process L_eps, a time change of a process reversible for Ising(beta, 0).

Time stepping: alternating checkerboard half-steps. Sites of one colour do not interact, so with
the other colour frozen each site evolves as an independent two-state chain for time dt, and its
transition probabilities are used exactly (Trotter splitting, error O(dt)).

This is an illustration only: on a finite torus every such chain is ergodic, and the plateaux of
L_eps are metastable states with astronomically long lifetimes.

Usage: python3 simulate.py [--n 200] [--beta 0.5] [--eps 1.0] [--T 40] [--dt 0.02] [--seed 1]
Writes magnetisation.csv and magnetisation.pdf/.png into the current directory.
"""

import argparse
import csv

import numpy as np


def simulate(n, beta, eps, noise, T, dt, init, rng):
    sigma = np.full((n, n), init, dtype=np.int8)
    ii, jj = np.indices((n, n))
    masks = [((ii + jj) % 2) == p for p in (0, 1)]
    b = 1.0 + noise
    times, mags = [0.0], [float(sigma.mean())]
    for k in range(1, int(round(T / dt)) + 1):
        for mask in masks:
            s = (np.roll(sigma, 1, 0) + np.roll(sigma, -1, 0)
                 + np.roll(sigma, 1, 1) + np.roll(sigma, -1, 1)).astype(float)
            a = (1.0 + eps) * np.exp(2.0 * beta * s)
            r = a + b
            decay = np.exp(-r * dt)
            p_plus_from_minus = a / r * (1.0 - decay)
            p_plus_from_plus = a / r + b / r * decay
            u = rng.random((n, n))
            plus = np.where(sigma == 1, u < p_plus_from_plus, u < p_plus_from_minus)
            new = np.where(plus, 1, -1).astype(np.int8)
            sigma = np.where(mask, new, sigma)
        times.append(k * dt)
        mags.append(float(sigma.mean()))
    return np.array(times), np.array(mags)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--beta", type=float, default=0.5)
    ap.add_argument("--eps", type=float, default=1.0)
    ap.add_argument("--T", type=float, default=40.0)
    ap.add_argument("--dt", type=float, default=0.02)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)

    runs = {}
    for name, noise in (("L", 0.0), ("L_eps", args.eps)):
        for init in (+1, -1):
            runs[(name, init)] = simulate(args.n, args.beta, args.eps, noise, args.T, args.dt, init, rng)

    t = runs[("L", 1)][0]
    with open("magnetisation.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "L_from_plus", "L_from_minus", "Leps_from_plus", "Leps_from_minus"])
        for k in range(len(t)):
            w.writerow([f"{t[k]:.4f}"] + [f"{runs[key][1][k]:.5f}" for key in
                                           (("L", 1), ("L", -1), ("L_eps", 1), ("L_eps", -1))])

    # Onsager-Yang spontaneous magnetisation of the 2D Ising model at zero field.
    sh = np.sinh(2 * args.beta)
    m_star = (1 - sh ** -4) ** 0.125 if sh > 1 else 0.0

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ink, muted, grid = "#0b0b0b", "#52514e", "#e4e3df"
    c_plus, c_minus = "#2a78d6", "#eb6834"  # categorical slots 1 and 2
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": muted, "axes.labelcolor": ink,
                         "xtick.color": muted, "ytick.color": muted, "font.family": "serif",
                         "mathtext.fontset": "cm"})
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.6), sharey=True)
    titles = {"L": r"$L$: field $h=\frac{1}{2}\log(1+\varepsilon)>0$",
              "L_eps": r"$L_\varepsilon$: noise cancels the field ($h=0$)"}
    for ax, name in zip(axes, ("L", "L_eps")):
        ax.grid(True, color=grid, linewidth=0.6)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        if name == "L":
            ax.text(0.97 * args.T, 0.78, "both starts reach\nthe same limit", color=muted,
                    ha="right", va="top", fontsize=8)
        if name == "L_eps" and m_star > 0:
            ax.text(0.97 * args.T, m_star - 0.07, rf"plateau at $m^*(\beta)\approx{m_star:.3f}$",
                    color=muted, ha="right", va="top", fontsize=8)
            ax.text(0.97 * args.T, -m_star + 0.07, r"plateau at $-m^*(\beta)$",
                    color=muted, ha="right", va="bottom", fontsize=8)
        for init, col, lab in ((1, c_plus, "start all $+1$"), (-1, c_minus, "start all $-1$")):
            tt, mm = runs[(name, init)]
            ax.plot(tt, mm, color=col, linewidth=1.6, label=lab)
        ax.set_title(titles[name], fontsize=9, color=ink)
        ax.set_xlabel("time $t$")
        ax.set_xlim(0, args.T)
        ax.set_ylim(-1.05, 1.05)
    axes[0].set_ylabel("magnetisation")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False, fontsize=8,
               bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig("magnetisation.pdf")
    fig.savefig("magnetisation.png", dpi=200)
    print(f"m* = {m_star:.4f}")
    for key, (tt, mm) in runs.items():
        print(key, "final m =", round(mm[-1], 4))


if __name__ == "__main__":
    main()
