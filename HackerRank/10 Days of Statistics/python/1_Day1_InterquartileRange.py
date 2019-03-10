'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 1: Interquartile Range

Objective
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

Task
The interquartile range of an array is the difference between its first ()
and third () quartiles (i.e., ).

Given an array, , of  integers and an array, , representing the
respective frequencies of 's elements, construct a data set, , where each
occurs at frequency . Then calculate and print 's interquartile range, rounded
to a scale of  decimal place (i.e.,  format).

Tip: Be careful to not use integer division when averaging the middle two
elements for a data set with an even number of elements, and be sure to not
include the median in your upper and lower data sets.

'''

import statistics

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += ([data[i]] * freq[i])
N = sum(freq)
s.sort()

if n % 2 != 0:
    q1 = statistics.median(s[:N//2])
    q3 = statistics.median(s[N//2+1:])

else:
    q1 = statistics.median(s[:N//2])
    q3 = statistics.median(s[N//2:])

print(round(float(q3-q1), 1))
