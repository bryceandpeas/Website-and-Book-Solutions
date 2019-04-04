'''

Question: 46

3.4

Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.

'''

def square(n):
	return(n ** 2)

nums = [1,2,3,4,5,6,7,8,9,10]

print(list(map(square, nums)))

