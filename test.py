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
tree2 = pygp.BinaryTree(f, 2, primitives, set_dict)


pop = [pygp.BinaryTree(f, 2, primitives, set_dict) for i in range(100)]


##for item in tree1:
##    try:
##        print(item.value)
##    except AttributeError:
##        print("None")
##print()
##print(tree1.get_rand_function())


##print(tree1._assemble())
###new = pygp._crossover(tree1, ['a'], 2, 0)
##print(new._assemble())
