'''

Codewars Kata - 8 Kyu - Fake Binary

Description:

Given a string of numbers, you should replace any number below 5 with '0' and any number 5 and above with '1'. Return the resulting string.

'''

def fake_bin(x):
    return(str([0 if int(i) < 5 else 1 for i in x]).strip('[]').replace(', ', ''))