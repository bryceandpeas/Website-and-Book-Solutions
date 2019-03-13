'''

Codewars Kata - 6 Kyu - Highest Scoring Word

Description:

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

import string

def high(x):
    scores = []
    letters = [i for i in string.ascii_lowercase]
    words = x.split(' ')
    current = 0
    for word in words:
        for letter in word:
            current += (letters.index(letter) + 1)
        scores.append(current)
        current = 0
        
    highest =  scores.index(max(scores))

    return words[highest]