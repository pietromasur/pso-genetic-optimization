from traceback import print_tb
from unittest import result
from src.algorithms.pso import Swarm
from src.functions import *
from src.algorithms import *
from src.metrics.plots import plot
import random



def pso_exp(functions, num_particles, c1_c2, exp_alias = "", epochs = 80, normalized = False):
    results = []
    for num_particle in num_particles:
        for c1, c2 in c1_c2:
            for function, domain in zip (functions.values(), domains):
                experiment_alias = "{}_swarm_size_{}_c1_{}_c2_{}".format(exp_alias, num_particle, c1, c2)
                print(str(function)+experiment_alias)
                swarm = Swarm(num_particle, 30, function, domain, 0.2, 0.3)
                result = swarm.train(epochs)
                results.append(result)

            plot(experiment_alias, functions.keys(), results, normalized)
            results = []


# for function, domain in zip(function_dict.values(), domains):
#     pop = Population(1000, 30, function, domain)
#     result = evolve(pop, 1000, 0.8, 0.3, debug=False, progress_bar=True)
#     print(result)

def main():
    num_particles = [10,20,30]
    c1_c2 = [(0.5,0.5), (0.3, 0.7), (0.7, 0.3)]
    ex0 = function_dict.copy()
    ex1 = function_dict.copy()
    del ex1['schwefel'] 
    ex2 = {'schwefel':function_dict['schwefel']}
    pso_exp(ex0, num_particles, c1_c2, "All", epochs = 10000)
    pso_exp(ex1, num_particles, c1_c2)
    pso_exp(ex2, num_particles, c1_c2, "schwefel", epochs = 10000, normalized=True)

if __name__ == "__main__":
    main()