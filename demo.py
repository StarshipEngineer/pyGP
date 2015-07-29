import pygp
import math
import random

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
popsize = 10
max_depth = 3
cross_rate = 0.89
rep_rate = 0.97
mut_rate = 1.0

"""Step 5
Specify termination condition.
"""
fitness = 1

"""Initialization

"""
pop = []
half = int(popsize / 2)
for i in range(half):
    pop.append(pygp.BinaryTree(p, s, "full", random.randint(1, max_depth)))
    
for i in range(half, popsize+1):
    pop.append(pygp.BinaryTree(p, s, "grow", random.randint(1, max_depth)))

"""

"""
# evaluate each tree to see if it satisfies termination criterion
