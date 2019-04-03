'''

Question: 64

Question:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float


'''

input_num = int(input("Please enter the number you wish to calculate from: "))

def calc_num(input_num):
	output_num = 0

	for i in range(1, input_num + 1):
		output_num += i / (i + 1)

	return output_num

print(round(calc_num(input_num), 2))