'''

Codewars Kata - 8 Kyu - Get number from string

Description:

Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:

javascript

getNumberFromString(s)

ruby

get_number_from_string(s)

CSharp

GetNumberFromString(string s)

'''

def get_number_from_string(string):
    return(int(''.join([''.join(i) for i in string if i.isdigit()])))

