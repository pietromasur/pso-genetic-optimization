from src.algorithms.pso import Swarm
from src.functions import *
from src.algorithms import *

swarm = Swarm(100, 30, ackley, get_acley_domain(), 0.2, 0.3)
swarm.train(200)