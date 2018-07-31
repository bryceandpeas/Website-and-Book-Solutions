'''

Codewars Kata - 6 Kyu - Find the odd int

Description:

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''

from collections import Counter

def find_it(seq):
    return(int(str([i for i, v in Counter(seq).items() if v % 2 !=0]).strip('[]')))