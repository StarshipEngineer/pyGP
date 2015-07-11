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
tree1 = pygp.BinaryTree(primitives, set_dict, g, 1)
tree2 = pygp.BinaryTree(primitives, set_dict, f, 2)
#tree3 = pygp.BinaryTree()

#print(pygp.tree_list(tree1))
#print(tree1.get_rand_node())

#pop = [pygp.BinaryTree(f, 2, primitives, set_dict) for i in range(100)]
print("tree1:")
print(pygp.tree_list(tree1))
new = pygp.subtree_mutation(tree1, primitives, set_dict, max_depth)
print("new tree:")
print(pygp.tree_list(new))




##print(x)
##def outer(x):
##    y = []
##    def inner(x):
##        if x != 1:
##            y.append(x)
##        return y
##
##    return inner(x)
##
##print(outer(2))

##def test(tree):
##    """"""
##
##    def choose_cross_pt():
##        index = random.randint(0, len(tree)-1) 
##        if tree[index] != None:
##            return index
##
##        return choose_cross_pt()
##
##    x = choose_cross_pt()
##    return x

##p = test(tree1)
##print(pygp.tree_list(tree1))
##print(p)
