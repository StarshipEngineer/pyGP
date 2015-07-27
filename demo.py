import pygp
import math
import random

variables = ["x"]
p = pygp.primitives
s = pygp.primitive_handler(p, variables)

filename = "datafile.csv"
data = pygp.read_data(filename)

popsize = 5

pop = [pygp.BinaryTree(p, s, 'full', 1) for x in range(popsize)]

cross_rate = 0.9
rep_rate = 0.98
mut_rate = 1.0


# Generation loop:
# Populate the generation
# 

