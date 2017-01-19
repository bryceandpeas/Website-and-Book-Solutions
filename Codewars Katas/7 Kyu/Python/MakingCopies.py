'''

Codewars Kata - 7 Kyu - Making Copies

Description:

Write a function that takes a list (in Python) or array (in other languages) of numbers, and makes a copy.

Note that you may have troubles if you do not return an actual copy, item by item, not just a pointer or an alias for an existing list or array.

If not list or array is given as a parameter, the function should raise an error.

Examples:

t = [1,2,3,4]
t_copy = copy_list(t)
t[1] += 5
t == [1,7,3,4]
t_copy = [1,2,3,4]

'''

def copy_list(l):
    list_copy = []
    for i in l:
        list_copy.append(i)
        
    return list_copy
