import pygp
import math
import random


p = pygp.primitives
v = ["x"]
for item in v:
    p[item] = 0

s = pygp.primitive_handler(p, v)
filename = "datafile.csv"
data = pygp.read_data(filename)

popsize = 10

pop = [pygp.BinaryTree(p, s, 'grow', 2) for x in range(popsize)]

cross_rate = 0.9
rep_rate = 0.98
mut_rate = 1.0



#tree = pygp.BinaryTree(p, s, 'grow', 2)
