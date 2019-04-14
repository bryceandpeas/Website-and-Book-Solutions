'''

Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def val_calc(input_number):
	a = input_number
	calc_val = (a + (a * 11) + (a * 111) + (a * 1111))
	return calc_val

input_number = int(input("Please enter the number you wish to calculate from: "))

print(val_calc(input_number))