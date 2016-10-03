'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Basic Data Types: https://www.hackerrank.com/domains/python/py-basic-data-types

Hackerrank - Python - Basic Data Types - Nested Lists

Let's implement a nested list! A nested list is a list that contains another list (i.e.: a list of lists). For example:

>> a = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
>> len(a)
3  
>> a[1]
['red', 'black']
>> a[1][0]
red
To go through every element in a list, use a nested for loop.

Given the names and grades for each student in a Physics class of NN students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, NN, the number of students. 
The 2N2N subsequent lines describe each student over 22 lines; the first line contains a student's name, and the second line contains their grade.

Constraints

2≤N≤52≤N≤5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
L = [[input(), float(input())] for i in range(N)]

s = sorted({i[1] for i in L})
r = sorted(i[0] for i in L if i[1] == s[1])

print ('\n'.join(r))