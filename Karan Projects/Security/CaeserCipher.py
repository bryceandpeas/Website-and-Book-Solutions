'''

Karan 100 Projects - Security - Caesar Cipher

Implement a Caesar cipher, both encoding and decoding.
The key is an integer from 1 to 25.
This cipher rotates the letters of the alphabet (A to Z).

The encoding replaces each letter with the 1st to 25th
next letter in the alphabet (wrapping Z to A).

So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".

This simple "monoalphabetic substitution cipher" provides almost no security,
because an attacker who has the encoded message can either use frequency
analysis to guess the key, or just try all 25 keys.

'''

import sys

''' Argparser is probably better for handling arguments, usage etc. in the real world. '''

# Great user, print usage
print('\n' + 'This script requires three arguments: ' + '\n' + '\n',
	  '1: Your input file (\'.txt\')' + '\n',
	  '2: Your choice of \'endcode\' or \'decode\'' + '\n',
	  '3: Your choice of cipher key (between 1 and 25)' + '\n')

# Check user input
try:
	input_file = sys.argv[1]
except:
	print ('Input Error: Your first argument should be a \'.txt\' file, please try again.' + '\n')
	exit()

try:
	encode_decode = sys.argv[2]
except:
	print ('Input Error: Your second argument should be \'encode\' or \'decode\', please try again.' + '\n')
	exit()

try:
	cipher_key = sys.argv[3]
except:
	print ('Input Error: Your third argument should be a key number between 1 and 25, please try again.' + '\n')
	exit()

# Process user input
def process_input(input_file, encode_decode, cipher_key):

	# Check user cipher key is an integer
	try:
		cipher_key = int(cipher_key)
	except:
		print('Input Error: Your cipher key is not an integer, please try again.')

	# Check user cipher key is within the correct range
	if cipher_key >= 1 and cipher_key <= 25:
		cipher_key = cipher_key
	else:
		print ('Input Error: Your cipher key should be a key number between 1 and 25, please try again.' + '\n')
		exit()

	# Check user input file is .txt
	if input_file.endswith('.txt'):
		input_file = input_file
	else:
		print ('Input Error: Your input file should be a \'.txt\' file, please try again.' + '\n')
		exit()

	# Check user choice, call indicated function

	encode_decode = encode_decode.lower()

	if encode_decode == 'encode':
		encode(input_file, cipher_key)
	elif encode_decode == 'decode':
		decode(input_file, cipher_key)
	else:
		print('Input Error: You need to enter either \'encode\' or \'decode\'')
		exit()

# Encode user file
def encode(input_file, cipher_key):
	#Empty output list
	output_string = []

	# Set user output filename
	output_file = (str(input_file.split('.')[0] + '_encoded.txt'))

	# Prompt user
	print ('You have selected to encode your file with a key of ' + str(cipher_key) + '...' + '\n')

	# Open user file
	with open(input_file, 'r') as user_txt_file:
		# Get each line
		for line in user_txt_file:
			# Get each letter
			for letter in line:
				# Convert each letter to a number and shift by cipher key
				# Convert this number back to letter
				letter_number = ord(letter)
				new_letter_number = letter_number + cipher_key

				# Ensure only letters are used for letters, not symbols (no ords over 26)
				if letter.isupper():
					if new_letter_number > ord('Z'):
						new_letter_number -= 26
					elif new_letter_number < ord('A'):
						new_letter_number += 26
				elif letter.islower():
					if new_letter_number > ord('z'):
						new_letter_number -= 26
					elif new_letter_number < ord('a'):
						new_letter_number += 26

				new_letter_character = chr(new_letter_number)

				output_string.append(new_letter_character)

	user_txt_file.close()

	# Write output file
	with open(output_file, 'w') as user_ouput_file:
		for letter in output_string:
			user_ouput_file.write(letter)

	user_ouput_file.close()

	print('\n' + 'Your encoded file is: ' + output_file + '\n')

# Decode user file
def decode(input_file, cipher_key):
	#Empty output list
	output_string = []

	# Set user output filename
	output_file = (str(input_file.split('.')[0] + '_decoded.txt'))

	# Prompt user
	print ('You have selected to decode your file with a key of ' + str(cipher_key) + '...')

	# Open user file
	with open(input_file, 'r') as user_txt_file:
		# Get each line
		for line in user_txt_file:
			# Get each letter
			for letter in line:
				# Convert each letter to a number and shift by cipher key
				# Convert this number back to letter
				letter_number = ord(letter)
				new_letter_number = letter_number - cipher_key

				# Ensure only letters are used for letters, not symbols (no ords over 26)
				if letter.isupper():
					if new_letter_number > ord('Z'):
						new_letter_number -= 26
					elif new_letter_number < ord('A'):
						new_letter_number += 26
				elif letter.islower():
					if new_letter_number > ord('z'):
						new_letter_number -= 26
					elif new_letter_number < ord('a'):
						new_letter_number += 26

				new_letter_character = chr(new_letter_number)

				output_string.append(new_letter_character)

	user_txt_file.close()

	# Write output file
	with open(output_file, 'w') as user_ouput_file:
		for letter in output_string:
			user_ouput_file.write(letter)

	user_ouput_file.close()

	print('\n' + 'Your decoded file is: ' + output_file + '\n')

def main(input_file, encode_decode, cipher_key):
	process_input(input_file, encode_decode, cipher_key)

if __name__ == '__main__':
	main(input_file, encode_decode, cipher_key)
