'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 1: Standard Deviation

Objective
In this challenge, we practice calculating standard deviation.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of  decimal place
(i.e., format). An error margin of  will be tolerated for the standard deviation.

'''

n = int(input().strip())
x = [int(i) for i in input().strip().split()]

m = (sum(x) / n)
v = (sum(((i - m) ** 2) for i in x) / n)
sdev = (v ** 0.5)

print("{0:0.1f}".format(sdev))
