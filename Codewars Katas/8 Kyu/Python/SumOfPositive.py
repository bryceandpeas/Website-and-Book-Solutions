'''

Codewars Kata - 8 Kyu - Sum of positive

Description:

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

'''

def positive_sum(arr):
    out = 0
    for i in arr:
        if i > 0:
            out += i
    return out
