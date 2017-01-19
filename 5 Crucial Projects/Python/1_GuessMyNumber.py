'''
5 Crucial Projects for Beginners - https://www.daniweb.com/programming/software-development/threads/131973/5-crucial-projects-for-beginners

1 - Guess My Number:

Overview:

The computer randomly generates a number. The user inputs a number, 
and the computer will tell you if you are too high, or too low. 
Then you will get to keep guessing until you guess the number.
What you will be Using:
Random, Integers, Input/Output, Print, While (Loop), If/Elif/Else
My Thoughts on Project:
If you are new to Python this is a great learning experience, 
remember the code you used here and how you used it. 
This will help your natural learning curve into Python.
'''

import random

print('Hello, I am thinking of a number between 0 and 100. '
    'You should try to guess it...')
computer_number = random.randint(0, 100)
user_guess = input('Please enter your first guess: ')

def number_checker(computer_number, user_guess):
  try:
    user_guess = int(input('Please guess again: '))
    if user_guess == computer_number:
      print('Well done, you are correct!')
    elif user_guess > computer_number:
      print('My number is lower...')
      number_checker(computer_number, user_guess)
    elif user_guess < computer_number:
      print('My number is higher...')
      number_checker(computer_number, user_guess)
  except:
    print('Oops, it doesn\'t look like you entered a number...')

def main(computer_number, user_guess):
  number_checker(computer_number, user_guess)

if __name__ == '__main__':
  main(computer_number, user_guess)
