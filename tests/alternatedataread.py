##def read_data2(filename):
##    """Reads data from a file and returns a list of tuples. Each tuple
##    contains variable values at a specific step
##    """
##    
##    file = open(filename, "r")
##    first_line = file.readline()
##    first_line.rstrip('\n')
##    first_line_list = first_line.split(',')
##    
##    if first_line_list[0].isnumeric == False:
##        data = []
##        for line in file:
##            line_string = line.rstrip('\n')
##            line_list = line_string.split(',')
##            data.append(line_list)
##        headers = data.pop[0]
##        headers = tuple(headers)
##        for item in data:
##            for i in range(len(item)):
##                item[i] = float(item[i])
##        data = (headers, data)
##        
##    else:
##        data = []
##        for line in file:
##            line_string = line.rstrip('\n')
##            line_list = line_string.split(',')
##            for i in range(len(line_list)):
##                line_list[i] = float(line_list[i])
##            line_tuple = tuple(line_list)
##            data.append(line_tuple)
##
##    file.close()
##    return data
