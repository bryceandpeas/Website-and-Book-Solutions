'''

Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def string_counter(input_string):
	letters = 0
	digits = 0
	for i in input_string:
		if i.isdigit():
			digits += 1
		elif i.isalpha():
			letters += 1
		else:
			continue

	return letters, digits


input_string = input("Please enter the string you would like to count the number of letters and digits in: ")

letters, digits = string_counter(input_string)

print("LETTERS {0}".format(letters))
print("DIGITS {0}".format(digits))