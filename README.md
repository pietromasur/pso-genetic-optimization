# PSO and Gentic Algorithm function optimization
Our project aims to benchmark the performance of two algorithms: PSO and Genetic Algorithm. For this purpose we've chosen the following functions in a 30-N dimension space:
- Ackley https://www.sfu.ca/~ssurjano/ackley.html
- Levy https://www.sfu.ca/~ssurjano/levy.html
- Rastrigin https://www.sfu.ca/~ssurjano/rastr.html
- Rosenbrock https://www.sfu.ca/~ssurjano/rosen.html
- Schwefel https://www.sfu.ca/~ssurjano/schwef.html
# Algorithms
## Particle Swarm Optimization (PSO)
PSO is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. The computation occurs in a manner that mimics the behavior of swarms when trying to reach for food. The flow of PSO can be described as:
- Initialize a swarm with randomly set particle location
- For each particle, while a stop criteria is not reached:
  - Compute the fitness value
  - Check whether the current fitness is the best solution yet on particle memory (pbest). If so, update the personal best
  - Check whether the current fitness is better than the previous best fitness known to the swarm (gbest). If so, update gbest
  - Update speed based on the the new pbest and gbest.
  - Update particle location on the function domain.
## Genetic Algorithm

# Experiments and results
