'''

Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

'''

def gen_list_tuple(input_number):
	gen_list = str(input_number).split(',')
	gen_tuple = tuple(str(input_number).split(','))
	return(gen_list, gen_tuple)

input_number = input("Please input a number to generate the list and tuple from: ")

gen_list, gen_tuple = gen_list_tuple(input_number)
print(gen_list)
print(gen_tuple)