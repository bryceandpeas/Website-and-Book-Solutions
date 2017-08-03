'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 5: Poisson Distribution I

Objective
In this challenge, we learn about Poisson distributions.
Check out the Tutorial tab for learning materials!

Task
A random variable, , follows Poisson distribution with mean of .
Find the probability with which the random variable  is equal to .

'''

import math

m = float(input())
x = int(input())

print(round((m**x) * math.exp(-m) / math.factorial(x), 3))
