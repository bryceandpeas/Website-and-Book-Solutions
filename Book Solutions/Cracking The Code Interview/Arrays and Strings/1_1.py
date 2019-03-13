'''

Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

'''

def check_string(string):
	return True if len(string) == len(set(string)) else False

