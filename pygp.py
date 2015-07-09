#!/usr/bin/python3

import random
import math
import copy


primitives = {"+":2, "-":2, "*":2, "/":2, "**":2, "rand":0}
# is imported by user in program, passed as prims to trees

#primset = arity2functions


class Node(object):

    def __init__(self, value, arity):
        if value == "rand":
            self.value = random.random()
        else:
            self.value = value

        self.arity = arity
        # this takes care of random value generation, no special functionality required in writing


class BinaryTree(list):

    def __init__(self, choice, depth, primitives, set_dict):
        #pass dict instead, storing p, f, t
        self.primitives = primitives
        self.set_dict = set_dict
        self.depth = depth
        self.size = 2 ** (self.depth + 1) - 1
        self.last_level = 2 ** self.depth - 1
        self.extend([None]*self.size)
        self.type = choice
        if self.type == 'full':
            self._full(self.size, self.last_level, 0)
        elif self.type == 'grow':
            self._grow(self.size, self.last_level, 0)
        self.prog = self._assemble(0)

    def get_left_index(self, n):
        return 2 * n + 1

    def get_right_index(self, n):
        return 2 * n + 2
        
    def get_parent_index(self, n):
        return int( (n - 1) / 2)

    def has_children(self, n):
        if (2 * n + 1) >= len(self) or (self[self.get_left_index(n)] == None and \
                                        self[self.get_right_index(n)] == None):
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
            self[n] = Node(random.choice(self.set_dict["functions"]), 2)
            self._full(s, m, 2*n+1)
            self._full(s, m, 2*n+2)
        elif (n < s):
            self[n] = Node(random.choice(self.set_dict["terminals"]), 0)

    def _grow(self, s, m, n):
        """Populates the tree using the grow method"""
        parent = self.get_parent(n) # this needs to change as well
        if n == 0 and self.depth >= 1:
            prim = random.choice(self.set_dict["primitives"])
            self[n] = Node(prim, self.primitives[prim])
            self._grow(s, m, 2*n+1)
            self._grow(s, m, 2*n+2)
        elif (n < m):
            if parent is None or parent.value not in self.set_dict["functions"]:
                self[n] = None
            else:
                prim = random.choice(self.set_dict["primitives"])
                self[n] = Node(prim, self.primitives[prim])
            self._grow(s, m, 2*n+1)
            self._grow(s, m, 2*n+2)
        elif (n < s):
            if parent is None or parent.value not in self.set_dict["functions"]:
                self[n] = None
            else:
                self[n] = Node(random.choice(self.set_dict["terminals"]), 0)

    def _assemble(self, n=0):
        left_index = self.get_left_index(n)
        right_index = self.get_right_index(n)
        if (2 * n + 2) < self.size:
            left_child = self.get_left_child(n)
            right_child = self.get_right_child(n)
            left_s = ""
            right_s = ""
            if left_child != None:
                left_s = str(self._assemble(left_index))
            if right_child != None:
                right_s = str(self._assemble(right_index))
            return "(" + left_s + self[n].value + right_s + ")"
        else:
            return self[n].value

    ##    def contents(self):
##        content = []
##        for node in self:
##            try:
##                content.append(node.value)
##            except AttributeError:
##                content.append(None)
##        # return a string? Have to fix this before debugging other things
##        return content

    def get_rand_terminal(self):
        """Returns the index of a random terminal"""
        index = random.randint(0, self.size - 1)
        rand_node = self[index]
        if rand_node.value not in self.set_dict["functions"]:
            return index
        else:
            return self.get_rand_terminal()


    def get_rand_function(self):
        """Returns the index of a random function, or None if no such node
        exists in tree
        """
        if self[0].value not in self.set_dict["functions"]:
            raise NodeSelectionError
        
        index = random.randint(0, self.last_level - 1)
        rand_node = self[index]
        if rand_node.value in self.set_dict["functions"]:
            return index
        
        return self.get_rand_function()

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


class NodeSelectionError(Exception):
    
    def __init__(self):
        self.msg = 'at least one tree does not have any function nodes, \
function crossover cannot be performed'

    def __str__(self):
        return self.msg


