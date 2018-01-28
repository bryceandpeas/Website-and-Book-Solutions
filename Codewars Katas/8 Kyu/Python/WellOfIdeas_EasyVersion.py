'''

Codewars Kata - 8 Kyu - Well of Ideas - Easy Version

Description:

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

'''

def well(x):
    g = 0
    for i in x:
        if i == 'good':
            g += 1
            
    if g > 2:
        return ('I smell a series!')
    elif g >= 1:
        return ('Publish!')
    else:
        return ('Fail!')