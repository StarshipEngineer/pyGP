#!/usr/bin/python3

import pygp 
import random
import string
import copy
import math


primitives = pygp.primitives
variables = ("x")
set_dict = pygp.primitive_handler(primitives, variables)
max_depth = 2
### introduce a structure that contains all of the necessary arguments for tree generation?
data = pygp.read_data('datafile.csv')
f = 'full'
g = 'grow'
##
##
tree1 = pygp.BinaryTree(primitives, set_dict, g, 2)
##tree2 = pygp.BinaryTree(primitives, set_dict, f, 2)
#tree3 = pygp.BinaryTree()



new = pygp.BinaryTree(primitives, set_dict, f, 0)
print(pygp.tree_list(new))


#pop = [pygp.BinaryTree(f, 2, primitives, set_dict) for i in range(100)]

##grow = pygp.BinaryTree(primitives, set_dict, ["+", "rand", "*", None, None, "rand", "x"])
##single = pygp.BinaryTree(primitives, set_dict, ["x", None, None, None, None, None, None])

##print("tree1:")
##print(pygp.tree_list(tree1))
##print(tree1.prog)
##new = pygp.subtree_mutation(tree1, primitives, set_dict, max_depth)
##print("new tree:")
##print(pygp.tree_list(new))
##print(new.prog)

# if depth passed is zero, subtree is just None- find a way to fix this, then we're good
# suspect problem may arise on line 40

# any tree that is the product of crossover or mutation will need to have its program rebuilt
# might it be better to just have crossover and mutation take and produce a list,
# then initialize a new tree with it???

##print(pygp.tree_list(grow))
##print(grow.prog)
##grow.prog = grow._build_prog()
##print(grow.prog)
