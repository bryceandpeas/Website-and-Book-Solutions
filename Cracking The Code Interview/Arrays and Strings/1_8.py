'''

Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s i and s2, write code to check if s2 is a rotation of si using only 
one call to isSubstring (e.g.,"waterbottle"is a rota- tion of"erbottlewat").

'''

from itertools import permutations

def is_substring(string_one, string_two):
	if tuple(string_two) in permutations(string_one, len(string_one)):
		return True
	else:
		return False

