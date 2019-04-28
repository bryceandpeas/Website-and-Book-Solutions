'''

Question: 31

2.10


Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string

'''

def max_len(x, y):
	len_x = len(x)
	len_y = len(y)

	if len_x > len_y:
		return(x)
	elif len_y > len_x:
		return(y)
	elif len_x == len_y:
		return(x + '\n' + y)
	else:
		return "Error"