'''

Question: 47

3.5

Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

'''

def evens(n):
	if n % 2 == 0:
		return n  

def square(n):
	return(n ** 2)

nums = [1,2,3,4,5,6,7,8,9,10]

print(*(x for x in list(map(evens, list(map(square, nums)))) if x is not None))
