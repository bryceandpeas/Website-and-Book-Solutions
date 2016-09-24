'''	

Karan 100 Projects - Text - Count Words In A String

Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a summary.

'''

import sys

# Check user input
try:
	input_file = sys.argv[1]
except:
	print ('Input Error: Your first argument should be a \'.txt\' file, please try again.' + '\n')
	exit()

def count_words(input_file):
	#Init word count
	word_count = 0	

	# Open user file
	with open(input_file, 'r') as user_txt_file:
		# Get each line
		for line in user_txt_file:
			for character in line:
				if character == ' ':
					word_count += 1

	print('There are ' + str(word_count) + ' words in your file.')


def main(input_file):
	count_words(input_file)

if __name__ == '__main__':
	main(input_file)