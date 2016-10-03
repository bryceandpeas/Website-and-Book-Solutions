'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Sets: https://www.hackerrank.com/domains/python/py-sets

Hackerrank - Python - Sets - Set Mutations

We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |= 
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
TASK
You are given a set AA and NN number of other sets. These NN number of sets have to perform some specific mutation operations on set AA.

Your task is to execute those operations and print the sum of elements from set AA.

Input Format

The first line contains the number of elements in set AA.
The second line contains the space separated list of elements in set AA.
The third line contains integer NN, the number of other sets.
The next 2∗N2∗N lines are divided into NN parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

0<0< len(set(A)) <1000<1000 
0<0< len(otherSets) <100<100 
0<N<1000<N<100
Output Format

Output the sum of elements in set AA.

contact: bryce@brycefury.com

'''

noSets = int(input())
s = set(map(int, input().split()))
noOtherSets = int(input())

for i in range(0, (noOtherSets)):
    cmds, nextSet = input().split(), set(map(int, input().split()))
    
    if cmds[0] == 'intersection_update':
        s.intersection_update(nextSet)
    elif cmds[0] == 'update':
        s.update(nextSet)
    elif cmds[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(nextSet)
    elif cmds[0] == 'difference_update':
        s.difference_update(nextSet)
        
print (sum(s))

