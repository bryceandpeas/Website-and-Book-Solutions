"""

February 2016

Hackerrank - Python - Sets - Set .intersection() Operation

.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains nn, the number of students who have subscribed to the English newspaper. 
The second line contains nn space separated roll numbers of those students.
The third line contains bb, the number of students who have subscribed to the French newspaper. 
The fourth line contains bb space separated roll numbers of those students.

Constraints

0<Total number of students in college<10000<Total number of students in college<1000
Output Format

Output the total number of students who have subscriptions to both English and French newspapers.



"""


subscribes = int(input())
rollEnglish = set((input().split()))
french = (input().split())
rollFrench = set((input().split()))

finalRoll = rollEnglish.intersection(set(rollFrench))

print (len(finalRoll))
    






    














    




