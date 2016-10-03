'''

Codewars Kata - 8 Kyu - Convert boolean values to strings 'Yes' or 'No'.

Description:

Complete the bool_to_word (Javascript: boolToWord ) method.

Given: a boolean value

Return: a 'Yes' string for true and a 'No' string for false

'''

def bool_to_word(bool):
    return('{string}'.format(string = 'Yes' if bool == True else 'No'))