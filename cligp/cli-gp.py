#!/usr/bin/python3
from pyGP.pyGP import pygp
import math
import random
from copy import deepcopy


filename = input("Enter the name of the file containing fitness data: ")
data = pygp.read_data(filename)


p = pygp.primitives
v = ["x"] # enter variables
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)


settings = open("settings.txt", "r")
for line in settings:
    eval(line)
settings.close()


# Make a function, add to pygp
pop = []
half = int(popsize / 2)
for i in range(1, half):
    pop.append(pygp.BinaryTree(p, s, "full", random.randint(1, max_depth)))
    
for i in range(half, popsize+1):
    pop.append(pygp.BinaryTree(p, s, "grow", random.randint(1, max_depth)))


# Add function to pygp
def evolve(pop, generation=1):
    """This function examines each generation of programs, and if none meet
    the termination criterion, evolves a new generation and calls itself
    until an individual is found which satisfies the termination criterion,
    at which point it returns a dictionary with the solution program and
    other info.
    """
    print(generation)
    best_in_gen = pygp.termination_test(pop, data)    
    if best_in_gen[1] < target_fitness:
        return {"best":best_in_gen[0], "score":best_in_gen[1],
                "gen": generation}

    next_gen = []
    for i in range(len(pop)):
        choice = random.random()
        if choice < cross_rate:
            child = pygp.subtree_crossover(pop, tourn_size, data)
        elif choice < rep_rate:
            child = pygp.reproduction(pop, tourn_size, data)
        elif choice < mut_rate:
            child = pygp.subtree_mutation(pop[i], max_depth)

        next_gen.append(child)

    return evolve(next_gen, generation+1)


solutioninfo = evolve(pop)
winner = deepcopy(solutioninfo["best"])
print("The winning program is:")
print(winner.display())
print("Its fitness score was", solutioninfo["score"],
      "and it appeared in generation", solutioninfo["gen"])
print()