def get_depth(k):
    """"""
    d = math.log2(k + 1) - 1
    return d


"""Data handling functions for user use"""


def primitive_handler(prim_dict, variables):
    """Sorts a dictionary of primitive/arity pairs into a dictionary of
    lists containing terminals, functions, and primitives
    """
    for item in variables:
        prim_dict[item] = 0

    functions = []
    terminals = []
    for key in prim_dict:
        arity = prim_dict[key]
        if arity == 0:
            terminals.append(key)
        else:
            functions.append(key)

    primitives = functions + terminals
    return {"primitives":primitives, "functions":functions, "terminals":terminals}


def next_level_size(k):
    """Takes a tree size (number of nodes) k and returns the number of nodes
    that would be in the next deeper level
    """
    d = get_depth(k)
    d = d + 1
    next_level_size = 2 ** d
    return next_level_size


def fitness(tree, variables, dataset):
    """variables is a tuple of strings denoting variable names, and dataset is
    a list of tuples of floats denoting variable values
    """
    m = len(variables)
    var_list = [] # could just convert tuple to a list
    var_list.extend(variables)
    tot_err = 0
    for item in dataset:
        for i in range(m):
            vars()[var_list[i]] = item[i]
        try:
            dvar_actual = eval(var_list[-1])
            dvar_calc = eval(tree.prog)
            err = abs(dvar_actual - dvar_calc)
            tot_err = tot_err + err
        except ZeroDivisionError:
            raise SingularityError
    
    return tot_err


def sample(population, n):
    """A wrapper for the random module's sample function"""
    pop_sample = random.sample(population, n)
    return pop_sample


def tournament(pop_sample, variables, data):
    """Performs tournament selection, randomly choosing n individuals from the
    population and thunderdome-ing it, returning the individual with the best
    fitness
    """
    best = None
    best_score = None
    for item in pop_sample:
        try:
            score = fitness(item, variables, data)
            if (best_score == None) or (score < best_score):
                best = item
                best_score = score
        except SingularityError:
            pass
    
    return best


def read_data(filename):
    """Reads data from a file and returns a list of tuples. Each tuple
    contains variable values at a specific step
    """
    data = []
    file = open(filename, "r")
    for line in file:
        line_string = line.rstrip('\n')
        line_list = line_string.split(',')
        for i in range(len(line_list)):
            line_list[i] = float(line_list[i])
        line_tuple = tuple(line_list)
        data.append(line_tuple)
    file.close()
    return data


def _crossover(tree1, tree2, cross_pt1, cross_pt2):
    """"""
    tree1copy = copy.deepcopy(tree1)
    tree2copy = copy.deepcopy(tree2)
    sub = tree2copy.get_subtree(cross_pt2)
    tree1copy.replace_subtree(cross_pt1, sub)
    return tree1copy


"""Tree reproduction and mutation functions for user use"""


def subtree_crossover(population, n, variables, data):
    """"""
    pop_sample = sample(population, n)
    first_parent = tournament(pop_sample, variables, data)
    second_parent = tournament(pop_sample, variables, data)
    choice = random.random()
    if choice < 0.9:
        try:
            cross_pt1 = first_parent.get_rand_function()
            cross_pt2 = second_parent.get_rand_function()
        except NodeSelectionError:
            return None
    else:
        cross_pt1 = first_parent.get_rand_terminal()
        cross_pt2 = second_parent.get_rand_terminal()

    new_tree = _crossover(first_parent, second_parent, cross_pt1, cross_pt2)

    if new_tree is not None:
        return new_tree
    # test this!
    return subtree_crossover(population, n, variables, data)


def subtree_mutation():
    """"""
    init_options = ['full', 'grow']
    subtree = BinaryTree(random.choice(init_options),
                         random.randint(0,max_depth), primitives, set_dict)
    # test this!
    return _crossover(tree, subtree, random.randint(0, len(tree)-1), 0)


def point_mutation():
    pass


def reproduction(population, n, variables, data):
    """"""
    pop_sample = sample(population, n)
    winner = tournament(pop_sample, variables, data)
    return winner

# Another method that extracts headers and passes a tuple
