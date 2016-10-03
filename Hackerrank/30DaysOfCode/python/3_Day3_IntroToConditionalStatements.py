'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/tutorials/30-days-of-code

Hackerrank - 30 Days Of Code - Day 3: Intro to Conditional Statements

Objective 
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an integer, nn, perform the following conditional actions:

If nn is odd, print 𝚆𝚎𝚒𝚛𝚍Weird.
If nn is even and in the inclusive range of 22 to 55, print 𝙽𝚘𝚝 𝚆𝚎𝚒𝚛𝚍Not Weird.
If nn is even and in the inclusive range of 66 to 2020, print 𝚆𝚎𝚒𝚛𝚍Weird.
If nn is even and greater than 2020, print 𝙽𝚘𝚝 𝚆𝚎𝚒𝚛𝚍Not Weird.
Complete the stub code provided in your editor to print whether or not nn is weird.

Input Format

A single line containing a positive integer, nn.

Constraints

1≤n≤1001≤n≤100
Output Format

Print 𝚆𝚎𝚒𝚛𝚍Weird if the number is weird; otherwise, print 𝙽𝚘𝚝 𝚆𝚎𝚒𝚛𝚍Not Weird.

contact: bryce@brycefury.com

'''

#!/bin/python3

import sys


N = int(input().strip())

if N % 2 != 0:
    print ('Weird')
elif N % 2 == 0 and (N > 2 and N < 5+1):
    print('Not Weird')
elif N % 2 == 0 and (N > 6 and N < 20+1):
    print ('Weird')
elif N % 2 == 0 and N > 20:
    print ('Not Weird')
else:
    print ('Error')
    

