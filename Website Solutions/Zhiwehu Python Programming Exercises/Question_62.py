'''

Question: 62

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

'''

string = "This is a string"

string.encode(encoding='UTF-8', errors='strict')
