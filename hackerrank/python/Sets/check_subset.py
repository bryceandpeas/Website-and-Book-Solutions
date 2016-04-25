"""

February 2016

Hackerrank - Python - Sets - Check Subset

You are given two sets, AA and BB. 
Your job is to find whether set AA is a subset of set BB.

If set AA is subset of set BB, print True.
If set AA is not a subset of set BB, print False.

Input Format

The first line will contain the number of test cases, TT. 
The first line of each test case contains the number of elements in set AA.
The second line of each test case contains the space separated elements of set AA.
The third line of each test case contains the number of elements in set BB.
The fourth line of each test case contains the space separated elements of set BB.

Constraints

0<T<210<T<21 
0<Number of elements in each set<10010<Number of elements in each set<1001
Output Format

Output True or False for each test case on separate lines.


"""

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print (True if A < B else False)



