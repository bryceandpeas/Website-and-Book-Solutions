'''

Question: 53

7.2

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

'''

class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calc_area(self, length, width):
		return (length * width)


r = Rectangle(5, 2)

print(r.calc_area(5, 2))
