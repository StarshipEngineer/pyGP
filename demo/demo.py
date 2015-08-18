#!/usr/bin/python3
from pyGP.pyGP import components as pygp
from random import random, randint
from copy import deepcopy


"""Prepatory steps"""


"""Steps 1 & 2
Specify the function and terminal sets.
"""
p = pygp.primitives
v = ["x"]
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)


"""Step 3
Define the fitness measure. This is the pygp.fitness function found
in the pygp module; the data this fitness function will use to evaluate evolved
programs and determine their fitnesses is imported below.
"""
filename = "datafile.csv"
data = pygp.read_data(filename)


"""Step 4
Set run parameters.
"""
popsize = 1000
max_depth = 3
cross_rate = 0.90
rep_rate = 0.98
mut_rate = 1.0
tourn_size = 5


"""Step 5
Specify termination condition.
"""
target_fitness = 0.00001


"""Running GP"""


"""Initialization
An initial population is generated, in this case using the ramped half-and-half
technique.
"""
def ramped(popsize, p, s, max_depth):
    """Initializes and returns a population using the ramped half-and-half
    technique, where half the initial population is generated with grow and the
    other half with full, using a range of depths. This function can also be
    found in the majorelements module, but is shown here for illustration.
    """
    pop = []
    half = int(popsize / 2)
    for i in range(1, half):
        pop.append(pygp.BinaryTree(p, s, "full", randint(1, max_depth)))
        
    for i in range(half, popsize+1):
        pop.append(pygp.BinaryTree(p, s, "grow", randint(1, max_depth)))

    return pop


pop = ramped(popsize, p, s, max_depth)


"""Evolve the population toward a solution
Continue evolving the population until an individual
meeting the target fitness is found.
"""
def evolve(pop, generation=1):
    """This function examines each generation of programs, and if none meet
    the termination criterion, evolves a new generation and calls itself
    until an individual is found which satisfies the termination criterion,
    at which point it returns a dictionary with the solution program and
    other info. This function can also be found in the majorelements module, but
    is shown here for illustration.
    """
    print(generation)
    best_in_gen = pygp.termination_test(pop, data) # include a program return
    
    if best_in_gen[1] < target_fitness:
        return {"best":best_in_gen[0], "score":best_in_gen[1],
                "gen": generation}

    # if above fitness test fails, produce a new generation
    next_gen = []
    for i in range(len(pop)):
        choice = random()
        if choice < cross_rate:
            child = pygp.subtree_crossover(pop, tourn_size, data)
        elif choice < rep_rate:
            child = pygp.reproduction(pop, tourn_size, data)
        elif choice < mut_rate:
            child = pygp.subtree_mutation(pop[i], max_depth)

        next_gen.append(child)

    # After producing a new generation, call recursively
    return evolve(next_gen, generation+1)


"""Results of the run"""
solutioninfo = evolve(pop)
winner = deepcopy(solutioninfo["best"])
print("The winning program is:")
print(winner.display())
print("Its fitness score was", solutioninfo["score"],
      "and it appeared in generation", solutioninfo["gen"])
print()
