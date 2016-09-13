'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Introduction: https://www.hackerrank.com/domains/python/py-introduction

Hackerrank - Python - Data Types - List Comprehensions

Let's learn about list comprehensions! You are given three integers X,YX,Y and ZZ representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of XXii ++ YYii ++ ZZii is not equal to NN. If X=2X=2, the possible values of XXii can be 00, 11 and 22. The same applies to YY and ZZ.

Input Format

Four integers X,Y,ZX,Y,Z and NN each on four separate lines, respectively.

Output Format

Print the list in lexicographic increasing order.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

L = [ [x,y,z] 
     for x in range(0, X+1) 
     for y in range(0, Y+1) 
     for z in range(0, Z+1) 
     if x + y + z != N ]

print (L)
