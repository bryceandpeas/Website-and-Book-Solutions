'''

Codewars Kata - 8 Kyu - Calculate Average

Description:

Write function avg which calaculates average of numbers in given list.

'''

def find_average(array):
    return ((sum(array) / len(array)) if len(array) > 0 else 0)