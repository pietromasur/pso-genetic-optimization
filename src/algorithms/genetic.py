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
    son1 = p1.location.copy()
    son2 = p2.location.copy()
    
    replacements = random.sample(range(p1.dimensions_count), p1.dimensions_count // 2)
    
    for i in replacements:
        son1[i], son2[i] = p2.location[i], p1.location[i]

    son1 = Individual(p1.dimensions_count, p1.fitness_func, p1.domain, son1)
    son2 = Individual(p2.dimensions_count, p2.fitness_func, p2.domain, son2)
    return son1, son2


def mutate(ind):
    pos = random.sample(range(ind.dimensions_count), int(ind.dimensions_count * 1/3))

    offset = np.random.normal(0, ind.domain[1])
    for i in pos:
        ind.location[i] += offset
        ind.location[i] = min(ind.domain[1], ind.location[i])
        ind.location[i] = max(ind.domain[0], ind.location[i])

    return ind


def select_parents(pop):
    possible_parents = np.random.choice(pop.individuals, 30, replace=False)
    possible_parents = sorted(possible_parents, key=lambda x: x.fitness)
    return possible_parents[0], possible_parents[1]


def evolve(pop, epochs, p_crossover, p_mutation, debug=False, progress_bar=False):
    iter = range(epochs)
    best_individual = None
    best_ind_list = []
    for epoch in iter:
        curr_best_individual = min(pop.individuals, key=lambda x: x.fitness)
        
        best_individual = curr_best_individual if best_individual == None or curr_best_individual.fitness < best_individual.fitness else best_individual
        best_ind_list.append(best_individual.fitness)
           
        p1, p2 = select_parents(pop)

        s1, s2 = Individual(p1.dimensions_count, p1.fitness_func, p1.domain), Individual(p2.dimensions_count, p2.fitness_func, p2.domain)

        if random.randint(1, 10) / 10 > p_crossover:
            s1, s2 = crossover(p1, p2)

        if random.randint(1, 10) / 10 > p_mutation:
            s1 = mutate(s1)
            s2 = mutate(s2)

        new_pop = pop.individuals + [s1, s2]

        new_pop = sorted(new_pop, key=lambda x: x.fitness)
        new_pop = new_pop[: pop.size]
        pop.individuals = new_pop

    return best_ind_list



