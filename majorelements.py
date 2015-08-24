"""This module contains major program elements for use in writing GP programs,
including pre-written functions for initializing and evolving populations of
programs.
"""


from pyGP import pygp
from random import random, randint


def ramped(p, s, controls):
    """Initializes and returns a population using the ramped half-and-half
    technique, where half the initial population is generated with grow and the
    other half with full, using a range of depths.
    """
    pop = []
    popsize = controls["popsize"]
    max_depth = controls["max_depth"]
    half = int(popsize / 2)
    for i in range(1, half):
        pop.append(pygp.BinaryTree(p, s, "full", randint(1, max_depth)))
        
    for i in range(half, popsize+1):
        pop.append(pygp.BinaryTree(p, s, "grow", randint(1, max_depth)))

    return pop


def evolve(pop, data, controls, generation=1):
    """This function examines each generation of programs, and if none meet
    the termination criterion, evolves a new generation and calls itself
    until an individual is found which satisfies the termination criterion,
    at which point it returns a dictionary containing the solution program and
    other info.
    """
    print("Generation:", generation)
    best_in_gen = pygp.termination_test(pop, data)
    
    if best_in_gen[1] < controls["target_fitness"]:
        return {"best":best_in_gen[0], "score":best_in_gen[1],
                "gen": generation}

    next_gen = []
    for i in range(len(pop)):
        choice = random()
        if choice < controls["cross_rate"]:
            child = pygp.subtree_crossover(pop, controls["tourn_size"], data)
        elif choice < controls["rep_rate"]:
            child = pygp.reproduction(pop, controls["tourn_size"], data)
        elif choice < controls["mut_rate"]:
            child = pygp.subtree_mutation(pop[i], controls["max_depth"])

        next_gen.append(child)

    return evolve(next_gen, data, controls, generation+1)
