'''

Codewars Kata - 8 Kyu - validate code with simple regex

Description:

Basic regex tasks. Write a function that takes in a numeric code of any lenght. 
The function will check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

You can assume the input will always be a nuber.

'''

import re

def validate_code(code):
    return True if re.match('^(1|2|3)', str(code), flags=0) != None else False