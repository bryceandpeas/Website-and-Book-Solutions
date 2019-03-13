'''

Codewars Kata - 8 Kyu - Square(n) Sum

Description:

Complete the squareSum method so that it squares each number passed into it and then sums the results together.

For example:

square_sum([1, 2, 2]) # should return 9

'''

def square_sum(numbers):
    total = 0
    for i in numbers:
        total += (i**2)
    return(total)
