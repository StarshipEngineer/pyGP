import os

    

def etime():
    """See how much user and system time this process has used
    so far and return the sum."""
    
    user, sys, chuser, chsys, real = os.times()
    return user+sys


### random.sample
##start = etime()
##    
### place code here
##
##end = etime()
##elapsed = end - start
##print("time:", elapsed)
##
##"""""""
##

##
