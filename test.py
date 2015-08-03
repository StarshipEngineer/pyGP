#!/usr/bin/python3
import pygp
import math
import random
import decimal


p = pygp.primitives
v = ["r"]
#v = ["r"]
for item in v:
    p[item] = 0
s = pygp.primitive_handler(p, v)
otherfile = "datafile.csv"
filename = "circlearea.csv"
data = pygp.read_data(filename)


def fitness(tree, dataset):
    """variables is a list of strings denoting variable names, and dataset is
    a list of tuples of floats denoting variable values
    """
    #
    decimal.getcontext().prec = 10
    #
    prog = tree.build_program()
    variables = tree.set_dict["variables"]
    m = len(variables)
    tot_err = 0
    for item in dataset:
        for i in range(m):
            vars()[variables[i]] = item[i]
        try:
            dvar_actual = decimal.Decimal(item[-1])
            dvar_calc = decimal.Decimal(eval(prog)) # have a problem here for some cases
            err = abs(dvar_actual - dvar_calc)
            tot_err = tot_err + err
        except ZeroDivisionError:
            raise SingularityError

    return tot_err



#tree = pygp.BinaryTree(p, s, ["*", "math.pi", "*", None, None, "r", "r"])
#tree = pygp.BinaryTree(p, s, ["+", "x", "y"])
#tree = pygp.BinaryTree(p, s, 'full', 2)
tree = pygp.BinaryTree(p, s, ['**', '-', '**', '+', '*', '**', '+', 'r', 'math.pi', '0.6230005876558375', 'r', 'math.pi', 'math.pi', 'math.pi', '0.5060062922851026'])
print(pygp.tree_list(tree))
print(tree.build_program())
print(fitness(tree, data))
 


