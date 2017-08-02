'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 0: Weighted Mean

Objective
In the previous challenge, we calculated a mean.
In this challenge, we practice calculating a weighted mean.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers and an array, ,
representing the respective weights of 's elements,
calculate and print the weighted mean of 's elements.
Your answer should be rounded to a scale of  decimal place (i.e.,  format).
'''

n = int(input())
x = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]
print (round(1.0 * sum([x[i] * w[i] for i in range(n)]) / sum(w), 1))

