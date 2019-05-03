'''

Question: 34

2.10

Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.

'''

def print_dict(input_dict):
	for key, value in input_dict:
		print(str(key) + str(value ** 2))


'''
This is the same question as 33, I think the intention is to also build the dictionary, I don't think I need to practice that.
'''