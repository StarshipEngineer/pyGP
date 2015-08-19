#!/usr/bin/python3
"""This module contains all of the classes and functions required for a
basic symbolic-regression implementation of genetic programming, including
classes binary trees and nodes to fill them, recombination and mutation
operations, and basic data-handling functionality.
"""


from random import sample, random, randint, choice
from pyGP.primitives import pi, e
from math import log2
from copy import deepcopy


class Node(object):
    """"""
    def __init__(self, value, arity):
        if value == "rand":
            self.value = str(random()) 
        else:
            self.value = value

        self.arity = arity


class LinearTree(list):
    def __init__(self):
        pass


class BinaryTree(list):
    """"""
    def __init__(self, primitives, set_dict, contents, depth=None):
        self.primitives = primitives
        self.set_dict = set_dict
        values_provided = (type(contents) == list)
        if values_provided:
            self.size = len(contents)
            self.depth = get_depth(self.size)
        else:
            self.depth = depth
            self.size = 2 ** (self.depth + 1) - 1

        self.extend([None]*self.size)
        self.last_level = 2 ** self.depth - 1
        if values_provided:
            for i in range(len(contents)):
                if contents[i] != None:
                    self[i] = Node(contents[i], primitives[contents[i]])
        elif contents == 'full':
            self._full(self.size, self.last_level, 0)
        elif contents == 'grow':
            self._grow(self.size, self.last_level, 0)

    def get_left_index(self, n):
        return 2 * n + 1

    def get_right_index(self, n):
        return 2 * n + 2

    def get_parent_index(self, n):
        return int( (n - 1) / 2)

    def has_children(self, n):
        if (2 * n + 1) >= len(self) or (self[self.get_left_index(n)] == None
                                        and self[self.get_right_index(n)]
                                        == None):
            return False
        else:
            return True

    def get_left_child(self, n):
        if self.has_children(n):
            i = self.get_left_index(n)
            return self[i]
        else:
            return None

    def get_right_child(self, n):
        if self.has_children(n):
            i = self.get_right_index(n)
            return self[i]
        else:
            return None

    def get_parent(self, n):
        return self[self.get_parent_index(n)]

    def _full(self, s, m, n):
        """Populates the tree using the full method"""
        if (n < m):
            self[n] = Node(choice(self.set_dict["functions"]), 2)
            self._full(s, m, 2*n+1)
            self._full(s, m, 2*n+2)
        elif (n < s):
            self[n] = Node(choice(self.set_dict["terminals"]), 0)

    def _grow(self, s, m, n):
        """Populates the tree using the grow method"""

        # somewhere in here is the problem- need to assign a terminal node to 0 if
        # tree has length 1

        parent = self.get_parent(n) # this needs to change as well
        if n == 0: #and self.depth >= 1: switch order, do if equal zero and else
            if self.depth >= 1:
                prim = choice(self.set_dict["primitives"])
            elif self.depth == 0:
                prim = choice(self.set_dict["terminals"])

            self[n] = Node(prim, self.primitives[prim])
            self._grow(s, m, 2*n+1)
            self._grow(s, m, 2*n+2)
        elif (n < m):
            if parent is None or parent.value not in \
            self.set_dict["functions"]:
                self[n] = None
            else:
                prim = choice(self.set_dict["primitives"])
                self[n] = Node(prim, self.primitives[prim])
            self._grow(s, m, 2*n+1)
            self._grow(s, m, 2*n+2)
        elif (n < s):
            if parent is None or parent.value not in \
            self.set_dict["functions"]:
                self[n] = None
            else:
                self[n] = Node(choice(self.set_dict["terminals"]), 0)

    def build_program(self, n=0):
        strng = ""
        if n < self.size and self[n] != None:
            strng = self[n].value
            left = self.build_program(2*n+1)
            right = self.build_program(2*n+2)
            strng = "(" + left + strng + right + ")"

        return strng

    def display(self):
        contents = []
        for item in self:
            try:
                contents.append(item.value)
            except AttributeError:
               contents.append(None)
        return contents

    def get_rand_terminal(self):
        """Returns the index of a random terminal"""
        try:
            index = randint(0, self.size - 1)
        except RuntimeError:
            print("A recursion depth limit exceeded error occurred. The \
                  offending program is:")
            print(self.display())
        if (self[index] is None) or (self[index].value in
                                     self.set_dict["functions"]):
            return self.get_rand_terminal()

        return index

    def get_rand_function(self):
        """Returns the index of a random function, or raises an error if tree
        does not contain one
        """
        if (self[0] is None) or (self[0].value not in self.set_dict["functions"]):
            raise NodeSelectionError

        index = randint(0, self.last_level - 1)
        if (self[index] is None) or (self[index].value not in
                                     self.set_dict["functions"]):
            return self.get_rand_function()

        return index

    def get_rand_node(self):
        index = randint(0, self.size-1)
        if self[index] != None:
            return index

        return self.get_rand_node()

    def get_subtree(self, n, depth=0):
        """Retrieves and returns as a list the subtree starting at index n"""
        if n >= len(self):
            return []

        start = n
        stop = (2 ** depth) + n
        subtree = self[start:stop]
        return subtree + self.get_subtree(start*2+1, depth+1)

    def _fill_subtree(self, n, subtree, depth=0):
        """Takes in a subtree as a list and a starting index n, and
        re-populates the subtree rooted at self[n] with the contents of
        subtree
        """
        if n >= self.size:
            return

        start = n
        stop = (2 ** depth) + n
        for i in range(start,stop):
            self[i] = subtree.pop(0)
        self._fill_subtree(start*2+1, subtree, depth+1)

    def _pad(self, n, subtree):
        """Takes in a starting node index n and a subtree as a list, and pads
        the tree if the subtree would extend beyond the deepest level, or the
        subtree if it does not extend down to the tree's deepest level
        """
        old = self.get_subtree(n)
        new = subtree
        nodes_in_old = len(old)
        nodes_in_new = len(new)

        if nodes_in_new == nodes_in_old:
            return

        if nodes_in_new < nodes_in_old:
            new.extend([None]*(int(next_level_size(nodes_in_new))))
        elif nodes_in_new > nodes_in_old:
            self.extend([None]*(int(next_level_size(self.size))))
            self.size = len(self)

        self._pad(n, new)

    def replace_subtree(self, n, subtree):
        """Takes in a subtree and starting node n, and replaces the original
        subtree beginning at node n with the new one
        """
        self._pad(n, subtree)
        self._fill_subtree(n, subtree)


