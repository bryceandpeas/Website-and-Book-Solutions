'''

Question: 65

Question:

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.


'''

input_num = int(input("Please enter the number you wish to calculate from (any number > 0): ")) 

def calc_num(input_num):

	if input_num == 0:
		return 1
	else:
		return calc_num(input_num - 1) + 100

print(calc_num(input_num) - 1)