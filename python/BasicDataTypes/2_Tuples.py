'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Basic Data Types: https://www.hackerrank.com/domains/python/py-basic-data-types

Hackerrank - Python - Basic Data Types - Tuples

Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot be modified once created). This restricts their use because we cannot add, remove, or assign values; however, it gives us an advantage in space and time complexities.

A common tuple use is the swapping of 22 numbers:

a,b = b,a 
Here a,ba,b is a tuple, and it assigns itself the values of b,ab,a.

Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashable.

Task 
You are given an integer, NN, on a single line. The next line contains NN space-separated integers. Create a tuple, TT, of those NN integers, then compute and print the result of hash(TT).

Note: hash() is one of the functions in the __builtins__ module.

Input Format

The first line contains an integer, NN (the number of elements in the tuple). 
The second line contains NN space-separated integers describing TT.

Output Format

Print the result of hash(TT).

contact: bryce@brycefury.com

'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

print input() == False or hash(tuple(map(int, input().split(' '))))

