'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 2: Basic Probability

Objective
In this challenge, we practice calculating probability. Check out the Tutorial
tab for a breakdown of probability fundamentals!

Task
In a single toss of  fair (evenly-weighted) six-sided dice,
find the probability that their sum will be at most .
2 / 3
5 / 6
1 / 4
1 / 6

'''

5/6

total_outcomes = []
desired_outcomes = []
for num1 in range(1,7):
    for num2 in range(1,7):
        if num1+num2 <= 9:
            desired_outcomes.append(num1+num2)
        total_outcomes.append(num1+num2)
prob = len(desired_outcomes)/len(total_outcomes)
print('%d/%d' % (len(desired_outcomes), len(total_outcomes)))
