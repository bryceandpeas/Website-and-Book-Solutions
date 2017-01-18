'''

Codewars Kata - 5 Kyu - Rot13

Description:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.

'''


import string
from codecs import encode as _dont_use_this_

specials = string.punctuation + ' '


def rot13(message):
    output_string = []

    for letter in message:
    
        letter_number = ord(letter)
        new_letter_number = letter_number + 13

        if letter in specials or letter.isdigit():
            output_string.append(letter)
        else:
            if letter.isupper():
                if new_letter_number > ord('Z'):
                    new_letter_number -= 26
                elif new_letter_number < ord('A'):
                    new_letter_number += 26
                    
            elif letter.islower():
                if new_letter_number > ord('z'):
                    new_letter_number -= 26
                elif new_letter_number < ord('a'):
                    new_letter_number += 26
            
            new_letter_character = chr(new_letter_number)
            output_string.append(new_letter_character)
        
    return (''.join(output_string))