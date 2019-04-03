'''

Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
import math

def calc_val(d_input, c=50, h=30):
	calculated_values = []
	for d in d_input:
		calculated_values.append(int(math.sqrt((2 * c * int(d)) / h)))
	return calculated_values

d_input = input("Please enter your values as a comma seperated sequence: ").split(',')
calculated_values = str(calc_val(d_input, c=50, h=30))
print(calculated_values)