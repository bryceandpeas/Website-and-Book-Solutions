'''

Codewars Kata - 8 Kyu - Invert values

Description:

Invert a given list of integer values.

Python/JS/PHP:

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers.


'''

def invert(lst):
    lst2 = []
    for i, n in enumerate(lst):
        if n > 0:
            lst2.append(n * -1)
        else:
            lst2.append(n * -1)
    return (lst2)