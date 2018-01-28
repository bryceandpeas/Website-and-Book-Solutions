'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 2: Compound Event Probability

Objective
In this challenge, we practice calculating the probability of a compound event.
We recommend you review today's Probability Tutorial before attempting this
challenge.


Task
There are  urns labeled , , and .

Urn  contains  red balls and  black balls.
Urn  contains  red balls and  black balls.
Urn  contains  red balls and  black balls.

One ball is drawn from each of the  urns. What is the probability that,
of the  balls drawn,  are red and  is black?

10 / 63
2 / 7
17 / 42
31 / 126

'''

17/42

import itertools
from fractions import Fraction

X = ["b","b","b","r","r","r","r"]
Y = ["b","b","b","b","r","r","r","r","r"]
Z = ["b","b","b","b","r","r","r","r"]

r = [(i)for i in itertools.product(X,Y,Z)]
e = list(map(lambda x : x.count('r') == 2 and x.count('b') == 1,r))
Fraction(e.count(True),len(e))
