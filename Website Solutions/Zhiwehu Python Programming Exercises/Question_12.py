'''

Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def check_even(lowest, highest):
	even_numbers = []
	truth_check = False

	for i in range(lowest, highest):
		for j in str(i):
			if int(j) % 2 == 0:
				truth_check = True
			else:
				truth_check = False

		if truth_check == True:
			even_numbers.append(i)
		else:
			continue 

	return even_numbers

lowest, highest = map(int, input("Please unput your number range in the format \"lowest, highest\": ").split(','))

print(check_even(lowest, highest))