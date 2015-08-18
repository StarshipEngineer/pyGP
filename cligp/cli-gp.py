#!/usr/bin/python3
from pyGP.pyGP import components as pygp
from pyGP.pyGP import majorelements as me
from copy import deepcopy


filename = input("Enter the name of the file containing fitness data: ")
data = pygp.read_data(filename)

popsize = 1000
max_depth = 3
cross_rate = 0.90
rep_rate = 0.98
mut_rate = 1.0
tourn_size = 5
target_fitness = 0.01


p = pygp.primitives
v = ["x"] # enter variables
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)


settings = open("settings.txt", "r")
for line in settings:
    eval(line)
settings.close()

pop = me.ramped()
solutioninfo = me.evolve(pop)
winner = deepcopy(solutioninfo["best"])
print("The winning program is:")
print(winner.display())
print("Its fitness score was", solutioninfo["score"],
      "and it appeared in generation", solutioninfo["gen"])
print()
