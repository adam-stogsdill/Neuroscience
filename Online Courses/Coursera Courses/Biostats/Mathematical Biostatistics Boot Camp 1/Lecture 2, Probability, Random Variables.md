## Probability

A **probability measure**, P, is a real valued function from the collection of possible events so that the following holds:

1) For an event $E \subset \Omega, 0 \leq P(E) \leq 1$
2) $P(\Omega) = 1$
3) If $E_1$ and $E_2$ are mutually exclusive events $P(E_1 \cup E_2) = P(E_1) + P(E_2)$

The third statement implies **<mark style="background: #FF5582A6;">finite additivity</mark>**

$$P(\bigcup_{i=1}^{n} A_i) = \sum_{i=1}^{n} P(A_i))$$

where the ${A_i}$ are mutually exclusive. This is usually extended to **<mark style="background: #FF5582A6;">countable additivity</mark>**

$$P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i))$$

Finite implies countable but not true in the reverse.

* P is defined on F a collection of subsets $\Omega$ (domain)
* Example $\Omega$ = {1,2,3} then
	* F = {$\emptyset$, {1}, {2}, {3}, {1,2}, {1, 3}, {2, 3}, {1, 2, 3}}.
* When $\Omega$ is a continuous set, the definition gets much trickier. In this case we assume that F is sufficiently rich so that any set that we're interested in will be in it.
## Random Variables

## PMFs and PDFs

## CDFs, survival functions and quantiles

## Summary