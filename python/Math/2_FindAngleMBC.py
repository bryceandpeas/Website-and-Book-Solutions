'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Math: https://www.hackerrank.com/domains/python/py-math

Hackerrank - Python - Math - Find Angle MBC

ABCABC is a right triangle, 90°90° at BB.
Therefore, ∡ABC=90°∡ABC=90°.

Point MM is the midpoint of hypotenuse ACAC.

You are given the lengths ABAB and BCBC. 
Your task is to find ∡MBC∡MBC (angle θ°θ°, as shown in the figure) in degrees.

Input Format

The first line contains the length of side ABAB.
The second line contains the length of side BCBC.

Constraints

0<AB≤1000<AB≤100
0<BC≤1000<BC≤100
Lengths ABAB and BCBC are natural numbers.

Output Format

Output ∡MBC∡MBC in degrees. 

Note: Round the angle to the nearest integer. 

NOTE: Python 3 is disabled for this challenge.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = input()
BC = input()

h = (math.sqrt((AB**2) + (BC**2)))
h = (h / 2.0)
a = (BC / 2.0)

print (str(int(round(math.degrees(math.acos(a/h))))) + '°')

