'''

Codewars Kata - 8 Kyu - simple validation of a username with regex

Description:

Write a simple regex to validate a username.

Allowed characters are:

-lowercase letters -numbers -underscore

length shoould be between 4 and 16 characters.

'''

import re

def validate_usr(username):
    if not re.match(r'[a-z0-9_]{4,16}$', username):
        return False
    else:
        return True