from traceback import print_tb
from src.algorithms.pso import Swarm
from src.functions import *
from src.algorithms import *
from src.metrics.plots import plot

results = []
for function, domain in zip (function_dict.values(), domains):
    swarm = Swarm(100, 30, function, domain, 0.2, 0.3)
    results.append(swarm.train(5000))
plot("test", function_dict.keys(), results)
