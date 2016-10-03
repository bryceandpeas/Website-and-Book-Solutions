'''

Codewars Kata - 8 Kyu - Parse float

Description:

Write function parseFloat which takes a string and returns a number or Nothing (for Python None) if conversion is not possible.

'''

def parse_float(string):
    try:
        return float(string)
    except:
        return None