'''

Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.	

'''

def factorial(input_number):
	factorial = 1
	for i in range(1, input_number + 1):
		factorial = factorial * i
	return(factorial)

input_number = int(input("Please input a number to get the factorial of: "))

print(factorial(input_number))