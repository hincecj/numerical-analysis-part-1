# numerical-analysis-part-1

Two Python simulations built around a forward finite-difference method for
numerically solving ordinary differential equations, derived and explained in
[*Numerical Analysis: A Tourist's Guide, Part 1*](https://hincecj.github.io/cooperhince/papers/numerical_analysis_part_1.pdf).

## Contents

- `Three_body_problem.py` — simulates three gravitationally-interacting
  bodies in 2D, animated live with matplotlib.
- `Damped_pendulum.py` — simulates a damped pendulum's swing over time,
  animated the same way.

## Requirements

```
pip install numpy matplotlib
```

## Running

```
python Three_body_problem.py
python Damped_pendulum.py
```

Each opens a live matplotlib window and animates until you close it.

## Three_body_problem.py

Simulates three bodies of given mass under mutual gravity, using the
second-order finite-difference recursion derived in the write-up. The
default initial conditions produce a stable, periodic orbit.

Three other configurations are included as commented-out blocks, ready to
use by uncommenting them (and commenting out the default block above them):

- **Figure eight** — the well-known figure-eight three-body orbit
- **In line** — three bodies starting collinear
- **Sun, Earth, Mars** — unequal masses, roughly modelled on the solar system

Adjustable parameters at the top of the file: `G` (gravitational constant),
`h` (time step), `n` (iterations), `a` (plot boundary), and each body's
mass, initial position and initial velocity.

## Damped_pendulum.py

Simulates a single pendulum with linear drag, applying the same
finite-difference approach to a second-order ODE.

Adjustable parameters: `g` (gravitational acceleration), `h` (time step),
`n` (iterations), `l` (rod length), `a0` (initial angle, in radians), `m`
(mass), and `mu` (drag coefficient).

## Notes

Both scripts implement the recursion derived in Part 1 of the Numerical
Analysis series — see the write-up linked above for the full derivation.
Truncation error and energy conservation aren't accounted for in either
script; these are basic implementations of the underlying numerical idea,
not physically rigorous simulations.
