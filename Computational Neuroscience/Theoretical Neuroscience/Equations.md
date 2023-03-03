
## 1.2 Spike Trains and Firing Rates

#### Neural Response function
$\rho(t) = \sum^{n}_{i=1}\delta(t-t_i)$

#### $\delta$ Function
$\int\delta(t-\tau)h(\tau)d\tau = h(t)$, provided the limits of the integral surrounded the point $t$.

#### Spike-Count Rate (r)
$r = \frac{n}{T} = \frac{1}{T}\int^{T}_{0}\rho(\tau)d\tau$,
where $n=$ number of spikes in trial, and $T=$ the period of the trial

#### Firing Rate (r(t))
$r(t) = \frac{1}{\Delta t}\int^{t + \Delta t}_{t}<\rho(\tau)>d\tau$

#### Average Firing Rate
$<r> = \frac{<n>}{T} = \frac{1}{T}\int^{T}_{0}<\rho(\tau)>d\tau = \frac{1}{T}\int^{T}_{0}r(t)dt$ ^518f0a

#### Response Tuning Curve (Spikes/Second(Hz))
$<r> = f(s)$, where $s$ is the stimulus!

