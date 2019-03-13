'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 4: Binomial Distribution II

Objective
In this challenge, we go further with binomial distributions.
We recommend reviewing the previous challenge's Tutorial before attempting
this problem.

Task
A manufacturer of metal pistons finds that, on average,  of the pistons
they manufacture are rejected because they are incorrectly sized. What is
the probability that a batch of  pistons will contain:

No more than  rejects?
At least  rejects?



'''

p, n = list(map(int, input().split(' ')))

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n - x))

def b(x, n, p):
    return comb(n, x) * p ** x * (1 - p) ** (n - x)

print(round(sum([b(i, n, p / 100) for i in range(3)]), 3))
print(round(sum([b(i, n, p / 100) for i in range(2, n+1)]), 3))
