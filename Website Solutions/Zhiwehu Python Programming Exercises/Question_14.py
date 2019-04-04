'''

Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case uppercase and lower case uppercase.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def case_counter(input_string):
	uppercase = 0
	lowercase = 0
	for i in input_string:
		if i.islower():
			lowercase += 1
		elif i.isupper():
			uppercase += 1
		else:
			continue

	return uppercase, lowercase


input_string = input("Please enter the string you would like to count the number of uppercase and lowercase uppercase in: ")

uppercase, lowercase = case_counter(input_string)

print("UPPER CASE {0}".format(uppercase))
print("LOWER CASE {0}".format(lowercase))