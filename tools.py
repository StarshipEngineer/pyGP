"""Data handling functions for user use at the top level of their programs"""


def primitive_handler(prim_dict, variables):
    """Sorts a dictionary of primitive/arity pairs into a dictionary of
    lists containing terminals, functions, primitives, and variables
    """
    functions = []
    terminals = []
    for key in prim_dict:
        if prim_dict[key] == 0:
            terminals.append(key)
        else:
            functions.append(key)

    primitives = functions + terminals
    return {"primitives":primitives, "functions":functions,
            "terminals":terminals, "variables":variables}


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
