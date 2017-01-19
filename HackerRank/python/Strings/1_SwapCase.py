"""

February 2016

Hackerrank - Python - Strings - sWAP cASE

You are given a string SS. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string SS.

Constraints

0<len(S)≤10000<len(S)≤1000
Output Format

Print the modified string SS.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

STDIN = raw_input()

o = STDIN.swapcase()
   
print o
