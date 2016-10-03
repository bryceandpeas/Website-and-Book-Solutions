"""

February 2016

Hackerrank - Python - Introduction - Integers Come in All Sizes

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 231−1231−1 (c++ int) or 263−1263−1 (C++ long long int).

As we know, the result of abab grows really fast with increasing bb.

Let's do some calculations on very large integers.

Task 
Read four numbers, aa, bb, cc, and dd, and print the result of ab+cdab+cd.

Input Format 
Integers aa, bb, cc, and dd are given on four separate lines, respectively.


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

STDA = int(raw_input())
STDB = int(raw_input())
STDC = int(raw_input())
STDD = int(raw_input())

print (pow(STDA, STDB) + pow(STDC, STDD))



