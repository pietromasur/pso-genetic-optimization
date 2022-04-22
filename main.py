from traceback import print_tb
from unittest import result
from src.algorithms.pso import Swarm
from src.functions import *
from src.algorithms import *
from src.metrics.plots import plot

results = []
num_particles = [10,20,30]
c1_c2 = [(0.5,0.5), (0.3, 0.7), (0.7, 0.3)]
for num_particle in num_particles:
    for c1, c2 in c1_c2:
        for function, domain in zip (function_dict.values(), domains):

            experiment_alias = "swarm_size_{}_c1_{}_c2_{}".format(num_particle, c1, c2)
            print(str(function)+experiment_alias)
            swarm = Swarm(num_particle, 30, function, domain, 0.2, 0.3)
            result = swarm.train(100)
            results.append(result)
            
        plot(experiment_alias, function_dict.keys(), results, normalized=False)
        results = []
