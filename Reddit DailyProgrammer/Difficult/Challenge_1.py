'''

Reddit Daily Programmer - /r/dailyprogrammer

[Difficult] - Challenge #1

we all know the classic "guessing game" with higher or lower prompts. 
lets do a role reversal; you create a program that will guess numbers between 1-100, 
and respond appropriately based on whether users say that the number is too high or too low. 
Try to make a program that can guess your number based on user input and great code!

'''

import random

computer_guess_lower = 0
computer_guess_higher = 101

computer_guess = random.randint(computer_guess_lower, computer_guess_higher)
print ('Welcome to the number guessing game!' + '\n'
	 + 'The computer will try to guess your number based on your input' + '\n'
	 + 'After every computer guess, please enter \'Lower\', \'Higher\' or \'Correct\' based on the computer\'s guess'
	 + 'The computer\'s first guess is: {0}'.format(computer_guess))

users_input = input('Please tell me if my guess is \'Lower\', \'Higher\' or \'Correct\': ')

def computer_guesser(users_input, computer_guess, computer_guess_lower, computer_guess_higher):

	if users_input.lower() == 'lower':

		computer_guess_higher = computer_guess
		computer_guess = random.randint(computer_guess_lower, computer_guess_higher)

		print('My new guess is: {0}'.format(computer_guess))
		users_input = input('Please tell me if my guess is \'Lower\', \'Higher\' or \'Correct\': ')

		computer_guesser(users_input, computer_guess, computer_guess_lower, computer_guess_higher)

	elif users_input.lower() == 'higher':

		computer_guess_lower = computer_guess
		computer_guess = random.randint(computer_guess_lower, computer_guess_higher)

		print('My new guess is: {0}'.format(computer_guess))
		users_input = input('Please tell me if my guess is \'Lower\', \'Higher\' or \'Correct\': ')

		computer_guesser(users_input, computer_guess, computer_guess_lower, computer_guess_higher)

	elif users_input.lower() == 'correct':
		computer_guess == True
		print('Hurray! I guessed correctly!')
		
	
	return (computer_guess, computer_guess_lower, computer_guess_higher)

if computer_guess != True:
	computer_guesser(users_input, computer_guess, computer_guess_lower, computer_guess_higher)
