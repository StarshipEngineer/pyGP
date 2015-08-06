#!/usr/bin/python3
import pygp
import math
import random
import decimal


p = pygp.primitives
v = ["r"]
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)
otherfile = "datafile.csv"
filename = "circlearea.csv"
data = pygp.read_data(filename)




#tree = pygp.BinaryTree(p, s, ["*", "pi", "*", None, None, "r", "r"])
#tree = pygp.BinaryTree(p, s, ["+", "x", "y"])
#tree = pygp.BinaryTree(p, s, 'full', 2)
b = ['+', '**', '+', '-', '+', '**', '*', 'r', 'pi',
     'rand', 'r', 'rand', 'rand', 'r', 'pi']
tree = pygp.BinaryTree(p, s, b)
print(pygp.tree_list(tree))
print(tree.build_program())
print()
print(pygp.fitness(tree, data))
#print(pygp.fitness(tree2, data))


