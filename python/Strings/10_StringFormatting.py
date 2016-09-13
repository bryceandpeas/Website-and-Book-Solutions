'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Introduction: https://www.hackerrank.com/domains/python/py-strings

Hackerrank - Python - Strings - String Formatting

Task

Read the integer, NN and print the decimal, octal, hexadecimal, and binary values from 11 to NN with space padding so that all fields take the same width as the binary value.

Input Format 
The first line contains an integer, NN.

Constraints
1≤N≤991≤N≤99
Output Format 
Print NN lines. Format the fields as the width of the binary value of NN.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

STDIN = int(input())
w = len(str(bin(STDIN)).replace('0b',''))

for i in range(1, STDIN+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0','', 1).rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print (j, o, h, b)

