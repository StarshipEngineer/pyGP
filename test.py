#!/usr/bin/python3
import pygp
import math
import random


"""Prepatory steps"""


"""Steps 1 & 2
Specify the function and terminal sets.
"""
p = pygp.primitives
v = ["r"]
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)


"""Step 3
Define the fitness measure. This is the pygp.fitness function found
in the pygp module; the data this fitness function will use to evaluate evolved
programs and determine their fitnesses is imported below.
"""
filename = "circlearea.csv"
data = pygp.read_data(filename)


"""Step 4
Set run parameters.
"""
popsize = 20
max_depth = 3
cross_rate = 0.90
rep_rate = 0.98
mut_rate = 1.0
tourn_size = 10


"""Step 5
Specify termination condition.
"""
target_fitness = 1


"""Running GP"""
tree = pygp.BinaryTree(p, s, ["*", "math.pi", "*", None, None, "r", "r"])
print(pygp.tree_list(tree))
print(tree.build_program())
print(pygp.fitness(tree, data))

##pop = [pygp.BinaryTree(p, s, 'grow', 2) for i in range(1000)]
##winner = pygp.tournament(pop, 5, data)

##try:
##    score = pygp.fitness(tree, data)
##    print(score)
##except SingularityError:
##    pass




"""Initialization
An initial population is generated, in this case using the ramped half-and-half
technique, where half the initial population is generated with grow and the
other half with full, using a variety of depths.
"""
##pop = []
##half = int(popsize / 2)
##for i in range(1, half):
##    pop.append(pygp.BinaryTree(p, s, "full", random.randint(1, max_depth)))
##    
##for i in range(half, popsize+1):
##    pop.append(pygp.BinaryTree(p, s, "grow", random.randint(1, max_depth)))
##
##
##"""Evolve the population toward a solution
##Continue evolving the population until an individual
##meeting the target fitness is found.
##"""
##def evolve(pop, generation=1):
##    """This function examines each generation of programs, and if none meet
##    the termination criterion, evolves a new generation and calls itself
##    until an individual is found which satisfies the termination criterion,
##    at which point it returns a dictionary with the solution program and
##    other info.
##    """
##    best_in_gen = pygp.termination_test(pop, data)
##    
##    if best_in_gen[1] < target_fitness:
##        return {"best":best_in_gen[0], "score":best_in_gen[1],
##                "gen": generation}
##
##    # if above fitness test fails, produce a new generation
##    next_gen = []
##    for i in range(len(pop)):
##        choice = random.random()
##        if choice < cross_rate:
##            child = pygp.subtree_crossover(pop, tourn_size, data)
##        elif choice < rep_rate:
##            child = pygp.reproduction(pop, tourn_size, data)
##        elif choice < mut_rate:
##            child = pygp.subtree_mutation(pop[i], max_depth)
##
##        next_gen.append(child)
##
##    # After producing a new generation, call recursively
##    return evolve(next_gen, generation+1)
##
##"""Results of the run"""
##solution = evolve(pop)
##print(pygp.tree_list(solution["best"]))
##print(solution["score"])
##print(solution["gen"])
