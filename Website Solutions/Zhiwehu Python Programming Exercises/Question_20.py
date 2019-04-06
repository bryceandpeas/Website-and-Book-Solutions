'''

Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

'''

class NumberIterater(object):
	"""docstring for NumberIterater"""
	def __init__(self):
		super(NumberIterater, self).__init__()

	def iterate_nums(range):
		for i in range(range):
			if i % 7 == 0:
				yield i


ni = NumberIterater()

print(NumberIterater.iterate_nums(100))