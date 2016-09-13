'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Strings: https://www.hackerrank.com/domains/python/py-strings

Hackerrank - Python - Strings - String Split and Join

In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task 
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format 
The first line contains a string consisting of space separated words.

Output Format 
Print the formatted string as explained above.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

STDIN = input()

STDIN = STDIN.split(' ')

STDIN = '-'.join(STDIN)

print (STDIN)