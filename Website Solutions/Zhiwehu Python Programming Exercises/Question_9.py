'''

Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def capitalize_lines(input_lines):
	lines = input_lines.split(',')
	capitalized_lines = [i.upper() for i in lines]
	return capitalized_lines

input_lines = input("Please enter the lines you wish to capitalize, each line seperated by a comma: ")

print(*(i + '\n' for i in capitalize_lines(input_lines)))