'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Errors and Exceptions: https://www.hackerrank.com/domains/python/errors-exceptions

Hackerrank - Python - Incorrect Regex

You are given a string SS.
Your task is to find out whether SS is a valid regex or not.

Input Format

The first line contains integer TT, the number of test cases.
The next TT lines contains the string SS.

Constraints

0<T<1000<T<100
Output Format

Print "True" or "False" for each test case without quotes.

contact: bryce@brycefury.com

'''

import re

T = int(input())

for i in range(T):

    try:
        x=re.compile(input().strip())
        if x:
            print (True)

    except:
        print (False)


