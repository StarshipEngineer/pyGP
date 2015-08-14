import math
pi = math.pi

tot = 0
for x in range(0, 8):
    y = ((pi-.01)-pi)**((.03-pi)/(pi-x))
    y_act = pi * x ** 2
    err = abs(y - y_act)
    tot += err

print(tot)
