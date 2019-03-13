'''
Given two strings, write a method to decide if one is a permutation of the other.
'''

from itertools import permutations

def check_permutations(string_one, string_two):
	for i in permutations(string_one, len(string_one)):
		if i == tuple(string_two):
			yield True
		else:
			yield False


