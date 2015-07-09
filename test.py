#!/usr/bin/python3

import pygp 
import random
import string
import copy
import math


primitives = pygp.primitives
variables = ("x")
set_dict = pygp.primitive_handler(primitives, variables)
# introduce a structure that contains all of the necessary arguments for tree generation?
data = pygp.read_data('datafile.csv')
f = 'full'
g = 'grow'


tree1 = pygp.BinaryTree(f, 2, primitives, set_dict)


pop = [pygp.BinaryTree(f, 2, primitives, set_dict) for i in range(5)]


def subtree_crossover(population, n, variables, data):
    print()
    print("starting new run...")
    exception_occurred = False
    pop_sample = pygp.sample(population, n)

    print("pop sample:")
    for item in pop_sample:
        print(item._assemble(0))

    print("begin tournament 1")
    
    first_parent = pygp.tournament(pop_sample, variables, data)

    print("begin tournament 2")
    
    second_parent = pygp.tournament(pop_sample, variables, data)

    print("1st parent",first_parent._assemble(0))
    print("2nd parent",second_parent._assemble(0))
    
    choice = random.random()
    print("choice:",choice)
    
    if choice < 0.9:
        try:
            cross_pt1 = first_parent.get_rand_function()
            cross_pt2 = second_parent.get_rand_function()
        except pygp.NodeSelectionError:
            exception_occurred = True
    else:
        cross_pt1 = first_parent.get_rand_terminal()
        cross_pt2 = second_parent.get_rand_terminal()

    if exception_occurred == False:
        
        print("crosspt1", cross_pt1, "crosspt2", cross_pt2)
        
        new = pygp._crossover(first_parent, second_parent, cross_pt1, cross_pt2)

        print("new tree:",new._assemble(0))

        return new
    
    return subtree_crossover(population, n, variables, data)



new = subtree_crossover(pop, 5, variables, data)
