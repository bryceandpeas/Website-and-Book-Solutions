"""

February 2016

Hackerrank - Python - Introduction - Mod Divmod

One of the built-in functions of Python is divmod, which takes two arguments aa and bb and returns a tuple containing the quotient of a/ba/b first and then the remainder aa.

For example:

>>> print divmod(177,10)
(17, 7)
Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

Task
Read in two integers, aa and bb, and print three lines.
The first line is the integer division a//ba//b (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%ba%b.
The third line prints the divmod of aa and bb.

Input Format
The first line contains the first integer, aa, and the second line contains the second integer, bb.

Output Format
Print the result as described above.


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


from __future__ import division

STDFIR = int(raw_input())
STDSEC = int(raw_input())

print STDFIR //STDSEC
print STDFIR % STDSEC
print divmod(STDFIR,STDSEC)













