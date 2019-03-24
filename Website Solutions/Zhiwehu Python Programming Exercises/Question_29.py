'''

Question: 29

2.10

Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

'''

def add_int(x, y):
	x, y = int(x), int(y)
	return(x + y)

print(add_int(x, y))

