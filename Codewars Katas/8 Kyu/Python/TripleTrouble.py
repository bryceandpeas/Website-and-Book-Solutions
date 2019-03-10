'''

Codewars Kata - 8 Kyu - Triple Trouble

Description:

#Triple Trouble

Create a function that will return a string that combines all of the letters of
the three inputed strings in groups. Taking the first letter of all of the inputs
and grouping them next to each other. Do this for every letter, see example below!

Ex) Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.

'''

def triple_trouble(one, two, three):
    return ''.join(i + j + k for i, j, k in zip(*(s + s[-1]*(max(len(one),len(two))-len(s)) for s in (one, two, three))))
