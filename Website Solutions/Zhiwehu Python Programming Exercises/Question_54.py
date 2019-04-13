'''

Question: 54

7.2

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

'''

class Shape(object):
	"""docstring for Shape"""
	def __init__(self):
		return None

class Square(Shape):
	"""docstring for Square"""
	def __init__(self, length):
		super(Shape, self).__init__()
		self.length = 0

	def calc_area(self, length):
		return (length * length)
		

s = Square(5)

print(s.calc_area(5))

