"""This module contains major program elements for use in writing GP programs,
including pre-written functions for initializing and evolving populations of
programs.
"""


import pyGP.pyGP.components as pygp
from random import random, randint


def ramped(popsize, p, s, max_depth):
    """Initializes and returns a population using the ramped half-and-half
    technique, where half the initial population is generated with grow and the
    other half with full, using a range of depths.
    """
    pop = []
    half = int(popsize / 2)
    for i in range(1, half):
        pop.append(pygp.BinaryTree(p, s, "full", randint(1, max_depth)))
        
    for i in range(half, popsize+1):
        pop.append(pygp.BinaryTree(p, s, "grow", randint(1, max_depth)))

    return pop


def evolve(pop, generation=1):
    """This function examines each generation of programs, and if none meet
    the termination criterion, evolves a new generation and calls itself
    until an individual is found which satisfies the termination criterion,
    at which point it returns a dictionary containing the solution program and
    other info.
    """
    print(generation)
    best_in_gen = pygp.termination_test(pop, data)
    
    if best_in_gen[1] < target_fitness:
        return {"best":best_in_gen[0], "score":best_in_gen[1],
                "gen": generation}

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

    return evolve(next_gen, generation+1)
