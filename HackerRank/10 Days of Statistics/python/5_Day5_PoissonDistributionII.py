'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 5: Poisson Distribution II

Objective
In this challenge, we go further with Poisson distributions.
We recommend reviewing the previous challenge's Tutorial before attempting
this problem.

Task
The manager of a industrial plant is planning to buy a machine of either type
or type . For each day’s operation:

The number of repairs, , that machine  needs is a Poisson random variable
with mean . The daily cost of operating  is .
The number of repairs, , that machine  needs is a Poisson random variable
with mean . The daily cost of operating  is .
Assume that the repairs take a negligible amount of time and the machines
are maintained nightly to ensure that they operate like new at the start of
each day. Find and print the expected daily cost for each machine.



'''

ma, mb = map(float, input().split())

print (('%.3f' % (160 + 40*(ma+ma**2))) + '\n' + ("%.3f" % (128 + 40*(mb+mb**2))))
