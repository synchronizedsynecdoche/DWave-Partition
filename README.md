# DWave-Partition
Implementation of the NP-Complete "partitioning problem": given a set $S$, does there exist a partition $P\subset S$ such that $\sum_{p\in P} p = \frac{1}{2}\sum_{s\in S}$? The QUBO formulation is sourced from [1], and the script supports DWave neal's SimulatedAnnealingSampler, as well as real quantum annealers accessed via DWaveSampler. Uses pyqubo for symbolic manipulation of our Hamiltonian $H$.
## Sources
[1] https://www.frontiersin.org/articles/10.3389/fphy.2014.00005/full