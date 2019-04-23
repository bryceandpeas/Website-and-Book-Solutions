'''

Question: 36

2.10

Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

'''

def gen_dict(input_number + 1):
	number_dict = {}
	for i in range(input_number):
		number_dict[i] = input_number ** 2

	return(number_dict)

'''
This is the same question as 35, this list really needs clearing up.
'''