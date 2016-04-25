"""

February 2016

Hackerrank - Python - Data Types - Find the Second Largest Number

Let's delve into one of the most basic data types in Python, the list. You are given NN numbers. Store them in a list and find the second largest number.

NOTE: Do not use the insertion sort method.

Input Format

The first line contains NN. The second line contains an array AA[] of NN integers each separated by a space.

Output Format

Output the value of the second largest number.



"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(raw_input())
L = map(int, raw_input().split())

print max([i for i in L if i != max(L)])



        
        



        

        
        
        
        
        
        
        
        
        
        
    



