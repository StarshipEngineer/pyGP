# Import modules
import pygp
import math
import random

variables = ("r")
prim_dict = pygp.primitives
primitives = pygp.primitive_handler(prim_dict, variables)

filename = "datafile.csv"
data = pygp.dataread(filename)

popsize = 100
pop = []
pop.extend([None]*popsize)

cross_rate = 0.9
rep_rate = 0.98
mut_rate = 1.0

# Select inidividuals from the population, test their fitness,
# and use them to populate the next generation

