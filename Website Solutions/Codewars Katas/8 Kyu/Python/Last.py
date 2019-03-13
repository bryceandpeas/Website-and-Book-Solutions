'''

Codewars Kata - 8 Kyu - Last
30-89

Description:

Find the last element of a list.

Example:

last([1,2,3,4]) # => 4
last("xyz") # => z
last(1,2,3,4) # => 4
In javascript and CoffeeScript a list will be an array, a string or the list of arguments.

(courtesy of haskell.org)


'''

def last(*args):
    try:
        return args[-1][-1]
    except TypeError:
        return args[-1]