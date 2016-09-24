'''	

Karan 100 Projects - Text - Check if Palindrome

Checks if the string entered by the user is a palindrome. 
That is that it reads the same forwards as backwards like “racecar”.

'''

user_string = input('Please enter a string to check if it is a palindrome: ')

if user_string == user_string[::-1]:
	print('Your string is a palindrome!')
else:
	print('Your string is not a palindrome...')

