"""

February 2016

Hackerrank - Python - Strings - Find a String

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

1≤len(string)≤2001≤len(string)≤200
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

S = raw_input()
s = raw_input()

count = 0

for i in range(0, len(S)):
    if S[i:i+len(s)] == s:
        count += 1

print count
