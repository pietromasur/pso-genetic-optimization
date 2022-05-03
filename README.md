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
All experiments we performed are a mean of 30 executations of the algorithm.
## PSO  
We have defined a grid with the following parameters for experiments on the functions to be optimized:
- Swarm size [10,20,30]
- Cognitive Coefficient (c1) [0.3,0.5,0.7]
- Social Coefficient (c2) [0.3,0.5,0.7]
The number of epochs was set after experimenting with large values and watching we're convergence would happen. We also set a stopping criteria to activate when a experiment has no improve during a thousand epochs.  
  
The first four functions we experimented on [Ackely,Levy, Rastrigin, Rosenbrock], the algorithm converged to the same point, without variation for every combination of swarm size, cognitive and social coefficient we've explored. The following graphic shows the results on a size 10 swarm with cognitive and social coefficient set to 0.5:  
![image](https://drive.google.com/uc?export=view&id=1KVRF0PkziVzUU6tvLSH2znRtPbH9oPyZ)  
However, for the Schwefel we faced a greater problem complexity. We've tried experimenting with various values for c1 and c2 and also set the experiments running for a greater number of epochs. The constants c1 and c2 seem to have had little to no effect on the convergence value, whereas the swarm size semeed to have a greater influence on the final convergence value.
- Swarm size 10, c1 0.5, c2 0.5  
![image](https://drive.google.com/uc?export=view&id=1Roj5GNFchUfGMc6qFgqbmfJXMSrC-Eel)  
- Swarm size 20, c1 0.5, c2 0.5  
![image](https://drive.google.com/uc?export=view&id=1KUiANnRRJX3mKUss0J4gJRSTbwJ1jpD-)  
- Swarm size 30, c1 0.5, c2 0.5  
![image](https://drive.google.com/uc?export=view&id=1KVRF0PkziVzUU6tvLSH2znRtPbH9oPyZ)  
On the following link you can find a folder containing all the experiments that were performed: https://drive.google.com/drive/folders/1rT8Mxik2OEQFYZBKnQhuK6B7rNwnbeh2?usp=sharing  
## Genetic Algorithm  
