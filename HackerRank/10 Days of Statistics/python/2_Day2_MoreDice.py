'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 2: More Dice

Objective
In this challenge, we practice calculating probability.
We recommend you review the previous challenge's Tutorial before attempting
this problem.


Task
In a single toss of  fair (evenly-weighted) six-sided dice,
find the probability that the values rolled by each die will be different
and the two dice have a sum of .
1 / 9
1 / 6
2 / 3
5 / 6

'''


1/9

total_outcomes = []
desired_outcomes = []
for num1 in range(1,7):
    for num2 in range(1,7):
        if num1+num2 == 6 and num1!=num2 :
            desired_outcomes.append(num1+num2)
        total_outcomes.append(num1+num2)
prob = len(desired_outcomes)/len(total_outcomes)
print('%d/%d' % (len(desired_outcomes), len(total_outcomes)))
