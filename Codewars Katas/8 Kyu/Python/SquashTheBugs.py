'''

Codewars Kata - 8 Kyu - Squash the bugs

Description:

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.

'''

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i =  0
    for i in spl:
        if len(i) > longest:
            longest = len(i)
    return longest
