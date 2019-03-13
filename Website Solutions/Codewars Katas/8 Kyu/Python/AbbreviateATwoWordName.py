'''

Codewars Kata - 8 Kyu - Abbreviate a Two Word Name

Description:

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F

'''

def abbrevName(name):
  return('{0}.{1}'.format(name.split(' ')[0][0], name.split(' ')[1][0]).upper())