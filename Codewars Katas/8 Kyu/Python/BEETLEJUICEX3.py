'''

Codewars Kata - 8 Kyu - BEETLEJUICE X3 "ENTERTRAINMENT" // BUG FIX

Description:

Everyone knows if you say Beetle Juice three times he appears!



Well Lydia wants to invite some new ghosts into her home but has a cold that is making her throat too sore to speak and is on some crazy cold medicine that's making her brain fuzzy!

She wrote a program that takes the input of the ghost she wants to appear and says it three times for her in the form of a string! But she needs you to fix it while she recovers from her cold!

EXAMPLE : beetleJuice("Harry!") => "Harry!  Harry!  Harry!"

Note: each name in the example needs to be separated by exactly TWO spaces.
(there will be no wild inputs just names followed by exclamation points in string form)

ALSO CHECK OUT MY RAMMSTEIN KATA WHICH IS STILL IN BETA!! I CAN'T WAIT FOR IT TO BE APPROVED!

'''

def beetle_juice(name):
   return(((''.join(name) + '  ') * 3).rstrip('  '))

