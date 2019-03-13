'''

Codewars Kata - 8 Kyu - easy logs

Description:

Add two logs with base X, with the value of A and B. Example log A + log B where the base is X.

'''

import math

def logs(x, a, b):
    return(math.log(a, x) + math.log(b, x))