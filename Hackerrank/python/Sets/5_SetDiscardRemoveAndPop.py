"""

February 2016

Hackerrank - Python - Sets - Set .discard(), .remove() & .pop()

.remove(x)
This operation removes element xx from the set. 
If element xx does not exist, it raises a KeyError.
The .remove(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
.discard(x)
This operation also removes element xx from the set. 
If element xx does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
.pop()
This operation removes and return an arbitrary element from the set. 
If there are no elements to remove, it raises a KeyError.

Example

>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
Task
You have a non-empty set ss, and you have to execute NN commands given in NN lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer nn, the number of elements in the set ss. 
The second line contains nn space separated elements of set ss. All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer NN, the number of commands.
The next NN lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints

0<n<200<n<20 
0<N<200<N<20
Output Format

Print the sum of the elements of set ss on a single line.


"""


n = int(input())
s = set(map(int, input().split()))
cmdno = int(input())

for i in range(0, cmdno):
    cmds = input().split()
    if cmds[0] == 'pop':
        s.pop()
    elif cmds[0] == 'remove':
        s.remove(int(cmds[1]))
    elif cmds[0] == 'discard':
        s.discard(int(cmds[1]))

print (sum(s))

    






    




