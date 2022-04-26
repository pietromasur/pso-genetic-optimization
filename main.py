from traceback import print_tb
from unittest import result

from numpy import average, single, zeros
from src.algorithms.pso import Swarm
from src.functions import *
from src.algorithms import *
from src.metrics.plots import plot
import random


def pso_exp(functions, num_particles, c1_c2, exp_alias="", epochs=20, normalized=False):
    results = []
    for num_particle in num_particles:
        for c1, c2 in c1_c2:
            for function, domain in zip(functions.values(), domains):
                experiment_alias = "{}_swarm_size_{}_c1_{}_c2_{}".format(
                    exp_alias, num_particle, c1, c2
                )
                print(str(function) + experiment_alias)
                single_run_results = []
                # Geting the average result, for trust sake
                for i in range(100):
                    swarm = Swarm(num_particle, 30, function, domain, 0.2, 0.3)
                    result = swarm.train(epochs)
                    single_run_results.append(result)

                average_result = zeros(epochs)
                for i in range(epochs):
                    for j in range(len(single_run_results)):
                        average_result[i] += single_run_results[j][i]
                    average_result[i] = average_result[i] / len(single_run_results)
                results.append(average_result)

            plot(experiment_alias, functions.keys(), results, normalized)
            results = []


def pso():
    num_particles = [10, 20, 30]
    c1_c2 = [(0.5, 0.5), (0.3, 0.7), (0.7, 0.3)]
    ex0 = function_dict.copy()
    ex1 = function_dict.copy()
    del ex1["schwefel"]
    ex2 = {"schwefel": function_dict["schwefel"]}
    pso_exp(ex0, num_particles, c1_c2, "All", epochs=10000)
    pso_exp(ex1, num_particles, c1_c2)
    pso_exp(ex2, num_particles, c1_c2, "schwefel", epochs=1000)


def ga():
    #del function_dict["schwefel"]
    #del function_dict["rosenbrock"]
    epochs = 400
    results = []
    for function, domain in zip(function_dict.values(), domains):
        single_run_results = []
        for _ in range(1):
            pop = Population(300, 10, function, domain)
            single_run_results.append(evolve(pop, epochs, 0.7, 0.6, False, False))
        
        avarage_results = zeros(epochs)
        for i in range(epochs):
            for j in range(len(single_run_results)):
                avarage_results[i] += single_run_results[j][i]
            avarage_results[i] = avarage_results[i] / len(single_run_results)
        results.append(avarage_results)
        print(avarage_results)
    print(results)
    plot("ga", function_dict.keys(), results, False)


if __name__ == "__main__":
    #pso()
    ga()
