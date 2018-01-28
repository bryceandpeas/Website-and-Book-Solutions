'''

Codewars Kata - 8 Kyu - Find the position!

Description:

When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

This kata is meant for beginners. Rank and upvote to bring it out of beta

'''

import string

def position(alphabet):
    position = ([i for i in string.ascii_lowercase].index(alphabet.lower()) + 1)
    return('Position of alphabet: {0}'.format(position))
