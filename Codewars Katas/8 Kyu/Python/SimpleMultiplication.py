'''

Codewars Kata - 8 Kyu - Simple multiplication

Description:

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

'''

def simple_multiplication(number) :
    return (number * 8) if number % 2 == 0 else (number * 9)