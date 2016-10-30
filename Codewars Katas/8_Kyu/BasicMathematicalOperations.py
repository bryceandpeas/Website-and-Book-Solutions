'''

Codewars Kata - 8 Kyu - Basic Mathematical Operations

Description:

Your task is to create a function - basicOp().

The function should take three arguments - operation(string/char), value1(number), value2(number). The function should return result of numbers after applying chosen operation.

Examples:

basic_op('+', 4, 7)         # Output: 11
basic_op('-', 15, 18)       # Output: -3
basic_op('*', 5, 5)         # Output: 25
basic_op('/', 49, 7)        # Output: 7

'''

def basic_op(operator, value1, value2):
    return(eval('{0} {1} {2}'.format(value1, operator, value2)))