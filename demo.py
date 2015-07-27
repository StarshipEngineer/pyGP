import pygp
import math
import random

variables = ["x"]
p = pygp.primitives
s = pygp.primitive_handler(p, variables)

filename = "datafile.csv"
data = pygp.read_data(filename)

popsize = 10

pop = [pygp.BinaryTree(p, s, 'grow', 2) for x in range(popsize)]
#pop = [pygp.BinaryTree(p, s, ["+", "rand", "math.pi"])]

cross_rate = 0.9
rep_rate = 0.98
mut_rate = 1.0


# Generation loop:
# Populate the generation
# 

new = pygp.subtree_crossover(pop, 3,variables, data)
print()
print(pygp.tree_list(new))
print(new.prog)
print(new._build_prog())
