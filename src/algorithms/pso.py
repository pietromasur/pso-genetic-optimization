import random
import numpy as np

class Swarm():
    def __init__(self, num_particles, num_dimensions, objective_function, domain, c1, c2) -> None:
        """
        num_particles: number of entities in the swarm
        num_dimensions: number of dimensions on the location vector
        objective_function: the functions that will be updated
        domain: the domain to be explored by the swarm [x,y]
        c1: pso constant
        c2: pso constant
        """
        self.num_particles = num_particles
        self.num_dimensions = num_dimensions
        self.objective_function = objective_function
        self.domain = domain
        self.c1 = c1
        self.c2 = c2
        self.particles = list()
        for i in range (self.num_particles):
            self.particles.append(Particle(num_dimensions, objective_function, domain, c1, c2))
        self.gbest = np.array([])
        self.gbest_fitness = 0
    def update_particles(self):
        for particle in self.particles:
            particle.update_particle()
    def update_gbest(self):
        pbests = []
        pbests_fitness = []
        for particle in self.particles:
            pbest, pbest_fitness = particle.get_pbest()
            pbests.append(pbest)
            pbests_fitness.append(pbest_fitness)
        
        self.gbest_fitness = min(pbests_fitness)
        self.gbest = pbests[pbests_fitness.index(self.gbest_fitness)]
        for particle in self.particles:
            particle.update_gbest(self.gbest, self.gbest_fitness)
    def train(self, epochs, criteria = 300):
        #TODO implement stopping criteria
        gbests = []
        #Manage over-computing
        best = 10000000
        counter = 0
        for i in range(epochs):
            c_best = self.gbest_fitness
            gbests.append(c_best)
            if (best>c_best):
                best = c_best
                counter = 0
            else:
                counter+=1
            if (counter == criteria):
                break
            self.update_particles()
            self.update_gbest()
        gbests.append(self.gbest_fitness)
        #Avoid uneven returns
        while(len(gbests)<epochs):
            gbests.append(self.gbest_fitness)
        return gbests

class Particle():

    def __init__(self, num_dimensions, objective_function, domain, c1, c2) -> None:
        self.num_dimensions = num_dimensions
        self.objective_function = objective_function
        self.domain = domain
        self.location = np.array([random.uniform(domain[0], domain[1]) for i in range(num_dimensions)])
        #PSO attributes
        self.fitness = objective_function(self.location)
        self.pbest = self.location
        self.pbest_fitness = self.fitness
        self.gbest = np.array([])
        self.gbest_fitness = 0
        self.speed = np.zeros(num_dimensions)
        self.c1 = c1
        self.c2 = c2
    def update_location(self):
        self.location = self.location + self.speed
        self.fitness = self.objective_function(self.location)
    def update_pbest(self):
        if (self.fitness<=self.pbest_fitness):
            self.pbest = self.location
            self.pbest_fitness = self.objective_function(self.pbest)
    def update_speed(self):
        r1 = random.random()
        r2 = random.random()
        for i, (spd, pbst, gbst, lct) in enumerate (zip (self.speed, self.gbest, self.pbest, self.location)):
            self.speed[i] = spd + self.c1*r1*(pbst-lct) + self.c2*r2*(gbst-lct)
   
    def update_particle(self):
        #method to update partcle speed and location, called by the Swarm class at each iteration
        self.update_speed()
        self.update_location()
        self.update_pbest()
    def update_gbest(self, new_gbest, new_gbest_fitness):
        self.gbest = new_gbest
        self.gbest_fitness = new_gbest_fitness
    def get_pbest(self):
            return self.pbest, self.pbest_fitness

