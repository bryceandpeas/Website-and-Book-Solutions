'''

Question: 33

2.10

Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

'''

def print_dict(input_dict):
	for key, value in input_dict:
		print(str(key) + str(value ** 2))