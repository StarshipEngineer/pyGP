import math
pi = math.pi

tot = 0
for x in range(0, 8):
    y = ((x - pi) ** (.0009476 + x)) + (.2106893 ** .0316142) + (x * pi)
    y_act = pi * x ** 2
    err = abs(y - y_act)
    tot += err

print(tot)
    
