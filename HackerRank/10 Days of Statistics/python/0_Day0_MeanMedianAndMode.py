'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 0: Mean, Median, and Mode

Objective
In this challenge, we practice calculating the mean, median, and mode.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate and print the respective mean, median,
and mode on separate lines. If your array contains more than one modal value,
choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer),
your answers should be in decimal form, rounded to a scale of  decimal place
(i.e., ,  format).

'''

from collections import Counter

x = int(input())
numbers = sorted([int(i) for i in input().split()])

mean = (sum(numbers) / x)
median = (numbers[x // 2] + numbers[-(x // 2 + 1)]) / 2
mode = sorted(sorted(Counter(numbers).items()), key = lambda x: x[1], reverse = True)[0][0]

print(mean, median, mode, sep = '\n')
