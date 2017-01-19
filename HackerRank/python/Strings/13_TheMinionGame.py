"""

February 2016

Hackerrank - Python - Strings - The Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, SS.
Both players have to make substrings using the letters of the string SS.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string SS.

For Example:
String SS = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string SS.
Note: The string SS will contain only uppercase letters: [A−Z][A−Z].

Constraints

0<len(S)≤1060<len(S)≤106

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

"""


word = input()
stuartScore = 0
kevinScore = 0
o = 0

vowels = 'AEIOU'

for i in range(len(word)):
    if word[i] in vowels:

        kevinScore += (len(word) - i)

for i in range(len(word)):
    if word[i] not in vowels:

        stuartScore += (len(word) - i)


if stuartScore > kevinScore:
    print ('Stuart ' + str(stuartScore))
elif kevinScore > stuartScore:
    print ('Kevin ' + str(kevinScore))
else:
    print ('Draw')









