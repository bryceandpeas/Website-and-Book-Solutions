'''

Question: 52

7.2

Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

'''

import math

class Circle(object):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius

	def calc_area(self, radius):
		return (math.pi * (radius ** 2))


c = Circle(5)

print(c.calc_area(5))

		