# A141399_Proof

Proof papers and supporting material for the claim that **$633555 \times 633556$
is the last prime-complete product of two consecutive integers** — equivalently,
that OEIS [A141399](https://oeis.org/A141399) is finite with largest term
$633555$.

A product $m(m+1)$ is **prime-complete of order $r$** if its radical (its set of
distinct prime factors) is exactly the primorial $P_r = p_1 p_2 \cdots p_r$: every
one of the first $r$ primes divides $m(m+1)$, and no other prime does. The
sequence of such $m$ is A141399; the largest known is $633555$, of order $8$.

> **Status.** The finiteness of A141399 is **not yet an established theorem.** A
> dubious finiteness claim was removed from the OEIS entry (S. A. Irvine, Mar
> 2026). This repository contains work in progress toward a rigorous proof.
> Nothing here should be read as asserting finiteness as settled fact; the
> unconditional case in particular remains open. See *Status of each result*
> below.

## The wall

The proof is organized around a single inequality between two exactly computable
sequences:

- $A_r = $ [A118478](https://oeis.org/A118478)$(r)$ — the **floor**: the least
  $m$ with $m(m+1)$ divisible by $P_r$.
- $L_r = $ [A002072](https://oeis.org/A002072)$(r)$ — the **ceiling**: the
  largest $m$ with both $m$ and $m+1$ being $p_r$-smooth.

Any prime-complete product of order $r$ satisfies $A_r \le m \le L_r$. For
$r \ge 14$ the certified data give $A_r > L_r$ (the **wall**): the interval is
empty, so no prime-complete product of order $r$ can exist. This is unconditional
arithmetic, verifiable directly from the two OEIS b-files, over the certified
range. The open problem is to prove the wall never reopens for any larger $r$.

## Contents

### Papers

- **`N2_track1.tex` / `.pdf`** — *The last prime-complete product of two
  consecutive integers, conditional on a consecutive-smooth ceiling and a
  discrete-floor growth hypothesis.* The conditional proof. Unconditional through
  the certified finite base; the tail rests on two explicitly stated, tail-only
  hypotheses (a ceiling bound and a floor-growth bound), whose relationship to
  the $abc$ conjecture is delineated precisely.
- **`N2_reduction.tex` / `.pdf`** — *A reduction theorem for prime-complete
  products of two consecutive integers.* An unconditional structure theorem:
  every prime-complete product of order $r \ge 5$ occupies one of $2^r-1$ Pell
  branches at an index constrained by three necessary conditions (fundamental
  $y$-value smooth; rank-of-apparition divisibility; primitive-divisor index
  cap). Reduces the problem to an explicitly described *small-index core*.

### A141399 edits

- Proposed OEIS example/comment material placing the terms of A141399 in the
  interval $[A_r, L_r]$, showing the nonempty orders ($r \le 8$) and the onset of
  the wall. Stated as arithmetic only; no finiteness claim.

## Status of each result

| Result | Status | Depends on |
|---|---|---|
| Squeeze $A_r \le m \le L_r$; wall $A_r > L_r \Rightarrow$ no order-$r$ solution | **proved** | elementary |
| Wall holds for $14 \le r \le$ (certified frontier) | **proved** (computational) | exhaustive certification; see coverage repos |
| Reduction Theorem (structure of any solution) | **proved** | primitive divisor theorem (Carmichael/BHV) |
| Wall holds for all $r$ (finiteness), conditional route | **conditional** | $abc$ + ceiling hypothesis + floor hypothesis |
| Wall holds for all $r$, unconditional route | **open** | the small-index core / Three-Jaw program |

The conditional and unconditional cases are the two blades of "cutting off the
tail": the first completes the proof modulo stated hypotheses; the second aspires
to remove them.

## Sequences

- [A141399](https://oeis.org/A141399) — Prime-Complete products of two consecutive integers. (this proof'ssubject).
- [A118478](https://oeis.org/A118478) — the floor $A_r$.
- [A002072](https://oeis.org/A002072) — the ceiling $L_r$.
- [A215021](https://oeis.org/A215021) — the quotient $A_r(A_r+1)/P_r$.
- [A055932](https://oeis.org/A055932) — Numbers all of whose prime divisors are consecutive primes starting at 2.
- [A385415](https://oeis.org/A385415) — Prime-Complete products of three consecutive integers.
- [A052762](https://oeis.org/A052762) — Products of four consecutive integers.
- [A385631](https://oeis.org/A385631) — Prime-Complete products of five consecutive integers.
- [A217056](https://oeis.org/A217056) - Highly composite products of four consecutive integers.
  
## Related repositories

The computational certification of the finite base lives in separate
repositories (the "coverage" stack):

- [`Ar_Solver`](https://github.com/kenatiod/Ar_Solver) — computes $A_r$ = A118478.
- [`A002072_Solver`](https://github.com/kenatiod/A002072_Solver) — computes $L_r$
  = A002072.
- [`LC_Solver`](https://github.com/kenatiod/LC_Solver) — Lehmer–Clements
  elimination engine.
- [`CRT_Pruning_Survey`](https://github.com/kenatiod/CRT_Pruning_Survey),
  [`Delta_min`](https://github.com/kenatiod/Delta_min) — supporting eliminations.

A forthcoming coverage paper will certify the finite base and serve as the
citation target for the computational range used by the proofs here.

## Building the papers

```bash
pdflatex N2_track1.tex && pdflatex N2_track1.tex
pdflatex N2_reduction.tex && pdflatex N2_reduction.tex
```
(Run twice for cross-references. No external packages beyond a standard
TeX Live installation.)

## Citing

These are working drafts. Frozen, citable versions (with DOIs) will be deposited
as the results mature; cite those in preference to this repository's `HEAD`. The
proofs form part of a planned monograph on finite-termination phenomena in
arithmetic.

## Acknowledgment

This work was developed in collaboration with Claude (Anthropic), as part of an
ongoing study of human–AI collaboration in mathematical research.

## License

MIT License — see [LICENSE](LICENSE).
