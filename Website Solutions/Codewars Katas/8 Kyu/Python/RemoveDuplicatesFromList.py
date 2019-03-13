'''

Codewars Kata - 8 Kyu - Remove duplicates from list

Description:

Write function distinct that removes duplicate from list of numbers.

The order of the sequence needs to stay the same.

'''

def distinct(seq):
    return(sorted(set(seq), key=lambda i: seq.index(i)))
