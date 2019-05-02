'''

Question: 32

2.10

Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

'''

def odd_even(number):
	return("It is an even number" if number % 2 == 0 else "It is an odd number")