'''

Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

'''

class GetPrint(object):
	"""docstring for GetPrint"""
	def __init__(self):
		super(GetPrint, self).__init__()
		
	def get_string_func(self):
		get_string = input("Please enter your string: ")
		return (get_string)

	def print_string_func(self, get_string):
		print_string = get_string.upper()
		return (print_string)

p = GetPrint()

print(p.print_string_func(p.get_string_func()))	