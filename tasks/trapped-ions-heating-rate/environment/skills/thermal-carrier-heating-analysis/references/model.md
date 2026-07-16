# Nine-ion carrier thermometry model

## Data reduction

For each HDF5 file, read:

- `datasets/rabi_t`, in microseconds;
- `datasets/pmt_counts_avg_thresholded`, the total thresholded fluorescence from the nine-ion chain.

The acquisition contains a 0–200 us scan. Use the notebook-selected fit windows:

| Delay | File | Discard from tail |
|---:|---|---:|
| 0 us | `delay_0us.h5` | 10 points |
| 300 us | `delay_300us.h5` | 10 points |
| 500 us | `delay_500us.h5` | 10 points |
| 1000 us | `delay_1000us.h5` | 9 points |

Convert fluorescence to normalized excitation with

\[
P_{\mathrm{exc}}(t)=
\frac{\max(C)-C(t)}
{\max\left[\max(C)-C(t)\right]}.
\]

## COM Lamb-Dicke parameter

For nine identical ions in the COM mode,

\[
\eta_{\mathrm{COM}}=
\frac{2\pi}{\lambda}
\sqrt{\frac{\hbar}{2m\omega_z}}
\frac{1}{\sqrt{9}},
\]

using \(\lambda=729\) nm, \(m=6.6551079\times10^{-26}\) kg, and
\(\omega_z=2\pi\times0.177\) MHz.

## Thermal carrier probability

For a thermal occupation \(\bar n\), truncate the sum at \(n=500\):

\[
P(t)=\frac12-\frac12\sum_{n=0}^{499}
\frac{(\bar n/(\bar n+1))^n}{\bar n+1}
\cos\left(2\pi\Omega_n t\right),
\]

with the fourth-order Lamb-Dicke correction

\[
\Omega_n=\Omega_0\left[
1-\eta^2\left(n+\frac12\right)
+\frac{\eta^4}{8}\left(1+2n(n+1)\right)
\right].
\]

Average this probability over all nine supplied beam-intensity factors. Fit
amplitude, base Rabi frequency, offset, and \(\bar n\) simultaneously by
nonlinear least squares.

Use starting points `(1, 0.04, 0.1, 20)`, `(1, 0.03, 0.1, 20)`,
`(1, 0.03, 0.1, 20)`, and `(1, 0.01, 0.1, 0)` in delay order. Estimate
one-standard-error parameter uncertainties from the fit covariance.

## Heating rate

Fit a straight line to the four fitted occupations versus delay in
microseconds. The slope is initially in quanta/us. Multiply it by \(10^6\) to
report quanta/s.
