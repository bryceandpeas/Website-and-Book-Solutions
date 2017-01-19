'''

Codewars Kata - 8 Kyu - Pre-FizzBuzz Workout #1

Description:

This is the first step to understanding FizzBuzz.

Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.

Your expected outputs: an array of positive integers from 1 to n

Your job is to write an algorithm that gets you from the input to the output.

'''

def pre_fizz(n):
    return [n for n in range(1, n+1)]
