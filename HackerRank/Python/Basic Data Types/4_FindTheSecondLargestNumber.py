'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Basic Data Types: https://www.hackerrank.com/domains/python/py-basic-data-types

Hackerrank - Python - Basic Data Types - Find the Second Largest Number

Let's delve into one of the most basic data types in Python, the list. You are given NN numbers. Store them in a list and find the second largest number.

NOTE: Do not use the insertion sort method.

Input Format

The first line contains NN. The second line contains an array AA[] of NN integers each separated by a space.

Output Format

Output the value of the second largest number.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
L = map(int, input().split())

print (max([i for i in L if i != max(L)]))
