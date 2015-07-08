import os
import pygp
import random

functions = ['+','-','*','/']
terminals = ['x','1']
primitives = functions + terminals
f = 'full'
g = 'grow'
n = 5
pop = [pygp.Tree(f, 2, functions, terminals, primitives) for x in range(1000000)]

def etime():
    """See how much user and system time this process has used
    so far and return the sum."""
    
    user, sys, chuser, chsys, real = os.times()
    return user+sys


# random.sample
start = etime()
    
sample1 = random.sample(pop, n)

end = etime()
elapsed = end - start
print("random sample", elapsed)

# pygp random.sample
start = etime()
    
sample1 = pygp.random_sample(pop, n)

end = etime()
elapsed = end - start
print("pygp random sample", elapsed)
