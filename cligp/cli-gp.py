#!/usr/bin/python3
from pyGP import pygp, tools, primitives
from pyGP import majorelements as me
from copy import deepcopy


filename = input("Enter the name of the file containing fitness data: ")
data = pygp.read_data(filename)

print("Specify characteristics of the run")
popsize = int(input("Enter the population size: "))
max_depth = int(input("Enter the maximum starting depth of trees: "))
tourn_size = int(input("Enter the number of individuals to be selected to \
                       participate in tournaments: "))
target_fitness = float(input("Enter the target fitness a program must score \
                       below to be declared the solution and terminate the \
                       run: "))
print("Enter the rates of crossover, reproduction, and mutation. Their sum \
      must be exactly 1.0.")
cross_rate = float(input("Crossover rate: "))
rep_rate = float(input("Reproduction rate: ")) + cross_rate #0.98
mut_rate = float(input("Mutation rate: ")) + cross_rate + rep_rate


p = primitives.pset

#make a function
vs = input("Enter the variables corresponding to the columns in the data \
           file, in order from left to right, separated only by commas: ")
print("The specified variables are:", vs)
v = vs.split(",")
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)


print("Generating initial population")
pop = me.ramped()
print("")
solutioninfo = me.evolve(pop)
winner = deepcopy(solutioninfo["best"])
print("The winning program is:")
print(winner.display())
print("Its fitness score was", solutioninfo["score"],
      "and it appeared in generation", solutioninfo["gen"])
print()
