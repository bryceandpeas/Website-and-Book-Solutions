'''

Question: 57

Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

'''

class Q57Error(Exception):
	"""docstring for Q57Error"""
	def __init__(self, message):
		super().__init__(message)
		

raise Q57Error("This is a custom error")
