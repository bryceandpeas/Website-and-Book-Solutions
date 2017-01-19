'''	

Karan 100 Projects - Text - Pig Latin

Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant 
sound is transposed to the end of the word and an ay is affixed 
(Ex.: 'banana' would yield anana-bay). 

Read Wikipedia for more information on rules.

'''


user_string = input('Please enter a string to turn into pig latin: ')

vowel_list = ['a', 'e', 'i', 'o', 'u']

user_string_first_letter = user_string[:1]
user_string_everything_else = user_string[1:]

if user_string_first_letter in vowel_list:
    print('%syay' % user_string)
else:
    print('%s%say' % (user_string_everything_else, user_string_first_letter))
