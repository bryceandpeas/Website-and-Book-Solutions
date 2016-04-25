"""

Monday 25th April 2016

Hackerrank - XML - XML2 - Find the Maximum Depth

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 00.

Input Format

The first line contains NN, the number of lines in the XML document. 
The next NN lines follow containing the XML document.

Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.

"""

import xml.etree.ElementTree as etree

def ans(r):
    return (max([0] + [ans(child) + 1 for child in r]))
    
N = int(input())

c = ''
    
for i in range(N):
    c += str(input())

tree = etree.ElementTree(etree.fromstring(c))
r = tree.getroot()

print (ans(r))






