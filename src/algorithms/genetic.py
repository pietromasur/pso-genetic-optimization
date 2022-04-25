import random
import numpy as np


class Individual:
    def __init__(self, dimensions_count, fitness_func, domain, array=None) -> None:
        self.dimensions_count = dimensions_count
        self.fitness_func = fitness_func
        self.domain = domain
        if type(array) is np.ndarray:
            self.location = array
        else:
            self.location = np.array([random.uniform(domain[0], domain[1]) for i in range(dimensions_count)])

    @property
    def fitness(self):
        return self.fitness_func(self.location)


class Population:
    def __init__(self, size, dimensions_count, fitness_func, domain) -> None:
        self.size = size
        self.dimensions_count = dimensions_count
        self.fitness_func = fitness_func
        self.domain = domain
        self.individuals = [
            Individual(dimensions_count, fitness_func, domain) for i in range(size)
        ]


def crossover(p1, p2):
    son1 = p1.location[:4]
    son2 = p2.location[:4]

    son1 = np.append(son1, p2.location[4:])
    son2 = np.append(son2, p1.location[4:])

    son1 = Individual(p1.dimensions_count, p1.fitness_func, p1.domain, son1)
    son2 = Individual(p2.dimensions_count, p2.fitness_func, p2.domain, son2)
    return son1, son2


def mutate(ind):
    pos = random.randint(0, ind.dimensions_count - 1)

    ind.location[pos] = random.uniform(ind.domain[0], ind.domain[1])

    return ind


def select_parents(pop):
    possible_parents = np.random.choice(pop.individuals, 5)
    possible_parents = sorted(possible_parents, key=lambda x: x.fitness)

    return possible_parents[0], possible_parents[1]


def evolve(pop, epochs, p_crossover, p_mutation, debug=False, progress_bar=False):
    iter = range(epochs)
    best_individual = None
    for epoch in iter:
        curr_best_individual = min(pop.individuals, key=lambda x: x.fitness)
        
        best_individual = curr_best_individual if best_individual == None or curr_best_individual.fitness < best_individual.fitness else best_individual
        
        p1, p2 = select_parents(pop)

        s1, s2 = p1, p2

        if random.randint(1, 10) / 10 > p_crossover:
            s1, s2 = crossover(p1, p2)

        if random.randint(1, 10) / 10 > p_mutation:
            s1 = mutate(s1)
            s2 = mutate(s2)

        new_pop = pop.individuals + [s1, s2]

        new_pop = sorted(new_pop, key=lambda x: x.fitness)
        new_pop = new_pop[: pop.size]
        pop.individuals = new_pop

    return best_individual.fitness, best_individual.location



