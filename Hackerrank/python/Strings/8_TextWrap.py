'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Strings: https://www.hackerrank.com/domains/python/py-strings

Hackerrank - Python - Strings - Text Wrap

Textwrap

The textwrap module provides two convenient functions: wrap() and fill().

textwrap.wrap() 
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
textwrap.fill() 
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
Task

You are given a string SS and width ww. 
Your task is to wrap the string into a paragraph of width ww.

Input Format

The first line contains a string, SS. 
The second line contains the width, ww.

Constraints

0<len(S)<10000<len(S)<1000 
0<w<len(S)0<w<len(S)
Output Format

Print the text wrapped paragraph.

contact: bryce@brycefury.com

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import textwrap

STDIN = input()
WIDTH = int(input())

print (textwrap.fill(STDIN, WIDTH))