"""Error classes"""


class SingularityError(Exception):

    def __init__(self):
        self.msg = 'the function called has a singularity'

    def __str__(self):
        return self.msg


class UnfitError(Exception):

    def __init__(self):
        self.msg = 'the individual has a fitness score too large to be represented'

    def __str__(self):
        return self.msg


class NodeSelectionError(Exception):

    def __init__(self):
        self.msg = 'at least one tree does not have any function nodes, \
function crossover cannot be performed'

    def __str__(self):
        return self.msg


"""Functions for working with individual trees"""


def get_depth(k):
    """Takes the size k of a binary tree and returns its depth"""
    return int(log2(k + 1) - 1)


def next_level_size(k):
    """Takes a tree size (number of nodes) k and returns the number of nodes
    that would be in the next deeper level
    """
    d = get_depth(k)
    d = d + 1
    return 2 ** d


"""Tree recombination and mutation functions for user use"""


def subtree_crossover(population, n, data):
    """Takes a population, performs 2 tournament selections with sample size n,
    performs subtree crossover on the winners, and returns a new tree
    """
    exception_occurred = False
    first_parent = tournament(population, n, data)
    second_parent = tournament(population, n, data) # This returned a None- probably because all programs failed
    # make tournament recursive
    choice1 = random()
    choice2 = random()
    if choice1 < 0.9:
        try:
            cross_pt1 = first_parent.get_rand_function()
        except NodeSelectionError:
            exception_occurred = True
    else:
        cross_pt1 = first_parent.get_rand_terminal()

    if choice2 < 0.9:
        try:
            cross_pt2 = second_parent.get_rand_function()
        except NodeSelectionError:
            exception_occurred = True
    else:
        cross_pt2 = second_parent.get_rand_terminal()

    if exception_occurred == False:
        return _crossover(first_parent, second_parent, cross_pt1, cross_pt2)

    return subtree_crossover(population, n, data)


def subtree_mutation(tree, max_depth):
    """Takes in a tree and parameters for generating a new tree, and returns
    a copy of the original tree with a subtree replaced by the new tree
    """
    p = tree.primitives
    s = tree.set_dict
    init_options = ['full', 'grow']
    subtree = BinaryTree(p, s, choice(init_options), randint(0, max_depth))
    return _crossover(tree, subtree, tree.get_rand_node(), 0)


def point_mutation():
    pass


def reproduction(population, n, data):
    """Performs a single tournament selection and returns a copy of the most
    fit individual
    """
    winner = tournament(population, n, data)
    return deepcopy(winner)


"""Functions used in fitness evaluation, recombination, and mutation"""


def fitness(tree, dataset):
    """variables is a list of strings denoting variable names, and dataset is
    a list of tuples of floats denoting variable values
    """
    prog = tree.build_program()
    variables = tree.set_dict["variables"]
    m = len(variables)
    tot_err = 0
    for item in dataset:
        for i in range(m):
            vars()[variables[i]] = item[i]
        try:
            dvar_actual = item[-1]
            dvar_calc = eval(prog)
            err = abs(dvar_actual - dvar_calc)
            tot_err = tot_err + err
        except ZeroDivisionError:
            raise SingularityError
        except OverflowError:
            raise UnfitError

    return tot_err


def tournament(population, n, data):
    """Performs tournament selection, randomly choosing n individuals from the
    population and thunderdome-ing it, returning the individual with the best
    fitness
    """
    pop_sample = sample(population, n)
    best = None
    best_score = None
    for item in pop_sample:
        try:
            score = fitness(item, data)
            if (best_score == None) or (score < best_score):
                best = item
                best_score = score
        except SingularityError:
            pass
        except UnfitError:
            pass

    if best == None:
        return tournament(population, n, data)

    return best


def _crossover(tree1, tree2, cross_pt1, cross_pt2):
    """Takes two tree objects and a crossover index on each and returns a copy
    of the first tree with the subtree rooted at the first crossover point
    replaced by the subtree rooted at the second point on the second tree
    """
    tree1copy = deepcopy(tree1)
    tree2copy = deepcopy(tree2)
    sub = tree2copy.get_subtree(cross_pt2)
    tree1copy.replace_subtree(cross_pt1, sub)
    return tree1copy


def termination_test(population, data):
    """Tests the fitness of every member of the population, returning the
    individual with the best fitness and that fitness as a tuple
    """
    pop_sample = sample(population, len(population)-1)
    best = None
    best_score = None
    for item in pop_sample:
        try:
            score = fitness(item, data)
            if (best_score == None) or (score < best_score):
                best = item
                best_score = score
        except SingularityError:
            pass
        except UnfitError:
            pass

    return best, best_score

##Another method that extracts headers and passes a tuple for automatic variable
##generation; could import a data file as a list of tuples and then use pop to
##return the headers
